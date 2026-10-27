#!/usr/bin/env python3
# SCRIPT_VERSION=1.0.0
"""校验文档镜像的译文页与英文原页在结构、链接与用词上的一致性。

用法：
  check_i18n.py [--docs DIR] [--locale zh-CN] [--json] [--strict]
                [--banned-file FILE] [--quiet] [--selftest]

  --docs DIR         文档根（含英文页与 <locale>/ 子目录），默认脚本所在仓库的 docs/
  --locale NAME      译文语言目录名，默认 zh-CN
  --json             stdout 只输出 JSON 结果
  --strict           警告也计入失败退出码
  --banned-file FILE 追加禁用词表，每行 `词` 或 `词=替代`
  --allow-file FILE  豁免清单，默认 scripts/i18n-allow.txt（`CODE 文件 # 理由`）
  --quiet            stderr 只报最终汇总
  --selftest         构造临时样本断言各检查项行为，不读仓库文件

退出码：0 无错误（--strict 时含警告）；1 有错误；2 参数或环境问题。
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

SCRIPT_VERSION = "1.0.0"

HAN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`\n]*`")
MD_TARGET = re.compile(r"\]\(([^)\s]+)\)")
HTML_TAG = re.compile(r"<[^>]+>")
TABLE_ROW = re.compile(r"^\s*\|")
TABLE_SEP = re.compile(r"^\s*\|?[\s:|-]+\|[\s:|-]*$")
HEADING = re.compile(r"^(#{1,6}) +(.+?)\s*$")
ANCHOR = re.compile(r'<a id="([^"]+)"></a>')
SOURCE = re.compile(r"<!--\s*source:\s*(\S+)\s*-->")

# 繁体词与被术语表取代的旧译法。前者可直接判定，后者来自术语表定稿，
# 误报时用 --banned-file 覆盖或改这里，不要在译文里逐个眼查。
BANNED_DEFAULT = {
    "設定": "设置", "取得": "获取", "資訊": "信息", "執行": "执行", "釋出": "发布",
    "演算法": "算法", "開啟": "开启", "關閉": "关闭", "登入": "登录", "介面": "界面",
    "檔案": "文件", "程式": "程序", "帳戶": "账户", "點選": "单击", "點擊": "单击",
    "輸出": "输出", "輸入": "输入", "親和性": "相关性", "計算機": "电脑",
    "亲和性": "相关性", "关联性": "相关性", "启动加速": "启动提升", "响应性": "响应能力",
    "响应率": "响应能力", "驻留": "常驻", "驻车": "停放", "停驻": "停放",
    "临界": "关键", "现在购买": "立即购买", "点击": "单击",
}


class Issue:
    __slots__ = ("level", "code", "file", "line", "column", "message")

    def __init__(self, level, code, file, line, column, message):
        self.level = level
        self.code = code
        self.file = file
        self.line = line
        self.column = column
        self.message = message

    def as_dict(self):
        return {
            "level": self.level, "code": self.code, "file": self.file,
            "line": self.line, "column": self.column, "message": self.message,
        }

    def __str__(self):
        loc = self.file if not self.line else f"{self.file}:{self.line}"
        if self.column:
            loc += f":{self.column}"
        return f"{loc}: [{self.code}] {self.message}"


def read(path):
    return path.read_text(encoding="utf-8", errors="replace")


def slugify(text):
    """近似 MkDocs 的标题 id：保留字母数字（含中文），其余折成连字符。"""
    text = HTML_TAG.sub("", text).strip()
    text = text.replace("`", "")
    text = unicodedata.normalize("NFKC", text).lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"[-\s]+", "-", text).strip("-")


def headings(text):
    """返回 [(行号, 标题文本, 隐式 id, 紧邻其上的显式 id 列表)]。"""
    lines = text.split("\n")
    out = []
    for index, line in enumerate(lines):
        m = HEADING.match(line)
        if not m:
            continue
        explicit = []
        back = index - 1
        while back >= 0:
            prev = lines[back].strip()
            if not prev:
                back -= 1
                continue
            a = ANCHOR.fullmatch(prev)
            if a:
                explicit.append(a.group(1))
                back -= 1
                continue
            break
        out.append((index + 1, m.group(2), slugify(m.group(2)), explicit))
    return out


def page_ids(text):
    ids = set(ANCHOR.findall(text))
    for _, title, implicit, explicit in headings(text):
        ids.add(implicit)
        ids.update(explicit)
    return ids


def mask_line(line):
    """把不该参与标点检查的片段替换成等长占位，保住列号。"""
    out = list(line)
    for pattern in (INLINE_CODE, MD_TARGET, HTML_TAG):
        for m in pattern.finditer(line):
            for i in range(m.start(), m.end()):
                out[i] = "\x00"
    return "".join(out)


def is_han(ch):
    return bool(ch) and bool(HAN.match(ch))


def collect_pages(docs, locale):
    en, zh = {}, {}
    for path in sorted(docs.rglob("*.md")):
        if path.is_relative_to(docs / locale):
            zh[path.relative_to(docs / locale).as_posix()] = path
        else:
            en[path.relative_to(docs).as_posix()] = path
    return en, zh


def check(docs, locale, banned, allow):
    en_pages, zh_pages = collect_pages(docs, locale)
    issues = []

    def add(level, code, file, line, column, message):
        if (code, file) in allow or (code, file.split("/", 1)[-1]) in allow:
            return
        issues.append(Issue(level, code, file, line, column, message))

    for missing in sorted(set(en_pages) - set(zh_pages)):
        add("error", "COVERAGE", f"{locale}/{missing}", 0, 0, "缺少译文页")
    for extra in sorted(set(zh_pages) - set(en_pages)):
        add("error", "COVERAGE", f"{locale}/{extra}", 0, 0, "没有对应的英文原页")

    texts = {rel: read(path) for rel, path in zh_pages.items()}
    ids_cache = {}

    def ids_of(rel, base):
        key = (rel, base)
        if key not in ids_cache:
            path = (base / rel) if base else zh_pages.get(rel)
            ids_cache[key] = page_ids(read(path)) if path and path.is_file() else None
        return ids_cache[key]

    for rel, text in texts.items():
        display = f"{locale}/{rel}"
        lines = text.split("\n")

        en_rel = rel if rel in en_pages else None
        if en_rel is None:
            continue
        en_text = read(en_pages[en_rel])

        src_en = SOURCE.search(en_text)
        src_zh = SOURCE.search(text)
        if src_en and not src_zh:
            add("error", "SOURCE", display, 1, 0, f"页首缺少 <!-- source: {src_en.group(1)} -->")
        elif src_en and src_zh and src_en.group(1) != src_zh.group(1):
            add("error", "SOURCE", display, 1, 0,
                f"source 与英文页不一致：{src_zh.group(1)} ≠ {src_en.group(1)}")

        en_heads, zh_heads = headings(en_text), headings(text)
        if len(en_heads) != len(zh_heads):
            add("error", "HEADINGS", display, 0, 0,
                f"标题数不一致：英文 {len(en_heads)} / 译文 {len(zh_heads)}")
        else:
            present = set(ANCHOR.findall(text))
            for (en_line, en_title, en_id, en_extra), (zh_line, zh_title, zh_id, _) in zip(en_heads, zh_heads):
                needed = set(en_extra)
                if en_id != zh_id:
                    needed.add(en_id)
                lost = sorted(needed - present)
                if lost:
                    add("error", "ANCHOR", display, zh_line, 0,
                        "缺少标题锚点 " + ", ".join(f'<a id="{x}">' for x in lost)
                        + f"（英文标题 {en_title!r} 第 {en_line} 行）")
                present.update(needed)

        in_fence = 0
        table_width = None
        for number, line in enumerate(lines, 1):
            if FENCE.match(line):
                in_fence ^= 1
                continue
            if in_fence:
                continue

            if TABLE_ROW.match(line):
                if TABLE_SEP.match(line):
                    continue
                width = len(re.sub(r"\\\|", "", line).split("|")) - 2
                if table_width is None:
                    table_width = width
                elif width != table_width:
                    add("warning", "TABLE", display, number, 0,
                        f"表格该行 {width} 列，表头 {table_width} 列")
            else:
                table_width = None

            masked = mask_line(line)
            for m in re.finditer(r"[,;:?!()]", masked):
                pos = m.start()
                left = masked[pos - 1] if pos else ""
                right = masked[pos + 1] if pos + 1 < len(masked) else ""
                if is_han(left) or is_han(right):
                    add("error", "PUNC", display, number, pos + 1,
                        f"中文语境里的半角标点 {m.group(0)!r}（应为全角）")

            for word, better in banned.items():
                start = line.find(word)
                while start >= 0:
                    add("error", "BANNED", display, number, start + 1, f"禁用词 {word!r}（应为 {better!r}）")
                    start = line.find(word, start + len(word))

            for m in MD_TARGET.finditer(line):
                target = m.group(1)
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    if target.startswith("#"):
                        if target[1:] not in page_ids(text):
                            add("error", "FRAG", display, number, m.start(1) + 1,
                                f"本页没有锚点 #{target[1:]}")
                    continue
                path_part, _, frag = target.partition("#")
                resolved = os.path.normpath(os.path.join(os.path.dirname(rel), path_part))
                if not (zh_pages and (docs / locale / resolved).is_file()):
                    hint = ""
                    if "media/" in path_part:
                        hint = "；media/ 只有一份在 docs/ 下，子目录页需用 ../../media/"
                    add("error", "LINK", display, number, m.start(1) + 1,
                        f"链接目标不存在：{target}{hint}")
                    continue
                if frag:
                    target_ids = ids_of(resolved, docs / locale)
                    if target_ids is not None and frag not in target_ids:
                        add("error", "FRAG", display, number, m.start(1) + 1,
                            f"目标页 {resolved} 没有锚点 #{frag}")

        if in_fence:
            add("error", "FENCE", display, 0, 0, "代码围栏未成对闭合")

    return issues, len(en_pages), len(zh_pages)


def load_allow(path):
    """豁免项只收「上游原文如此」与「结构本就不同」两类，理由必填，便于审计。"""
    allow = set()
    if not path or not Path(path).is_file():
        return allow
    for raw in read(Path(path)).splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            sys.stderr.write(f"豁免行格式应为 CODE FILE # 理由：{raw!r}\n")
            sys.exit(2)
        allow.add((parts[0], parts[1]))
    return allow


def load_banned(extra_file):
    banned = dict(BANNED_DEFAULT)
    if not extra_file:
        return banned
    path = Path(extra_file)
    if not path.is_file():
        sys.stderr.write(f"禁用词文件不存在：{path}\n")
        sys.exit(2)
    for raw in read(path).splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        word, _, better = line.partition("=")
        banned[word.strip()] = (better.strip() or "—")
    return banned


def report(issues, strict, as_json, en_count, zh_count):
    errors = [i for i in issues if i.level == "error"]
    warnings = [i for i in issues if i.level == "warning"]
    if as_json:
        json.dump(
            {
                "script_version": SCRIPT_VERSION,
                "pages": {"en": en_count, "zh": zh_count},
                "errors": [i.as_dict() for i in errors],
                "warnings": [i.as_dict() for i in warnings],
                "summary": {"errors": len(errors), "warnings": len(warnings)},
            },
            sys.stdout, ensure_ascii=False, indent=2,
        )
        sys.stdout.write("\n")
    else:
        for issue in sorted(issues, key=lambda i: (i.file, i.line, i.column, i.code)):
            sys.stdout.write(f"{issue}\n")
        sys.stdout.write(f"\n英文页 {en_count} / 译文页 {zh_count} · 错误 {len(errors)} · 警告 {len(warnings)}\n")
    failed = bool(errors) or (strict and bool(warnings))
    return 1 if failed else 0


def run(docs, locale, banned_file, allow_file, as_json, strict, quiet):
    if not docs.is_dir():
        sys.stderr.write(f"文档目录不存在：{docs}\n")
        return 2
    if not (docs / locale).is_dir():
        sys.stderr.write(f"译文目录不存在：{docs / locale}\n")
        return 2
    if not quiet:
        sys.stderr.write(f"扫描 {docs}（译文 {locale}）…\n")
    issues, en_count, zh_count = check(docs, locale, load_banned(banned_file), load_allow(allow_file))
    code = report(issues, strict, as_json, en_count, zh_count)
    errors = sum(1 for i in issues if i.level == "error")
    warnings = sum(1 for i in issues if i.level == "warning")
    sys.stderr.write(
        f"结果：错误 {errors} · 警告 {warnings} · "
        f"{'通过' if code == 0 else '未通过'}（check_i18n v{SCRIPT_VERSION}）\n"
    )
    return code


FIXTURE_EN = {
    "index.md": "<!-- source: https://example.com/docs/ -->\n\n# Welcome\n\n<a id=\"editing-rules\"></a>\n\n## Editing Rules\n\nSee [CPU](rules/cpu.md#cpu-affinity).\n",
    "rules/cpu.md": "<!-- source: https://example.com/docs/rules/cpu/ -->\n\n# CPU\n\n<a id=\"cpu-affinity\"></a>\n\n## CPU Affinity\n\n![shot](../media/shot.png)\n",
    "rules/extra.md": "# Extra\n",
}

FIXTURE_ZH_OK = {
    "index.md": "<!-- source: https://example.com/docs/ -->\n\n<a id=\"welcome\"></a>\n\n# 欢迎\n\n<a id=\"editing-rules\"></a>\n\n## 编辑规则\n\n参见 [CPU](rules/cpu.md#cpu-affinity)。\n",
    "rules/cpu.md": "<!-- source: https://example.com/docs/rules/cpu/ -->\n\n# CPU\n\n<a id=\"cpu-affinity\"></a>\n\n## CPU 相关性\n\n![截图](../../media/shot.png)\n",
    "rules/extra.md": "<!-- source: https://example.com/docs/rules/extra/ -->\n\n<a id=\"extra\"></a>\n\n# 附加\n",
}

FIXTURE_ZH_BAD = {
    "index.md": "<!-- source: https://example.com/other/ -->\n\n# 欢迎設定, 请看。\n",
    "rules/cpu.md": "# CPU\n\n## CPU 相关性\n\n![截图](../media/shot.png)\n\n```\n未闭合\n",
    "rules/stray.md": "# 多余\n",
}


def selftest():
    root = Path(tempfile.mkdtemp(prefix="check_i18n_selftest_"))
    try:
        docs = root / "docs"
        (docs / "media").mkdir(parents=True)
        (docs / "media" / "shot.png").write_bytes(b"png")
        for rel, text in FIXTURE_EN.items():
            path = docs / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        (docs / "zh-CN").mkdir()

        def invoke(files):
            shutil.rmtree(docs / "zh-CN")
            (docs / "zh-CN").mkdir()
            for rel, text in files.items():
                path = docs / "zh-CN" / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
            proc = subprocess.run(
                [sys.executable, str(Path(__file__).resolve()), "--docs", str(docs),
                 "--locale", "zh-CN", "--json", "--quiet"],
                capture_output=True, text=True,
            )
            return proc, json.loads(proc.stdout or "{}")

        checks = []

        proc, data = invoke(FIXTURE_ZH_OK)
        checks.append(("合规样本零问题", proc.returncode == 0 and not data["errors"] and not data["warnings"],
                       f"rc={proc.returncode} errors={data.get('errors')}"))

        proc, data = invoke(FIXTURE_ZH_BAD)
        codes = {}
        for item in data["errors"] + data["warnings"]:
            codes.setdefault(item["code"], []).append(item)
        checks.append(("检出缺译", "COVERAGE" in codes and proc.returncode == 1, str(codes.keys())))
        checks.append(("检出多余的译文页",
                       any("stray" in i["message"] + i["file"] for i in codes.get("COVERAGE", [])),
                       str(codes.get("COVERAGE"))))
        checks.append(("检出 source 不一致", "SOURCE" in codes, str(codes.get("SOURCE"))))
        checks.append(("检出标题数漂移", "HEADINGS" in codes, str(codes.get("HEADINGS"))))
        checks.append(("检出半角逗号", any(i["column"] for i in codes.get("PUNC", [])), str(codes.get("PUNC"))))
        checks.append(("检出禁用词", "BANNED" in codes, str(codes.get("BANNED"))))
        checks.append(("检出 media 层级错误",
                       any("media/" in i["message"] for i in codes.get("LINK", [])),
                       str(codes.get("LINK"))))
        checks.append(("检出未闭合代码围栏", "FENCE" in codes, str(codes.get("FENCE"))))

        broken = {
            "index.md": "<!-- source: https://example.com/docs/ -->\n\n# 欢迎\n\n<a id=\"editing-rules\"></a>\n\n## 编辑规则\n\n参见 [CPU](rules/cpu.md#missing-anchor)。\n",
            "rules/cpu.md": FIXTURE_ZH_OK["rules/cpu.md"],
            "rules/extra.md": FIXTURE_ZH_OK["rules/extra.md"],
        }
        proc, data = invoke(broken)
        codes = {}
        for item in data["errors"]:
            codes.setdefault(item["code"], []).append(item)
        checks.append(("检出丢失的标题锚点", "ANCHOR" in codes, str(codes.get("ANCHOR"))))
        checks.append(("检出失效的页内锚点", "FRAG" in codes, str(codes.get("FRAG"))))

        proc, data = invoke({**FIXTURE_ZH_OK,
                             "rules/cpu.md": FIXTURE_ZH_OK["rules/cpu.md"] + "\n| a | b |\n| --- | --- |\n| 1 | 2 | 3 |\n"})
        codes = {i["code"] for i in data["warnings"]}
        checks.append(("检出表格列数不一致", "TABLE" in codes, str(codes)))
        checks.append(("警告不改变退出码", proc.returncode == 0, f"rc={proc.returncode}"))

        proc, _ = invoke(FIXTURE_ZH_OK)
        strict = subprocess.run(
            [sys.executable, str(Path(__file__).resolve()), "--docs", str(docs),
             "--locale", "zh-CN", "--strict", "--quiet", "--json"],
            capture_output=True, text=True,
        )
        checks.append(("--strict 在零警告时仍通过", strict.returncode == 0, f"rc={strict.returncode}"))

        failed = [name for name, ok, detail in checks if not ok]
        for name, ok, detail in checks:
            sys.stderr.write(f"  {'ok  ' if ok else 'FAIL'} {name}\n")
            if not ok:
                sys.stderr.write(f"       {detail}\n")
        sys.stdout.write(f"selftest: {len(checks) - len(failed)}/{len(checks)} 通过\n")
        return 0 if not failed else 1
    finally:
        shutil.rmtree(root, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser(description="校验文档镜像的译文一致性")
    parser.add_argument("--docs", default=str(Path(__file__).resolve().parent.parent / "docs"))
    parser.add_argument("--locale", default="zh-CN")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--banned-file")
    parser.add_argument("--allow-file",
                        default=str(Path(__file__).resolve().parent / "i18n-allow.txt"))
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    return run(Path(args.docs).resolve(), args.locale, args.banned_file, args.allow_file,
               args.json, args.strict, args.quiet)


if __name__ == "__main__":
    sys.exit(main())

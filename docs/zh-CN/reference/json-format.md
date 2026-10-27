<!-- source: https://bitsum.com/apps/process-lasso/docs/reference/json-format/ -->

<a id="rules-import-and-export-json"></a>

# 规则导入与导出（JSON）

Process Lasso 可以以 JSON 形式复制、导出与导入进程规则。您可以用它在机器之间迁移规则、分享规则集，或为少数进程备份规则。若要复制或部署整套配置（包括全局选项），请改用 [INI 配置文件](ini-config.md)。

[Process Lasso 的 JSON 架构已在此发布](https://bitsum.com/json-schemas/2026-01-17-00/processlasso.schema.json)。

<a id="exporting-rules"></a>

## 导出规则

- *菜单路径：「文件 / 导出规则」*

选择要导出其规则的进程。Process Lasso 会把规则复制到剪贴板，然后询问是否同时保存为 `.json` 文件。

若要复制单个进程的规则，右键单击它并选择 **复制规则**。这会复制作用于该进程的每一条规则，包括通过通配符或路径匹配到它的规则。

<a id="importing-rules"></a>

## 导入规则

- *菜单路径：「文件 / 导入规则」*

如果剪贴板中存有已导出的规则，Process Lasso 会提示导入它们；否则请选择一个 `.json` 文件。随后由您选择为哪些进程导入规则。

> **导入会替换进程的规则**
>
> 对于每个导入的进程，Process Lasso 会先移除该进程现有的所有规则，再施加导入的规则。未被导入的进程，其规则保持不变。

要把复制的规则应用到列表中的进程，请右键单击某个进程或多个已选进程，选择 **粘贴规则**。保持运行规则不会被粘贴，因为它们属于特定的程序路径。如果剪贴板中存有多个进程的规则，粘贴规则会改为打开完整的导入流程。

**规则**窗口（*「选项 / 查看所有规则」*）有自己的导入与导出命令。在那里导入只会为尚未列出的进程添加规则，并且在您单击 **确定** 之前不会保存任何内容。

<a id="when-rules-were-exported-on-a-different-cpu"></a>

### 当规则是在不同 CPU 上导出时

导出文件会记录生成它的机器的 CPU 型号。如果您的 CPU 型号不同，Process Lasso 会在导入前询问，因为 CPU 相关性与 CPU 集这类规则指向特定核心。导入后请检查这些规则。

<a id="whats-included"></a>

## 包含的内容

导出会包含作用于单个进程的所有规则类型：CPU、I/O、GPU 与内存优先级，GPU 适配器偏好，CPU 相关性与 CPU 集，效率模式，线程优先级提升，应用电源计划，CPU 限制器，启动提升，实例均衡器，实例数量限制，处理器组扩展器，硬性节流，看门狗，保持运行，不允许的进程及其例外项，阻止睡眠，性能模式，以及 ProBalance、智能内存整理、前台提升、空闲节能与性能模式的排除项。对于「首条匹配规则生效」的规则类型，规则的顺序会被保留。

不包含的内容：

- 全局选项，例如 ProBalance 阈值或刷新频率。
- 您已允许 ProBalance 越过内置排除条件去作用的进程。
- Internet Explorer 限制列表。

优先级名称始终以英文写入（18.4.1.7 及之后），因此导出文件可以导入到以任何语言运行的 Process Lasso 中。更早的版本会以界面语言写入名称。

<a id="format"></a>

## 格式

导出内容是一个带有 `ruleSets` 数组的 JSON 对象：每个进程匹配对应一个规则集，只含该进程拥有的规则。下面的示例有两个规则集：

```
{
 "$id": "https://bitsum.com/json-schemas/2026-01-17-00/processlasso.schema.json",
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Process Lasso Rules",
 "description": "Rulesets for Process Lasso",
 "cpuModel": "Intel(R) Core(TM) i5-12600K",
 "ruleSets": [
  {
   "processName": "game.exe",
   "priorityClass": "High",
   "priorityClassEnforcedByRegistry": false,
   "cpuAffinity": "0-7",
   "cpuAffinityDelay": 0,
   "probalanceExclusion": true
  },
  {
   "processName": "backup*.exe",
   "priorityClass": "Below Normal",
   "priorityClassEnforcedByRegistry": false,
   "ioPriority": "Very Low",
   "ioPriorityEnforcedByRegistry": false
  }
 ],
 "priorityClassRuleOrder": [ "game.exe", "backup*.exe" ]
}
```

您也可以手写规则文件：

- 只有当文件包含 `ruleSets` 数组、且 `$schema` 为上面所示的值时，Process Lasso 才会导入它。`$id` 是可选的，但若出现，其值也必须与上面一致。
- 每个规则集都需要 `processName`，它接受完整的[进程匹配](process-matching.md)语法。其他字段都是可选的，包括 `priorityClassEnforcedByRegistry`、`cpuAffinityDelay` 这类配套字段。
- `cpuModel` 是可选的。缺少它时，Process Lasso 会在导入前询问，如同 CPU 型号不同时那样。
- 取值格式与 [INI 文件](ini-config.md)相同，例如 CPU 相关性写作 `0-3;6`。[架构文件](https://bitsum.com/json-schemas/2026-01-17-00/processlasso.schema.json)列出了每个字段及其允许值，您也可以用任何 JSON Schema 校验器检查文件。

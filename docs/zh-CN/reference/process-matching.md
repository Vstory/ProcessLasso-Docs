<!-- source: https://bitsum.com/apps/process-lasso/docs/reference/process-matching/ -->

<a id="processmatch"></a>

<a id="process-matching"></a>

# 进程匹配

「进程匹配」可以是简单的进程名、通配符，甚至是[针对多个进程属性校验的正则表达式](https://rulebuilder.bitsum.com)，例如用户名与命令行。

<a id="traditional"></a>

## 传统匹配

传统进程名匹配使用简单的通配符匹配，`?` 表示任意单个字符，`*` 表示任意字符序列。它不区分大小写。用户名可以用冒号附加在匹配串之后。视功能而定，开启路径或命令行匹配后，这些字段也会与匹配短语比较。

**示例（非正则）：**

```
chrome.exe
 匹配任何名为 chrome.exe 的进程

chrome*
 匹配任何以 'chrome' 开头的进程

chrome.exe:bob
 匹配任何由用户 'bob' 运行的名为 chrome.exe 的进程
```

<a id="htoc-childof"></a>

<a id="child-processes-childof"></a>

## 子进程（childof:）

要匹配某个应用程序启动的所有进程，请给父进程名加上 `childof:` 前缀。所有后代都会匹配，而不只是直接子进程，因此由父进程的某个子进程启动的进程同样匹配。父进程名接受与传统匹配相同的通配符，且不区分大小写。冒号后的空格会被忽略。

**示例：**

```
childof:steam.exe
 匹配任何源自 steam.exe 的进程，例如游戏及其辅助进程

childof: boinc.exe
 匹配任何源自 boinc.exe 的进程

childof:epic*.exe
 匹配任何源自名称以 'epic' 开头的进程的进程
```

父进程本身不匹配 `childof:` 规则；如有需要请为它单独添加规则。进程只有在其父链已知时才会被匹配：如果中间某个父进程在 Process Lasso 见到子进程之前就已退出，或子进程比父进程活得更久而规则被重新评估，该子进程就不再匹配。

`childof:` 受以下功能支持：CPU 优先级、CPU 相关性、CPU 集、I/O 优先级、内存优先级、GPU 优先级、线程优先级提升、效率模式、启动提升、CPU 限制器、实例均衡器、看门狗、处理器组扩展、ProBalance 排除项以及性能模式排除项。

以下功能**不**支持它：不允许的进程、实例数量限制、GPU 适配器偏好，以及通过注册表强制执行的规则（通过注册表强制执行要求使用普通进程名）。

`childof:` 不能与用户名组合使用。若要按用户或其他属性限制子进程匹配，请使用[正则表达式](process-matching.md#htoc-regular-expressions)。正则表达式只能看到直接父进程（ParentName 字段），而 `childof:` 会检查每一个祖先。

<a id="htoc-regular-expressions"></a>

<a id="regular-expressions"></a>

## 正则表达式

Process Lasso 支持针对多个进程属性进行正则表达式匹配。这让创建原本无法实现的复杂规则成为可能。例如，一条规则可以在用户是 Bob 或 Jeremy 时作用于 Chrome.exe 或 Firefox.exe。此前这需要 4 条不同的规则，而使用正则表达式可以合并为一条。

您可以使用我们的 [Process Lasso 规则生成器](https://rulebuilder.bitsum.com)创建这些规则，也可以继续阅读下文学习手动编写。

<a id="what-is-a-regular-expression"></a>

##### 什么是正则表达式？

正则表达式是一种用于模式匹配（与替换）的语言。它已使用数十年，并获得广泛支持。

|  |
| --- |
| 正则表达式是用于描述搜索模式的特殊文本字符串。您可以把正则表达式想象成强化版的通配符。您大概熟悉文件管理器中用 \*.txt 这类通配符表示法查找所有文本文件。与之等价的正则写法是 .\*.txt。 – [RegexBuddy](https://www.regexbuddy.com/regex.html) |

延伸阅读：[快速参考](https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)（Microsoft）[RegEx101 测试器](https://regex101.com/r/t69lfP/1)

<a id="use-of-regex-in-process-lasso"></a>

##### Process Lasso 中正则的用法

匹配正则时，Process Lasso 会把关于该进程的多个字段拼接起来。这条合并后的进程信息字符串格式为：

```
PID,User,ProcessName,Path,ParentPID,ParentName,,,,CommandLine (always last)
```

PID 进程 ID User 进程运行所属的用户 Process 进程基名 Path 进程映像的文件路径 ParentPID 父进程 ID Parent 父进程名 CommandLine 实例命令行（该字段始终位于最后。若将来插入新字段，其索引可能变化！）这样一来，表达式可以匹配拼接串中的任何内容，也可以只匹配特定字段，取决于表达式的精确程度。在 Process Lasso 中，正则表达式与传统匹配短语的区分方式是*用正斜杠包裹*（例如 `/myregex/`）。所有匹配都不区分大小写。字段内嵌的逗号（通常只出现在命令行字段）以反斜杠转义，因此编写精确规则时应考虑这一点。

<a id="examples"></a>

##### 示例

<a id="simple"></a>

###### 简单示例

尽管正则可以对多个模式与字段进行强大匹配，它也可以用于简单的场景：

```
/firefox.exe/
 在任意字段中匹配 'firefox?exe'。注意 '.' 在正则中是通配符，若要更精确可转义为 'firefox\\.exe'。

/,firefox\\.exe/
 只匹配位于字段开头（>0）的 firefox.exe

/,fire[^,]*\\.exe/
 匹配以 'fire' 开头且包含 '.exe' 的字段（>0），例如 firefox.exe

/,(fire|chr)[^,]*\\.exe,/
 匹配以 'fire' 或 'chr' 开头且以 '.exe' 结尾的字段（>0）

/,app[123]\\.exe/
 若任一字段是 app1.exe、app2.exe 或 app3.exe 则匹配（>0）

/,bobsmith/
 匹配位于字段开头（>0）的用户 bobsmith

/10280,/
 匹配 PID 10280。（简化形式，严格来说也可能匹配其他字段）

/,.*-type=renderer[^,]*$/
 在最后一个字段（命令行）中匹配 '-type=renderer'。其后不得有逗号（关于内嵌逗号见下一个示例）。

/,.*-type=renderer([^,\\\\]|\\\\.)*$/
 上一个示例，但处理了命令行中经转义的内嵌逗号（\\,）。
```

<a id="advanced"></a>

###### 进阶示例

要匹配特定字段，可使用类似下面的表达式专门匹配第 3 个字段（进程名）：

```
^([^,]*,){2}
 解释：
 ^ = 从字符串起始处开始
 ([^,]*,) = 非逗号字符重复零次或多次，后跟一个逗号
 {2} = 重复前一项匹配（一个逗号分隔字段）2 次
```

```
/^[^,]*,(jeremy|bob),/
 匹配用户名为 jeremy 或 bob 的进程

/^([^,]*,){2}chrome\\.exe,/
 匹配名为 chrome.exe 的进程

/^([^,]*,){2}[^,]*chr[^,]*,/
 匹配名称包含 'chr' 的进程

/^([^,]*,){2}(chrome|firefox)\\.exe,/
 匹配名为 chrome.exe 或 firefox.exe 的进程

/^([^,]*,){5}boinc\\.exe,/
 匹配作为 boinc.exe 直接子进程的进程（若要包含所有后代，请改用 childof:）

/^([^,]*,){2}conhost\\.exe,([^,]*,){2}boinc\\.exe,/
 匹配作为 boinc.exe 子进程、名为 conhost.exe 的进程

/^[^,]*,(jeremy|bob),chrome\\.exe,/
 匹配用户为 jeremy 或 bob、名称为 chrome.exe 的进程

/^([^,]*,){2}chrome\\.exe,.*-type=renderer([^,\\\\]|\\\\.)*$/
 匹配进程名为 'chrome.exe' 且命令行（最后一个字段）中含 '-type=renderer' 的进程

/^([^,]*,){3}[^,]*\\\\program files/
 匹配路径包含 '\\Program Files' 的进程（匹配不区分大小写）。
```

**自行编写规则**

- 用 `[^,]*` 而不是 `.*` 来限制在单个字段内。`.*` 会一直延伸到后面的字段，因此 `/^([^,]*,){2}.*chr.*,/` 也会匹配路径或父进程名含 'chr' 的进程。
- 把备选项放进圆括号：`(jeremy|bob)`。若不括号，`|` 会把整个表达式一分为二，于是 `/^([^,]*,)(jeremy)|(bob),/` 会匹配字符串中任意位置的 'bob,'。
- 字段匹配以逗号结尾，例如 `chrome\\.exe,`，这样它就不会同时匹配 chrome.exe.old 这类更长的值。
- 每个短语都以正斜杠开头和结尾。没有前导斜杠时，短语会被当作传统通配符匹配。短语在开头斜杠之后的第一个斜杠处结束，即便是转义斜杠也一样，因此字面斜杠请写成 `\\x2f`。
- Process Lasso 会在使用前把短语转换为小写。`\\d`、`\\s`、`\\w` 这类小写转义可用，但其大写形式（`\\D`、`\\S`、`\\W`、`\\B`）会变成小写形式；请用 `[^0-9]` 代替 `\\D`，依此类推。

**如何测试正则表达式** 要测试您的正则表达式，我们推荐[这个站点](https://regex101.com/r/t69lfP/1)。我们已预载了一份您将要匹配的样本，字段同样是（另见上文）：

```
PID,User,Process,Path,ParentPID,Parent,,,,CommandLine (always last)
```

此外，您可以创建一个文本文件，其中每行模拟 Process Lasso 提供的匹配串，然后用 grep（WSL 或 Linux）或其他工具匹配正则。注意需要去掉包裹用的正斜杠。示例：

```
sample.txt:
20116,jeremy,chrome.exe,C:\Program Files (x86)\Google\Chrome\Application\chrome.exe,19233,chrome.exe,,,,"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --type=renderer
```

```
测试命令：
grep -P 'chr.*' sample.txt
```

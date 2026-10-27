<!-- source: https://bitsum.com/apps/process-lasso/docs/reference/ini-config/ -->

<a id="ini-configuration-file"></a>

# INI 配置文件

<a id="using-the-ini-configuration-file"></a>

## 使用 INI 配置文件

Process Lasso 把配置选项与进程规则存储在 INI 文件 `prolasso.ini` 中。图形界面会替您编辑该文件，因此大多数人从不需要打开它。系统管理员以及规则集庞大的用户，有时会手动编辑它、推送到其他机器，或把它纳入版本控制。您可以从*文件*菜单打开该文件、导出与导入，或改用其他文件。

支持手动编辑，但校验比图形界面少。开始之前请先阅读[编辑规则](ini-config.md#editing-rules)。

<a id="configuration-profiles"></a>

### 配置方案

您从*文件*菜单创建的每个配置方案都有自己的子目录与自己的 `prolasso.ini`，可以在方案之间切换。「default」方案就是那个未命名的根配置文件，它并不表示默认设置。自动切换方案请见[配置方案切换器](../power/config-profile-switcher.md)。

<a id="where-is-the-ini-configuration-file-located"></a>

### INI 配置文件位于何处？

默认情况下，Process Lasso 会为它运行的每个用户上下文各创建一个配置文件，位于该用户应用数据文件夹下的 `ProcessLasso` 子文件夹中。日志也存放在同一文件夹。*关于*窗口会显示完整路径。

管理员可以在安装程序中指定全局配置路径，让每个 Process Lasso 实例与 Process Governor 都指向同一个共享配置文件。参见[配置与日志路径](config-paths.md)与[配置推送 / 拉取](../deployment/config-push-pull.md)。

<a id="editing-rules"></a>

## 编辑规则

- **手动编辑前请先退出图形界面。** 核心引擎（Process Governor）会察觉文件时间戳或大小变化并自动重新加载。但如果图形界面开着，它下一次保存可能会覆盖您的修改。
- **每条写成 `Key=value`。** 键名匹配不区分大小写。`=` 两侧允许有空格（`Key = value`），键与值的首尾空格会被去除。
- **段名只用于组织。** 键共享单一的扁平命名空间。Process Lasso 读取某个键时会忽略它位于哪个 `[Group]` 之下。同一个键出现多次时，第一次出现的生效。唯一的例外是 `[GPUAdapters]`，它按整段读取。
- **注释行以 `#` 或 `;` 开头。** 读取时被忽略，并在 Process Lasso 下次保存文件时被丢弃。
- **布尔值**接受 `true`、`1`、`yes` 或 `on`，以及 `false`、`0`、`no` 或 `off`，不区分大小写。Process Lasso 写入 `true` 与 `false`。其他取值无效，通常按 false 读取。
- **数字为普通十进制**，除非某个键另有说明。不是数字的值按 `0` 读取。大多数数值键没有范围校验，因此请留在文档给出的范围内。
- **编码：** Process Lasso 以带字节顺序标记（BOM）的 UTF-16LE 写入文件。它也能读取 UTF-8（带或不带 BOM）、UTF-16BE 与 ANSI：没有 BOM 的文件若为合法 UTF-8 则按 UTF-8 读取，否则按 ANSI。Process Lasso 下次保存时会把文件转换为 UTF-16LE。
- **缺失的键**取默认值。您只需要写想改动的键。

<a id="list-syntax"></a>

### 列表语法

大多数规则键在单个值中保存一组条目。

- 条目以逗号分隔：`a.exe,b.exe`。
- 每个条目含多个字段的规则类型，字段之间以分号分隔：`match;field2;field3`。有些较旧的规则类型改用逗号交替分隔匹配与取值：`match,value,match,value`。下文每个键都会说明它采用哪种形式。
- 若要在匹配项中放字面逗号，请转义为 `\,`；放字面分号则转义为 `\;`。
- Process Lasso 保存时会把大多数列表转为小写。
- 每个条目中的*匹配*接受完整的[进程匹配](process-matching.md)语法：通配符、路径名、命令行等等。

<a id="affinity-syntax"></a>

### 相关性语法

CPU 相关性写成从 0 开始的十进制 CPU 编号。范围用连字符表示，各项之间用分号分隔：`0-3;6;8-11`。

- `all` 表示所有 CPU。
- 在逻辑处理器超过 64 个的系统上，前缀处理器组编号与斜杠：`1/0-7`。
- CPU 集为每个圆括号项使用一条组相关性：`(0/0-3)(1/4-7)`。

<a id="priority-values"></a>

### 优先级取值

| 类别 | 取值 |
| --- | --- |
| CPU 优先级类别（按名称） | `real time`、`high`、`above normal`、`normal`、`below normal`、`idle` |
| CPU 优先级类别（Win32 常量） | `0x100` 实时、`0x80` 高、`0x8000` 高于正常、`0x20` 正常、`0x4000` 低于正常、`0x40` 空闲 |
| I/O 优先级 | `0` 很低、`1` 低、`2` 正常、`3` 高、`4` 关键 |
| 内存优先级 | `0` 最低、`1` 很低、`2` 低、`3` 中等、`4` 低于正常、`5` 正常 |
| GPU 优先级 | `0` 空闲、`1` 低于正常、`2` 正常、`3` 高于正常、`4` 高、`5` 实时 |
| GPU 适配器偏好 | `0` 由 Windows 决定、`1` 节能、`2` 高性能 |

<a id="sample-configuration-file"></a>

## 配置文件示例

这是一个经过删减的示例。Process Lasso 会写出它用到的每个键，段之间不留空行；手动编辑时允许空行。

```
[OutOfControlProcessRestraint]
OocOn=true
TotalProcessorUsageBeforeRestraint=70
PerProcessUsageBeforeRestraint=10
TimeOverQuotaBeforeRestraint=900
PerProcessUsageForRestore=3
MinimumTimeOfRestraint=4200
MaximumTimeOfRestraint=240000
ExcludeServices=true
OocExclusions=

[GUI]
ShowGraphCPU=true
GPUCollectMode=0

[Performance]
UpdateSpeedGUI=1000
UpdateSpeedCore=1000
ForcedMode=false

[ProcessDefaults]
DefaultPriorities=backup*.exe,below normal,game.exe,high
DefaultAffinitiesEx=render.exe,0,0-7
DefaultIOPriorities=indexer.exe,1

[ProcessAllowances]
DisallowedProcesses=badapp.exe
InstanceLimitedProcesses=notepad.exe;2

[AdvancedRules]
WatchdogRules2=leaky.exe;0;1;2048.00;30000;0;0;1;-;-;-;-
```

<a id="groups-overview"></a>

## 段一览

| 段 | 内容 |
| --- | --- |
| [Administration](ini-config.md#group-administration) | 配置版本 |
| [OutOfControlProcessRestraint](ini-config.md#group-outofcontrolprocessrestraint) | [ProBalance](../algorithms/probalance.md) |
| [GUI](ini-config.md#group-gui) | 图表与窗口外观 |
| [GPUAdapters](ini-config.md#group-gpuadapters) | 图表显示哪些 GPU 适配器 |
| [Advanced](ini-config.md#group-advanced) | 自动更新 |
| [Performance](ini-config.md#group-performance) | 常规行为、刷新频率、强制模式 |
| [Sampling](ini-config.md#group-sampling) | 进程的定期 CSV 快照 |
| [ForegroundBoosting](ini-config.md#group-foregroundboosting) | [前台提升](../rules/foreground-boosting.md) |
| [SystemTrayIcon](ini-config.md#group-systemtrayicon) | 托盘图标外观 |
| [Logging](ini-config.md#group-logging) | 记录哪些事件 |
| [MemoryManagement](ini-config.md#group-memorymanagement) | [智能内存整理](../algorithms/smarttrim.md) |
| [SysTrayBalloons](ini-config.md#group-systrayballoons) | 托盘通知 |
| [ProcessAllowances](ini-config.md#group-processallowances) | 不允许的进程、实例限制、节流、CPU 限制器、启动提升、效率模式 |
| [ProcessDefaults](ini-config.md#group-processdefaults) | 优先级、相关性、CPU 集、保持运行与电源计划规则 |
| [AdvancedRules](ini-config.md#group-advancedrules) | 看门狗、处理器组扩展器 |
| [GamingMode](ini-config.md#group-gamingmode) | [性能模式](../algorithms/performance-mode.md) |
| [PowerManagement](ini-config.md#group-powermanagement) | 启动电源计划、阻止睡眠的进程 |
| [PowerSaver](ini-config.md#group-powersaver) | [空闲节能](../power/idlesaver.md) |
| [LoadBasedPowerSwitcher](ini-config.md#group-loadbasedpowerswitcher) | [基于负载的配置方案切换](../power/load-based-switching.md) |

<a id="keys"></a>

## 键

布尔键接受 `true` 或 `false`（或其他[布尔写法](ini-config.md#editing-rules)）。时间单位是毫秒，除非键另有说明。

<a id="group-administration"></a>

### Administration

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| Version | 数字 |  | 最后写入该文件的 Process Lasso 版本。仅供参考，从不被读取。 |

<a id="group-outofcontrolprocessrestraint"></a>

### OutOfControlProcessRestraint

这些键用于配置 [ProBalance](../algorithms/probalance.md)。

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| OocOn | 布尔 | 视情况 | 开启或关闭 ProBalance。 |
| TotalProcessorUsageBeforeRestraint | 1-100 | 视情况 | 在抑制任何进程之前必须达到的系统总 CPU 百分比。 |
| PerProcessUsageBeforeRestraint | 1-100 | 视情况 | 进程被抑制前必须使用的 CPU 百分比。 |
| TimeOverQuotaBeforeRestraint | ms | 视情况 | 进程必须持续超过单进程阈值多久才会被抑制。 |
| PerProcessUsageForRestore | 1-100 | 视情况 | 受抑制的进程需降到该 CPU 百分比以下才会被恢复。 |
| MinimumTimeOfRestraint | ms | 视情况 | 进程处于抑制状态的最短时间。 |
| MaximumTimeOfRestraint | ms | 视情况 | 超过该时长后抑制结束；此后仅当进程仍符合条件才会再次被抑制。`0` 表示禁用该限制。 |
| TameOnlyNormal | 布尔 | true | 只抑制以正常优先级运行的进程。 |
| LowerToIdleInsteadOfBelowNormal | 布尔 | false | 把被抑制进程降到空闲优先级，而不是低于正常。 |
| DoNotLowerPriorityClass | 布尔 | false | 不改变被抑制进程的优先级类别。配合相关性或效率模式抑制使用。 |
| LowerIOPriorityDuringRestraint | 布尔 | false | 同时降低被抑制进程的 I/O 优先级。 |
| RestrainByAffinity | 布尔 | false | 同时通过更改 CPU 相关性来抑制。 |
| RestraintAffinity | [相关性](ini-config.md#affinity-syntax) 或 `random` | 空 | RestrainByAffinity 开启时施加的相关性。 |
| ProBalanceDropOneRandomCore | 布尔 | false | 不用 RestraintAffinity，而是从进程相关性中移除一个随机核心。 |
| DoNotAdjustAffinityIfCustomized | 布尔 | true | 不改变那些相关性已被自定义过的进程的相关性。 |
| UseEfficiencyMode | 布尔 | false | 同时通过把进程置入[效率模式](../rules/efficiency-mode.md)来抑制。 |
| OocDisableCoreParkingWhileIn | 布尔 | false | 有进程受抑制期间禁用核心停放。 |
| ExcludeForegroundProcesses2 | 布尔 | 视情况 | 从不抑制前台进程。 |
| ExcludeChildrenOfForeground | 布尔 | true | 从不抑制前台进程的子进程。 |
| ExcludeServices | 布尔 | true | 不抑制 Windows 服务。 |
| DisableProBalanceWhenSysIdle | 布尔 | false | 用户空闲时暂停 ProBalance。 |
| DisableProBalanceIfSysIdleThisManyMS | ms | 30000 | 用户需空闲多久才暂停 ProBalance。 |
| OocExclusions | 匹配列表 | 空 | ProBalance 永不抑制的进程。 |
| OocHardCodedExclusionOverrides | 匹配列表 | 空 | 您已覆盖的内置排除项，使 ProBalance 可以抑制这些进程。 |
| MatchExclusionsByPathnameToo | 布尔 | false | 让 OocExclusions 按完整路径名匹配，而不只是进程名。 |
| PlaySoundOnRestraint | 布尔 | false | 抑制进程时播放声音。 |
| PlaySoundOnRestore | 布尔 | false | 恢复进程时播放声音。 |
| PlayOnRestraint | 文件路径 | Windows 声音 | 抑制时播放的 `.wav` 文件。 |
| PlayOnRestore | 文件路径 | Windows 声音 | 恢复时播放的 `.wav` 文件。 |
| ChangeTrayIconOnRestraint | 布尔 | true | 有进程受抑制时更改托盘图标。 |

<a id="group-gui"></a>

### GUI

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| ClearLogAtExit | 布尔 | false | 图形界面退出时清空日志。 |
| ShowCPUCoreUtilGraphs | 布尔 | true | 显示每核心使用率面板。 |
| ShowGraphLegend | 布尔 | true | 显示图表图例。 |
| ShowGraphCPU | 布尔 | true | 绘制 CPU 使用率。 |
| ShowGraphResponsiveness | 布尔 | true | 绘制系统响应能力。 |
| ShowGraphMemoryLoad | 布尔 | true | 绘制内存负载。 |
| ShowGraphProBalanceEvents | 布尔 | true | 在图表上标记 ProBalance 抑制。 |
| ShowGraphSelectedProcessesCPUHistory | 布尔 | true | 绘制所选进程的 CPU 历史。 |
| ShowGraphGPU | 布尔 | true | 绘制 GPU 使用率。 |
| GraphGPUShowAllLines | 布尔 | false | 为每个 GPU 适配器单独画一条线。 |
| GraphGPUCombinedWidget | 布尔 | false | 把所有 GPU 显示在一个合并小部件中。 |
| GPUCollectMode | `0` 自动、`1` 所有适配器、`2` 仅可见适配器 | 0 | 从哪些 GPU 适配器收集数据。 |
| GraphAntiAliasing | 布尔 | true | 对图表线条抗锯齿。 |
| GraphShowTooltips | 布尔 | true | 悬停在图表上时显示提示。 |
| ProBalanceCountersOnGraph | 布尔 | true | 在图表上显示 ProBalance 计数器。 |
| ShowGraphLicenseName | 布尔 | false | 在图表上显示被许可人名称。 |
| ShowPowerProfile | 布尔 | true | 显示当前电源计划。 |
| ShowCPUUtilityAsPrimary | 布尔 | true | 绘制 CPU *实用率*（像任务管理器那样计入时钟频率），而不是 CPU *时间*。 |

*显示进程图标*这一设置保存在注册表中，而非 INI 文件。

<a id="group-gpuadapters"></a>

### GPUAdapters

该段为每个 GPU 适配器保存一条 `adapter=true|false` 条目，记录图表是否显示该适配器。这些条目由图形界面写入。

<a id="group-advanced"></a>

### Advanced

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| AutomaticUpdate | 布尔 | false | 自动安装更新。 |

<a id="group-performance"></a>

### Performance

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| UpdateSpeedGUI | `0`（暂停）、`250`、`500`、`1000`、`2000`、`5000`、`10000` | 1000 | 图形界面刷新间隔，单位 ms。其他值会回落为 1000。 |
| UpdateSpeedCore | `10`、`50`、`100`、`250`、`500`、`1000`、`2000`、`5000`、`10000` | 1000 | Process Governor 刷新间隔，单位 ms。取值越低反应越快，但占用更多 CPU。 |
| ForcedMode | 布尔 | false | 持续重新应用规则。参见[强制模式](global-options.md#forced_mode)。 |
| ManageOnlyCurrentUser | 布尔 | false | 只管理属于当前用户的进程。 |
| ExitOnCloseWindow | 布尔 | false | 窗口关闭时退出图形界面，而不是最小化到托盘。 |
| SoundsOff | 布尔 | true | 关闭所有声音。 |
| GracefulWaitTimeInMs | ms | 5000 | 在终止应用程序之前，等待其正常关闭的时长。 |
| IgnoreProblematicProcesses | 布尔 | false | 把 Process Lasso 无法访问的进程（例如受保护的系统进程）从进程列表中隐藏。 |
| AllowBlacklistedProcesses | 布尔 | false | 对 Process Lasso 通常不碰的关键系统进程也施加规则。不推荐。 |
| IgnoreSuspendedProcesses | 布尔 | false | 隐藏已挂起的进程。 |
| RecentlyTerminatedViewExclusions | 匹配列表 | 空 | 不显示在「最近终止」视图中的进程。 |
| SetTimerResolutionAtStartup | 100 ns 单位 | 0 | 启动时设置的系统定时器分辨率；例如 `5000` 表示 0.5 ms。`0` 表示不设置。参见[系统定时器分辨率](../rules/timer-resolution.md)。 |
| DefaultsLevel | 数字 |  | 内部使用：ProBalance 默认值版本。默认值变更后 Process Lasso 用它来提供重置。请勿修改。 |

<a id="group-sampling"></a>

### Sampling

启用采样后，Process Lasso 会定期为匹配的进程写出 CSV 快照。

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| SamplingEnabled | 布尔 | false | 开启或关闭采样。 |
| SamplingIntervalSeconds | 秒 | 900 | 两次快照之间的间隔。 |
| SamplingOutputPath | 文件路径 | 空 | CSV 的写入位置。可包含 `%yyyy%`、`%MM%`、`%dd%`、`%hh%`、`%mm%` 与 `%ss%`，它们按当前 UTC 时间填充。 |
| SamplingIncludePattern | 以 `;` 分隔的通配符 | `*` | 要包含的进程名。 |
| SamplingExcludePattern | 以 `;` 分隔的通配符 | 空 | 要排除的进程名。 |

<a id="group-foregroundboosting"></a>

### ForegroundBoosting

参见[前台提升](../rules/foreground-boosting.md)。

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| BoostForegroundProcess | 布尔 | false | 开启或关闭前台提升。 |
| ForegroundBoostPriorityClass | [Win32 优先级常量](ini-config.md#priority-values) | 0x8000 | 赋予前台进程的优先级类别。接受十六进制（`0x`）或十进制。 |
| BoostOnlyNormal | 布尔 | true | 只提升以正常优先级运行的进程。 |
| ForegroundBoostGPU | [GPU 优先级](ini-config.md#priority-values) 或 `-1` | -1 | 赋予前台进程的 GPU 优先级。`-1` 表示不改变 GPU 优先级。 |
| BoostOnlyNormalGPU | 布尔 | true | 只对以正常 GPU 优先级运行的进程做 GPU 提升。 |
| ForegroundBoostExclusions | 匹配列表 | 空 | 永不提升的进程。 |

<a id="group-systemtrayicon"></a>

### SystemTrayIcon

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| UseStaticIcon | 布尔 | false | 使用静态托盘图标，而不是动态图表图标。 |
| ShowResponsivnessInTrayInsteadOfProcessorUsage | 布尔 | false | 在托盘图标中显示响应能力而非 CPU 使用率。 |

<a id="group-logging"></a>

### Logging

参见[日志查看器与日志记录](../interface/logging.md)。

| 键 | 默认 | 记录内容 |
| --- | --- | --- |
| LogDisable | false | 关闭所有日志记录。 |
| IncludeCommandLines | false | 在日志条目中包含进程命令行。 |
| LogProcessExecutions | false | 进程启动 |
| LogProcessTerminations | false | 进程退出 |
| LogProcessesDisallowed | true | 不允许的进程被终止 |
| LogInstanceLimitTerminations | true | 因实例数量限制而终止 |
| LogDefaultPriorityAdjustments | true | 优先级规则动作 |
| LogDefaultAffinityAdjustments | true | 相关性规则动作 |
| LogProBalanceBegin | true | ProBalance 抑制 |
| LogProBalanceEnd | true | ProBalance 恢复 |
| LogProBalanceParkingChanges | true | ProBalance 核心停放更改 |
| LogPowerProfileChanges | true | 电源计划更改 |
| LogSmartTrim | true | 智能内存整理动作 |
| LogCPULimiter | true | CPU 限制器动作 |
| LogStartupBoostActions | true | 启动提升动作 |
| LogEfficiencyMode | true | 效率模式更改 |
| LogGroupExtender | true | 处理器组扩展器动作 |
| LogCPUSets | true | CPU 集更改 |

<a id="group-memorymanagement"></a>

### MemoryManagement

参见[智能内存整理](../algorithms/smarttrim.md)。

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| SmartTrimIsEnabled | 布尔 | false | 开启或关闭智能内存整理。 |
| SmartTrimWorkingSetTrims | 布尔 | false | 整理进程工作集。 |
| SmartTrimClearStandbyList | 布尔 | false | 清除系统待机列表。 |
| SmartTrimClearFileCache | 布尔 | false | 清除系统文件缓存。 |
| ClearStandbyFreeRAMThresholdMB | MB | 1024 | 只有当可用内存低于该值时才清除待机列表。 |
| ClearStandbyOnlyInPerfMode | 布尔 | true | 只在性能模式期间清除待机列表。 |
| SmartTrimAutoMinimumRAMLoad | % | 65 | 只有当系统内存负载达到或超过该百分比时，智能内存整理才动作。 |
| MinimumProcessWSSInMb | MB | 196 | 只整理工作集大于该值的进程。 |
| SmartTrimIntervalMins | 分钟 | 15 | 两次整理之间的最短间隔。 |
| SmartTrimExclusions | 匹配列表 | 空 | 永不整理的进程。 |
| SmartTrimLogNoAction | 布尔 | true | 智能内存整理检查过但未采取动作时也记录日志。 |

<a id="group-systrayballoons"></a>

### SysTrayBalloons

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| EnableSystemTrayNotification | 布尔 | false | 显示托盘通知。 |
| BalloonTipDuration | ms | 10000 | 通知显示时长。Windows 可能施加自己的限制。 |
| ShowBalloonsForOocPriorityRestoration | 布尔 | false | ProBalance 恢复进程时也发出通知。 |

<a id="group-processallowances"></a>

### ProcessAllowances

| 键 | 格式 | 说明 |
| --- | --- | --- |
| DisallowedProcesses | `match,match,...` | 启动后即被终止的进程。参见[自动终止](../rules/auto-terminate.md)。 |
| AllowedProcesses | `match,match,...` | DisallowedProcesses 的例外项。例如禁止 `notepad*.exe` 而允许 `notepad1.exe` 时，`notepad1.exe` 可以运行，`notepad2.exe` 不行。 |
| InstanceLimitedProcesses | `match;max,...` | 进程允许的最大实例数。参见[实例数量限制](../rules/instance-limits.md)。 |
| ApplyInstanceCountLimitsToAllUsers | 布尔（默认 false） | 跨所有用户会话统计实例数，而不只是按会话。 |
| InstanceManagedCPUAffinities | `match;algorithm;cores;threshold;reserved;smt;random,...` | [实例均衡器](../algorithms/instance-balancer.md)规则。*algorithm*：`0` 平均分配、`1` 每实例固定核心数、`2` NUMA 节点。*cores*：每实例核心数，供算法 1 与 2 使用。*threshold*：实例被均衡前必须使用的 CPU 百分比。*reserved*：从 CPU 0 开始保留不用的核心数。*smt*：`y` 表示避免把实例放到 SMT 兄弟核心上。*random*：`y` 表示随机分配核心。 |
| ProcessThrottles | `match;level,...` | [硬性节流](../algorithms/hard-throttling.md)规则。*level*：`1` 最低、`3` 低、`5` 中、`10` 高、`20` 最高。 |
| OneTimeProcessThrottles | `match;pid;level,...` | 只作用于某个运行中进程 ID 的节流。这些由图形界面管理。 |
| CPULimitRules | `match;cpu%;over_ms;cores;for_ms,...` | [CPU 限制器](../algorithms/cpu-limiter.md)规则。当进程在 *over\_ms* 内至少使用 *cpu%* 时，从它的相关性中移除 *cores* 个核心，持续 *for\_ms*。 |
| StartupBoostRules | `match;priority;seconds;efficiency,...` | [启动提升](../rules/startup-boost.md)规则。*priority*：优先级类别名称。*seconds*：提升持续时间。*efficiency*：`1` 表示提升期间让进程避开效率模式，否则为 `0`。 |
| EfficiencyMode | `match,mode,match,mode,...` | [效率模式](../rules/efficiency-mode.md)规则。*mode*：`1` 开启、`0` 关闭。 |

<a id="group-processdefaults"></a>

### ProcessDefaults

| 键 | 格式 | 说明 |
| --- | --- | --- |
| DefaultPriorities | `match,priority,match,priority,...` | CPU 优先级类别规则，使用[优先级类别名称](ini-config.md#priority-values)。参见[优先级](../rules/priorities.md)。 |
| DefaultIOPriorities | `match,value,...` | [I/O 优先级](ini-config.md#priority-values)规则。 |
| DefaultMemoryPriorities | `match,value,...` | [内存优先级](ini-config.md#priority-values)规则。 |
| DefaultGPUPriorities | `match,value,...` | [GPU 优先级](ini-config.md#priority-values)规则。 |
| DefaultGPUAdapterPreferences | `match,value,...` | [GPU 适配器偏好](ini-config.md#priority-values)规则。 |
| ManageWindowsGpuPreferences | 布尔（默认 true） | 让 GPU 适配器偏好规则与注册表中 Windows 的按应用显卡设置保持同步。 |
| DefaultAffinitiesEx | `match,delay_ms,affinity,...` | [CPU 相关性](../rules/cpu-affinities.md)规则。*delay\_ms* 延迟在进程启动后施加相关性的时间；`0` 表示不延迟。*affinity* 使用[相关性语法](ini-config.md#affinity-syntax)。 |
| CPUSets | `match,sets,...` | [CPU 集](../rules/cpu-sets.md)规则。*sets* 使用[相关性语法](ini-config.md#affinity-syntax)的圆括号形式。 |
| NamedAffinities | `name,affinity,...` | 保存在相关性菜单中显示的预设相关性。 |
| ThreadPriorityBoosts | `match;value,...` | Windows 动态线程优先级提升。*value*：`0` 禁用、`1` 启用。参见[线程提升](../rules/priorities.md#boost)。 |
| KeepRunningProcessesEx | `match;command_line;;elevate,...` | [保持运行](../rules/keep-running.md)规则。第三个字段为保留位，留空。*elevate*：`true` 或 `false`。 |
| DefaultPowerSchemes | `match;power plan name,...` | [应用电源计划](../power/power-profiles.md)规则，按电源计划名称。 |
| MatchWildcardsToPathnames | 布尔（默认 true） | 让规则同时按完整路径名与进程名匹配。参见[进程匹配](process-matching.md)。 |
| MatchOnCommandLine | 布尔（默认 false） | 让规则按命令行匹配。 |

设置为*通过 Windows 注册表强制执行*的规则存储在注册表中，而非 INI 文件。参见[优先级](../rules/priorities.md)。

<a id="group-advancedrules"></a>

### AdvancedRules

| 键 | 格式 | 说明 |
| --- | --- | --- |
| WatchdogRules2 | 见[下文](ini-config.md#documentation-of-watchdogrules) | [进程看门狗](../rules/watchdog.md)规则。 |
| DivideCPUPercentThresholdsBySystemCPUCount | 布尔（默认 false） | 按 CPU 数量缩放看门狗的 CPU 阈值。 |
| ProcessorGroupExtended | `match,match,...` | 由[处理器组扩展器](../algorithms/group-extender.md)处理的进程。 |
| ProhibitInternetExplorerExceptWhenAny | `match,match,...` | Internet Explorer（`iexplore.exe`）只有在这些进程之一运行时才能运行。 |

<a id="group-gamingmode"></a>

### GamingMode

参见[性能模式](../algorithms/performance-mode.md)。

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| GamingModeEnabled | 布尔 | false | 性能模式是否开启。 |
| GamingChangePowerPlan | 布尔 | true | 性能模式启动时切换电源计划。 |
| TargetPowerPlan | 电源计划名称 | Bitsum 最高性能 | 要切换到的计划。 |
| GamingModeEngageForSteam | 布尔 | false | 对 Steam 游戏自动启动性能模式。 |
| AutomaticGamingModeProcessPaths | `match,match,...` | 空 | 自动启动性能模式的进程。 |
| AutomaticGamingModeUserExclusions | `match,match,...` | 空 | 永不自动启动性能模式的进程。 |

<a id="group-powermanagement"></a>

### PowerManagement

| 键 | 取值 | 说明 |
| --- | --- | --- |
| StartWithPowerPlan | 电源计划名称 | Process Lasso 启动时要激活的电源计划。留空表示不更改。 |
| Display | `match,match,...` | 运行期间让显示器保持唤醒的进程。参见[阻止睡眠的进程](../rules/anti-sleep.md)。 |
| PC | `match,match,...` | 运行期间让电脑保持唤醒的进程。 |

<a id="group-powersaver"></a>

### PowerSaver

参见[空闲节能](../power/idlesaver.md)。

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| EnergySaverEnabled | 布尔 | false | 开启或关闭空闲节能。 |
| PowerSaver\_IdleTime | 秒 | 300 | 用户需空闲多久后空闲节能才切换计划。 |
| PowerSaver\_TargetGUID | 电源计划名称 |  | 空闲时使用的计划。尽管键名叫 GUID，取值是计划名称而非其 GUID。 |
| EnergySaverForceActivePowerProfile | 布尔 | false | 用户活跃时，保持 EnergySaverUpPowerProfileName 生效。 |
| EnergySaverUpPowerProfileName | 电源计划名称 | 空 | 用户回来时使用的计划。 |
| DisableEnergySaverDuringGamingMode | 布尔 | true | 性能模式期间不切换计划。 |
| EnergySaverUseCPUThreshold | 布尔 | false | 只有当 CPU 使用低于 EnergySaverCPUThreshold 时才认为系统空闲。 |
| EnergySaverCPUThreshold | %（允许小数） | 5.00 | 用于空闲检测的 CPU 阈值。 |
| PowerSaver\_Exclusions | `match,match,...` | 空 | 运行期间阻止空闲节能介入的进程。 |
| EnergySaverEvents | 布尔 | true | 记录空闲节能事件。 |

<a id="group-loadbasedpowerswitcher"></a>

### LoadBasedPowerSwitcher

参见[基于负载的配置方案切换](../power/load-based-switching.md)。

| 键 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| LoadBasedPowerSwitcherEnabled | 布尔 | false | 开启或关闭基于负载的切换。 |
| LoadBasedPowerSwitcherLowPowerProfileName | 电源计划名称 |  | 轻负载时使用的计划。 |
| LoadBasedPowerSwitcherHighPowerProfileName | 电源计划名称 |  | 重负载时使用的计划。 |
| LoadBasedPowerSwitcherLowCPULoadThreshold | %（允许小数） | 10.00 | CPU 负载低于该值时切换到低负载计划。 |
| LoadBasedPowerSwitcherHighCPULoadThreshold | %（允许小数） | 50.00 | CPU 负载高于该值时切换到高负载计划。保持它高于低负载阈值。 |
| LoadBasedPowerSwitcherMinimumTimeInPowerPlanMs | ms | 5000 | 再次切换前在某个计划中的最短停留时间。 |
| LoadBasedPowerSwitcherAveragingWindowSamples | 1-60 | 5 | CPU 负载参与平均的采样数。 |
| LoadBasedPowerSwitcherDeferLowPlan | 布尔 | true | 只管理高负载计划：负载下降时恢复切换前活动的计划，而不是激活低负载计划。 |
| LoadBasedPowerSwitcherLoggingEnabled | 布尔 | true | 记录计划切换。 |

<a id="documentation-of-watchdogrules"></a>

## WatchdogRules 说明

[进程看门狗](../rules/watchdog.md)规则存储在 `WatchdogRules2` 键中。规则之间以逗号分隔，每条规则有 12 个以分号分隔的字段。写为 `-` 的字段表示空。

```
WatchdogRules2=match;action;metric;threshold;duration;action_value;metric_detail;compare;launch_path;launch_args;-;-
```

| # | 字段 | 取值 |
| --- | --- | --- |
| 1 | match | 要监视的进程，采用[进程匹配](process-matching.md)语法。逗号转义为 `\,`。 |
| 2 | action | `0` 终止、`1` 重启、`2` 更改 CPU 相关性、`3` 整理虚拟内存、`4` 设置 CPU 优先级、`5` 设置 I/O 优先级、`6` 停止处理后续规则、`7` 只记录日志、`8` 运行命令 |
| 3 | metric | `0` CPU、`1` 内存 |
| 4 | threshold | CPU 百分比，或内存 MB。允许小数。 |
| 5 | duration | 执行动作前，进程必须超过（或低于）阈值的时长，单位 ms。 |
| 6 | action\_value | 动作 2：以十进制位掩码表示的相关性。动作 4：十进制的 [Win32 优先级常量](ini-config.md#priority-values)。动作 5：[I/O 优先级](ini-config.md#priority-values)。其他情况填 `0`。 |
| 7 | metric\_detail | 内存规则：`0` 工作集、`1` 提交费用（专用字节）、`2` 虚拟内存总量、`3` 任一内存指标。CPU 规则填 `0`。 |
| 8 | compare | `1` 大于、`2` 小于。`0` 表示大于。 |
| 9 | launch\_path | 动作 8 要运行的程序。其他情况填 `-`。 |
| 10 | launch\_args | 动作 8 的命令行参数。其他情况填 `-`。 |
| 11-12 | 保留 | 始终为 `-`。 |

**示例：** 当 `leaky.exe` 的提交费用持续 30 秒高于 2 GB 时重启它：

```
WatchdogRules2=leaky.exe;1;1;2048.00;30000;0;1;1;-;-;-;-
```

更早的版本使用 `WatchdogRules` 与 `OverloadProcessActions` 两个键。当前版本会忽略它们，因此请在 `WatchdogRules2` 或图形界面中重建那些规则。

<a id="legacy-keys"></a>

## 旧版键

当 Process Lasso 载入较旧的配置时，它仍会读取下列键并迁移它们。下次保存时，它们会以新名称写入，旧键被移除。

| 旧键 | 由谁取代 |
| --- | --- |
| DefaultAffinities | DefaultAffinitiesEx（合并进去，延迟为 0） |
| DefaultPowerSchemesEx | DefaultPowerSchemes（进程重复时新键优先） |
| KeepRunningProcesses | KeepRunningProcessesEx（迁移的规则为提升权限运行） |
| DisableThreadPriorityBoost、DisableThreadPriorityBoostBoost | ThreadPriorityBoosts（条目以取值 0 迁移） |
| ExcludeForegroundProcesses | ExcludeForegroundProcesses2（新键优先） |
| RoundRobinAffinitySelection | ProBalanceDropOneRandomCore |
| AllowDisplaysPreventPC | PC |

以下旧键完全不再被读取：`UpdateSpeed`、`CloseApplicationTimeoutSeconds`、`LogAllProcessesExecuted`、`LogOutOfControlProcessesRestrained`、`LogOutOfControlProcessesRestored2`、`HideGraph`、`ShowThreadsAndModulesView`、`WatchdogRules` 与 `OverloadProcessActions`。

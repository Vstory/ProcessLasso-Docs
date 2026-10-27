<!-- source: https://bitsum.com/apps/process-lasso/docs/rules/ -->

<a id="automation"></a>

# 自动化

您是否需要：

- 设置永久的 CPU 相关性、优先级或其他进程设置？
- 在特定应用程序运行时切换电源计划？
- 在进程的 CPU 使用超过某个水平后对其加以约束？

这些只是 Process Lasso 众多自动化能力的一部分！您可以通过自行编写的规则掌控电脑，也可以让 Process Lasso 的自动化[算法](../algorithms/index.md#algorithms)代劳。

> **提示**
>
> 您创建的规则会以简写形式显示在进程列表的「规则」列中。每个符号的含义见 [规则列图例](../interface/rules-column.md)。

大多数规则都接受通配符，也可使用正则表达式进行更复杂的匹配。[在此了解更多](../reference/process-matching.md#processmatch)。若要针对某个应用程序启动的所有进程，请使用 [`childof:` 匹配](../reference/process-matching.md#htoc-childof)，例如 `childof:steam.exe`。

Process Lasso 的自动化能力包括：

- **[CPU 相关性](cpu-affinities.md#default_affinities)** — 设置永久的 CPU 相关性，使进程每次启动时都在指定的 CPU 集合上运行。
- **[CPU 集](cpu-sets.md#cpusets)** — 一种「更软」的 CPU 相关性形式，更像是首选核心。
- **[优先级类别](priorities.md#default_priorities)** — 设置永久的 CPU、GPU、I/O 与内存优先级，使进程每次启动时都以期望的优先级运行。
- **[线程优先级提升](priorities.md#boost)** — 为进程启用或禁用动态线程优先级提升。
- **[效率模式](efficiency-mode.md#efficiency_mode)** — 设置并持久保存每个进程的效率模式设置。
- **[不允许的进程](auto-terminate.md#auto_terminate)** — 按您设定的条件立即终止任何匹配的进程。
- **[保持运行](keep-running.md#keep_running)** — 在选定的进程终止时自动重启它们。
- **[空闲节能](../power/idlesaver.md#idlesaver)** — 在电脑空闲时切换到更节省的电源计划以节能。
- **[电源计划自动化](../power/power-profiles.md#application_power_profiles)** — 在空闲时（[空闲节能](https://bitsum.com/idlesaver/)）或在指定进程运行时切换电源计划。
- **[阻止睡眠](anti-sleep.md#anti_sleep)（保持唤醒）** — Process Lasso 可以让电脑在指定时间内、或在选定进程运行期间不进入睡眠。
- **[禁用超线程或 SMT](cpu-affinities.md#smt)** — 按进程动态禁用超线程或 SMT。
- **[前台提升](foreground-boosting.md#foreground-boosting)** — 动态提高拥有输入焦点的应用程序的优先级。
- **[启动提升](startup-boost.md#startup_boost)** — 在进程启动后的一段时间内临时提高其优先级类别。
- **[系统定时器分辨率](timer-resolution.md#system-timer-resolution)** — 以最小 0.5ms 的步进调整并持久保存系统定时器分辨率。
- **[多选操作](../interface/all-processes.md#multi_context)** — 一次对多个进程执行终止之类的操作！
- **[高级看门狗规则](watchdog.md#watchdog)** — 创建「如果…则…」规则，在匹配的进程达到特定资源消耗阈值或其他条件时执行动作。
- **[配置方案](../power/config-profile-switcher.md#config-profile-switcher)** — 配置方案让您可以创建并使用多套规则配置。
- **更多……** — Process Lasso 还包含大量其他功能，欢迎您自行探索！

![进程上下文菜单](../../media/process-context-menu.png)

进程上下文菜单

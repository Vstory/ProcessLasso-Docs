<!-- source: https://bitsum.com/apps/process-lasso/docs/algorithms/probalance/ -->

# ProBalance

*若需总体介绍，包括排除项以及它与性能模式的对比，请参阅 [Process Lasso 中的 ProBalance：它如何保持 Windows 响应能力](https://bitsum.com/how-probalance-works/)。*

ProBalance（Process Balance）是 Process Lasso 的旗舰算法。它通过临时降低独占 CPU 的后台进程的优先级，在高 CPU 负载下保持系统响应能力。该功能默认启用，无需调校。

<a id="what-problem-it-solves"></a>

## 它解决什么问题

Windows 的 CPU 调度程序允许以正常优先级运行的 CPU 密集型进程占用所有可用周期。一旦如此，系统上其他所有东西都要与它争抢 CPU 时间，从而造成迟滞、停顿与卡死。即便在现代多核系统上，少数贪婪的线程也能明显降低响应能力。

ProBalance 处理这一问题的方式与 Linux 调度程序内部的做法相同：干扰响应能力的 CPU 密集型进程会被施加惩罚，而交互式与 I/O 密集型进程则不受干涉。

<a id="how-it-works"></a>

## 工作原理

当 ProBalance 检测到某个后台进程超过其阈值时，会临时降低该进程的优先级类别，通常降到低于正常。这一调整：

- **是临时的。** 条件一旦解除，原优先级立即恢复。
- **是轻微的。** 受抑制的进程仍能获得可观的 CPU 时间，只是优先次序被降低。测试表明后台任务几乎以相同的时间完成，而前台响应能力显著改善。
- **是有选择性的。** 前台进程以及没有造成麻烦的进程绝不会被触碰。

当 ProBalance 正在抑制某个进程时，系统托盘图标会变红，该进程在状态列中显示*受抑制*，该动作也会记入[日志](../interface/logging.md)。如果某个进程从未出现在日志中，说明 ProBalance 从未对它动作。

想亲眼看到效果，可以运行 [ProBalance 概述页](https://bitsum.com/how-probalance-works/)中的 CPUEater 演示。它会让未受保护的系统被正常优先级的线程拖停；而在运行 Process Lasso 时，同样的负载下系统依然可用。

> **提示**
>
> 不要为了保持重要进程的响应能力而把它们提到高或实时优先级。ProBalance 从相反方向入手，降低肇事进程的优先级，这样安全得多。

<a id="ooc_options"></a>

<a id="probalance-options"></a>

## ProBalance 选项

*菜单路径：选项 / CPU / ProBalance*

若干高级参数控制 ProBalance 是否以及何时动作，包括进程必须超过的 CPU 阈值、必须持续多久，以及施加何种调整。默认值是长期打磨的产物；改动它们时要谨慎。

![ProBalance 高级配置对话框](../../media/probalance-settings.png)

有一个值得注意的选项把 ProBalance 与[效率模式](../rules/efficiency-mode.md)关联起来：被抑制的进程还可以被置入效率模式。该选项默认关闭，因为它比常规的优先级调整更重手。

<a id="probalance-exclusions"></a>

## ProBalance 排除项

基于名称的排除通常没有必要，因为 ProBalance 的其他条件已经使它忽略大多数不该动作的进程。如果日志或洞察显示 ProBalance 正在抑制一个您希望放过的进程，就添加一条命名排除。

![ProBalance 排除项对话框](../../media/probalance-exclusions.png)

排除项支持[正则表达式，以便进行更复杂精确的匹配](../reference/process-matching.md#processmatch)。

<a id="common-questions"></a>

## 常见问题

**ProBalance 会让被抑制的进程变慢吗？**
只会轻微影响。降低优先级改变的是调度优先次序，而不是 CPU 应得份额。系统不争抢时，低于正常优先级的进程全速运行。

**在核心数很多的 CPU 上还有用吗？**
有用。由耗 CPU 进程引起的响应问题在当前一代硬件上依然存在，ProBalance 在这些平台上仍然有效。

**我是否应该改为手动给所有进程设置优先级？**
不必。持久优先级是支持的，但对所有进程一刀切地手动重排优先级带来的问题多于解决的问题。让算法去做动态、临时的调整。

**那改为提高前台进程优先级呢？**
Windows 已经会提升前台应用程序。再提高它的优先级会让调度更不利于它所依赖的进程。Process Lasso 提供了[前台提升](../rules/foreground-boosting.md)作为可选项，但出于这个原因默认关闭。

<a id="related-pages"></a>

## 相关页面

- [CPU 限制器](cpu-limiter.md)：当您确实想给进程的 CPU 使用设上限时
- [效率模式](../rules/efficiency-mode.md)
- [日志记录](../interface/logging.md)：查阅 ProBalance 动作
- [前台提升](../rules/foreground-boosting.md)

<!-- source: https://bitsum.com/apps/process-lasso/docs/algorithms/instance-balancer/ -->

<a id="instancebalancer"></a>

<a id="instance-balancer"></a>

# 实例均衡器

- *菜单路径：「选项 / CPU / 实例均衡器 …」*

实例均衡器把 CPU 核心分配到正在运行的进程实例之间，既可以是同一应用程序的实例，也可以是多个应用程序的实例（使用[高级匹配规则](../reference/process-matching.md#processmatch)时）。例如在 8 核系统上运行着 4 个 notepad.exe 实例，按规则每个实例可能分到 2 个 CPU 核心。随着 notepad.exe 实例数量的变化，分配给每个实例的 CPU 核心数也会调整。

当实例数超过分配的核心数时，实例以轮转方式「堆叠」。当受管应用程序因新进程创建或终止而实例数变化时，会重新均衡。

[![](../../media/instance-balancer.png)](../../media/instbalance.png)

实例均衡器规则配置

<a id="algorithm-types"></a>

## 算法类型

- **每实例均等核心** — 在匹配的进程实例之间平均分配 CPU 核心，并随着新实例运行或终止动态调整。
- **每实例固定核心数** — 为每个匹配的进程实例分配固定数量的 CPU 核心。
- **NUMA** — 把实例加载到不同的 NUMA 节点上。核心数可以设为每个 NUMA 节点的核心数，也可以更少。任何实例都不会跨越多个 NUMA 节点。

<a id="options"></a>

## 选项

- **每实例核心数** — 选择「每实例固定核心数」时，这是分配给每个匹配该规则的运行实例的 CPU 核心数。
- **保留核心（可选）** — 这是每个处理器组中要从匹配该规则实例的可用集合里排除的逻辑 CPU 核心数。用户可以用它把 CPU 核心留给其他系统活动。不过大多数情况下，这个值应当就是 0。
- **CPU 使用阈值（可选）** — 这是匹配进程被纳入集合并按规则做实例均衡所需的最低 CPU 使用百分比。如果您想排除那些不怎么用 CPU 的实例，这会很有用。不需要最低阈值时该值可为 0。
- **禁用 HT/SMT** — 勾选后，将选择物理 CPU 核心而非逻辑 CPU 核心。请注意，该功能与「固定核心数」或「保留核心」一起使用时，这些选项指定核心数仍以逻辑单元计算，因此 2 等于分配 1 个物理 CPU。
- **随机化** — 从可用集合中随机挑选 CPU 核心，而不是按顺序分配给每个进程实例。目的是把负载更好地分散到 CPU 拓扑上。与默认的顺序分配不同，该选项支持跨多个处理器组均衡。

进程的所有子进程都可以用 [`childof:` 前缀](../reference/process-matching.md#htoc-childof)匹配，例如 `childof: boinc.exe`。直接子进程也可以用正则表达式匹配，例如 `/^([^,]*,){5}boinc\.exe.*,/`。

该功能支持[正则表达式，以便进行更复杂精确的匹配](../reference/process-matching.md#processmatch)。

![](../../media/instbalance_example.png)

实例均衡器运行示例

<a id="demo-video"></a>

## 演示视频

[观看演示视频（YouTube）](https://www.youtube.com/watch?v=VrE9jgovhTo)

Process Lasso 实例均衡器演示视频

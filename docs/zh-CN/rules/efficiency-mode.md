<!-- source: https://bitsum.com/apps/process-lasso/docs/rules/efficiency-mode/ -->

<a id="efficiency_mode"></a>

<a id="efficiency-mode"></a>

# 效率模式

效率模式是 Windows 的一种信号，表示进程并非时间关键，因此操作系统可以降低其优先级、以更低的时钟速度运行它，或把它调度到能效核（E 核）上（如果存在）。Windows 本身无法让该设置保持生效；Process Lasso 则可以让您为特定进程持久保持效率模式开启或关闭。

> **注意**
>
> 需要 Windows 11 或更高版本。在混合架构 CPU（例如 Intel 的 P 核/E 核设计）上，效率模式会强烈影响进程运行在哪些核心上。

<a id="when-to-use-it"></a>

## 适用场景

- **强制关闭**：用于被 Windows 不恰当地归为高效的性能关键进程，使其避开 E 核，并免于其他节能动作。
- **强制开启**：用于您不在意其响应能力的后台进程，降低其功耗以及对前台工作的干扰。

关于让程序留在 P 核上的其他方法，以及哪些 CPU 具有 E 核，参见 [Intel 混合架构 CPU：在 P 核与 E 核上调度](https://bitsum.com/intel-hybrid-p-cores-e-cores/)。

<a id="how-to-set-it"></a>

## 如何设置

右键单击进程，使用上下文菜单为当前实例设置效率模式；或在「始终」子菜单下建立持久规则。

![进程上下文菜单中的效率模式](../../media/efficiency-mode-context-menu.png)

持久规则可以在「选项 / CPU / 效率模式」中统一管理。

![效率模式规则所在的应用程序菜单位置](../../media/efficiency-mode-app-menu.png)

![效率模式规则配置对话框](../../media/efficiency-mode-rules.png)

<a id="how-it-is-displayed"></a>

## 显示方式

- **状态**列会为当前处于效率模式的进程显示*效率*。（该列显示的状态还包括 ProBalance 施加的*受抑制*与*已挂起*。）
- **[规则](../interface/rules-column.md)**列中，效率模式始终开启的规则显示为 **E**，始终关闭显示为 **e**。

![效率模式状态列与规则符号](../../media/efficiency-status-rules.png)

<a id="caveats-and-interactions"></a>

## 注意事项与相互影响

- 有些应用程序是把单个*线程*而非整个进程标记为高效。Process Lasso 目前不显示线程级别的分类，但「效率模式始终关闭」规则可确保该进程内没有任何线程被归为高效。
- [ProBalance](../algorithms/probalance.md#ooc_options) 有一个选项，可以在抑制进程期间把它们置入效率模式。该选项默认关闭，因为它比 ProBalance 常规的优先级调整更重手。

<a id="related-pages"></a>

## 相关页面

- [CPU 相关性](cpu-affinities.md)：对进程可用核心的硬性约束
- [CPU 集](cpu-sets.md)：软性的核心偏好
- [ProBalance](../algorithms/probalance.md)

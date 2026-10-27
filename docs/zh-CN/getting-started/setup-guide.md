<!-- source: https://bitsum.com/apps/process-lasso/docs/getting-started/setup-guide/ -->

<a id="process-lasso-settings-how-to-set-it-up-and-the-best-settings-for-gaming"></a>

# Process Lasso 设置：如何配置（以及游戏场景的最佳设置）

Process Lasso 用默认设置就能很好地工作：安装后，[ProBalance](https://bitsum.com/how-probalance-works/) 立刻开始保持 Windows 的响应能力。本指南介绍少数值得调整的设置，以及游戏场景的最佳设置。内容与最新版 Process Lasso 保持一致。

[下载 Process Lasso](https://bitsum.com/download-process-lasso/)

<a id="set-up-process-lasso-in-five-steps"></a>

## 五步完成 Process Lasso 设置

1. **安装并保持默认设置。** ProBalance 默认开启，无需调校。大多数人从不改动其他设置。
2. **为最重要的程序标记性能模式。** 在进程列表中右键单击每个程序，选择「触发性能模式」。只要其中任一程序在运行，Process Lasso 就会切换到 Bitsum 最高性能电源计划。只标记最要紧的程序。参见 [性能模式](https://bitsum.com/bhp/)。
3. **在使用 P 核与 E 核的 Intel CPU 上，让关键程序避开 E 核。** 右键单击程序，选择「效率模式 / 始终 / 关」。若需要更强的偏好，再选择「CPU 集 / 始终」并选中「P 核」。参见 [效率模式](../rules/efficiency-mode.md) 与 [CPU 集](../rules/cpu-sets.md)，以及 [Intel 混合架构 CPU：在 P 核与 E 核上调度](https://bitsum.com/intel-hybrid-p-cores-e-cores/)，了解该做法适用于哪些 CPU。
4. **在拥有多个 CCD 的 AMD CPU 上，让游戏只用一个 CCD。** 右键单击游戏，选择「CPU 集 / 始终」，然后选中单个 CCD（「CCD0」或「CCD1」）。在双 CCD 的 Ryzen X3D 型号上，按钮会标明哪个 CCD 带 3D V-Cache（通常是「CCD0: cache」）。参见 [AMD Ryzen X3D CPU：让游戏留在 3D V-Cache CCD 上](https://bitsum.com/amd-x3d-ccd-affinity/)。
5. **排除任何程序之前先查看日志。** 如果您认为 ProBalance 在不恰当的时机对某个程序动作，先到日志或 ProBalance 洞察中查找它。如果日志里没有它，说明 ProBalance 没碰过它。如果有，右键单击该程序并选择「从 ProBalance 排除」。

<a id="best-process-lasso-settings-for-gaming"></a>

## 游戏场景的最佳 Process Lasso 设置

对大多数游戏而言，方法很简单：

- **让 ProBalance 保持开启。** 您正在玩的游戏就是前台进程，ProBalance 默认不干预前台进程，同时它会防止后台任务抢占 CPU 时间。
- **为游戏触发性能模式**，让 CPU 在您游玩时保持全速待命。如果您希望每次启动游戏都这样，请打开「选项 / 电源 / 性能模式 / 启用自动检测（例如 Steam）」。该选项默认关闭。
- **用上文第 3、4 步的 Intel 或 AMD 规则，把游戏留在正确的核心上。**
- **不要动游戏的优先级。** 把游戏提到高或实时优先级很少有益，反而可能造成卡顿或挂起。

<a id="counter-strike-2-cs2"></a>

### Counter-Strike 2（CS2）

CS2 的进程是 `cs2.exe`。

1. 右键单击 `cs2.exe`，选择「触发性能模式」。
2. Intel 混合架构 CPU：右键单击 `cs2.exe`，选择「效率模式 / 始终 / 关」，可选再用「CPU 集 / 始终」并选中「P 核」。
3. 双 CCD 的 AMD CPU：右键单击 `cs2.exe`，选择「CPU 集 / 始终」，选中带 3D V-Cache 的 CCD（通常是「CCD0」）；非 X3D 型号则任选一个 CCD。

如果日志显示 Process Lasso 无法更改 `cs2.exe`，请改用下文 Tarkov 所用的启动器方法。

### Escape from Tarkov

游戏进程是 `EscapeFromTarkov.exe`，由 BSG 启动器（`BsgLauncher.exe`）启动。Tarkov 的反作弊可能阻止 Process Lasso 直接修改游戏进程，因此请把规则设在仍然生效的对象上：

1. 右键单击 `EscapeFromTarkov.exe`，选择「触发性能模式」。性能模式在游戏运行时切换电源计划，因此无需修改游戏进程本身。
2. 若要把游戏限定在特定核心上，改为在启动器上设置规则：右键单击 `BsgLauncher.exe`，选择「CPU 相关性 / 始终 / 选择 CPU 相关性」，然后选中核心（Intel 混合架构 CPU 选 P 核，AMD X3D 选带 3D V-Cache 的 CCD）。进程会继承父进程的 CPU 相关性，因此游戏启动时就带有相同的核心，无需 Process Lasso 亲自打开它。

关于会阻止更改的游戏，更多内容见 [使用反作弊系统](../help/anti-cheat.md)。

<a id="settings-by-feature"></a>

## 按功能划分的设置

- [ProBalance](https://bitsum.com/how-probalance-works/)：在后台程序抢占 CPU 时保持 Windows 的响应能力。默认开启。
- [性能模式](https://bitsum.com/bhp/)：在选定的程序或游戏运行时切换到 Bitsum 最高性能电源计划。
- [智能内存整理](https://bitsum.com/smarttrim/)：仅在真正存在内存压力时整理后台进程。默认关闭，并附带针对 16 GB 与 32 GB 系统的建议设置。
- [CPU 限制器](https://bitsum.com/docs/limiting-cpu-use-with-process-lasso-cpu-limiter/)：对程序可用的 CPU 施加硬性上限。
- [空闲节能](../power/idlesaver.md)：在您离开时切换到更保守的电源计划；[应用电源计划](../power/power-profiles.md) 则为每个程序指定电源计划。

<a id="avoid-over-tweaking"></a>

## 避免过度调校

除非您确信某项高级设置的作用，否则坚持用基础功能。使用范围明确的规则：针对您在意的程序写一条规则，胜过对所有进程做一刀切的改动。当某项优化对几乎所有人都有益时，它会被纳入 ProBalance 这类默认功能，所以极少存在您漏掉的隐藏设置。试验一般不会造成持久问题，而且每条规则都能从创建它的同一菜单中移除。

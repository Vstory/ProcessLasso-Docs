<!-- source: https://bitsum.com/apps/process-lasso/docs/rules/cpu-affinities/ -->

<a id="default_affinities"></a>

<a id="cpu-affinities"></a>

# CPU 相关性

CPU 相关性控制某个进程允许使用哪些 CPU 核心；它的线程只会被调度到那组核心上。

<a id="when-to-use-it"></a>

## 适用场景

- 把特定核心专门留给某个游戏、应用程序或服务，并让其他软件避开它们。
- 通过缩小可用核心的范围，为进程的 CPU 消耗设置上限。
- 在多芯片 CPU 上让进程只留在某一个 CCD 或缓存域内。参见 [AMD Ryzen X3D CPU：让游戏留在 3D V-Cache CCD 上](https://bitsum.com/amd-x3d-ccd-affinity/)。
- 在 Intel 混合架构 CPU 上让进程留在 P 核，或让后台任务留在 E 核。参见 [Intel 混合架构 CPU：在 P 核与 E 核上调度](https://bitsum.com/intel-hybrid-p-cores-e-cores/)。

如果您只想在进程*行为异常时*降低其 CPU 使用，而不是永久限制，请改用 [CPU 限制器](../algorithms/cpu-limiter.md#cpulimiter)：它会动态约束相关性并在之后恢复。如果您想要一种调度程序在需要时可以覆盖的更软偏好，请使用 [CPU 集](cpu-sets.md#cpusets)。

<a id="how-to-set-it"></a>

## 如何设置

右键单击进程并选择「CPU 相关性」，可以只对当前实例生效，也可以在「始终」子菜单下建立持久规则。持久规则可以在「选项 / CPU / CPU 相关性」中统一管理。

![CPU 相关性规则对话框](../../media/cpu-affinities.png)

<a id="the-delay-field"></a>

### 延迟字段

可选的「延迟」字段只在进程启动后经过指定秒数时才施加相关性。这对那些在启动阶段对相关性变化敏感的游戏和应用程序有帮助，也可以刻意用来在加载期间先给进程完整的 CPU、之后再加以限制。

<a id="smt"></a>

<a id="disable-smt-or-hyper-threading"></a>

## 禁用 SMT 或超线程

「CPU 相关性」上下文菜单中有一项可以禁用某个进程的 SMT（超线程）：它施加一种只保留每个物理核心中一个逻辑核心的相关性。在大多数 CPU 型号上，这会产生交替的相关性模式。

<a id="caveats"></a>

## 注意事项

- **逻辑核心超过 64 个的系统：** Windows 把 CPU 相关性限制在单个处理器组内。Process Lasso 会尽力把多组进程的线程迁移到您选择的相关性上，但新线程不会被自动约束，除非持续重新施加相关性——Process Lasso 对持久规则会这样做。也可以考虑改用 [CPU 集](cpu-sets.md)，它没有多组限制。另见[处理器组扩展器](../algorithms/group-extender.md)。
- **受反作弊保护的游戏**会阻止直接修改相关性。关于利用启动器继承的变通做法，见[使用反作弊系统](../help/anti-cheat.md)。

<a id="related-pages"></a>

## 相关页面

- [CPU 集](cpu-sets.md)
- [CPU 限制器](../algorithms/cpu-limiter.md)
- [系统保留 CPU 集](reserved-cpu-sets.md)
- [反作弊系统](../help/anti-cheat.md)
- [CPU 相关性何时重要](https://bitsum.com/tips-and-tweaks/when-cpu-affinity-matters/)

<!-- source: https://bitsum.com/apps/process-lasso/docs/rules/priorities/ -->

<a id="priorities"></a>

# 优先级

<a id="default_priorities"></a>

<a id="cpu-priority-classes"></a>

## CPU 优先级类别

- *菜单路径：「选项 / CPU / CPU 优先级 …」*

优先级类别（在 Process Lasso 中有时也称作「CPU 优先级」）可让应用程序始终以特定优先级运行。

通常最好把重点放在降低后台和不重要进程的优先级上，而不是提高重要进程的优先级。这纯粹是 Windows 的设计使然。[ProBalance](../algorithms/probalance.md#probalance) 算法会动态地对 CPU 占用高的后台进程施加这类调整。

Windows 中可用的优先级类别有：

- 实时
- 高
- 高于正常
- 正常
- 低于正常
- 空闲

![](../../media/cpu-priorities.png)

通常设置优先级类别就足够了，但 I/O 优先级与内存优先级也可以通过各自的菜单项与对话框设置。

勾选菜单项「启用 Windows 动态线程优先级提升」可以禁用该 Windows 原生功能。这与「[线程提升](priorities.md#boost)」上下文菜单项反映的是同一个设置。

<a id="gpu-priority-classes"></a>

## GPU 优先级类别

- *菜单路径：「选项 / GPU / GPU 优先级 …」*

随着 AI 工作负载越来越多地争夺 GPU 资源，我们认为有必要为 Process Lasso 增加 GPU 优先级支持。现在用户可以确保最重要的 GPU 工作负载（例如游戏）获得优先。

可用的 GPU 优先级类别与 CPU 优先级类别相同：

- 实时
- 高
- 高于正常
- 正常
- 低于正常
- 空闲

进程列表中新增了「GPU 优先级」列，用于指示 GPU 优先级类别。

用户可以通过进程上下文菜单或菜单项「选项 / GPU / GPU 优先级…」设置 GPU 优先级规则。

![GPU 优先级类别规则配置对话框](../../media/gpu-priorities.png)

遗憾的是，GPU 优先级类别不会被子进程继承，也不支持「通过注册表强制执行」（IFEO）方式。这意味着受反作弊系统保护的进程无法设置 GPU 优先级。遇到这种情况，我们建议改为把注意力放在确保其他有 GPU 工作负载的进程被设为低于正常或空闲优先级。

<a id="io-priorities"></a>

## I/O 优先级

I/O 优先级向操作系统提示某个进程 I/O 的相对重要性。但它并不保证相对于其他 I/O 的优先次序，也不保证特定的 QoS 参数。

- 高
- 正常
- 低
- 很低

<a id="memory-priorities"></a>

## 内存优先级

内存优先级向操作系统提示内存页在被换出时的相对重要性。

> … 应当降低执行后台操作、或访问短期内不会再次访问的文件与数据的线程的默认内存优先级。例如，文件索引应用程序可能会为执行索引任务的进程设置较低的默认优先级。
>
> **内存优先级**有助于决定页面在被整理之前能在进程的[工作集](https://learn.microsoft.com/en-us/windows/desktop/Memory/working-set)中保留多久。进程的内存优先级决定了该进程的线程加入其工作集的物理页的默认优先级。当内存管理器整理工作集时，会先整理低优先级的页面，再整理高优先级的页面。这会提升系统整体性能，因为高优先级页面不太可能被从工作集中整理出去、并在再次访问时触发页面错误。
>
> [SetProcessInformation 函数 (processthreadsapi.h) – Win32 应用 | Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessinformation)

- 正常
- 低于正常
- 中等
- 低
- 很低

<a id="enforce-by-registry"></a>

<a id="enforce-by-windows-registry"></a>

## 通过 Windows 注册表强制执行

通过注册表强制执行使用 [Windows 映像文件执行选项](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/xperf/image-file-execution-options)功能，把优先级保存到注册表，使该进程每次启动时都以选定的优先级运行。由于优先级是在创建进程时由 Windows 施加的，这种方法对通常无法访问的进程同样有效，例如受反作弊系统保护的进程。缺点是这些设置会一直留在注册表中，如果不用 Process Lasso 这类工具管理，它们可能被忽略甚至遗忘。

该功能支持优先级类别、I/O 优先级与内存优先级。不支持 CPU 相关性及其他规则类型。

这种方式属于无碍操作，已知不会在反作弊系统内触发任何警报。反作弊系统施加的优先级限制更多是进程保护的副作用，而不是其目的之一。

<a id="setting-registry-enforced-priorities"></a>

### 设置由注册表强制执行的优先级

设置由注册表强制执行的优先级有两种方式：

- 在 [CPU 优先级类别](priorities.md#default_priorities)、I/O 优先级与内存优先级的规则配置对话框中，添加规则时勾选「通过注册表强制执行」。

![勾选了「通过注册表强制执行」的优先级类别对话框](../../media/enforce-by-registry-dialog.png)

- 在进程上下文菜单的「CPU 优先级 / 始终」（或「I/O 优先级 / 始终」「内存优先级 / 始终」）下，切换「通过 Windows 注册表强制执行」。勾选后，该进程该类型的「始终」优先级会存入注册表，而不是写入 Process Lasso 配置；取消勾选则把该规则转回普通的配置规则。

请注意，由注册表强制执行的优先级需要重启进程才会生效，因为它们是在进程创建时由 Windows 施加的。

<a id="reviewing-registry-enforced-priorities"></a>

### 查看由注册表强制执行的优先级

- *菜单路径：「选项 / 常规 / 查看保存到注册表的优先级 …」*

保存到注册表的优先级可以在此对话框中查看和移除。

![保存到注册表、可供查看与清理的优先级](../../media/registry-priorities.png)

保存到注册表、可供查看与清理的优先级

<a id="boost"></a>

<a id="thread-boost"></a>

## 线程提升

- *菜单路径：「选项 / CPU / 动态线程优先级提升 …」*

[动态线程优先级提升](https://learn.microsoft.com/en-us/windows/win32/procthread/priority-boosts)是 Windows 的一项原生功能，在线程被唤醒继续工作时临时提高其优先级。对新进程而言它默认开启，通常应保持开启。

当某个进程的动态线程优先级提升被禁用时，其优先级类别名称后会附加一个连字符。您可以通过「线程提升」上下文菜单或「选项 / CPU / 动态线程优先级提升…」开启或关闭提升。

![动态线程优先级提升](../../media/priority-boost-hyphen.png)

动态线程优先级提升被禁用时以连字符标示。

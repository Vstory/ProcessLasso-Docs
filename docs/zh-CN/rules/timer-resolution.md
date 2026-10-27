<!-- source: https://bitsum.com/apps/process-lasso/docs/rules/timer-resolution/ -->

<a id="system-timer-resolution"></a>

# 系统定时器分辨率

- *菜单路径：「工具 / 系统定时器分辨率」*

这是一个内置工具，用于持久保存对系统定时器分辨率的调整，精度最小可达 0.5ms。市面上其他工具不允许用户持久保存这项更改，因此每次开机都需要手动重新施加。我们无法断言这项调整的普遍效果，但不怀疑某些场景下它确实可取。重要的是，从 Windows 10 2004 起，对于自身未请求特定定时器分辨率的进程，除非您勾选了「全局应用」，该项调整不会产生影响。

来自 MSDN：

> 在 Windows 10 版本 2004 之前，此函数影响的是全局 Windows 设置。对所有进程，Windows 使用任一进程所请求的最低值（即最高分辨率）。从 Windows 10 版本 2004 起，此函数不再影响全局定时器分辨率。对于调用了此函数的进程，Windows 使用任一进程所请求的最低值（即最高分辨率）。对于未调用此函数的进程，Windows 不保证其分辨率高于系统默认分辨率。
>
> 从 Windows 11 起，如果拥有窗口的进程被完全遮挡、最小化，或以其他方式对最终用户不可见或不可闻，Windows 不保证其分辨率高于系统默认分辨率。有关此行为的更多信息，请参阅 [SetProcessInformation](https://learn.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessinformation)。
>
> 设置更高的分辨率可以提高等待函数中超时间隔的准确性。但它也可能降低系统整体性能，因为线程调度程序会更频繁地切换任务。高分辨率还可能阻止 CPU 电源管理系统进入节能模式。设置更高的分辨率并不会提高高分辨率性能计数器的准确性。
>
> [timeBeginPeriod 函数 (timeapi.h) – Win32 应用 | Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/api/timeapi/nf-timeapi-timebeginperiod)

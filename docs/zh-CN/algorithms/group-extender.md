<!-- source: https://bitsum.com/apps/process-lasso/docs/algorithms/group-extender/ -->

<a id="groupextend"></a>

<a id="processor-group-extender"></a>

# 处理器组扩展器

Process Lasso 9.7 新增了处理器组扩展器。这一新颖的算法让不支持处理器组的应用程序也能利用完整的 CPU。它的做法是监视目标进程的线程，并在需要时把线程动态分配到补充处理器组。

处理器组只用于逻辑核心超过 64 个的系统。由于 Windows 的 CPU 相关性以 64 位位掩码表示，人们引入了处理器组以支持超过 64 个逻辑核心。因此，一条 CPU 相关性只作用于单个处理器组，而每个进程在启动时都会被分配一个默认处理器组。除非手动把线程分配到其他处理器组，进程的线程都被限制在该默认组内。通常这种线程分配由应用程序自行完成。能够把自身线程分配到其他处理器组的应用程序称为「组感知」的。

因此，组不感知的应用程序会被限制在单个处理器组内，使其他组中的 CPU 核心得不到充分利用。理想情况下，应用程序开发者会更新软件使其具备组感知能力；但在尚未如此的情况下，Bitsum 现在有了解决方案！我们称之为处理器组扩展器。它监视目标进程的线程，并把多余的线程分配到补充处理器组。

请注意，只有在应用程序需要额外 CPU 核心、却不具备处理器组感知能力时，处理器组扩展器才是必要的，也才应当使用。不必要的或不当的使用可能影响应用程序的性能表现。

<a id="update-windows-11-and-windows-server-2022"></a>

## 更新：Windows 11 与 Windows Server 2022

在 Windows 11 与 Windows Server 2022 上，我们的处理器组扩展器功能已不再必要。Windows CPU 调度程序现在默认会把应用程序线程散布到所有处理器组 [[MSDN](https://docs.microsoft.com/en-us/windows/win32/procthread/processor-groups)]。若要完全掌控其发生方式，请试试 Process Lasso 的 [CPU 集](https://bitsum.com/product-update/process-lasso-10-4-cpu-sets-and-adler-lake/)功能。

![处理器组扩展器](../../media/groupextender.png)

处理器组扩展器

[观看演示视频（YouTube）](https://www.youtube.com/watch?v=LB6qWhP35KE)

<!-- source: https://bitsum.com/apps/process-lasso/docs/getting-started/how-it-works/ -->

<a id="components-of-process-lasso"></a>

# Process Lasso 的组成部分

Process Lasso 由一个核心引擎和一个用户界面组成。两者相互分离，因此用户可以在完全关闭用户界面的同时让 Process Lasso 保持活动、继续管理进程。核心引擎以 ProcessGovernor.exe 运行，用户界面则是 ProcessLasso.exe。只运行核心引擎时，内存占用仅约 1-3MB（通常如此），且几乎不消耗 CPU。启动用户界面 ProcessLasso.exe 时，如果当前用户或服务方式下还没有 ProcessGovernor.exe 核心引擎在运行，它会自动启动一个实例。关闭用户界面时，程序会询问您是否让核心引擎继续运行。默认情况下，每个用户会话都有各自的 ProcessLasso.exe 与 ProcessGovernor.exe 实例。另一种常见配置是把 Governor 作为服务运行，并按需启动图形界面。

| 组件 | 文件名 | 说明 |
| --- | --- | --- |
| 图形用户界面（GUI） | ProcessLasso.exe | 该图形界面用于配置进程规则与功能、显示正在运行的进程，以及 Process Governor 服务的近期活动（日志）。它还承载系统托盘图标。 |
| 核心引擎（Governor） | ProcessGovernor.exe | 这个非交互式系统服务称为 Process Governor 或「核心引擎」，负责实际执行进程规则与算法。它可以在没有 GUI 的情况下独立运行，占用资源极少。 |
| 会话代理 | bitsumsessionagent.exe | 这个极小的进程帮助 Process Lasso 获取每个交互式用户会话的特定信息，即前台进程 ID 与最后输入时间（供空闲计时器使用）。ProBalance 与空闲节能会使用这些数据。保持唤醒与阻止睡眠功能也依赖此进程，它未运行时这些功能无法正常工作。bitsumsessionagent.exe 几乎没有开销，因此不应禁用其启动任务。 |
| 配置文件 | prolasso.ini | 该配置文件保存 Process Lasso 的进程规则与选项。可通过「选项 / 常规 / 配置启动…」更改路径。 |
| 日志文件 | prolasso.log | 该日志文件记录近期操作。可以将其禁用。可通过「选项 / 常规 / 配置启动…」更改路径。该文件为 CSV 格式。 |

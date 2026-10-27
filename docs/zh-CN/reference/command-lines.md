<!-- source: https://bitsum.com/apps/process-lasso/docs/reference/command-lines/ -->

<a id="command_line"></a>

<a id="command-line-arguments"></a>

# 命令行参数

<a id="htoc-installer-command-line"></a>

<a id="installer"></a>

## 安装程序

| 开关 *（粗体为默认值）* | 说明 | 示例 |
| --- | --- | --- |
| /S（区分大小写） | 执行静默安装，也就是非交互式或无人值守安装。由于安装过程中不会显示任何配置对话框，您应当配合使用下面列出的其他开关，以指明希望如何配置 Process Lasso。 | ProcessLassoSetup.exe /S |
| /language=[**English**] | 指明要使用的语言。若未提供该值，默认使用英语。不要尝试使用不受支持的语言，并确保语言名称拼写与这里列出的一致（例如 SimpChinese）。您也可以指定语言的代码页编号。English (1033) German (1031) Russian (1049) Polish (1045) Italian (1040) Slovenian (1060) Japanese (1041) TradChinese (1028) SimpChinese (2052) …… | ProcessLassoSetup.exe /S /language=English ProcessLassoSetup.exe /S /language=1033  ProcessLassoSetup.exe /S /language=German ProcessLassoSetup.exe /S /language=1031  ProcessLassoSetup.exe /S /language=Slovenian  ProcessLassoSetup.exe /S /language=Italian  ProcessLassoSetup.exe /S /language=SimpChinese |
| /gui\_start\_type=[**all** \| current \| manual] | 指明 GUI 的启动方式：all 为所有用户登录时启动，current 为仅当前用户，manual 为手动启动。 | ProcessLassoSetup.exe /S /gui\_start\_type=all |
| /governor\_start\_type=[all \| current \| **service**] | 指明核心引擎（Governor）的启动方式：以服务方式启动，或在所有/当前用户登录时启动。 | ProcessLassoSetup.exe /S /governor\_start\_type=service |
| /logfolder=[folder] | 指明为系统上所有用户使用统一的日志文件夹。默认情况下，每个用户在各自的应用数据目录中拥有自己的日志文件夹。但有时把所有日志事件集中到单一日志文件夹是理想的。请确保该日志文件夹对 Governor 将要运行所处的上下文可写。若设为以普通进程运行，这可能意味着所有用户；若设为以服务运行，则应对服务用户（或 SYSTEM 用户）可写。 | ProcessLassoSetup.exe /S /logfolder=c:\\systemlogs  ProcessLassoSetup.exe /S /logfolder=c:\\systemlogs |
| /configfolder=[folder] | 指明为系统上所有用户使用统一的配置文件夹。默认情况下，每个用户在各自的应用数据目录中拥有自己的配置。但有时为所有用户使用同一配置是理想的，而当 Governor 以服务方式运行时则是必需的。请确保该配置文件夹对 Governor 将要运行的所有用户上下文可读，并对您允许更改配置的用户可写。 | ProcessLassoSetup.exe /S /configfolder=c:\\pl\_config  ProcessLassoSetup.exe /S /configfolder=c:\\pl\_config |
| /launch\_gui=[**true** \| false] | 指明安装后是否启动 GUI。即便启动了 GUI，它也会最小化到系统托盘。 | ProcessLassoSetup.exe /S /launch\_gui=false |
| /importconfigfrom=[path] | 指明从您指定的文件导入配置。这应与 /configfolder 配合使用。此处指定的文件将成为 Process Lasso 的初始配置。这里可以只指定文件夹，也可以指定具体文件名。若只指定文件夹，将在路径名后直接附加「prolasso.ini」。 | ProcessLassoSetup.exe /S /configfolder=c:\\pl\_config /importconfigfrom=c:\\temp  ProcessLassoSetup.exe /S /configfolder=c:\\pl\_config /importconfigfrom=c:\\temp\\my\_default\_config.ini |
| /username=[user] /password=[pass] | 以服务方式运行核心引擎（/governor\_start\_type=service）时，这些开关可用于指明以哪个用户身份启动服务。该用户必须拥有「作为服务登录」的权限（关于如何授予，见我们的[常见问题](https://bitsum.com/process-lasso-faq/)）。若未提供具体用户名，核心引擎将以系统上下文运行。请记住 Windows 用户密码是区分大小写的。 | ProcessLassoSetup.exe /S /governor\_start\_type=service /username=myuser /password=mypass |
| /configpw=[password] | 设置配置密码。当用户试图修改配置文件时，GUI 会要求输入该密码。使用该参数但不带值可移除现有密码。 | ProcessLassoSetup.exe /S /configpw=somepassword |
| /key=[licensekey] | 设置许可证密钥。 | ProcessLassoSetup.exe /S /key=1A79A4D60DE6718E8E5B326E338AE533 |
| /keyfile=[keyfile] | 密钥文件的绝对路径。不要使用相对路径。 | ProcessLassoSetup.exe /S /keyfile=c:\\users\\admin\\downloads\\prolasso.key |

## ProcessLasso.exe

GUI 与核心引擎都提供命令行参数。您可以用它们覆盖配置与日志路径，但通常并不必要，也不推荐这样做。更改配置与日志路径应通过安装程序（首选）或 InstallHelper 应用程序完成。

| 开关 | 说明 | 示例 |
| --- | --- | --- |
| /ShowWindow | 启动后打开主窗口。 | ProcessLasso.exe /showwindow |
| /ConfigFolder= | 指明应使用的配置文件夹。程序假定其中存在「prolasso.ini」；若不存在，将以默认值创建。 | ProcessLasso.exe /ConfigFolder=”c:\\program files\\Process Lasso\\config” ProcessLasso.exe /ConfigFolder=c:\\config\\ ProcessLasso.exe /ConfigFolder=\\server1\\ProcessLassoConfig\\ |
| /LogFolder= | 指明包含日志文件的文件夹。该文件夹需要读写权限。 | ProcessLasso.exe /LogFolder=\\server1\\logfolder ProcessLasso.exe /LogFolder=c:\\pslogs |
| /NoRaiseExisting | 仅当 ProcessLasso.exe 尚未运行时才启动新实例；但与默认行为不同，不显示已有实例的窗口。 | ProcessLasso.exe /NoRaiseExisting *（注意：v12.1 之前请使用 /no\_raise\_existing）* |
| /SetActiveProfile=name | 把当前配置方案切换为指定的已存在命名方案。该命令不会启动 Process Lasso，切换方案后即退出。 | ProcessLasso.exe /SetActiveProfile=myprofile |
| /StartWithProfile=name | 切换到指定配置方案，然后启动 Process Lasso。 | ProcessLasso.exe /StartWithProfile=myprofile |
| /TrimNow | 通知智能内存整理立即执行动作（若已如此配置）。 | ProcessLasso.exe /TrimNow |
| /ActivateOnly | 使用先前在安装程序命令行上给出的密钥激活产品，然后退出。 | ProcessLasso.exe /ActivateOnly |

## ProcessGovernor.exe

| 开关 | 说明 | 示例 |
| --- | --- | --- |
| /ConfigFolder= | 指明应使用的配置文件夹。程序假定其中存在「prolasso.ini」；若不存在，将以默认值创建。 | ProcessGovernor.exe /ConfigFolder=”c:\\program files\\Process Lasso\\” ProcessGovernor.exe /ConfigFolder=c:\\config\\ ProcessGovernor.exe /ConfigFolder=\\server1\\ProcessLassoConfig\\ |
| /LogFolder= | 指明包含日志文件的文件夹。该文件夹需要读写权限。 | ProcessGovernor.exe /LogFolder=\\server1\\logfolder ProcessGovernor.exe /LogFolder=c:\\pslogs |

<!-- source: https://bitsum.com/apps/process-lasso/docs/deployment/installation/ -->

<a id="installation"></a>

# 安装

Process Lasso 的安装程序可以从命令行无交互运行，只需在安装程序命令行后加上 /S 开关。INI 配置文件可能需要预先按期望的规则编好。为此，我们建议先在一台工作站上安装 Process Lasso，用图形界面创建规则。安装命令可能类似：

```
ProcessLassoSetup64.exe /S /gui_start_type=current /governor_start_type=service /importconfigfrom=\\somepath\lasso\prolasso.ini
```

便于产品激活或离线使用的密钥文件可以向 Bitsum 索取，站点版与服务器版的被许可人可以使用。安装程序命令行选项的完整列表见[此处](../reference/command-lines.md#command_line)。另外，Process Lasso 的可执行文件也可以直接嵌入您的软件包中，此时部署后用 /ConfigFolder=xxx 开关启动 processgovernor.exe 即可。视用途而定，可能无需启动图形界面（processlasso.exe）。若需要手动配置方面的指导，请[联系我们](https://bitsum.com/contact/)。

<a id="editions-and-architecture"></a>

## 版本与架构

Process Lasso 以三种原生构建发布：

| 构建 | 适用 | 安装程序文件 |
| --- | --- | --- |
| 32 位（x86） | 32 位 Windows | `ProcessLassoSetup.exe` |
| 64 位（x64） | Intel 与 AMD 上的 64 位 Windows | `ProcessLassoSetup64.exe` |
| ARM64 | ARM 上的 Windows（骁龙及其他 ARM64 电脑） | `ProcessLassoSetupARM64.exe` |

大多数用户从不需要选择。下载与安装程序会挑选与您系统匹配的构建，若误用了 32 位或 64 位安装程序，它会提示下载正确的那个。在 ARM64 电脑上，推荐使用原生 ARM64 构建以获得最佳性能；64 位 x64 构建也可以在 Windows 内置的模拟层下运行，因此已有的 x64 安装会继续可用。

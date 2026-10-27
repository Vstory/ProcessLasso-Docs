<!-- source: https://bitsum.com/apps/process-lasso/docs/deployment/enterprise/ -->

<a id="enterprise-deployment"></a>

# 企业部署

<a id="in-the-enterprise"></a>

## 在企业中

Process Lasso 在服务器上表现出色。它可以防止单个进程独占服务器的 CPU 资源。我们提供专门的 Process Lasso 服务器版，可免费试用 30 天。更多信息见 [bitsum.com](https://bitsum.com/)。

Process Lasso 可用于终端服务器、Web 服务器、文件服务器，或更复杂的网络客户端/服务器环境。事实上，几乎在任何您能想到的场景中都能使用它。核心引擎与图形界面相互独立，因此安装后无需对最终用户可见。您甚至可以把核心引擎作为系统服务运行，这是许多网络管理员会喜欢的功能。

<a id="on-a-terminal-server"></a>

### 在终端服务器上

在终端服务器上，我们建议让核心引擎（processgovernor.exe）为每个登录的用户各启动一个实例，该实例只管理该用户的进程。安装临近结束时会被问到这一点。因此，请选择只为自己启动图形界面（用于重新配置或查看日志），然后选择为所有用户启动核心引擎。在随后的配置对话框中，只需告知核心引擎仅管理其自身会话中的进程（默认设置即可）。这就是 Process Lasso 的设计方式，也是它运行效果最好的方式。

不要把核心引擎作为管理所有用户的服务来运行，原因是它无法识别其他用户会话中哪个进程处于前台，因此 ProBalance 算法无法做出同样明智的判断，可能临时降低活跃前台进程的优先级——这通常并不理想（不过大多数情况下也无大碍）。如果您仍想这样配置，可以把一些常见应用程序排除在 ProBalance 抑制之外，或者通过提高「ProBalance 参数」中的配额来「放缓」ProBalance。

如果您不使用 ProBalance，而是使用其他功能，那就不必担心，两种方式皆可。

您可以选择让每个用户拥有自己的配置文件与日志文件夹，也可以让所有用户共享同一份。安装临近结束时会给出该选项，与询问启动配置的是同一处。

<a id="on-distributed-networks-with-workstations-and-servers"></a>

### 在分布式网络（含工作站与服务器）中

在这里，您可以选择在工作站和服务器上都安装 Process Lasso，或只装在服务器上，由您决定。若愿意，您可以通过映射驱动器或 UNC 路径共享全局日志与配置文件。只要用户有访问权限，UNC 路径就没问题。这样就能实现一定程度的集中管理。

<a id="methods-of-deployment"></a>

### 部署方式

安装过程中临近结束时，会弹出一个小的配置向导，询问 Process Lasso 及其核心引擎应如何启动。首先请了解：核心引擎完全在后台运行，没有任何可见界面。系统托盘图标属于图形界面。您有两个基本选择：

1. 每个用户登录时获得一个属于自己的静默后台核心引擎实例（默认，也最有效）
2. 由单个核心引擎实例管理所有用户的进程（精度较低）

最大的问题在于：您想使用集中式网络配置与日志存储、按机器存储，还是按用户存储。

**方案 1：集中式配置与日志**

在这种模式下，所有工作站都配置为使用同一个配置文件与日志文件夹。它们可以位于网络共享上，也可以通过其他方式推送到工作站。

**方案 2：按工作站的配置文件与日志**

在这种模式下，您会在每个工作站上安装 Process Lasso，并使用该工作站所有用户都会访问的公共配置与日志路径。

**方案 3：按用户的配置文件与日志**

在这种模式下，您会在每个工作站上安装 Process Lasso，让每个用户拥有自己的配置与日志。这是 Process Lasso 的默认行为。如果您不需要或不想更改配置、也不想修改日志文件，这是运行 Process Lasso 的好方式。

**方案 4：上述方案的某种组合，或其他方法**

归根结底，您可以按几乎任何想要的方式使用 Process Lasso。例如，您可以让工作站从网络共享运行它，而不必在这些工作站上安装 Process Lasso。运行 Process Lasso 的前提条件非常少。较旧的系统（SP2 之前的 XP）需要先安装 Microsoft 的 GDIPLUS.DLL，Process Lasso 图形界面才能运行；不过核心引擎并不需要 GDIPLUS 库。除此之外没有其他前提条件。这让便携使用或从网络路径启动变得非常简单。

<a id="service-mode"></a>

### 服务模式

您可以把 Process Lasso 的核心引擎 processgovernor 安装为服务。安装 Process Lasso Pro 的过程中会给出该选项，在静默安装时也可通过命令行开关使用。

以服务方式运行核心引擎有利也有弊。如上所述，它不知道其他用户会话中哪个进程处于前台，因此 ProBalance 的动作远没有那么精确。不过这只影响 ProBalance，所以如果您不用 ProBalance，就不成问题。即便使用 ProBalance，加上一两条排除项与额外调校后通常也不会有问题（或许根本从来不是问题）。

<a id="silent-installation"></a>

### 静默安装

Process Lasso（自 v3.53 起）支持完全静默安装。更多信息见[命令行开关文档](../reference/command-lines.md#htoc-installer-command-line)。

<a id="more-help"></a>

### 还需要帮助？

如果您在把 Process Lasso 部署到企业中时遇到任何问题，请发邮件至 [support@bitsum.com](mailto:support@bitsum.com)。我们也提供定制方案。

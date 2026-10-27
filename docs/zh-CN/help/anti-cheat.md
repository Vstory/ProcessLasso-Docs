<!-- source: https://bitsum.com/apps/process-lasso/docs/help/anti-cheat/ -->

<a id="working-with-anti-cheat-systems"></a>

# 使用反作弊系统

许多游戏受反作弊系统保护，这些系统会阻止其他软件（包括 Process Lasso）打开它们的进程来更改 CPU 相关性或优先级等设置。这些游戏仍可以通过下列方法间接管理，按推荐程度排序。

<a id="set-rules-on-the-game-launcher"></a>

## 在游戏启动器上设置规则

子进程会继承父进程的 CPU 相关性。把 CPU 相关性规则（或其他可继承的设置）设在游戏启动器上，例如 `steam.exe` 或 `epicgameslauncher.exe`，由它启动的游戏就会继承该相关性，而 Process Lasso 从不需要触碰受保护的进程。

<a id="priorities-use-enforce-by-registry"></a>

## 优先级：使用通过注册表强制执行

专门针对优先级规则，请启用[通过注册表强制执行](../rules/priorities.md#enforce-by-registry)选项。它使用 Windows 原生机制，在创建进程时施加优先级，因此即便对启动后无法打开的进程同样有效。

<a id="last-resort-system-reserved-cpu-sets"></a>

## 最后手段：系统保留 CPU 集

有些用户会使用[系统保留 CPU 集](../rules/reserved-cpu-sets.md#system-reserved-cpu-sets)，它是系统级的 [CPU 集](../rules/cpu-sets.md#cpusets)形式，告知 Windows 让所有普通进程避开一组保留核心，游戏便实际上独享了这些核心。

> **警告**
>
> 这是一个激进的全系统设置，精度不如按进程的规则，而且它会一直留在注册表中直到被移除。使用前请阅读[系统保留 CPU 集](../rules/reserved-cpu-sets.md)页面。

<a id="related-pages"></a>

## 相关页面

- [CPU 相关性](../rules/cpu-affinities.md)
- [优先级](../rules/priorities.md)
- [系统保留 CPU 集](../rules/reserved-cpu-sets.md)

<!-- source: https://bitsum.com/apps/process-lasso/docs/reference/global-options/ -->

<a id="global-options"></a>

# 全局选项

<a id="forced_mode"></a>

<a id="forced-mode"></a>

## 强制模式

- *菜单路径：「选项 / 强制模式（持续重新应用设置）」*

强制模式位于「选项」菜单中，是一个开关，开启后会让规则被持续重新应用到正在运行的进程。对于会自行更改自身设置的进程，这可能是需要的。通常 Process Lasso 只会对进程的每个新实例做一次性调整；而强制模式会让它评估目标设置（例如 CPU 相关性或优先级类别）是否被改动过，若被改动则重新施加。

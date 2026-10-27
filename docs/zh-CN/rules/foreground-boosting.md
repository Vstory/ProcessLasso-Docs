<!-- source: https://bitsum.com/apps/process-lasso/docs/rules/foreground-boosting/ -->

<a id="foreground-boosting"></a>

# 前台提升

- *菜单路径：「选项 / CPU / 前台提升」*

前台提升会提高当前处于前台的进程的优先级类别。Windows 本身已对前台做优先级提升，额外的提升通常并无效果。ProBalance 反其道而行，降低有问题后台进程的优先级类别，这是有原因的。不过，前台提升在某些环境中仍然有用，在 Alder Lake 上它是向 Windows 调度程序发出「前台进程应优先使用 P 核」信号的简便方式。

注意：不要把前台提升与「线程提升」子菜单混淆，后者控制的是 Windows 动态线程优先级提升。

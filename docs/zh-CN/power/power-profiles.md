<!-- source: https://bitsum.com/apps/process-lasso/docs/power/power-profiles/ -->

<a id="application_power_profiles"></a>

<a id="application-power-profiles"></a>

# 应用电源计划

- *菜单路径：「选项 / 电源 / 应用电源计划 …」*

用户可以创建规则，使指定进程运行时系统进入所选电源计划，进程终止后再恢复到先前的电源计划。这让用户能把系统电源计划对准特定应用程序。您可以右键单击进程使用「*应用电源计划*」子菜单，或使用菜单项「*选项 / 电源 / 应用电源计划 …*」。

![应用电源计划规则对话框](../../media/app-power-profiles.png)

<a id="start-with-base-power-profile"></a>

## 起始（基础）电源计划

- *菜单路径：「选项 / 电源 / 以指定电源计划启动 Process Lasso …」*

该选项让您指定系统在 Process Lasso 首次启动时（任何规则执行之前），以及没有任何电源规则处于活动状态时应当处于的电源计划。它可以避免系统因同时生效的电源规则相互冲突、或电源计划被外部更改而最终落在非预期的电源计划上。

<!-- source: https://bitsum.com/apps/process-lasso/docs/rules/reserved-cpu-sets/ -->

# System Reserved CPU Sets

- *Menu path: ‘Tools / System Reserved CPU Sets’*

System Reserved CPU Sets is a kernel registry option that instructs the system to avoid using a particular set of CPU cores, which you can then dedicate to your real-time applications. Unlike per-process [CPU Sets](cpu-sets.md#cpusets) rules, this setting applies to the entire system.

WARNING: This is a draconian action that can persist after Process Lasso is uninstalled, though you will be prompted to remove it. Furthermore, application incompatibilities may exist and complications could arise from CPU affinity rules that include both reserved and unreserved cores.

This setting will prevent your system from being able to make full use of your CPU cores since you’ve reserved some of them. Additionally, this setting will disable core parking for reserved CPUs cores.

A system restart is required after changing this setting.

We recommend trying other features first before adjusting this kernel option, if for no other reason than the possibility of this value getting set, then forgotten about and forever impacting system performance.

![System Reserved CPU Sets Tool](../media/system-reserved-cpu-sets.png)

System Reserved CPU Sets Tool

When a System Reserved CPU Sets value is set Process Lasso will show it on the graph.

![](../media/reserved-cpu-sets-on-graph.png)

System Reserved CPU Sets Shown on Graph

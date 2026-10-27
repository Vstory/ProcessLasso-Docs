<!-- source: https://bitsum.com/apps/process-lasso/docs/help/anti-cheat/ -->

# Working With Anti-Cheat Systems

Many games are protected by anti-cheat systems that block other software, including Process Lasso, from opening their processes to change settings like CPU affinity or priority. These games can still be managed indirectly, using the methods below in order of preference.

## Set Rules on the Game Launcher

Child processes inherit the CPU affinity of their parent. Set your CPU affinity rule (or other inheritable settings) on the game's launcher, such as `steam.exe` or `epicgameslauncher.exe`, and games started from it will inherit that affinity, without Process Lasso ever touching the protected process.

## Priorities: Use Enforce By Registry

For priority rules specifically, enable the [Enforce By Registry](../rules/priorities.md#enforce-by-registry) option. This uses a native Windows mechanism that applies the priority at process creation time, so it works even on processes that cannot be opened after launch.

## Last Resort: System Reserved CPU Sets

Some users use [System Reserved CPU Sets](../rules/reserved-cpu-sets.md#system-reserved-cpu-sets), a system-wide form of [CPU Sets](../rules/cpu-sets.md#cpusets) that tells Windows to keep all ordinary processes off a set of reserved cores, which the game then effectively gets to itself.

> **Warning**
>
> This is a drastic, system-wide setting with less precision than per-process rules, and it persists in the registry until removed. Read the [System Reserved CPU Sets](../rules/reserved-cpu-sets.md) page before using it.

## Related Pages

- [CPU Affinities](../rules/cpu-affinities.md)
- [Priorities](../rules/priorities.md)
- [System Reserved CPU Sets](../rules/reserved-cpu-sets.md)

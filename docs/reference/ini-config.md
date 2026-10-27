<!-- source: https://bitsum.com/apps/process-lasso/docs/reference/ini-config/ -->

# INI Configuration File

## Using the INI Configuration File

Process Lasso stores its configuration options and process rules in an INI file, `prolasso.ini`. The graphical user interface (GUI) edits this file for you, so most people never need to open it. System administrators, and users with large rule sets, sometimes edit it by hand, push it to other machines, or keep it under version control. You can open the file from the *File* menu, export and import it, or choose an alternate file.

Hand editing is supported, but there is less validation than in the GUI. Read [Editing rules](ini-config.md#editing-rules) before you start.

### Configuration Profiles

Each config profile you create from the *File* menu gets its own subdirectory with its own `prolasso.ini`, and you can switch between profiles. The 'default' profile is simply the unnamed root configuration file. It doesn't mean default settings. See the [Config Profile Switcher](../power/config-profile-switcher.md) for switching profiles automatically.

### Where Is the INI Configuration File Located?

By default, Process Lasso creates a configuration file for each user context it runs in, in the `ProcessLasso` subfolder of that user's application data folder. The log is stored in the same folder. The *About* window shows the full paths.

Administrators can point every instance of Process Lasso and the Process Governor at one shared configuration file by choosing a global configuration path in the installer. See [Config and Log Paths](config-paths.md) and [Config Push / Pull](../deployment/config-push-pull.md).

## Editing Rules

- **Exit the GUI before you edit by hand.** The core engine (Process Governor) notices when the file's timestamp or size changes and reloads it automatically. If the GUI is open, though, its next save can overwrite your edit.
- **Write each entry as `Key=value`.** Key names are matched case-insensitively. Spaces around the `=` are allowed (`Key = value`), and leading and trailing spaces are trimmed from keys and values.
- **Group names are only for organization.** Keys share a single, flat namespace. When Process Lasso reads a key, it ignores which `[Group]` the key is under. If the same key appears more than once, the first occurrence wins. The one exception is `[GPUAdapters]`, which is read as a group.
- **Comment lines start with `#` or `;`.** They're ignored when the file is read, and dropped the next time Process Lasso saves the file.
- **Booleans** accept `true`, `1`, `yes` or `on`, and `false`, `0`, `no` or `off`, in any case. Process Lasso writes `true` and `false`. Other values aren't valid, and are generally read as false.
- **Numbers are plain decimal** unless a key says otherwise. A value that isn't a number reads as `0`. Most numeric keys have no range check, so stay within the documented values.
- **Encoding:** Process Lasso writes the file as UTF-16LE with a byte order mark (BOM). It also reads UTF-8 (with or without a BOM), UTF-16BE and ANSI: a file without a BOM is read as UTF-8 if it's valid UTF-8, and otherwise as ANSI. Process Lasso converts the file to UTF-16LE the next time it saves.
- **Missing keys** take their default values. You only need the keys you want to change.

### List Syntax

Most rule keys hold a list of entries in one value.

- Entries are separated by commas: `a.exe,b.exe`.
- In rule types with several fields per entry, the fields are separated by semicolons: `match;field2;field3`. Some older rule types alternate match and value with commas instead: `match,value,match,value`. Each key below shows which form it uses.
- To put a literal comma in a match, escape it as `\,`. To put a literal semicolon in a match, escape it as `\;`.
- Process Lasso lowercases most lists when it saves them.
- The *match* in each entry accepts the full [process matching](process-matching.md) syntax: wildcards, pathnames, command lines, and so on.

### Affinity Syntax

CPU affinities are written as decimal CPU numbers starting at 0. A range is written with a dash, and items are separated with semicolons: `0-3;6;8-11`.

- `all` means every CPU.
- On systems with more than 64 logical processors, prefix the processor group number and a slash: `1/0-7`.
- CPU Sets use one group affinity per parenthesized item: `(0/0-3)(1/4-7)`.

### Priority Values

| Kind | Values |
| --- | --- |
| CPU priority class (by name) | `real time`, `high`, `above normal`, `normal`, `below normal`, `idle` |
| CPU priority class (Win32 constant) | `0x100` real time, `0x80` high, `0x8000` above normal, `0x20` normal, `0x4000` below normal, `0x40` idle |
| I/O priority | `0` very low, `1` low, `2` normal, `3` high, `4` critical |
| Memory priority | `0` lowest, `1` very low, `2` low, `3` medium, `4` below normal, `5` normal |
| GPU priority | `0` idle, `1` below normal, `2` normal, `3` above normal, `4` high, `5` real time |
| GPU adapter preference | `0` let Windows decide, `1` power saving, `2` high performance |

## Sample Configuration File

This is a shortened example. Process Lasso writes every key it uses, without blank lines between groups; blank lines are allowed when you edit by hand.

```
[OutOfControlProcessRestraint]
OocOn=true
TotalProcessorUsageBeforeRestraint=70
PerProcessUsageBeforeRestraint=10
TimeOverQuotaBeforeRestraint=900
PerProcessUsageForRestore=3
MinimumTimeOfRestraint=4200
MaximumTimeOfRestraint=240000
ExcludeServices=true
OocExclusions=

[GUI]
ShowGraphCPU=true
GPUCollectMode=0

[Performance]
UpdateSpeedGUI=1000
UpdateSpeedCore=1000
ForcedMode=false

[ProcessDefaults]
DefaultPriorities=backup*.exe,below normal,game.exe,high
DefaultAffinitiesEx=render.exe,0,0-7
DefaultIOPriorities=indexer.exe,1

[ProcessAllowances]
DisallowedProcesses=badapp.exe
InstanceLimitedProcesses=notepad.exe;2

[AdvancedRules]
WatchdogRules2=leaky.exe;0;1;2048.00;30000;0;0;1;-;-;-;-
```

## Groups Overview

| Group | Contents |
| --- | --- |
| [Administration](ini-config.md#group-administration) | Config version |
| [OutOfControlProcessRestraint](ini-config.md#group-outofcontrolprocessrestraint) | [ProBalance](../algorithms/probalance.md) |
| [GUI](ini-config.md#group-gui) | Graph and window appearance |
| [GPUAdapters](ini-config.md#group-gpuadapters) | Which GPU adapters the graph shows |
| [Advanced](ini-config.md#group-advanced) | Automatic updates |
| [Performance](ini-config.md#group-performance) | General behavior, refresh rates, Forced Mode |
| [Sampling](ini-config.md#group-sampling) | Periodic CSV snapshots of processes |
| [ForegroundBoosting](ini-config.md#group-foregroundboosting) | [Foreground Boosting](../rules/foreground-boosting.md) |
| [SystemTrayIcon](ini-config.md#group-systemtrayicon) | Tray icon appearance |
| [Logging](ini-config.md#group-logging) | Which events are logged |
| [MemoryManagement](ini-config.md#group-memorymanagement) | [SmartTrim](../algorithms/smarttrim.md) |
| [SysTrayBalloons](ini-config.md#group-systrayballoons) | Tray notifications |
| [ProcessAllowances](ini-config.md#group-processallowances) | Disallowed processes, instance limits, throttles, CPU Limiter, Startup Boost, Efficiency Mode |
| [ProcessDefaults](ini-config.md#group-processdefaults) | Priority, affinity, CPU Sets, Keep Running and power profile rules |
| [AdvancedRules](ini-config.md#group-advancedrules) | Watchdog, Processor Group Extender |
| [GamingMode](ini-config.md#group-gamingmode) | [Performance Mode](../algorithms/performance-mode.md) |
| [PowerManagement](ini-config.md#group-powermanagement) | Startup power plan, anti-sleep processes |
| [PowerSaver](ini-config.md#group-powersaver) | [IdleSaver](../power/idlesaver.md) |
| [LoadBasedPowerSwitcher](ini-config.md#group-loadbasedpowerswitcher) | [Load-Based Profile Switching](../power/load-based-switching.md) |

## Keys

Boolean keys accept `true` or `false` (or the other [boolean spellings](ini-config.md#editing-rules)). Times are in milliseconds unless the key says otherwise.

<a id="group-administration"></a>

### Administration

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| Version | number |  | The version of Process Lasso that last wrote the file. Informational only; it is never read. |

<a id="group-outofcontrolprocessrestraint"></a>

### OutOfControlProcessRestraint

These keys configure [ProBalance](../algorithms/probalance.md).

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| OocOn | boolean | varies | Turns ProBalance on or off. |
| TotalProcessorUsageBeforeRestraint | 1-100 | varies | Total system CPU % that must be reached before any process is restrained. |
| PerProcessUsageBeforeRestraint | 1-100 | varies | CPU % a process must use before it is restrained. |
| TimeOverQuotaBeforeRestraint | ms | varies | How long a process must stay above the per-process threshold before it is restrained. |
| PerProcessUsageForRestore | 1-100 | varies | CPU % a restrained process must drop below to be restored. |
| MinimumTimeOfRestraint | ms | varies | The minimum time a process stays restrained. |
| MaximumTimeOfRestraint | ms | varies | After this long, a restraint ends and the process is restrained again only if it still qualifies. `0` disables the limit. |
| TameOnlyNormal | boolean | true | Only restrain processes running at normal priority. |
| LowerToIdleInsteadOfBelowNormal | boolean | false | Lower restrained processes to idle priority instead of below normal. |
| DoNotLowerPriorityClass | boolean | false | Don't change the priority class of restrained processes. Use with an affinity or Efficiency Mode restraint. |
| LowerIOPriorityDuringRestraint | boolean | false | Also lower the I/O priority of restrained processes. |
| RestrainByAffinity | boolean | false | Also restrain by changing CPU affinity. |
| RestraintAffinity | [affinity](ini-config.md#affinity-syntax) or `random` | empty | The affinity applied when RestrainByAffinity is on. |
| ProBalanceDropOneRandomCore | boolean | false | Instead of using RestraintAffinity, remove one random core from the process's affinity. |
| DoNotAdjustAffinityIfCustomized | boolean | true | Don't change the affinity of processes whose affinity was already customized. |
| UseEfficiencyMode | boolean | false | Also restrain processes by putting them in [Efficiency Mode](../rules/efficiency-mode.md). |
| OocDisableCoreParkingWhileIn | boolean | false | Disable core parking while any process is restrained. |
| ExcludeForegroundProcesses2 | boolean | varies | Never restrain the foreground process. |
| ExcludeChildrenOfForeground | boolean | true | Never restrain children of the foreground process. |
| ExcludeServices | boolean | true | Don't restrain Windows services. |
| DisableProBalanceWhenSysIdle | boolean | false | Pause ProBalance while the user is idle. |
| DisableProBalanceIfSysIdleThisManyMS | ms | 30000 | How long the user must be idle before ProBalance pauses. |
| OocExclusions | match list | empty | Processes ProBalance never restrains. |
| OocHardCodedExclusionOverrides | match list | empty | Built-in exclusions that you've overridden, so ProBalance may restrain those processes. |
| MatchExclusionsByPathnameToo | boolean | false | Match OocExclusions against full pathnames, not just process names. |
| PlaySoundOnRestraint | boolean | false | Play a sound when a process is restrained. |
| PlaySoundOnRestore | boolean | false | Play a sound when a process is restored. |
| PlayOnRestraint | file path | Windows sound | The `.wav` file played on restraint. |
| PlayOnRestore | file path | Windows sound | The `.wav` file played on restore. |
| ChangeTrayIconOnRestraint | boolean | true | Change the tray icon while a process is restrained. |

<a id="group-gui"></a>

### GUI

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| ClearLogAtExit | boolean | false | Clear the log when the GUI exits. |
| ShowCPUCoreUtilGraphs | boolean | true | Show the per-core utilization panel. |
| ShowGraphLegend | boolean | true | Show the graph legend. |
| ShowGraphCPU | boolean | true | Plot CPU utilization. |
| ShowGraphResponsiveness | boolean | true | Plot system responsiveness. |
| ShowGraphMemoryLoad | boolean | true | Plot memory load. |
| ShowGraphProBalanceEvents | boolean | true | Mark ProBalance restraints on the graph. |
| ShowGraphSelectedProcessesCPUHistory | boolean | true | Plot the CPU history of the selected processes. |
| ShowGraphGPU | boolean | true | Plot GPU utilization. |
| GraphGPUShowAllLines | boolean | false | Draw a separate line for each GPU adapter. |
| GraphGPUCombinedWidget | boolean | false | Show all GPUs in one combined widget. |
| GPUCollectMode | `0` auto, `1` all adapters, `2` visible adapters only | 0 | Which GPU adapters to collect data from. |
| GraphAntiAliasing | boolean | true | Anti-alias graph lines. |
| GraphShowTooltips | boolean | true | Show tooltips when hovering over the graph. |
| ProBalanceCountersOnGraph | boolean | true | Show the ProBalance counters over the graph. |
| ShowGraphLicenseName | boolean | false | Show the licensee's name on the graph. |
| ShowPowerProfile | boolean | true | Show the active power profile. |
| ShowCPUUtilityAsPrimary | boolean | true | Graph CPU *utility* (which accounts for clock frequency, like Task Manager) rather than CPU *time*. |

The *show process icons* setting is stored in the registry, not the INI file.

<a id="group-gpuadapters"></a>

### GPUAdapters

This group holds one `adapter=true|false` entry per GPU adapter, recording whether the graph shows that adapter. The GUI writes these entries.

<a id="group-advanced"></a>

### Advanced

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| AutomaticUpdate | boolean | false | Install updates automatically. |

<a id="group-performance"></a>

### Performance

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| UpdateSpeedGUI | `0` (paused), `250`, `500`, `1000`, `2000`, `5000`, `10000` | 1000 | GUI refresh interval, in ms. Other values revert to 1000. |
| UpdateSpeedCore | `10`, `50`, `100`, `250`, `500`, `1000`, `2000`, `5000`, `10000` | 1000 | Process Governor refresh interval, in ms. Lower values react faster but use more CPU. |
| ForcedMode | boolean | false | Continuously re-apply rules. See [Forced Mode](global-options.md#forced_mode). |
| ManageOnlyCurrentUser | boolean | false | Only manage processes belonging to the current user. |
| ExitOnCloseWindow | boolean | false | Exit the GUI when its window closes, instead of minimizing to the tray. |
| SoundsOff | boolean | true | Turn off all sounds. |
| GracefulWaitTimeInMs | ms | 5000 | How long to wait for an application to close gracefully before it is terminated. |
| IgnoreProblematicProcesses | boolean | false | Hide processes that Process Lasso can't access, such as protected system processes, from the process list. |
| AllowBlacklistedProcesses | boolean | false | Apply rules even to the critical system processes that Process Lasso normally leaves alone. Not recommended. |
| IgnoreSuspendedProcesses | boolean | false | Hide suspended processes. |
| RecentlyTerminatedViewExclusions | match list | empty | Processes left out of the recently terminated view. |
| SetTimerResolutionAtStartup | 100-ns units | 0 | System timer resolution to set at startup; for example, `5000` is 0.5 ms. `0` means don't set it. See [System Timer Resolution](../rules/timer-resolution.md). |
| DefaultsLevel | number |  | Internal: the ProBalance defaults version. Process Lasso uses it to offer a reset after the defaults change. Don't edit. |

<a id="group-sampling"></a>

### Sampling

When sampling is enabled, Process Lasso periodically writes a CSV snapshot of the matching processes.

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| SamplingEnabled | boolean | false | Turns sampling on or off. |
| SamplingIntervalSeconds | seconds | 900 | Time between snapshots. |
| SamplingOutputPath | file path | empty | Where to write the CSV. It may contain `%yyyy%`, `%MM%`, `%dd%`, `%hh%`, `%mm%` and `%ss%`, which are filled in from the current UTC time. |
| SamplingIncludePattern | `;`-separated wildcards | `*` | Process names to include. |
| SamplingExcludePattern | `;`-separated wildcards | empty | Process names to exclude. |

<a id="group-foregroundboosting"></a>

### ForegroundBoosting

See [Foreground Boosting](../rules/foreground-boosting.md).

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| BoostForegroundProcess | boolean | false | Turns foreground boosting on or off. |
| ForegroundBoostPriorityClass | [Win32 priority constant](ini-config.md#priority-values) | 0x8000 | The priority class given to the foreground process. Accepts hex (`0x`) or decimal. |
| BoostOnlyNormal | boolean | true | Only boost processes running at normal priority. |
| ForegroundBoostGPU | [GPU priority](ini-config.md#priority-values), or `-1` | -1 | The GPU priority given to the foreground process. `-1` means don't change GPU priority. |
| BoostOnlyNormalGPU | boolean | true | Only GPU-boost processes running at normal GPU priority. |
| ForegroundBoostExclusions | match list | empty | Processes never boosted. |

<a id="group-systemtrayicon"></a>

### SystemTrayIcon

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| UseStaticIcon | boolean | false | Use a static tray icon instead of the animated graph icon. |
| ShowResponsivnessInTrayInsteadOfProcessorUsage | boolean | false | Show responsiveness in the tray icon instead of CPU usage. |

<a id="group-logging"></a>

### Logging

See [Log Viewer & Logging](../interface/logging.md).

| Key | Default | Logs |
| --- | --- | --- |
| LogDisable | false | Turns all logging off. |
| IncludeCommandLines | false | Include process command lines in log entries. |
| LogProcessExecutions | false | Process starts |
| LogProcessTerminations | false | Process exits |
| LogProcessesDisallowed | true | Terminations of disallowed processes |
| LogInstanceLimitTerminations | true | Terminations caused by instance count limits |
| LogDefaultPriorityAdjustments | true | Priority rule actions |
| LogDefaultAffinityAdjustments | true | Affinity rule actions |
| LogProBalanceBegin | true | ProBalance restraints |
| LogProBalanceEnd | true | ProBalance restorations |
| LogProBalanceParkingChanges | true | ProBalance core parking changes |
| LogPowerProfileChanges | true | Power profile changes |
| LogSmartTrim | true | SmartTrim actions |
| LogCPULimiter | true | CPU Limiter actions |
| LogStartupBoostActions | true | Startup Boost actions |
| LogEfficiencyMode | true | Efficiency Mode changes |
| LogGroupExtender | true | Processor Group Extender actions |
| LogCPUSets | true | CPU Set changes |

<a id="group-memorymanagement"></a>

### MemoryManagement

See [SmartTrim](../algorithms/smarttrim.md).

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| SmartTrimIsEnabled | boolean | false | Turns SmartTrim on or off. |
| SmartTrimWorkingSetTrims | boolean | false | Trim process working sets. |
| SmartTrimClearStandbyList | boolean | false | Clear the system standby list. |
| SmartTrimClearFileCache | boolean | false | Clear the system file cache. |
| ClearStandbyFreeRAMThresholdMB | MB | 1024 | Only clear the standby list when free RAM is below this amount. |
| ClearStandbyOnlyInPerfMode | boolean | true | Only clear the standby list during Performance Mode. |
| SmartTrimAutoMinimumRAMLoad | % | 65 | SmartTrim only acts when system memory load is at or above this percentage. |
| MinimumProcessWSSInMb | MB | 196 | Only trim processes whose working set is larger than this. |
| SmartTrimIntervalMins | minutes | 15 | Minimum time between trims. |
| SmartTrimExclusions | match list | empty | Processes never trimmed. |
| SmartTrimLogNoAction | boolean | true | Also log when SmartTrim checks but takes no action. |

<a id="group-systrayballoons"></a>

### SysTrayBalloons

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| EnableSystemTrayNotification | boolean | false | Show tray notifications. |
| BalloonTipDuration | ms | 10000 | How long notifications are shown. Windows may enforce its own limits. |
| ShowBalloonsForOocPriorityRestoration | boolean | false | Also notify when ProBalance restores a process. |

<a id="group-processallowances"></a>

### ProcessAllowances

| Key | Format | Description |
| --- | --- | --- |
| DisallowedProcesses | `match,match,...` | Processes that are terminated when they start. See [Auto-Terminate](../rules/auto-terminate.md). |
| AllowedProcesses | `match,match,...` | Exceptions to DisallowedProcesses. For example, if `notepad*.exe` is disallowed and `notepad1.exe` is allowed, `notepad1.exe` runs but `notepad2.exe` doesn't. |
| InstanceLimitedProcesses | `match;max,...` | The maximum number of instances of a process. See [Instance Count Limits](../rules/instance-limits.md). |
| ApplyInstanceCountLimitsToAllUsers | boolean (default false) | Count instances across all user sessions, not just per session. |
| InstanceManagedCPUAffinities | `match;algorithm;cores;threshold;reserved;smt;random,...` | [Instance Balancer](../algorithms/instance-balancer.md) rules. *algorithm*: `0` spread evenly, `1` set number of cores per instance, `2` NUMA node. *cores*: cores per instance, used by algorithms 1 and 2. *threshold*: CPU % an instance must use before it is balanced. *reserved*: number of cores, starting at CPU 0, left unused. *smt*: `y` to avoid placing instances on SMT siblings. *random*: `y` to randomize core assignment. |
| ProcessThrottles | `match;level,...` | [Hard-Throttling](../algorithms/hard-throttling.md) rules. *level*: `1` lowest, `3` low, `5` middle, `10` high, `20` highest. |
| OneTimeProcessThrottles | `match;pid;level,...` | Throttles applied to one running process ID only. These are managed by the GUI. |
| CPULimitRules | `match;cpu%;over_ms;cores;for_ms,...` | [CPU Limiter](../algorithms/cpu-limiter.md) rules. When the process uses at least *cpu%* for *over\_ms*, remove *cores* cores from its affinity for *for\_ms*. |
| StartupBoostRules | `match;priority;seconds;efficiency,...` | [Startup Boost](../rules/startup-boost.md) rules. *priority*: a priority class name. *seconds*: how long the boost lasts. *efficiency*: `1` to keep the process out of Efficiency Mode during the boost, otherwise `0`. |
| EfficiencyMode | `match,mode,match,mode,...` | [Efficiency Mode](../rules/efficiency-mode.md) rules. *mode*: `1` on, `0` off. |

<a id="group-processdefaults"></a>

### ProcessDefaults

| Key | Format | Description |
| --- | --- | --- |
| DefaultPriorities | `match,priority,match,priority,...` | CPU priority class rules, using [priority class names](ini-config.md#priority-values). See [Priorities](../rules/priorities.md). |
| DefaultIOPriorities | `match,value,...` | [I/O priority](ini-config.md#priority-values) rules. |
| DefaultMemoryPriorities | `match,value,...` | [Memory priority](ini-config.md#priority-values) rules. |
| DefaultGPUPriorities | `match,value,...` | [GPU priority](ini-config.md#priority-values) rules. |
| DefaultGPUAdapterPreferences | `match,value,...` | [GPU adapter preference](ini-config.md#priority-values) rules. |
| ManageWindowsGpuPreferences | boolean (default true) | Keep GPU adapter preference rules synchronized with Windows' per-app graphics settings in the registry. |
| DefaultAffinitiesEx | `match,delay_ms,affinity,...` | [CPU affinity](../rules/cpu-affinities.md) rules. *delay\_ms* delays applying the affinity after the process starts; use `0` for no delay. *affinity* uses the [affinity syntax](ini-config.md#affinity-syntax). |
| CPUSets | `match,sets,...` | [CPU Set](../rules/cpu-sets.md) rules. *sets* uses the parenthesized form of the [affinity syntax](ini-config.md#affinity-syntax). |
| NamedAffinities | `name,affinity,...` | Saved affinity presets that appear in the affinity menus. |
| ThreadPriorityBoosts | `match;value,...` | Windows dynamic thread priority boost. *value*: `0` disabled, `1` enabled. See [Thread Boost](../rules/priorities.md#boost). |
| KeepRunningProcessesEx | `match;command_line;;elevate,...` | [Keep Running](../rules/keep-running.md) rules. The third field is reserved; leave it empty. *elevate*: `true` or `false`. |
| DefaultPowerSchemes | `match;power plan name,...` | [Application Power Profile](../power/power-profiles.md) rules, by power plan name. |
| MatchWildcardsToPathnames | boolean (default true) | Match rules against full pathnames as well as process names. See [Process Matching](process-matching.md). |
| MatchOnCommandLine | boolean (default false) | Match rules against command lines. |

Rules set to *Enforce by Windows Registry* are stored in the registry, not the INI file. See [Priorities](../rules/priorities.md).

<a id="group-advancedrules"></a>

### AdvancedRules

| Key | Format | Description |
| --- | --- | --- |
| WatchdogRules2 | see [below](ini-config.md#documentation-of-watchdogrules) | [Process Watchdog](../rules/watchdog.md) rules. |
| DivideCPUPercentThresholdsBySystemCPUCount | boolean (default false) | Scale watchdog CPU thresholds by the number of CPUs. |
| ProcessorGroupExtended | `match,match,...` | Processes handled by the [Processor Group Extender](../algorithms/group-extender.md). |
| ProhibitInternetExplorerExceptWhenAny | `match,match,...` | Internet Explorer (`iexplore.exe`) can only run while one of these processes is running. |

<a id="group-gamingmode"></a>

### GamingMode

See [Performance Mode](../algorithms/performance-mode.md).

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| GamingModeEnabled | boolean | false | Performance Mode is on. |
| GamingChangePowerPlan | boolean | true | Switch power plans when Performance Mode starts. |
| TargetPowerPlan | power plan name | Bitsum Highest Performance | The plan to switch to. |
| GamingModeEngageForSteam | boolean | false | Start Performance Mode automatically for Steam games. |
| AutomaticGamingModeProcessPaths | `match,match,...` | empty | Processes that start Performance Mode automatically. |
| AutomaticGamingModeUserExclusions | `match,match,...` | empty | Processes that never start Performance Mode automatically. |

<a id="group-powermanagement"></a>

### PowerManagement

| Key | Values | Description |
| --- | --- | --- |
| StartWithPowerPlan | power plan name | The power plan to activate when Process Lasso starts. Empty means don't change it. |
| Display | `match,match,...` | Processes that keep the display awake while they run. See [Anti-Sleep Processes](../rules/anti-sleep.md). |
| PC | `match,match,...` | Processes that keep the PC awake while they run. |

<a id="group-powersaver"></a>

### PowerSaver

See [IdleSaver](../power/idlesaver.md).

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| EnergySaverEnabled | boolean | false | Turns IdleSaver on or off. |
| PowerSaver\_IdleTime | seconds | 300 | How long the user must be idle before IdleSaver switches plans. |
| PowerSaver\_TargetGUID | power plan name |  | The plan to use while idle. Despite the key name, the value is the plan's name, not its GUID. |
| EnergySaverForceActivePowerProfile | boolean | false | While the user is active, keep EnergySaverUpPowerProfileName in effect. |
| EnergySaverUpPowerProfileName | power plan name | empty | The plan to use when the user returns. |
| DisableEnergySaverDuringGamingMode | boolean | true | Don't switch plans during Performance Mode. |
| EnergySaverUseCPUThreshold | boolean | false | Only consider the system idle when CPU use is below EnergySaverCPUThreshold. |
| EnergySaverCPUThreshold | % (decimal allowed) | 5.00 | The CPU threshold for idle detection. |
| PowerSaver\_Exclusions | `match,match,...` | empty | Processes that prevent IdleSaver from engaging while they run. |
| EnergySaverEvents | boolean | true | Log IdleSaver events. |

<a id="group-loadbasedpowerswitcher"></a>

### LoadBasedPowerSwitcher

See [Load-Based Profile Switching](../power/load-based-switching.md).

| Key | Values | Default | Description |
| --- | --- | --- | --- |
| LoadBasedPowerSwitcherEnabled | boolean | false | Turns load-based switching on or off. |
| LoadBasedPowerSwitcherLowPowerProfileName | power plan name |  | The plan used under light load. |
| LoadBasedPowerSwitcherHighPowerProfileName | power plan name |  | The plan used under heavy load. |
| LoadBasedPowerSwitcherLowCPULoadThreshold | % (decimal allowed) | 10.00 | Below this CPU load, switch to the low plan. |
| LoadBasedPowerSwitcherHighCPULoadThreshold | % (decimal allowed) | 50.00 | Above this CPU load, switch to the high plan. Keep it above the low threshold. |
| LoadBasedPowerSwitcherMinimumTimeInPowerPlanMs | ms | 5000 | Minimum time in a plan before switching again. |
| LoadBasedPowerSwitcherAveragingWindowSamples | 1-60 | 5 | Number of samples the CPU load is averaged over. |
| LoadBasedPowerSwitcherDeferLowPlan | boolean | true | Only manage the high plan: when load drops, restore whatever plan was active before the switch up, instead of activating the low plan. |
| LoadBasedPowerSwitcherLoggingEnabled | boolean | true | Log plan switches. |

## Documentation of WatchdogRules

[Process Watchdog](../rules/watchdog.md) rules are stored in the `WatchdogRules2` key. Rules are separated by commas, and each rule has 12 semicolon-separated fields. A field written as `-` is empty.

```
WatchdogRules2=match;action;metric;threshold;duration;action_value;metric_detail;compare;launch_path;launch_args;-;-
```

| # | Field | Values |
| --- | --- | --- |
| 1 | match | The process to watch, in [process matching](process-matching.md) syntax. Escape commas as `\,`. |
| 2 | action | `0` terminate, `1` restart, `2` change CPU affinity, `3` trim virtual memory, `4` set CPU priority, `5` set I/O priority, `6` stop processing further rules, `7` log only, `8` run a command |
| 3 | metric | `0` CPU, `1` memory |
| 4 | threshold | CPU %, or memory in MB. Decimals are allowed. |
| 5 | duration | How long the process must exceed (or fall below) the threshold before the action fires, in ms. |
| 6 | action\_value | Action 2: affinity as a decimal bitmask. Action 4: a [Win32 priority constant](ini-config.md#priority-values), in decimal. Action 5: an [I/O priority](ini-config.md#priority-values). Otherwise `0`. |
| 7 | metric\_detail | For memory rules: `0` working set, `1` commit charge (private bytes), `2` total virtual memory, `3` any memory metric. `0` for CPU rules. |
| 8 | compare | `1` greater than, `2` less than. `0` means greater than. |
| 9 | launch\_path | The program to run, for action 8. Otherwise `-`. |
| 10 | launch\_args | Command-line arguments, for action 8. Otherwise `-`. |
| 11-12 | reserved | Always `-`. |

**Example:** restart `leaky.exe` when its commit charge stays above 2 GB for 30 seconds:

```
WatchdogRules2=leaky.exe;1;1;2048.00;30000;0;1;1;-;-;-;-
```

Older versions used the keys `WatchdogRules` and `OverloadProcessActions`. Current versions ignore both, so recreate those rules in `WatchdogRules2` or in the GUI.

## Legacy Keys

When Process Lasso loads an older configuration, it still reads the keys below and migrates them. On the next save they are written under their new names and the old keys are removed.

| Old key | Replaced by |
| --- | --- |
| DefaultAffinities | DefaultAffinitiesEx (merged with it, using a delay of 0) |
| DefaultPowerSchemesEx | DefaultPowerSchemes (the new key wins for duplicate processes) |
| KeepRunningProcesses | KeepRunningProcessesEx (migrated rules are elevated) |
| DisableThreadPriorityBoost, DisableThreadPriorityBoostBoost | ThreadPriorityBoosts (entries are migrated with a value of 0) |
| ExcludeForegroundProcesses | ExcludeForegroundProcesses2 (the new key wins) |
| RoundRobinAffinitySelection | ProBalanceDropOneRandomCore |
| AllowDisplaysPreventPC | PC |

These old keys are no longer read at all: `UpdateSpeed`, `CloseApplicationTimeoutSeconds`, `LogAllProcessesExecuted`, `LogOutOfControlProcessesRestrained`, `LogOutOfControlProcessesRestored2`, `HideGraph`, `ShowThreadsAndModulesView`, `WatchdogRules` and `OverloadProcessActions`.

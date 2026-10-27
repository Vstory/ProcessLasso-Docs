<!-- source: https://bitsum.com/apps/process-lasso/docs/interface/rules-column/ -->

# The Process Lasso Rules Column

#### Rules

The Rules column in the process list provides a shorthand notation of rules set for each process. Hover over the Rules column header for a quick legend.

Format: `[E|e][+|-][S][^][_][X][L][W][g][K][d][D][x][t][f][ic|ih|in|il|ib][(GPU..)][R|H|A|N|B|I][p][< to <<<<][affinity][(CPU sets)][M0-M7][#n]`

Symbols appear in the order listed.

| Character(s) | Meaning |
| --- | --- |
| E | Efficiency Mode ON |
| e | Efficiency Mode OFF |
| + | Thread priority boost rule: enabled |
| – | Thread priority boost rule: disabled |
| S | Startup Boost rule |
| ^ | Extended across processor groups (Group Extender) |
| \_ | Instance Balancer rule |
| X | Excluded from ProBalance restraint |
| L | CPU Limiter rule |
| W | A watchdog rule is set |
| g | Classified as a game (induces Performance Mode) |
| K | Keep running (restart if terminated) |
| d | Prevents PC sleep while running |
| D | Prevents display sleep while running |
| x | Excluded from foreground boosting |
| t | Excluded from SmartTrim |
| f | Excluded from IdleSaver (IdleSaver won't engage while this process is running) |
| ic | I/O priority class: Critical |
| ih | I/O priority class: High |
| in | I/O priority class: Normal |
| il | I/O priority class: Low |
| ib | I/O priority class: Very Low (background) |
| (GPU..) | GPU rules, described below |
| R | Priority class: Real time |
| H | Priority class: High |
| A | Priority class: Above normal |
| N | Priority class: Normal |
| B | Priority class: Below normal |
| I | Priority class: Idle |
| p | Switches to a specific power plan while running |
| < | Hard throttle: lowest |
| << | Hard throttle: low |
| <<< | Hard throttle: moderate |
| <<<< | Hard throttle: high |
| 0,1,.. | CPU affinity (list of CPU indices) |
| (0,1,..) | CPU sets, shown in parentheses |
| M0-M7 | Default memory priority (0 to 7) |
| #n | Instance count limit of n, e.g. #2 for a limit of 2 |

## GPU Rules

When a GPU adapter preference and/or GPU scheduling priority rule is set, it is shown in parentheses after the `GPU` prefix. The adapter preference symbol comes first, followed by the scheduling priority code, e.g. `(GPU+H)` for high-performance adapter with High scheduling priority.

| Symbol | Adapter preference |
| --- | --- |
| + | High performance |
| – | Power saving |
| / | System default |

| Code | GPU scheduling priority |
| --- | --- |
| RT | Real time |
| H | High |
| AN | Above normal |
| N | Normal |
| BN | Below normal |
| I | Idle |

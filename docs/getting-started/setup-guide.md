<!-- source: https://bitsum.com/apps/process-lasso/docs/getting-started/setup-guide/ -->

# Process Lasso Settings: How to Set It Up (and the Best Settings for Gaming)

Process Lasso works well with its default settings: Install it and [ProBalance](https://bitsum.com/how-probalance-works/) starts keeping Windows responsive right away. This guide covers the few settings worth changing, and the best settings for gaming. It is current for the latest Process Lasso release.

[Download Process Lasso](https://bitsum.com/download-process-lasso/)

## Set Up Process Lasso in Five Steps

1. **Install it and keep the defaults.** ProBalance is on by default and needs no tuning. Most people never change anything else.
2. **Mark your most important programs for Performance Mode.** Right-click each one in the process list and choose *Induce Performance Mode*. While any of them runs, Process Lasso switches to the Bitsum Highest Performance power plan. Only mark the programs that matter most. See [Performance Mode](https://bitsum.com/bhp/).
3. **On Intel CPUs with P-cores and E-cores, keep critical programs off the E-cores.** Right-click the program and choose *Efficiency Mode / Always / Off*. For a stronger preference, also choose *CPU Sets / Always* and select *P-Cores*. See [Efficiency Mode](../rules/efficiency-mode.md) and [CPU Sets](../rules/cpu-sets.md), and [Intel Hybrid CPUs: Scheduling on P-Cores and E-Cores](https://bitsum.com/intel-hybrid-p-cores-e-cores/) for which CPUs this applies to.
4. **On AMD CPUs with more than one CCD, keep games on one CCD.** Right-click the game, choose *CPU Sets / Always*, and select a single CCD (*CCD0* or *CCD1*). On Ryzen X3D models with two CCDs, the buttons show which CCD has the 3D V-Cache (*CCD0: cache*, usually). See [AMD Ryzen X3D CPUs: Keeping Games on the 3D V-Cache CCD](https://bitsum.com/amd-x3d-ccd-affinity/).
5. **Check the log before you exclude anything.** If you think ProBalance is acting on a program at the wrong time, look for it in the log or ProBalance Insights first. If it is not there, ProBalance has not touched it. If it is, right-click the program and choose *Exclude from ProBalance*.

## Best Process Lasso Settings for Gaming

For most games, the recipe is short:

- **Leave ProBalance on.** The game you are playing is the foreground process, which ProBalance leaves alone by default, while it keeps background tasks from stealing CPU time.
- **Induce Performance Mode for the game,** so the CPU stays at full readiness while you play. If you would rather have this happen for every game you launch, turn on *Options / Power / Performance Mode / Enable Automatic Detection (e.g. Steam)*. It is off by default.
- **Keep the game on the right cores** with the Intel or AMD rule from steps 3 and 4 above.
- **Leave the game's priority alone.** Raising a game to High or Realtime priority rarely helps and can cause stutter or hangs.

### Counter-Strike 2 (CS2)

The CS2 process is `cs2.exe`.

1. Right-click `cs2.exe` and choose *Induce Performance Mode*.
2. Intel hybrid CPUs: Right-click `cs2.exe` and choose *Efficiency Mode / Always / Off*, and optionally *CPU Sets / Always* with *P-Cores* selected.
3. AMD CPUs with two CCDs: Right-click `cs2.exe`, choose *CPU Sets / Always*, and select the 3D V-Cache CCD (usually *CCD0*) or, on non-X3D models, either single CCD.

If the log shows Process Lasso could not change `cs2.exe`, use the launcher method described for Tarkov below.

### Escape from Tarkov

The game process is `EscapeFromTarkov.exe`, started by the BSG Launcher (`BsgLauncher.exe`). Tarkov's anti-cheat may block Process Lasso from changing the game process directly, so set rules where they still apply:

1. Right-click `EscapeFromTarkov.exe` and choose *Induce Performance Mode*. Performance Mode switches the power plan while the game runs, so it does not need to change the game process itself.
2. To keep the game on specific cores, set the rule on the launcher instead: Right-click `BsgLauncher.exe`, choose *CPU Affinity / Always / Select CPU Affinity*, and select the cores (P-cores on Intel hybrid CPUs, or the 3D V-Cache CCD on AMD X3D). Processes inherit their parent's CPU affinity, so the game starts with the same cores without Process Lasso opening it.

See [Working with anti-cheat systems](../help/anti-cheat.md) for more on games that block changes.

## Settings by Feature

- [ProBalance](https://bitsum.com/how-probalance-works/): Keeps Windows responsive when background programs hog the CPU. On by default.
- [Performance Mode](https://bitsum.com/bhp/): Switches to the Bitsum Highest Performance power plan while chosen programs or games run.
- [SmartTrim](https://bitsum.com/smarttrim/): Trims background processes only under real memory pressure. Off by default, with suggested settings for 16 GB and 32 GB systems.
- [CPU Limiter](https://bitsum.com/docs/limiting-cpu-use-with-process-lasso-cpu-limiter/): Puts a hard cap on how much CPU a program can use.
- [IdleSaver](../power/idlesaver.md): Switches to a more conservative power plan when you are away, and [Application Power Profiles](../power/power-profiles.md) pick a power plan per program.

## Avoid Over-Tweaking

Stick to the basics unless you are confident in what an advanced setting does. Use narrowly targeted rules: one rule for the program you care about beats a blanket change to every process. When an optimization helps nearly everyone, it goes into a default feature such as ProBalance, so there is rarely a hidden setting you are missing. You are unlikely to cause lasting problems by experimenting, and every rule can be removed from the same menu that created it.

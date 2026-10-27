# Process Lasso Documentation

**Read online: <https://vstory.github.io/ProcessLasso-Docs/>**

An offline Markdown mirror of the official Process Lasso documentation at <https://bitsum.com/apps/process-lasso/docs/>, published as a static site via GitHub Pages.

Process Lasso is Windows process automation and optimization software by [Bitsum](https://bitsum.com/). It keeps a PC responsive under heavy CPU load with the ProBalance algorithm, and lets you enforce persistent rules such as CPU affinities, priority classes, CPU sets, power profiles, instance limits, and process watchdogs.

## Documentation Index

- [Introduction](docs/index.md)
- [Setup Guide](docs/getting-started/setup-guide.md)
- [How Process Lasso Works](docs/getting-started/how-it-works.md)
- **The Interface**
  - [Main Window](docs/interface/main-window.md)
  - [The Graph](docs/interface/graph.md)
  - [All Processes Tab](docs/interface/all-processes.md)
  - [Active Processes Tab](docs/interface/active-processes.md)
  - [Process Info Columns](docs/interface/columns.md)
  - [The Rules Column](docs/interface/rules-column.md)
  - [Log Viewer & Logging](docs/interface/logging.md)
  - [Keyboard Shortcuts](docs/interface/keyboard-shortcuts.md)
- **Process Rules**
  - [Automation](docs/rules/index.md)
  - [Priorities](docs/rules/priorities.md)
  - [CPU Affinities](docs/rules/cpu-affinities.md)
  - [CPU Sets](docs/rules/cpu-sets.md)
  - [System Reserved CPU Sets](docs/rules/reserved-cpu-sets.md)
  - [Efficiency Mode](docs/rules/efficiency-mode.md)
  - [Instance Count Limits](docs/rules/instance-limits.md)
  - [Keep Running](docs/rules/keep-running.md)
  - [Auto-Terminate](docs/rules/auto-terminate.md)
  - [Process Watchdog](docs/rules/watchdog.md)
  - [Foreground Boosting](docs/rules/foreground-boosting.md)
  - [Startup Boost](docs/rules/startup-boost.md)
  - [System Timer Resolution](docs/rules/timer-resolution.md)
  - [Anti-Sleep Processes](docs/rules/anti-sleep.md)
- **Algorithms**
  - [Overview](docs/algorithms/index.md)
  - [ProBalance](docs/algorithms/probalance.md)
  - [Performance Mode](docs/algorithms/performance-mode.md)
  - [CPU Limiter](docs/algorithms/cpu-limiter.md)
  - [Instance Balancer](docs/algorithms/instance-balancer.md)
  - [Processor Group Extender](docs/algorithms/group-extender.md)
  - [Hard-Throttling](docs/algorithms/hard-throttling.md)
  - [SmartTrim](docs/algorithms/smarttrim.md)
- **Power**
  - [Application Power Profiles](docs/power/power-profiles.md)
  - [IdleSaver](docs/power/idlesaver.md)
  - [Load-Based Profile Switching](docs/power/load-based-switching.md)
  - [Config Profile Switcher](docs/power/config-profile-switcher.md)
- **Tools**
  - [LatencyTest](docs/tools/latencytest.md)
- **Reference**
  - [Command Line Arguments](docs/reference/command-lines.md)
  - [INI Configuration File](docs/reference/ini-config.md)
  - [Rules Import and Export (JSON)](docs/reference/json-format.md)
  - [Process Matching](docs/reference/process-matching.md)
  - [Config and Log Paths](docs/reference/config-paths.md)
  - [Global Options](docs/reference/global-options.md)
- **Deployment**
  - [Overview](docs/deployment/index.md)
  - [Installation](docs/deployment/installation.md)
  - [Licensing](docs/deployment/licensing.md)
  - [Auto-Start Behavior](docs/deployment/auto-start.md)
  - [Config Push / Pull](docs/deployment/config-push-pull.md)
  - [Enterprise Deployment](docs/deployment/enterprise.md)
- **Help**
  - [Anti-Cheat Systems](docs/help/anti-cheat.md)
  - [More Help](docs/help/more-help.md)

## All Pages

[All pages (A-Z)](docs/all-pages.md)

## Simplified Chinese Translation

Every page is also available in Simplified Chinese at <https://vstory.github.io/ProcessLasso-Docs/zh-CN/>; the site header has a language switcher. The sources live in `docs/zh-CN/` and mirror the English page paths one to one.

Translation consistency is checked by a script rather than by eye:

```bash
python3 scripts/check_i18n.py            # readable list on stdout, summary on stderr
python3 scripts/check_i18n.py --json     # machine-readable, for CI
python3 scripts/check_i18n.py --strict   # warnings fail too
python3 scripts/check_i18n.py --selftest # verify the checks themselves
```

It covers page coverage, the `<!-- source: -->` header, heading-count parity, the heading anchors that keep cross-page links alive, relative links and `#fragments` (including the `media/` depth), banned wording, half-width punctuation next to Chinese text, unclosed code fences and table column counts. Upstream defects and the page that is deliberately structured differently are listed with reasons in `scripts/i18n-allow.txt`. CI runs it on every push.

## Get Process Lasso

[Download the latest release](https://bitsum.com/download-process-lasso/) | [How ProBalance works](https://bitsum.com/how-probalance-works/) | [Performance Mode](https://bitsum.com/bhp/) | [SmartTrim](https://bitsum.com/smarttrim/)

## Source and Copyright

Documentation content is copyright Bitsum LLC and was fetched from <https://bitsum.com/apps/process-lasso/docs/> on 2026-10-27 (52 pages). This repository is a personal offline mirror for reading and searching; it claims no rights over the content and adds no changes beyond formatting into Markdown.

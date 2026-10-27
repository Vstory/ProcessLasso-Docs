<!-- source: https://bitsum.com/apps/process-lasso/docs/reference/json-format/ -->

# Rules Import and Export (JSON)

Process Lasso can copy, export and import process rules as JSON. Use it to move rules between machines, share a rule set, or back up rules for a few processes. To copy or deploy an entire configuration, including global options, use the [INI configuration file](ini-config.md) instead.

The [Process Lasso JSON schema is published here](https://bitsum.com/json-schemas/2026-01-17-00/processlasso.schema.json).

## Exporting Rules

- *Menu path: ‘File / Export Rules’*

Select the processes whose rules you want to export. Process Lasso copies the rules to the clipboard, then offers to save them to a `.json` file as well.

To copy the rules of a single process, right-click it and choose **Copy Rules**. This copies every rule that applies to that process, including rules that match it through a wildcard or path.

## Importing Rules

- *Menu path: ‘File / Import Rules’*

If the clipboard holds exported rules, Process Lasso offers to import them. Otherwise, choose a `.json` file. You then select which processes to import rules for.

> **Importing replaces a process's rules**
>
> For each process you import, Process Lasso first removes all of that process's existing rules, then applies the imported ones. Rules for processes you don't import are left unchanged.

To apply copied rules to processes in the list, right-click a process, or several selected processes, and choose **Paste Rules**. Keep Running rules aren't pasted, since they belong to a specific program path. If the clipboard holds rules for more than one process, Paste Rules opens the full import instead.

The **Rules** window (*‘Options / View All Rules’*) has its own Import and Export commands. Importing there adds rules only for processes that aren't already listed, and nothing is saved until you click **OK**.

### When Rules Were Exported on a Different CPU

Exports record the CPU model of the machine that made them. If yours differs, Process Lasso asks before importing, because rules such as CPU affinities and CPU Sets refer to specific cores. Check those rules after importing.

## What's Included

Exports carry every rule type that applies to a single process: CPU, I/O, GPU and memory priorities, GPU adapter preference, CPU affinities and CPU Sets, Efficiency Mode, thread priority boosting, app power profiles, CPU Limiter, Startup Boost, Instance Balancer, instance count limits, the Processor Group Extender, hard throttling, the watchdog, Keep Running, disallowed processes and their exceptions, anti-sleep, Performance Mode, and the ProBalance, SmartTrim, Foreground Boost, IdleSaver and Performance Mode exclusions. The order of rules is kept for the rule types where the first matching rule applies.

Not included:

- Global options, such as ProBalance thresholds or refresh rates.
- Processes you've allowed ProBalance to act on despite its built-in exclusions.
- The Internet Explorer restriction list.

Priority names are always written in English (18.4.1.7 and later), so an export imports into Process Lasso running in any language. Older versions wrote names in their UI language.

## Format

An export is a JSON object with a `ruleSets` array: one rule set per process match, holding only the rules that process has. This example has two rule sets:

```
{
 "$id": "https://bitsum.com/json-schemas/2026-01-17-00/processlasso.schema.json",
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Process Lasso Rules",
 "description": "Rulesets for Process Lasso",
 "cpuModel": "Intel(R) Core(TM) i5-12600K",
 "ruleSets": [
  {
   "processName": "game.exe",
   "priorityClass": "High",
   "priorityClassEnforcedByRegistry": false,
   "cpuAffinity": "0-7",
   "cpuAffinityDelay": 0,
   "probalanceExclusion": true
  },
  {
   "processName": "backup*.exe",
   "priorityClass": "Below Normal",
   "priorityClassEnforcedByRegistry": false,
   "ioPriority": "Very Low",
   "ioPriorityEnforcedByRegistry": false
  }
 ],
 "priorityClassRuleOrder": [ "game.exe", "backup*.exe" ]
}
```

You can write rule files by hand:

- Process Lasso imports a file only when it has a `ruleSets` array and `$schema` has the value shown above. `$id` is optional, but if present it must also have the value shown.
- Each rule set needs a `processName`, which accepts the full [process matching](process-matching.md) syntax. All other fields are optional, including companion fields such as `priorityClassEnforcedByRegistry` and `cpuAffinityDelay`.
- `cpuModel` is optional. Without it, Process Lasso asks before importing, as it does for a different CPU.
- Values use the same formats as the [INI file](ini-config.md), for example `0-3;6` for a CPU affinity. The [schema](https://bitsum.com/json-schemas/2026-01-17-00/processlasso.schema.json) lists every field and its allowed values, and you can check a file against it with any JSON Schema validator.

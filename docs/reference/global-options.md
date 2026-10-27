<!-- source: https://bitsum.com/apps/process-lasso/docs/reference/global-options/ -->

# Global Options

## Forced Mode

- *Menu path: ‘Options / Forced Mode (continuously reapply settings)’*

Forced Mode, available in the Options menu, is a toggle that causes rules to be continuously re-applied to running processes. This can be desirable in the case of a process that changes its own settings. Normally, Process Lasso would make a one-time adjustment to each new instance of a process, but Forced Mode causes it to evaluate whether the target settings (e.g. CPU affinity or priority class) were changed, and re-apply them if so.

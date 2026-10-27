<!-- source: https://bitsum.com/apps/process-lasso/docs/reference/config-paths/ -->

# Config and Log Paths

In the config and log path presented in the second dialog, users can choose to use a centralized network configuration and log store, a per-machine store, or a per-user store.

**Option 1: Centralized config and log** In this mode, all workstation are configured to either (1) use a centralized configuration and log path hosted on a network share OR *(2)* use a machine local configuration and/or log path, but have a centralized INI configuration file pushed out to clients when changed, and the logs pulled from clients periodically. If the INI config path is a network share, it is polled for changes at least once a minute. For local paths, file-system change events are used to get notification of changes, so no polling is required and changes will be picked up instantaneously.

**Option 2: Per-workstation configuration file and log** In this mode, you’d install Process Lasso on each workstation and use a common configuration and log path that every user of the system would access.

**Option 3: Some combination of the above, or an alternate method** In the end, you can utilize Process Lasso just about however you want. You could have workstations launch it from a network share, for instance, without ever having to install Process Lasso on those workstations.

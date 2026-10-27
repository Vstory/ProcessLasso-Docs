<!-- source: https://bitsum.com/apps/process-lasso/docs/getting-started/how-it-works/ -->

# Components of Process Lasso

Process Lasso consists of a core engine and a user interface. The two are separated so that users can completely close the user interface while keeping Process Lasso active, managing processes. The core engine is run as ProcessGovernor.exe, while the user interface is ProcessLasso.exe. Running only the core engine results in memory usage of a mere 1-3MB (typically) and almost no CPU use. When the user interface, ProcessLasso.exe, is launched it automatically launches an instance of the ProcessGovernor.exe core engine if one isn’t already running for the current user, or as a service. When you close the user interface, you are asked whether you want to keep the core engine running or not. By default, each user session has their own instance of ProcessLasso.exe and ProcessGovernor.exe. An alternate popular configuration would be to run the governor as a service and the GUI as-necessary.

| Component | Filename | Description |
| --- | --- | --- |
| Graphical User Interface (GUI) | ProcessLasso.exe | This graphical user interface (GUI) serves the purposes of configuring process rules and features, displaying running processes and recent activity (logs) by the Process Governor service. It also hosts the system tray icon. |
| Core Engine (Governor) | ProcessGovernor.exe | This non-interactive system service, called the Process Governor or ‘core engine’, does the actual work of applying process rules and algorithms. It can run stand-alone without the GUI for minimal resource use. |
| Session Agent | bitsumsessionagent.exe | This tiny process facilitates Process Lasso’s retrieval of select information about each interactive user session, namely the foreground process ID and the last input time (for the idle timer). This data is used by ProBalance and IdleSaver. The Keep Awake and Prevent Sleep functions also rely on this process and will not function properly if it is not running. The bitsumsessionagent.exe process has virtually zero overhead so its startup task should not be disabled. |
| Configuration File | prolasso.ini | This configuration file holds the process rules and options for Process Lasso. The path can be changed via ‘Options / General / Configure Startup…’. |
| Log File | prolasso.log | This log file keeps a record of recent actions. It can be disabled. The path can be changed using ‘Options / General / Configure Startup…’. This file is in a CSV format. |

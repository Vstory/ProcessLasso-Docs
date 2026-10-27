<!-- source: https://bitsum.com/apps/process-lasso/docs/reference/command-lines/ -->

# Command Line Arguments

## Installer

| Switch *(defaults in bold)* | Description | Examples |
| --- | --- | --- |
| /S (case sensitive) | Performs a silent installation, also known as non-interactive or unattended. Since no configuration dialogs will be shown during install, you should compliment this switch with others (listed below) to specify how you would like Process Lasso configured. | ProcessLassoSetup.exe /S |
| /language=[**English**] | This indicates the language to use. If this value is not supplied, it defaults to English. Do not try to use unsupported languages, and be sure your language name is spelled as listed here (i.e. SimpChinese). Alternatively, you can specify the language’s code page number. English (1033) German (1031) Russian (1049) Polish (1045) Italian (1040) Slovenian (1060) Japanese (1041) TradChinese (1028) SimpChinese (2052) …. | ProcessLassoSetup.exe /S /language=English ProcessLassoSetup.exe /S /language=1033  ProcessLassoSetup.exe /S /language=German ProcessLassoSetup.exe /S /language=1031  ProcessLassoSetup.exe /S /language=Slovenian  ProcessLassoSetup.exe /S /language=Italian  ProcessLassoSetup.exe /S /language=SimpChinese |
| /gui\_start\_type=[**all** | current | manual] |
| /governor\_start\_type=[all | current | **service** |
| /logfolder=[folder] | This indicates to use a global log folder for ALL users on the system. By default, each user has his or her own log folder in their respective application data directory. However, it is sometimes desirable to consolidate all log events into a single log folder. Be sure that this log folder is writable by contexts the governor will be running in. If set to run as a normal process, this may mean all users. If set to run as a service, it should be writable by the service user (or SYSTEM user). | ProcessLassoSetup.exe /S /logfolder=c:\systemlogs  ProcessLassoSetup.exe /S /logfolder=c:\systemlogs |
| /configfolder=[folder] | This indicates to use a global configuration folder for ALL users on the system. By default, each user has his or her own configuration in their respective application data directory. However, it is sometimes desirable to use the same configuration for all users, and is required when the governor is run as a service. Be sure that this configuration folder is readable by all user contexts the governor will be running in, and writable by those who you wish to allow configuration changes. | ProcessLassoSetup.exe /S /configfolder=c:\pl\_config  ProcessLassoSetup.exe /S /configfolder=c:\pl\_config |
| /launch\_gui=[**true** | false] | This indicates whether or not to launch the GUI after installation. Even when the GUI is launched, it remains minimized to the system tray. |
| /importconfigfrom=[path] | This indicates to import the configuration from the file you’ve specified. This should be used in conjunction with /configfolder. The file you specify here will be the initial configuration for Process Lasso. You can specify only a folder OR a specific filename here. If you specify only a folder, “prolasso.ini” will simply be appended to the path name. | ProcessLassoSetup.exe /S /configfolder=c:\pl\_config /importconfigfrom=c:\temp  ProcessLassoSetup.exe /S /configfolder=c:\pl\_config /importconfigfrom=c:\temp\my\_default\_config.ini |
| /username=[user] /password=[pass] | When running the core engine as a service (/governor\_start\_type=service), these switches can be used to indicate under which user you should start the service. The user MUST have permission to ‘logon as a service’ (see our [FAQ](https://bitsum.com/process-lasso-faq/) for info on allowing that). If a specific user is not supplied, the core engine will run in the system context. Please remember that the Windows user password is case sensitive. | ProcessLassoSetup.exe /S /governor\_start\_type=service /username=myuser /password=mypass |
| /configpw=[password] | This sets the configuration password. This password is required for by the GUI when a user tries to make a change to the configuration file. Use this parameter without a value to remove any existing password. | ProcessLassoSetup.exe /S /configpw=somepassword |
| /key=[licensekey] | This sets the license key. | ProcessLassoSetup.exe /S /key=1A79A4D60DE6718E8E5B326E338AE533 |
| /keyfile=[keyfile] | This is the absolute path of the key file. Do not use a relative path. | ProcessLassoSetup.exe /S /keyfile=c:\users\admin\downloads\prolasso.key |

## ProcessLasso.exe

Command line arguments for the GUI and core engine are available. You can use them to over-ride the configuration and log paths, but this is not normally necessary or recommended. Changes to the configuration and log paths should instead be performed by the installer (preferred) or the InstallHelper application.

| Switch | Description | Examples |
| --- | --- | --- |
| /ShowWindow | Open the main window after launching. | ProcessLasso.exe /showwindow |
| /ConfigFolder= | Indicates the configuration folder that should be used. It is assumed that ‘prolasso.ini’ will exist in it. If not, it one be created with default values. | ProcessLasso.exe /ConfigFolder=”c:\program files\Process Lasso\config” ProcessLasso.exe /ConfigFolder=c:\config\ ProcessLasso.exe /ConfigFolder=\server1\ProcessLassoConfig\ |
| /LogFolder= | Indicates the folder containing the log files. This folder requires read and write access. | ProcessLasso.exe /LogFolder=\server1\logfolder ProcessLasso.exe /LogFolder=c:\pslogs |
| /NoRaiseExisting | Start a new instance of ProcessLasso.exe only if it is not already running, but do not show the window of existing instance as would be the default behavior. | ProcessLasso.exe /NoRaiseExisting *(NOTE: Use /no\_raise\_existing instead prior to v12.1)* |
| /SetActiveProfile=name | Switch the active configuration profile to the indicated preexisting named profile. This command does not launch Process Lasso, it exits after changing the profile. | ProcessLasso.exe /SetActiveProfile=myprofile |
| /StartWithProfile=name | Switch to configuration profile, then launch Process Lasso. | ProcessLasso.exe /StartWithProfile=myprofile |
| /TrimNow | Signal SmartTrim to take action immediately, as and if configured. | ProcessLasso.exe /TrimNow |
| /ActivateOnly | Activate product with key previously given on installer command line, then exit. | ProcessLasso.exe /ActivateOnly |

## ProcessGovernor.exe

| Switch | Description | Examples |
| --- | --- | --- |
| /ConfigFolder= | Indicates the configuration folder that should be used. It is assumed that ‘prolasso.ini’ will exist in it. If not, it one be created with default values. | ProcessGovernor.exe /ConfigFolder=”c:\program files\Process Lasso\” ProcessGovernor.exe /ConfigFolder=c:\config\ ProcessGovernor.exe /ConfigFolder=\server1\ProcessLassoConfig\ |
| /LogFolder= | Indicates the folder containing the log files. This folder requires read and write access. | ProcessGovernor.exe /LogFolder=\server1\logfolder ProcessGovernor.exe /LogFolder=c:\pslogs |

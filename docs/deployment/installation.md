<!-- source: https://bitsum.com/apps/process-lasso/docs/deployment/installation/ -->

# Installation

Process Lasso’s installer can run from the CLI without interaction. This is done by adding the /S switch to the installer command line. The INI configuration file may need to be precomposed with the desired rules. For that, we recommend installing Process Lasso on a workstation and using the GUI to create the rules. The installation command might look like:

```
ProcessLassoSetup64.exe /S /gui_start_type=current /governor_start_type=service /importconfigfrom=\\somepath\lasso\prolasso.ini
```

Key files for easier product activation or offline use can be requested by contacting Bitsum. They are available to Site and Server Edition licensees. For a full listing of installer command line options, see [here](../reference/command-lines.md#command_line). Alternatively, Process Lasso’s binaries could be directly embedded in your software packages. In that case, after deployment, you’d launch processgovernor.exe with the command line switch /ConfigFolder=xxx. Launching the GUI (processlasso.exe) may not be necessary, depending on your use case. Please [contact us](https://bitsum.com/contact/) if you require guidance on manual configuration.

## Editions and Architecture

Process Lasso ships as three native builds:

| Build | For | Installer file |
| --- | --- | --- |
| 32-bit (x86) | 32-bit Windows | `ProcessLassoSetup.exe` |
| 64-bit (x64) | 64-bit Windows on Intel and AMD | `ProcessLassoSetup64.exe` |
| ARM64 | Windows on ARM (Snapdragon and other ARM64 PCs) | `ProcessLassoSetupARM64.exe` |

Most users never need to choose. The download and the installer select the build that matches your system, and running the wrong 32-bit or 64-bit installer offers to download the correct one. On an ARM64 PC, the native ARM64 build is recommended for the best performance; the 64-bit x64 build also runs there under Windows' built-in emulation, so an existing x64 installation continues to work.

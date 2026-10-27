<!-- source: https://bitsum.com/apps/process-lasso/docs/deployment/enterprise/ -->

# Enterprise Deployment

## In the Enterprise

Process Lasso works wonders on servers. It can prevent a single process from monopolizing the server's CPU resources. We offer
a special Server Edition of Process Lasso, with a 30-day free trial available. See [bitsum.com](https://bitsum.com/) for more information.

Process Lasso can be used on Terminal Servers, web servers, file servers, or more complex network client/server environments.
In fact, it can be used in just about any scenario you can envision. The fact that the core engine is separate from the GUI makes it easy to install
without it being visible to the end user.  You can even run the core engine
as a system service, a feature many network admins will appreciate.

### On a Terminal Server

On a Terminal Server what we recommend is letting the core engine (processgovernor.exe) start for every user that logs in. This
instance of the core engine would manage only that user's processes. This is asked towards the end of install. So, choose to start
the GUI only for you (to reconfigure or view log), then select to start the core engine for all users. In the config dialog that
follows that one, simply tell the core engine to manage only processes in its session (the default setup). This is how Process Lasso
was designed to work, and is how it operates best.

The reason not to run the core engine as a service that manages all users is because it cannot identify which processes are in the foreground
of other user sessions, and therefore the ProBalance algorithm cannot make as informed decisions and may temporarily lower the priority of active foreground
processes - something that isn't usually desirable (though not particularly harmful in most cases). If you wanted to set it up this way anyway, you could exclude some common
applications from ProBalance restraint, or 'tone down' ProBalance by raising the quotas in the 'ProBalance Parameters'.

If you are not using ProBalance, and instead using other features, then this is not a worry and you can use either method.

You have the option of allowing each user to have his or her own configuration file and log folder, or have all users share the same
ones. This option is presented to you towards the end of install, at the same time you are asked about startup configuration.

### On Distributed Networks (with Workstations and Servers)

Here you have the option of installing Process Lasso on the workstations and server, or just on the server. It is up to you.
You can share a global log and configuration file with a mapped drive or UNC path if you choose. UNC paths are fine so long as the user has
access. In this way a level of centralized management is possible.

### Methods of Deployment

During the install process, towards the end a little config wizard pops up that will ask you questions relevant to how
Process Lasso and its core engine should start. First, know that the core engine is totally in the background and has no visible
presence. The system tray icon is part of the GUI. You have two basic choices:

1. Each user gets their own instance of the silent background core engine when they log in (default, most effective)
2. A single instance of the core engine manages all user processes (less accurate)

The big question is whether you want to use a centralized network configuration
and log store, a per-machine store, or a per-user store.

**Option 1: Centralized configuration and log**

In this mode, all workstation are configured to use the same configuration file
and log folder. These can be on network shares, or can be pushed out to
workstations through alternate methods.

**Option 2: Per-workstation configuration file and log**

In this mode, you'd install Process Lasso on each workstation and use a common
configuration and log path that every user of the workstation would access.

**Option 3: Per-user configuration file and log**

In this mode, you'd install Process Lasso on each workstation and let each user
have their own configuration and log. This is the default behavior of Process
Lasso. If you don't need or want to make changes to the configuration or modify
the log files, this is a good way to run Process Lasso.

**Option 4: Some combination of the above, or an alternate method**

In the end, you can utilize Process Lasso just about however you want. You could
have workstations launch it from a network share, for instance, without ever
having to install Process Lasso on those workstations. The prerequisites to
running Process Lasso are very few. Older systems (XP before SP2) will require Microsoft's
GDIPLUS.DLL to be installed before the Process Lasso GUI can run. However, the
core engine does not require the GDIPLUS library to be present. There are no
other pre-requisites. This makes for simplistic portable use or launching from a network path.

### Service Mode

You can install Process Lasso's core engine, processgovernor, as a service. This option is presented to you
during the install process of Process Lasso Pro. It is also available during silent installs using the command
line switches.

Running the core engine as a service has its advantages as disadvantages. As described above, it has no knowledge of what process is in the foreground
of other user sessions so ProBalance is not nearly as accurate in its actions. This only affects ProBalance though, so is not an issue if you aren't using
ProBalance. Even if you are using ProBalance, it may not be problematic with an exclusion or two and additional tweaking (or maybe it is never a problem).

### Silent Installation

Process Lasso (as of v3.53) now supports completely silent installation. For more information, see the
[command line switches documentation](../reference/command-lines.md#htoc-installer-command-line).

### More Help?

If you have any questions about getting Process Lasso up and running in your
enterprise, please email us at [support@bitsum.com](mailto:support@bitsum.com). Customized solutions are also available.

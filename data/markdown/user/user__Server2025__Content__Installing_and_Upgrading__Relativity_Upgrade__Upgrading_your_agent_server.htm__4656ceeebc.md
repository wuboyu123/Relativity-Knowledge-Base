---
title: "Upgrading your agent server"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Relativity_Upgrade/Upgrading_your_agent_server.htm
collection: user
fetched_at: 2026-06-22T06:03:58+00:00
sha256: f0e4e214f00ac6b4ac63b62e14cfc9ab4c44af4fed1f947a3e2c942bab75c465
---

Upgrading your agent server

# Upgrading your agent server

This section provides the prerequisites and the steps required to upgrade your agent server to a new version of Relativity. For more information, see Pre-installation .

Before you begin upgrading your agent server, confirm that you have upgraded the SQL Server and have started the SQL service.

After you run the installer on at least one agent server, the system begins upgrading individual workspaces. You can now log in to Relativity to monitor workspace upgrades via the Workspace Upgrade queue.

## Agent server upgrade

Contact Customer Support to get a copy of the Relativity installer.

Save the following files to the root directory of any server contributing to the Relativity environment:

- Relativity.exe —the executable file that installs Relativity components determined by the values entered in the RelativityResponse.txt file.

- You must save Relativity.exe on a drive local to the server. Running Relativity.exe from a shared location results in upgrade or installation failure.

- Use Install.bat to proceed with installation. The Relativity.exe file does not open a user interface.

- Install.bat —the code that prompts Relativity.exe to proceed with the installation process. You must edit line 11 of the Install.bat file with the exact name of the Relativity installation file.

```text
 start /wait "" "INSERT EXACT NAME OF RELATIVITY INSTALLATION FILE" /log InstallLog.txt /responsefilepath=RelativityResponse.txt
```

- Run this file from an elevated command line prompt to avoid permission issues.

- You must surround the name of the Relativity installation file with quotation marks.

- RelativityResponse.txt —the text file that determines which components Relativity.exe installs, uninstalls, or upgrades on the server.

Every line in the RelativityResponse.txt file that starts with ### is a comment and meant to provide instruction.

To upgrade the agent server:

Open the RelativityResponse.txt file in a text editor and edit the parameters as follows to upgrade Relativity on the machine that serves the role of the agent server:

The following settings assume that the same machine does not host the agent server that hosts the primary or distributed SQL database servers.

#### Common properties

- INSTALLDIR —enter the installation directory. This is the target directory for all files related to the local installation. This path must be local to the machine and accessible by the server. You can't use unicode special characters for this path.

```text
INSTALLDIR=C:\Program Files\kCura Corporation\Relativity
```

- PRIMARYSQLINSTANCE —enter the primary SQL instance. If you are installing to a cluster, specify the cluster and instance name. If you are installing to a named instance, specify the server and instance name. All features require this input.

```text
PRIMARYSQLINSTANCE=ML12
```

- EDDSDBOPASSWORD —enter the EDDS database object password.

```text
EDDSDBOPASSWORD=MySecretPassword
```

- SERVICEUSERNAME —enter the service username. The Windows login must already exist.

```text
SERVICEUSERNAME=example\exampleusername
```

- SERVICEPASSWORD —enter the service password.

```text
SERVICEPASSWORD=MySecretPassword
```

- USEWINAUTH —set this to one to use Windows authentication for the SQL Server.

```text
USEWINAUTH=1
```

If the USEWINAUTH value is set to one, then the user running the installer must be a SQL sysadmin, and any values entered for SQLUSERNAME and SQLPASSWORD are ignored.

- SQLUSERNAME —enter the SQL username to use SQL Server login authentication.

```text
SQLUSERNAME=mySqlUserName
```

This value is ignored if USEWINAUTH is set to one.

- SQLPASSWORD —enter the SQL password to use SQL Server login authentication.

```text
SQLPASSWORD=myPassword
```

This value is ignored if USEWINAUTH is set to one.

- USEWINAUTH —set this to one to use Windows authentication for the SQL Server.

```text
USEWINAUTH=1
```

If the USEWINAUTH value is set to one, then the user running the installer must be a SQL sysadmin, and any values entered for SQLUSERNAME and SQLPASSWORD are ignored.

Save your edits to the RelativityResponse.txt file, and launch the Install.bat file to proceed with the upgrade.

A sample RelativityResponse.txt file for a agents only upgrade looks like this:

```text
INSTALLAGENTS=1
INSTALLDIR=C:\Program Files\kCura Corporation\Relativity
PRIMARYSQLINSTANCE=ML12
EDDSDBOPASSWORD=MySecretPassword
SERVICEUSERNAME=example\exampleusername
SERVICEPASSWORD=MySecretPassword
USEWINAUTH=1
```

Every line in the RelativityResponse.txt file that starts with ### is a comment and meant to provide instruction.

## Service Host Manager HTTPS configuration

Service Host Manager runs Relativity services on all web and agent servers in your environment. The services are used by applications like Production and Processing on. If your web and agent servers must be set up for HTTPS access, special setup is required for Service Host Manager.

For more information, see HTTPS configuration in Service Host Manager .

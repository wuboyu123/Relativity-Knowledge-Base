---
title: "Upgrading your web server"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Relativity_Upgrade/Upgrading_your_web_server.htm
collection: user
fetched_at: 2026-06-22T06:04:00+00:00
sha256: 55b4249a341625a1d77832ce21cb4674b5fda5ed8c9129c02610a656da36dbe1
---

Upgrading your web server

# Upgrading your web server

This section provides the prerequisites and the steps required to upgrade your web server to a new version of Relativity. For more information, see Pre-installation .

Before you begin upgrading your web server, confirm that you have upgraded the SQL Server, started the SQL service, and that IIS is stopped.

When you install Relativity, it is configured to use HTTPS by default. If you decided not to use HTTPS in your environment, you must set the CookieSecure instance setting to False before logging in to Relativity, or you receive an error message. For more information, see Instance setting table . If you later decide to use HTTPS in your environment, you can find information about how to set up this functionality in Pre-installation .

This documentation contains references to third-party software, or technologies. While efforts are made to keep third-party references updated, the images, documentation, or guidance in this topic may not accurately represent the current behavior or user interfaces of the third-party software. For more considerations regarding third-party software, such as copyright and ownership, see Terms of Use .

## Web server upgrade

The web server hosts Relativity and its services, such as the Services and Web APIs. After you have installed the primary SQL Server, you can run the web and agent server, as well as the distributed database server installations in parallel.

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

The following settings assume that the same machine does not host the web server that hosts the primary or distributed SQL database servers.

Open the RelativityResponse.txt file in a text editor and edit the parameters as follows to install Relativity on the machine that serves the role of the web server:

#### Common properties

- INSTALLWEB —set this value to one.

```text
INSTALLWEB=1
```

If the web server is already installed on this machine and the above value is set to zero, the installer removes the previously existing web server.

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

Save your edits to the RelativityResponse.txt file, and then launch the Install.bat file to proceed with the upgrade.

A sample RelativityResponse.txt file for a web only upgrade looks like this:

```text
INSTALLWEB=1
INSTALLDIR=C:\Program Files\kCura Corporation\Relativity
PRIMARYSQLINSTANCE=ML12
EDDSDBOPASSWORD=MySecretPassword
SERVICEUSERNAME=example\exampleusername
SERVICEPASSWORD=MySecretPassword
USEWINAUTH=1
```

Every line in the RelativityResponse.txt file that starts with ### is a comment and meant to provide instruction.

### Verifying the machine key settings on the IIS

When setting up the IIS for a Relativity installation, you need to verify that the machine keys are configured to use the appropriate methods for the encryption and decryption of forms authentication data.

Use these steps to set the machine key for the IIS:

- Open the IIS Manager.

- Highlight your Relativity website to display configuration options in the Feature View on the IIS dashboard.

- Double-click the Machine Key icon.

- Update the following fields for your version of Windows server:

-

Validation method —SHA1

-

Encryption method —AES

- Save your changes.

## Upgrading a web server configured for mixed authentication with AD

Use the following steps to upgrade a web server configured for mixed mode authentication with Active Directory (AD). For information about setting up a web server configured for mixed authentication with AD, see Authentication .

To update the UseWindowsAuthentication instance setting:

- Open SQL Server Management Studio on your Relativity database server.

- Connect to the EDDS database.

- Execute one of the following SQL statement to set the WindowsAuthentication instance setting to True:

- Update all servers to use Windows Authentication.

```text
UPDATE EDDS.eddsdbo.InstanceSetting SET
value = 'True' WHERE
Name = 'UseWindowsAuthentication'
```

- Update a specific server to use Windows Authentication. Replace YourServerName in the WHERE clause to the name of your machine, which you want to configure for Windows Authentication. You only need the machine name if you want to set this setting per server.

```text
UPDATE EDDS.eddsdbo.InstanceSetting SET
value = 'True' WHERE
Name = 'UseWindowsAuthentication' and MachineName = 'YourServerName'
```

- Add a new row to the instance setting table for each additional machine that you need to enable AD authentication. Use this option when you want AD enabled on multiple web servers in your Relativity environment, but not on all of them. You need to execute the following SQL statement with the name of the additional machine, which you want to configure for Windows Authentication. Replace YourSecondServerName with the name of that machine.

```text
INSERT INTO EDDS.eddsdbo.InstanceSetting
VALUES ('Relativity.Authentication','UseWindowsAuthentication','True','YourSecondServerName','Determines whether Relativity uses Windows Authentication. Set this value False if you want to disable WinAuth. Set it to True if you want to enable WinAuth and require the user to log in to Relativity from the current machine.')
```

## Service Host Manager HTTPS configuration

Service Host Manager runs Relativity services on all web and agent servers in your environment. The services are used by applications like Production and Processing on. If your web and agent servers must be set up for HTTPS access, special setup is required for Service Host Manager.

For more information, see HTTPS configuration in Service Host Manager .

## SignalR

When running Relativity on IIS 7.5 and older, the SignalR protocol may exhibit performance issues, including slow responses and connection failures as it falls back to other supported connection protocols. To resolve this issue, disable dynamic content compression for the Relativity.REST application in the Compression section in IIS:

You can also add the following property to the system.webServer section of the Relativity.REST web.config file:

```text
<urlCompression doDynamicCompression="false" />
```

This change will improve SignalR performance on older versions of IIS.

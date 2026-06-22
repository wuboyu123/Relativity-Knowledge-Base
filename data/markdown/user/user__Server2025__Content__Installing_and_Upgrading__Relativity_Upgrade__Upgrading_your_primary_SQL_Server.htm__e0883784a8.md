---
title: "Upgrading your SQL Server"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Relativity_Upgrade/Upgrading_your_primary_SQL_Server.htm
collection: user
fetched_at: 2026-06-22T06:03:27+00:00
sha256: 95d0029c86d03025d2cb6b5b9361f0fe58082863ee9ae48ddb9495528d38ca21
---

Upgrading your SQL Server

# Upgrading your SQL Server

Follow these steps to upgrade your primary SQL Server. Before doing so, ensure you have completed the required pre-upgrade steps. For more information, see Pre-installation .

This page also contains steps for upgrading a distributed SQL Server. You must upgrade your primary SQL Server before proceeding with these upgrades.

## Primary SQL Server upgrade

The master database, called the EDDS database, resides on the primary SQL Server. You must upgrade Secret Store before updating the primary database. For more information, see Upgrading the Secret Store .

You can then run the web and agent server installations in parallel.

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

Open the RelativityResponse.txt file in a text editor and edit the parameters as follows to upgrade Relativity on the machine that serves the role of the primary SQL Server:

#### Common properties

If you are upgrading to Server 2025 , some values in your response file may now be stored in the Secret Store. These values are identified by the following message: "Value exported to Secret Store." You don't need to edit these values unless you want to update the Secret Store. For more information, see Secret Store .

- INSTALLPRIMARYDATABASE —set this value to one.

```text
INSTALLPRIMARYDATABASE=1
```

- INSTALLDISTRIBUTEDDATABASE —verify that this value is set to zero. You cannot store the distributed database on the same machine as the primary database.

```text
INSTALLDISTRIBUTEDDATABASE=0
```

- INSTALLDIR —enter the installation directory. This is the target directory for all files related to the local installation. This path must be local to the machine and accessible by the server. You must use ASCII characters for this path.

```text
INSTALLDIR=C:\Program Files\kCura Corporation\Relativity
```

- PRIMARYSQLINSTANCE —enter the primary SQL instance. If you are installing to a cluster, specify the cluster and instance name. If you are installing to a named instance, specify the server and instance name. All features require this input.

```text
PRIMARYSQLINSTANCE=ML12
```

- EDDSDBOPASSWORD —enter the EDDSDBO password.

```text
EDDSDBOPASSWORD=MySecretPassword
```

- SERVICEUSERNAME —enter the service username. The Windows login must already exist.

```text
SERVICEUSERNAME=example\exampleusername
```

- SERVICEPASSWORD —enter the Service password.

```text
SERVICEPASSWORD=MySecretPassword
```

- USEWINAUTH —set the value to one to use Windows authentication for the SQL Server.

```text
USEWINAUTH=1
```

If the USEWINAUTH value is set to one, then the user running the installer must be a SQL sysadmin, and any values entered for SQLUSERNAME and SQLPASSWORD are ignored.

- SQLUSERNAME —enter the SQL username if you want to use SQL Server login authentication.

```text
SQLUSERNAME=mySqlUserName
```

This value is ignored if USEWINAUTH is set to one.

- SQLPASSWORD —enter the SQL password if you want to use SQL Server login authentication.

```text
SQLPASSWORD=myPassword
```

This value is ignored if USEWINAUTH is set to one.

#### Primary database properties

- DEFAULTFILEREPOSITORY —enter the default file repository. This path must be a shared folder to which both the user running the installer and the Relativity Service Account have read and write permissions.

```text
DEFAULTFILEREPOSITORY=\\yourmachine\FileShare
```

- EDDSFILESHARE —enter the EDDS fileshare path. This path must be a shared folder to which both the user running the installer and the Relativity Service Account have read and write permissions.

```text
EDDSFILESHARE=\\yourmachine\Fileshare
```

- CACHELOCATION —a valid UNC path for the viewer cache location. The installer ignores this value during an upgrade. It only uses this value on a new installation of Relativity. This parameter is available in Relativity 9.5.292.12 and above. For more information, see Relativity installation .

```text
CACHELOCATION=\\yourmachine\ViewerCache
```

- DTSEARCHINDEXPATH —enter the dtSearch index. This path must be a shared folder to which both the user running the installer and the Relativity Service Account have read and write permissions.

```text
DTSEARCHINDEXPATH=\\yourmachine\dtSearch
```

- RELATIVITYINSTANCENAME —enter the Relativity instance name. Only set this value during a first-time installation. The installer ignores this value on upgrade.

```text
RELATIVITYINSTANCENAME=My Relativity Instance
```

- ADMIN_EMAIL —enter the email address that you want to use for the default Relativity admin account. If you do not specify an email address, the installer uses the default value of relativity.admin@relativity.com. This parameter is available for 9.5.342.116 and above.

```text
ADMIN_EMAIL=relativity.admin@relativity.com
```

- SERVICEACCOUNT_EMAIL —enter the email address that you want to use for the default Relativity service account. If you do not specify an email address, the installer uses the default value of serviceaccount@relativity.com. This parameter is available for 9.5.342.116 and above.

- If you want to use a specific email address for the default Relativity admin or service account, you must enter it for each Relativity upgrade that you perform. If you entered a custom email address during a previous installation, it is overwritten by current email address that you entered or by the default email address when this parameter is blank.

- Use different email addresses for the ADMIN_EMAIL and SERVICEACCOUNT_EMAIL parameters. If you use the same email address for both parameters, the installation fails.

- The ADMIN_EMAIL parameter functions as the username for the default admin account. If you leave the ADMIN_EMAIL value blank, this username defaults to relativity.admin@relativity.com.

```text
SERVICEACCOUNT_EMAIL=serviceaccount@relativity.com
```

- ADMIN_PASSWORD —enter the password that you want to use for the default Relativity admin account. This parameter is available for 9.5.342.116 and above.

```text
ADMIN_PASSWORD=myPassword
```

- SERVICEACCOUNT_PASSWORD —enter the password that you want to use for the default Relativity service account. This parameter is available for 9.5.342.116 and above.

```text
SERVICEACCOUNT_PASSWORD=myPassword
```

To change the ADMIN_PASSWORD or SERVICEACCOUNT_PASSWORD password, you must also update the associated email address. If you enter a new password but do not update the email address, then new password is ignored. For example, if you use an existing or default email address, then the password remains unchanged. However, you can change the email addresses for the admin and service accounts without updating the password.

#### Common database properties

We recommend that the following database paths are local to the SQL Server and accessible. However, we also support UNC paths on SQL Server 2017 and above.

- DATABASEBACKUPDIR —enter the database backup directory.

```text
DATABASEBACKUPDIR=C:\Backup
```

- LDFDIR —enter the LDF directory.

```text
LDFDIR=C:\Logs
```

- MDFDIR —enter the MDF directory.

```text
MDFDIR=C:\Data
```

- FULLTEXTDIR —enter the full text directory.

```text
FULLTEXTDIR=C:\FullText
```

Save your edits to the RelativityResponse.txt file, and launch the Install.bat file to proceed with the upgrade.

A sample RelativityResponse.txt file for a primary SQL database upgrade using Windows authentication looks like this:

```text
INSTALLPRIMARYDATABASE=1
INSTALLDIR=C:\Program Files\kCura Corporation\Relativity
PRIMARYSQLINSTANCE=ML12
EDDSDBOPASSWORD=MySecretPassword
SERVICEUSERNAME=example\exampleusername
SERVICEPASSWORD=MySecretPassword
DEFAULTFILEREPOSITORY=\\yourmachine\FileShare
EDDSFILESHARE=\\yourmachine\Fileshare
CACHELOCATION=\\yourmachine\ViewerCache
DTSEARCHINDEXPATH=\\yourmachine\dtSearch
RELATIVITYINSTANCENAME=My Relativity Instance
ADMIN_EMAIL=relativity.admin@relativity.com
SERVICEACCOUNT_EMAIL=serviceaccount@relativity.com
ADMIN_PASSWORD=myPassword
SERVICEACCOUNT_PASSWORD=myPassword
DATABASEBACKUPDIR=C:\Backup
LDFDIR=C:\Logs
MDFDIR=C:\Data
FULLTEXTDIR=C:\FullText
USEWINAUTH=1
```

Every line in the RelativityResponse.txt file that starts with ### is a comment and meant to provide instruction.

## Distributed SQL Server upgrade

If your Relativity environment uses a distributed SQL Server, then you need to run the installer on a machine other than the one that hosts the primary SQL database. After you have upgraded the primary SQL Server, you can upgrade the distributed database server and the web and agent server upgrades in parallel. Make sure that you review the steps for database server setup on Pre-installation page, including those in the Optionally configure an authentication token-signing certificate section.

Open the RelativityResponse.txt file in a text editor and edit the parameters as follows to upgrade Relativity on the machine that serves the role of the distributed SQL Server:

#### Common properties

- INSTALLPRIMARYDATABASE —set this value to zero. You cannot store the distributed database on the same machine as the primary database.

```text
INSTALLPRIMARYDATABASE=0
```

- INSTALLDISTRIBUTEDDATABASE —set this value to one.

```text
INSTALLDISTRIBUTEDDATABASE=1
```

- INSTALLDIR - Enter the installation directory. This is the target directory for all files related to the local installation. This path must be local to the machine and accessible by the server. You must use ASCII characters for this path.

```text
INSTALLDIR=C:\Program Files\kCura Corporation\Relativity
```

- PRIMARYSQLINSTANCE —enter the primary SQL instance. If you are installing to a cluster, specify the cluster and instance name. If you are installing to a named instance, specify the server and instance name. All features require this input.

```text
PRIMARYSQLINSTANCE=ML12
```

- EDDSDBOPASSWORD —enter the EDDSDBO password.

```text
EDDSDBOPASSWORD=MySecretPassword
```

- SERVICEUSERNAME —enter the service username. The Windows login must already exist.

```text
SERVICEUSERNAME=example\exampleusername
```

- SERVICEPASSWORD —enter the Service password.

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

#### Distributed database properties

- DISTRIBUTEDSQLINSTANCE —enter the Distributed SQL instance. You cannot store the distributed database on the same machine as the primary SQL Server.

```text
DISTRIBUTEDSQLINSTANCE=ML14
```

#### Common database properties

We recommend that the following database paths are local to the SQL Server and accessible. However, we also support UNC paths on SQL Server 2017 and above.

- DATABASEBACKUPDIR —enter the database backup directory.

```text
DATABASEBACKUPDIR=C:\Backup
```

- LDFDIR —enter the LDF directory.

```text
LDFDIR=C:\Logs
```

- MDFDIR —enter the MDF directory.

```text
MDFDIR=C:\Data
```

- FULLTEXTDIR —enter the full text directory.

```text
FULLTEXTDIR=C:\FullText
```

Save your edits to the RelativityResponse.txt file, and launch the Install.bat file to proceed with the upgrade.

A sample response file for a distributed SQL database upgrade using Windows authentication looks like this:

```text
INSTALLDISTRIBUTEDDATABASE=1
INSTALLDIR=C:\Program Files\kCura Corporation\Relativity
PRIMARYSQLINSTANCE=ML12
EDDSDBOPASSWORD=MySecretPassword
SERVICEUSERNAME=example\exampleusername
SERVICEPASSWORD=MySecretPassword
DISTRIBUTEDSQLINSTANCE=ML14
DATABASEBACKUPDIR=C:\Backup
LDFDIR=C:\Logs
MDFDIR=C:\Data
FULLTEXTDIR=C:\FullText
USEWINAUTH=1
```

Every line in the RelativityResponse.txt file that starts with ### is a comment and meant to provide instruction.

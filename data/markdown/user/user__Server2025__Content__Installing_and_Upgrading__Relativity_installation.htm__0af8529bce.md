---
title: "Relativity installation"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Relativity_installation.htm
collection: user
fetched_at: 2026-06-22T06:03:25+00:00
sha256: b81885e824e9dbd0cf9f42bbc36d701db6cc403f2609798a56a65de2a11e6669
---

Relativity installation Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Relativity installation

In line with our commitment to quality, we provide you with comprehensive support during your initial installation of Relativity. Contact the Customer Support team for detailed information about pre-deployment steps you must complete as part of a first-time installation. For more information about pre-deployment steps, see Installation prerequisites .

Use the following instructions to install Relativity for the first time in your environment. These instructions provide you with the information necessary to install Relativity. For additional assistance, contact the Customer Support team .

For instructions about how to upgrade an existing Relativity environment, see Relativity upgrade and Using the Relativity installer .

Relativity no longer supports Service Bus for Windows. RabbitMQ is now the only the message broker option available for use with Relativity.

This documentation contains references to third-party software, or technologies. While efforts are made to keep third-party references updated, the images, documentation, or guidance in this topic may not accurately represent the current behavior or user interfaces of the third-party software. For more considerations regarding third-party software, such as copyright and ownership, see Terms of Use .

## Installation order

Relativity should be installed in the following order:

- Microsoft SQL Server is installed.

- Secret Store is installed. To learn more, see Secret Store installation .

- Relativity Primary SQL is installed. To learn more, see Primary SQL Server installation .

## Installation prerequisites

Before you install Relativity, review the following information to confirm that your environment meets the installation requirements. Make sure that you created the directories as well as obtained the user names and passwords that the installer requires. Review the following pages for information about the hardware, software, and infrastructure requirements for Relativity installations:

- System requirements

- Pre-installation

We recommend changing the default password for the system admin account and the Relativity service account when you first log in to a new environment.

### Pre-upgrade requirements and cleanup process

Please complete the following checks prior to beginning your upgrade to Server 2025.

- Application services shutdown - all Relativity services must be stopped on all servers prior to starting the upgrade. You can use the Relativity-PreUpgrade-CleanUp.ps1 script described below to stop services.

- Disk space verification and temp folder cleanup - Server 2025 includes enhancements to our temp directory structure to allow compatibility with Windows Storage Sense*. Due to these changes, Relativity temp files may be orphaned after upgrading to Server 2025. The Relativity installer does not automatically clean up these temp files, so it is possible for services to be disrupted if the drive becomes full. To prevent this from occurring, Relativity recommends clearing existing temp files and ensuring at least 50GB of free disk space on Web and Agent servers before upgrading to Server 2025. Customers may use the attached Relativity-PreUpgrade-CleanUp.ps1 script to facilitate this on each server.

- Relativity-PreUpgrade-CleanUp.ps1 - this script automates the process of shutting down Relativity services, checking available disk space and clearing files from the following Relativity-only temp folders. This script is available in the installation files attached to the Relativity Server 2025 GA installation files Community Site article and should be executed prior to beginning your upgrade.

- {drive}:\Users\{service_account_name}\AppData\Local\Temp

- {drive}:\Users\{service_account_name}\AppData\Local\Relativity\TempStorage

*Clients who have previously disabled Windows Storage Sense can now enable the feature because Relativity Server 2025 utilizes a new custom temp location at {drive}:\Users\{service_account_name}\AppData\Local\Relativity\TempStorage .

## Secret Store installation

Secret Store is a required infrastructure component that adds a layer of security for Relativity secrets. A secret can be user credentials, a database connect string, an instance setting that contains confidential information such as your SMTP credentials, or a TLS certificate. All confidential information is stored in the Secret Store database that can be accessed only from authenticated servers.

Secret Store is required for installing or upgrading Relativity. You must install and configure Secret Store before installing Relativity on any other machines in your environment. You must also configure all machines to access Secret Store. For more information, see Relativity Secret Store .

## Download the Relativity installer

Download the Relativity installer from the Relativity Community . To access these files, you must be a designated administrative contact for your company or receive permission from an administrative contact before the Community team will grant access to these files.

If you want to set up a single-server installation of Relativity, change the setting for all applicable components from zero to one in the Feature Selection section of the RelativityResponse.txt file before running Install.bat. During a single server installation, the installer will not add any component that is not set to 1 for a new installation. Any feature set to zero in the RelativityResponse.txt file gets uninstalled if it detects a previous installation for that component.

## Using the Relativity installer

A basic instance of Relativity requires multiple servers. You must configure two or more machines to fulfill the following roles:

- Primary SQL Server — the primary database called the EDDS resides on the primary SQL Server.

- Distributed database server —the secondary database that accommodates a distributed instance of the primary SQL Server and can store multiple workspace databases.

- Agents server —the server that launches all Relativity agents and runs the agents framework.

- Web server —the server that facilitates web background processing and handles authentication tasks.

- Message broker server —the server used to configure Relativity to work with RabbitMQ.

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

### Command line alternative to the RelativityResponse.txt file

You can pass in response file parameters on the command line during installation if you do not want your password information in a file stored locally on the machine hosting Relativity components. The command line parameters overwrite, or if left blank, insert the parameters that are in the RelativityResponse.txt file.

Use the following steps to enter parameters you do not want to include in the RelativityResponse.txt file.

- Launch the Windows command prompt as an system admin.

- Navigate to the directory that stores Relativity.exe, Install.bat, and RelativityResponse.txt.

- Enter the following command:

```text
start /wait Relativity.exe /log installLog.txt /responsefilepath=RelativityResponse.txt EDDSDBOPASSWORD=my_password
```

If you do not have your password in the RelativityResponse.txt file and the password includes a space, you must insert quotation marks around the password if you opt to use command line input. The following example assumes that your password is: my password

```text
start /wait Relativity.exe /log installLog.txt /responsefilepath=RelativityResponse.txt EDDSDBOPASSWORD="my password"

```

### Optional installer inputs

You can edit the Install.bat file in a text editor to alter the default behavior of the Relativity installer. There are four optional inputs:

- Dry Run —this configuration only runs validations and does not perform a full installation. Dry run is quick way to determine whether an installation will fail due to a misconfigured environment or response file. It's also useful in debugging scenarios where a validator is failing; instead of running the full installation process, you can run a dry run, determine if the issue is fixed, and then run the installation.

```text
start /wait "" "12.3.xxx.x Relativity.exe" /log InstallLog.txt /responsefilepath=RelativityResponse.txt /dryrun
```

- Skip Validations —this configuration skips validations in the bundle. The validations still run during MSI execution.

```text
start /wait "" "12.3.xxx.x Relativity.exe" /log InstallLog.txt /responsefilepath=RelativityResponse.txt /skipvalidations
```

- Uninstall —this configuration uninstalls Relativity, but you can also accomplish the same task through the Windows Control Panel in the Add or Remove Programs list.

```text
start /wait "" "12.3.xxx.x Relativity.exe" /log InstallLog.txt /responsefilepath=RelativityResponse.txt /uninstall
```

- Repair —this configuration repairs a failed installation.

```text
start /wait "" "12.3.xxx.x Relativity.exe" /log InstallLog.txt /responsefilepath=RelativityResponse.txt /repair
```

### Using PowerShell script

An alternative installation method to using the Install.bat file is available in the form of a sample Windows PowerShell script. You can obtain a sample PowerShell batch script from your Relativity support representative. It contains default values for the various installer processes you can modify in a text editor according to your preferences. The sample script contains custom logic for basic input prompting, parsing, and status indication. The sample file is intended to be an example of a script that uses custom logic to drive the different installer behaviors. For example, the script prompts you to enter the location of the installer executable, but the script also contains default editable values for the RelativityResponse.txt file and log file locations. It displays any errors that occur and the last line in the most recent log file. You can execute it from a PowerShell prompt and pass options in, like the location of the installer executable or the installer mode.

## Primary SQL Server installation

The master database called the Electronic Document Delivery System (EDDS) resides on the primary SQL Server. You must first install the primary SQL database server.

After you install the primary SQL Server, you can run the distributed database server. You can then run the agent and web server installations in parallel.

Open the RelativityResponse.txt file in a text editor and edit the following parameters to install Relativity on the machine that serves the role of the primary SQL Server:

#### Feature selection

- INSTALLPRIMARYDATABASE —set this value to one.

```text
INSTALLPRIMARYDATABASE=1
```

- INSTALLDISTRIBUTEDDATABASE —verify that this value is set to zero. You cannot store the distributed database on the same machine as the primary database.

```text
INSTALLDISTRIBUTEDDATABASE=0
```

#### Primary database properties

- DEFAULTFILEREPOSITORY —enter the default file repository. This path must be a shared folder to which both the user running the installer and the Relativity Service Account have read and write permissions.

```text
DEFAULTFILEREPOSITORY=\\yourmachine\FileShare
```

- EDDSFILESHARE —enter the EDDS fileshare path. This path must be a shared folder to which both the user running the installer and the Relativity Service Account have read and write permissions.

```text
EDDSFILESHARE=\\yourmachine\Fileshare
```

- CACHELOCATION —enter a valid UNC path for the viewer cache location. The user running the installation and the Relativity Service Account must have read and writer permissions to this path. The installer only uses this value on a new installation of Relativity. It ignores this setting during an upgrade.

Use the following format for this path to avoid any errors during installation:

```text
CACHELOCATION=\\yourmachine\ViewerCache
```

If you do not specify a value, then it defaults to the DEFAULTFILEREPOSITORY setting as follows:

```text
\\<DEFAULTFILEREPOSITORY>\cache
```

- DTSEARCHINDEXPATH —enter the dtSearch index. This path must be a shared folder to which both the user running the installer and the Relativity Service Account have read and write permissions.

```text
DTSEARCHINDEXPATH=\\yourmachine\dtSearch
```

- RELATIVITYINSTANCENAME —enter the Relativity instance name.

```text
RELATIVITYINSTANCENAME=My Relativity Instance
```

- ADMIN_EMAIL —enter the email address you want to use for the default Relativity admin account. If you do not specify an email address, the installer uses the default value of relativity.admin@relativity.com.

```text
ADMIN_EMAIL=relativity.admin@relativity.com
```

- SERVICEACCOUNT_EMAIL —enter the email address that you want to use for the default Relativity service account. If you do not specify an email address, the installer uses the default value of serviceaccount@relativity.com.

```text
SERVICEACCOUNT_EMAIL=serviceaccount@relativity.com
```

Use different email addresses for the ADMIN_EMAIL and SERVICEACCOUNT_EMAIL parameters. If you use the same email address for both parameters, the installation fails.

- ADMIN_PASSWORD —enter the password that you want to use for the default Relativity admin account.

```text
ADMIN_PASSWORD=myPassword
```

- SERVICEACCOUNT_PASSWORD —enter the password that you want to use for the default Relativity service account.

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

Save your edits to the RelativityResponse.txt file, and launch the Install.bat file to proceed with the installation.

A sample RelativityResponse.txt file for a primary SQL database installation using Windows authentication looks like this:

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

## Distributed SQL Server installation

A distributed SQL server environment has two or more SQL instances linked together. When creating a new Relativity workspace, you can choose any of the SQL servers to house the database. This helps to spread the load of active workspaces across multiple servers.

If your Relativity environment uses a distributed SQL Server, then you need to run the installer on a machine other than the one that hosts the primary SQL database. You must install the primary SQL Server before you install a distributed server. You can then install the distributed database server in parallel with the web and agent servers. Make sure that you review the steps for database server setup on the Pre-installation page.

To set up a distributed SQL server, ensure the following:

- There is already a primary SQL server with Relativity installed.

- Your environment has at least two or more SQL servers running Windows Server 2016, 2019, 2022, or 2025 and SQL Server 2017, 2019, or 2022. SQL Server 2019 requires Windows Server 2016 or 2019.

### Creating linked servers

Each SQL Server in the Relativity instance that will be distributed must have a linked server entry for every other SQL Server. For example, if there will be four distributed SQL Servers, each SQL Server must have a linked server entry for the other three SQL Servers in the sys.servers table.

To check for any existing linked servers, execute the script below from each SQL Server:

```text
select * from sys.servers
```

On each server to be linked, run the following scripts:

The remoteServerName is the name of the SQL server you want to link to.

```text
sp_addlinkedserver 'remoteServerName'
exec sp_serveroption @server='remoteServerName', @optname='rpc', @optvalue='true'
exec sp_serveroption @server='remoteServerName', @optname='rpc out', @optvalue='true'
exec sp_addlinkedsrvlogin @rmtsrvname = N'remoteServerName', @locallogin = NULL , @useself = N'True'

```

The following screen shot provides an example of running the above script from the Primary SQL Server:

The following screen shot provides an example of running the same script on the Distributed Servers in the same environment:

### Distributed SQL Server installation

Open the RelativityResponse.txt file in a text editor and edit the parameters as follows to install Relativity on the machine that serves the role of the distributed SQL Server:

#### Feature selection

- INSTALLPRIMARYDATABASE —set this value to zero. You cannot store the distributed database on the same machine as the primary database.

```text
INSTALLPRIMARYDATABASE=0
```

- INSTALLDISTRIBUTEDDATABASE —set this value to one.

```text
INSTALLDISTRIBUTEDDATABASE=1
```

#### Common properties

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

- USEWINAUTH - Set this to one to use Windows authentication for the SQL Server.

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

Save your edits to the RelativityResponse.txt file, and then launch the Install.bat file to proceed with the installation.

A sample response file for a distributed SQL database installation using Windows authentication looks like this:

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

## RabbitMQ installation

Relativity requires RabbitMQ as the message broker. RabbitMQ must be installed and configured prior to running the Relativity Installer. For information, see Pre-installation .

Open the RelativityResponse.txt file in a text editor and edit the parameters as follows to install Relativity on the machine that serves the role of the service bus server:

#### Feature selection

- INSTALLSERVICEBUS —set this value to one to install the message broker.

```text
INSTALLSERVICEBUS=1
```

- If the message broker server is already installed on this machine and the INSTALLSERVICEBUS property is set to zero, the installer removes the previously existing server.

- When using RabbitMQ, the Relativity Installer with the INSTALLSERVICEBUS=1 feature selection can be run on any server with network connectivity to both the Primary SQL Server and the RabbitMQ server / cluster.

#### Common properties

The following non-alpha-numeric characters are not allowed in passwords: \, ", <, >.

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

- SERVICEUSERNAME —enter the service user name. The Windows login must already exist.

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

- SERVICEBUSPROVIDER —enter RabbitMQ when using RabbitMQ as your message broker

```text
SERVICEBUSPROVIDER=RabbitMQ
```

- SERVERFQDN —enter the fully qualified domain name of your message broker.

```text
SERVERFQDN=myRabbitMQFQDN
```

- SHAREDACCESSKEY —enter the password Relativity will use when connecting.

```text
SHAREDACCESSKEY=myRabbitMQPassword
```

- SHAREDACCESSKEYNAME —enter the username Relativity will use when connecting.

```text
SHAREDACCESSKEYNAME=myRabbitMQUserName
```

This value is case sensitive.

- SERVICENAMESPACE —enter the virtual host Relativity will use.

```text
SERVICENAMESPACE=Relativity
```

- TLSENABLED —set this to zero if RabbitMQ is not configured for TLS, and set this to one if RabbitMQ is configured for TLS.

```text
TLSENABLED=1
```

Save your edits to the RelativityResponse.txt file, and launch the Install.bat file to proceed with the installation.

A sample response file for a service bus only installation looks like this:

```text
INSTALLSERVICEBUS=1
INSTALLDIR=C:\Program Files\kCura Corporation\Relativity
PRIMARYSQLINSTANCE=ML12
EDDSDBOPASSWORD=MySecretPassword
SERVICEUSERNAME=example\exampleusername
SERVICEPASSWORD=MySecretPassword
USEWINAUTH=1
SERVICEBUSPROVIDER=RabbitMQ
SERVERFQDN=myRabbitMQFQDN
SHAREDACCESSKEY=myRabbitMQPassword
SHAREDACCESSKEYNAME=myRabbitMQUserName
SERVICENAMESPACE=Relativity
TLSENABLED=1
```

Every line in the RelativityResponse.txt file that starts with ### is a comment and meant to provide instruction.

### ServiceBusFullyQualifiedDomainName instance setting

The Relativity installer populates the ServiceBusFullyQualifiedDomainName instance setting according to the following rule during a new installation:

When using RabbitMQ, ServiceBusFullyQualifiedDomainName specifies the fully-qualified domain name for the machine or load balancer where Relativity can reach the environment’s cluster. The Relativity installer automatically sets this value during an installation or upgrade based on the inputs in the RelativityResponse.txt file.

For more information, see ServiceBusFullyQualifiedDomainName instance setting .

## Web server installation

The web server hosts Relativity and its services, such as the Services and Web APIs. First, you upgrade the primary SQL Server, and install or upgrade the Relativity Service Bus. You can then run the web, agent, and distributed database server installations in parallel. The following settings assume that the web server resides on a machine that does not host the primary or distributed databases.

When you install Relativity, it is configured to use HTTPS by default. If you decided not to use HTTPS in your environment, you must set the CookieSecure instance setting to False before logging in to Relativity, or you receive an error message. For more information, see Instance setting table . If you later decide to use HTTPS in your environment, you can find information about how to set up this functionality in Pre-installation .

Open the RelativityResponse.txt file in a text editor and edit the parameters as follows to install Relativity on the machine that serves the role of the web server:

#### Feature selection

- INSTALLWEB —set this value to one.

```text
INSTALLWEB=1
```

If the web server is already installed on this machine and the above value is set to zero, the installer removes the previously existing web server.

#### Common properties

The following non-alpha-numeric characters are not allowed in passwords: \, ", <, >.

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

#### Web properties

- ENABLEWINAUTH —set this property to 1 to enable Integrated Authentication for your Relativity instance. It updates IIS configuration and sets the value of the UseWindowsAuthentication instance setting to True.

```text
ENABLEWINAUTH=1
```

After Integrated Authentication is enabled by the installer, you must configure it for individual Relativity users. For more information, see Managing user authentication methods .

Save your edits to the RelativityResponse.txt file, and launch the Install.bat file to proceed with the installation.

A sample RelativityResponse.txt file for a web only installation looks like this:

```text
INSTALLWEB=1
INSTALLDIR=C:\Program Files\kCura Corporation\Relativity
PRIMARYSQLINSTANCE=ML12
EDDSDBOPASSWORD=MySecretPassword
SERVICEUSERNAME=example\exampleusername
SERVICEPASSWORD=MySecretPassword
USEWINAUTH=1
ENABLEWINAUTH=1

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

## Agent installation

The agent server runs background processes for Relativity, such as those used for imaging, branding, and others. First, you upgrade the primary SQL Server, and install or upgrade the Relativity Service Bus. You can then run the web, agent, and distributed database server installations in parallel.

The following settings assume that the same machine does not host the agent server that hosts the primary or distributed SQL database servers.

Open the RelativityResponse.txt file in a text editor and edit the parameters as follows to install Relativity on the machine that serves the role of the agent server:

#### Feature selection

- INSTALLAGENTS —set this value to one.

```text
INSTALLAGENTS=1
```

This value only effects first time installations. The setting is ignored by all subsequent upgrades.

#### Common properties

The following non-alpha-numeric characters are not allowed in passwords: \, ", <, >.

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

#### Agent properties

- DEFAULTAGENTS —set this to one for core agents servers or zero for non-core agents.

```text
DEFAULTAGENTS=1
```

Save your edits to the RelativityResponse.txt file, and launch the Install.bat file to proceed with the installation.

A sample RelativityResponse.txt file for a agents only installation looks like this:

```text
INSTALLAGENTS=1
INSTALLDIR=C:\Program Files\kCura Corporation\Relativity
PRIMARYSQLINSTANCE=ML12
EDDSDBOPASSWORD=MySecretPassword
SERVICEUSERNAME=example\exampleusername
SERVICEPASSWORD=MySecretPassword
DEFAULTAGENTS=1
USEWINAUTH=1
```

Every line in the RelativityResponse.txt file that starts with ### is a comment and meant to provide instruction.

## Install the worker manager server

After completing the Relativity installation, you must install the worker manager server. For more information, see the following pages:

- Worker manager server pre-installation steps

- Installing the worker manager server

## Configuring an SMTP Server

You can configure your SMTP server to relay messages from Relativity agent and web servers. You need to configure your SMTP server so that it can send email messages outside of your domain with encrypted attachments. In addition, you must update specific instance setting values on the Instance setting table in the EDDS database.

Use this procedure to configure your SMTP server:

- To enable SMTP communication, verify that port 25 is open on your Relativity agent and web servers. Also, verify that it is configured to allow relaying.

- Use the kCura.Notification.WinForm utility to verify that SMTP relay works properly. Click here to download this utility, extract it, and run it in your environment.

- Log in to Relativity as a system admin.

- Click the Relativity Script Library tab to display a list of Relativity scripts.

- Click New Relativity Script .

- Copy and paste the following code in the Script Body box. This script outputs a list of instance settings and their current settings.

```text
SELECT *
FROM eddsdbo.[Configuration]
WHERE Name IN ('SMTPServer','Account','Instance','EnvironmentName','EmailFrom','EmailTo','CaseStatisticsNotificationList')
```

Your code should look similar to this screen shot:

- Click Save .

- Click Run Script to display a pop-up window on the details view.

- Click Run to display a list containing the settings in your instance settings.

- Select Export to File in the mass operation drop-down box and click Go . Save the file in a local directory. You can also optionally output a .csv file with these settings.

If you have already set any of the instance settings, keep a copy of these settings in case you need to refer to it later.

## Testing your SMTP server configuration

You can test the configuration of your SMTP server to make sure that it has the proper settings.

Use this procedure to test your SMTP configuration:

- Create a test workspace.

- Build a small dtSearch index in your test workspace, and enter your email address in the Email notification recipients field.

- Build the index and verify that you received an email.

- Check the Errors tab to determine if any errors occurred from the Home tab.

- Re-run this test on an email address outside of your domain.

- Check the Errors tab to determine if any errors occurred from home.

## Enable telemetry

After you install Relativity, complete the steps to enable telemetry in your environment. Telemetry collects metrics for performance, usage, and billing. For more information, see Telemetry and metrics .

## Log files

The Relativity installer automatically creates log files to assist in troubleshooting. There is no set list of log file names, but all the log files save to the same directory and share the same naming scheme as the log specified in the batch script.

For example, the following command saves a log to the directory that the command prompt is pointing to when run:

```text
start /wait Relativity.Installer.exe /log Install.log
```

The above command yields the following logs:

- Install.log —this is the main installer log. Check this log first when troubleshooting. The log records the error and directs you to the next log file to check. This is the only log created during a dry run.

- Install_0_<package identifier>.log —this is the log for the first package run.

- Install_1_<package identifier>.log —this is the log for the second package run.

- Install_2_<package identifier>.log —this is the log for the third package run.

Package identifiers might display as VCRedist2005x86, Agents, PrimaryDatabase, or something else.

On this page

- Relativity installation

- Installation order

- Installation prerequisites

- Pre-upgrade requirements and cleanup process

- Secret Store installation

- Download the Relativity installer

- Using the Relativity installer

- Command line alternative to the RelativityResponse.txt file

- Optional installer inputs

- Using PowerShell script

- Primary SQL Server installation

- Distributed SQL Server installation

- Creating linked servers

- Distributed SQL Server installation

- RabbitMQ installation

- ServiceBusFullyQualifiedDomainName instance setting

- Web server installation

- Verifying the machine key settings on the IIS

- Agent installation

- Install the worker manager server

- Configuring an SMTP Server

- Testing your SMTP server configuration

- Enable telemetry

- Log files


Why was this not helpful?

Check one that applies.

I could not find the information I was looking for.

The information was incorrect.

The instructions are confusing or unclear.

The instructions did not work.

Thank you for your feedback.

Want to tell us more?


Great!

Thanks for taking the time to provide feedback.


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use

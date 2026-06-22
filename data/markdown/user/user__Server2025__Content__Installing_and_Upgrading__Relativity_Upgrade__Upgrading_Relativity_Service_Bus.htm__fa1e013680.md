---
title: "Upgrading Relativity Service Bus"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Relativity_Upgrade/Upgrading_Relativity_Service_Bus.htm
collection: user
fetched_at: 2026-06-22T06:04:18+00:00
sha256: 94e446271871cde5a325aa7f49003c738c6cce5c947bbf617717e87c5f6f3eb7
---

Upgrading Relativity Service Bus Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Upgrading Relativity Service Bus

Relativity no longer supports Service Bus for Windows. RabbitMQ is now the only the message broker option available for use with Relativity.

To upgrade Relativity Service Bus, you run the installer on a machine where it is already installed, or where RabbitMQ is installed. You must include the Relativity Service Bus server as a node in the RabbitMQ cluster. For more information, see Pre-installation .

When you perform an upgrade, the Relativity installer saves information about the about the farm/cluster to the primary SQL Server database. It also performs setup tasks on farm/cluster, so that Relativity can connect to the service bus.

## Relativity Service Bus upgrade

The Relativity Service Bus supports messaging between application components. Before installing or upgrading the Relativity Service Bus, upgrade the primary SQL Server. For more information, see Relativity Service Bus .

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

## Setting properties in the RelativityResponse.txt file

Relativity requires RabbitMQ as the message broker.

For information about prerequisites, see Pre-installation . If you're re-purposing a worker as a conversion agent, see Re-Purposing .

Open the RelativityResponse.txt file in a text editor and edit the parameters as follows to install Relativity on the machine that serves the role of the service bus server:

#### Feature selection

- INSTALLSERVICEBUS —set this value to one to install the Relativity Service Bus.

```text
INSTALLSERVICEBUS=1
```

- If the service bus server is already installed on this machine and the INSTALLSERVICEBUS property is set to zero, the installer removes the previously existing service bus server.

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

- SERVERFQDN —enter the fully qualified domain name of your message broker.

```text
SERVERFQDN=localhost
```

- SHAREDACCESSKEY —enter the password Relativity will use when connecting.

```text
SHAREDACCESSKEY=guest
```

- SHAREDACCESSKEYNAME —enter the username Relativity will use when connecting.

```text
SHAREDACCESSKEYNAME=guest
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
SERVERFQDN=localhost
SHAREDACCESSKEY=guest
SHAREDACCESSKEYNAME=guest
SERVICENAMESPACE=Relativity
TLSENABLED=1
```

Every line in the RelativityResponse.txt file that starts with ### is a comment and meant to provide instruction.

### Troubleshooting service bus installation

For more information to troubleshoot issues that may occur during the service bus installation, see Troubleshooting RabbitMQ .

### ServiceBusFullyQualifiedDomainName instance setting

The Relativity installer populates the ServiceBusFullyQualifiedDomainName instance setting according to the following rules during a new installation:

When using RabbitMQ, ServiceBusFullyQualifiedDomainName specifies the fully-qualified domain name for the machine or load balancer where Relativity can reach the environment’s cluster. The Relativity installer automatically sets this value during an installation or upgrade based on the inputs in the RelativityResponse.txt file.

For more information, see ServiceBusFullyQualifiedDomainName instance setting .

On this page

- Upgrading Relativity Service Bus

- Relativity Service Bus upgrade

- Setting properties in the RelativityResponse.txt file

- Troubleshooting service bus installation

- ServiceBusFullyQualifiedDomainName instance setting


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

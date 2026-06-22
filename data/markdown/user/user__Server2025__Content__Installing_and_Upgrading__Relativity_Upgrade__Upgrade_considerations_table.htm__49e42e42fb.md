---
title: "Upgrade considerations"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Relativity_Upgrade/Upgrade_considerations_table.htm
collection: user
fetched_at: 2026-06-22T06:01:55+00:00
sha256: c8e55d8a4213bde27032eedbc52bba4215773c358ea0a30cd267a785997c6505
---

Upgrade considerations

# Upgrade considerations for Relativity

This page lists the key system updates for Server 2025 that all customers should be aware of before upgrading. Also included are changes introduced in the two other supported Server versions, Server 2023 and Server 2024.

If you are upgrading to Server 2025 from Relativity 6.x - Server 2024, contact your Customer Success Manager.

You must install and configure the Relativity Secret Store before installing any other Server 2025 components. For more information, see Relativity Secret Store .

Relativity does not support in-place upgrades of the Operating System on production servers.

Version Feature Upgrade consideration

Version Feature Upgrade consideration

Server 2025 Windows Server

Windows Server 2025 is now supported.

See the Compatibility matrix for more information.

Server 2025 RabbitMQ

RabbitMQ 4.1.4 is now supported and is the only version of RabbitMQ supported for Server 2025.

- RabbitMQ 4.1.4 requires Erlang 26.2–27.x.

- If you're using an unsupported Erlang version, RabbitMQ nodes will not start.

See the System requirements and RabbitMQ for more information.

Server 2025 Microsoft Office 2024

- Relativity Server 2025 supports Microsoft Office 2024, building on the initial availability introduced in Server 2024 Patch 2.

- Microsoft ended support for Office 2016 on October 14, 2025; upgrading to Office 2024 is recommended to maintain a secure and supported environment.

- Worker servers that run Office 2024 must be on Windows Server 2022. Other server roles (SQL, Web, Agent and others) may remain on their existing operating systems, provided those versions are still supported and you intend to continue using them in their current configurations.

- For detailed upgrade steps, including removing legacy Office versions and installing Office 2024, see Upgrading your Workers to Office 2024 .

Server 2025 Environment Watch Environment Watch is available as an optional component for Relativity Server 2025 and was introduced in Relativity Server 2024 Patch 2. Environment Watch provides monitoring and insights to help you assess the health and performance of your Relativity environment. For more information, see Environment Watch .

Server 2025 Platform SDK Updated versions of the Relativity Server SDKs have been published for Server 2025. Follow the platform version support policy when developing or testing extensions. For details, see Relativity Server SDK and API Packages Changes on the Platform site.

Server 2025 PDF application The PDF application is now bundled with the Relativity Server 2025 installer; no separate deployment is required.

Server 2025 Batch Set Cleanup The Batch Set Cleanup application has replaced the Remove Documents from Batch Sets application; no agents are required to run it. For details, see Batch Set Cleanup .

Server 2025 Database schema A number of EDDS and/or Workspace database schema updates are new in Server 2025. See Database scheme updates on the Platform site for more information.

Server 2025 Instance settings There are new instance settings for Server 2025. See Instance settings change log for more information.

Server 2025 Agents

The following agent is new:

- Alert Manager – this agent is used for Environment Watch, and it runs every 30 seconds to fetch alert data from Kibana and populate it into corresponding Relativity Alert RDOs. The Alert Manager Agent is automatically added when the Relativity Alerts application is installed in the instance.

Server 2025 Elasticsearch version

Server 2025 is compatible with Elasticsearch 8.x and 9.x. The following versions are officially certified for both Data Grid Audit and Environment Watch:

- Elasticsearch 8.19.8

- Elasticsearch 9.1.3

Server 2025 Data Grid Audit

Relativity Server 2024 Patch 1 introduced changes to Data Grid Audit authentication and licensing. Data Grid Audit no longer uses the Custom Realms plug-in or requires a Platinum Elasticsearch license. Instead, authentication now relies on API key–based OAuth2, and the Relativity-provided license key will expire in April 2026. All customers using Data Grid Audit must, by April 1, 2026:

- Upgrade Elasticsearch to 7.17.9 or higher (v8 supported only after cut-over).

- Upgrade to Server 2024 Patch 1 (or higher) or Server 2025.

- Complete the API key-based authentication cut-over via the Relativity Server CLI.

- Update Elasticsearch to remove the old Relativity-provided Platinum license; customers may use a free/open Elastic license or their own Platinum/Enterprise license for premium features.

Data Grid Audit will stop functioning after April 1, 2026 if you do not complete these steps. Core functionality remains unchanged when you move to the free/open license. For more information, see Enable Data Grid Audit .

Server 2024 Patch 2 Worker

You can apply Server 2024 Patch 2 with Office 2016 as well.

If you want to use Office 2024, there is a script that you need to run to insert toggles.

To install Office 2024 and Patch 2:

- Stop Invariant queue manager and all workers.

- Install Office 2024.

- Upgrade Invariant Patch 2.

After upgrading Patch 2 with Office 2024, processing and native imaging might be unchecked for each worker. We recommend verifying each worker's status.

If you are going to use Office 2024, you can run the following scripts:

- Run the following script in the Invariant Database:

```text
Use Invariant
IF EXISTS (
	SELECT 1
	FROM [Invariant].[dbo].[Toggle]
	WHERE [Name] = 'Invariant.Toggles.Office2024Toggle'
)
BEGIN
	UPDATE [Invariant].[dbo].[Toggle]
	SET [IsEnabled] = 1
	WHERE [Name] = 'Invariant.Toggles.Office2024Toggle';
END
ELSE
BEGIN
	INSERT INTO [Invariant].[dbo].[Toggle] ([Name], [IsEnabled])
	VALUES ('Invariant.Toggles.Office2024Toggle', 1);
END
```

- Run the following script in the EDDS Database:

```text

Use EDDS

IF EXISTS (
	SELECT 1
	FROM [EDDS].[eddsdbo].[Toggle]
	WHERE [Name] = 'Relativity.Imaging.Toggles.Office2024Toggle'
)
BEGIN
	UPDATE [EDDS].[eddsdbo].[Toggle]
	SET [IsEnabled] = 1
	WHERE [Name] = 'Relativity.Imaging.Toggles.Office2024Toggle';
END
ELSE
BEGIN
	INSERT INTO [EDDS].[eddsdbo].[Toggle] ([Name], [IsEnabled])
	VALUES ('Relativity.Imaging.Toggles.Office2024Toggle', 1);
END
```

Server 2024 Instance settings There are several new instance settings for Server 2024. See Instance settings change log for more information.

Server 2024 Pre-upgrade cleanup

Please complete the following checks prior to beginning your upgrade to Server 2025.

- Application services shutdown - all Relativity services must be stopped on all servers prior to starting the upgrade. You can use the Relativity-PreUpgrade-CleanUp.ps1 script described below to stop services.

- Disk space verification and temp folder cleanup - Server 2025 includes enhancements to our temp directory structure to allow compatibility with Windows Storage Sense*. Due to these changes, Relativity temp files may be orphaned after upgrading to Server 2025. The Relativity installer does not automatically clean up these temp files, so it is possible for services to be disrupted if the drive becomes full. To prevent this from occurring, Relativity recommends clearing existing temp files and ensuring at least 50GB of free disk space on Web and Agent servers before upgrading to Server 2025. Customers may use the attached Relativity-PreUpgrade-CleanUp.ps1 script to facilitate this on each server.

- Relativity-PreUpgrade-CleanUp.ps1 - this script automates the process of shutting down Relativity services, checking available disk space and clearing files from the following Relativity-only temp folders. This script is available in the installation files attached to the Relativity Server 2025 GA installation files Community Site article and should be executed prior to beginning your upgrade.

- {drive}:\Users\{service_account_name}\AppData\Local\Temp

- {drive}:\Users\{service_account_name}\AppData\Local\Relativity\TempStorage

*Clients who have previously disabled Windows Storage Sense can now enable the feature because Relativity Server 2025 utilizes a new custom temp location at {drive}:\Users\{service_account_name}\AppData\Local\Relativity\TempStorage .

Server 2024 Audit Elasticsearch version 7.17 is the minimum required version for Data Grid Audit in Server 2024. Support for the Elasticsearch v8 series is planned for late 2024 in conjunction with the release of a new Relativity-Elasticsearch configuration tool.

Server 2024 Service Bus

You must use RabbitMQ version 3.12.x or 3.13.x and a compatible version of Erlang. Note, however, that there are compatibility issues between RabbitMQ 3.12.x and Erlang 26.0 and 26.1. There are no issues with Erlang 26.2 and above and RabbitMQ 3.12.x. For compatibility details, see Erlang Version Requirements . To download the latest version of Erlang, see Download Erlang . RabbitMQ 3.13.x is certified compatible with Server 2024 when TLS 1.3 is enabled. Relativity only supports TLS 1.2 and 1.3. If you have prior versions of TLS, we recommend manually disabling them. To learn more, see Disabling previous versions of TLS in Windows . Ensure that you're using the 64-bit version of Erlang, or else the system will be constrained to 2GB of memory. For details on RabbitMQ's version policies, see RabbitMQ versions . Review the RabbitMQ upgrade overview beforehand to avoid issues during the upgrade process.

To ensure RDP access to the server, enable both TLS 1.3 and TLS 1.2. Disabling TLS 1.2 may result in the inability to connect to the server using RDP.

Server 2024 Agents

The following agents are new:

- RSMF Slicing Agent - Works with the Message Broker to complete RSMF slicing operation to create subsets of larger RSMF documents/conversations.

Server 2024 Worker Microsoft Office 2016 is still required to be installed on Worker Servers for Server 2024 GA and Patch 1. Relativity intends to retroactively certify support for Office 2024 for Server 2024 Patch 2 by September 2025. See this Community article for more information.

Server 2024 Environment Watch Relativity will release a new optional feature called Environment Watch in late 2025. This feature will provide Server customers with new telemetry insights, an enhanced in-app alerting experience, streamlined log searching, and dashboards to help customers monitor the health of their environment. Environment Watch will require Elasticsearch and Kibana to be installed alongside Relativity Server 2024. More details about the feature and release date will be shared in the coming months.

Server 2023

Patch 2

Extensibility Points Non-temporary Relativity program files are no longer saved in Windows Temp folders. The automatic deletion of files from these folders (e.g. by anti-virus software or Microsoft Storage Sense) would occasionally cause Relativity product functionality issues.

Server 2023 Instance settings

There are a number of new, removed, and modified instance settings for Server 2023. See Instance settings change log for more information.

The default value of the TreatArmRestoreJobFailureAsWarning instance setting, which you must manually add to your instance, is now True. This means that, by default, ARM restore jobs will skip analytics indexes and structured analytics sets that have failed. If you'd like to revert to the previous behavior of ARM erroring when an index or set fails, set this instance setting to false.

Server 2023 SDK and NuGet packages

Effective with the Relativity Server 2023 General Availability (GA) release, the NuGet packages required to extend core functionality and implement custom applications for Relativity Server will be published and maintained separately from the SDKs hosted on the Relativity NuGet Gallery. The latest SDKs for Relativity Server will be hosted in a separate repository, while the Relativity NuGet Gallery is now considered the repository for RelativityOne packages. Separating the RelativityOne and Relativity Server packages provides for a more stable and reliable developer experience as each platform evolves. You are not required to recompile your custom application against the relocated packages for your application to work on Server 2023. Custom applications compiled against the packages hosted on the Relativity NuGet Gallery will continue to work on future Relativity Server releases, as long as no breaking changes are introduced by the RelativityOne platform. However, we do recommend recompiling your code to consume the new repository packages when possible, to ensure that your application is running against the latest Relativity Server SDKs. The new package repository and documentation for consuming the Server-specific packages will be made available within a few weeks of the official Server 2023 release. We will make an announcement and provide additional documentation when the repository is made available. For more information, see the Relativity Server 2023 Developer News topic on the platform site.

Server 2023 RSAPI RSAPI has been removed in the Relativity Server 2023 release. See the RSAPI deprecation process topic in the Developer Guide for more information.

Server 2023 Classic Viewer Classic Viewer has been removed in the Relativity Server 2023 release. Viewer extensions that only work with the Classic Viewer will no longer be functional. If you have not already done so, you will need to migrate your classic viewer extension code to the Review APIs. See Viewer Extension Migration Guide for more details.

Server 2023 .NET Framework .NET Framework 4.8 and 4.8.1 are now supported.

Server 2023 SQL Server SQL Server 2022 is now supported.

Server 2023 Windows Server Windows Server 2022 is now supported.

Server 2023 Windows Server Windows Server 2012 is no longer supported.

Server 2023 Service Bus Service Bus for Windows Server is no longer a supported message broker option for Relativity service bus. RabbitMQ is the only supported message broker.

Server 2023 Service Bus

For Server 2023, versions 3.11.x, 3.12.x, and 3.13.x are supported. You must use RabbitMQ version 3.11.x - 3.13.x and a compatible version of Erlang. For compatibility details, see Erlang Version Requirements . Ensure that you're using the 64-bit version of Erlang, or else the system will be constrained to 2GB of memory.

Server 2023 Legal Hold Preservation basic authentication deprecation For Legal Hold, you are now required to use Modern Authentication, certificate based, for setting up Preservation Hold Settings. Basic Authentication, username and password, is no longer available for Preservation Hold Settings.

Server 2023 Workspace management The new Workspace Delete agent and Workspace Housekeeping agent are responsible for deleting workspaces. The Case Manager agent is removed in Server 2023.

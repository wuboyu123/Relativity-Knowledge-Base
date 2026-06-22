---
title: "System requirements"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/System_requirements/System_requirements.htm
collection: user
fetched_at: 2026-06-22T06:03:18+00:00
sha256: 72a212f69876c536a8453a37c3b04e9c1a629b1ea18abd68744fbffdf2e8aec1
---

System requirements

# System requirements

These system requirements contain detailed information about the software and hardware you use to host Relativity in your environment and in the cloud. These requirements also provide various recommendations for configuring a new deployment of Relativity, as well as scaling your environment as the number of users and the amount of data continue to grow.

This documentation contains references to third-party software, or technologies. While efforts are made to keep third-party references updated, the images, documentation, or guidance in this topic may not accurately represent the current behavior or user interfaces of the third-party software. For more considerations regarding third-party software, such as copyright and ownership, see Terms of Use .

## Infrastructure overview

Relativity is designed with a scalable infrastructure that you can tailor to the requirements of your environment. It is developed on the .NET framework with a Microsoft SQL Server back-end. As illustrated in the following diagram, all areas of the platform are scalable providing support for any hardware vendor, hypervisor, and storage protocol.

### Web server

The Web Server is the gateway for all users to access Relativity. It authenticates the user with the system, contains APIs for searching and third-party applications, transfers documents to the Viewer, and is responsible for communications during imports and exports in workspaces.

There are different mechanisms for authentication into the system including forms, active directory, two-factor, SAML 2.0, and OpenID Connect. User sessions can be load balanced with the included Relativity User Load Balancer or with available hardware load balancing solutions.

### Agent server - core

Agents in Relativity are responsible for running all background processing tasks. When a user submits a job, such as a production or OCR job, the associated agents will pick up the job and complete the work.

The agents run under a Windows Service and often require various levels of CPU, RAM and I/O, depending on the job type. The agents can be scaled vertically and horizontally to accommodate organizational needs.

### Agent server - conversion

Viewer conversion jobs are handled by the Conversion agents. Any Relativity agent server designated as a conversion agent server should only have one conversion agent deployed. Conversion jobs are multi-threaded and one conversion agent may utilize all available processor cores on a server.

For more information, see Required configurations for new deployments .

### Agent server - dtSearch

dtSearch queries are multi-threaded and spawn as many threads as there are sub-indexes or cores—whichever number is lowest will be the constraint. One dtSearch search agent may be able to utilize all available processor cores on a server. Therefore, each Relativity agent server that is designated to be a dtSearch search agent server should only have one dtSearch search agent, and nothing else.

### SQL Server - workspaces

This SQL Server is where the structured text and metadata resides for the documents. Each Relativity workspace is represented by its own SQL Server database. Environments may have one or more SQL Servers. In addition to workspace databases there are Relativity system databases present on each server that contain tables for system configurations, agent job queues, users or groups, and more.

### SQL Server - Invariant/Worker Manager server

Relativity processing has individual store databases that correspond to each Relativity workspace database with processing enabled. Total memory and processor requirements for this role are not as demanding as the SQL Servers that house workspace databases. This server is also used for native imaging and save as PDF request management.

### Worker

The Worker role is responsible for handling enhanced native imaging and processing jobs. Relativity has placed a hard cap on the amount of threads that each Worker server is allowed to spawn. The hard cap is 16 threads. Each processor core and 2 GB RAM will create two threads. Therefore, it is suggested that 8 logical cores and 16 GB RAM be allocated to each worker server to get the most throughput.

### Secret Store

Secret Store is a required component that provides secure, auditable storage for Relativity secrets. A secret could be user credentials, a database connect string, an instance setting that contains confidential information such as your SMTP credentials, or a TLS certificate.

All confidential information is stored securely in the Secret Store database that can be accessed only from authenticated servers. For more information, see Relativity Secret Store .

### Message broker

The Relativity Service Bus is a message delivery service that communicates information about agent jobs to different application components. This infrastructure feature supports this communication by routing messages between application components. For example, Relativity uses the service bus for submitting conversion jobs to agents and returning converted documents.

### Analytics

The analytics server is responsible for building and storing the conceptual indexes in the environment. Once an index is built, the server is also used to run the conceptual features such as categorization and clustering. In addition to conceptual indexing, structured analytics sets are run on this server for textual analysis features such as email threading or language identification. The indexes and structured analytics sets are stored on disk in a configurable location.

### File server

This server may not be required depending on the available storage. Relativity does not install any software on a file server for Relativity. Relativity just needs to know where the files, Natives/Images, live and the web servers need to be able to access those locations. The same applies to dtSearch, Analytics index, and viewer cache locations.

### Data Grid master node

This is the server within a cluster that manages changes across the entire cluster.

### Data Grid client node

This is the server that serves as the gateway through which data enters a cluster. When there is more than one in an environment, these can be thought of as load balancers which service requests for data.

### Data Grid data node

This is the server that stores data within a cluster.

## Scalability

You can scale Relativity installations to handle the performance, storage, and other environmental factors necessary to support the addition of new users, continual growth of data, and increased demands for searching capabilities.

### Tier level definitions

We have identified tier levels that support varying numbers of users and sizes of active data. You can use these tier level definitions to determine the cores, RAM, and other equipment required to support the rapid growth of your Relativity installation. Key terms used in the following table include:

- Enabled User Accounts —amount of enabled Relativity User accounts.

- Simultaneous Users —average amount of simultaneous users logged into Relativity.

- Active SQL Data (TB) —total amount of disk space consumed by SQL databases (mdf) and full text (ndf) indexes.

- Active Record Count (MM) —total amount of records, or documents, included across all active Relativity workspaces.

- Active File Size (TB) —total amount of disk space consumed by native and image files.

This table identifies the combination of users, data, and file sizes associated with each tier.

Tier 1 - Entry Level Environment

Tier 2 - Mid Level Environment

Tier 3 - Large Scale Environment

Enabled User Accounts < 300 300 - 1000 1000+

Simultaneous Users

< 100 100 - 500 500+

Active SQL Data (TB)

< 1 1 - 10 10+

Active Record Count (MM) < 20 20 - 100 100+

Active File Size (TB)

< 5 5 - 30 30+

The equipment used to support environments at each tier is described in the following table.

Tier 1 - Entry Level Environment

Tier 2 - Mid Level Environment

Tier 3 - Large Scale Environment

Total Cores for Non-SQL < 48 48 - 192 192+

Total Memory (GB) for Non-SQL < 96 96 - 384 384+

Total Cores for SQL Server < 16 16 - 96 96+

Total Memory (GB) for SQL Server < 128 128 - 1024 1024+

Total SQL Storage I/O (Gbps) 4 - 8 8+ 16+

SQL Tempdb Storage Separate spindles SSD or flash SSD or flash

## Required configurations for new deployments

Contact Customer Support for assistance with designing your Relativity infrastructure.

- The following Tier 1 example environments provide information for different user and data counts. Most new deployments adhere to one of these Tier 1 examples.

- Determine if your processing needs can be achieved with your selected number of named users. For example, you have 30 named users but process a heavy amount of data daily. For best performance, add additional workers to your current tier or move up a tier.

## Tier 1 - Hardware requirements (45-50 named users)

We support the installation of all Relativity components on a single device for 45-50 named user agreements. We also require that you install a hypervisor to this device so each Relativity role has its own virtual machine.

### 25-50 named users

We support the installation of all Relativity components on a single device for 25-50 named user agreements. We also require that a hypervisor is installed to this device so each Relativity role has its own virtual machine.

The following table provides virtual machine specifications for the single server setup.

Tier 1 (45-50 named users) - Single Server Deployment

Quantity

Memory (GB)

CPU

Web* 2 32 8-16

Agent (core) 2 4 4

Agent (dtSearch) 1 4 4

Agent (conversion) 1 8 4

Agent (PDF)** 1 16 8

Analytics 1 32 4

Worker 1 16 8

Secret Store 1 4 4

SQL (workspace databases) 1 64 8

SQL (Invariant/Worker Manager server) 1 16 4

Data Grid master/data/client node 1 16 4

Message broker server 1 4 4

* Relativity has only been tested with optimal performance for up to 50 users. Anything above the recommended optimal user count per web server is considered unsupported since there are additional considerations that you would need to address beyond increasing the CPU and RAM resources.

** If users have a dedicated Invariant worker for Save As PDF jobs they can either decommission it or convert it to an agent server following the recommendation of two PDF Worker agents per VM.

This table lists the recommendations for environments at Tier 1.

Tier 1 (100+ named users) - Entry Level Environment

Quantity

Memory (GB)

CPU

Web* 2 32 8-16

Agent (core) 2 4 4

Agent (dtSearch) 1 4 4

Agent (conversion) 1 16 8

Agent (PDF)** 1 16 8

Analytics 1 32 8

Worker 2 16 8

Secret Store 1 4 4

Message broker server 1 8 8

SQL (workspace databases) 1 64 8

SQL (Invariant/Worker Manager server) 1 16

4

Data Grid Mast Node/Data Node/Client Node 3 16 4

* Relativity has only been tested with optimal performance for up to 50 users. Anything above the recommended optimal user count per web server is considered unsupported since there are additional considerations that you would need to address beyond increasing the CPU and RAM resources.

** If users have a dedicated Invariant worker for Save As PDF jobs they can either decommission it, or convert it to an agent server following the recommendation of two PDF Worker agents per VM.

## Tier 2 - Hardware requirements

### 300 or more named users

For Tier 2 environments, additional virtual machines are required as well as increased RAM and CPUs as illustrated in the following table. Additionally, it is suggested that SQL, Workspace Databases, instances are not virtualized when supporting larger data sets.

Tier 2 (300+ named users) - Mid Level Environment

Quantity

Memory (GB)

CPU

Web* 5-6 64-96 16-32

Agent (core) 3 16 8

Agent (dtSearch) 2 16 8

Agent (conversion) 2 16 8

Agent (PDF)** 2 16 8

Analytics (structured analytics) 1 32 8

Analytics (Analytics indexing) 1 32 4

Worker (processing, imaging) 2 16 8

Secret Store 1 4 4

Message broker server 1 16 16

SQL (workspace databases) 2 256 16

SQL (Invariant/Worker Manager server) 1 32 4

Data Grid master node 3 32 8

* Relativity has only been tested with optimal performance for up to 50 users. Anything above the recommended optimal user count per web server is considered unsupported since there are additional considerations that you would need to address beyond increasing the CPU and RAM resources.

** If users have a dedicated Invariant worker for Save As PDF jobs they can either decommission it, or convert it to an agent server following the recommendation of two PDF Worker agents per VM.

Please take the following into consideration for any sized environment:

For the File, Document, role, the type of storage system used will determine if you need to install the Windows operating system.

File (Document)

- Processor: 4 cores (2GHz)

- Memory: 4GB RAM

- Network: Gigabit Ethernet

- Storage: See Storage .

SMTP (Notification) Relativity requires an active SMTP server on your network. It interfaces with this server to send notifications and monthly billing statistics. The hardware requirements for this role are minimal. You can leverage an existing SMTP server in the network or merge this server with the agent server role.

### Storage

For each type of data, the amount of recommended space depends on the number of records imported, as well as the type and length of the expected reviews. Each server or VM needs space for the OS, page file, and Relativity installation files. For the Relativity Processing SQL Server, all the same SQL data is required with the exception of SQL Full Text Indexes. Throughput, especially when multiple SQL Servers or Data Grid Data Nodes are virtualized on a single host, should be put through a regiment of rigorous random and sequential read/write IO testing before installation of Relativity is completed.

Recommended space by data type:

Data Type 25-50 Named Users 100+ Named Users Disk I/O

SQL databases 500 GB 750 GB High

The databases can live across multiple storage volumes and SQL instances.

SQL full text indexes 150 GB 250 GB Moderate

Index size depends on the number of fields and records indexed.

SQL database logs 150 GB 250 GB High

Regular transaction log backups keep these values small and provide point in time recovery.

SQL Tempdb 80 GB 80 GB High

We recommend eight 10GB Tempdb data files for new deployments. SSDs recommended.

SQL backups 500 GB 1000 GB Low-High

We recommend having a backup strategy. This volume is not required. Larger data sizes may require higher I/O throughput.

dtSearch indexes 150 GB 250 GB Moderate

The dtSearch index share is typically stored in the same location as the files.

Analytics indexes 150 GB 250 GB High

The Analytics index volume is mounted to the Analytics virtual machine with speed and connectivity similar to that of SQL Server.

Files (natives/images) 1500 GB 3000 GB Low-High

The files may not require a Windows installation depending on the storage. Multiple Processing Workers online will require more file storage I/O.

Viewer cache

500 GB 1000 GB High

Temporarily store natives, images, productions, and other file types the viewer uses. It is recommended that the cache be stored on tier-one storage, SSDs, in environments with hundreds of concurrent users. Recommended 1TB viewer cache space available for every 100 concurrent users.

Agent (conversion) 250 GB 250 GB High

This is the Windows temp directory used during document conversion.

Worker (native

imaging/processing) 250 GB 250 GB High

This is the Windows temp directory used by native applications during imaging and processing. This temp location never exceeds 250 GB for each Worker server.

Data Grid data node 1 TB 1-10 TB High

## Infrastructure configuration

Relativity supports the following technologies as part of its infrastructure configuration:

- Virtualization —all aspects of Relativity can be virtualized. Some roles are more RAM and CPU intensive as others. You have to make sure when virtualizing Relativity that you do not over commit the RAM and CPU on a virtual machine to host ratio.

- High Availability (HA) —Relativity supports SQL Server Failover and File Server Clustering along with available hypervisor solutions.

- Disaster Recovery (DR) —Relativity supports Microsoft SQL Server mirroring, log shipping, and SAN replication technologies. These approaches typically require manual failover and increased downtime.

- Web Server Load Balancing —Relativity supports third-party load balancers, for example Windows Network Load Balancing (NLB). All load balancers require single affinity/sticky sessions/persistence. The Relativity User Load Balancer (RULB) provides the ability to distribute the user load evenly.

- Perimeter Networking (DMZ) —Relativity requires certain ports to remain open for proper server communication. For more details, download the Relativity Infrastructure Ports Diagram from the Relativity Community. Note that you must have a valid username and password to download this content.

### Guides for infrastructure management

Review the following guides to become familiar with best practices for managing the Relativity infrastructure:

- Pre-Installation

- Environment Optimization guide

- Infrastructure Planning Recommendations

## Software requirements

Relativity has specific software requirements for servers or virtual machines, user workstations, and the Relativity Desktop Client. The requirements for servers differ by the role assigned to them in your system configuration.

Make sure that you install the latest service packs and updates for your Windows Operating system and the latest service packs and cumulative updates for your SQL Server. However, compatibility for higher .NET versions is not guaranteed and we do not recommend installing higher .NET versions than what is listed as required by your Relativity version.

### System - servers or virtual machines

Relativity is compatible with local settings Only for webservice servers.

The general software requirements for servers and virtual machines include Microsoft Windows Server and .NET technologies. Microsoft Office and other applications are required for worker servers.

The following table provides software requirements by server role.

Server Role

Software Requirements

Web

-

Windows Server 2025, 2022, 2019, and 2016

- .NET 4.7.2, 4.8, or 4.8.1

- .NET 3.5

-

When adding a new server to your resource pool, ensure that you apply the same hotfix to the new server that you may have applied to any existing Web or Agent Servers.

- You must enable Long Path Support on all web and agent servers to support long file paths.

Agent

- Windows Server 2025, 2022, 2019, and 2016

- .NET 4.7.2, 4.8, or 4.8.1

- .NET 3.5

-

When adding a new server to your resource pool, ensure that you apply the same hotfix to the new server that you may have applied to any existing Web or Agent Servers.

- You may need to enable Long Path Support on Windows Server to support long file paths.

Analytics

-

Windows Server 2025, 2022, 2019, and 2016

-

.NET 4.7.2, 4.8, or 4.8.1

-

Java is already packaged with the Analytics installer, so it is not considered a separate requirement.

Secret Store

-

Windows Server 2025, 2022, 2019, and 2016

-

.NET 4.7.2, 4.8, or 4.8.1

-

.NET 3.5

Message broker

-

Windows Server 2025, 2022, 2019, and 2016

- .NET 4.7.2, 4.8, or 4.8.1

- .NET 3.5

- RabbitMQ - For more information, see RabbitMQ .

SQL

- Windows Server 2025, 2022, 2019, and 2016

- SQL Server 2022, SQL Server 2019, or SQL Server 2017

Due to issues found within email aliasing and name normalization, if you're running SQL Server 2019 on any SQL Server in your instance, you need to get Cumulative Update package 28 from Microsoft. To do so, see Cumulative Update 28 .

Relativity supports in-place upgrades from SQL 2016 to any higher supported version. For details on SQL Server upgrade, follow the EDDS migration Guide . To determine if you should upgrade your current SQL Server version to SQL Server 2019, contact Relativity Support .

- .NET 4.7.2, 4.8, or 4.8.1

- .NET 3.5

Additional considerations:

-

Each environment is different, research settings that your specific environment may utilize before performing any upgrades.

-

Ensure that you have tested backups before performing any upgrades.

-

Although an in-place SQL upgrade is supported by Relativity. Performing an EDDS migration is the cleanest way to perform a SQL upgrade.

Worker

Software Description

Required for system installation?

Required for Native Imaging/Processing

Windows Server 2022, Windows Server 2025

Required server software.

The Windows Print Spooler service must also be enabled on all Worker Server machines in the environment.

Windows Server Core is not supported.

Yes

.NET 4.7.2, 4.8, or 4.8.1

.NET 3.5

Required server software. Yes

Microsoft Office 2024 Professional Plus (32-bit)

Note the following:

-

If you are using Office 2024, Click-to-Run installations are supported, and it is the only option to install Office.

- There is no backwards compatibility for Microsoft Office versions. The versions listed here are the only ones supported.

This includes:

-

Excel—used for Processing and Native Imaging of most spreadsheet based documents .xlsx, .xlsm, .xlsb, .odc, .ods, and others.

- Word—used for Processing and Native Imaging of .docx, .docm, .dotx, .dotm, .doc, and others.

- Powerpoint—used for Processing and Native imaging of .pptx, .pptm, .ppsm, .potx, .potm, and others.

- Outlook - used for Processing and Native imaging of .msg, .pst, .ost, and others.

- OneNote—used for Processing and Native Imaging of .one and .tmp files, and others.

- Publisher—used for Processing and Native Imaging of .pub files and others. This is no longer supported in Office 2024.

The Courier New font must be installed on your machine. This font is installed by default when you install Microsoft Office, in which case you must ensure that you do not remove it.

Relativity does not support add-ins for Microsoft Office.

No

Yes

You are able to install the worker manager server without first installing Office.

Some features found in files created in different versions of Office may not be available or render correctly when processed or imaged using a different version than the file was originally created in. For more information about features differences between Office versions, please consult the appropriate Microsoft documentation.

Microsoft Works 6–9 File Converter The Microsoft Works Converter is also required. You can download it from the Relativity Community here . No Yes

Microsoft Visio 2024 Professional Used for processing and imaging .vsd, .vdx, .vss, .vsx, .vst, .vsw files.

No

No

Only required for processing and imaging .vsd, .vdx, .vss, .vsx, .vst, .vsw files. You can still install processing without this component, but you will not be able to process or image those files without it.

Microsoft Project Professional 2024 (32-bit) Used for processing and native imaging of .mpp files.

No

No

Only required for processing and imaging .mpp files. You can still install processing without this component, but you will not be able to process or image .mpp files without it.

(Optional) Lotus Notes v8.5 and higher

-

Lotus Notes v8.5.3 with Fix Pack 6

-

Lotus Notes v8.5.2 with Fix Pack 4

-

Lotus Notes v9.0

-

Lotus Notes v9.0.1

-

Lotus Notes v10.0.1

It is recommended that you install Lotus Notes 9 or higher on your workers, because Lotus Notes version 8.5.x cannot read certain Lotus 9 databases. Please note that some Lotus 9 databases cannot be opened in 8.5.x and will generate an error during processing.

No

No

When you install Lotus Notes, you need to restart the worker machine. There is no need to restart the queue manager service.

-

Solidworks eDrawings Viewer 2017 (64-bit) version only with SP5 or above.

-

Solidworks eDrawings Viewer 2018 (64-bit)

-

Solidworks eDrawings Viewer 2019

-

Solidworks eDrawings Viewer 2020

Used for processing, text extraction, and imaging for CAD files.

-

To download the viewer, go here .

-

Solidworks eDrawings Viewer 2017 SP5 and above is supported.

No

No

Only required for performing native imaging and text extraction on any supported CAD files in your data sources. You should install it only on the worker designated to perform these types of jobs. If you attempt to process a CAD file without the Solidworks viewer installed, you receive a simple document-level error prompting you to install it. Once you install the Solidworks viewer, you can retry that error and proceed with your processing job

JungUm Global Viewer v9.1 or higher This is required for processing and imaging GUL files, for Korean documents.

No

No

After you install the JungUm Global Viewer on the worker, you should restart the worker machine, but there is no need to restart the queue

### Workstations - end-user PCs

In Relativity, end users perform their reviews on workstations. Each workstation should be configured with a browser in which to use the Relativity web application, an operating system on which to run the Relativity Desktop Client, and the currently supported version of .NET.

#### Supported browsers for Relativity Web application

Software Latest Version Tested by Relativity

Chrome (Windows, Mac OSX) 130.0.6723.59

Edge (Windows, Mac OSX) 130.0.2849.52

Firefox (Windows, Mac OSX) 131.0.3

Safari (Mac OSX) 18.1

Relativity does not currently support the Linux operating system for any browser.

#### Supported .NET version

-

.NET 4.7.2, 4.8, or 4.8.1

-

.NET 3.5

### Relativity Desktop Client

The Relativity Desktop Client (RDC) is a utility used for importing and exporting documents, images, natives, and productions. This utility requires the following software:

The RDC requires Microsoft .NET 4.7.2 and Visual C++ 2015 Redistributable Update 3 RC.

Your operating system determines whether you need to download the 64-bit or 32-bit version of these applications:

- If you're running a 32-bit machine, you must install the RDC 32-bit and the Visual C++ 2015 Redistributable Update 3 RC. For more information, see Microsoft Visual C++ 2015 Redistributable Update 3 RC .

- If you're running a 64-bit machine, you want to install the RDC 64-bit and the Visual C++ 2015 Redistributable Update 3 RC You may notice a significant improvement in the speed of the RDC with the 64-bit version. However, a 64-bit machine can have both the x86 and x64 redistributables installed at the same time, and it can run the 32-bit or 64-bit version of the RDC.

While the RDC primarily uses Visual C++ 2015 Redistributables, certain internal dependencies also require Visual C++ 2010 Redistributables to be present. Ensure both versions are installed to avoid any disruption in RDC functionality. Relativity is actively working to transition all dependencies to fully supported versions in a future release.

# Licensing Microsoft products

Relativity requires Microsoft Windows and Microsoft SQL Server, both of which you need to license through Microsoft or one of their resellers. If using Relativity Processing or Native Imaging, you also need to license Microsoft Office, Visio, and Project through Microsoft or one of their resellers.

If Relativity is hosted for external customers, you may need to license Microsoft products through Microsoft’s SPLA (Service Provider License Agreement). You can find more information about Microsoft’s SPLA program on Microsoft’s Hosting site .

We recommend contacting Microsoft, or one of their resellers, for guidance on the licensing options available.

This section outlines requirements and recommendations for a workstation used to access Relativity.

## Resolution Support

Relativity is supported in the following resolutions:

- Standard resolution: 1920x1080

- Smallest resolution: 1366x768

- Largest resolution: 2560x1440

## Minimum workstation configuration

- 512MB SDR memory

- Intel Pentium 3 or equivalent

## Recommended workstation configuration

- Minimum of 5 GB DDR memory

- Recommended 8GB DDR memory

- Intel Pentium 4/AMD Athlon XP

## Relativity help site requirements

For the best experience viewing the Relativity online documentation website, we recommend using one of the following browsers:

- Firefox 10 or above

- Google Chrome 13 or above

- Safari 5 or above

In some cases, browser hardware acceleration can cause font rendering issues with the PDF.js library used to display PDF files. In these cases, disabling hardware acceleration in the browser settings (e.g. Chrome->settings->system->use hardware acceleration when available) will resolve the issue.

To print pages from this website, use the button in the upper left corner of the content pane.

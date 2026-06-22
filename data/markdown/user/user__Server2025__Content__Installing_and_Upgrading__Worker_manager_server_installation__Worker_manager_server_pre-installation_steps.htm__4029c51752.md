---
title: "Worker manager server pre-installation steps"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Worker_manager_server_installation/Worker_manager_server_pre-installation_steps.htm
collection: user
fetched_at: 2026-06-22T06:04:03+00:00
sha256: d9103d8a357993b91fb8c9a9eaaefef61817150f75c436da99e2861981767ec1
---

Worker manager server pre-installation steps Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Worker manager server pre-installation steps

Before you begin installing the worker manager server, you must update your environment with the required security and other configuration settings. See System requirements .

This documentation contains references to third-party software, or technologies. While efforts are made to keep third-party references updated, the images, documentation, or guidance in this topic may not accurately represent the current behavior or user interfaces of the third-party software. For more considerations regarding third-party software, such as copyright and ownership, see Terms of Use .

## Install Relativity

Before you install the worker manager server, make sure that you install Relativity. For more information, see Relativity installation.

## Required software on the worker

The following software is required on the worker server for processing or native imaging. While you may not being processing files corresponding to some of the required software listed below, note that some of those components are still required for system use.

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

Note that the worker, database, and queue manager do not all require the same number of software components. The following table breaks down which part of the processing infrastructure requires which software component.

Processing infrastructure component Software component

Worker See Required permissions .

Database

- Windows Server 2016, 2019, 2022, 2025

Queue manager

- Windows Server 2016, 2019, 2022, 2025

- .NET Version 4.7.2, 4.8, or 4.8.1

Windows Server 2025 is supported for Relativity Server 2025.

## Required permissions

You must set the security permissions required for installing Invariant components. The Relativity Service account must have these permissions, as the Queue Manager and workers are required to run under this account.

You are not required to install the Invariant database and Queue Manager on the same server, but you have the option of doing so. The servers that you install to must have the permissions listed under the Database and Queue Manager sections, respectively.

### Database

The following permissions are required to install the Invariant Database:

- Domain Rights —the account used for installing the database must have read and write permissions to the path entered in the Invariant Worker Network File Path share in the installation wizard.

- Server Administrator Rights —the account used for installing the database must have the following server administration rights:

- Domain or Workgroup Member —if the server is a member of a Domain, this account must also be a Domain user. If the server is a member of a Workgroup, this account must be a local user.

- Local Administration Rights —the account used for installation must have local administration rights on the server. It can also be in the Domain administrator group with local administrator rights on the server.

- SQL Administrator Rights —the installer can use Windows or SQL authentication to log in to the SQL Server. This account must have sysadmin permissions on the SQL Server.

### Queue Manager

The Queue Manager is required to run under the Relativity Service account. This account must have the following permissions on the machine where the Queue Manager is installed:

- Server Administrator Rights —the Relativity Service account must have the following server administration rights:

- Domain or Workgroup Member —if the server is a member of a Domain, the Relativity Service account must also be a Domain user. If the server is a member of a Workgroup, the Relativity Service account must be a local user.

- Local Administration Rights —the Relativity Service account must also have local administration rights on the server. It can also be in the Domain administrator group with local administrator rights on the server.

- SQL Administrator Rights —the Queue Manager Service account runs as the Relativity Service account, and uses the EDDSDBO account to log in to the SQL Server. Neither account requires administrator rights to the SQL Server.

### Workers

Workers are required to run under the Relativity Service account. This account must have the following permissions on the machine where a worker is installed:

- Domain Rights —the Relativity Service account must have read and write permissions to the path entered in the Invariant Worker Network File Path share during installation.

- Server Administrator Rights —the Relativity Service account must have the following server administration rights:

- Domain or Workgroup Member —if the server is a member of a Domain, the Relativity Service account must also be a Domain user. If the server is a member of a Workgroup, the Relativity Service account must be a local user.

-

Local Administration Rights —the Relativity Service account must also have local administration rights on the server. It can also be in the Domain administrator group with local administrator rights on the server.

The Relativity Service account must have rights to the network directory created for the database installation, as well as to other network locations used to store files, which the workers need to access.

A local user account may also be configured on each worker machine to allow secure file conversion operations for Processing. Note the following details:

- The user account must be able to read and write local temporary files.

- The user account is not required to have permissions to access a file share or network.

- A single account name and password will be used for all workers in use by Invariant.

- The user account name and password must be stored in the Relativity Secret Store for Processing access. For more information on storing this information, see Installing the worker manager server Installing the worker manager server .

## Environment configuration steps

Before running the Invariant installer, you must perform the following steps to modify your environment.

Component Environment Configuration Settings

Database

Disable User Access Control (UAC) and the Windows Firewall.

Queue Manager None

Workers

- Disable User Access Control (UAC) and the Windows Firewall. Disabling UAC on the worker server suppress pop-ups from the application in which the processing engine opens files.

- Set Windows Updates to download, but allow you to choose whether to install. You can set this option through the Control Panel under System and Security.

## Database file and network folders setup

During the installation of the Invariant Database and Queue Manager, you need to provide the file paths to the folders used for database and worker files. Create the following folders before you begin the installation.

- MDF File Folder —create this folder as a local directory on the SQL Server. It is used for Invariant and Relativity Imaging database files. You can add this folder to a different drive than Invariant database, but it must be local to the machine.

- LDF File Folder —create this folder as a local directory on the SQL Server. It is used for Invariant and Relativity Imaging log files. You can add this folder to a different drive than Invariant database, but it must be local to the machine.

- Network Directory —create a local network directory on the SQL Server. The Relativity Service account must have read and write permissions to this network share. The installer adds files required by the Invariant Workers to this folder. You will enter the path to this directory in the Invariant Worker Network File Path box during installation.

The Invariant worker share should be around 10 GB, since it does not contain data that grows with use.

## Enabling token authentication

You must enable token authentication on your web server for certain Relativity features, such as the worker manager server, which requires this authentication type for processing.

You must also edit the ProcessingWebAPIPath Instance Setting. This setting identifies the URL that directs to the Relativity token-authenticated endpoints that Invariant uses to process and image files. Invariant requires this URL and a Relativity admin must enter it.

To do this, perform the following steps to comply with this change:

- While in Home mode, navigate to the Instance Settings sub-tab.

- In the default All Instance Settings view, enable filters and enter ProcessingWebAPIPath in the Name field.

- Click the ProcessingWebAPIPath name and click Edit in the instance setting layout.

- In the Value field change the existing ProcessingWebAPI URL to the RelativityWebAPI URL.

- Click Save .

Depending on what Relativity version you're installing or upgrading, you may need to enable the RelativityWebAPI setting in IIS for Anonymous authentication in order to publish documents to a workspace.

To do this, perform the following steps:

- Open IIS.

- To enable anonymous authentication, complete the following steps:

- Click on the RelativityWebAPI site.

- In the Features view, click Authentication .

- In the Authentication view, right-click on Anonymous Authentication and click Enable.

- To update the web.config file, locate it in the following folder:

C:\Program Files\Relativity Corporation\Relativity\WebAPI

- Open the file in an editor. Update the authentication mode and authorization sections as follows:

```text
<system.web>
     <authentication mode="None" />
     <authorization><allow users="*" />
</authorization>
</system.web>
```

- Restart IIS.

## Installation setting for Microsoft Office Professional 2016

When you install Microsoft Office, you must use the following setting to ensure that Invariant can extract text and create TIFFs form WordPerfect documents.

Run the installer for Microsoft Office. On the Installation Options tab, point to Office Shared Features . Point to Converters and Filters , and select Run all from My Computer .

## Installing Microsoft Visual C++ Redistributable Packages

The following table breaks down which versions of Microsoft Visual C++ are required for which versions of Relativity/Invariant. Note that you are required to install each version of Microsoft Visual C++ only if you are upgrading to the Relativity/Invariant version listed and not if you are installing it for the first time.

Required Microsoft Visual C++ version (Redistributable x86 and x64)

Relativity/Invariant version 2010 2012 2013 2015

Server 2022/7.1.431.1 √ √ √ √

Server 2023/ 7.3.841.24 √ √ √ √

Server 2024/ √ √ √ √

On this page

- Worker manager server pre-installation steps

- Install Relativity

- Required software on the worker

- Required permissions

- Database

- Queue Manager

- Workers

- Environment configuration steps

- Database file and network folders setup

- Enabling token authentication

- Installation setting for Microsoft Office Professional 2016

- Installing Microsoft Visual C++ Redistributable Packages


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

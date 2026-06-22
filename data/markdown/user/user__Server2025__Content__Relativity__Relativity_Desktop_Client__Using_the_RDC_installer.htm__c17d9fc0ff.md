---
title: "Using the RDC installer"
url: https://help.relativity.com/Server2025/Content/Relativity/Relativity_Desktop_Client/Using_the_RDC_installer.htm
collection: user
fetched_at: 2026-06-22T06:14:42+00:00
sha256: 2c4b32c157f9a6323ecaa70bdeca21ede1c4d785038e3bdbbe34f6cbcb00b2b5
---

Using the RDC installer Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Using the RDC installer

To use the Relativity Desktop Client (RDC), you must download a copy of the RDC installer and then install it.

To ensure a safe and stable product experience, effective with the Server 2024 release, we only support the version of RDC that was shipped with the current release as well as one release back. For example, Server 2024 RDC will work with both Server 2023 and Server 2024 but not with any releases prior to Server 2023.

## Software requirements

The RDC installer checks for the software prerequisites. If you're missing any of the prerequisites, your computer must have Internet access, so the RDC installer can fetch the required software. If your computer doesn't have Internet access, the RDC installer can't fetch the required software, so the installation fails.

You do not need Internet access to install the RDC if your computer has all the prerequisites.

The RDC requires the following software:

- Microsoft .NET 4.6.2 or above - For additional information about operating system requirements, see Relativity compatibility matrix .

- Redistributables listed in the following table:

Operating System VC++2010 (x86) VC++2010 (x64) VC++2017 (x86) VC++2017 (x64)

32-bit ✓ ✓

64-bit ✓ ✓ ✓ ✓

If you need to perform an offline installation, you must manually install the software required for the RDC listed in this section.

## Downloading the RDC installer

To use RDC, you must first download a single executable file that runs on both 32-bit and 64-bit operating systems.

To download the RDC installer file:

- Open your workspace in Relativity.

- Select the Workspace Admin tab.

- Click Workspace Details to display the Relativity Utilities Console.

- Click Relativity Desktop Client under the Relativity Downloads selection. Relativity downloads the Relativity.Desktop.Client.Setup.exe .

- Complete the steps for installing the RDC. See Installing the RDC for more information.

## Installing the RDC

After downloading the installer file, you can proceed with installing it.

To install the RDC:

- Complete the steps to download the Relativity.Desktop.Client.Setup.exe in Downloading the RDC installer .

- Double-click on Relativity.Desktop.Client.Setup.exe to launch the installer.

- If you want to specify an installation location, complete these steps:

- Click Options .

- Click Browse to select a directory where you want the RDC installed. The default installation directories include:

32-bit —C:\Program Files (x86)\kCura Corporation\Relativity Desktop Client

64-bit —C:\Program Files\kCura Corporation\Relativity Desktop Client

- Click OK .

The RDC installer checks for the software prerequisites. If you're missing any of the prerequisites, your computer must have Internet access, so the RDC installer can fetch the required software. If your computer doesn't have Internet access, the RDC installer can't fetch the required software, so the installation fails.

You don't need Internet access to install the RDC if your computer has all the prerequisites.

- Click Install on the RDC setup wizard to start the installation.

- Click Close when the installation has completed.

The executable for the RDC has been renamed to Relativity.Desktop.Client.exe . If you use an antivirus scan in your environment, you may want to update your settings to accommodate the renamed RDC executable.

Your desktop now displays a shortcut icon for the RDC, which you can click to launch it.

## Installing the RDC in quiet mode

You can use quiet mode to run unattended RDC installations through the command line. Open a command prompt and enter the following:

```text
Relativity.Desktop.Client.exe /q /log InstallLog.txt /INSTALLFOLDER "<RDC_Installation_Directory>"
```

This command takes the following parameters.

Parameter Description

/INSTALLFOLDER Specifies a custom installation path. This parameter is optional.

/log Used to create a log file. Specify a file name and path for the log file. This parameter is optional.

/q Runs the installation in quiet mode.

## Repairing or removing RDC installation

You can also run the installer to repair, or remove an existing installation of the RDC. Run the installer on a machine where the application is installed. Select one of the following options:

- Repair —attempts to fix errors in the most recent installation.

- Uninstall —removes the RDC from your machine.

On this page

- Using the RDC installer

- Software requirements

- Downloading the RDC installer

- Installing the RDC

- Installing the RDC in quiet mode

- Repairing or removing RDC installation


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

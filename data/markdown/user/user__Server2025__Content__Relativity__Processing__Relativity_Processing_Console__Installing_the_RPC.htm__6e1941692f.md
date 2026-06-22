---
title: "Installing the RPC"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Relativity_Processing_Console/Installing_the_RPC.htm
collection: user
fetched_at: 2026-06-22T06:13:42+00:00
sha256: 5e74021ef0ec6ebcf4d100a890b7b89613188a1d1a27b3368e334d10f3c07545
---

Installing the RPC

# Installing the RPC

Before you begin installing the Relativity Processing Console (RPC), you must update your environment with the required security and other configuration settings. See System requirements .

## Licensing

You must have a Processing license and be running Server 2025 or above in order to use the Relativity Processing Console. See Licensing .

## Distribution

For RPC distribution, contact Customer Support .

## Pre-installation requirements

The RPC is an application that you can install to your desktop on a local machine or to the same server on which the Queue Manager is installed. The machine must be on the same domain as the processing worker and file servers, and the SQL Server.

Before running the RPC installer, verify that the items in the following checklists have been completed. This ensures that you won't encounter any disruptions during the RPC installation process:

Web UI Done

You’re running Relativity 8.2 or above.

Processing is installed to at least one workspace.

You have a valid Processing license.

The RPC version matches the Invariant version.

At least one Worker is running and is designated for processing work.

The version of Processing installed via the Servers tab is correct.

The version of the RPC Installation package corresponds to the Relativity version.

IE Enhanced Security Configuration is off.

Authentication process is now mandate client registration.

Use of a local admin user account, and running RPC with Run as administrator .

Processing SQL Server Done

In SQL Server Management Studio, the DataFiles location is set in the Invariant.dbo.AppSettings table. This should be a network share accessible to the Relativity Service Account:

SELECT Value1 from Invariant.dbo.AppSettings

WHERE Category = 'DataFiles'

In SQL Server Management Studio, the dtSearchPath location is set in the Invariant.dbo.AppSettings table. This should be a network share accessible to the Relativity Service Account:

SELECT Value1 from Invariant.dbo.AppSettings

WHERE Category = 'dtSearchPath'

In SQL Server Management Studio, the IdentityServerURL is set correctly in the Invariant.dbo.AppSettings table. This value is case sensitive. If it isn't entered in the proper case, you can run the following statement to capitalize "relativity":

```text
--begin tran
--update Invariant.dbo.AppSettings
--set Value1 = 'https://<WebServerName>/Relativity/Identity'
--where Category = 'IdentityServerURL'
--commit

```

The user (or group) account running the RPC from the desktop has access to SQL Server Management Studio via Windows Authentication and has to have the following server roles assigned:

- bulkadmin

- dbcreator

- public

All pre-existing and newly created processing server databases (Invariant and Store databases) have RPC users mapped to the SQL Server logins with the db_owner permission set.

Local machine Done

The account you're logged in to has a Windows Authentication login on the Processing SQL Server.

The account running the RPC is a local administrator on the worker servers. This is required to stop a worker and take a worker offline.

The following four SQL CLR type packages are installed locally, as well as the Microsoft Report Viewer 2012. These must be installed before you install the Microsoft Report Viewer 2012:

- CLR Types for SQL 2012 (x86 32 bit)

- CLR Types for SQL 2012 (64-bit)

The Microsoft Report Viewer 2012 is installed locally:

- Microsoft Report Viewer 2012

- Before running the RPC installer, you are required to first whitelist and then register any processing-related machines for the Secret Store so that those machines can read and write to and from the store. This includes the Invariant queue manager, all workers, and all machines on which the RPC is installed. See Secret Store for more information on configuring servers for the Secret Store.

Once you've verified or completed all of the above items, you can move on to running the RPC installer.

## Installing the RPC

The RPC is available in a 64-bit version and is only available on a local install, not on a network install.

To install the RPC:

- Log in to the machine with the local admin account where you want to install the RPC.

- Open the installer executable to launch the setup wizard.

- Click Next on the Welcome screen.

- Enter the installation directory for the RPC. This path must be 200 characters or fewer.

- Click Next and enter the following database information:

- Invariant instance database server name with the optional port number

- Relativity instance database server name with the optional port number

- Sql username must be EDDSDBO

- Sql password

- Click Next and then click Install .

## Validating the RPC installation

Before you can use the RPC for the first time, you must successfully submit one processing or inventory job from Processing.

## Repairing or uninstalling the RPC

Use the installation wizard to repair or uninstall the RPC and the Queue Manager Server.

- Log in to the machine with the local admin account where the RPC and the Queue Manager are installed.

- Open the installer executable to launch the setup wizard.

- Click Next on the Maintenance screen.

- Click Repair or Remove to modify your installation.

- Repair - click this button to repair your RPC installation. The installer adds a fresh copy of any deleted RPC files, but it doesn't make any configuration changes or replace other files that already exist. On the Ready to Repair the RPC window, click Repair .

- Remove - click this button to uninstall all RPC components from your machine. On the Ready to Remove the RPC window, click Remove .

## Upgrading the RPC

To upgrade the RPC, run the latest version's installer. You don't need to uninstall your current RPC version.

---
title: "Installing Integration Points"
url: https://help.relativity.com/Server2025/Content/Relativity/Integration_Points/Installing_Integration_Points.htm
collection: user
fetched_at: 2026-06-22T06:09:23+00:00
sha256: 302893568764301484682d75bd388517364e7e6d2a3cf169b27a38dbcd9f0a6b
---

Installing Integration Points Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Installing Integration Points

To successfully use Integration Points, you need to install the Integration Points application to at least one workspace.

## System requirements and specifications

You must have the following in order to use Integration Points:

Processing is not required to use Integration Points.

- Integration Points has the same system requirements as its compatible Relativity version. See the System requirements .

- The WebAPIPath instance setting in the kCura.IntegrationPoints section configured correctly. Note that this path is case sensitive.

## Installing Integration Points

Since Integration Points uses the ADS framework, you have the following options available for installing Integration Points in your environment. See Relativity applications .

- Install Integration Points from the Application Library - If you add the Integration Points application to the Application Library, you can install it to the current workspace, or to multiple workspaces at once, from the Application Library.

- Install Integration Points from an external file - You can import the Integration Points application into your workspace from an external file if it has not been added to the Application Library.

Once you install Integration Points application, the necessary Integration Points agents will be deployed automatically.

## Accessing Integration Points

Once you have installed Integration Points, the Integration Points application tab appears in your workspace.

## Security permissions

The following tables provide detailed breakdowns of the security permissions required to use Integration Points.

To submit a job for a non-Relativity source provider (FTP, LDAP, or Load File) and display console errors for that job, you need the following permissions:

Workspace

Object/operation/tab

Permission type

Source

Workspace

View, Edit, Add

Source

Integration point

View

Source

Job History

View, Edit, Add

Source

Destination Provider

View

Source

Source Provider

View

Source

Integration Point Type

View

Destination

Destination RDO

View, Edit, Add

Destination

Allow Import

Admin operation

To submit a job with Relativity as the source provider and display console errors for that job, you need the following permissions:

Workspace

Object/operation/tab

Permission type

Source

Workspace

View, Edit, Add

Source

Integration point

View

Source

Job History

View, Edit, Add

Source

Destination Provider

View

Source

Source Provider

View

Source

Integration Point Type

View

Source

Document

View, Edit

Source

Search

View, Edit, Add

Source

Advanced & Saved Searches

- The saved search that you use for the integration point must have an owner of Public.

Browser

Source View Workspace Details

Admin operation

Destination

Destination Workspace

View, Edit, Add

Destination

Allow Export

Admin operation

Destination View Workspace Details

Admin operation

If you are creating an integration point for a non-Relativity source provider (FTP, LDAP, or Load File), Relativity assumes you have the following system admin permissions:

Workspace

Object/operation/tab

Permission type

Source

Integration point

View, Edit

- Edit is required for adding Job History RDO’s.

Source

Job History

View, Edit, Add

Source

Job History Error

View, Edit, Add

- Edit is required to mark errors as new and expired

If you are creating an integration point with Relativity as the source provider, Relativity assumes you have the following system admin permissions:

Workspace

Object/operation/tab

Permission type

Source

Destination workspace

View, Edit, Add

- Edit is required to rename destination workspaces.

Destination

Manage Object Types

- This is required to create new object types.

Admin operation

Destination

Source workspace

Add, Edit

- Edit is required for situations when Relativity renames the destination workspace upon a source workspace name change.

Destination

Source job

Add

To view an integration point with any source provider, you need the following permissions:

Workspace

Object/operation/tab

Permission type

Source

Job History

View

Source

Integration point

View

Source

Integration point type

View

To create and edit an integration point with any source provider, you need the following permissions:

Workspace

Object/operation/tab

Permission type

Source

Integration point

View, Edit, Add

- Edit is only required if you're editing the integration point.

- Add is only required if you're creating the integration point.

Source

Integration point type

View

Destination

Allow Import

Admin operation

To create an integration point with a Relativity source provider, you need the following permissions:

Workspace

Object/operation/tab

Permission type

Source

Allow Import

Admin operation

To create an integration point with any source provider from an integration point profile, you need the following permissions:

Workspace

Object/operation/tab

Permission type

Source

Integration point profile

View

To view any integration point profile, you need the following permissions:

Workspace

Object/operation/tab

Permission type

Source

Integration point profile

View

Source

Source provider

View

Source

Destination provider

View

Source

Integration point type

View

To create and edit an integration points profile with any source provider, you need the following permissions:

Workspace

Object/operation/tab

Permission type

Source

Integration Point Profile

View, Edit, Add

- Edit is only required if you're editing the integration point profile.

- Add is only required is you're creating the integration point profile.

Source

Integration Point Type

View

Source

Source Provider

View

Source

Destination Provider

View

Destination

Allow Import

Admin operation

To create and edit an integration points profile with a Relativity source provider, you need the following permissions:

Workspace

Object/operation/tab

Permission type

Source

Allow Import

Admin operation

If you do not have sufficient permissions and you attempt to perform either of the following actions, you will see an error message stating "You do not have sufficient permissions. Please contact your system administrator." In each case, Relativity creates an error listing all missing permissions.

- Loading the integration points console or clicking Run Now or Retry:

- If the error occurs after a button click, the message is prefixed with, "Failed to submit integration job."

- If the job is a retry job, the prefix reads, "Failed to submit the retry job."

- Saving an integration point after creating a new one or editing an existing one.

Integration points is tenant-aware. This means that workspace admins within a tenancy receive an error if they attempt to push to a workspace they do not have permissions to. This error occurs when they click Run Now on the integration point that they create to push documents to review.

## Troubleshooting

If you encounter issues with Integration Points while seeing either of the errors listed below, you must install the certificates that you are using for HTTPS on your web server to the trusted root certificate store on all Relativity Servers in your environment. If this doesn’t work, restart the kCura Service Host Manager and kCura Agent Manager windows services.

- On import - No WebApi nor Kepler service found to perform the request. at Relativity.DataExchange.Service.WebApiVsKeplerSwitch.WebApiVsKepler.UseKepler() at kCura.WinEDDS.Service.Kepler.WebApiVsKeplerFactory.UseKepler(Uri webApiUrl, NetworkCredential credentials, Func`1 getCorrelationId) at System.Lazy`1.CreateValue()...

- On export - Relativity.Sync.SyncException: Sync job failed. See inner exceptions for more details. ---> System.AggregateException: One or more errors occurred. ---> kCura.WinEDDS.Exceptions.InvalidLoginException: Login failed. ---> System.Exception: Unknown failure during authentication ---> ...

On this page

- Installing Integration Points

- System requirements and specifications

- Installing Integration Points

- Accessing Integration Points

- Security permissions

- Troubleshooting


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

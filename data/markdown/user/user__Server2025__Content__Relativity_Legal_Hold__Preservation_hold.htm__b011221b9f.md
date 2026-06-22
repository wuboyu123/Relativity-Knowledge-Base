---
title: "Preservation hold"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Preservation_hold.htm
collection: user
fetched_at: 2026-06-22T06:13:21+00:00
sha256: 91110b73eb40eed5377c5870f3345a46e87678b163048d22bdee700c37e2c8c5
---

Preservation hold Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Creating a preservation hold case

A preservation hold preserves files and emails in an custodian's Microsoft 365 account, OneDrive and Exchange, as well as any files in an custodian's Sharepoint. A preservation hold ensures that original copies, prior to any edits or deletions, of emails and files are preserved in a Microsoft 365 Preservation Library. The Preservation Library ensures that there is no loss of data through accidental or willful deletion or editing of items under a Preservation Hold. Preservation Holds are transparent to custodians. For more information on the Security and Compliance Center, see Microsoft 365 Security Compliance Center .

A custodian can be active in multiple projects and can be on multiple preservation holds. If one preservation hold is removed, another could still be in place. When a preservation hold is removed in Relativity, only that one preservation hold is removed in Security & Compliance Center.

Enable the Preservation Hold Settings security permission in order to create a Preservation Hold Setting. For more information on security permissions, see Legal Hold Application Permissions .

A custodian can be active in multiple projects and can be on multiple preservation holds. If one preservation hold is removed, another could still be in place. When a preservation hold is removed in Relativity, only that one preservation hold is removed in Security & Compliance Center.

Before creating a Preservation Hold, add a Preservation Hold Setting. Fill out the information for the Preservation Hold Setting to create a data source in which preservation holds will be created. To learn more about Preservation Hold Settings, see Adding preservation hold settings .

## Adding a preservation hold to a project

In the Projects edit layout, there is a Preservation Case field. Enter the created Preservation Hold Setting to the Preservation Case. To create a Preservation Case, follow the steps below:

- Click the Add link next to Preservation Case.

- Enter a name into the Preservation Case Name field in the Preservation Case pop-up menu. For more information, see Adding a preservation case .

- Click the Preservation Sources button.

- In the Preservation Sources pop-up menu, click the check boxes next to the necessary Preservation Hold Settings.

- Click Add .

- Click Save .

- Fill out rest of the Preservation Case fields. For more information on the Preservation Case fields, see Adding a preservation case .

- Click Save .

## Adding a preservation case

Add a Preservation Case to the project to specify the data sources for the preservation holds.

## Permissions

Enable the Preservation Hold security permission to add, edit, or remove Preservation Holds within projects.. For more information on security permissions, see Legal Hold Application Permissions .

## Prerequisites

Before creating a Preservation Hold, add a Preservation Hold Setting. Fill out the information for the Preservation Hold Setting to create a data source in which preservation holds will be created. To learn more about Preservation Hold Settings, see Adding preservation hold settings .

## Considerations

Before adding a preservation, consider the following list. If a data source is not listed, there are no considerations or limitations.

Microsoft 365

If you want to preserve data in multiple tenants, you must create two separate legal hold projects. One project for each tenant.

You must have a user account must with modern authentication to be able to preserve in Microsoft. With modern authentication, you must have an Exchange Administrator to configure preservation holds.

The service account, URL, and other items related to Relativity's implementation of preservation cannot be made more secure than what is currently available.

Microsoft Archived mailbox

The configuration on your SharePoint site can cause performance limitations. The larger the Sharepoint footprint, the less performant preservation is.

Microsoft Teams

You can preserve data in one-on-one chats only. Teams Channels, group chats, are not preserved because channels are not tied to individual custodian mailboxes. Microsoft stores Teams Channel data in Sharepoint. They are stored in Group Mailboxes.

You can preserve Teams Channel attachments if you know which SharePoint site they reside on.

You must target OneDrive to collect all Teams data. Microsoft preserves Teams messages in a custodian’s Outlook mailbox. Microsoft preserves Teams message attachments in a custodian’s OneDrive.

## Adding a preservation hold to a project

In the Projects edit layout, there is a Preservation Case field. Enter the created Preservation Hold Setting to the Preservation Case. To create a preservation case, follow the steps below:

- Click the Add link next to Preservation Case.

- Enter a name into the Preservation Case Name field in the Preservation Case pop-up menu. Use alphanumeric characters only. For more information, see Adding a preservation case .

- Click the Preservation Sources button.

- In the Preservation Sources pop-up menu, click the check boxes next to the necessary Preservation Hold Settings.

- Click Add .

- Click Save .

- Fill out rest of the Preservation Case fields. For more information on the Preservation Case fields, see Adding a preservation case .

- Click Save .

## Adding a preservation case

Add a Preservation Case to the project to specify the data sources for the preservation holds.

- Name —the name of the Preservation Case. Use alphanumeric characters only.

- Preservation Source —the data sources created in Preservation Hold Settings for the Preservation Hold. For more information on Preservation Hold Settings, see Adding preservation hold settings using Modern Authentication .

- Retry Count —the number of times Legal Hold will retry to correct a failed Preservation Hold process.

- Retry Interval (Minutes) —the number of minutes between each retry.

- Monitoring Interval (Hours) —the number of hours between each time Legal Hold monitors Microsoft 365 for deletions/disabling or edits to filter criteria made within Microsoft 365 Security & Compliance Center. Default is 0 hours, meaning no monitoring by default.

- Start Date —(optional) a preservation filter criteria that preserves data starting with this date. If no date is entered, all data will be preserved.

- End Date —(optional) a preservation filter criteria that preserves data ending with this date. If no date is entered, all data will be preserved.

- Auto-discover targets —the option to catalog all the SharePoint sites that custodians on the legal hold have access to in your Microsoft 365 environment. Once SharePoint sites are discovered, you will need to proactively select the sites to place on preservation hold using the Select Targets Project console button.

If you do not know if you need to preserve SharePoint data immediately, do not enable this field. You can manually start the process from the Project console. For more information, see Manage preservation targets .

- Re-discover wait window (hours) —the number of hours between each rediscovery process.

## Preservation hold status

After running a preservation hold, a status of the hold available in the Preservation Hold section on the Projects tab. Any changes made to the preservation is reflected within an hour. For a list of the statuses available, see below:

- Pending —Relativity is creating the preservation hold in Microsoft 365.

- Pending - Retry —Relativity encountered a problem creating the hold, now retrying.

- Pending - Error —all retries failed and Relativity is unable to create the preservation hold.

- On Hold —Relativity successfully placed the custodian data source on a preservation hold.

- Releasing —Relativity is in the process of deleting or disabling the hold in Microsoft 365.

- Releasing - Retry —Relativity encountered a problem deleting or disabling the hold and is retrying to create the preservation hold.

- Releasing - Error —all retries failed and Relativity is unable to delete or disable the preservation hold.

- Off Hold —the custodian data source is no longer on a preservation hold.

- Externally Modified —a user or some process outside of Relativity altered the filter criteria affecting the case or holds. (e.g. User in Security & Compliance Center).

- Externally Removed —a user or some process outside of Relativity deleted or disabled the preservation hold (e.g. User in Security & Compliance Center).

## Preservation target status

The Preservation Target Status tab shares the progress of the target discovery for each custodian. The discovery process is the inventorying of the sites each custodian has access to. This status indicates where in the discovery process the targets are. The statuses are:

- Scheduled To Be Discovered —the preservation targets will be discovered after other targets have completed.

- Discovered —the preservation targets have been discovered. Once complete each custodian assigned to the project, you can view a list of all SharePoint sites each custodian has access to and select the target you want to preserve by using the Project console. For more information, see Selecting SharePoint targets .

- Error —the preservation targets have not been discovered due to an error. For information on fixing preservation target errors, click the Discover Targets button in the Project Console. For information, see Project console .

## Manage preservation targets

Manage SharePoint preservation targets after they have been discovered. The following buttons are available in the Project console:

- Discover Targets —manually start the Sharepoint preservation target discovery process for the project's custodians. Can use to retry errors.

- Select Targets —select Custodian's SharePoint target sites to be placed on a preservation hold. Access to the button when the custodian discovery status is Discovered . To learn how to select targets, follow the steps in Selecting SharePoint targets .

The length of the SharePoint targets discovery process in your environment depends on the size of your Microsoft 365 environment. Size depends on the number of users and how many custodians are on hold.

##### Selecting SharePoint targets

After discovering SharePoint targets, you need to select targets based on SharePoint URLs associated to a custodian.

To select targets, follow the steps below.

-

Click the Select Targets console button.

-

In the Select window, select the check boxes next to the custodian name and target URL you want to put on a preservation hold.

-

Use the arrows to select the custodians.

-

Click Select Targets .

- Re-discover wait window (hours) —the number of hours between each rediscovery process.

## Preservation hold status

After running a preservation hold, a status of the hold available in the Preservation Hold section on the Projects tab. Any changes made to the preservation is reflected within an hour. For a list of the statuses available, see below:

- Pending —Relativity is creating the preservation hold in Microsoft 365.

- Pending - Retry —Relativity encountered a problem creating the hold, now retrying.

- Pending - Error —all retries failed and Relativity is unable to create the preservation hold.

- On Hold —Relativity successfully placed the custodian data source on a preservation hold.

- Releasing —Relativity is in the process of deleting or disabling the hold in Microsoft 365.

- Releasing - Retry —Relativity encountered a problem deleting or disabling the hold and is retrying to create the preservation hold.

- Releasing - Error —all retries failed and Relativity is unable to delete or disable the preservation hold.

- Off Hold —the custodian data source is no longer on a preservation hold.

- Externally Modified —a user or some process outside of Relativity altered the filter criteria affecting the case or holds. (e.g. User in Security & Compliance Center).

- Externally Removed —a user or some process outside of Relativity deleted or disabled the preservation hold (e.g. User in Security & Compliance Center).

## Preservation target status

The Preservation Target Status tab shares the progress of the target discovery for each custodian. The discovery process is the inventorying of the sites each custodian has access to. This status indicates where in the discovery process the targets are. The statuses are:

- Scheduled To Be Discovered —the preservation targets will be discovered after other targets have completed.

- Discovered —the preservation targets have been discovered. Once complete each custodian assigned to the project, you can view a list of all SharePoint sites each custodian has access to and select the target you want to preserve by using the Project console. For more information, see Selecting SharePoint targets .

- Error —the preservation targets have not been discovered due to an error. For information on fixing preservation target errors, click the Discover Targets button in the Project Console. For information, see Project console .

## Manage preservation targets

Manage SharePoint preservation targets after they've been discovered. The following buttons are available in the Project Console:

- Discover Targets —manually start the Sharepoint preservation target discovery process for the project's custodians. Can use to retry errors.

- Select Targets —select Custodian's SharePoint target sites to be placed on a preservation hold. Access to the button when the custodian discovery status is Discovered . To learn how to select targets, follow the steps in Selecting SharePoint targets .

##### Selecting SharePoint targets

After discovering SharePoint targets, you need to select targets based on SharePoint URLs associated to a custodian.

To select targets, follow the steps below.

-

Click the Select Targets console button.

-

In the Select window, select the check boxes next to the custodian name and target URL you want to put on a preservation hold.

-

Use the arrows to select the custodians.

-

Click Select Targets .

On this page

- Creating a preservation hold case

- Adding a preservation hold to a project

- Adding a preservation case

- Permissions

- Prerequisites

- Considerations

- Adding a preservation hold to a project

- Adding a preservation case

- Preservation hold status

- Preservation target status

- Manage preservation targets

- Preservation hold status

- Preservation target status

- Manage preservation targets


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

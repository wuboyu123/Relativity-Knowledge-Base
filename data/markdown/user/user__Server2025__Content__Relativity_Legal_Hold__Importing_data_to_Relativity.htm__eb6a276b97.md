---
title: "Importing legal hold data to Relativity"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Importing_data_to_Relativity.htm
collection: user
fetched_at: 2026-06-22T06:04:06+00:00
sha256: 06a603edd356a20911ef5a0d261bdbbf0ff8e2372b58b537917748b219fd11fe
---

Importing legal hold data to Relativity

# Importing hold data to Relativity Legal Hold

After installing Legal Hold, you can use the Relativity Desktop Client (RDC) to migrate hold information from a legacy system into Legal Hold. See Relativity Desktop Client .

## Prerequisites

Before migration, you must convert existing hold information into separate load files with specific formats, as detailed below.

Not all of the following information may exist in the legacy system, so you don’t need to populate non-applicable fields, with the exception of required values, such as Name .

### Load file types

- Entity information. For example: email, department, manager.

- Project/communication information. For example, description, email content, Portal content, BCC.

- Custodian reminder and escalation dates

- Custodian association to projects/communications

- Communication acknowledgment dates per custodian

- Questions into the Question Library

- Questionnaire completion dates per custodian

- Message information

This migration does not cover:

- Migrating custodian responses to questions on questionnaires

- Migrating email history

The following items must all be unique:

- Project names

- Communication names

- Custodian full names

## Importing the legacy data

Importing legacy data into Relativity Legal Hold requires separate imports through the RDC for each object type. For example, import the custodians load file into the Entity object.

Entity Field must have email field populated for the Legal Hold system to work correctly. If the data is not imported correctly, you will need to restart the process.

- Import the Entity load file. View Import Custodians values

- (Required) Full Name - this unique value appears on all Legal Hold grids and pickers when selecting a custodian. This value must be unique. We recommend generating a unique value using the fill feature in Excel when preparing the load file.

Each row of a CSV must have a unique pairing of Custodian Name and Communication Name. If any row contains a duplicate custodian name and communication name pair, you will receive an error upon trying to import this file into Relativity via the RDC. Resolve this issue by either consolidating those two entries down to one row (ideally the one with the more recent date/accurate acknowledgement info) or change the communication name or names so each pairing is unique (like adding a "2" after the communication name).

- (Required) First Name - the custodian's first name.

- Middle Name - the custodian's middle name.

- (Required) Last Name - the custodian's last name.

- (Required) Email - the custodian's email address.

- Secondary Email - the custodian's secondary email.

- Phone Number - the custodian's phone number.

- Company - the custodian's company.

- Job Title - the custodian's job title.

- Department - the custodian's department within the organization. This value is available for filtering and searching when selecting custodians.

- Manager - the custodian's manager. This value should also exist as a separate custodian in the load file.

The manager field must be in last name, first name. Last name, comma, space, then first name. For example, Discovery, Edward. It must match the Full Name of that manager exactly.

- Employee Number - the custodian's employee number.

- Employment Status - the custodian's current employment status.

- Start Date - the date the custodian's position started.

- Leave Date - the date the custodian's position ended.

- Username - the custodian's employee username at the company.

- Address 1 - the custodian's home address.

- Address 2 - the second line of the custodian's home address.

- City - the custodian's home address city.

- State/Province - the custodian's home address state/province.

- Zip/Postal Code - the custodian's home address zip/postal code.

- Country - the custodian's home address country.

- Location - An optional field used to denote a specific building/office or to provide a friendly name for different business unites.

- Notes - use this field to add any applicable notes regarding the custodian.

- Unique ID - use this field when, for example, performing Active Directory data imports using Integration Points . Because you must reference a unique field when setting up the import, you can specify the UniqueID field as unique and map it to an Active Directory field such as ObjectGuid.

- Import the Projects load file. View Import Projects values

- (Required) Name - the unique name of the project, which can contain several communications. This value often reflects the matter name and must be unique.

- Project Description - a description to help you classify and organize projects.

- (Required) Project Status - this value is either Active or Closed . Setting a project as Closed prevents any further actions from being taken in the project. You can re-open a project at any time.

- Project Start Date - the date that the project was created.

- Project Close Date - the date that the project was closed, corresponding to the Project Status value mentioned above.

- Project Owner - the first and last name of the project owner. If the setting is enabled, all custodian replies to communications are forwarded to this user.

- (Required) Owner Email - the email address of the project owner. If the setting is enabled, all custodian replies to communications are forwarded to this user.

- (Required) Type - you can create custom project types to classify projects according to custom workflows. The default value is Legal Hold .

- (Required) Use as Template - this value is either True or False to distinguish this project as being a template. You can change the value as necessary.

- Subject Matter Start Date - the date that the project’s subject matter actually began. This value is useful for referencing a time period from which documents are preserved.

- Subject Matter End Date - this is the date the project’s subject matter concluded, and is useful for referencing a time period for which documents should are preserved.

- Import the Communications load file. View Import Communications values

- (Required) Name - the unique name of the communication, which Legal Hold sends to custodians. This value must be unique. We recommend generating a unique value using the fill feature in Excel when preparing the load file.

Each row of a CSV must have a unique pairing of Custodian Name and Communication Name. If any row contains a duplicate custodian name and communication name pair, you will receive an error upon trying to import this file into Relativity via the RDC. Resolve this issue by either consolidating those two entries down to one row (ideally the one with the more recent date/accurate acknowledgement info) or change the communication name or names so each pairing is unique (like adding a "2" after the communication name).

- (Required) Communication Type - there are three main communication types listed below. Creating a communication type other than these types will contain the properties of the General Hold Notice communication type.

- General Hold Notice - the standard communication sent to custodians who must review or accept specific language and/or complete a questionnaire.

- Release Notice - Legal Hold only sends this communication type to custodians that are released from a project.

- Alert Group - Legal Hold only sends this communication type to users who must be alerted to a custodian’s specific answers to questions on questionnaires.

- (Required) Project (Name) - this project name should correspond with the project name from the previous load file.

- Communication Description - the description of the communication. You can add any details regarding the communication’s purpose or content.

- Response Due Date - the date at which all custodians should reply to the communication. If a custodian does not respond by this date, they are flagged as having an overdue communication.

- (Required) Use as Template - this value is either True or False to distinguish this communication as being a template. You can change the value as necessary.

- (Required if Legal Hold is the communication type) Acknowledgement Required - this value is either True or False to indicate if the specific communication requires the custodian to log in to the Custodian Portal and acknowledge the communication.

- (Required) Email Subject - the email subject for the communication.

- (Required) Email Body - this is the email body for the communication. The body should already contain the [PortalLink] merge field if the communication requires acknowledgement.

- (Required if Legal Hold is the communication type) Enable Reminders - this required value is either True or False to indicate if Legal Hold sends automatic reminders to non-responsive custodians. If the value is True, you must also fill out the other reminder fields below. The body should already contain the [PortalLink] merge field if the communication requires acknowledgement.

- (Required if enabling reminders) Reminder Interval - if Enable Reminders is set to True , this value determines how many days apart Legal Hold sends the reminders. For example, a value of “7” means that Legal Hold sends reminders every 7 days until the custodian responds.

- (Required if enabling reminders) Allotted Reminders - if Enable Reminders is set to True , this value determines how many total reminders are sent.

- (Required if enabling reminders) Reminder Subject - if Enable Reminders is set to True , this contains the subject of the reminder email.

- (Required if enabling reminders) Reminder Body - if Enable Reminders is set to True , this contains the email body of the reminder email. The body should contain the [PortalLink] merge field if the communication requires acknowledgement.

- (Required if Legal Hold is the communication type) Enable Automatic Escalation - this value is either True or False to configure if Legal Hold sends an escalation to the custodian’s manager after all automatic reminders are sent.

- (Required if enabling reminders) Escalation Detail - if Enable Automatic Escalation is set to True, this contains the email body that will get sent to the custodian’s manager.

- (Required if Legal Hold is the communication type) Portal Detail - this is what custodians see and requires their acknowledgement in the Custodian Portal.

- Send As - this value populates an email alias as the sender for all holds going forward.

- BCC People - this requires the custodian’s full name value from above and will then send these custodian's notices when other custodians receive the hold going forward.

- BCC Subject - this is the subject of the BCC email that Legal Hold sends to the BCC People above.

- BCC Body - this is the body of the BCC email that Legal Hold sends to the BCC People above.

- Import the Attachments load file. This a list of all the attachments that custodians view on the Portal and the Projects that those attachments are associated with. View Attachment values

- (Required) Name - the name of the attachment file (you can use the file name).

- (Required) File Link - this should contain a link to the native file attachment you want to import. Under the “Native File Behavior” section in the Desktop Client, click “Load Native Files.” From the drop-down, select the field from your load file that contains the link.

- (Required if you are linking attachments) Communication Name - this links the attachment with an existing communication. You must specify the exact communication name to correctly associate the attachment to the communication.

- Import the Custodian Role load file. These values link a custodian to a specific project and, if they are a custodian, specifies if they have been released. A custodian requires one Custodian Role value for each project. View Custodian Role values

- (Required) Name - this value must be unique. We recommend generating a unique value using the fill feature in Excel when preparing the load file. The end user never sees this value.

- (Required) Project - this is the specific project name that the communication belongs to. In the RDC, select this as the Parent Info RDO.

- (Required) Communications - this is the specific communication name from above that was sent to the custodian. Separate multiple communications by entering each communication on separate lines.

Use the field settings when merging data.

- (Required) Custodian - this is the custodian (full name) who received the communication.

- (Required) Role - you can generate any number of custom roles, but we recommend importing with the default: Custodian .

- (Required if the custodian is released) Release Date - populate this with the release date if the custodian was released from the Project.

- Access to Sensitive Material - This value is either True or False to indicate if the custodian on this project has access to sensitive material.

- Notes - An optional area to store specific notes about this custodian’s involvement on this specific project. For example, ESI Tier .

- Import the Custodian Status load file. These values link specifics regarding when custodians receive and respond to notices. View Custodian Status values

- (Required) Name - the end users never sees this value but it must be unique. We recommend generating a unique value using the fill feature in Excel when preparing the load file.

- (Required) Communication - this is the specific communication name from above that Legal Hold sent to the custodian.

- Communication View Date - if known, this is the date that the custodian actually viewed the communication.

- Acknowledgement Date - this is the date that the custodian acknowledged the communication. Leave this value blank if the custodian did not acknowledge the communication.

- (Required) Custodian - this is the custodian (full name) who received the communication.

- Escalation Date - if Legal Hold sent an escalation for this custodian and communication, this is the date it was sent.

- Notice Last Sent Date - this is the last date that Legal Hold sent a communication to the custodian.

- (Required) Project - this is the specific project name that the communication belongs to. In the RDC, select this as the Parent Info RDO.

- Reminders Last Sent Date - this is the last time that Legal Hold sent a reminder to the custodian.

- Reminders Sent - this is the total number of reminders that Legal Hold has sent to the custodian for the communication.

- Resolved By - (Custodian Full Name) - this is the Relativity User artifact ID who acknowledged a communication on behalf of this communication.

- Resolved By Reason - for auditing purposes, this is the reason why someone else acknowledged the communication on behalf of this custodian.

- Import the Message load file. These values link specifics regarding messages sent or received in specific holds. View Message values

- (Required) Name - Unique identifier for the row of data.

- (Required) Custodian - Custodian name.

- (Required) Communication - Name of the communication.

- (Required) Project - Name of the project to which the custodian is being added. In the RDC, select this as the Parent Info RDO.

- (Required) Message Type - Enter "General" (without quotes) into this field.

- (Required) Message Status - Enter "Sent" (without quotes) into this field.

- (Required) Last Sent Date - The data that the last communication was sent.

- Re-save communications.

- For any communications that have scheduled reminders, go into those communications from the front end and resave them so that Legal Hold schedules the automatic reminder/escalation job. For communications with scheduled reminders, resave the communication from Legal Hold so that Legal Hold schedules the automatic reminder/escalation job.

- If custodians need to see any portal attachments, you must go into each communication on the front end and add them.

## Migrating with ARM

Use the ARM application in conjunction with Legal Hold to archive, restore, and move a Relativity Legal Hold workspace between Relativity installations or SQL Servers. For more information on ARM, its job types, security permissions, and considerations, see the ARM documentation .

To run ARM with Legal Hold, you will need to select the Legal Hold check box in ARM. For more information, see Creating a running a Restore job .

When restoring Legal Hold data, the Portal URL field in Legal Hold should be re-entered immediately after performing a restore. When restoring a Legal Hold workspace, the link to the Portal URL is automatically removed. The removal of the Portal URL prevents any further communication from being sent. Communications will not work until the Portal URL field is repopulated.

To update the Portal URL after the restore, follow the steps below:

-

Navigate to the restored workspace.

-

Navigate to the Hold Admin tab.

-

Click Edit .

-

Re-enter the Portal URL into the field.

-

Click Save .

After updating the Portal URL, it may be useful to notify users of the new URL with a Global Reminder. You can easily include the new URL in the reminder by using the Portal Link merge field. For more information, see Enabling Global Reminder .

## Importing custodian data using Microsoft Azure AD

Use Integration Points in conjunction with Legal Hold to import entity data, employee or custodian, from Microsoft Azure Active Directory. For example, the workstations, employee names, data shares, etc. To do this, install Integration Points application into your workspace from the Relativity Application Library. Once installed, add the Azure AD Provider source.

Add the Azure AD Provider source by creating an Azure AD application and credentials in your Azure Portal. During this you'll create the app, select the Graph API, grant permissions, and find Azure credentials. For more information, see Microsoft Azure AD provider and Microsoft’s documentation .

The Integration Points Azure AD Provider is a separate application that isn't in the Relativity Application Library. Contact Customer Support to add Azure AD provider as a source to Integration Points. Completing this adds Azure AD as a source within Integration Points.

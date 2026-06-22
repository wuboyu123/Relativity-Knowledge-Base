---
title: "Adding general settings"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Adding_general_settings.htm
collection: user
fetched_at: 2026-06-22T06:12:44+00:00
sha256: f9f59b22039ed83683bac60a62122c7b3d1ae76ce0cd7e467f3a301457a82ab8
---

Adding general settings Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Adding general settings

Update the fields in the General section. The General section covers settings that affect the high-level overview items of a legal hold project such as forwarding reply emails to the project owner, setting hold notice approval requirements.

To update the General settings on the Legal Hold Settings page, follow the steps below:

-

Click Edit .

-

Locate the General section.

-

Enter information in the fields. See General settings fields for more information.

-

Update another section or click Save .

## General settings fields

The general settings must be entered on the Legal Hold Settings page prior to starting a legal hold project.

- Forward Reply Emails to Project Owner

Emails, that are not acknowledgements, get forwarded to the project owner. Acknowledgement emails are sent to the email address entered in the Reply to Email Address. For more information, see Adding Outgoing Email settings .

- Select Yes to have Legal Hold automatically forward all custodian replies to the project owner, as specified in the project details. See Project Details layout fields . Legal Hold sends custodian replies first to the primary Legal Hold inbox for import into the system, while still giving visibility to the project owner of the custodian’s reply.

- Select No to prevent Legal Hold from forwarding custodian replies to the project owner.

- Send Confirmation Email

- Select Yes to have Legal Hold send a confirmation email to the custodian once they acknowledge a communication or complete a questionnaire.

- Select No to prevent Legal Hold from sending a confirmation email to the custodian upon their acknowledgement.

- Automated Send Time - the time at which Legal Hold sends automated reminders and automated escalations. Use the HH:MM format (24-hour format). The time is local to the server, not your local PC.

- Hold Notices Require Approval - the workspace setting that sets whether Relativity Legal Hold users need to send all communications to an admin for approval before sending to custodians.

- Enable Project Wizard

- Select Yes to use the Project Wizard when creating a new legal hold project. For more information, see Creating a project .

- Select No to use the alternative steps to create a new legal hold project. For more information, see Alternate project creation method .

- PRL High Threshold (%) - the percentage of acknowledged communications, out of all sent communications in a project, to be considered at a successful level and turn the PRL icon in the project list green. Default is set at 100%. See Project response level .

- PRL Medium Threshold (%) - the percentage of acknowledged communications, out of all sent communications in a project, to be considered at a standard level and turn the PRL icon in the project list yellow. Default is set at 50%. See Project response level .

- Entity OneDrive URL Field - the OneDrive URL field is used to put a custodian's OneDrive content on hold when a client isn't able to use an account with SharePoint Admin privileges. When editing the Entity OneDrive URL field, you select a field on the Entity object that Legal Hold expects to contain the user’s OneDrive URL. See Entity OneDrive URL field .

## Entity OneDrive URL field

SharePoint Admin privileges are required for automated look up of a custodian's OneDrive Site URL. If the preservation account can't be granted SharePoint Admin privileges, then enter the Entity OneDrive URL field for each custodian so that automated look up isn't required.

When the preservation account used for Microsoft 365 preservations doesn't have SharePoint Admin privileges the Entity OneDrive URL field is the alternative way to put a custodian's OneDrive source on a preservation hold. When the Entity SharePoint URL is provided, Relativity Legal Hold uses it to put a custodian's OneDrive content on a hold. For more information, see Creating a Microsoft 365 admin account .

If the User Principal Name in your Azure AD account doesn't match the email address, you can use the Entity OneDrive URL field to put a custodian's OneDrive account on hold. Sharepoint Sites cannot be placed on Hold if the User Principal Name is different from Email in your Azure AD account.

If the Entity OneDrive URL field setting is empty, Legal Hold reverts to the original logic and queries SharePoint directly for this information.

### Setting up OneDrive

A Legal Hold administrator needs to perform additional setup for this functionality to work. Use an existing field or create a new field on the entity object to host OneDrive URL information for each custodian. Use Integration Points or the RDC to populate this field with fully qualified OneDrive URL for eachcustodian.

Point Legal Hold to use such field as a reference to OneDrive URL information:

- Navigate to the Legal Hold Settings tab.

- Click Edit .

- Click the Entity OneDrive URL field Select button.

- In the Select Items - Entity OneDrive Url Field modal, select an existing field that can contain OneDrive URL information. For example, select the Note field.

- Click Set .

- Enter each entity's OneDrive URL for their OneDrive site in the selected field. For example, enter https://company-my.sharepoint.com/personal/firstlast01_company_com in the OneDrive URL in the Note field.

- Click Save .

On this page

- Adding general settings

- General settings fields

- Entity OneDrive URL field

- Setting up OneDrive


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

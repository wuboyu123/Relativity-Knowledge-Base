---
title: "Creating legal hold entities"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Creating_entities.htm
collection: user
fetched_at: 2026-06-22T06:12:49+00:00
sha256: 2470de935380c84d1188a60ccab5bc5b3b38a41d5cd5582376af471939acf0ab
---

Creating legal hold entities

# Creating legal hold entities

The Entity object functions as the central location for people, companies, organizational groups, and their metadata. Relativity Legal Hold, Processing, and Analytics all leverage the Entity object.

## Creating and editing an entity

To create an entity, complete the following:

- From the Entities tab, click New Entity .

- Select a layout from the drop-down list. For more information, see Legal Hold layout

- Complete the fields in the layout.

- Click Save .

The following section contains entities information specific to Legal Hold.

Legal Hold entities

## Legal Hold layout

The Legal Hold Custodian detail layout contains the following fields:

Basic Contact

- First Name - the entity's first name.

- Last Name - the entity's last name.

- Email - (Optional) the entity's email address.

Legal Hold entities can share the same email address.

- Middle Name - (Optional) the entity's middle name.

Company

- Company - (Optional) the entity's company.

- Current Title - (Optional) the entity's job title.

- Department - (Optional) the entity's department.

- Manager - (Optional) the entity's manager. Select a person from the available entities to designate as the new entity's manager. The designated manager will receive any Escalation communication for this entity.

- Employee Number - (Optional) the entity's employee number.

- Employment Status - (Optional) the entity's current employment status.

- Employment Start Date - (Optional) the date the entity's position started.

- Employment End Date - (Optional) the date the entity's position ended.

- Username - (Optional) the entity's employee username at the company.

- Domain - (Optional) the company's network name. For example, " Relativity .corp".

- Phone Number - (Optional) the entity's phone number.

Location

- Address 1 - (Optional) the entity's home address.

- Address 2 - (Optional) the second line of the entity's home address.

- City - (Optional) the entity's home address city.

- State/Province - (Optional) the entity's home address state/province.

- Zip/Postal Code - (Optional) the entity's home address zip/postal code.

- Country - (Optional) the entity's home address country.

- Location - (Optional) An optional field used to denote a specific building/office or to provide a friendly name for different business unites.

Other

- Secondary Email - (Optional) the entity's secondary email address.

- Notes - (Optional) use this field to add any applicable notes regarding the entity.

- Unique ID - (Optional) use this field when, for example, performing Active Directory data imports using Integration Points. Because you must reference a unique field when setting up the import, you can specify the UniqueID field as unique and map it to an Active Directory field such as ObjectGuid.

- Entity Interaction - (Optional) determines the level of interaction the Legal Hold application has with the entity. You can select None, Full, Limited, Redirected.

- Full - the entity receives standard communication functionality. This is the default behavior.

- None - the entity no longer receives communications. Entities set to None do not appear in the Communication Summary report or the Open Tasks report and have N/A in the responded field on Entity reports. If an entity sends a message to an admin, the admin can respond to the entity.

- Redirect - the entity communications are redirected to a Redirect Recipient, another entity, to act on behalf of the original entity. If a redirect recipient is acting on behalf of another entity, the information can be found in the database.

If an entity is selected to receive redirected communications, they then cannot be removed from Legal Hold nor set to None. For more information, see Custodian Interaction level .

### Custodian Interaction level

When creating or editing an entity, there is a Custodian Interaction level that can be set. You can find this setting within the Other tab. Custodians have three different interaction levels: Full, None, Redirect.

Full is the default and the entities with this setting get all communications as normal. None is a setting for entities who should not receive any communications. The Redirect setting is used for entities that need communications and questionnaires sent to another entity, or redirect recipient, that is able to acknowledge on behalf. When acting as a Redirect Recipient, the entity cannot be deleted, as they are acting on behalf of other entities within the project.

When a custodian's Interaction level is set to None or Redirect, the entity does not appear in the Redirect Recipients dialog. Custodians that have their Custodian Interaction level set to None, will not appear on the Communication Summary report and the Open Tasks report.

Different communication actions and different interaction level settings combined with the Silent Custodian setting can get complicated. In order to make sure the correct entity, if any, gets the correct communication, see the chart below.

Entity Interaction Level Action Do Not Notify (Is set) Target Entity Receives Email

Full Send General Notice Communication False Yes

Full Send BCC True Yes

Full Send BCC False Yes

Full Send BCC Not on project Yes

Full Send Escalation/Automatic Escalation (Manager) True Yes

Full Send Escalation/Automatic Escalation (Manager) False Yes

Full Send Escalation/Automatic Escalation (Manager) Not on project Yes

Full Send Reminder/Automatic Reminder False Yes

Full Global Reminder False (for at least one project they are active on) Yes

Full Release Entity False Yes

Full Send Alert Notice True/False/Not on project Yes

Full Resend Expired Portal Link False Sends out link

Full Resend Expired Portal Link True Sends out link

Full Responses False Yes (never redirect)

Full Send Portal Link True No (button disabled)

Full Send Portal Link False (for at least one project they are active on) Yes

Full Send Escalation to CC recipients True/False/Not on Project Yes

Redirect Send General Notice Communication False Redirected

Redirect Send BCC True Redirected

Redirect Send BCC False Redirected

Redirect Send BCC Not on Project Redirected

Redirect Send Escalation/Automatic Escalation (Manager) True Redirected

Redirect Send Escalation/Automatic Escalation (Manager) False Redirected

Redirect Send Escalation/Automatic Escalation (Manager) Not on Project Redirected

Redirect Send Reminder/Automatic Reminder False Redirected

Redirect Global Reminder False (for at least one project they are active on) Redirected

Redirect Release Entity False Redirected

Redirect Send Alert Notices True Redirected

Redirect Send Alert Notices False Redirected

Redirect Send Alert Notices Not on Project Redirected

Redirect Resend Expired Portal Link False Sends out link to original entity

Redirect Resend Expired Portal Link True Sends out link to original entity

Redirect Responses False Yes (never redirect)

Redirect Send Portal Link True No (button disabled)

Redirect Send Portal Link False (for at least one project they are active on) Redirected

Redirect Send Escalation to CC recipients True/False/Not on Project

No

None Send Escalation/Automatic Escalation (Manager) True Yes

None Send Escalation/Automatic Escalation (Manager) False Yes

None Send Escalation/Automatic Escalation (Manager) Not on project Yes

None Send Portal Link True No (button disabled)

None Send Portal Link False (for at least one project they are active on) No (button disabled)

None Send Escalation to CC recipients True/False/Not on Project No

## Entity console

Use the Entity console to take an action related to that entity and run reports specific to that entity across multiple projects. Buttons are shaded gray when the action is unavailable or may not appear if you don't have the correct permissions. See Securing a project .

Custodian

-

Use Portal As - view the Legal Hold portal as a specified entity in a separate tab. Use this feature to acknowledge participation in a project or answer a questionnaire on someone else's behalf. For example, use this feature during a guided entity interview.

-

Send Portal Link - send a communication to the entity that contains the link to their Entity portal home page. Entities can enter their email address to access the portal.

Custodians can only receive communications if they have their email address on their entity record.

-

Reports - run a project-specific report from this section. The report appears inline. See Report types for more information about each report. Note that you may not be able to view all reports depending on your permissions.

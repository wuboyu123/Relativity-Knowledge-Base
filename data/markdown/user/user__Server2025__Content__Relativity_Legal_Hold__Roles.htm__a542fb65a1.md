---
title: "Roles"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Roles.htm
collection: user
fetched_at: 2026-06-22T06:12:56+00:00
sha256: 873f96f7993e642721d6a7e3c63ef115fa6d765eeb238d6b9ff86f072206d4e5
---

Roles

# Assigning roles to custodians

In Relativity Legal Hold, roles provide a way to distinguish between people on a legal hold and those assisting with the legal hold compliance. A project can have multiple people assigned to it in different roles.

Use roles when sending communications to specific groups. For example, you may need to send a specific communication to only the Human Resources group at your company. Use roles to filter your custodian list when you use the Select option to send a communication from the Project console. See Project console .

Roles appear on the Entities tab in the Entity Details section.

## Creating a role

To manage the roles:

- Navigate to Roles tab. Legal Hold ships with the following roles by default:

These default roles cannot be deleted.

- Alert Group —indicates that the person is a member of the Alert Group. These groups may include HR, legal, and IT or any group of individuals impacted by a custodian’s response to a question. They will be notified if a custodian answers a question in a certain manner.

- Custodian —indicates that the person or company is a custodian on the project.

- Human Resources —indicates that the person is a member of the Human Resources group.

- Information Technology —indicates that the person is a member of the Information Technology group.

- Project Member —indicates that a non-custodian can be assigned a task. Hold notices cannot be sent to entities assigned with the Project Member role on a legal hold project. A custodian with assigned with the Project Member role will not impact the PRL.

- Silent Custodian —indicates that the custodian is a member of the Silent Custodian group. Use this role to place a custodian on a silent hold. By default, the Silent Custodian role has the Do Not Notify tag applied. Silent Custodians:

- Won't receive communications from Legal Hold.

- Still appear in the Custodians and Custodian Active Projects reports.

- Are people that you do not want to:

- Make aware that they're on a legal hold.

- Disturb with excess hold communications, such as the company CEO.

- Preservation Hold —indicates that the custodian has a preservation hold on their Microsoft Exchange and One Drive accounts in place. This tag triggers preservation in place for custodians. For more information, see Adding preservation hold settings using Modern Authentication .

- To add a new role, click New Roles .

- Enter a new role in the Name field.

- (Optional) Select one or more Tags.

- Do Not Notify —prevents custodians from receiving any communications.. For example, you might want to create a role of Executive or Parental Leave and apply that role to employees that are still part of a project or hold, but shouldn't receive communications for a determined period of time. Select the Place On Preservation Hold tag check box to prevent any removal or deletion of data in the custodian's Office 365 account. Click Manage to add a new Tag type.

- Place On Preservation Hold —triggers preservation in place for custodians. For more information, see Creating a preservation hold case .

- Project Member —used to indicate non-custodians that can be assigned tasks.

- Click Save .

Click Edit to edit a role name. You can delete a role by clicking Delete from the role object.

## Assigning a role

You can apply a role and a tag to a person when you assign a custodian to a project. See Assigning custodians to a project .You can also change a role using the Project console button Change Role. See Project console .

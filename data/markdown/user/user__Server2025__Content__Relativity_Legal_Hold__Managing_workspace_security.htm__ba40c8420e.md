---
title: "Securing a workspace"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Managing_workspace_security.htm
collection: user
fetched_at: 2026-06-22T06:12:31+00:00
sha256: dad7373297228ec57256344d2e3497a63e871cd7dc618cb9e13f12ee236a3646
---

Securing a workspace

# Managing Legal Hold workspace security

To use Relativity Legal Hold, you need to configure the workspace security.

## Accessing and configuring Legal Hold

Once you've installed Legal Hold and the Portal, you should see the following Legal Hold application tabs in your workspace:

Legal Hold includes all pages available with a base Relativity install.

- Entities

- Legal Hold

- Projects

- Communications

- Reports

- Question Responses

- Mailbox

- Project Reminder

- Custodian Status Dashboard

- Tasks

- Libraries

- Questionnaires

- Questions

- Attachments

- Scheduled Reports

- Legal Hold Admin (Relativity tab)

- Legal Hold Settings

- Global Reminder

- Roles

- Custodian Portal Authentication Provider

- Item Selectors

### Legal Hold template

Legal Hold ships with a default template entitled, Legal Hold Template in the Projects tab. You can create a new project from scratch or use this template to customize your new project.

To create a project from a template you must have edit rights on the project object.

When creating a project from a template, the following items carry over:

- Project details - this includes all of the Project response level fields.

- Associated communications with details - the template includes the following communications:

- Acknowledge Email Template - an example communication that includes an acknowledge email merge field inside the body of the text for a custodian to acknowledge the legal hold without further navigation.

- Alert Notice Template - an example communication that notifies anyone in the Alert Group that a custodian might have potential involvement in a legal hold or matter.

- Legal Hold Notice Template - an example communication that notifies custodians of an anticipated (or actual) legal hold and contains a link to the custodian portal where the custodian can acknowledge their participation in the hold or that they've received the notice.

- Legal Hold Release Notice - an example communication that notifies on-hold custodians that they have been released from the hold or project.

- Associated questionnaires - the Legal Hold Notice Template communication contains the Legal Hold Questionnaire Template questionnaire that ships with the template. This questionnaire contains typical questions that a company might want to collect information from a custodian, such as whether they had prior knowledge of the hold, or if they have access to electronic documents that may pertain to the hold.

Legal Hold preserves item-level security on the above items for the new project, including communications and questionnaires. See Managing workspace security .

## Managing workspace security

The Legal Hold custom permissions are independent from the System Admin group and aren't automatically assigned to the group. For Relativity System Administrators or Workspace Admin Group members to have access to the functions controlled by the Legal Hold Application, you must add these users to another security group or add a new group with access to the Legal Hold Application. When Legal Hold is installed to a workspace Relativity creates a Legal Hold Security Admins group where you can add users.

The Legal Hold application security is set at the workspace and item level. For more information, see Security and permissions.

We recommend configuring the security permissions on your Legal Hold workspace as soon as you install Relativity Legal Hold. See Securing a project for more information.

For a Relativity Legal Hold user to run and complete a project, certain permissions need to be set. See the table below for the security permissions to run a Legal Hold project.

Object Security Tab Visibility Other Settings

- Attachments – View, Edit, Add

- Communication – View, Edit, Delete, Add

- Custodian Portal Authentication Provider -

- Custodian Role – View, Edit, Delete, Add

- Custodian Status – View, Edit, Delete, Add

- Entity – View, Add

- Field – View, Add

- Add Field Choice By Link

- Global Reminder – View, Add

- Job Schedule - View, Edit, Delete, Add

- Legal Hold Application Permissions – View

- Select all check boxes

- Legal Hold Selector Configurations - View, Edit, Delete, Add

- Legal Hold Selectors - View

- Select all check boxes

- Legal Hold Task - View, Edit, Delete, Add

- Preservation Case – View, Edit, Add

- Preservation Case Source – View, Edit, Delete, Add

- Preservation Custodian Hold – View, Edit, Delete, Add

- Preservation Custodian Status – View, Edit, Delete, Add

- Preservation Custodian Target - View, Edit, Delete, Add

- Preservation Hold Settings – View, Edit, Delete, Add

- Preservation Source – View, Edit, Delete, Add

- Preservation Target Discovery Status - View, Edit, Delete, Add

- Preservation Target Filter - View, Edit, Delete, Add

- Preserve Product – View, Edit, Delete, Add

- Preserve Product Source – View, Edit, Delete, Add

- Project – View, Edit, Delete, Add

- Project Health - View, Edit, Delete, Add

- Project Questionnaires - View, Edit, Delete, Add

- Project Questionnaires Report Sub View - View

- Project Reminder - View, Edit, Delete, Edit

- Question – View, Edit, Delete, Add

- Questionnaire – View, Edit, Delete, Add

- Questionnaire Question – View, Edit, Delete, Add

- Questionnaire Response – View, Edit, Delete, Add

- Questionnaire Response Answer – View

- Report – View, Edit, Delete, Add

- Roles - View, Edit, Delete, Add

- Scheduled Communication - View, Edit, Delete, Add

- Schedule Report – View, Add

- Entities

- Legal Hold

- Projects

- Communications

- Reports

- Question Responses

- Mailbox

- Project Reminder

- Custodian Status Dashboard

- Tasks

- Legal Hold Libraries

- Questionnaires

- Questions

- Attachments

- Scheduled Reports

- Legal Hold Admin

- Legal Hold Settings

- Global Reminder

- Preservation Hold Settings

- Roles

- Custodian Portal Authentication Provider

- Item Selectors

- Admin Operations

- View All Audits

- Manage Object Types*

When you install Legal Hold into a workspace, Relativity creates a Legal Hold Security Admins group. This group will have all Legal Hold permissions enabled by default. You can add users into this group. You will also be able to create new groups, or give existing groups, Legal Hold permissions by selecting the custom Legal Hold permissions. For more information on the Legal Hold permissions, see Securing a project .

*If you are installing the Legal Hold application without Processing and Analytics, you will also need the Admin Operations - Manage Object Types permission enabled to use the project wizard.

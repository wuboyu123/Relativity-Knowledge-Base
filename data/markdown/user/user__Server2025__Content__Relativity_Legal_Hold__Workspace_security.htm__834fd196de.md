---
title: "Workspace security"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Workspace_security.htm
collection: user
fetched_at: 2026-06-22T06:12:33+00:00
sha256: 14d3bc39c4daadb2e4e887fe0078325141c931a6a1b6ed891064ef4a8f44e0a8
---

Workspace security

# Securing a legal hold project

To use Relativity Legal Hold, you need to configure the workspace security and secure a legal hold project for each user group.

## Securing a project

The Legal Hold custom permissions are independent from the System Admin group and aren't automatically assigned to the group. For Relativity System Administrators or Workspace Admin Group members to have access to the functions controlled by the Legal Hold Application, you must add these users to another security group or add a new group with access to the Legal Hold Application. When Legal Hold is installed to a workspace Relativity creates a Legal Hold Security Admins group where you can add users.

To secure these custom permissions:

- Navigate to the Workspace Details tab.

- From the Relativity Utilities console, click Manage Workspace Permissions .

- Determine the group you want to apply these custom permissions to, then click Edit Permissions on that group.

- Scroll down to the Legal Hold Application Permissions .

- From here, select the checkbox next to the permissions that you want to grant the users in the specified workspace group. You also need to ensure that a corresponding object level permission is also set to Add or Edit.

If you leave a checkbox cleared, the users in that group won't be able to perform the permission, which corresponds to a button or link in Legal Hold or the Custodian portal.

Legal Hold Application Permissions

- Approve Communications - Approve button on Project console appears when:

- Approve Communication - select this checkbox

- Assign Custodian - Assign button on the Project console appears when:

- Assign Custodian(s) - select this checkbox.

- Object level permission: Custodian Role - Add

- Release Custodian(s) - Release button on the Project console appears when:

- Release Custodian(s) - select this checkbox.

- Object level permission: Custodian Role - Edit

- Remove Custodian(s) - Remove button on the Project console appears when:

- Remove Custodian(s) - select this checkbox.

- Open Project/Close Project - Open/Close button on the Project console appears when:

- Open Project/Close Project - select this checkbox.

- Object level permissions

- Project - Edit

- Preservation Custodian Status - Read

- Message - Create

- Custodian Role - Edit

- Send Communication(s) - Send Communication button on the Communication console appears when:

- Send Communication(s) - select this checkbox.

- Send Communication Preview - Send Preview button on the Communication console appears when:

- Send Communication Preview - select this checkbox.

- Send Communication Reminder - Remind button on the Communication console appears when:

- Send Communication Reminder - select this checkbox.

- Send Escalation - Escalate button on the Communication console appears when:

- Send Escalation - select this checkbox.

- View Portal As Custodian - Controls the ability to access the Custodian portal and view active holds, tasks requiring attention, and completed tasks.

- View Portal As Custodian - select this checkbox.

- Act on Behalf Of Custodian - Acknowledge on Behalf button on the Communication console. Controls the ability to acknowledge or respond on behalf of another custodian.

- Act on Behalf Of Custodian - select this checkbox.

- Respond to Message - Reply to Message button on the Reply console appears when:

- Respond to Message - select this checkbox.

- Object level permission: Message - Add and Edit

- Send Global Reminder Now - Send Global Reminder Now button on the Global Reminder console appears when:

- Send Global Reminder Now - select this checkbox.

- Send Test Global Reminder - Send Test Email button on the Global Reminder console appears when:

- Send Test Global Reminder - select this checkbox.

- Test Outgoing Email Settings - Test Outgoing Email Settings button on the Settings console appears when:

- Test Outgoing Email Settings - select this checkbox.

- Send Project Reminder Now - Send Project Reminder button on the Project Reminder Notify console appears when:

- Send Project Reminder Now - select this checkbox.

- Send Test Project Reminder - Send Test Email button on the Project Reminder Notify console appears when:

- Send Test Project Reminder - select this checkbox.

- Preservation Hold - Controls the ability to add, edit, or remove Preservation Holds within projects.

- Preservation Hold - select this checkbox.

System admins must ensure that the following object level permissions are enabled in order for specific buttons or links appear in the Legal Hold UI.

These object level permissions aren't contained in the Legal Hold Application Permissions.

- New Project button - the user can create a project from a template when the following permissions are enabled:

- Project - Add, Edit

- Communication - Add, Edit

- Questionnaire - Add, Edit

- Create Communication button - this button appears when:

- Communication - Add, Edit

- Questionnaire - Add

- QuestionnaireQuestion - Add, Edit

- Schedule Report button - this button appears when:

- Scheduled Report - Add, Edit

- Job Schedule - Add

- Add link - this link appears on the Communication layout Portal Content tab when:

- Object level permission: Field - Add, Edit

- Add Field Choice By Link - select this checkbox.

System admins must ensure that the following permissions are enabled in order for specified users to run reports from the Project and Communication consoles.

- Tab Visibility - Legal Hold::Reports - select this row.

We recommend not overwriting inherited security on the Reports tab. This may cause unexpected Report permissions issues.

To ensure that the Question Response report link appears on the Communication console, the following must be in place:

- The communication contains a questionnaire

- The user has permission to view the Question Responses tab both under the workspace tabs and under the Tab Visibility.

- Object Security - Question Responses and Questionnaire Response Answer - View

To ensure that the Question Response report link appears on the Custodian and Project Details, the following must be in place:

- The user has permission to view the Question Responses tab both under workspace tabs and under the Tab Visibility.

- Object Security - Question Responses and Questionnaire Response Answer - View

- Click Save .

The Legal Hold Application Permissions are only available when the Legal Hold application is installed.

. For more information, see Security and permissions.

### Configuring Legal Hold

To configure Legal Hold, access the Settings tab. See Adding legal hold settings for more information.

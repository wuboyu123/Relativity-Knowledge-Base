---
title: "Preview security"
url: https://help.relativity.com/Server2025/Content/Relativity/Security_permissions/Preview_security.htm
collection: user
fetched_at: 2026-06-22T06:08:30+00:00
sha256: ef7a08791b394b151115db0f2666d1dbb620ebdad703f47013b1d92acbd3b3ef
---

Preview security

# Preview security

The preview security feature lets system admins interact with Relativity as if they are logged in as a specific user or a member of a specific group. A system admin can then easily verify that the correct permissions are applied without logging in to Relativity under a different account.

For example, say you secured a layout from a user and you want to verify that person no longer has access to the layout. With the preview security feature, you can select the user and view Relativity as that person right from your system admin account.

If you perform a job while previewing a user's security settings, the audited action is credited to your username and not to the user whose security you were previewing when you started the job.

The preview security feature does NOT allow the system admin to monitor the actions of a user in real time; it only simulates what the user would see.

## Previewing security from the Workspace Details tab

To preview the security of a user at the workspace-level only from the workspace details page, follow these steps as a system admin:

- Click the Administration tab, and then click Workspace Details .

- Click Manage Workspace Permissions .

- Click Preview for a group on the Group Management tab.

A preview window opens and shows the workspace as it looks for any user in the group. A bar labeled You are previewing as a member of the <group name> group. appears at the top of the window indicating that this instance of the workspace is not the system admin's view, but rather a preview of the group's view according to the assigned permissions.

- Click Exit Preview in the preview bar to close the preview security session and return to workspace details.

## Previewing security from the Groups tab

To preview security from the Groups tab, follow these steps as a system admin:

- Navigate to the Groups tab.

- Click the group name of the group whose permissions you want to preview.

- Click Preview Security.

A preview window opens and shows what members of the group see upon logging in to Relativity. A bar labeled You are previewing as a member of the <group name> group. appears at the top of the window indicating that this instance of the workspace is not the system admin's view, but rather a preview of the group's view according to the assigned permissions.

- Click the Exit Preview on the preview bar to close the preview security session and return to the group details.

## Previewing security from the Users tab

To preview security from the Users tab, follow these steps as a system admin:

- Navigate to the Users tab.

- Click the full name of the user whose permissions you want to preview.

- Click Preview Security .

A preview window opens and shows what the user sees upon logging in to Relativity. A bar labeled You are previewing as <username>. appears at the top of the window indicating that this instance of the workspace is not the system admin's view, but rather a preview of the user's view according to the assigned permissions.

If the user is a member of the System Administrators group, the preview security button is unavailable. The favorites menu and some options in the user menu are disabled during preview security sessions.

- Click the Exit Preview on the preview bar to close the preview security session and return to the user details.

## Preview security audit

Actions made during preview security sessions are audited as actions of the system admin performing the preview session, not the user being impersonated. Any action performed by a system admin are audited. Additionally, the start and end of a security preview session are audited:

- View Audit from User Details: The audit lists the User Name , Action , and Timestamp of any preview security session. The audit reports the username of the system admin performing the preview security session and Timestamps for Security Preview Started and Security Preview Ended .

- View Audit from Group Details: The audit lists the User Name , Action , and Timestamp of any preview security session. The audit reports the username of the system admin performing the preview security session and Timestamps for Security Preview Started and Security Preview Ended .

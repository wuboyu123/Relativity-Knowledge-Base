---
title: "Setting workspace permissions"
url: https://help.relativity.com/Server2025/Content/Relativity/Security_permissions/Setting_workspace_permissions.htm
collection: user
fetched_at: 2026-06-22T06:07:53+00:00
sha256: 33ce07079eab64ec822adcc3bb3592bcecb538529f0deb457ababfa5f9ea3615
---

Setting workspace permissions

# Setting workspace permissions

Edit workspace permissions using the Workspace Security dialog accessible from the Workspace Details tab. Access the dialog using the following steps in a workspace:

- Click the Administration tab followed by Workspace Details .

- Click Manage Workspace Permissions to open the Workspace Security dialog.

To add and remove groups, you must have the Edit Security permission set for the Workspace object and the Add and Delete permissions set for the Groups object (instance level security).

## Group Management

The Group Management tab displays all groups added to a workspace. The following actions are available for groups added to a workspace other than system admins:

- View Users - displays a list of users in a group.

- Edit Permissions - opens the Object Security tab for you to begin editing the workspace permissions for a group.

- Copy - opens a list of groups whose permission settings you can transfer to the group.

Select a group and click Copy Permissions at the bottom of the list to complete the transfer.

- Preview - preview currently applied security settings for a group. See Preview Security for more information.

- Add/Remove Groups - opens the Add/Remove Groups dialog on which you can search for and add or remove groups.

Relativity displays a warning message when a sys admin attempts to edit or copy permissions for any group in a client domain. This warning makes the sys admin aware that modifying permissions may have significant consequences. For example, changing permissions may allow client domain users to modify items outside their tenancy. The sys admin can click Manage Permissions to proceed with the update or Cancel to exit the pop-up window.

### Add/Remove Groups

The Add/Remove Groups window displays the following lists:

- Available Groups - lists available groups in your Relativity environment not yet granted access to the workspace.

- Groups in Workspace - lists groups granted access to the workspace.

#### Adding groups to a workspace

To add one or more groups to a workspace, follow these steps:

If you are in a Workspace admin group, you must have the instance-level Edit permission to the Group object to add a group to a workspace.

- Click the Administration tab followed by Workspace Details .

- Click Manage Workspace Permissions .

- Click Add/Remove Groups on the Group Management tab.

- Select one or more groups from the Available Groups list in any order. Scroll the list or search for a specific group using the search bar.

- Click Add .

- Click Save .

#### Removing groups from a workspace

To remove one or more groups from a workspace, follow these steps:

- Click the Administration tab followed by Workspace Details .

- Click Manage Workspace Permissions .

- Click Add/Remove Groups on the Group Management tab.

- Select one or more groups from the Groups in Workspace list in any order.Scroll the list or search for a specific group using the search bar.

- Click Remove .

- Click Save .

## Saving permissions for a group

In the Workspace Security dialog you can switch between the Object Security, Tab Visibility, and Other Settings tabs before saving modified security permissions for a selected group. If you modify security settings on any of these three tabs, and try to close the dialog or click the Group Management tab, Relativity prompts you with the following options:

- Save - saves all permissions changes and applies them to the selected group.

- Revert - discards all unsaved permissions changes and reverts to the group's last saved permissions.

- Cancel - cancels the attempted dialog close or tab change action.

After making security changes on the Object Security, Tab Visibility, and Other Settings tabs, click Save at any time to apply the selected permissions settings.

## Object Security

Use the Object Security tab to manage the following object-level permissions for a selected group:

- None —denies users access to the object.

- View —view the object. This is the lowest level object permission.

- Edit —edit and view the object.

- Delete —delete, edit, and view the object.

- Add —add new objects. This icon turns blue when the setting is unsaved; once you click Save, the blue icon becomes grey. This icon turns green when you give users this permission both when the setting is unsaved and saved.

- Edit Security —grants users the ability to edit the security of objects. This icon turns blue if you click twice indicating a not applicable status.

See Object list for a list of securable objects.

### Assigning object-level permissions

To assign object-level security permissions to a group:

- Click the Administration tab followed by Workspace Details .

- Click Manage Workspace Permissions .

- Click Edit Permissions for a group on the Group Management tab. Or, click Object Security and select a group from the Current Group drop-down menu.

- Click the applicable object security permission(s) you want to apply to the selected group. Icons for selected security permissions appear in color, and names of objects for which you changed security permissions appear in italic typeface until you save the modified permissions.

- Click Save .

### Denying object access

To deny a group any access to an object, click the icon. After setting a group's permission level to None, the icon appears in color .

## Tab Visibility

The Tab Visibility tab lists all parent and child tabs in a workspace. Combine object-level permissions and tab visibility to give users the tools they need to complete their tasks.

To grant access to workspace tabs, select all tabs you want visible for a selected group and click Save . For a complete list of tabs, see Tab Visibility.

### Selecting parent and child tabs

Indented tab names indicate child tabs of a parent tab. The following example shows Password Bank and Imaging Profiles as child tabs of Job Admin.

To select a parent tab and all its child tabs, mouse over the parent tab and click Select all(#) .

When you select a child tab, the related parent tab is automatically selected. To only select a child tab, click the parent to clear the parent selection.

## Other Settings

With the Other Settings tab you can control browser visibility and accessibility to admin operations and mass operations in a workspace. For a complete list of admin operations, see Workspace security .

To enable one or more browsers, mass operations, and admin operations for a selected group in a workspace, select all settings that apply and click Save .

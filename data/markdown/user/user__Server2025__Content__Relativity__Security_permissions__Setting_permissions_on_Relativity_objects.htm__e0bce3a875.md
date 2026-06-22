---
title: "Relativity object security"
url: https://help.relativity.com/Server2025/Content/Relativity/Security_permissions/Setting_permissions_on_Relativity_objects.htm
collection: user
fetched_at: 2026-06-22T06:07:54+00:00
sha256: 4d484f9c1a234598cacd15c9f4c32b2c98886e0fa4297283192c91047ebe6a2a
---

Relativity object security

# Relativity object security

Individual items inherit their objects' rights. For example, a group's rights to an individual field are determined by the field's rights across the workspace. In some cases, you may want to change the security for certain items.

Say you have a group doing contract review, and you want the group to be able to see the custodian field, but not be able to edit it. You can customize object permissions to ensure users have view rights, and not edit rights to the custodian field object.

To change the security on individual items:

- Navigate to the item’s details page, and then click Edit Permissions . For example, to open the details page for a particular view in a workspace, click the Administration tab followed by the Views tab, and then click the name of a view in the list. Or, click the icon for an object in a item list view with the Security field added.

- Click the Overwrite Inherited Security toggle on the Group Management tab to set one of the following options:

- OFF - object inherits security settings from its parent object (i.e., case workspace).

- ON - modifies group access and object security overrides the workspace level security settings.

Altering security permissions from overwrite inherited security to inherit security and vice versa may involve a wait time for 50,000 records or more. If this occurs, a notification appears to inform you of the impact of the change.

- If you set Overwrite Inherited Security to ON to modify an object's security, click Add/Remove Groups to add or remove groups for which you want to set explicit object permissions.

- Click Edit Permissions for a group to modify the group's object security rights.

- Select any of the following object permissions to assign to the group:

- None —denies users access to the object.

- View —view the object. This is the lowest level object permission.

- Edit —edit and view the object.

- Delete —delete, edit, and view the object.

- Add —add new objects. This icon turns blue when the setting is unsaved; once you click Save, the blue icon becomes grey. This icon turns green when you give users this permission both when the setting is unsaved and saved.

- Edit Security —grants users the ability to edit the security of objects. This icon turns blue if you click twice indicating a not applicable status.

Not all permissions listed above apply to all objects. The Object Security tab doesn't display the icon for a permission that doesn't apply.

- Click Save .

## Securing a folder for selected groups

Folders can also be managed so that only selected groups can access a folder's contents.

To change which groups can access a folder:

- Navigate to the Documents tab.

- Right-click on the folder you wish to control a group's access to, and then select Secure .

Parent-level folders cannot be secured.

- Click Overwrite Inherited Security to toggle it ON .

- Click Add/Remove Groups .

- Select the group or groups that you wish to add or remove, and then click the Add or Remove button.

- Once you've added or removed all of the desired groups, click Save .

- Optionally, click Edit Permissions next the desired group to modify that group's folder security rights.

- Select any of the following folder permissions to assign to the group:

- View - view the folders. This is the lowest level folder permission.

- Edit - edit and view the folders.

- Delete - delete, edit, and view the folders.

- Add - add new folders. This icon turns blue when the setting is unsaved; once you click Save, the blue icon becomes grey. This icon turns green when you give users this permission both when the setting is unsaved and saved.

- Edit Security - grants users the ability to edit the security of folders. This icon turns blue if you click twice indicating a not applicable status.

- Click Save .

The folder will display a padlock icon to show that Overwrite Inherited Security has been toggled On for that folder.

### Folder security inheritance

If a user drags a folder with item-level security into another folder, the new child folder inherits the parent folder's security.

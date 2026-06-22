---
title: "Instance security"
url: https://help.relativity.com/Server2025/Content/Relativity/Security_permissions/Instance_security.htm
collection: user
fetched_at: 2026-06-22T06:03:47+00:00
sha256: a61d3e789095bc23cde282a0957ee1df8fd365fd0e1b758a8f6fb3dd86705dbc
---

Instance security

# Instance security

With instance security you can apply permissions to system admin groups to limit or grant access to particular system admin objects. You can access the Admin Security dialog from the Instance Details tab .

Users must be assigned to the following two groups in order to have full system administration access:

1. System Administrators - This grants access to all admin-level permissions, such as ARM, queue management, users, and groups tabs.

2. <Customer Name> Admin Group - This gives the user permissions to access all workspaces in the instance, unless the workspace was migrated through ARM or Migrate without the group being properly mapped first.

See the following related pages:

- Setting instance permissions

- Setting permissions on objects

- Preview security

## Object Security tab

The Object Security tab lists all system admin objects with their related item-level permissions. Item-level rights include:

- None —denies users access to the object.

- View —view the object. This is the lowest level object permission.

- Edit —edit and view the object.

- Delete —delete, edit, and view the object.

- Add —add new objects. This icon turns blue when the setting is unsaved; once you click Save, the blue icon becomes grey. This icon turns green when you give users this permission both when the setting is unsaved and saved.

- Edit Security —grants users the ability to edit the security of objects. This icon turns blue if you click twice indicating a not applicable status.

You can apply system admin permission settings to any of the following objects in the Object Security tab:

Only system administrators can edit the Client and Matter for a workspace. In addition, the Errors tab is only available to system administrators.

- Agent - access to the Agents tab .

- Agent Type - access to the Agent Types page when creating a new agent.

- Choice - access to the Choice tab .

- Client - access to the Clients tab .

- Error - access to the Errors tab .

- Group - access to the Groups tab .

- License - access to the License tab . Only full system admins can edit license information.

- Matter - access to the Matters tab .

- Relativity Script - access to the Relativity Script Library tab .

- Resource File - access to the Resource files tab .

- Resource Pool - access to the Resource pools tab .

- Servers - access to the Servers tab .

- Tab Type - access to the Tabs tab .

- User - access to the Users tab .

- View - access to the Views tab .

- Workspaces - access to the Workspaces tab .

- Workspace Application - access to Workspace Applications .

- Workspace Portal Services

- Workspace Portal Services Permission - allows you to view the workspace names from other instances in Workspace Portal.

If you see the Workspace Processing Settings item listed in the object security section of your console, note that this represents an RDO for which there is no front-end implementation. It stores the Invariant StoreID and Data Grid settings for the workspace, but it provides no functionality, and it controls nothing.

## Tab Visibility tab

In Relativity, the Tab Visibility setting allows you to control which tabs in the user interface are visible to specific groups. This includes parent and child tabs that can be granted access to groups. To give users the tools they need to complete their tasks, you can combine object security permissions and tab visibility access. However, it's important to note that tab visibility settings do not change the permission rights to the objects displayed on each tab. Rather, they only control whether the user can see the tab in the navigational menu.

It's possible to display a tab to the user, even if the user lacks the necessary permissions to view any of the objects listed on that tab. However, tab visibility cannot be used to restrict access to the objects listed on a particular tab. Users can still access those objects through a direct URL or via the API, even if the tab is not visible to them in the navigational menu.

Granting tab visibility to a group without view permissions for the object allows users to view the tab but prevents them from taking action. Granting object permissions to a group without tab permissions for the object restricts users from completing required tasks.

- Workspaces - visibility of the Workspaces tab .

- Administration - visibility of the Administration tab.

- Clients - visibility of the Clients sub-tab .

- Users - visibility of the Users sub-tab .

- Groups - visibility of the Groups sub-tab .

- User Status - visibility of the User Status sub-tab .

- Matters - visibility of the Matters sub-tab .

- Views - visibility of the Views sub-tab .

- Choices - visibility of the Choices sub-tab .

- Tabs - visibility of the Tabs sub-tab .

- Resource Files - visibility of the Resource Files sub-tab .

- License - visibility of the License sub-tab . Only full system admins can edit license information.

- Application Library - visibility of the Application Library sub-tab .

- Servers - visibility of the Servers tab .

- Agents - visibility of the Agents tab .

- Queue Management - visibility of the Queue Management tab.

- Processing Queue - visibility of the Processing Queue sub-tab .

- Production Queue - visibility of the Production Queue sub-tab .

- OCR Queue - visibility of the OCR Queue sub-tab .

- Branding Queue - visibility of the Branding Queue sub-tab .

- Instance Details - visibility of the Instance Details tab .

- Relativity Script Library - visibility of the Relativity Script Library tab .

- Resource Pools - visibility of the Resource Pools tab .

## Admin Operations tab

You can alter the following permission settings from the Admin Operations tab of the Admin Security page.

- Agent Operations - access to agent operations .

- Change Queue Priority - access to priority of queues.

- Force Logout on User Status - access to the ability to bump users out of Relativity.

- Manage Object Types —permission that grants group members the ability to:

-

Create a new tab for a new object type when adding the new object type.

- Automatically gain view, add, edit, delete, and secure permissions for all newly created object types .

- Automatically gain tab visibility for newly created tabs.

- Send Message - access to send messages to users in Relativity.

- Use Quick Nav - access to the quick nav button.

- View Admin Repository - required in order to access tabs and objects from home.

Users will have access to the Workspaces tab even without the View Admin Repository permission.

- View Audits - access to the ability to view audit records on the View Audits tab .

#### A Note on View Admin Repository

This permission setting is required for some features and supported applications to function properly. Outside of features that specifically require this permission, access can also be granted so that users can run a report and filter against the Workspace/Client/Matter/User/Group objects in report set-up. Please keep in mind that due to this fact, when View Admin Repository is granted to a user for whatever reason, that user is also gaining access to the User and Group objects from the context of the platform. In other words, these users are now capable of retrieving Users and Groups with or without the mobile app.

The following features and/or supported applications require the View Admin Repository permission.

-

Case Metrics

-

Staging Explorer

-

Workspace Portal

-

Processing Administration

-

RelativityOne Activity Dashboard

-

Production/Branding Queue

-

ARM

## Group Permissions report

With the Group Permissions Report you can easily assess all permission settings applied to any group. Navigate to the Instance Details tab and click Group Permissions Report .

You can perform the following actions from this console:

- Horizontal or Vertical - displays the console horizontally or vertically according to you preference.

- Group - select any group in your Relativity environment from the Group drop-down menu. Click Run to see a list of all system admin permission settings for that group.

- Preview - displays the Script Body that defines the selected group's permission settings.

- Run - generates Group Permissions Report on the selected group.

- Export to File - click Go to export a .CSV file of all the selected group's system admin permission settings.

### Reading the Group Permissions Report

- Group - displays the selected group's name.

- Permission - displays the name of the system admin object on which system admin rights are granted for the selected group.

- Type - displays the group's permission level on the object listed in the Permission column.

## Uneditable admin permission settings for the Everyone group

All users in any instance of Relativity are members of the Everyone group. The following admin permissions apply to the Everyone group by default, and this permission setting configuration is necessary for your Relativity environment to function properly. You can't add or revoke any of the following permission settings on the Everyone group:

- View User - visibility of user.

- View View - visibility of views.

- View Code - visibility of code.

- View Group - visibility of groups.

- View , Edit , and Add Error - visibility, edit rights, and add rights to errors.

- View Relativity Script - visibility of Relativity script.

- View Resource Server - visibility of resource servers.

- View Tab Type - visibility of tab types.

## Script and application library permissions

System admins are the only users able to access the following items:

Application Library View :

- Upload Application button - access to the button that uploads applications into workspaces.

Application Library Details :

- Install - access to the Install button on the Application details screen.

- Upgrade - access to the upgrade applications button. This button only appears if an upgrade to the application is available.

- Cancel - access to the Cancel button. This button only displays during installation.

- Push to Library button - access to the Push to library button.

Relativity Script Library view :

- New Script button - access to the New Relativity Script button on the Relativity Script Library tab.

New Script page :

- Edit button - access to the Edit button on scripts.

- Delete button - access to the Delete button on scripts.

- Script Header - access to the Script Header in the XML editor.

- XML Editor - access to the XML editor on the New Script page.

Edit Script page :

- Script Header - access to the Script header on the Edit Script page.

- XML Editor - access to the XML editor on the Edit Script page.

Run Script page :

- Preview button - access to the Preview button on the Run Script page.

## System administrator privileges

The following actions are exclusive to System Administrators and don't require additional permissions:

-

Perform Mass Operations on admin. level objects

-

Permanently delete or recover workspaces from the Recycle Bin

-

Access to the Errors tab on the Admin. level

-

Manage group permissions within Instance details

---
title: "Upgrading applications"
url: https://help.relativity.com/Server2025/Content/Relativity/Applications/Upgrading_applications.htm
collection: user
fetched_at: 2026-06-22T06:17:00+00:00
sha256: 3d01eb856bb392dc27f269048a82b5b7511aefe6604f6a345282cfc51b99bfe4
---

Upgrading applications Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Upgrading applications

You can upgrade an existing application by using the Upgrade Application option available on its detail view.

## Upgrading an application

Before you upgrade an application, review the following information:

- Some Relativity applications are pre-populated with instances of object types used to store settings, which you can modify to control application functionality. Upgrading the application resets these instances, so any modifications made to them are lost. As a best practice, create new instances of these object types in your application instead of modifying the default settings. For example, you might create a new profile with your custom settings in the Imaging application.

You can avoid resetting instances of object types by developing applications that use Post Install event handlers set to run only once. Using these event handlers, you can create instances of objects and set default values on them during the initial application installation, but not on subsequent upgrades. See Post Install event handlers on the Server 2025 Developers site.

- Relativity preserves modifications made to saved searches included in locked applications. For more information, see Customizing locked applications .

- Confirm that any existing application jobs have completed before upgrading out-of-the-box Relativity applications, such as OCR, search terms report, transform set, or imaging. You may interrupt the current job if you upgrade the application while it is running.

### Upgrading an application in a workspace

Use the following procedure to upgrade an application:

- Confirm that you have the appropriate system admin permissions to install an application in Relativity. For more information, see Workspace security .

- Select the Relativity Applications tab in the target workspace.

- Click the name of the application that you want to upgrade.

- Click Upgrade Application in the Relativity Application console. If you don't see this button, then you don't have the appropriate system admin permissions.

- Select Import from file in the Application Type field.

- Click Browse to select a application file.

- Click Open on the browse dialog.

- Click Upload to initiate upgrade script.

### Upgrading an application through the Application Library

- Confirm that you have the appropriate system admin permissions to install an application in Relativity. For more information, see Instance Security .

- Select the Application LIbrary tab.

- Click the name of the application that you want to upgrade.

- In the Workspaces Installed associated object, select the workspaces in which you want to upgrade the application and click Upgrade Installed Workspaces . If you don't see this button, then you don't have the appropriate system admin permissions.

- Click Continue on the confirmation modal to proceed with upgrading the application in all the workspaces it's installed in.

- Select Import from file in the Application Type field.

Relativity will upgrade the selected application, and the new version will be visible in the applications list in the workspaces it's installed in.

### Application resource file purge

The application upgrade process purges assembly resource files (DLLs) no longer associated to the newer application version:

- Physically deletes all DLL resource files that were part of the original application version.

- Removes event handler associations on objects types such as Document or Entities.

- Remaps object references in the workspace database to reference the new DLL.

- Eliminates workspace references to resources that no longer exist.

- If an agent of a removed type is currently running, it will complete its work and then self-destruct.

The following application components are not deleted by the upgrade process:

- Object types (fields, views, layouts, etc.)

- Scripts

- Saved searches

- Dashboards

## Troubleshooting application upgrades

You can use the following information to identify and resolve issues that may occur when upgrading your applications.

### Custom pages not working properly when multiple application versions exist on the same server

If you have an application with custom pages in Workspace A, and import a new version of the same application to Workspace B on the same server, then the custom pages may not function as expected since they are outdated. However, they continue to display as components of the application.

### Applications can't be downgraded

You can't import an application with an earlier version number into the Relativity applications library. However, an application with an earlier version number can exist in a workspace even though the application in the environment's library has a higher version number.

On this page

- Upgrading applications

- Upgrading an application

- Upgrading an application in a workspace

- Upgrading an application through the Application Library

- Application resource file purge

- Troubleshooting application upgrades

- Custom pages not working properly when multiple application versions exist on the same server

- Applications can't be downgraded


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

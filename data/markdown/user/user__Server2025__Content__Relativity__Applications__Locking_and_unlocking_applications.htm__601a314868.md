---
title: "Locking and unlocking applications"
url: https://help.relativity.com/Server2025/Content/Relativity/Applications/Locking_and_unlocking_applications.htm
collection: user
fetched_at: 2026-06-22T06:08:00+00:00
sha256: dc621495eb6f2709b556535b3258f03caf7088da6a0ccf807e4c248c37b619fa
---

Locking and unlocking applications Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Locking and unlocking applications

In Relativity, you can edit applications by unlocking them. You can also lock applications to prevent any modifications to them. On the Relativity Application tab, use the Lock Application and Unlock Application buttons to perform these operations. You need the appropriate system admin permissions to lock or unlock an application. For more information, see Workspace security .

You can't lock or unlock system secured applications that are shipped with Relativity. The Relativity Application tab doesn't display these options for system secured applications. See System secured applications .

This page contains the following information:

- Locking an application

- Modifying saved searches in a locked application

- Unlocking an application

## Locking an application

You can't edit a locked application or any of its components except for saved searches, layout, views and default tab. On the details view of the application, you can't add new components to an application, delete them, or unlink them. On the details view of a specific component, you can't edit any of its fields without receiving an error message.

For example, you attempt to modify a locked application that contains a custom Entities object. Because the application is locked, you can't remove this object from the application through its details view. You also can't add or remove a field from the Entities object through its details view. For information about saved searches, see Customizing locked applications . For information about layouts, views, and default tab, see Customizing locked applications .

If you attempt to edit any of the following components in a locked application, you receive an error message:

- Choice

- Field

- Layout

- Object Type

- Relativity Script

- Tab

- View

- Dashboard

Relativity automatically locks an unlocked application on export. See Exporting applications .

Use the following procedure to lock an application:

- Navigate to the workspace containing the application that you want to lock.

- Click the Relativity Applications tab.

- Click the name of the application that you want to lock.

- Click Lock Application in the Application Console.

## Customizing locked applications

You can make the following customizations to locked applications without unlocking the application:

- You can set a tab in a locked application as the default tab for the workspace.

- You can use the Copy mass operation to copy views and layouts in a locked application.

- The copied views and layout are identical to the original and can be customized.

- When you open views and layouts in a locked application, Relativity displays a user-friendly alert:

If you later upgrade the application, Relativity preserves any changes made to the customized layouts, views, and default tab.

## Modifying saved searches in a locked application

You can perform the following tasks to modify saved searches included in locked applications:

- Move a saved search to a different folder in the saved searches browser. For more information, see Saved search .

- Change the index type for a saved search.

If you later upgrade the application, Relativity preserves any changes made to the saved searches. It also increments the version when you export an application with modified saved searches.

## Unlocking an application

When an application is unlocked, you can add components to it, delete them, or unlink them. You can also edit the fields on any the components in an unlocked application. For example, you want to modify an unlocked application with a custom view. You can add or remove columns from the view when you unlock the application. Consequently, you only want to unlock an application when you purposely want to update it.

The RelativityApplication object has the applicationIsDirty property. This property is set to true when you unlock an application. The current state of an unlocked application is unknown because users may inadvertently modify it. The applicationIsDirty property also determines the type of upgrade installation required for an application in a workspace.

Use the following procedure to unlock an application:

- Navigate to the workspace containing the application that you want to unlock.

- Click the Relativity Applications tab.

- Click the name of the application that you want to unlock.

- Click Unlock Application in the Application Console.

- Click OK on the confirmation message. You can now edit the application by adding or removing components. In addition, you can update individual components by adding, removing, or making other changes to their fields.

On this page

- Locking and unlocking applications

- Locking an application

- Customizing locked applications

- Modifying saved searches in a locked application

- Unlocking an application


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

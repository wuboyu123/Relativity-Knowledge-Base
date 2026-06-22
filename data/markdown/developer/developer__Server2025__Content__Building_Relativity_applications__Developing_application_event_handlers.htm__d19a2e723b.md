---
title: "Develop application event handlers"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Developing_application_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:31:34+00:00
sha256: ba6cf8524e9cf8a9e724fb970c4eb8c655c38d94e9c893c311543ffe0e8ffe65
---

Develop application event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Develop application event handlers

You can develop event handlers that facilitate common tasks performed when installing and uninstalling applications. For example, they can facilitate creating workspaces and database tables, or setting default values on objects. They can also perform cleanup activities when you delete a workspace or uninstall an application. These event handlers execute at the application level rather than on specific object types. For more information, see Develop object type event handlers .

The following table provides a brief description of the application type event handlers available in the Relativity platform.

Application type event handler Brief description

Post Install event handler Executes immediately after the user installs an application. You can use this event handler type to create new instances of Relativity Dynamic Objects (RDOs) or to set default values on fields.

Post Workspace Create event handler Executes as the final task performed during workspace creation. You can use this event handler type to update or perform other operations workspaces or EDDS database tables.

Pre Workspace Delete event handler Executes as the last step in the process used to flag a workspace for deletion. In other words, this event handler executes as the last action that occurs while the progress bar is running in the Relativity UI for a delete operation. It removes unneeded application data from your database when you flag a workspace for deletion.

Pre Uninstall event handler Executes immediately after an agent starts running an uninstall job. This event handler performs cleanup tasks associated with removing an application from workspaces or from your Relativity environment, such as deleting choices, fields, objects, and other items.

Pre Install event handler Executes during the installation of an application. You can use Pre Install event handlers to create database tables or perform other tasks that you must complete before fully deploying an application.

On this page

- Develop application event handlers


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use

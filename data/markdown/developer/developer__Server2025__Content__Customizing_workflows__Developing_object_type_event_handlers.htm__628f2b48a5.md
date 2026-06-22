---
title: "Develop object type event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Developing_object_type_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:31:28+00:00
sha256: f5b71766c513c674edb876f0d9e6d3530b7df093c8d9e33109da0835168662a7
---

Develop object type event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Develop object type event handlers

The Relativity platform supports multiple types of event handlers that you can use for interactions with document objects and Relativity Dynamic Objects (RDOs). You can use these object type event handlers to customize workflows and control user activities in the Relativity UI. You can associate these event handlers with specific object types to write custom code for following tasks:

- Validate data entered in their fields.

- Perform mass operations on several instances of an object simultaneously.

- Trigger specific events on the object when users click console buttons.

For information about other event handler types, see Develop application event handlers .

The following table provides a brief description of the object type event handlers available in the Relativity platform. Some of the following event handlers may be affected setting the Use Relativity Forms field on your object type to Yes . For more information, see the notes below the table, and Relativity Forms API .

Object type event handler Brief description

Console event handler Executes when the user navigates to the view page of an object. You can add a button to a console. Next, use this event handler to define a custom action that occurs when a user clicks the button.*

Page Interaction event handler Injects your JavaScript code or loads Cascading Style Sheets (CSS) file on the layout (view, edit, and new) pages of an object. Use this event handler to add specialized behavior to these pages, and control their look and feel.**

Pre Cascade Delete event handler Executes when a user attempts to delete an object, which has dependent objects. This event handler ensures that Relativity initiates a forced delete operation only when it can successfully remove the specified objects. Use this event handler to verify that no restrictions exist on an object selected for deletion.***

Pre Delete event handler Executes after a user clicks the Delete button or performs a mass delete in the Relativity UI. After Relativity deletes the target object, the event handler commits the delete database transaction.***

Pre Load event handler Executes before Relativity loads a new, edit, or view page layout. Use this event handler to populate fields on RDOs and documents with default values.****

Pre Mass Delete event handler Performs a one-time operation on group of objects before Relativity deletes them. You can use this event handler to perform a one-time operation on child objects before deleting them.***

Pre Save event handler Executes when the user clicks the Save or Save & Next button on a Relativity layout after changing a value for at least one field. These event handlers run before the data on the object is written to the database. They provide you with the ability to manipulate information before storing it.*****

Post Save event handler Executes after a user clicks the Save or Save & Next button on a layout for a document or RDO. This event handler executes after the values entered by the user are written to the database as object properties. Use the Relativity Services API if you later want to modify the object properties, but you can’t update the artifact directly. Use these event handlers to send email notifications, or to instantiate a second object after saving the properties of the original object.*****

The following notes pertain to Relativity Forms' impact on event handlers, for more information on these impacts and for information on Relativity Forms, see Relativity Forms API .

* Console event handlers are ignored when your object type is using Relativity Forms, but the same functionality can achieved within Relativity Forms.

** This type of event handler is treated differently when your object type is using Relativity Forms. The functionality can still be achieved, but script is supplied in a different way.

*** These event handlers are implemented during deletions within Object Manager API, which Relativity Forms uses by default for deletions. If your object is using Relativity Forms, but is not implementing replaceDelete or is using Object Manager API for the deletion, these event handlers will continue to work.

**** Pre Load event handlers are implemented during reads within Object Manager API, which Relativity Forms uses by default for reads. If your object is customized via Relativity Forms, but is not implementing replaceRead or is using Object Manager API for the read, Pre Load event handlers will continue to work for view and edit modes. However, as no read is necessary for creating new objects, Relativity Forms will not fire Pre Load event handlers when rendering a Layout for a new object. Additionally, script contained in Response.Message will not be executed by Relativity Forms, as the only supported mechanism for running script in Relativity Forms is via Page Interaction event handler. To pre-populate values when rendering a form for new objects in Relativity Forms, implement replaceGetNewObjectInstance. Any other script which would normally be executed by displaying the Message property of the Pre Load event handler's response should be moved into a Page Interaction event handler, when using Relativity Forms.

***** These event handlers are implemented during or following saves (creations and updates) within Object Manager API, which Relativity Forms uses by default for saves. If your object is using Relativity Forms, but is not implementing replaceSave or is using Object Manager API for the save, these event handlers will continue to work.

On this page

- Develop object type event handlers


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

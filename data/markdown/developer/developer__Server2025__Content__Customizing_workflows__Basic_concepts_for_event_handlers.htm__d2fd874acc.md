---
title: "Basic concepts for event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Basic_concepts_for_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:31:24+00:00
sha256: fb0fafe5440e628cf0b8cbc5884cb87edf09f12b9e7ede43c11bba39a0cbd50e
---

Basic concepts for event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Basic concepts for event handlers

Review these basic concepts to learn about implementation tasks for event handler development. Additionally, they include information about how to add custom behavior to your applications.

## Common implementation tasks for event handlers

Complete these common implementation tasks when developing custom event handlers:

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages.

- Inherit from the appropriate base class – extend the appropriate base class for the type of event handler that you want to develop. Each event handler type has a unique base class. For more information, see Develop object type event handlers or Develop application event handlers.

- Set the CustomAttribute.Name attribute – provide a description for the event handler that you want to appear in the Relativity UI.

- Add a GUID for the event handler – set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Override the required methods and properties – ensure that you override the appropriate methods or properties for the type of event handler that you are developing. Most event handles require that you override the Execute() method by providing your own business logic. For specific event handler types, see Develop object type event handlers or Develop application event handlers.

## Manipulate or validate data with event handlers

Use event handlers to manipulate or validate data that users see or modify through the Relativity UI. The Relativity platform provides event handlers that support these methods of manipulating data:

- Validate data entered in forms by users before saving it. See Pre Save event handlers .

- Prevent users from deleting protected data. See Pre Cascade Delete event handlers and Pre Delete event handlers .

- Pre-populate field data in layouts before users see them. See Pre Load event handlers .

- Clean up queues or tracking tables when users delete data. See Pre Cascade Delete event handlers and Pre Delete event handlers .

- Control workflows by submitting jobs to a queue table, monitoring their progress, and resolving errors. See Console event handlers .

- Control the look and feel of layouts by loading custom CSS and JavaScript. See Page Interaction event handlers .

On this page

- Basic concepts for event handlers

- Common implementation tasks for event handlers

- Manipulate or validate data with event handlers


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

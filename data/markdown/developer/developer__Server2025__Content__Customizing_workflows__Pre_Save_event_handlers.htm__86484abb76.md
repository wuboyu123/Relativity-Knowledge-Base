---
title: "Pre Save event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Pre_Save_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:29:04+00:00
sha256: 318d3de30becbf0b489ade875ef2108cee59d18fb5fe7cb04a7aa42b206badad
---

Pre Save event handlers

# Pre Save event handlers

Pre Save event handlers execute after a user changes field values and clicks the Save or Save & Next button in Relativity. They run before the data on the object is written to the database, so you can use them to manipulate information before it's stored. These event handlers are supported on document objects and Relativity Dynamic Objects (RDOs). If the criteria for a pre-save process aren't met, you can cancel the operation.

For example, you can use Pre Save event handlers for the following tasks:

- Validating data.

- Auto-updating field values.

- Adding additional data during a save operation for coded information.

See this related page:

- Support for File fields

## Guidelines for Pre Save event handlers

Use these guidelines when developing Pre Save event handlers:

- Create a new class in Visual Studio .

You can also use a template to create this event handler type. For more information, see Visual Studio templates .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages.

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from PreSaveEventHandler – extend the PreSaveEventHandler base class.

- Override the Execute() method – add your business logic for the event handler to this method. This method runs when your event handler is triggered.

- Override the RequiredFields property – represents fields that are required on object creation.

- The ActiveArtifact.Fields collection includes the fields returned by the RequiredFields property, and those on the current layout. It also includes the values of these fields.

- Any Field in ActiveArtifact.Fields that is referenced in this event handler must be placed in the RequiredFields property.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

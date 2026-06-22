---
title: "Relativity Event Handler Express"
url: https://help.relativity.com/Server2025/Content/Relativity/Event_Handler_Express/Relativity_Event_Handler_Express.htm
collection: user
fetched_at: 2026-06-22T06:06:34+00:00
sha256: f515f448f448970136382f3e323601a2fe45239aef6ebb7e2521f2f822dcde5c
---

Relativity Event Handler Express

# Relativity Event Handler Express

Relativity Event Handler Express is specific to Relativity Server applications. In RelativityOne, it has been replaced with Conditional Coding Rules. For details about using Conditional Coding Rules in RelativityOne, refer to Conditional Coding Rules Overview within RelativityOne documentation.

To help drive review workflows, the Event Handler Express app enables you to define validation rules for Relativity layout fields to ensure reviewers enter correct data before saving. The layouts display custom messages to reviewers when they fail to follow the rules specified in the event handler, prompting corrections.

See these related pages:

- Using Event Handler Express

- Building your first event handler

## Basic concepts

Event Handler Express simplifies the development of event handlers so that you don't manually need to write the code for them. When you build event handlers with this tool, you need to define their behavior by creating condition groups and conditions. The following list includes key concepts that you need to understand when building these event handlers:

- Event handler —an assembly (.dll file) that executes when a specific event occurs. You can create Pre Save event handlers that perform validation when the user clicks the Save button on a layout, but before Relativity writes any data to the database. When you deploy the event handler, the application automatically generates an assembly that executes when a user performs a specific task on an object.

Event Handler Express only supports attaching event handlers to document objects and Relativity Dynamic Objects (RDOs). It doesn't support attaching event handlers to any system objects.

- Condition —a validation rule. You build conditions by performing these tasks:

- Identifying a validation type (such as current user, fixed-length text, or others).

- Selecting a field name and an operator for evaluation purposes.

- Choosing a valid choice or value.

For example, you may have a layout that includes fields called Responsive and Issue Designation. You could add a condition that results in an error message when the user selects true for the Responsive field, but doesn't select an option for the Issue Designation field.

Event Handler Expresses supports five field types, including Current User, Fixed-length Text, Single Choice, Multiple Choice, and Yes/No fields. You can use only the supported operators for each field type when building an event handler. If you add multiple conditions, you can choose to evaluate them as a series of expressions connected by the AND or OR operators. See Building your first event handler .

- Condition group —a set of related validation conditions. For example, a condition group might include a series of conditions that test for these items:

- A field containing a certain value.

- A field containing a value that is set.

- A user belonging to a specific group.

You can add an error message that appears when a user makes an inappropriate selection based on the requirements specified in the condition. If you create multiple condition groups, Event Handler Express evaluates them as a series of expressions connected by the AND operator.

- Dynamic link library (DLL) file —a file that Event Handler Express automatically generates when you deploy an event handler to a workspace. During deployment, Event Handler Express validates the logic of the conditions set in the event handler, compiles a .dll file, and pushes it to Relativity as a resource file. The application also attaches the event handler to a specified object, so that it is immediately available on layouts in the workspace. You can download the resource file and then upload it to another Relativity installation. This process makes the event handler functionality available in additional workspaces. For more information, see Using an event handler in another Relativity environment .

In addition to these key concepts, review the following functionality that characterizes the event handlers developed through Event Handler Express:

- Triggered only for updates to a single record —Your event handlers execute when a user clicks Save , Save & Next , and Save and Back . They aren't executed on mass operations.

- Read-only fields and propagation —Propagation doesn't occur when a field populated by an event handler condition is set to Read Only = Yes and propagation is enabled on the field.

- Coding decisions prior to event handler deployment —The conditions that you define in your event handlers only apply to coding decisions made after you deploy the event handler in your environment. You must re-code previously reviewed documents for the event handler conditions to take effect.

## Best practices for building event handlers

Use these guidelines to optimize your event handler development through Event Handler Express.

### Use a test environment

Confirm that your environment handlers are working properly by verifying the expected functionality in a test environment.

An improperly functioning event handler could impede the document review process across your environment. Perform thorough testing of new event handlers before deploying them in a production environment. If your event handler isn't functioning properly, you can update, remove, or detach it from the object type. For more information, see Editing or deleting an event handler , or Editing Relativity Objects .

### Check the logic for your conditions

Ensure that you don't have any conflicting conditions in your event handlers. For example, a conflict occurs if you have one condition that checks if Responsive is true, and a second condition that checks if Responsive is false.

Event Handler Express checks the conditions that you set to ensure that they are logical statements. However, it can't confirm the validity of your business rules. You can avoid interruptions to your review process by validating the business logic used in your event handlers before you deploy them in a workspace. The event handlers are immediately available in layouts, and execute during the review process. For more information, contact Customer Support

### Use unique names for choices

Ensure that the choices and the sub-choices associated with each choice that are added to your workspace all have unique names. If your workspace contains choices or sub-choices associated with each choice with identical names, errors occur when you attempt to build an event handler referencing these choices.

For example, creating a single choice field that has two "Yes" sub-choices can cause errors to occur in Event Handler Express.

### Avoid changing field names

Don't change the names of fields referenced by an event handler. Event Handler Express doesn't update any changes to the field names referenced by an event handler already added to a workspace. If you modify the field name, the event handler that referenced the field no longer exists in the workspace.

Event Handler Express references the Artifact Name for a layout, field, choice, or group. It doesn't use custom labels assigned to fields or groups.

### Keep event handlers in their original workspace

The Artifact Names and IDs that event handlers rely on are specific to an individual workspace. We do not support exporting and importing event handlers from one workspace to another. Doing this may cause performance issues.

Instead of moving event handlers, install Event Handler Express in the new workspace and re-create them there.

### Avoid using unicode characters

Event Handler Express doesn't support the use of unicode characters for event handler names.

### Attach event handlers to documents or RDOs

Event Handler Express supports attaching event handlers to document objects and RDOs. For an object with multiple event handlers, the event handlers execute in the order that you added them to the object. We don't support attaching event handlers to system objects.

The Pre Save event handler doesn't execute when you create a new instance of an RDO. It only executes when you edit an RDO instance.

### Deploy event handlers during off hours

Deploy your event handlers during off hours to minimize disruptions to your production environment.

### Improve performance

To improve performance, create multiple rules within one event handler rather than creating multiple event handlers.

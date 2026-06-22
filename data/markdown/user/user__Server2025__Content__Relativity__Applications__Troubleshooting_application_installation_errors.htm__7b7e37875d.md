---
title: "Troubleshooting application installation errors"
url: https://help.relativity.com/Server2025/Content/Relativity/Applications/Troubleshooting_application_installation_errors.htm
collection: user
fetched_at: 2026-06-22T06:16:56+00:00
sha256: fa950abdaa3a9a5716a09d320d0599268444cc60bb4367c6f0163568a1f2a8a9
---

Troubleshooting application installation errors

# Troubleshooting application installation errors

You can use this page to identify the causes of common application installation errors.

This page contains the following information:

- Installation error list

- Resolving installation errors

- Pre and Post Install event handler errors

## Installation error list

Use the following table to identify common causes of errors that may occur when you attempt to install an application. You can resolve some of these errors manually through the target workspace or you may be able to resolve them as you install the application.

Error sources Possible resolutions

Application contains duplicate Object Type or field names

- Rename the item in the target workspace

- Rename the item in the application

- Remove the item from the application

- Remove the item from the target workspace

- Map fields before installing

Application file contains a relational field that uses a friendly name that a relational field in the target workspace already uses

- Change the friendly name of the relational field in the target workspace

- Change the friendly name of the relational field in the application

- Map fields before installing

Application contains an Object Type that already exists in the target workspace inside a locked application

- Unlock the application in the target workspace

- Remove the object type from the application

Application has a malformed file

- Re-export the application and try again

Application contains an external resource of a restricted file type

- Remove the external resource from the application and re-install

## Resolving installation errors

You can resolve conflicts through the Import Status page without having to modify the application or its artifacts in the current workspace. This page displays errors by type, such as locking errors, name conflicts, or other errors.

You can view the Artifact Name, Artifact Type, and Artifact ID of the component associated with an error, as well as the error status. In the artifact status section, you may have the option to resolve an error before retrying the installation. Error resolution options vary according to error type.

After you finish resolving errors, click Retry Import . Relativity disables this button until you resolve all the errors.

### Locking conflicts

To resolve a locking conflict, select the Unlock checkbox, and then click Retry Import .

You can use this operation to temporarily unlock the application while you resolve a locking conflict during installation. After you successfully import the application, Relativity locks the application again so that you can't inadvertently modify it. See Locking and unlocking applications .

### Name conflicts

You can rename the conflicting artifact so that you can import the components of your application.

Use the following procedure to resolve these errors:

- Select an option in the Resolve Errors drop-down menu. Available options include Rename and Map Field.

- Perform one of the following tasks:

- Rename - Enter a new name in this field to resolve the Name Conflict error. When you've entered a valid name, a green check mark appears next to the new name field.

- Map Field - When you select this option, Relativity automatically maps the field that you're importing to the conflicting field in the target workspace.

### Other errors

For other errors, the Resolve Errors column may display a message that you can only resolve the error manually in the workspace. You must resolve the issue in the target workspace before proceeding with the application import.

## Pre and Post Install event handler errors

Your applications may contain custom code for Pre and Post Install event handlers, which run when you install them. These event handlers configure your Relativity environment so that it can support your applications. If an error occurs while the event handlers are running, your application fails to install. The third-party developer who created your application may provide custom error messages to help you resolve these types of installation failures.

### Failure of Pre Install event handler

When a Pre Install event handler fails, you may receive an error message that indicates the status of the event handler.

In this case, follow the instructions provided in the message. After you resolve the error, reimport the application.

### Failure of Post Install event handler

Post Install event handlers execute after the Application Deployment System (ADS) has updated all of the components in the application. When a Post Install event handler fails, an error message appears on the details view of the application.

## Checking the error statuses

When a Pre or Post Install event handler fails from the Application Library, you can check the status of that error.

Use this procedure to check the error statuses:

- From Home , click the Application Library tab .

- Click on the name of your application.

- In the Workspaces Installed section, locate the workspace containing the application with errors, and then click the Errors link to display a pop-up containing an import status message.

You can review the error message returned by the failed event handler during the last installation attempt.

---
title: "Exporting applications"
url: https://help.relativity.com/Server2025/Content/Relativity/Applications/Exporting_applications.htm
collection: user
fetched_at: 2026-06-22T06:16:55+00:00
sha256: eb7e3fcc738b7d10a4c7265600a506affe4ed1f45041917d2343f7d902b96c13
---

Exporting applications Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Exporting applications

You can export applications that you want to install in other workspaces or instances of Relativity. Additionally, you may want to export an application for upgrading in your development environment. You can export applications as RAP files.

## Avoiding errors during application export

You're unable to export an application until you've manually resolved all errors listed via the Show Errors link on the application console.

Because of this, it's helpful to note the ways by which you can reduce those errors or avoid them completely before you're ready to export the application.

The following table provides the actions you can take to avoid errors.

Object you're adding Notes for preparing the application for export Error you'll avoid

Object type Make sure the Dynamic field on all object types you add to the application is set to Yes. Object Type <Name of Object Type> is not exportable because it is not dynamic.

Add all object types to the application before adding event handlers. The <Name of Object Type> object type is associated with the <Name of Event Handler> event handler. Please add the object type to your application in order to proceed.

Add the objects to the application before adding the fields. The <Name of Object> object associated with Document field <Name of Field> is required in order to proceed. Please add this object to your application.

Add all layouts to the application before adding the object types. The <Name of Object> object that owns the <Name of Layout> layout must be added to your application in order to proceed.

Tab

Make sure none of the tabs you link to from your application are parent tabs.

The <Name of Tab> tab is a parent tab. Parent tabs cannot be included in an application. If your application contains any non-parent tabs they will be placed under an auto-generated tab named after the application on install. Please remove this tab from your application to proceed.

Add all object types to your application before adding tabs separately. The <Name of Tab> tab is associated with the <Name of Object Type> object type. Please add this object type to your application in order to proceed.

View Add the views to the application before adding the layouts and fields. The <Name of View> view includes the following field(s): Field X, Field Y, etc. Please add the field(s) to your application in order to proceed.

Add the views to the application before adding the layouts and fields. The <Name of View> view is referenced in the <Name of Layout> layout. Please add this view to your application in order to proceed.

Add all views to the application before adding the object types, with the exception of any non-dynamic object types. The <object type> associated with the <view name> is required in order to proceed. Please add this object to your application.

Layout Add the layouts to the application before adding the fields. The <Name of Layout> layout includes the following field(s): Field X, Field Y, etc. Please add the field(s) to your application in order to proceed.

Add the views to the application before adding the layouts and fields. The <Name of Layout> layout includes popup pickers using the following view(s): View X, View Y, etc. Please add the view(s) to your application in order to proceed.

Field Make sure all views, including relational views, are added to the application before you add the fields. The field <Name of Field> is a relational field. The view, Family Documents, associated with this relational field must be added to your application in order to proceed.

Make sure all unsupported fields are removed from the application. Relativity applications don't support the Batch::Assigned To field. Remove Batch::Assigned To field from your application to proceed.

Add all fields to your application before adding the choices with which they are associated. The Handler associated with the choice <Name of Choice> is required in order to proceed. Please add this field to your application.

Remove all system fields from the application.

The Document field <Name of Field> is a System field. You must remove this field from the application in order to proceed.

Add all fields to the application before adding object types, with the exception of any non-dynamic object types. The <object type> associated with the <field name> is required in order to proceed. Please add this object to your application.

Dashboard Make sure all the fields found in the dashboards you include in the application are added to the application. The <Name of Dashboard> dashboard associated with the <Name of Object Type> object type includes the following field(s): Field X, Field Y, etc. Please add the field(s) to your application in order to proceed.

Agent Make sure the correct agents are attached with the application. <Name of Agent> agent is not assigned to the correct application domain.

Rule Add all object types to your application before adding object rules separately. The <Name of Rule> Object Rule is associated with the <Name of Object Type > Object Type. Please add the Object Type to your application in order to proceed.

Saved Search Add all choices to the application before adding the saved searches. The <Name of Saved Search> saved search is associated with the <Name of Choice> choice. Please add this choice to your application in order to proceed.

Add all fields to the application before adding the saved searches that contain them. The <Name of Saved Search> saved search includes the following field(s) in its conditions: Field X, Field Y, etc. Please add these field(s) to your application in order to proceed.

Event Handler Make sure all event handlers that you intend to add to the application are correctly configured. Event Handler <Name of Event Handler> is not assigned to the correct application domain.

Mass Operation Add all object types to the application before adding the mass operations with which they are associated. The <Name of Mass Operation> mass operation is associated with the <Name of Object Type> object type. Please add the Object Type to your application in order to proceed.

System Artifact Remove all system artifacts from the application. You have included one or more System Artifacts in the application. You must remove these artifacts to proceed: Artifact X, Artifact Y, etc.

## Application state settings on export

When you export an application, Relativity automatically updates the following state settings on the application:

- Locking - Relativity automatically locks any unlocked applications on export. See Locking and unlocking applications .

- applicationIsDirty flag - Relativity automatically resets the applicationIsDirty to false on any unlocked applications with the applicationIsDirty flag set to true. The value of false indicates that application is in a clean, unedited state. This flag determined the type of upgrade required for an application installed in a workspace.

- Application version - Relativity increments the revision number of the application version with each export if the application is unlocked, the application schema has been modified, or if Developer Mode is enabled.

- Schema version - Relativity increments the schema version according to the rules described in Application schema versions .

Additionally, Relativity automatically increments the version of any application that contains saved searches, which have been modified. For more information, see Customizing locked applications .

## Exporting an application

During export, Relativity automatically assigns a version number to any application that doesn't already have a version.

Use the following procedure to export an application:

- In the target workspace, select the Relativity Applications tab.

- Click the name of the application that you want to export.

- Click Export Application in the Application Console .

- If your application contains external resources, click Export on the Confirm Application Export dialog. Relativity only displays this dialog for applications with external resources, such as custom pages. It exports those applications as a RAP files.

If you export an application with a Single or Multiple Choice field without choices, you receive a message asking if you want to continue with the export. Click OK on this message dialog.

- Click Save or Save As to download the file to your selected location.

- Click Refresh Page in the Application Console . You can find the RAP file for your application in the folder that you selected. Upload this file to the workspace or Relativity instance where you want to deploy the application.

On this page

- Exporting applications

- Avoiding errors during application export

- Application state settings on export

- Exporting an application


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

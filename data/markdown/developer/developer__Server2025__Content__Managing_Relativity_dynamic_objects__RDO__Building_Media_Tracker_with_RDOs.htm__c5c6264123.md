---
title: "Building Media Tracker with Relativity Dynamic Objects"
url: https://platform.relativity.com/Server2025/Content/Managing_Relativity_dynamic_objects/RDO/Building_Media_Tracker_with_RDOs.htm
collection: developer
fetched_at: 2026-06-22T06:29:29+00:00
sha256: 2a3307eff311d30579f4cad99d49ff1036c2a17b0b0f6f6c748ad9b5702a28cf
---

Building Media Tracker with Relativity Dynamic Objects

# Building Media Tracker with Relativity Dynamic Objects

Media Tracker is an application you can build using Relativity Dynamic Objects (RDOs). With Media Tracker, you can track media received from vendors, clients, and opposing counsel. After you build and deploy the application in a workspace, you can manually input the media and related metadata.

Complete the following steps to create a Media Tracker application and then import it into Relativity workspaces.

To build Media Tracker with Relativity Dynamic Objects:

- Create a new application .

- Link and create object types .

- Update and create fields .

- Update views .

- Build layouts .

- Export the Media Tracker application .

## Create a new application

Create a new application in the target workspace. To create a new application:

- Navigate to the Relativity Applications tab.

- Click New Relativity Application .

- Enter Media Tracker as the new application name.

- Click Save .

The Media Tracker application information page displays.

## Link and create object types

Next, add object types to the application from the Media Tracker application information page. For more information, see Editing Relativity Objects .

- Click Link , and then select Document under the Object Type section.

- Click Add , and then click Set .

- Click New under Object Type, to create the following new object types:

- Media Received - stores information about each delivery including a scanned PDF copy of the letter received.

- Source Media - serves as a record of each disk or hard drive received.

- Processed Media - records the volume of data on the disks or the hard drive and relates back to the documents in the database.

For each new object type, set Parent Object Type to Workspace and Relativity Applications to Media Tracker .

The four object types appear on the Media Tracker application information page.

## Update and create fields

Create and edit fields for the Media Tracker application. See Fields . See Fields .

- Navigate to the Fields tab in the target workspace.

- Select All Fields from the View drop-down menu.

- Click Show Filters .

- Type Name in the Name column filter.

- Press Enter .

- Click Edit to rename the Name fields for the following object types:

- Source Media - change name to Media ID .

- Media Received - change name to Media Received ID .

- Processed Media - change name to Processed Volume .

- Click Save to apply each name change.

- Click New Field to create the following fields. The options in the Field Information section must be completed first before the remaining options are displayed. For each field, set the object type, name, and field type as specified in the table below. Set Relativity Applications to Media Tracker , and leave the rest of the options as the default values.

Object Type Name Field Type

Media Received Letter Date Date

Media Received Letter From Fixed-Length Text : 255

Media Received Letter Scan File

Media Received Letter Title Fixed-Length Text : 255

Media Received Letter To Fixed-Length Text : 255

Media Received Received From Single Choice

Media Received Received On Date

Media Received Type Single Choice

Source Media Custodians Multiple Choice; Set Open to Associations to Yes .

Source Media Media Scan File

Source Media Media Type Single Choice

Source Media Media Received Single Object with Associative Object Type: Media Received

Source Media Source Media Storage Location Fixed-Length Text : 255

Processed Media Processed By Single Choice

Processed Media Processed Media Storage Location Fixed-Length Text : 255

Processed Media Source Single Object with Associative Object Type: Source Media

Document Processed Volume Single Object with Associative Object Type: Processed Media

## Update views

In the Relativity Applications tab, go to the Media Tracker application information page. Using the new fields, you can now update the application's views. See Views Views .

- Click Link , and then select the Document view under View.

- Click Add , and then click Set . Adding the Document view requires adding all fields referenced by the Document view to the application.

- Click Edit to update the following views under the View section. For each view, set the fields as listed below. Click Save to apply the view settings.

- Name -All Media Received

- Object Type - Media Received

- Fields

- Edit

- Security

- Media Received ID

- Type

- Received From

- Received On

- Name - All Source Media

- Object Type - Source Media

- Fields

- Edit

- Security

- Media ID

- Media Type

- Media Received

- Source Media Storage Location

- Custodians

- Name - All Processed Media

- Object Type - Processed Media

- Fields

- Edit

- Security

- Processed Volume

- Processed Media Storage Location

- Processed By

- Source::Custodians

## Build layouts

Finally, you can build the layouts that drive the Media Tracker workflow. See Layouts Layouts .

To build a layout for Media Tracker:

- Click Edit Layout Information: Media Tracker to add order in drop-down values (using increments of 10) to each of the following layouts.

- Media Received Layout (Object Type of Media Received)

- Source Media Layout (Object Type of Source Media)

- Processed Media Layout (Object Type of Processed Media)

- Click Save .

- Build the Media Received Layout using the following steps:

- Click Build Layout in the Layout console.

- Click Add Category and enter Media Received. Click Save .

- Drag and drop the following fields into the Media Received category:

- Received From

- Received On

- Type

- Click Add Category and name the new category Letter Information .

- Drag and drop the following fields into the Letter Information category:

- Letter From

- Letter To

- Letter Date

- Letter Title

- Letter Scan

- Click the Add Category drop down > Add Object List . Enter the following:

- Object - Source Media - Media Received

- View - All Source Media

- Link View - All Source Media

- Links Point to Popup - No

- Friendly Name - Source Media - Media Received

- Click Save .

- Build the Source Media Layout using the following steps:

- Click Build Layout in the Layout console.

- Click Add Category and enter Media for the name.

- Drag and drop the following fields into the Media category:

- Media ID

- Media Received

- Media Type

- Click Add Category and name it Custodians .

- Drag and drop the following fields in the Custodians category:

- Source Media Storage Location

- Media Scan

- Click the Add Category drop down > Add Object List . Enter the following:

- Object - Processed Media - Source

- View - All Processed Media

- Link View - All Processed Media

- Links Point to Popup - No

- Friendly Name - Processed Media - Source

- Click Save .

- Build the Processed Media Layout through the following steps:

- Click Build Layout in the Layout console.

- Click Add Category and enter Processed Media for the name. Click Save .

- Drag and drop the following fields into the Processed Media category:

- Processed Volume

- Processed By

- Click Add Category and name it Source Media .

- Drag and drop the Source field into the Source Media category.

- Click Add Category and name it Storage Location .

- Drag and drop the Processed Media Storage Location field into the Storage Location category.

- Click the Add Category drop down > Add Object List .Enter the following:

- Object - Document - Processed Volume

- View - Processed Documents (You may have to create this view. See Views Views . Set the Processed Volume field you created as the field for this view.)

- Link View - Processed Documents

- Links Point to Popup - No

- Friendly Name - Document - Processed Volume

- Click Save .

## Export Media Tracker application

You can now export the Media Tracker application. When you export the application you can also import the application into other workspaces.

- Click Export Application on the Application Console.

- Save the application as an XML file or a RAP file to a folder on your machine.

- Install the application to a workspace or to the Application Library from Home.

Media Tracker is only one way that Relativity applications can support your workflow and data management needs. After you create this sample application and become familiar with its functionality, try modifying its views, field names, and/or layouts to best fit your needs.

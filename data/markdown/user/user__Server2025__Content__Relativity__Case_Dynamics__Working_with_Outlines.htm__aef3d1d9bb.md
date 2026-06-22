---
title: "Working with Outlines"
url: https://help.relativity.com/Server2025/Content/Relativity/Case_Dynamics/Working_with_Outlines.htm
collection: user
fetched_at: 2026-06-22T06:09:12+00:00
sha256: dd4e98bccc3c290c9d22f43ca7379e900e5a86583c858700352dd112589019ef
---

Working with Outlines Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Working with Outlines

With the Outlines feature in Case Dynamics, you can easily build case narratives, create free-form outlines, and link to existing or create new Case Dynamics objects and documents.

The Outlines tab includes a sample outline that gives a brief overview of how to use the feature and lets you test creating and linking objects to the outline.

## Adding an outline

To add a new outline from the Outlines tab, click New Outline . Enter a title for your outline, and then click Save . You can also apply a color to an outline.

## Editing an outline

To edit an outline, click . The Outline layout appears. Enter your text in the rich text editor. You can also copy and paste directly from Word into the outline. See Using the rich text editor .

### Locked outlines

If one user is editing an outline, the outline will be locked and available as read-only. A warning message appears to let users know the outline is being modified and who is editing the outline.

Before unlocking an outline, we recommend making sure no one is currently making edits. If you unlock an outline while edits are in progress, you may lose those changes.

To edit a locked outline:

- Make sure the Edition Locked field is added to a view in the Outlines tab.

- The Edition Locked field will read Yes. Click Yes to enable the field for editing.

- Click Yes again to edit the field.

- Select No .

- Click Save .

You can now edit the outline.

We recommend not editing Outline layouts as this may have adverse effects on Outlines functionality.

### Setting up a saved font color and style for users

To set up or edit a saved font color and style:

- Edit an outline.

- Click the User format settings toggle ( ) found along the top of the rich text editor.

- The font icon ( )is highlighted. Click the drop-down arrow to open the font options.

- Choose the designated font formatting for the user.

- Click Save .

To remove the saved font, click the User format settings toggle to turn it off.

### Adding new objects to an outline

You can create facts, key people, key organizations, and interview questions from within your outline.

To create a new Case Dynamics object from within an outline, complete the following steps:

- Highlight a section of text.

- Right-click and then select the Case Dynamics object you want to create.

You can also create a new Case Dynamics object from within an outline using keyboard shortcuts. See Outlines' keyboard shortcuts .

- (Optional) If you selected Key Person or Key Organization as your object type, Relativity compares the highlighted text to existing entities in the workspace to see if there is a possible match. Match types table

Match type Pop-up name Options

Key entity match Key Entity Match

- Link this Key Entity - the key entity becomes linked to the document.

- Create New Entity - creates a new key entity and links the key entity to the document.

- Cancel - closes the pop-up and does not link the highlighted text to an existing entity or create a new entity.

Entity match Possible Match

- Classify as Key Person or Classify as Key Organization - classifies the existing entity as key and links the key entity to the document.

- Create New Entity - creates a new key entity and links the key entity to the document.

- Cancel - closes the pop-up and does not classify an existing entity as key or create a new entity.

No match found Create New Entity

- Create New Entity - creates a new key entity and links the key entity to the document.

- Cancel - closes the pop-up and does not create a new entity.

-

Search Existing Entities - enables you to search existing entities to see if the entity already exists under a different spelling variation. Through the view that opens, you can search and filter on fields.

For an entity to appear in Case Dynamics, it must be classified as Key - Case Dynamics and required fields must be set. See Case Dynamics entities .

- (Optional) If you selected Fact as your object type, complete the following fields:

- Fact - a brief title for the fact. This field auto-populates with the text you highlighted.

- Date Type - designates whether the event occurred on or around a single date, or between two dates.

- Primary Fact Date - the date when the fact occurred, or the start date for an event that occurred between certain date.

- End Date -the completion of a fact that took place over a period of greater than one day.

- Click Add [object name] to create your object. Click Cancel to return to your outline without creating a new object.

#### Outlines' keyboard shortcuts

Keyboard shortcut Action

Alt +F Create Fact

Alt + I Create Issue

Alt + P Create Key Person (Entity)

Alt + O Create Key Organization (Entity)

Alt + Q Create Interview Question

### Linking an outline to existing objects

You can link to existing Case Dynamics objects as you type using the auto-fill feature. In the text editor, type the "@" symbol followed by one or more letters to bring up the auto-fill feature. Case Dynamics presents a pop-up list of facts, issues, entities, or interview questions based on the letters you type.

For an entity to appear in Case Dynamics, it must be classified as Key - Case Dynamics and required fields must be set. See Case Dynamics entities .

If you want to view and/or edit the full object details of an object within an outline, right-click on the object tag, and then click View . If a document is linked to an object, that document is automatically linked to the outline. If an object is tagged within an Outline tag, the tags are automatically linked to each other.

To remove an object tag from within an outline, right-click on the object tag, and then click Remove Tag . Any documents linked to that object will also be unlinked from the outline.

### Linking a document from within an outline

To link a document from within an outline, complete the following steps:

- Highlight a section of text.

- Right click and select Link to document .

- A pop-up window appears. Navigate to and select the document within Relativity you would like to link to the outline.

- Click Set .

- A hyperlink in the outline appears linking directly to the document.

### Viewing and editing object details

If you want to view and/or edit the full object details of an object within an outline, right-click on the object tag, and then click View .

To remove an object tag from within an outline, right-click on the object tag, and then click Remove Tag .

### Running a conflict check

If you tag a Case Dynamics object in the text editor and then update or delete that object outside the outline, the outline doesn't update automatically.

To resolve or ignore the conflicts:

-

Click Check Conflicts .

The Conflict Check window opens. The Conflict Check window has two sections: the Outline Text section and the Stored Value section. The Outline Text section reflects content from the outline. The Stored Value section contains the modified object.

-

(Optional) Click Resolve Conflict to update the Outline Text to match the Stored Value. For example, if you clicked Resolve Conflict in the screenshot above, Relativity would replace KCura in the Outline.

To change the Stored Value, close the Check Conflicts window and edit the object outside of the Outline.

- (Optional) Click Ignore Conflict to keep the Outline Text the same.

## View mode

When you save an outline, the outline appears in View mode. You can also open View mode by clicking from the Outlines tab. From View mode, you can view the full details of an outline including all facts, issues, people, organizations, and interview questions linked to the outline. You can also link documents to the outline and export the outline as a Word document. An option to download export history of Outline export date, user, and files is also available.

### Linking documents to an outline

To link documents to an outline while in View mode, complete the following steps:

- Click Link . a pop-up appears.

- Select the documents you want to link to your outline, and then click Add .

- Click Set .

To unlink documents from an outline, select the documents you want to unlink, and then click Unlink .

### Editing the view when linking to documents

You can edit the view when linking to documents.

When you link documents to an outline, a pop-up view appears. You can edit this view by unlocking the application and editing the Linking Documents view:

If you would like to keep the changes made to the Linking Documents view upon upgrading Case Dynamics, you must copy the existing Linking Documents View and name it Linking Documents Custom . This way, you do not have to unlock the application again to make changes.

### Exporting an outline

To export an outline while in View mode, click the Export Outline drop-down arrow in the Outline Text section, and then click Word .

You can export documents linked to an outline by checking Include Documents .

The documents will download as a zip file along with the outline text.

Only the native file version of the documents linked to the outline are downloaded in the zip file. If you have linked image files in your outline, they are not downloaded.

If you linked any documents within the outline, they will appear as hyperlinks. Clicking on the hyperlinks opens the documents in the zip file.

#### Export History

The Export History section contains the following fields:

- Export File - the files exported along with the Outline export.

- System Created By - the user who completed the export.

- System Created On - the date the files were exported.

You can export a list of the Export history as a .csv file by clicking the export button .

On this page

- Working with Outlines

- Adding an outline

- Editing an outline

- Locked outlines

- Setting up a saved font color and style for users

- Adding new objects to an outline

- Linking an outline to existing objects

- Linking a document from within an outline

- Viewing and editing object details

- Running a conflict check

- View mode

- Linking documents to an outline

- Editing the view when linking to documents

- Exporting an outline


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

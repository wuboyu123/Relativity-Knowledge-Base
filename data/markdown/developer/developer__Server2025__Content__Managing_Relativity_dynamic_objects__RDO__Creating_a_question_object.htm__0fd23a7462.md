---
title: "Creating a question object"
url: https://platform.relativity.com/Server2025/Content/Managing_Relativity_dynamic_objects/RDO/Creating_a_question_object.htm
collection: developer
fetched_at: 2026-06-22T06:29:27+00:00
sha256: b1aed6dfb2db67542226cdaa8e14a5ccfeafe6a28090302676e96613a9fb7de8
---

Creating a question object Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Creating a question object

Custodians can have multiple documents linked to them, but documents can have only one custodian. This is a one-to-many relationship: one custodian to many documents.

A reviewer may have one or many questions about a document, and each question may be associated with one or many documents. This is a many-to-many relationship: many documents to many questions.

For such a case, you can use the following steps to build a question and answer object that functions as a conversation about a document.

## Creating the Question object type

To create the object type:

- Inside the chosen workspace, navigate to the Object Type tab.

- Click New Object Type .

- Customize the object as follows:

- Name —Question

- Parent Object Type —Workspace

- Snapshot Auditing On Delete —enabled

- Click Save & Back .

The new Question object type appears in the list.

## Editing field and layout views

After creating the Question object type, edit the views for the Fields and Layouts tabs to show which object types are in use. If you already made the Object Type column visible, skip these steps and go to Creating the Question object fields .

### Editing the Fields view

To add the Object Type column to the Fields view:

- Navigate to the Fields tab.

- Click the View drop-down menu and click on the Edit icon (pencil) to the right of the All Fields view.

- Select Object Type from the Unselected section, then click the icon with the single right-pointing arrow to move it to the Selected section. You can adjust its position by clicking and dragging the field up or down in the list.

- Click Save .

The Object Type column now appears in the grid.

### Editing the Layouts view

After editing the Fields view, do the same for the Layouts view:

- Navigate to the Layouts tab.

- Click the View drop-down menu and click on the Edit icon (pencil) to the right of the All Layouts view.

- Select Object Type from the Unselected section, then click the icon with the single right-pointing arrow to move it to the Selected section. You can adjust its position by clicking and dragging the field up or down in the list.

- Click Save .

The Object Type column now appears in the grid.

### Filtering to view Question types

After editing the Fields and Layouts views, filter the Object Type column on those tabs to view items with the Question object type.

If the filter controls do not appear, click the Show Filters symbol at the top of the grid.

## Creating the Question object fields

Now that you have an object to store data, create question and answer fields to hold the information for that object. Typically, each question will be about a document being reviewed, and the reviewer will complete the answer field during review.

### Creating the Question field

To create a question field:

- Navigate to the Fields tab.

- At the top of the page, select All Fields from the drop-down menu.

- Filter the fields to show the Question object type.

- Locate the Name field and click on the Edit icon (pencil) for that row.

- Change the Name of the Name field to Question .

- Click Save & Back .

### Creating the Answer field

To create an answer field:

- Click New Field .

- Customize the new field as follows:

- Name —Answer

- Object Type —Question

- Field Type —Long Text

- Select Advanced Settings . Toggle the following field:

- Open to Associations —Enabled

- Click Save & Back .

### Creating a multiple object field

Now that the first two fields exist, create a multiple object field on the Document object to connect them. This field will be called Questions.

To create the Questions multiple object field:

- Click New Field .

- Customize the new field as follows:

- Name —Questions

- Object Type —Document

- Field Type —Multiple Object

- Associative Object Type —Question

- Click Save & Back .

## Writing questions and modifying the Question tab

Now that you have the object and fields, you can create the individual questions, add answers, and modify the Question tab for easy management.

### Adding new questions

Creating the Question object automatically adds a new tab called Question to your workspace. If you cannot locate this tab, or if you need to recreate it for any reason, see Creating and editing tabs Creating and editing tabs Creating and editing tabs .

To add a question for your reviewers to answer:

- Navigate to the Question tab.

- Click New Question .

- Type a question in the field.

- Click Save .

Repeat these steps to add as many questions as you want.

### Adding an Answer to the Question detail page

To add the Answer field to the detail page for a Question:

- From the Question tab, click on any question.

- In the upper left corner, click on the Edit icon (pencil) next to Question Layout.

This will open the Layout editor.

- Drag and drop the Answer field into the Default Category section.

- Click on the Default Category section to select it.

The section's options will appear on the right.

- Enter a more descriptive section name into the Name field, such as “Questions and Answers.”

- Click Save and Close .

The Answer field appears on the layout.

### Adding the Documents list to the Question detail page

To add a list of Documents associated with a Question to the layout, you must add an associative object list.

To add the Documents list to the layout:

- From the Question detail page, click on the Edit icon (pencil) next to Question Layout.

This will open the Layout editor.

- Click the down arrow next to Add Category and select Add Object List .

- Set the properties as follows:

- Object —Document (Questions)

- View —All Documents

- Link View —All Documents

- Friendly Name —Questions

- Click Save & Close .

You may need to refresh the page to see the changes.

### Adding Answers to the Question tab

Next, edit the All Question view to include the answers to the questions:

- From the main Question tab, expand the drop-down menu at the top of the page.

- Click the Edit icon (pencil) next to All Question.

The options for editing the All Question view will appear.

- Select Answer from the Unselected section, then click the icon with the single right-pointing arrow to move it to the Selected section.

- Adjust the Answer field's position by clicking and dragging it up or down in the list.

- Click Save .

## Adding questions to a layout in the viewer

Add questions to one or more review layouts.

The Question type object cannot be added to the layout as a field. Because it is a multi-object field, it must be added as an Object type.

To add questions to a layout:

- From the Documents list, click on any document.

- Select the coding layout where you want to add Questions.

- Click the Edit icon (pencil) next to the layout name.

The Layout editor will appear.

- Under Layout Options, click the down arrow next to Add Category and select Add Object List .

- Set the properties to the following:

- Object —Question (Questions)

- View —All Question

- Link View —All Question

- Friendly Name —Questions

- Click Save and Close .

This will add an associative list to the layout with the Questions and Answers visible for that document.

## Setting up Question-related views

The following views will help with tracking which documents have questions attached.

For more information on creating views, see Creating a view Creating a view .

### Creating a Document view for documents with questions

- Navigate to the Documents tab.

- Open the View drop-down menu and click New View .

- Enter “Documents with Questions” in the Name field.

- In the Fields section, double-click on each of the following fields to move them to the Selected column:

- Edit

- File-Icon

- Control Number

- Questions

- Questions::Answer

- On the Conditions tab, click the + Condition button.

- Select the Questions field from the drop-down list.

A pop-up modal appears.

- Select the following:

- these conditions

- Questions

- In the selector that appears, choose is set from the upper left drop-down menu.

- Click Apply on the selector, then again on the Conditions modal.

- Click Save .

### Creating a Document view for documents with no questions

- Navigate to the Documents tab.

- Open the View drop-down menu and click New View .

- Enter “Documents without Questions” in the Name field.

- In the Fields section, double-click on each of the following fields to move them to the Selected section:

- Edit

- File-Icon

- Control Number

- Questions

- Questions::Answer

- Unified Title

- On the Conditions tab, click the + Condition button.

- Select the Questions field from the drop-down list.

A pop-up modal appears.

- Select the following:

- NOT these conditions

- Questions

- In the selector that appears, choose is set from the upper left drop-down menu.

- Click Apply on the selector, then again on the Conditions modal.

- Click Save .

## Linking questions to a document during review

After the associative list has been added to the review layout, the controls for linking questions will appear during review.

Reviewers can add or remove questions from the document using these buttons:

- New —opens the screen to create a brand new question. To return to the document viewer from this screen, click Save and Back .

- Link —opens a modal to select an existing question and link it to the document.

- Unlink —unlinks a selected question from the document.

After linking or unlinking a question, the reviewer may need to refresh the page to see changes.

On this page

- Creating a question object

- Creating the Question object type

- Editing field and layout views

- Editing the Fields view

- Editing the Layouts view

- Filtering to view Question types

- Creating the Question object fields

- Creating the Question field

- Creating the Answer field

- Creating a multiple object field

- Writing questions and modifying the Question tab

- Adding new questions

- Adding an Answer to the Question detail page

- Adding the Documents list to the Question detail page

- Adding Answers to the Question tab

- Adding questions to a layout in the viewer

- Setting up Question-related views

- Creating a Document view for documents with questions

- Creating a Document view for documents with no questions

- Linking questions to a document during review


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

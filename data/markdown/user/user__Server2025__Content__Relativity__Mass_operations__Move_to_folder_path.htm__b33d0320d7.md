---
title: "Move to folder path"
url: https://help.relativity.com/Server2025/Content/Relativity/Mass_operations/Move_to_folder_path.htm
collection: user
fetched_at: 2026-06-22T06:09:40+00:00
sha256: 73615dd173ef50c8b9329856f89d6b153fa820d3ed5a70fc5a4a0bebdc69f543
---

Move to folder path Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Move to folder path

You can use the move to folder path mass operation to move documents to a new folder that you specify in a text field on the document object. Relativity automatically creates the new folder when you run this mass operation. You can also specify a default folder that Relativity uses when the destination folder path isn't set on a document. You must install the Document Utilities application to add the Move to folder path mass operation to your workspace. The Document Utilities application also contains the Document Unitization solution. For more information, see Document Unitization .

A sample use case for this mass operation involves updating the folder path for documents loaded into the wrong folder on a workspace. For example, you may have inadvertently selected file path as the folder path when importing documents through the Relativity Desktop Client (RDC).

In addition, the move to folder path mass operation provides you with the ability to move multiple documents to different folders simultaneously. Unlike the mass move operation, where you can only select a single folder when moving documents. For more information, see Mass move .

This page contains the following information:

- Prerequisites for the move to folder path mass operation

- Running the move to folder path mass operation

## Prerequisites for the move to folder path mass operation

You must complete the following prerequisites before you can use the move to folder path mass operation:

### Installing the Document Utilities application

Installing the Document Utilities application

You must install the Document Utilities application to add the Move to folder path mass operation to your workspace. The installation process follows the same steps used to install other Relativity applications. For more information, see Installing applications .

You must have system admin permissions to install an application. See Workspace security .

Complete these steps to install the application:

- The Document Utilities application requires Relativity 9.4 or above of Relativity. Confirm that you are running Relativity 9.4 or above in your environment.

- Log in to the Relativity Community , and search on Document Utilities. When the search results appear, locate the Relativity.DocumentUtilities.rap in the Files section.

You need to register to access the Relativity Community if you don't currently have an account. You also must have an Admin Contact account type in the Relativity Community to download applications. If you don't currently have this account type, contact an Admin Contact in your organization, who can then request that Customer Support assign this account type to you. For more information, contact Customer Support .

- Download the Relativity.DocumentUtilities.rap.

- Install the Document Utilities application in a workspace or add it to the Application Library tabs making it available for installation in workspaces across your environment. For more information, see Installing applications .

After installing the application, Relativity displays the Move to folder path option in the drop-down menu on the mass operations bar.

### Setting required security permissions

Setting required security permissions

You must have the following security permissions to run the move to folder mass operation:

- Mass operations - Under the Mass Operations section of the Other Settings Tab in Workspace Security, you need permissions to the following:

- Move

- Move to folder path

- Object security - you need to have the following permissions on these objects in the Object Security tab under Workspace Security:

- Document - requires Add and Delete permissions.

- Folder - requires Add and Edit permissions. If you want to remove empty folders, you also need Delete permissions.

- Layout security - you need to have View permissions on the Move Documents to Folder Path Layout in the Layouts tab.

- Folders security - you need permissions to Folders in the Browsers section of the Other Settings tab.

For more information about permissions, see Workspace security .

Creating a destination folder path field

Before you can run this mass operation, create a fixed-length or long text field type for storing a destination folder path on the document object. For more information, see Fields .

Use these guidelines for formatting your folder path:

- Separate nested folders in the path with forward slashes (/) or backward slashes (\).

- Don't use a slash as the initial character in your folder path. A final slash isn't required in the folder path.

- Don’t use these special characters (/ \ : ? " * < > |) in your folder names. If your folder names include these characters, Relativity strips them out, except for back and forward slashes used as delimiters. For example, a path with folders named Custodians|<>/Revie\wed/Ja*?ne would become Custodians/Reviewed/Jane .

- Folder paths may include Unicode characters.

- Folder paths may include the workspace name, but it isn't required. For example, if you have a document with a destination path of <WorkspaceName>\Custodian and another one with the path of Custodian , this mass operation moves both documents to the Custodian folder under the workspace root.

Populating the folder path field on the document object

After creating a folder path field on the document object, you must populate it with a destination folder path for the documents that you want to move.

Perform one of the following tasks to populate this field with the destination folder path:

- Edit the field - click the Edit link that appears on the Documents tab, and update this field on the document when Relativity displays the layout containing it.

- Run a mass edit operation - see Mass edit .

- Overlay the destination folder fields on documents - see Importing document metadata, files, and extracted text .

The following screen shot illustrates a list of documents with a folder path field set to a specific destination:

## Running the move to folder path mass operation

When you run the move to folder mass operation, Relativity moves all the documents with the same destination folder in a single batch. While the Move to folder path mass operation batches documents moving to the same folder, the MassCustomBatchAmount and the MassMoveBatchAmount instance settings control the batching process. The MassCustomBatchAmount instance setting controls the number of documents per batch for each unique destination folder. The MassMoveBatchAmount value controls the number of documents for each batch size.

For optimum performance, use these guidelines when running this mass operation:

- Perform a test on a small sample set of documents before moving a large number of them.

- Execute only one move to folder path mass operation at a time.

Use these steps to move documents to a new folder:

- Navigate to the Documents tab in your workspace.

- Select the documents that you want to move to the destination folder path.

- In the first drop-down menu in the mass operations bar, choose Checked or All based on your selections from the current document set.

- Select Move to folder path in the second drop-down menu, and then click Go .

- Complete the fields in the Folder path settings dialog. See Fields for move to folder path mass operation .

- Click OK to run the mass operation. Relativity creates any destination folders that don't currently exist, and moves the documents to their specified destination folders. It also moves any documents with an empty folder path field to the location specified in the Empty folder path placeholder field. See Fields for move to folder path mass operation .

To stop the mass operation, click Cancel . The mass operation finishes moving the current batch of documents before it stops. Relativity then displays a message indicating the percent of documents that were moved.

- Optionally, refresh the page to see the newly created folders. See the following screen shot for an example of a new folder structure:

### Fields for move to folder path mass operation

The Folder path settings dialog includes the following fields:

- Folder Path Field - click to select the field that you populated with the destination folder path. See Move to folder path .

- Delimiter - select forward slash (/) or back slash (\) as the delimiter for any nested folders.

- Move documents with empty folder path - select this checkbox if you want to move documents with empty folder path fields to the location specified in the Empty folder path placeholder option. If you don't select this checkbox, Relativity doesn't move documents with empty folder path fields.

- Empty folder path placeholder - enter the name of a folder where you want to move documents that don't have a destination specified in their folder path field. If the path contains subfolders, separate the folders with the same delimiter as you selected in the Delimiter field. This folder path may include Unicode characters.

The following list describes how Relativity handles empty folders:

- If a folder path contains one or more empty folders, then Relativity replaces the blank location with the name in the Empty folder path placeholder field. For example, it updates the folder path MyFolder\\MySubfolder to MyFolder\[BLANK]\MySubfolder , if the name in this field is [BLANK].

- If a folder path contains consecutive empty directories, Relativity consolidates them into a single directory, so that MyFolder\\ \\\MySubfolder becomes MyFolder\[BLANK]\MySubfolder when the name in this field is [BLANK].

- If a folder path contains two consecutive delimiters separated by a space, Relativity sets the name of the newly created folder to blank.

- Delete empty folders - select this checkbox if you want to delete any folders that are empty after you move the documents. Relativity doesn't delete empty folders when they have dependencies.

If an error occurs during the deletion of empty folders, Relativity stops this process and displays an error message. It also logs any errors on the Error tab. For more information, see Errors .

On this page

- Move to folder path

- Prerequisites for the move to folder path mass operation

- Installing the Document Utilities application

- Setting required security permissions

- Running the move to folder path mass operation

- Fields for move to folder path mass operation


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

---
title: "Simple File Upload"
url: https://help.relativity.com/Server2025/Content/Relativity/Simple_File_Upload/Simple_File_Upload.htm
collection: user
fetched_at: 2026-06-22T06:08:27+00:00
sha256: c66c371e8d15851684126bd87ffe9a5a56cb4e209544ee6e70ddc9f3c4fe5533
---

Simple File Upload Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Simple File Upload

Simple File Upload, formerly Single File Upload, gives users the ability to add new documents to Relativity without using the Relativity Desktop Client.

## Special considerations

Keep the following considerations in mind:

- To use Simple File Upload, you must be running .NET 4.6.2 for all server side machines, including: web server, invariant, agents, and workers.

- To use Simple File Upload with Relativity, the Relativity web servers must have Visual C++ Redistributable 2013 x86 and x64.

- When you upload a document using Simple File Upload, Relativity imports the following metadata:

- ArtifactID

- Control Number

- Extracted Text

- Relativity Folder Name

- Has Images

- Has Native

- Relativity Native Type

- Supported By Viewer

- System Created By

- System Created On

- System Last Modified By

- System Last Modified On

- File Name

- File Size

- The direct upload of EXE, DLL, and HTML files is prohibited in Simple File Upload for security reasons. An error message will be displayed if you attempt to upload them.

- You can search extracted text with keyword search. However, if Data Grid is enabled on a field, keyword searching is disabled.

## Workspace security permissions

To configure workspace security permissions for Simple File Upload:

- Navigate to the Relativity Utilities console on the Workspace Details tab.

- Click Manage Workspace Permissions .

- Click Edit Permissions for a group on the Group Management tab.

- Grant access to the workspace security permissions listed in the table.

Object Security Tab Visibility Other Settings

- Document - View, Add

- New Document (child)

- Documents

- Admin Operations: Allow Import

- The New Document button will appear in all workspaces. You can only remove the button by removing the Add Document permission from individual users.

## Accessing Simple File Upload

Access Simple File Upload within a workspace in the Documents tab. The application functions on the Folders, Clusters, and Field Tree browsers.

You need to have the Add Document permission to access the New Document button.

## Uploading new documents

To upload a new document to a workspace:

- Click New Documents icon ( ), which is located to the left of the View bar. The New Documents pop-up window appears.

- Drag and drop up to 100 files into the New Documents pop-up window or click on the pop-up to select files that you want to upload.

- The SFUMaxFilesToUpload instance setting determines the maximum number of documents you can upload using Simple File Upload. Admins can set the maximum number of documents that you can upload at one time up to 100.

- When the instance setting is set to 100, you can only upload up to 100 files at one time with Simple File Upload. If you select more than 100 files, Relativity will only upload the first 100 files you selected. Any files after the first 100 will not upload. A warning message will be displayed in the pop-up if more than 100 files are selected.

The selected files will be displayed in a list. If you choose not to upload one of the selected files, click the delete icon next to the file's name in the pop-up.

-

Click Upload . When a document uploads successfully, a green check mark appears next to the file name. A progress bar tracks the progress of all the files selected.

You cannot upload a document that shares a Control Number with a document that already exists in Relativity. If you want to replace a document, use the Replace document native icon in the Review Interface. See Replacing documents .

### Replacing documents

The Viewer supports the ability to replace natives and images as an option in the Document Actions drop-down menu.

## Replacing documents

The Viewer supports the ability to replace natives and images as an option in the Document Actions drop-down menu.

You need edit, add, and delete document permissions as well as to access the Replace document native icon.

To replace a document in the viewer:

- Open a document.

- Navigate to the layout and click Replace document native . The Replace Document pop-up widow opens.

- Drag and drop or select the document that you would like to replace the current document in the viewer with.

On replace, the following meta data is uploaded:

- ArtifactID

- Control Number

- Extracted Text

- Folder Name

- Has Images

- Has Native

- Relativity Native Type

- Supported By Viewer

- System Created By

- System Created On

- System Last Modified By

- System Last Modified On

- FileName

- FileSize

- FileExtension

If you replace a document with a document that shares the same control number, Relativity overwrites the following fields:

- FileName

- FileSize

- FileExtension

- Extracted text

- Supported By Viewer

- Relativity Native Type

- Has Native

- System Last Modified On

- System Last Modified By

## Simple File Upload for processing errors

If you have the Simple File Upload application installed on your workspace, you have the option of opening an individual processing error, downloading the errored file, and uploading the repaired file as a replacement after you resolve the error outside of Relativity.

This is available through the Error Actions console, which appears on the Processing Error Layout after you have configured your environment with the assistance of a support representative.

- This option is available only for document-level errors that have a status of Ready to Retry.

- The Error Actions console is hidden from the error layout if the option to Download and upload files with processing errors is not checked for the Processing Error object in the workspace security console. In order to access this functionality, every user, including system administrators, must be included in a group where this option has been manually checked after installing or upgrading the Simple File Upload application.

- The Download and upload files with processing errors permission was added in Relativity 9.5.219.30 .

To upload a Simple file for a processing error, perform the following steps:

- Navigate to the Processing | Document Errors tab, locate the error you'd like to resolve, and click on the name of the error in the Current Error Message field to get to the document error layout.

- Click Download File on the Error Actions console on the right side of the layout. Note that when you do this, you're downloading the document from the same folder patch displayed in the Document file location field on the document error layout.

- Once the file appears in the lower-right hand corner of your browser window, either open or save it to your local machine.

- Outside of Relativity, address the error to repair the file. For example, if the error was due to password protection because you didn't previously provide that password in the Password Bank, enter it now to decrypt the file. Then, save the decrypted file to your local machine so that you can upload it here.

- Once you've repaired the file, return to the document error layout and click Upload Replacement File on the Error Actions console.

- You must upload a file of the same extension as the file you downloaded or you will receive an error. If you receive this error, either click Upload New Document to return to your file explorer or click Cancel to return to the document error layout.

- Confirm that the upload completed successfully. Note that when you replace a document in this way, the Document file location, File ID, and Name values of the replacement document are identical to those of the file you downloaded.

- Click Retry in the Error Actions console.

- When the Retry Error pop-up opens, click Retry .

- The current status will change to Resolved .

### Viewing audits for processing errors

When you use Simple File Upload for processing errors, Relativity audits your actions, which you can view via the View Audit button on the processing error layout. When you open the audit view, you can see such actions as File Download and File Upload , along with the processing error file download and replacement paths, among other details.

Auditing for Simple File Upload for processing errors was added in Relativity 9.5.219.30 .

You can also access audit information through the History tab by filtering on the Object Type field for ProcessingError and on the Action field for File Download and/or File Upload .

On this page

- Simple File Upload

- Special considerations

- Workspace security permissions

- Accessing Simple File Upload

- Uploading new documents

- Replacing documents

- Replacing documents

- Simple File Upload for processing errors

- Viewing audits for processing errors


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

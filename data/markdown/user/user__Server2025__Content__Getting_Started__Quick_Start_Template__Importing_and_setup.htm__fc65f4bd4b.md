---
title: "Importing and setup"
url: https://help.relativity.com/Server2025/Content/Getting_Started/Quick_Start_Template/Importing_and_setup.htm
collection: user
fetched_at: 2026-06-22T06:12:12+00:00
sha256: 4066bbf60044dceb49098c56dcab2d8dd701f86de63be8867a66fffc9bbcf50f
---

Importing and setup

# Importing and setup

Loading data is one of the first and most important parts of the system admin role. Performing this incorrectly can negatively impact subsequent processes and complicate document review.

The Quick Start template is built with a strong core group of fields but may not contain every field your case might need.

All importing functionality is handled by the Desktop Client. You can download this utility from the Workspace details tab in Relativity.

## Fields

To begin the loading process, first check to see that you have fields created for all of your data. Relativity offers a variety of field options. Determining the most appropriate field type for your data makes your database more intuitive and efficient. See the Relativity Desktop Client .

After you select your load file, you can change the delimiters on the left. The first row of your load file appears in the window to the right. If all delimiters are set with the correct specifications, then all the field names should appear in one column.

Click on the Field Map tab to line up your fields to load.

- The most important field is a unique identifier field. The Quick Start template uses the Beg Doc ID field.

- The identifier field must be unique for each record and is required as a part of every load or overlay.

- After creating a field you can change its name and other properties, but you can't change its type.

- Load file field names do not have to match database field name. You can load a field named Control Number into the template Beg Doc ID field. Likewise, Email BCC field might be named BCC in the load file.

You can choose to append new data or overlay data on already existing records by changing the settings below the field lists. If you overlay records, you must select the identifying field for the overlay. It can be any fixed-length text field that is indexed. However, the best method for overlaying data is to use the unique identifier field.

You enter the browser folder information and native file paths separately. Select the check box next to the fields to indicate that you have data to load for a folder and file path, then choose the appropriate fields. The folder path is the location within the folder hierarchy that the document appears in Relativity. The file path connects the viewer to the native file.

The Advanced button under Native File Behavior copied the native files from a disk or link to files already on a image server.

The extracted text option is where you indicate that the extracted text is available in a separate file. Only a file path is needed if this is checked. If this isn't checked the extracted text data is expected in the load file.

If errors occur, the Desktop Client produces an error file listing all problematic records, and no part of those records is loaded into Relativity. After the initial load is complete, click OK to save the error files, if needed. Edit the error file and then try to load the records again. For a list of errors and fixes for them, see Import errors for Desktop Client . Because Relativity creates a separate file of only records with errors and doesn't load them, you can edit the error load file instead of the large and sometimes cumbersome original load file.

Things to remember:

- At this point you can still create and add fields. If you find one in the load file that was missed in the database, go ahead and open Relativity and add a field or edit a field to match the data to load. Go to the File menu and select Refresh to see the field in the Relativity Desktop Client list. The new field appears at the bottom of the field list; it is not placed alphabetically.

- The Document Identifier must be unique. Only the first occurrence is loaded if there are duplicates in your load file. Choose Overlay to add more data to existing records. The Overlay must have the Document Identifier with the new data.

- You cannot change the field type for fields already created. You need to rename the current field and make a new one with the required field type.

- Not all fields need to be loaded. Leave the fields you don’t want loaded in the outside column.

- Don’t start the load process while creating fields. Be sure to only create fields before or after loading data.

- Fixed Length text fields should not be greater than 500 characters, larger field sizes might affect database performance.

- Be sure you have permissions to load to the selected folder.

- When overlaying a multi-choice field the previous content of the record is overwritten not merged with new data.

- If for any reason a record is not able to be loaded the entire record is skipped. A record is never partially loaded.

## Field list

Below is a breakdown of the fields found in the Quick Start template workspace, including type and a description. Fields can be added at anytime during the case but this standard set of fields should provide a solid foundation for your database. There are other fields visible in the case; however, those fields won't be populated until a later time. These are system fields or fields dependent on tasks that occur as you begin using the database.

Family group is all items that are physically or electronically attached. A fax cover sheet and documents sent are a family group as well as an email and its attachments. The parent item is the email and the child items are the attachments to the email.

### Extracted metadata fields

The following tables list document metadata fields included in the Quick Start template. These lists don't include the system-level fields.

Extracted metadata fields accommodate document extracted text.

Field Name Type Description Group By Pivot

All Custodians Multi-Object All custodians (deduped and original) associated with a file (available only when Global Deduplication is enabled and duplicates are present).

All Paths/Locations Multi-Object All path fields (deduped and original) associated with a file (available only when Global Deduplication is enabled and duplicates are present).

Attachment Name Long Text Lists the file name(s) of each attachment to an email message, separated by semicolons, extracted from metadata. Only present on parent items

Categories Multi-Choice Category field extracted from the metadata of the file by processing vendor Y Y

Control Num Beg Attach Fixed Length: 60 Document ID of first document page of family group ***for imaged documents

Control Num End Attach Fixed Length: 60 Document ID of last page of family group *** for imaged documents

Control Num End Fixed Length: 60 Document ID end number for scanned/TIFFed documents based on page level numbering

Control Number Fixed Length: 60 Document ID beginning number for scanned/TIFFed documents based on page-level numbering

Created Date Long Text The date on which a file was created.

Created Time Long Text The time at which a file was created.

Custodian Single Choice User-assigned custodian passed to metadata extraction software or manually associated with scanned documents Y

Date Created Date Date and time from the Date Created property extracted by the metadata extraction software from the original file

Date Last Modified Date Date from the Modified property of a document, representing the date and time that changes to the document were last saved

Date Received Date Date and time an email message was received (according to original time zones)

Date Sent Date Date and time an email message (according to original time zones) was sent Y

Delivery Receipt Yes/No Created by the email application if the email author turned on the delivery receipt request notification. The value is either (True) or (False) depending on whether the email was registered as delivered to a recipient.

Document Extension Fixed Length: 60 Three-character extension of document that represents the file type to Windows Operating System created by metadata extraction software. Y

Document Title Long Text The title of a non-email document. This is blank if there is no value available.

Email BCC Long Text Recipients of blind carbon copies of email messages

Email CC Long Text Recipients of carbon copies of email messages

Email Created Date/Time Date The date and time at which an email was created.

Email Entry ID Long Text The unique Identifier of an email in an mail store.

Email From Fixed Length: 320 Author of the email message extracted by metadata extraction software Y Y

Email Has Attachments Yes/No The yes/no indicator of whether an email has children (attachments).

Email Folder ID Long Text The folder path in which a custodian stored an email.

Email Format Single Choice The indicator of whether an email is HTML, Rich Text, or Plain Text.

Email Last Modified Date/Time Date The date and time at which an email was last modified.

Email Modified Flag Yes/No The yes/no indicator of whether an email was modified.

Email Sent Flag Yes/No The yes/no indicator of whether an email was sent, versus saved as a draft.

Email Subject Fixed Length: 255 Subject of the email message extracted by metadata extraction software

Email To Long Text Recipients of email message extracted from email file by metadata extraction software Y Y

Embedded Data Info Fixed Length: 400 Message indicating that there are tracked changes, hidden fields or data present in native file. Can be changed to HTML field in Relativity to provide warning to reviewers to check native file for data not available in viewer.

Excel Hidden Columns Yes/No The yes/no indicator of whether an Excel file contains one or more hidden columns.

Excel Hidden Rows Yes/No The yes/no indicator of whether an Excel file contains one or more hidden rows.

Excel Hidden Worksheets Yes/No The yes/no indicator of whether an Excel file contains one or more hidden worksheets.

Excel Pivot Tables Yes/No The yes/no indicator of whether an Excel file contains pivot tables.

Exceptions Yes/No "Y" for documents with issues while processing or exceptions that occurred during metadata extraction

Extracted Text Long Text The full, unformatted content of the document obtained either by extracting from electronic file or by OCR processing of scanned images

File Name 255 File name of the native file extracted as metadata

File Path Fixed Length: 255 The full path or relative path to the location of the physical file to be viewed in Relativity

Filesize Whole Number Size of the native file in bytes

Folder Path Fixed Length: 255 Path of original file not including file name. This may be the file hierarchy on the system.

Header Long Text Contents of the email message header extracted from metadata

Image Taken Date/Time Date The date and time at which an original image was taken.

Is Embedded Yes/No The yes/no indicator of whether a file is embedded in a Microsoft Office document.

Is Parent Yes/No The yes/no indicator of whether a file is not a child.

Keywords Long Text Keywords field extracted from the metadata of the native file

Last Accessed Date Date The date on which a loose file was last accessed.

Last Modified Date Date The date on which changes to a file were last saved.

Last Modified Time Long Text The time at which changes to a file were last saved.

Last Printed Date Date The date on which a file was last printed.

Last Printed Time Long Text The time at which a file was last printed.

Last Saved Date Long Text The date on which a file was last saved.

Last Saved Time Long Text The time at which a file was last saved.

Lotus Notes Other Folders Long Text A semi-colon delimited listing of all non-primary folders that a Lotus Notes message or document was included.

MD5 Hash Fixed Length: 32 Unique identifier created for electronic file or email generated by metadata extraction software and used for deduplication. This algorithm isn't available for deduplication scanned images.

Meeting End Date Long Text The date on which a meeting item in Outlook or Lotus Notes ended.

Meeting End Time Long Text The time at which a meeting item in Outlook or Lotus Notes ended.

Meeting Start Date Long Text The date on which a meeting item in Outlook or Lotus Notes started.

Meeting Start Time Long Text The time at which a meeting item in Outlook or Lotus Notes started.

Message Class Single Choice The type of item from an email client (e.g., email, contact, calendar, etc.).

Message ID Fixed Length: 255 Unique identifier of emails in mail stores created by software and extracted to field by software

Number of Attachments Whole Number Number of attachments for a particular record. The count of the child items in the family group only appear on the parent document record.

Organization Fixed Length: 255 Company field extracted from the metadata of the file

Original Author Name Fixed-Length Text The display name of the original author of an email.

Original Email Author Fixed-Length Text The email address of the original author of an email.

Original File Extension Fixed-Length Text The original three (or more) character extension of the file that represents the file type to the Windows Operating System (e.g., PDF, DOC, TXT, etc.).

Original Folder Path Fixed Length: 255 Folder location of each native file within the hierarchy extracted by software

Outlook Flag Status Single Choice The indicator of which flag, if any, an Outlook item has assigned to it (NoFlag, FlagMarked, or FlagComplete).

Pages Whole Number Available for imaged documents only

PowerPoint Hidden Slides Yes/No The yes/no indicator of whether a PowerPoint file contains hidden slides.

Privilege Hits Long Text List of responsive privilege term hits found in the document and separated by semicolons. These terms must be provided before metadata extraction.

Read Receipt Yes/No Read receipt request notification value saved within the email system and extracted from metadata

Received Date Date The date on which an email message was received.

Received Time Long Text The time at which an email message was received.

Recipient Name (To) Long Text The name(s) of the recipient(s) of an email message.

Review Beg Attach Fixed Length: 60 Review ID of the first item in a family group *** created by the metadata extraction software. The same numbers for begin and end attachments repeat for all members of the family group. ***

Review End Attach Fixed Length: 60 Review ID of the last file in a family group*** numbered by the metadata extraction software***

Review ID Fixed Length: 60 Unique document-level identification number assigned by metadata extraction software. It's incremented by one per document and not based on pages.

Review Volume Fixed Length: 60 Review volume name

Search Hits Long Text List of responsive search term hits found in document separated by semicolons. These terms must be provided before metadata extraction.

Sender Name Fixed-Length Text The name of the sender of an email message.

Sensitivity Single Choice Sensitivity field extracted from an email (ex: 0 = Normal; 1 = Personal; 2 = Private; 3 = Confidential)

Sent Date Date The date on which an email was sent.

Sent Time Long Text The time at which an email message was sent.

Suspect File Extension Yes/No The yes/no indicator if whether the extension of a file does not correspond to the actual type of the file (e.g., XLS for a Word document).

Title Long Text The title of the file. For emails, this is the subject line. For non-emails, this is any available title.

Unread Yes/No Read status of an email indicating whether an has ever been opened. True means is has never been opened. False means it has been opened.

### Processing fields

The following system-created metadata fields are always populated when data is processed.

Processing Field Name Field Type Description

Container Extension Fixed-Length Text Document extension of the container file in which the document originated.

Container ID Fixed-Length Text Unique identifier of the container file in which the document originated. This is used to identify or group files that came from the same container.

Container Name Fixed-Length Text Name of the container file in which the document originated.

Control Number Fixed-Length Text The identifier of the document.

Custodian Single Object Custodian associated with (or assigned to) the processing set during processing.

Discovery Error Child Document Long Text The identifier of the file that contains the parent document on which the error occurred.

Extracted Text Long Text Complete text extracted from content of electronic files or OCR data field. This field holds the hidden comments of MS Office files.

Last Published On Date Date on which the document was last updated via re-publish.

Level Whole Number Numeric value indicating how deeply nested the document is within the family. The higher the number, the deeper the document is nested.

Originating Processing Set Single Object The processing set in which the document was processed.

Originating Processing Data Source Single Object A single object field that refers to the processing data source.

Processing Duplicate Hash Fixed-Length Text Identifying value of an electronic record that is used for deduplication during processing.

Processing File ID Fixed-Length Text Unique identifier of the document in the processing engine database.

Processing Folder Path Long Text The folder structure and path to the file from the original location, which is used to generate the Relativity folder browser for your documents. This field is populated every time you process documents. See Processing folder path details for more information.

Processing Errors Multiple Object Any associated errors that occurred on the document during processing. This field is a link to the associated Processing Errors record.

Time Zone Field Single Object Indicates which time zone is used to display dates and times on a document image.

Virtual Path Long Text Folder structure and path to file from the original location identified during processing. See Virtual path details for more information.

### Relativity script fields

Relativity script fields are required when using Relativity scripts.

Field Name Type Description Group By Pivot

Parent Date Date Date of parent document propagated to entire family group. Generally the Date Sent field is used for email and date modified field is used for documents. Y

### Outside source fields

These outside fields are used to accommodate data from production software.

Field Name Type Description Group By Pivot

Bates Prod Beg Fixed Length: 60 Bates number or production number on first page of document

Bates Prod Beg Attach Fixed Length: 60 First Bates number or production number in family group ***

Bates Prod End Fixed Length: 60 Bates number or production number on last page of document

Bates Prod End Attach Fixed Length: 60 Last Bates number or production number of last page in family group ***

Production Volume Fixed Length: 60 Production volume name assigned during production and only available on documents produced

### User input

User input fields handle coding and production information.

Field Name Type Description Group By Pivot

Designation Single Choice Responsiveness of document determined by reviewers. Indicates whether document needs to be produced for a document request. Choices typically are Responsive, Non-Responsive, Privilege or Not Sure. Y Y

Issues Multi-Choice Issues for the case Y Y

Markup Set-Review Fixed Length: 400 Markup Set - Review

Privilege Description Long Text Explanation of privilege reason coded by reviewers

Privilege Type Multi-Choice Type of privilege information in document decided by reviewer. Choices might include Attorney-Client Communication, Attorney Work Product, etc. Y Y

Production Create Date Date Date and time of production creation Y Y

Production Date Date Date a production was sent Y Y

## Relational fields

Relativity has a Related Items pane for viewing groups of related documents. When reviewing a single document the related items pane is at the lower right corner by default. This relational information is passed to the database from the loaded data. Any fixed-length text field under 450 characters can be relational. Using the same document identifier information across documents, the database knows what items are related. Examples of relational fields are:

Field Name Displays

Conversation ID Email Threads

MD5 Hash Exact duplicate items

Review Beg Attach Family items

## Propagation

Propagation makes the field information consistent across all records in a related items group. In the template no fields have been set for propagation. You might want to propagate duplicates or family groups, but remember the field must be relational.

Things to remember:

- Propagation applies to only one tier of related items. Selecting the duplicate of an item only propagates to the duplicate, not to the duplicate and the duplicate's family members.

- Propagation doesn't work when importing items through the Desktop Client.

- Propagation requires two steps:

- Related item creation

- Checking Propagation on the field you want to propagate

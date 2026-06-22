---
title: "Mapping processing fields"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Mapping_processing_fields.htm
collection: user
fetched_at: 2026-06-22T06:02:31+00:00
sha256: 422cc37ccf2d6d981f7ec97ff7fabd52c572cd25f74cda39ae6662612f2be5cd
---

Mapping processing fields

# Mapping processing fields

To pull in all of your desired processing data, use the Field Catalog to map your document fields to Relativity's processing data.

This section provides information on all system-mapped fields in Relativity, as well as the optional metadata fields available to you to map to your data.

Read if you are studying for the Processing Specialist exam The content on this site is based on the most recent monthly version of Relativity, which contains functionality that has been added since the release of the version on which Relativity's exams are based. As a result, some of the content on this site may differ significantly from questions you encounter in a practice quiz and on the exam itself. If you encounter any content on this site that contradicts your study materials, please refer to the What's New and/or the Release Notes for details on all new functionality.

## Mapping fields

To map processing fields, perform the following steps:

- Open the Fields tab.

- Click New Field or Edit on an existing field.

- Provide a name in the Name field. We recommend that you give the field an identical name to the one you are mapping to.

- In the Object Type field, select Document . Only Relativity Document fields are eligible to map to a value in the Source field. Selecting any other object type disables the Source field.

- In the Field Type field, select the type of field to set what type of data can be entered into the field.

- When the Field Type is selected, you will see the menu for Field Settings and Advanced Settings appear. Click on the Advanced Settings tab.

- Click Select on the Source field to display the processing fields to which the Relativity field can be mapped.

- From the available processing fields, select the one to which you want to map, and click Set .

- Confirm that the field you just mapped appears in the Source field, complete the remaining required fields and click Save .

If the Processing application is not installed, you can still map fields as long as you have added the worker manager server to the resource pool.

### Processing system field considerations

Note the following regarding processing system fields:

- Processing system fields are mapped by default and cannot be modified.

- Processing system fields aren't listed in the Field Catalog.

A word on Field Catalog source fields

While processing data in an instance, Relativity discovers metadata fields and records them as source fields in the Field Catalog. You can map source fields in the Document object, where the field is then populated when a document is published.

This occurs instance-wide. This means if one workspace processes a field with a unique metadata name, all other workspaces will see the source field as available for mapping. Even if the workspace has never, and possibly will never, process a file with the same field name.

Example

Workspace 1 - processes a file with a unique metadata name, UniqueData . The field becomes part of the Field Catalog and is available to all other workspaces in the instance.

Workspace 2 - sees UniqueData in the Field Catalog, even though Workspace 2 has never processed a file with the metadata name.

### Field mapping validations

When mapping fields, you will receive an error if:

- You attempt to map fields of mismatching types. For example, if you map a long text field to a date field, you will receive an error upon saving the field.

- You attempt to map a fixed-length text field to a catalog field of a longer length.

- You do not have Edit permissions for the Field object. This is because mapping through the Source field is considered an edit to a field. If you only have Add permissions for the Field object and not Edit, and you attempt to map a field, you will receive an error stating, “Error saving field mapping."

## System-mapped processing fields

The following system-created metadata fields are always populated when data is processed.

These fields are automatically mapped when you install or upgrade the Processing application from a version earlier than 9.4. They are not available for manually mapping through the Source field on the Field layout:

Processing Field Name Field Type Description

Container Extension Fixed-Length Text Document extension of the container file in which the document originated.

Container ID Fixed-Length Text Unique identifier of the container file in which the document originated. This is used to identify or group files that came from the same container.

Container Name Fixed-Length Text Name of the container file in which the document originated.

Control Number Fixed-Length Text The identifier of the document.

Custodian Single Object Custodian associated with, or assigned to, the processing set during processing.

Extracted Text Long Text Complete text extracted from content of electronic files or OCR data field. This field holds the hidden comments of MS Office files.

Last Published On Date Date on which the document was last updated via re-publish.

Level Whole Number Numeric value indicating how deeply nested the document is within the family. The higher the number, the deeper the document is nested.

Originating Processing Set Single Object The processing set in which the document was processed.

Originating Processing Data Source Single Object A single object field that refers to the processing data source.

Processing File ID Fixed-Length Text Unique identifier of the document in the processing engine database.

Processing Folder Path Long Text The folder structure and path to the file from the original location, which is used to generate the Relativity folder browser for your documents. This field is populated every time you process documents. See Processing folder path details for more information.

Relativity Attachment ID Fixed-Length Text A system field that the Short Message Viewer uses to provide enhanced support for attachments and avatars. See the Relativity Short Message Format guide for more information.

Relativity Native Time Zone Offset Decimal

A numeric field that offsets how header dates and times appear in the viewer for processed emails. This field will be populated with the UTC offset value of the time zone chosen in the processing profile. For example, documents processed to Central Standard Time (CST), would be populated with a value of "-6" because CST is UTC-6. For more details on this field, see Relativity Native Time Zone Offset .

Time Zone Field Single Object Indicates which time zone is used to display dates and times on a document image.

Virtual Path Long Text Folder structure and path to file from the original location identified during processing. See Virtual path details for more information.

## Optional processing fields

The following, optional, metadata fields can be mapped through the Field Catalog. The Field Catalog contains a list of all available fields to map regardless of discovered data.

If you are setting up Processing prior to Discovery and Publish, you have the following options available in the Source field modal:

- Standard Fields—contains a collection of fields from both the Metadata Fields and Other Fields options.

- Metadata Fields—contains fields extracted from the actual file or file system.

- Other Fields—contains static, or Relativity system fields such as control number, processing set name, custodian, and so forth.

Please note:

- You can map one processing field to multiple Document object fields.

- You can only map a processing field to a Unicode-enabled field.

- The following metadata fields can be mapped to similar field types in the Field Catalog. To map different field types outside of the 135 metadata fields to one another, select All Fields from the drop-down menu in the Source field modal.

- Consider the following data compatible field types with valid mapping:

- You can map long text document fields to fixed-length text processing fields. However, Relativity does not support mapping fixed-length text document fields to long text processing fields.

- You can map single choice Catalog fields to destination fields of fixed-length text, long text, choice, or single object fields.

- You can map a DateTime field to a Date field if the source field is DateTime and the type of destination field is Date.

Processing field/

source name Field type Description Example value

All Custodians Multi Object

All custodians, deduped and master, associated with a file. The All Custodians field is mapped to a document and is updated only when Global or Custodial deduplication is enabled on the set and the field has been mapped, even if no duplicates exist for the document that was published in the workspace.

Lay, Kenneth; Doe, John

All Paths/Locations Long Text

This is the same as DeDuped Paths except that the virtual path of the current document is appended to the end of the list. The All Paths/Locations field is populated only when Global or Custodial deduplication is enabled on the set and the field has been mapped, even if no duplicates exist for the document that was published in the workspace.

Lay, Kenneth|\Lay, Kenneth\kenneth_lay_000_1_2_1.pst

\lay-k\Kenneth_Lay_Dec2000\Notes Folders\Notes inbox;

Doe, John|\Doe, John\John_Doe_000_1_2_1.pst

\Doe-J\John_Doe_Dec2000\Notes Folders\Discussion threads

Attachment Document IDs Long Text Attachment document IDs of all child items in family group, delimited by semicolon, only present on parent items. KL0000000031.0001;KL0000000031.0002

Attachment List Long Text Attachment file names of all child items in a family group, delimited by semicolon, only present on parent items. EC PRC Meeting Agenda.doc;Map to The St.Regis.doc

Author Fixed-Length Text (50) Original composer of document or sender of email message. This field has a maximum length of 50 alpha-numeric characters. Jane Doe

BCC Long Text The names, when available, and email addresses of the Blind Carbon Copy recipients of an email message. Capellas Michael D. [Michael.Capellas@COMPAQ.com]

BCC (SMTP Address) Long Text The full SMTP value for the email address entered as a recipient of the Blind Carbon Copy of an email message. Michael.Capellas@COMPAQ.com

CC Long Text The names, when available, and email addresses of the Carbon Copy recipients of an email message. Capellas Michael D. [Michael.Capellas@COMPAQ.com]

CC (SMTP Address) Long Text The full SMTP value for the email address entered as a recipient of the Carbon Copy of an email message. Michael.Capellas@COMPAQ.com

Child MD5 Hash Values Long Text

Attachment MD5 hash value of all child items in a family group, only present on parent items.

Relativity cannot calculate this value if you have FIPS (Federal Information Processing Standards cryptography) enabled for the worker manager server.

BA8F37866F59F269AE1D62D962B887B6;5DE7474

D13679D9388B75C95EE7780FE

Child SHA1 Hash Values Long Text Attachment SHA1 hash value of all child items in a family group, only present on parent items. 1989C1E539B5AE981820648623954872BEE3E483;

58D9E4B4A3068DA6E9BCDD969523288CF38F9FB3

Child SHA256 Hash Values Long Text Attachment SHA256 hash value of all child items in a family group, only present on parent items. 7848EEFC40C40F868929600BF033617642E0D37C2

F5FA444C7EF83350AE19883;628B6233DD6E0C89

F32D6EFF2885F26917F144B19F3678265BEBAC7

E9ACAAF5B

Comments Long Text Comments extracted from the metadata of the native file. For more information, see Comments considerations . Oracle 8i ODBC QueryFix Applied

Company Fixed-Length Text (255) The internal value entered for the company associated with a Microsoft Office document. This field has a maximum length of 255 alpha-numeric characters. Oracle Corporation

Contains Embedded Files Yes/No The yes/no indicator of whether a file such as a Microsoft Word document has additional files embedded in it. Yes

Control Number Beg Attach Fixed-Length Text (50) The identifier of the first document in a family group. This field is also populated for documents with no family members. This field has a maximum length of 50 alpha-numeric characters. KL0000000001

Control Number End Attach Fixed-Length Text (50) The identifier of the last document in a family group. This field is also populated for documents with no family members. This field has a maximum length of 50 alpha-numeric characters. KL0000000001.0002

Conversation Long Text Normalized subject of email messages. This is the subject line of the email after removing the RE and FW that are added by the system when emails are forwarded or replied to. Sigaba Secure Internet Communication

Conversation Family Fixed-Length Text (44) Relational field for conversation threads. This is a maximum 44-character string of numbers and letters that is created in the initial email. 01C9D1FD002240FB633CEC894C1985845049

B1886B67

Conversation Index Long Text Email thread created by the email system. This is a maximum 44-character string of numbers and letters that is created in the initial email and has 10 characters added for each reply or forward of an email. 01C9D1FD002240FB633CEC894C1985845049

B1886B67

Created Date Long Text The date on which a file was created. 12/24/2015

Created Date/Time Date

The date and time from the Date Created property extracted from the original file or email message.

This field will display the filesystem date created for the document if that's the only date created value available.

If a document has both a filesystem date created value and a document metadata date created value, this field will display the document metadata date created value.

"12/24/2015 11:59 PM"

Created Time Long Text The time at which a file was created. 11:59 PM

DeDuped Count Whole Number The number of duplicate files related to a master file. This is present only when Global or Custodial Deduplication is enabled and duplicates are present. If you discovered and published your set before Relativity Foxglove, you cannot map this field and re-publish the set. This is populated on the master document. You are not able to retroactively populate this field with custodian information. 2

DeDuped Custodians Multiple Object

The custodians associated with the de-duped records of a file. The DeDuped Custodians file is mapped to a document and is present only when Global or Custodial Deduplication is enabled and duplicates are present.

This is populated on the master document. You are not able to retroactively populate this field with custodian information.

The All Custodians field is mapped to a document and is updated only

Lay, Kenneth;Doe, John

DeDuped Paths Long Text

The virtual paths of duplicates of a file. This is present only when Global or Custodial Deduplication is enabled and duplicates are present. Each path contains the associated custodian.

This is populated on the master document. You are not able to retroactively populate this field with path information.

Lay, Kenneth|\Lay, Kenneth\kenneth_lay_000_1_2_1.pst

\lay-k\Kenneth_Lay_Dec2000\Notes Folders\Notes inbox|

Doe, John|\Doe, John\John_Doe_000_1_2_1.pst\Doe-J

\John_Doe_Dec2000\Notes Folders\Discussion threads

Delivery Receipt Requested Yes/No Indicates whether a delivery receipt was requested for an email. No

Discover Errors on Child Documents Multiple Object Identifier of the file that contains the parent document on which the error occurred.

Document Subject Long Text Subject of the document extracted from the properties of the native file. RE: Our trip to Washington

Document Title Long Text The title of a non-email document. This is blank if there is no value available. Manual of Standard Procedures

Email Categories Long Text Categories assigned to an email message. Personal

Email Created Date/Time Date The date and time at which an email was created. "12/24/2015 11:59 PM"

Email Entry ID Long Text The unique Identifier of an email in an mail store. 000000005B77B2A7467F56468D820375BC3DC582

44002000

Email Folder Path Long Text The folder path in which a custodian stored an email. See Email folder path details for more information. Inbox\New Business

Email Format Single Choice The indicator of whether an email is HTML, Rich Text, or Plain Text. HTML

Email Has Attachments Yes/No The yes/no indicator of whether a parent document has attachments. This field applies to the parent document and not child (email) files or attachments. Yes

Email In Reply To ID Long Text The internal metadata value within an email for the reply-to ID. <F9B1A278195DF640A4CC6EC973DFF0C85FBBEDEB

@Prod-EX-MB-01.company.corp>

Email Last Modified Date/Time Date The date and time at which an email was last modified. "12/24/2015 11:59 PM"

Email Modified Flag Yes/No The yes/no indicator of whether an email was modified. Yes

Email Sensitivity Single Choice The indicator of the privacy level of an email. Company Confidential

Email Sent Flag Yes/No The yes/no indicator of whether an email was sent, versus saved as a draft. Yes

Email Store Name Fixed-Length Text (255)

Any email, contact, appointment, or other data that is extracted from an email container, .pst, .ost, .nsf, .mbox, or any other, will have this field populated with the name of that email container.

Any children of those extracted emails, contacts, and appointments will not have anything populated in this field. For more information on this field, see Email Store Name details . This field has a maximum length of 255 alpha-numeric characters.

kenneth_lay_000_1_1_1_1.pst

Email Unread Yes/No The yes/no indicator of whether an email was not read. Yes

Error Category Single Choice The category assigned by the system to a processing error.>

This field was introduced in Server 2022. Password Protected Container

Error Message Long Text The message that details the error, cause, and suggested resolution of the error prioritized by processing phase—discovery, text extraction, publish, file deletion.

This field was introduced in Server 2022. There was an error during extraction of an email from this Notes container. It may be password protected. Consider adding the User.ID file and password(s) to Password Bank and retrying.

Error Phase Single Choice The phase of processing in which the error occurred—discovery, text extraction, publish, file deletion.

This field was introduced in Server 2022. Discovery

Error Status Single Choice The status of the error—undetermined, ready to retry, retried, submitted, unresolvable.

This field was introduced in Server 2022. Ready to retry.

Excel Hidden Columns Yes/No The yes/no indicator of whether an Excel file contains one or more hidden columns. No

Excel Hidden Rows Yes/No The yes/no indicator of whether an Excel file contains one or more hidden rows. Yes

Excel Hidden Worksheets Yes/No The yes/no indicator of whether an Excel file contains one or more hidden worksheets. No

Excel Pivot Tables Yes/No The yes/no indicator of whether an Excel file contains pivot tables. Yes

Extracted Text Size in KB Decimal This field indicates the size of the extracted text field in kilobytes.

27 KB

Family Group (formerly "Group Identifier") Fixed-Length Text (40) Group the file belongs to, used to identify the group if attachment fields are not used. This field has a maximum length of 40 alpha-numeric characters. KL0000000002

File Extension Fixed-Length Text (25)

The extension of the file, as assigned by the processing engine after it reads the header information from the original file. This may differ from the value for the Original File Extension field.

If you publish processing sets without mapping the File Extension processing field, the Text Extraction report does not accurately report document counts by file type. This field has a maximum length of 25 alpha-numeric characters.

MSG

File Name Fixed-Length Text (255) The original name of the file. This field has a maximum length of 255 alpha-numeric characters. enron corp budget.xls

File Size Decimal Generally a decimal number indicating the size in bytes of a file. 15896

File Type Fixed-Length Text (255) Description that represents the file type to the Windows Operating System. Examples are Adobe Portable Document Format, Microsoft Word 97 - 2003 Document, or Microsoft Office Word Open XML Format. This field has a maximum length of 255 alpha-numeric characters. Microsoft Excel 97-2003 Worksheet

From Fixed-Length Text (255) The name, when available, and email address of the sender of an email message. This field has a maximum length of 255 alpha-numeric characters. Capellas Michael D. [Michael.Capellas@COMPAQ.com]

From (SMTP Address) Fixed-Length Text (255) The full SMTP value for the sender of an email message. This field has a maximum length of 255 alpha-numeric characters. Michael.Capellas@COMPAQ.com

Has Hidden Data Yes/No

Indication of the existence of hidden document data such as hidden text in a Word document, hidden columns, rows, or worksheets in Excel, or slide notes in PowerPoint.

If a document contains hidden data that was found during processing, this field displays a value of Yes. If no hidden data was found, this field is blank. Note that this field does not display a value of No if no hidden data was found.

This is because Relativity cannot definitively state that a document contained no hidden data just because the system could not detect it.

Yes

Has OCR Text Yes/No The yes/no indicator of whether the extracted text field contains OCR text. Yes

Image Taken Date/Time Date The date and time at which an original image, such as a document scan or .jpg, was taken. "12/24/2015 11:59 PM"

Importance Single Choice Notation created for email messages to note a higher level of importance than other email messages added by the email originator. Low

Is Embedded Yes/No The yes/no indicator of whether a file is embedded in a Microsoft Office document. No

Is Parent Yes/No The yes/no indicator of whether a file is a parent with children or a child/loose record with no children. If this reads Yes, it is a top-level parent with children. If this reads No, it is an attachment or a loose record such as a standalone email or an Edoc. No

Keywords Long Text The internal value entered for keywords associated with a Microsoft Office document. Enron, Security Agreement

Last Accessed Date Long Text The date on which a loose file was last accessed. 12/24/2015

Last Accessed Date/Time Date The date and time at which the loose file was last accessed. "12/24/2015 11:59 PM"

Last Accessed Time Long Text The time at which the loose file was last accessed. 11:59 PM

Last Modified Date Long text The date on which changes to a file were last saved. 12/24/2015

Last Modified Date/Time Date The date and time at which changes to a file were last saved. "12/24/2015 11:59 PM"

Last Modified Time Long Text The time at which changes to a file were last saved. 11:59 PM

Last Printed Date Long Text The date on which a file was last printed. 12/24/2015

Last Printed Date/Time Date The date and time at which a file was last printed. "12/24/2015 11:59 PM"

Last Printed Time Long Text The time at which a file was last printed. 11:59 PM

Last Saved By Fixed-Length Text (255) The internal value indicating the last user to save a document. This field has a maximum length of 255 alpha-numeric characters. ymendez

Last Saved Date Long Text The date on which a file was last saved. 12/24/2015

Last Saved Date/Time Date The internal value entered for the date and time at which a document was last saved. "12/24/2015 11:59 PM"

Last Saved Time Long Text The time at which a file was last saved. 11:59 PM

Lotus Notes Other Folders Long Text A semi-colon-delimited listing of all folders that a Lotus Notes message or document appeared in, except for the one indicated in the Email Folder Path. For example: (Mail Threads);($All);($Drafts) (Mail Threads);($All);($Drafts)

MD5 Hash Fixed-Length Text (40)

Identifying value of an electronic record that can be used for deduplication and authentication generated using the MD5 hash algorithm.

Relativity cannot calculate this value if you have FIPS (Federal Information Processing Standards cryptography) enabled for the worker manager server. This field has a maximum length of 40 alpha-numeric characters.

21A74B494A1BFC2FE217CC274980E915

MS Office Document Manager Fixed-Length Text (255) The internal value entered for the manager of a document. This field has a maximum length of 255 alpha-numeric characters. Fabienne Chanavat

MS Office Revision Number Fixed-Length Text (255) The internal value for the revision number within a Microsoft Office file. This field has a maximum length of 255 alpha-numeric characters. 72

Media Type Single Choice A standard identifier used on the Internet to indicate the type of data that a file contains. application/msword

Meeting End Date Long Text The date on which a meeting item in Outlook or Lotus Notes ended. 12/24/2015

Meeting End Date/Time Date The date and time at which a meeting item in Outlook or Lotus Notes ended. "12/24/2015 11:59 PM"

Meeting End Time Long Text The time at which a meeting item in Outlook or Lotus Notes ended. 11:59 PM

Meeting Start Date Long Text The date on which a meeting item in Outlook or Lotus Notes started. 12/24/2015

Meeting Start Date/Time Date The date and time at which a meeting item in Outlook or Lotus Notes began. "12/24/2015 11:59 PM"

Meeting Start Time Long Text The time at which a meeting item in Outlook or Lotus Notes started. 11:59 PM

Message Class Single Choice The type of item from an email client—email, contact, calendar, and others. IPM.Note

Message Header Long Text The full string of values contained in an email message header. date: Wed, 4 Oct 2000 18:45:00 -0700 (PDT) Wed, 4

Oct 2000 18:45:00 -0700 (PDT) Message-ID: MIME-Version:

1.0 Content-Type: text/plain; charset="us-ascii"

Content-Transfer-Encoding: 7bit from: "Rosalee Fleming"

to: "Telle Michael S." subject: Re: Referendum Campaign

filename: klay.nsf folder: \Kenneth_Lay_Dec2000\Notes

Folders\'sent

Message ID Fixed-Length Text (255) The message number created by an email application and extracted from the email’s metadata. For more information, see Message ID considerations . This field has a maximum length of 255 alpha-numeric characters. <PLSRGLMRNQWEDFYPJL5ZJFF41USDEIQHB

@zlsvr22>

Message Type Single Choice Indicates the email system message type. Possible values include Appointment, Contact, Distribution List, Delivery Report, Message, or Task. The value may be appended with '(Encrypted)' or 'Digitally Signed' where appropriate. Message

Native File Long text The path to a copy of a file for loading into Relativity. \\files2.T026.ctus014128.r1.company.com\T026\Files\

EDDS2544753\Processing\1218799\INV2544753\

SOURCE\0\982.MSG

Number of Attachments Whole Number Number of files attached to a parent document. 2

Original Author Name Fixed-Length Text (50) The display name of the original author of an email. This field has a maximum length of 50 alpha-numeric characters. Jane Doe

Original Email Author Fixed-Length Text (255) The email address of the original author of an email. This field has a maximum length of 255 alpha-numeric characters. Jane.Doe@COMPAQ.com

Original File Extension Fixed-Length Text (25) The original extension of the file. This may differ from the value for the File Extension field, since that value is assigned based on the processing engine’s reading of the file’s header information. This field has a maximum length of 25 alpha-numeric characters. DOC

Other Metadata Long Text

Metadata extracted during processing for additional fields beyond the list of processing fields available for mapping. This includes TrackChanges, HiddenText, HasOCR, and dates of calendar items.

Field names and their corresponding values are delimited by a semicolon.

Excel/HasHiddenColumns=True;Office/Application=

Microsoft Excel;InternalCreatedOn=7/25/1997

9:14:12 PM;

Office/Security=2;Office/PROPID_23=528490;Office/

Scale=0;Office/

LinksDirty=0;Office/PROPID_19=0;Office

/PROPID_22=0;

Office/Parts=sum,ENRON;

Office/Headings=

Worksheets,2;Office/_PID_GUID=Unknown

PROPVARIANT type 65;

Excel/HasHiddenRows=True;

LiteralFileExtension=XLS

Outlook Flag Status Single Choice Indicates if an Outlook item is flagged. The field is blank if the item is not flagged. Flagged

Parent Document ID Fixed-Length Text Document ID of the parent document. This field is only available on child items.

KL0000000031.0001

Password Protected Single Choice Indicates the documents that were password protected. It contains the value Decrypted if the password was identified, Encrypted if the password was not identified, or no value if the file was not password protected. Encrypted

PowerPoint Hidden Slides Yes/No The yes/no indicator of whether a PowerPoint file contains hidden slides. Yes

Primary Date/Time Date

Date taken from Sent Date, Received Date, or Last Modified Date in the order of precedence.

"12/24/2015 11:59 PM"

Processing Errors Multiple Object Associated errors that occurred on the document during processing. This field is a link to the associated Processing Errors record.

Read Receipt Requested Yes/No Indicates whether a read receipt was requested for an email. Yes

Received Date Long Text The date on which an email message was received. 12/24/2015

Received Date/Time Date The date and time at which an email message was received. "12/24/2015 11:59 PM"

Received Time Long Text The time at which an email message was received. 11:59 PM

Recipient Count Whole Number The total count of recipients in an email which includes the To, CC, and BCC fields. 1

Recipient Domains (BCC) Multiple Object

The domains of the 'Blind Carbon Copy' recipients of an email. For information on domains and steps to create the Domains object and associative multi-object fields, see Relativity Objects .

The Domains processing fields listed in this table eliminate the need to perform domain parsing using transform sets for the processed documents.

enron.com;bellatlantic.com

Recipient Domains (CC) Multiple Object

The domains of the 'Carbon Copy' recipients of an email. For information on domains and steps to create the Domains object and associative multi-object fields, see Relativity Objects .

The Domains processing fields listed in this table eliminate the need to perform domain parsing using transform sets for the processed documents.

enron.com;bellatlantic.com

Recipient Domains (To) Multiple Object

The domains of the 'To' recipients of an email. For information on domains and steps to create the Domains object and associative multi-object fields, see Relativity Objects .

The Domains processing fields listed in this table eliminate the need to perform domain parsing using transform sets for the processed documents.

enron.com;bellatlantic.com

Recipient Name (To) Long text The names of the recipients of an email message. Jane Doe

Record Type Single Choice The single choice field that indicates that the file is an Email, Edoc, or Attach. Edoc

*You will not see RSMF fields in the catalog until you discover them. Any discovered RSMF fields are then available for mapping.

*RSMF Application Long Text This is used to identify source of the data, which is intended to be ambiguous. For example, it could be the application of the data contained in the RSMF file. Slack

*RSMF Attachment Count Whole Number This field should be a number that is a sum of all of the attachments present in the RSMF. 10

*RSMF Custodian Long Text This field is used to identify from whom the data was collected from. John Doe

*RSMF Event Collection Id Long Text This field should be a unique ID that is to be used to help keep many RSMFs from a single conversation together. D4C4EB398980E82B4B3064

*RSMF Generator Long Text Identifies the author of the RSMF file. Relativity v2.4

*RSMF Participants Long Text This field can be used to choose from a string of names (comma delimited) that are present in the conversation in the RSMF file. Relativity discovers the RSMF Participants field type as Multiple Choice. To maximize performance, map this field as Long Text.

John Doe <john.doe@relativity.com>, Jane Doe <jane.doe@relativity.com>

*RSMF Version Long Text The version of the RSMF specification that the file adheres to. 2.0.0

SHA1 Hash Fixed-Length Text (50) Identifying value of an electronic record that can be used for deduplication and authentication generated using the SHA1 hash algorithm. This field has a maximum length of 50 alpha-numeric characters. D4C4EB398980E82B4B3064CC2005F04D04BBAAE6

SHA256 Hash Fixed-Length Text (70) Identifying value of an electronic record that can be used for deduplication and authentication generated using the SHA256 hash algorithm. This field has a maximum length of 70 alpha-numeric characters. 4F8CA841731A4A6F78B919806335C963EE039F33

214A041F0B403F3D156938BC

Sender Domain Multiple Object The domain of the sender of an email. enron.com

Sender Name Fixed-Length Text (255) The name of the sender of an email message. This field has a maximum length of 255 alpha-numeric characters. Kenneth Lay

Sent Date Long text The date on which an email message was sent. 12/24/2015

Sent Date/Time Date The date and time at which an email message was sent. "12/24/2015 11:59 PM"

Sent Time Long Text The time at which an email message was sent. 11:59 PM

Sort Date/Time Date

For parent documents, the field is populated with the Primary Date/Time value. For child documents, the field is populated with the Sort Date/Time of the parent document. All documents in a family will therefore have the same Sort Date/Time value, keeping family members together when sorting on this field.

When processing documents without an actual date, Relativity provides a null value for the following fields: Created Date, Created Date/Time, Created Time, Last Accessed Date, Last Accessed Date/Time, Last Accessed Time, Last Modified Date, Last Modified Date/Time, Last Modified Time, and Primary Date/Time. The null value is excluded and not represented in the filtered list.

"12/24/2015 11:59 PM"

Source Path Long Text

The folder structure and path to the file from the original location identified during processing. For emails, this displays the subject rather than

the email's entry ID. This provides you with better context of the origin of the email.

Previously, the Virtual Path field displayed the entry ID with the email file name, and if you followed this virtual path, it was difficult to tell by that entry ID where the email came from. See Source path details for more information.

Reports\User\ Sample.pst\Inbox\

Requested February report

Speaker Notes Yes/No The yes/no indicator of whether a PowerPoint file has speaker notes associated with its slides. Yes

Subject Long Text The subject of the email message. Blackmore Report - August

Suspect File Extension Yes/No The yes/no indicator if whether the extension of a file does not correspond to the actual type of the file. For example, XLS for a Word document. Yes

Text Extraction Method Single Choice The method used to run text extraction. Excel

Title Long Text The title of the file. For emails, this is the subject line. For non-emails, this is any available title. June Scrum Notes

To Long Text The names, when available and email addresses of the recipients of an email message. Capellas Michael D. [Michael.Capellas@COMPAQ.com]

To (SMTP Address) Long Text The full SMTP value for the recipient of an email message, for example, “bob@example.com.” Michael.Capellas@COMPAQ.com

TrackChanges Yes/No

The yes/no indicator of whether the track changes metadata on an Office document is set to True. This does not necessarily indicate if tracked changes were made to the document or not.

- On Word documents, the track changes toggle may have been set to True, changes made to the document, then set back to False. In this situation, this field will still indicate ‘No’ because it is looking only at the setting and not for the actual existence of changes even though tracked changes still exist in the document.

- If the same situation is applied to Excel documents, the result is slightly different. Microsoft deletes tracked changes on Excel documents when the toggle is set back to False. The returned value will also indicate ‘No’ but there is no concern about missed tracked changes as none exist.

- For file types that cannot contain tracked changes, such as PDFs, email, and images, this field is blank.

Yes

Track Changes Yes/No

The yes/no indicator of whether the track changes toggle is set to True and/or there are tracked changes in the document.

This field maps to the TrackedChangesCombined Invariant field. This will be Yes if either of the following are true:

-

The Track Changes button is enabled in the document.

-

There is actual Tracked Change content in the document.

Unified Title Long Text The subject of the file. For emails, this is the subject line. For non-emails, this is the file name. Note that in short message (RSMF) conversion, Relativity may use the conversation name as the subject, and therefore the Unified Title.

Company Memo

Unprocessable Yes/No

The yes/no value indicating if a file was able to be processed. If the file could not be processed, this field is set to Yes.

- Even if a file is flagged as Unprocessable, it may still be visible in the native file viewer if Oracle is able to render the file.

- The Unprocessable field is set to Yes on any file for which Relativity does not have an Invariant plugin that is capable of extracting text or imaging/OCRing that document type. For example, it’s not set for a corrupt file for which we cannot extract text, such as a corrupt Word document that logs an error during data extraction.

- Unprocessable documents do not have errors associated with them because they never reach a point at which they can register a processing error.

No

Extracted Text Size in KB is also an available mappable field outside of the Field Catalog. This field was introduced in Relativity 9.4, and it indicates the size of the extracted text field in kilobytes. To map this field, you can edit the corresponding Relativity field, open the Field Catalog via the Source field, select the All Fields view, and select Extracted Text Size in KB as the Source value.

You can track which passwords successfully decrypted published documents by mapping the Password field found in the All Fields view. Specifically, you can find this Password field by clicking Source on the field layout, selecting the All Fields view, and locating the source field name of Password with a field type of Long Text.

## Email Store Name details

To better understanding how the Email Store Name field works, consider the following examples:

- When an email comes from .pst, the .pst is listed in the Email Store Name field. When a child Word document comes from a .rar archive and is attached to the email, the Email Store Name field is blank for the Word document.

- The RAR/ZIP information for the Word documents mentioned above is found in the Container Name field.

- In the following example, email 00011 comes from a .pst file named PSTContainingEmbeddedPSTInFolders.pst, which is the value for the Email Store Name field for that email. The other emails, 00011.001 and 00011.002, come from a .pst file attached to the 00011 email. This .pst file is named PSTWithEmails.pst. In this case, the Email Store Name field for those child messages is PSTWithEmails.pst, not the top-level .pst named PSTContainingEmbeddedPSTInFolders.pst.

- For an email taken from a zip folder, the Email Store Name field is blank.

## Virtual path details

The virtual path is the complete folder structure and path from the original folder or file chosen for processing to the file. This path includes any containers that the file may be in and, in the case of attached or embedded items, includes the file name of the parent document.

This path does not include the name of the file itself. If a file is selected for import instead of a folder, the virtual path for that file is blank.

The following are examples of virtual paths created from the folders, per the above images:

- \Maude Lebowski\Loose Docs

- \Walter Sobchak\Walter.pst\Inbox\Unimportant\Fest Junk\Walter

- test.pst\My Test Box

- In the case of a container or loose file being directly selected for processing, the virtual path does not have a leading backslash.

- test.pst\My Test Box\000000009B90A00DCC4229468A243C71810F71BC24002000.MSG

- Revisions.doc

- This is the virtual path of a file embedded in the Revisions.doc file.

## Processing folder path details

The processing folder path is the folder structure created in the folder browser of the Documents tab. Relativity creates this path by keeping any folders or container names in the virtual path and discarding any file names that a file may be attached to or embedded in.

Files without a virtual path and items embedded within them do not have a processing folder path. If a container is embedded in a loose file, the items in that container have a processing folder path that matches the name of the container.

The following are examples of virtual paths and corresponding processing folder paths.

Virtual Path Processing Folder Path

```text
test.pst\Inbox
```

```text
test.pst\Inbox
```

```text
test.pst\Inbox\000000009B90A00DCC4229468A243C71810F71BC24002000.MSG
```

```text
test.pst\Inbox
```

test.pst\Inbox\000000009B90A00DCC4229468A243C71810F71BC24002000.MSG\Pics.zip

test.pst\Inbox\Pics.zip

## Email folder path details

The email folder path is the folder path within the email container file in which an email was stored. All attachments to emails have no value for this field.

For example, an email stored in the ‘Escalations’ folder in the following image below would have a value of “Inbox\Tickets\Escalations."

## Source path details

The source path is a modified display of the virtual path. In the case of attachments to emails, any entry IDs of emails appearing in the virtual path are replaced by the subject of that email instead. In all other cases the source path value is identical to the virtual path.

For example, an attachment to an email could have the following virtual path and source path values:

Virtual Path Source Path

```text
Sample.pst\Inbox\000000009B90A00DCC4229468A243C71810F71BC24002000.MSG
```

Sample.pst\Inbox\Requested February reports

This source path field is not to be confused with the Source Path field found on the Processing Data Source layout on the saved processing set.

## Message ID considerations

Note the following details regarding the Message ID field:

- Message ID is an identifier applied to an email by the program that created the email, such as Outlook, Eudora, and more.

- Email programs can use whatever they want for a message ID, or they can leave it off entirely. The mail server is free to assign an identifier even if an email client did not.

- There is no guarantee that every message ID is unique because every email client and mail server uses a different algorithm to create one.

- Message ID is unique only in the fact Relativity does not know what tool generated the identifier or what algorithm generated it. In addition, Relativity cannot assume that the identifier will even exist in an email.

- Relativity cannot validate the message ID because it is made up of opaque data associated with an email.

- It is possible that two entirely different emails might share the same message ID.

- Using the Message ID is not a reliable alternative to SHA256 deduplication. For the purposes of deduplication, we recommend that you use the Processing Duplicate Hash. If you processed the information in another tool, it is recommended that you use the Hash Algorithm you selected in that tool.

## Comments considerations

There are two kinds of comments that are possible in all Office documents: metadata and inline. The following table breaks down which optional processing fields are populated by each type of comment.

Comment type Location in file Hidden Data value Comments value

Metadata Details tab of the Properties window, when you right-click on file name Null (blank) Contents of comments property on the file

Inline In the body of the document "Yes" Null (blank)

Both Details tab of file and body of document "Yes" Contents of comments property on the file

There are a number of reasons why a document could contain hidden text. A returned value of Yes for the Hidden Data field does not automatically mean that the document has inline comments.

## Deduped custodian and path considerations

If you run deduplication as part of your processing job, you may want to know where the documents that eventually get de-duplicated came from, the path, as well as which custodian those documents were associated with.

The DeDuped Custodians and DeDuped Paths optional fields allow you to track this information. When a document is de-duplicated, these fields are populated upon publish, or republish.

- DeDuped Custodians —a multi-object field with object type Document and associated object type Entity. You should only associate this field with the Entity object. If this field is associated with any other object type, you will not be able to publish documents to your workspace.

- DeDuped Paths —a long text document field that provides the location of the deduplicated document.

To use these fields, simply add them to a document view and refer to that view after your publish job has completed. You can then export the results to an Excel file, if necessary.

When Relativity populates the Deduped Custodians and Deduped Paths fields during republish, it performs an overlay. Because of this, if you modify a document's identifier field in Relativity, your information could become out of sync. For this reason, we recommend that you do not modify the identifier field.

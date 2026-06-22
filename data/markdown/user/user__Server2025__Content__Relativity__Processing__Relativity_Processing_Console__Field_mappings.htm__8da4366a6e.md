---
title: "Field mappings"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Relativity_Processing_Console/Field_mappings.htm
collection: user
fetched_at: 2026-06-22T06:13:59+00:00
sha256: 9473bbed17419a709a286494cab7b26991848694e27f5f36d5d8cf87c8ff22da
---

Field mappings

# Field mappings

The following table provides a breakdown of which processing fields match up with the most common fields in the RPC.

Processing Relativity field/source name RPC field name Field type Is Unicode? Description

Attachment Document IDs ChildRelativityControlNumbers Long Text Yes Attachment document IDs of all child items in family group, delimited by semicolon, only present on parent items.

Attachment List ChildFileNames Long Text Yes Attachment file names of all child items in a family group, delimited by semicolon, only present on parent items.

Author Author Fixed-Length Text (50) Yes Original composer of document or sender of email message.

BCC Address EmailBCCSmtp Long Text Yes The full SMTP value for the email address entered as a recipient of the Blind Carbon Copy of an email message.

CC Address EmailCCSmtp Long Text Yes The full SMTP value for the email address entered as a recipient of the Carbon Copy of an email message.

Child MD5 Hash Values ChildMD5Hashes Long Text Yes Attachment MD5 Hash values of all child items in a family group, delimited by semicolon, only present on parent items. The RPC can't calculate this value if you have FIPS (Federal Information Processing Standards cryptography) enabled for the worker manager server.

Child SHA1 Hash Values ChildSHA1Hashes Long Text Yes Attachment SHA1 Hash values of all child items in a family group, delimited by semicolon, only present on parent items.

Child SHA256 Hash Values ChildSHA256Hashes Long Text Yes Attachment SHA256 Hash values of all child items in a family group, delimited by semicolon, only present on parent items.

Comments Comments Long Text Yes Comments extracted from the metadata of the native file.

Company Company Fixed-Length Text (255) Yes The internal value entered for the company associated with a Microsoft Office document.

Contains Embedded Files Office/EmbeddedItems Yes/No N/A The yes/no indicator of whether a file such as a Microsoft Word document has additional files embedded in it.

Control Number Beg Attach BatesBeginAttach Fixed-Length Text (50) Yes The identifier of the first page of the first document in a family group. This is used for page-level numbering schemes.

Control Number End Attach BatesEndAttach Fixed-Length Text (50) Yes The identifier of the last page of the first document in a family group. This is used for page-level numbering schemes.

Conversation EmailConversation Long Text Yes Normalized subject of email messages. This is the subject line of the email after removing the RE and FW that are added by the system when emails are forwarded or replied to.

Conversation Family ConversationFamily Fixed-Length Text (44) Yes Relational field for conversation threads. This is a 44-character string of numbers and letters that is created in the initial email.

Conversation Index EmailConversationIndex Long Text Yes Email thread created by the email system. This is a 44-character string of numbers and letters that is created in the initial email and has 10 characters added for each reply or forward of an email.

Date Created CreatedOn Date N/A Date and time from the Date Created property extracted from the original file or email message.

Date Last Modified LastModified Date N/A Date and time from the Modified property of a document, representing the date and time that changes to the document were last saved.

Date Last Printed LastPrinted Date N/A Date and time that the document was last printed.

Date Received EmailReceivedOn Date N/A Date and time that the email message was received (according to original time zones).

Date Sent EmailSentOn Date N/A Date and time that the email message was sent (according to original time zones).

DeDuped Custodians DeDupedCustodians Multiple Object N/A Custodians associated with the de-duped records of this document.

DeDuped Paths DeDupedPaths Long Text Yes Folder structure and paths to this document?s duplicates. Each path will contain the associated custodian.

Delivery Receipt EmailDeliveryReceiptRequested Yes/No N/A The yes/no indicator of whether a delivery receipt was requested for an e-mail.

Document Class RelativityDocumentClass Single Choice N/A A single choice field that can be one of: Email, Edoc, or Attach.

Document Extension FileExtension Fixed-Length Text (25) Yes Three (or more) character extension of the document that represents the file type to the Windows Operating System. Examples are PDF, DOC, or DOCX.

Document Subject DocumentSubject Long Text Yes Subject of the document extracted from the properties of the native file.

Domains (Email BCC) Email/DomainParsedBCC Multiple Object N/A Domains of 'Blind Carbon Copy' recipients of the email message.

Domains (Email CC) Email/DomainParsedCC Multiple Object N/A Domains of 'Carbon Copy' recipients of the email message.

Domains (Email From) Email/DomainParsedFrom Multiple Object N/A Domains of Originator of the email message.

Domains (Email To) Email/DomainParsedTo Multiple Object N/A Domains of 'To' recipients of the email message.

Email BCC EmailDisplayBCC Long Text Yes Recipients of 'Blind Carbon Copies' of the email message.

Email Categories EmailKeywords Long Text Yes Category assigned to an email message.

Email CC EmailDisplayCC Long Text Yes Recipients of 'Carbon Copies' of the email message.

Email From EmailDisplaySender Fixed-Length Text (255) Yes Originator of the email message.

Email In Reply To ID Email/In_Reply_To Long Text Yes The internal metadata value within an email for the reply to ID.

Email Store Name EmailContainer Fixed-Length Text (255) Yes The identifier of the top-level container of an email message. For example, 'jdoe.nsf.' If a document comes from a rar/zip file attached to the email, the container is referred to in that file.

Email Subject EmailSubject Long Text Yes Subject of the email message.

Email To EmailDisplayTo Long Text Yes List of recipients or addressees of the email message.

File Name FileName Fixed-Length Text (25) Yes Original name of the file.

File Size FileSize Decimal N/A Generally a decimal number indicating the size in bytes of a file.

File Type FileType Fixed-Length Text (255) Yes Description that represents the file type to the Windows Operating System. Examples are Adobe Portable Document Format, Microsoft Word 97 - 2003 Document, or Microsoft Office Word Open XML Format.

From Address EmailSenderSmtp Long Text Yes The full SMTP value for the sender of an email message.

Group Identifier RelativityGroupId Fixed-Length Text (40) Yes Group the file belongs to (used to identify the group if attachment fields are not used).

Has Hidden Data HiddenText Yes/No N/A Indication of the existence of hidden document data such as hidden text in a Word document, hidden columns, rows, or worksheets in Excel, or slide notes in PowerPoint.

Importance EmailImportance Single Choice N/A Notation created for email messages to note a higher level of importance than other email messages added by the email originator.

Keywords Office/Keywords Long Text The internal value entered for keywords associated with a Microsoft Office document.

Last Accessed Date/Time LastAccessed Date N/A The date and time at which the loose file was last accessed.

Last Saved By Office/LastAuthor Fixed-Length Text (255) Yes The internal value indicating the last user to save a document.

Last Saved Date/Time LastSaved Date N/A The internal value entered for the date and time at which a document was last saved.

Lotus Notes Other Folders Lotus/OtherFolders Long Text Yes A semi-colon delimited listing of all non-primary folders that a Lotus Notes message or document was included.

MD5 Hash MD5Hash Fixed-Length Text (40) Yes Identifying value of an electronic record that can be used for deduplication and authentication generated using the MD5 hash algorithm.

Meeting End Date/Time Email/EndDate Date N/A The date and time at which a meeting item in Outlook or Lotus Notes ended.

Meeting Start Date/Time Email/StartDate Date N/A The date and time at which a meeting item in Outlook or Lotus Notes began.

Message Header Email/MessageHeader Long Text Yes The full string of values contained in an email message header.

Message ID EmailMessageID Fixed-Length Text (255) The message number created by an email application and extracted from the email's metadata.

Message Type Email/MessageType Single Choice N/A An indication of the email system message type. Possible values include Appointment, Contact, Distribution List, Delivery Report, Message, or Task. The value may be appended with '(Encrypted)' or 'Digitally Signed' where appropriate.

Native File StoredAs Long Text Yes The path to a copy of a file for loading into Relativity.

Number of Attachments AttachmentCount Whole Number N/A Number of files attached to a parent document.

OCR Text HasOcrText Yes/No N/A The yes/no indicator of whether the extracted text field contains OCR text.

Office Document Manager Office/Manager Fixed-Length Text (255) Yes The internal value entered for the manager of a document.

Office Revision Number Office/Revision Fixed-Length Text (255) Yes The internal value for the revision number within a Microsoft Office document.

Other Props OtherProps Long Text Yes Metadata extracted during processing for additional fields beyond the list of processing fields available for mapping. Field names and their corresponding values are delimited by semicolon.

Parent Document ID ParentRelativityControlNumber Fixed-Length Text (50) Yes Document ID of the parent document. This field will only be available on child items.

Password Protected PasswordProtected Single Choice N/A An indication of documents that were password protected. It will contain the value 'Decrypted' if the password was identified; 'Encrypted' if the password was not identified; or no value if the file was not password protected.

Primary Date DocDate Date N/A Date taken from Email Sent Date, Email Received Date, or Last Modified Date (in order of precedence).

Read Receipt EmailReadReceiptRequested Yes/No N/A The yes/no indicator of whether a read receipt was requested for an e-mail.

Sensitivity EmailSensitivity Single Choice N/A The indicator set on an email to denote the email's level of privacy.

SHA1 Hash SHA1Hash Fixed-Length Text (50) Yes Identifying value of an electronic record that can be used for deduplication and authentication generated using the SHA1 hash algorithm.

SHA256 Hash SHA256Hash Fixed-Length Text (70) Yes Identifying value of an electronic record that can be used for deduplication and authentication generated using the SHA256 hash algorithm.

Sort Date SortDate Date N/A Date taken from Email Sent Date, Email Received Date, or Last Modified Date (in order of precedence) repeated for parent document and all children items to allow for date sorting.

Speaker Notes PowerPoint/HasSpeakerNotes Yes/No N/A The yes/no indicator of whether a powerpoint file has speaker notes associated with its slides.

To Address EmailToSmtp Long Text Yes The full SMTP value for the recipient of an email message. For example, 'bob@example.com'

Track Changes TrackChanges Yes/No N/A The yes/no indicator of whether tracked changes exist in the document.

Unified Title UnifiedSubject Long Text Yes Subject of the document. If the document is an email, this field contains the email subject. If the document is not an email, this field contains the document's file name.

Unprocessable Unprocessable Yes/No N/A The yes/no value indicating if a file was able to be processed. If the file could not be processed, this field is set to Yes.

Unread Flag EmailIsUnread Yes/No N/A The yes/no indicator of whether an e-mail was not read.

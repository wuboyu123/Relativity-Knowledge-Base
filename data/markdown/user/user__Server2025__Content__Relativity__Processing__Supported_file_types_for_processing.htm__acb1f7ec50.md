---
title: "Supported file types for processing"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Supported_file_types_for_processing.htm
collection: user
fetched_at: 2026-06-22T06:02:28+00:00
sha256: 1139fb393994994744cfacd316fe6257aa5b63b6187374e10ca97f2f449a8c25
---

Supported file types for processing Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Supported file types for processing

Relativity supports many file types for processing. There are also some file types that are incompatible with the processing engine. Before processing your data, note what types are supported and unsupported, as well as any caveats involved with processing those file types.

Read if you are studying for the Processing Specialist exam The content on this site is based on the most recent monthly version of Relativity, which contains functionality that has been added since the release of the version on which Relativity's exams are based. As a result, some of the content on this site may differ significantly from questions you encounter in a practice quiz and on the exam itself. If you encounter any content on this site that contradicts your study materials, please refer to the What's New and/or the Release Notes for details on all new functionality.

This documentation contains references to third-party software, or technologies. While efforts are made to keep third-party references updated, the images, documentation, or guidance in this topic may not accurately represent the current behavior or user interfaces of the third-party software. For more considerations regarding third-party software, such as copyright and ownership, see Terms of Use .

Data pulled from supported versus unsupported file types: Relativity only pulls limited metadata from unsupported file types. Data pulled from supported file types includes metadata, text, and embedded items.

## Supported file types

The following file types and extensions are supported by Relativity for processing.

Renaming a file extension has little effect on how Relativity identifies the file type. When processing a file type, Relativity looks at the actual file properties, such as digital signature, regardless of the named extension. Relativity only uses the named extension as a tie-breaker if the actual file properties indicate multiple extensions.

File type Extensions

Adobe files .pdf, .fm, .ps, .eps

- Relativity performs Optical Character Recognition (OCR) on .pdf files during processing. Relativity handles a .pdf portfolio, which is an integrated .pdf unit containing multiple files, by extracting the metadata and associating it with the files contained in the portfolio.

AppleDouble AppleDouble-encoded attachments in e-mails.

CAD files .dxf, .dwg, .slddrw, .sldprt, .3dxml, .sldasm, .prtdot, .asmdot, .drwdot, .stl, . eprt, .easm, .edrw, .eprtx, .edrwx, .easmx

- For processing and imaging data sets containing CAD files, you can configure the timeout value in the AppSettings table. See AppSettings table . The OCR output for processed CAD files can vary significantly.

Compressed files .7z, .zip, .tar, .gz, .bz2, .rar, .z, .cab, .alzip

Zip file containers do not store time zone information for CreatedOn, LastModified, and LastAccessed fields. When extracting files, time stamps are only meaningful if the time zone that the zip file container was created in is known. Relativity extracts file metadata and updates the CreatedOn and LastModified fields if available. Otherwise, CreatedOn defaults to 1/1/1900 and LastModified reflects the worker local time zone. LastModified and LastAccessed fields will usually match.

Relativity does not support multi-part .zip, .tar, or .7z files.

Database files .dbf

- Relativity only supports .dbf 3 and .dbf 4 files.

- Relativity does not support the following database formats:

- VisualFoxPro

- VisualFoxPro autoincrement enabled

- Relativity uses Microsoft Excel to extract text from .dbf file types. For details on .dbf file type handling, see Excel file considerations .

Email .pst, .ost, .nsf, .msg, .p7m, .p7s, .ics, .vcf, .mbox, .eml, .emlx, .tnef, . dbx, Bloomberg Mail .xml

- Original electronic email data (.eml file types) are parsed and stored inside a personal storage table (.pst files.) If the email contains embedded electronic email data, the email data is also parsed and stored in the personal storage table. The processing engine reads tables, properties, and rows to construct an .msg (Outlook message item) file from a .pst file. The .msg file format supports all rich metadata inside an email in a personal storage table. The original electronic email data is not preserved.

- S/MIME-encrypted and digitally-signed emails are supported.

- Even though the .emlx file type is supported, the following partial .emlx file extensions are not supported:

- .emlxpart

- .partial.emlx

EnCase versions e01, .ex01, .l01, .lx01

- Processing supports .e01 and .ex01 files for the following operating and file systems:

- Windows—NTFS, FAT, ExFAT

- Mac—HFS+

- Linux (Ubuntu)- EXT2, EXT3, EXT4

- Deleted files that exist on an .e01 and .ex01 (disk) image file are skipped during processing, with the exception of recycle bin items, which are processed with limited metadata.

- Encrypted EnCase files are not supported. You must decrypt EnCase files prior to processing them.

- For details on .e01 file type handling, see Multi-part forensic file considerations .

Excel .xlsx, .xlsm, .xlsb, .xlam, .xltx, .xltm, .xls, .xlt, .xla, .xlm, .xlw, .uxdc

Excel version 2.0 through the current product version is supported. See Excel file considerations .

If you save a Powerpoint or Excel document in pre-2007 format, like .PPT or .XLS, and the document is read-only, we use the default known password to decrypt the document, regardless of whether or not the password exists in the Password Bank.

Hangul

.hwp

Hangul word processing files 1997 up to 2010 are supported.

HTML .html, .mht, .htm, .mhtml, .xhtm, .xhtml

Relativity extracts metadata and attachments from multipurpose internet mail (MIME) file formats such as .mht and .eml during processing.

Image files .jpg, .jpeg, .ico, .bmp, .gif, .tiff, .tif, .jng, .koala, .lbm, .pbm, .iff, .pcd, . pcx, .pgm, .ppm, .ras, .targa, .tga, .wbmp, .psd, .cut, .xbm, .dds, .fax, .sgi, .png, .exf, . exif, .webp, .wdp

JungUm Global .gul

OneNote .one

- Relativity uses Microsoft connectors to extract information from OneNote files at the section, or tab, level. All pages within a section are extracted as one file. During ingestion, Relativity extracts embedded items from OneNote files, and for some object types, generates them as .pdf or .tiff files natively.

- The Password Bank does not support OneNote files.

- Server 2024 does not support OneNote 2003 files.

OpenOffice .odc, .ods, .odt, .odp, .xps

PowerPoint .pptx, .pptm, .ppsx, .ppsm, .potx, .potm, .ppt, .pps, .pot

- PowerPoint 97 through the current product version is supported, including the dual-format 95/97 version.

- Modern comment are supported for Relativity Text Extraction.

If you save a Powerpoint or Excel document in pre-2007 format, like .PPT or .XLS, and the document is read-only, we use the default known password to decrypt the document, regardless of whether or not the password exists in the Password Bank.

Publisher .pub

Project .mpp, .mpt, .mpd, .mpx

The text extracted from Project files is from the Gantt chart view and includes Task Notes.

Short message .rsmf

- For details about Relativity Short Message Format metadata and mapping, see RSMF mapping considerations .

- For technical details, see Relativity short message format files .

Text files Such as .txt or .csv.

Processing supports any text file whose bytes are ASCII or Unicode text. Files are assumed to be in UTF8 if a Unicode BOM is not found. Files not in a Unicode format with characters outside the ASCII range may experience issues with text extraction.

Vector files .svg, .svgz, .wmf, .plt, .emf, .snp, .hpgl, .hpg, .plo, .prn, .emz, .wmz

Visio .vsd, .vdx, .vss, .vsx, .vst, .vsw, .vsdx, .vsdm

- Visio is a separate installation per the Worker Manager server page.

- Processing .vsdx and .vsdm files requires the Professional editions of Visio/Project in Office 2024.

Word .docx, .docm, .dotx, .dotm, .doc, .dot, .rtf

Word 2.0 through the current product version is supported, including templates.

WordPerfect .wpd, .wps

Relativity currently does not support the extraction of embedded images or objects from Visio, Project, or OpenOffice files. In addition, Relativity never extracts any embedded objects or images that were added to any files as links. For a detailed list of the Office file extensions from which Relativity does and does not extract embedded objects and images, see Microsoft Office child extraction support .

If you use the Native text extraction method on the profile, Processing does not handle pre-2008 Microsoft Office files that have the Protected view enabled. You must use the Relativity text extraction method to process these files.

### Excel file considerations

Due to Excel specifications and limits, when processing a database file with the native text extraction method, the database file may miss data in extracted text. For example, if a database file contains more than 1,048,576 rows and 16,384 columns, the extracted text of these files will not contain text on row 1,048,577 and onward and on column 16,385 and onward. For more information, see Excel specifications and limits on the Microsoft website.

### Multi-part forensic file considerations

When processing a multi-part forensic image, make sure the source location points to the root folder that contains all of the files that make up the image. If you select only the first file of the image, such as .e01, .l01, .ex01, .lx01, inventory and discovery will fail with an unrecoverable error.

This is because inventory looks at files where they reside in the processing source folder and does not copy them to the repository. If only the first file is selected, during discovery, that file only is copied to the repository, and the workers will attempt to extract from it and fail since the rest of the archive is not available.

When processing .e01 files, the following NTFS file system files are skipped:

- Unallocated space files

- Index $I30 files

- $TXF_DATE files

### Native text extraction and OCR

Processing distinguishes between text and line art in the documents you process. For these documents, processing will only OCR the line art. This means that Relativity does not skip OCR if a page has electronic text.

Accordingly, Relativity performs both native text extraction and OCR on the following file formats:

- All vector formats—.svg, CAD files, Metafiles [.wmf, .emf], Postscript, Encapsulated postscript

- .pdf, Visio, Publisher, MS Project, Hancom and JungUm files

All image formats, such as .tiff, .jpeg, .gif, .bmp, and .png, do not have native text, so only OCR is performed. If the file has electronic text and images, native text extraction and OCR is performed.

### Support for password-protected Roshal Archive files

Processing does not decrypt a file that gets its encryption directly from the .rar file that contains it. This means that if you attempt to process a password-protected .rar file where the Encrypt file names property is checked, Processing is unable to extract the files inside that archive.

In addition, Processing can extract a single password-protected file from a .rar file, but not multiple password-protected files in the same archive.

The following table breaks down Processing's support of password-protected .rar files.

- √ —Processing will decrypt the file.

- Empty—Processing will not decrypt the file.

Archive type Single password-protected file Multiple password-protected files Encrypt file names property

.rar √

Multi-part .rar √

### Outlook message item (.msg) to MIME encapsulation (.mht) conversion considerations

The following table provides details on the differences between how Relativity handles .msg and .mht file types. This information may be especially useful if you plan on setting the Email Output field on the processing profile to MIME encapsulation.

Category Field/attribute Outlook message item (.msg) MIME encapsultation (.mht)

Metadata fields Show Time As This field sometimes appears in the extracted text from MSG files when not explicitly stated in the message file itself. The default for a calendar invite is to show time as busy; the default for a cancellation is to show time as free. Show Time As does not appear in the extracted text if the default value is populated.

Metadata fields On behalf of This field is sometimes present in text from a message item. In some cases, this field is populated with the same value as the From field. On behalf of does not appear in the extracted text.

Interline spacing N/A

The expected number of blank lines appears in the extracted text. Line wrapping for long paragraphs will also be present.

In some cases, the text in the .mht file format has fewer blank lines than the text from a message item. In addition, there is no built-in line wrapping for long paragraphs.

Intraline spacing N/A

White-space characters are converted to standard space characters.

White-space characters may remain as non-breaking spaces.

Email addresses Email When a message file is converted to .mht, the text is extracted from the .mht file using OutsideIn. This can lead to a loss of data. If joe.smith@acme.com renders as Joe Smith in the .mht file, the email address is not captured in the extracted text.

### Email image extraction support

It is helpful to understand when Relativity treats an image that is attached to an email as an inline, or embedded, image and not as an actual attachment. The following table breaks down when this occurs based on email format and image characteristics:

Email format Attachments that are inline, embedded, images

Plain text None

Rich text IPicture-based OLE embedded images

HTML

- Images with content ID referenced in the HTML body

- Local, non-internet image references in the HTML that Relativity can match to an attachment

- .pst/.ost/.msg files containing metadata hints as to whether or not the image is marked hidden or is referenced in the HTML body

You can arrange for the discovery of inline images when creating Processing profiles , specifically through the field called When extracting children, do not extract .

### Microsoft Office child extraction support

See a breakdown of Relativity's support of Microsoft Office child extraction

The following table displays which Office file extensions will have their embedded objects and images extracted by Relativity and which will not.

- √ —Relativity fully extracts the embedded object and image.

- √* —Relativity partially extracts the embedded object or image.

- Empty—Relativity does not extract the embedded object or image.

Office program File extension Embedded object extraction Embedded image extraction

Excel .xlsx √ √

Excel .xlsm √ √

Excel .xlsb √ √

Excel .xlam √ √

Excel .xltx √ √

Excel .xltm √ √

Excel .xls √ √*

Excel .xlt √ √*

Excel .xla √ √*

Excel .xlm √ √*

Excel .xlw √ √*

Excel .uxdc

Outlook .msg √ √

Word .docx √ √

Word .docm √ √

Word .dotx √ √

Word .dotm √ √

Word .doc √ √*

Word .dot √ √*

Word .rtf √ √

Visio .vsd

Visio .vdx

Visio .vss

Visio .vsx

Visio .vst

Visio .vsw

Visio .vsdx √ √

Visio .vsdm √ √

Project .mpp

Publisher .pub √

PowerPoint .pptx √ √

PowerPoint .pptm √ √

PowerPoint .ppsx √ √

PowerPoint .ppsm √ √

PowerPoint .potx √ √

PowerPoint .ppt √ √

PowerPoint .pps √ √

PowerPoint .pot √ √

OneNote .one √

## Notable unsupported file types

Processing does not support files created with the following programs and versions:

Product category Product name and version

DOS Word Processors

- DEC WPS Plus (.dx) Through 4.0

- DEC WPS Plus (.wpl) Through 4.1

- DisplayWrite 2 and 3 (.txt) All versions

- DisplayWrite 4 and 5 Through Release 2.0

- Enable 3.0, 4.0, and 4.5

- First Choice Through 3.0

- Framework 3.0

- IBM Writing Assistant 1.01

- Lotus Manuscript Version 2.0

- MASS11 Versions through 8.0

- MultiMate Versions through 4.0

- Navy DIF All versions

- Nota Bene Version 3.0

- Office Writer Versions 4.0 through 6.0

- PC-File Letter Versions through 5.0

- PC-File+ Letter Versions through 3.0

- PFS:Write Versions A, B, and C

- Professional Write Versions through 2.1

- Q&A Version 2.0

- Samna Word IV+ Versions through Samna Word

- SmartWare II Version 1.02

- Sprint Versions through 1.0

- Total Word Version 1.2

- Volkswriter 3 and 4 Versions through 1.0

- Wang PC (.iwp) Versions through 2.6

- WordMARC Plus Versions through Composer

- WordStar Versions through 7.0

- WordStar 2000 Versions through 3.0

- XyWrite Versions through III Plus

Windows Word Processors

- Adobe FrameMaker (.mif) Version 6.0

- JustSystems Ichitaro Versions 5.0, 6.0, 8.0, 13.0, 2004

- JustWrite Versions through 3.0

- Legacy Versions through 1.1

- Lotus AMI/AMI Professional Versions through 3.1

- Lotus Word Pro Millenium Versions 96 through Edition 9.6, text only

- Novell Perfect Works Version 2.0

- Professional Write Plus Version 1.0

- Q&A Write Version 3.0

- WordStar Version 1.0

Mac Word Processors MacWrite II Version 1.1

Disk Images Symantec Ghost

Encryption Pretty Good Privacy (PGP)

HEIC High Efficiency Image Container

Spreadsheets

- Enable Versions 3.0, 4.0, and 4.5

- First Choice Versions through 3.0

- Framework Version 3.0

- Lotus 1-2-3 (DOS and Windows) Versions through 5.0

- Lotus 1-2-3 (OS/2) Versions through 2.0

- Lotus 1-2-3 Charts (DOS and Windows) Versions through 5.0

- Lotus 1-2-3 for SmartSuite Versions 97 and Millennium 9.6

- Lotus Symphony Versions 1.0, 1.1, and 2.0

- Microsoft MultiPlan Version 4.0

- Mosaic Twin Version 2.5

- Novell Perfect Works Version 2.0

- PFS: Professional Plan Version 1.0

- Quattro Pro (DOS) Versions through 5.0

- Quattro Pro (Windows) Versions through 12.0, X3

- SmartWare II Version 1.02

- SuperCalc 5 Version 4.0

- VP Planner 3D Version 1.0

In addition, Processing does not support the following files:

- Self-extracting .rar files

- Private mail certificate (.pem) files

- Apple i-Works suite (Pages, Numbers, Keynote)

- Apple Mail:

- .emlxpart

- .partial.emlx

The .emlxpart and .partial.emlx are distinct from the .emlx file extension, which is supported by processing.

- Audio/Video files

- .wav

- iCloud backup files

- Microsoft Access

- Microsoft Outlook for Mac (.olm)

- Microsoft Works

- Raw partition files:

- ISO

- NTFS

- HFS

For information on the limitations and exceptions to our supported file types, see Supported file types .

## Supported container file types

The following file types can act as containers:

File type Extensions

Bloomberg .xml

Relativity does not support Instant Bloomberg .xml files.

Cabinet .cab

Relativity does not support multi-part .cab files.

Relativity does not support Password Protected .cab files.

Compressed files .7z, .zip, .tar, .gz, .bz2, .rar, .z, .cab, .alzip

When working with archives, there is no limit to the number of layers deep Processing goes to extract data. It extracts until there is no more data to be extracted. Inventory, however, only extracts data from first-level documents. For example, you have a .zip file within a .zip file that contains an email with an attached Word document, inventory only extracts up to the email.

Relativity does not support multi-part .zip, .tar, or .7z files.

EnCase .e01, .l01, .lx01, .ex01

AccessData Logical Image .ad1

Relativity supports processing both single and multi-part non-encrypted .ad1 files. For encrypted .ad1 files, only single part files are supported. For multi-part .ad1 files, you must decrypt the files prior to processing. See Multi-part container considerations for more information.

iCalendar .ics

For Outlook meeting invites, the email that is sent with the meeting invite (the .msg file) will have a sent date that reflects when the sender sent out the meeting request. The resulting calendar file that is then added to the user's Outlook calendar (the .ics file) will not include a sent date, as the date doe not apply to the calendar file itself.

Lotus Notes Database .nsf

See Lotus Notes considerations for more information.

MBOX Email Store .mbox

.mbox is a standard format, in which case it does not matter whether you're using a Mac folder format or a Unix file format.

Outlook Offline Storage .ost

Outlook Mail Folder .pst

Relativity assigns duplicate hash values to calendar invites, as it does with email messages and other documents.

Outlook Express Mail Folder .dbx

PDF Portfolio .pdf

RAR .rar

You do not need to combine multi-part .rar files before processing them.

TAR (Tape Archive) .tar

Relativity does not handle multi-part .tar files.

ZIP See Compressed files.

Container files do not store encoding information. Because of this, you may see garbled characters in the file names of children files processed from a container file (such as a .zip file) if the originating locale differs from the processed locale. For example, if the originating container file's locale is set to Russian, then processed on an instance set to US, the container's children files may have garbled characters.

### Lotus Notes considerations

Note the following about how Processing handles note storage facility files:

- Processing does not perform intermediate conversion on .nsf files, meaning that they are not converted to .pst or .dxl files before discovering them. This ensures that document metadata is not missed during processing.

- Processing preserves the original formatting and attachments of the .nsf file. In addition, forms are not applied, since they are designed to hide information.

- Processing extracts the contents of .nsf files and puts them into individual message files using the Lotus Notes C/C++ API directly. This is because .nsf files do not have their own individual document entry file format. All of the original Lotus Notes metadata is embedded in the message, meaning if you look at the document metadata in an .nsf file within Lotus, all of the metadata listed is embedded in the message. In addition, the original Rich Text Format/HTML/Plaintext document body is written to the message. Relativity handles the conversion from .nsf to .msg files itself, and any errors regarding metadata or the inability to translate content are logged to the processing Errors tab. Relativity can process the following .nsf items as messages:

- Contacts

- Distribution lists

- Calendar items

- Emails and non-emails

This is an example of an original .nsf file before being submitted to the processing engine:

This is an example of an .nsf file that has been converted to a message:

#### Lotus Notes supported versions

Lotus Notes are supported through Version 10.

### Multi-part container considerations

When processing a multi-part container, the first part of the container must be included. If the first part of the container is not included, the Processing engine ignores the file.

### Calendar file, vCard file considerations

Calendar files (.ics) and vCard files (.vcf) are de-duplicated not as emails but as loose files based on the SHA256 hash. Since the system now considers these loose files, Relativity is no longer capturing the email-specific metadata that it used to get as a result of .ics or .vcf files going through the system's email handler.

The following table breaks down which metadata values the system populates for .ics files:

Processing engine property name Relativity property name

Author Author

DocTitle Title

Email/AllDayEvent [other metadata]

Email/AllowNewTimeProposal [other metadata]

Email/BusyStatus [other metadata]

Email/CommonEnd [other metadata]

Email/CommonStart [other metadata]

Email/ConversationTopic [other metadata]

Email/CreatedOn Email Created Date/Time

Email/DisplayTo [other metadata]

Email/DomainParsedBCC Recipient Domains (BCC)

Email/DomainParsedCC Recipient Domains (CC)

Email/DomainParsedFrom Sender Domain

Email/DomainParsedTo Recipient Domains (To)

Email/Duration [other metadata]

Email/EndDate Meeting End Date/Time

Email/IntendedBusyStatus [other metadata]

Email/IsRecurring [other metadata]

Email/LastModified Email Last Modified Date/Time

Email/Location [other metadata]

Email/MessageClass Message Class

Email/MessageType Message Type

Email/NetMeetingAutoStart [other metadata]

Email/ReminderMinutesBeforeStart [other metadata]

Email/SentRepresentingEmail [other metadata]

Email/SentRepresentingName [other metadata]

Email/StartDate Meeting Start Date/Time

EmailBCC [other metadata]

EmailBCCName [other metadata]

EmailBCCSmtp BCC (SMTP Address)

EmailCC [other metadata]

EmailCCName [other metadata]

EmailCCSmtp CC (SMTP Address)

EmailConversation Conversation

EmailFrom [other metadata]

EmailImportance Importance

EmailSenderName Sender Name

EmailSenderSmtp From (SMTP Address)

EmailSensitivity Email Sensitivity

EmailSubject Subject

EmailTo [other metadata]

EmailToName Recipient Name (To)

EmailToSmtp To (SMTP Address)

SortDate Sort Date/Time

Subject [other metadata]

The following table breaks down which metadata values the system populates for .vcf files:

Processing engine property name Relativity property name

DocTitle Title

Email/BusinessAddress [other metadata]

Email/BusinessAddressCity [other metadata]

Email/BusinessAddressCountry [other metadata]

Email/BusinessAddressPostalCode [other metadata]

Email/BusinessAddressState [other metadata]

Email/BusinessAddressStreet [other metadata]

Email/BusinessPostOfficeBox [other metadata]

Email/BusinessTitle [other metadata]

Email/CellNumber [other metadata]

Email/CompanyName [other metadata]

Email/ConversationTopic [other metadata]

Email/Country [other metadata]

Email/Department [other metadata]

Email/DisplayName [other metadata]

Email/DisplayNamePrefix [other metadata]

Email/Email2AddrType [other metadata]

Email/Email2EmailAddress [other metadata]

Email/Email2OriginalDisplayName [other metadata]

Email/Email3AddrType [other metadata]

Email/Email3EmailAddress [other metadata]

Email/Email3OriginalDisplayName [other metadata]

Email/EmailAddrType [other metadata]

Email/EmailEmailAddress [other metadata]

Email/EmailOriginalDisplayName [other metadata]

Email/FileUnder [other metadata]

Email/Generation [other metadata]

Email/GivenName [other metadata]

Email/HomeAddress [other metadata]

Email/HomeAddressCity [other metadata]

Email/HomeAddressCountry [other metadata]

Email/HomeAddressPostalCode [other metadata]

Email/HomeAddressState [other metadata]

Email/HomeAddressStreet [other metadata]

Email/HomeNumber [other metadata]

Email/HomePostOfficeBox [other metadata]

Email/Locality [other metadata]

Email/MessageClass Message Class

Email/MessageType Message Type

Email/MiddleName [other metadata]

Email/OfficeNumber [other metadata]

Email/OtherAddress [other metadata]

Email/OtherAddressCity [other metadata]

Email/OtherAddressCountry [other metadata]

Email/OtherAddressPostalCode [other metadata]

Email/OtherAddressState [other metadata]

Email/OtherAddressStreet [other metadata]

Email/OtherPostOfficeBox [other metadata]

Email/PostOfficeBox [other metadata]

Email/PostalAddress [other metadata]

Email/PostalCode [other metadata]

Email/PrimaryFaxNumber [other metadata]

Email/PrimaryNumber [other metadata]

Email/State [other metadata]

Email/StreetAddress [other metadata]

Email/Surname [other metadata]

EmailConversation Conversation

EmailSubject Subject

Subject [other metadata]

## Container file types supported for the password bank

The following container file types are supported by Relativity for Password Bank in Inventory.

File type Extensions

Compressed files .7z, .alzip, .zip, .z, .bz2, .gz

Lotus Notes Database .nsf

PDF Portfolio .pdf

PST .pst

RAR .rar

### Non-container file types supported for Password Bank in Inventory

The Password Bank also supports the following non-container formats:

- .pdf

- Excel*

- Word*

- PowerPoint*

- S/MIME

- .p7m

* Except .drm files or custom encryption

On this page

- Supported file types for processing

- Supported file types

- Excel file considerations

- Multi-part forensic file considerations

- Native text extraction and OCR

- Support for password-protected Roshal Archive files

- Outlook message item (.msg) to MIME encapsulation (.mht) conversion considerations

- Email image extraction support

- Microsoft Office child extraction support

- Notable unsupported file types

- Supported container file types

- Lotus Notes considerations

- Multi-part container considerations

- Calendar file, vCard file considerations

- Container file types supported for the password bank

- Non-container file types supported for Password Bank in Inventory


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

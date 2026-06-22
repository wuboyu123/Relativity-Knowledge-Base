---
title: "Processing an RSMF file"
url: https://help.relativity.com/Server2025/Content/System_Guides/Relativity_Short_Message_Format/Processing_an_RSMF_file.htm
collection: user
fetched_at: 2026-06-22T06:16:28+00:00
sha256: ad813c532ef74b3d4c06b94dd81002f352e1986f31f27e9e338892a84c6c6d4e
---

Processing an RSMF file Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing an RSMF file

Relativity Processing is the recommended method of importing RSMF files into Relativity. Using processing ensures that the appropriate metadata header fields are extracted and families and attachments within the RSMF file are properly linked to give you the best near-native review experience.

If you are using a non-Relativity processing tool, attachments need to be manually tied to the appropriate messages following the guidelines below with modifying the Relativity Attachment ID and Family (Group) fields. RSMF is wrapped in an EML so other processing tools should be able to process the other aspects of the RSMF file.

## Checklist for processing an RSMF file

Processing largely handles RSMF files like any other Internet Message Format such as EML. To learn more, see Relativity Short Message Format .

We recommend doing the following before you process an RSMF file:

Feature Steps needed to prepare

Processing profiles

-

Ensure that the default processing profile has the Extract children option set to Yes . Disabling this field results in missing attachments.

-

Ensure the Relativity Attachment ID field is populated for attachments within an RSMF. The Processing application comes with one field that is custom to RSMF and required to ensure attachments are properly mapped. The Relativity Attachment ID is the only system-mapped field and cannot be changed. The Relativity Attachment ID field is mapped. If the Attachment ID is missing for a single RSMF file, you can edit the Attachment ID field in the coding layout by adding the field to your layout and editing the field to include the file name. The file name should match the name in the manifest.json next to the ID.

- Ensure that you select a relational field such as Group Identifier for the Source field. See screenshots below for an example. Setting up Group Identifier in this manner will ensure that attachments appear in the Short Message Viewer and are tied to the correct parent messages. If the Family Identifier is missing for a single RSMF file, you can edit the Family (Group) Identifier field in the coding layout to include the control number.

RSMF Header fields

Ensure the X-RSMF-Version is included in the RSMF Header of the RSMF file. The X-RSMF-Version is required in both RSMF 1.0 and 2.0. To learn more about Headers, see Relativity Short Message Format .

RSMF files greater than 2GB are not supported and may be unable to process. We recommend creating and processing RSMF files no greater than 2GB.

We recommend that an RSMF file should have no more than 10,000 events to ensure high performance in Relativity.

## How parts of RSMF files are processed

The following subsections describe how different parts of RSMF are handled during processing. To learn more about how the RSMF file is constructed, see Relativity Short Message Format .

### RSMF Header

An RSMF will contain a set of headers that is specific to the RSMF file and they begin with the prefix X-RSMF-. These headers are generated at the time of file creation when converting from the source of chat data. The headers are extracted automatically during processing to the following mappable fields. This includes the set of fields highlighted below as part of Relativity as well as any custom headers.

The optional headers that begin with X-RSMF are extracted automatically during processing to the following mappable fields:

RSMF header Metadata field Field Type

X-RSMF-BeginDate Rsmf/BeginDate Date

X-RSMF-EndDate Rsmf/EndDate Date

X-RSMF-EventCount Rsmf/MessageCount Whole Number

X-RSMF-Version Rsmf/Version Long Text

X-RSMF-Generator Rsmf/Generator Long Text

X-RSMF-Application Rsmf/Application Long Text

X-RSMF-Custodian Rsmf/Custodian Long Text

X-RSMF-Participants Rsmf/Participants

Long Text

Only use the Long Text field type for mapping the X-RSMF-Participants header. Selecting Multiple Choice for this header can lead to hundreds of unique choices which negatively impacts performance.

X-RSMF-AttachmentCount Rsmf/AttachmentCount Whole Number

X-RSMF-EventCollectionID Rsmf/EventCollectionID Long Text

Since the RSMF file type is an open format, custom headers are supported as well. They are extracted automatically to the mappable fields using the following:

X-RSMF-CustomHeader → Rsmf/CustomHeader.

The phrase CustomHeader can be replaced with any name less than 255 characters. For example, you can use X-RSMF-IdentificationCode to assign an identification code to each RSMF at the time of creation.

RSMF headers are extracted as metadata fields. They become available for mapping after they are first discovered in a file. If you don't see the particular headers from the list above in your workspace, make sure you are processing RSMF files containing them.

For metadata to be extracted from fields they should be created before processing. As with metadata fields in Relativity, when setting up new headers, you will be required to discover new headers first during processing, establish mapping with fields and then publish the metadata. To learn more, Mapping processing fields .

Since the RSMF file is an EML file, it will also have the To, From, Subject, and Sent headers generated at the time of file creation. These headers will be populated at the time of file creation to adhere to the EML specification.

In addition to the four fields, the X-RSMF-BeginDate and X-RSMF-EndDate headers are commonly mapped into the Relativity Fields below.

Header Relativity Fields Mapping Description

To

-

Email To

-

Email To SMTP

-

Email To Name

-

Email Domain To

-

Email Display To

Usually all participants in the conversation including From sender

From

-

Email From

-

Email Sender SMTP

-

Email Sender Name

-

Author

-

Email Sent Representing Email

-

Email Sent Representing Name

-

Email Domain From

Usually the sender of first message in conversation

Subject

-

Email Conversation

-

Email Conversation Topic

-

Email Subject

Usually a combination of chat name, date, etc.

Sent X-RSMF-BeginDate

-

Date/Time Sent

-

Date/Time Created

Sent date of the first message in the conversation

X-RSMF-EndDate

-

Date/Time Received

-

Date/Time Last Modified

Sent date of the last message in the conversation

Similar to email messages, you can extract all of the headers into a long text field using the Message Header as a source. The Message Header field should exist prior to processing an RSMF file. This field will be populated with all of the metadata stored in the EML header of the RSMF file.

To learn more about what should be included in the header and body, see Requirements for RSMF head and body .

### RSMF.zip

Within the attached RSMF.zip file is the rsmf_manifest.json, which includes all message content and metadata, and the attachments. The rsmf_manifest.json file is not discovered as a publishable file.

For any other file within the rsmf.zip, the following rules apply:

- If the file is referenced within the rsmf_manifest.json:

- The virtual path will exclude the rsmf.zip portion in order to avoid the creation of an rsmf.zip folder in Relativity once the file is published.

- When published, a field called Relativity Attachment ID will be populated with additional metadata. If the file is an attachment, the metadata will be the id of the attachment as specified within the rsmf_manifest.json. If the file is an attached photo or PDF, the metadata will be the name of the file. The Relativity Attachment ID is a system field that the Short Message Viewer uses to provide enhanced support for attachments and avatars.

- If the file is not referenced within the rsmf_manifest.json, it is processed as any other file contained within a zip within an EML. So, when published, it will create a folder called rsmf.zip and the file will be placed within there.

- All discovered files, whether referenced within the rsmf_manifest.json or not, will be fully processed and given the same Group Identifier.

## RSMF deduplication

The deduplication of RSMF files is based on the same method as the deduplication of emails. Relativity is calculating the hash based on the contents of the file and comparing this hash between files, based on the following factors:

-

Header Hash (Subject, From, Date)

-

Recipient Hash (To)

-

Message Body Hash

-

Attachment Hash

This hash will not identify the same RSMF conversations that were collected from different custodians due to the headers being different. It will identify duplicate RSMF conversations from the same custodian assuming the headers are formatted the same. These considerations should be considered when incorporating this into your workflow.

To learn more about this algorithm, visit Deduplication considerations .

### Troubleshooting steps

If the RSMF file exceeds the limit of 2 GB and is reported as error during processing:

-

To be able to successfully process this RSMF file consider slicing it below 2 GB using the same software that was used to generate the file or contact the party that provided you the original file. Consider modifying the settings to smaller time increments when creating the RSMF.

If it appears that Processing is ignoring the Sent Date field or Last Modified field, you can do the following:

- If the RSMF file doesn't include a Sent Date, and the X-RSMF-BeginDate header exists, that header will be mapped to the Sent Date field. The latter takes precedent to the former if both are present.

- The same goes for the ‘Last Modified’ field and X-RSMF-EndDate with taking precedent if both are present.

If all of your data is populated accurately in the Group Identifier field, but your attachments are still not showing up, then verify that the Group Identifier field has the correct GUID. If you have SQL access, query for where the GUID is 1F036749-A691-4AA8-8CF7-5EEB80C36CAF. Otherwise, please contact Relativity Support for assistance.

### Troubleshooting attachments

If the Short Message Viewer shows an error on the attachments, you can also, download and run the RSMF validator for bulk groups of files or use the validator in the Viewer to see issues for a single file. To download, see RSMF validator . The results of the validator will be available using the RSMF Validation icon to the right of the Viewer.

Use the validator and look for these errors that may result in errors with attachments:

-

The attachment with ID {attachment.Id} was not found in the zip archive.

-

To solve this issue, you must recreate the RSMF file ensuring the files are zipped properly within the archive. Verify that the files were included when you created the RSMF.

-

You can check the RSMF file yourself outside of Relativity using any email application. See below for more information.

-

The file {file.Name} in the zip archive does not have a reference.

-

To solve this issue, you must recreate the RSMF file ensuring the manifest.json file is updated to include the file AttachmentID associated with the proper event or message. Verify that the value is a string.

On this page

- Processing an RSMF file

- Checklist for processing an RSMF file

- How parts of RSMF files are processed

- RSMF Header

- RSMF.zip

- RSMF deduplication

- Troubleshooting steps

- Troubleshooting attachments


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

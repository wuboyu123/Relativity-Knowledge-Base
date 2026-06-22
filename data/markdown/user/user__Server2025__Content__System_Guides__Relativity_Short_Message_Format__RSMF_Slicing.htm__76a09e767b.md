---
title: "RSMF Slicing"
url: https://help.relativity.com/Server2025/Content/System_Guides/Relativity_Short_Message_Format/RSMF_Slicing.htm
collection: user
fetched_at: 2026-06-22T06:16:30+00:00
sha256: f5d7f354f015abdff67649fb17e38f913938cdcd875c50dd093cbda3e228d4b3
---

RSMF Slicing Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# RSMF Slicing

This feature allows you to select events in a conversation and "slice" them to create a new document that contains the selected events which can then be imaged and produced like any other document in Relativity. Slicing reduces the need to apply markups to short message conversations and lets you tailor the content of short message documents to your needs.

Once a document has been sliced, it is also easy to track and manage them. When viewing a sliced document in the Short Message Viewer, a banner appears above the document to identify that it is sliced. You can quickly navigate to the original document by clicking on the document's name in the banner.

RSMF Slicing is not available in repository workspaces.

See these related pages:

-

Short Message Viewer

-

Relativity's short message format

## Slicing permissions

The following permissions are needed to use RSMF Slicing:

Object Security Tab Visibility Other Settings

-

Document - View, Add

-

Documents

-

Admin Operations: Allow Import

## Slicing an RSMF document

To slice a document with Relativity's short message format data, do the following:

-

Optionally, click on the Filter icon and filter the document as needed to quickly locate the events you wish to include in the sliced document. As you apply filters, any events that do not meet your currently selected filter options will be grayed out. These events cannot be selected for the sliced document unless you remove the filters.

-

Check the box to the left of any events you want to include in the sliced document. Alternatively, to select all events that are not currently filtered out, click Select all filtered events in the Filter card.

If you select a reply, the parent message will also be included in the new sliced document.

-

Click Save as new document in the bottom-right.

-

Enable or disable the following fields as desired:

-

Email confirmation - If enabled, a user will receive an email when the new document has been sliced.

-

Copy Layout data - If enabled, select the desired layout to make that the default layout in the new sliced document. Any coding decisions that have been saved using that layout will also be carried over to the sliced document.

-

Preserve all participants - If enabled, each participant from the original conversation will be in the metadata of the sliced document, regardless if they were active or not. If disabled, only the participants whose events are selected will be included in the sliced document.

-

Click Save as new document .

A new, sliced document is created with Control Number of the original document appended with "_sliceXXX" added to the name to differentiate it from the original document. When viewing the sliced document, a banner with a link to the original document will be displayed.

A sliced document will have the following fields populated when the sliced RSMF file is brought back into Relativity, along with the default document fields populated via the Import API. Note that attachments within the created slice will be populated with default document metadata via the Import API, along with available file size, file name, and extension.

If users would like to have more fields populated on the new RSMF file upon slicing, they should ensure those fields are on a coding layout, and when creating the slice, the Copy Layout data option is selected. For example, the ‘Custodian’ field is populated on the RSMF file. To bring that field and value over to the new slice, it must be on the coding layout, and that layout must be copied when creating the slice. Otherwise, that field and value will not appear on the new slice.

RSMF EML Header Mapped Fields (if available) Definition Explanation

X-RSMF-BeginDate

-

RSMF/Begin Date

-

RSMF Begin Date

-

Sent Date

-

Sent Date/Time

Populated with the date of the earliest event in the slice. This is reflected in ‘X-RSMF-BeginDate’ in the EML header of the RSMF file.

X-RSMF-EndDate

-

RSMF/EndDate

-

RSMF End Date

-

Last Modified

-

Last Modified Date

-

Last Modified Date/Time

Populated with the date of the latest event in the slice. This is reflected in ‘X-RSMF-EndDate’ in the EML header of the RSMF file.

X-RSMF-EventCount

-

RSMF/MessageCount

-

RSMF Message Count

- Populated with the EML header information within the RSMF file. Slicing updates the following fields within the EML header:

- X-RSMF-BeginDate

- X-RSMF-EndDate

- X-RSMF-EventCount

- X-RSMF-Version

-

The following X-RSMF- fields in the EML header are brought over from the original RSMF file and are not updated:

-

X-RSMF-Application

-

X-RSMF-Custodian

-

X-RSMF-Event-Collection-ID

To

-

Email To

-

Email From

-

Message Header

Populated with a list of participants in the ‘To’ field of the EML header. If you select Preserve All Participants before slicing, this field may remain unchanged from the original slice, based on participants whose events were selected in the slice.

Document Field Definition Explanation

Group Identifier Populated with Control Number of the sliced document, much like it is for regular RSMF documents.

Control Number Populated with the original RSMF document's Control Number but with the appended “_sliceXXX”. If the original RSMF document has attachments in the slice, the attachments will be named similarly to the sliced document, except they will have an additional "_XXX" appended to their name.

Relativity SliceID Populated with the ArtifactID of the original RSMF document.

Relativity Slice Origin ID

The Relativity Slice Origin ID relational field is released in the Review RAP 2.2.0.2. You can access this new field by upgrading your Review RAP to version 2.2.0.2. Otherwise, you will be able access this field when the Review RAP is automatically upgraded in March 2022.

This relational field is populated with the Artifact ID of the original RSMF file when a slice is created. Relativity Slice Origin ID helps users see all slices that were generated from a single RSMF file.

If a slice is created from an existing slice, the new slice has the Artifact ID of the original RSMF file processed into Relativity. Users can open a relational view in the Short Message Viewer that displays all slices created from an RSMF file.

## RSMF slicing filters

The Short Message Viewer has the following filtering options available:

-

Filter - displays or hides a panel containing all filters. Short Message Filtering allows users to quickly locate and investigate messages leveraging the following data dimensions: conversations, participants, events, and dates. See the table below for more information on what data is pulled in from the RSMF file to populate these filters’ values. For more info on the RSMF file format, visit Relativity's short message format .

Filter Category Data from RSMF File

Conversations

In the ‘conversations’ dictionary, there is a field called “display”, that relates to “id”, and is used to populate the conversations filter.

Participants In the ‘participants’ dictionary, there is a field called “display”, that relates to “id”, is used to populate the participants filter.

Events

In the ‘events’ dictionary, there is a field called “type”, which is used to populate the events filter.

-

For RSMF 2.0, event types include: message, join, leave, disclaimer, history.

-

For RSMF 1.0, event types include: message, join, leave, disclaimer.

Dates In the ‘events’ dictionary, there is a field called “timestamp”, the date filter uses to focus on messages in a certain timeframe.

Once a filter is selected, the Viewer will only display messages that meet that criteria. When filtering is applied to the conversation, all message activity bars that do not meet the filter criteria will be grayed out in the Timeline Navigator, but still visible.

If multiple filters are selected within a specific filter category, OR logic is applied to those criteria. When making selections across multiple filter categories, AND logic will be applied. In other words, all selections within a filter category are additive to your results due to the OR logic, and selections across filter categories are subtractive to your results due to the AND logic.

The filter only supports investigative workflows and you are unable to code or produce a filtered conversation.

## RSMF slicing audits

On the original RSMF document, an ‘Update’ audit will be added that captures the following information below.

On the newly created sliced document, a ‘Create’ audit will be added that captures the following information below. By default, there will be a ‘Native – Created’ audit, and two ‘Create’ audits, each of which will show the user name ‘Service Account Relativity’ in the Document History section. Expanding the most recent ‘Create’ audit will show the actual user who created the slice, along with the below information:

-

SourceLayoutID

-

ParentDocumentID

-

SliceDocumentID

-

UserEmail

-

UserID

-

CreatedDateTime

-

SelectedIndexes

-

CreateAttachments

-

PreserveAllParticipants

-

WorkspaceID

On this page

- RSMF Slicing

- Slicing permissions

- Slicing an RSMF document

- RSMF slicing filters

- RSMF slicing audits


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

---
title: "Short Message Viewer"
url: https://help.relativity.com/Server2025/Content/Relativity/Viewer/Short_Message_Viewer.htm
collection: user
fetched_at: 2026-06-22T06:07:16+00:00
sha256: 7c56ade268f76ff8d8a6341ac8a4ffe80f806c5fd4d2b1c0f28a1b8305f21bb7
---

Short Message Viewer

# Short Message Viewer

The Relativity Short Message Viewer displays conversations or individual messages sent using SMS such as iMessage and instant messenger services such as Skype Messenger, Slack, Bloomberg, etc. To learn more about the RSMF files which allow you to view short message data, visit Relativity Short Message Format .

You can determine the maximum document file size in megabytes that can be loaded in the Short Message Viewer by editing the value of the MaximumNativeSizeForViewerForRSMFFilesInMegaBytes instance setting. To ensure stable performance, we recommend entering a value of 250 or less.

Using the Viewer's built-in search capabilities, the Short Message Viewer allows you to find participant names, specific statements, or emojis in conversations. Additionally, you can easily find what was said during a particular time period by using the Timeline Navigator.

Starting in Relativity 12.1.2, the Short Message Viewer supports RSMF 2.0 and 1.0. RSMF 2.0 enriches the data captured within Relativity Short Message Format and enhances the user interface within the Viewer. If you are viewing an RSMF 1.0 file, the user interface may differ from the images below. While we recommend leveraging RSMF 2.0 to ensure the best experience in the Short Message Viewer, both versions are supported in Relativity. For more information about what has been added to RSMF 2.0, see New RSMF 2.0 functionality .

## Permissions

The following permission is needed to use the Short Message Viewer:

Object Security

- Document

- Local Access (Download, Copy Text)

## Short Message Viewer

Short Message Viewer displays an HTML rendering of the message or conversation including attachments, reactions, events, and emojis. The Viewer provides options for navigating through a single document and between documents in a document set. In Short Message Viewer you can also conduct text searching and highlighting text to copy and paste.

### Short Message Viewer toolbar options

The Short Message Viewer provides the following toolbar options:

Relativity automatically hides toolbar buttons and controls that aren't applicable to the currently loaded document type so that your toolbar isn't cluttered while you're reviewing documents.

-

Zoom Out/In - zooms out and in on the current document in increments of 10% within a range of 10% to 4,000%. If you attempt to zoom out to a percentage lower than 10%, the Short Message Viewer automatically sets the display to 10%. If you attempt to zoom in to a percentage higher than 4,000%, the viewer automatically sets the display to 4,000%. Your zoom setting persists as you navigate through a document set. This means that if you've set one document to 150% and you go to the next document, the next document defaults to 150% zoom.

To specify a zoom percentage without using the zoom out/in toolbar buttons, type the number in the percentage field and press the Enter key.

- Reset Zoom - resets the zoom to 100%.

- Fit Width - increases the size of the document to fit the maximum width of the Viewer. This setting persists when you re-size the window.

- Fit Page - fits the entire document into the total size of the page. Clicking this zooms out the document and reduces the font size.

- Fit Actual - fits the document display to the actual size it was in its native application. By default, this resets the zoom percentage to 100%.

- Layout Mode - select one of the following options to determine how documents that are more than one page long display in the Viewer.

- Single - One page of a document will display at a time. Use the page navigation options at the bottom of the Viewer to adjust which page you view.

- Single Continuous - Displays the pages in the document stacked vertically so you can scroll up and down to view them.

- Facing Continuous - Displays the pages in the document in a row horizontally so you can scroll left and right to view them.

- Go To Next/Previous Highlight - moves through previous and next highlighted terms in the document.

- Create PDF - click to save the current native document as a PDF file. When you click this option, the Create PDF pop-up displays. The document then opens in a new window in your browser as a PDF where you can then choose to save or print the document image.

After you click Create PDF , a copy of the document converts to a PDF file you can save from your web browser downloads. Relativity assigns a GUID for Create PDF file names.

- Search Bar - searches for terms in the current document and navigates through the hits.

- Entering a term and either clicking the left or right arrow button or pressing Enter in this text box scrolls to and highlights the text of the next instance of the term (from the placement of the cursor).

- Searching in this text box is not case sensitive.

- The Search Bar supports dtSearch and so proximity, fuzziness, and stemming can be used. To learn more about this search functionality, visit dtSearch .

- You can search for emojis using any of the following methods:

Option Description

Search using copy and paste

If you would like to search for an emoji that displays in the Short Message Viewer, do the following:

- Highlight the desired emoji.

- Either right-click on the emoji and select Copy or press Ctrl+C on your keyboard.

- Either right-click in the Search Bar and select Paste or click in the Search Bar and press Ctrl+V on your keyboard.

Search using an emoticon

If you would like to search for a popular emoji that has an emoticon, you can find the emoticon by visiting RSMF-supported Emoji Emoticon and Attachments . To search using an emoticon, do the following:

- Either type the emoticon or copy and paste it into the Search Bar.

- Press Enter on your keyboard or click to navigate to the first search result.

### Left drawer Short Message Viewer options

The following options are available in the left drawer:

- Persistent Highlighting - displays or hides a panel containing all Recent Searches from the criteria entered in the Search Bar and any persistent highlight sets in the workspace. Only terms in the sets and recent searches that are in the current document will display in the pane. To learn about persistent highlight sets, see Persistent highlight sets .

You can search for emojis in a search terms report or the Search Bar. You can only search for emoji short names using search terms reports in the Extracted Text Viewer. To find an emoji's short name, visit RSMF-supported Emoji Emoticon and Attachments .

- Thumbnail - click to expand the left drawer and display the Thumbnail Viewer and view a thumbnail version of the current document. Each page of the document you're reviewing has its own numbered thumbnail. To learn more, visit Thumbnail Viewer .

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

#### Right drawer Short Message Viewer options

The following option is available in the right drawer:

-

Contextual Search - click to expand the right drawer and display the Contextual Search card. This feature allows you to quickly navigate to matching search terms in a document which is useful in longer documents or ones that have many matching search terms. The Contextual Search card has the same functionality as the Search Bar. To learn more about the Search Bar's functionality, see Search Bar . Additionally, each search term match is displayed in a box that includes both words before and after the search term match to make it easy for you to view the context of each one.

Enter a term or terms in the search box and press Enter on your keyboard to highlight in yellow any matches in the current document. You can click on a desired search term box in the pane to jump to that place in the document. The active search term box will display with a blue border and the matching search term in the document will be highlighted in blue to make it easy to find.

## Navigating the Short Message Viewer

The Short Message Viewer offers a number of features to make finding the desired information in a conversation as easy as possible.

### Platform Icon

The following table displays the different platform icons that can display in the Short Message Viewer. If a file does not contain any information about the messaging platform, the SMS platform displays by default.

Icon Name of Platform Platform Value in RSMF

Slack slack

SMS or MMS sms or mms

Bloomberg bloomberg

Skype skype

iMessage imessage

Google googlechat, google hangout, googlehangout

### Conversation Pane

The Conversation Pane displays a list of the conversation's participants as well as the exact number of messages that were sent during the RSMF file's duration. To display as a participant in the pane, a person must either send a message or add a reaction to an event.

### Navigating the Conversation

To view additional information about the conversation such as start and end date, participants, and any additional custom data, hover your cursor over the platform icon.

To see which participants used a reaction or completed an event, hover your mouse over the reaction/event. Slack messages will only display up to 50 reactions per individual reaction.

Additional information displays to the right of each message to indicate whether a message was tagged by a participant as important or EDITED or DELETED displays to indicate a participant changed or removed that message from the conversation. For Slack messages, hover over the to view the original and edited messages.

By hovering or clicking on the direction icon to the right of a message, users can see what direction this message was sent (incoming or outgoing), which may help give an indication of who the custodian was. This feature is only available when viewing RSMF 2.0 files.

By hovering or clicking on the delivered or read icon, a modal with additional information will be displayed. You can filter or sort the modal as desired to locate relevant information. This feature is only available when viewing RSMF 2.0 files.

You can view a history event by hovering your cursor over the icon. A history event is intended to capture when a participant reviewed the history of the chat and the dates of the historical chats they reviewed. This feature is only available when viewing RSMF 2.0 files.

If there are attachments, including image files that are either a jpg, jpeg, png, or gif, and you have the Document - Local Access (Download, Copy Text) permission granted, the images will be placed in-line within a message. If the attachment is any other file format, it will not display in-line within a message. You can click on the image to expand it.

If you do not have the Document - Local Access (Download, Copy Text) permission and you wish to the view the attachment, open that attachment as a separate file in the Native Viewer.

Starting in Relativity 10.3.142.22, you cannot upload duplicate attachments to a single message.

### Viewer interface for missing information

The Short Message Viewer attempts to display as much information in the RSMF file as possible, even if some information might be incomplete or spoiled. For example, if a custodian deletes texts from their phone this can cause the data to be incomplete when collected. We recommend reaching out to your source of RSMF files to confirm that this data is indeed missing from the collection source.

If an RSMF file contains a chat with no messages, you will not be able to view any of the contents of that RSMF document in the Short Message Viewer.

Below are some examples of unique interfaces you may see in the Short Message Viewer and what they mean:

#### Validation card

When an RSMF document fails to load in the Viewer, a card displays that explains potential issues with the RSMF file. The Validation card is intended to help you discern whether there is an issue with an RSMF file.

#### Reconstructed conversation

This displays if there were events or messages that have a conversation ID in which they occurred, but that conversation doesn’t match any of the conversations in the RSMF file.

#### Unknown conversations

This displays if there were events or messages that have a missing or invalid associated conversation in which they occurred and that conversation isn’t present in the broader RSMF file.

#### Missing timestamps

This displays if an event does not have a timestamp. Events that are missing a timestamp will be displayed at the top of the conversation since they cannot be arranged in chronological order.

#### Undefined participant

This displays when a participant is not identified for an event.

#### Participant #

This displays when a participant who sent a message is not specified in the RSMF file.

#### Orphaned Replies

An event with a parent message, but the parent message is not provided in the RSMF file.

### Troubleshooting attachments

If the Short Message Viewer shows an error on the attachments, see Processing an RSMF file .

### Timeline Navigator

The Timeline Navigator at the bottom of the Short Message Viewer allows you to track the duration and message activity within a conversation. You can also view event activity with an RSMF file in the Timeline Navigator.

To quickly jump to a particular date, click in the Timeline Navigator and the conversation in the Short Message Viewer will move to the selected time. As you scroll through the messages, a blue highlight window will display in the Timeline Navigator to indicate where you are in the conversation.

To view additional information about the conversation on a particular date or time, hover your cursor over the desired time in the Timeline Navigator.

If you have active persistent highlights or search highlights, any bars in the Timeline Navigator that contain highlights display in orange. When filtering is applied to the conversation, all message activity bars that do not meet the filter criteria will be grayed out, but still visible.

Click on the desired bar to conveniently navigate to the desired highlight.

You can re-size the Timeline Navigator by left-clicking and dragging the top of the Navigator to the desired size.

You can click to the Message Timeline icon in the bottom-left to minimize the Timeline Navigator. To return to displaying the Timeline Navigator at its previous size, click Message Timeline icon.

### Copying text in the viewer

While viewing a document in the Short Message Viewer, you can copy text from the document you're currently viewing and then paste it into another application.

To do this:

- Highlight either the text in a single message or the entire text from multiple messages that you want copied.

- Right-click, and then select Copy from the menu.

You can't copy text if you:

- Haven't highlighted any text.

- Don't have permission to the Local Access option on the Document object. This is the same permission that permits you to open the file in its native application. For more information, see Object list in the Workspace security topic.

### Audit Records

Audits populated when viewing an RSMF include:

-

"View" for an RSMF file

-

"Download" for in-line images on that RSMF file only (not for other attachments)

### Adjusting the Time Zone in Short Message Viewer

To adjust the Short Message Viewer to display messages in a different time zone, use the Relativity Native Time Zone Offset field in the Coding Panel.

## Short Message Image Viewer

RSMF files function like documents in the Short Message Viewer with the exception of the Navigation features described below. For more information about imaging options, visit Image Viewer . Additionally, a document with an RSMF file and images that is produced will be treated like any other document in Production .

When emojis are rendered in HTML5, Relativity uses the native browser to render. When the emojis are imaged, the Google set is used. To learn more about the Google set, visit Emojipedia .

When RSMF files are imaged, all messages will be imaged, regardless of if any filtering was applied to the RSMF file in the Short Message Viewer. The image of the RSMF will mirror what you see in the Viewer, and will produce a PDF version of what you see in the Viewer.

By default, we add a ‘Summary Report’ to the first page of the imaged version of the RSMF file. Redactions and other edits are able to be applied to imaged version of the conversation, much like traditional email documents.

Imaging does respect the date format, “DD/MM/YYYY”, for example. The date used for Imaging is based on the Windows regional settings on a given machine.

The Relativity Short Message Format native type is set to use basic imaging in the Native Types tab. It is possible to image in color using the basic imaging engine by setting the Basic Image Format to JPEG on the imaging profile.

## Navigating the Short Message Image Viewer

The Short Message Image Viewer offers a number of features to make finding the desired information in a conversation as easy as possible.

### Short Message Report and Outline of Conversations

The Short Message Report is displayed by default when viewing images in the Short Message Viewer.

At the top of the RSMF file, the Short Message Report displays data about the messages contained within. This report lists the total number of participants, whether they sent a message or added a reaction or not.

The Outline of Conversations displays underneath the Short Message Report and also contains statistical data about the messages. Unlike the Short Message Report, the name of each participant who either sends a message or adds a reaction to an event are listed here. Any participants who have not taken one of these actions are not displayed in this section.

### Navigating the conversation

If a participant enters or leaves a conversation, a message displays underneath their name and avatar to help you track who was involved in the conversation.

If a reaction or event occurs in the conversation, the name of each participant who used that reaction or event displays next to it.

Additional information displays to the right of each message to indicate whether a message was tagged by a participant as important or EDITED or DELETED displays to indicate a participant changed or removed that message from the conversation. When previous events are included, the Edit/Delete modals also include historical posts that you can sort and filter.

Messages that include read or delivered receipts display the time that the event(s) occurred underneath the message text. This feature is only available when viewing RSMF 2.0 files.

Messages can also include an arrow in the upper-right that indicates what direction this message was sent (incoming or outgoing), which may help give an indication of who the custodian was. This feature is only available when viewing RSMF 2.0 files.

### Short Message Image Viewer interface for missing information

The Short Message Image Viewer attempts to display as much information in the RSMF file as possible, even if some information might be incomplete or spoiled. Below are some examples of unique interfaces you may see in the Short Message Viewer and what they mean:

-

Conversations Display field - If this field is not available, the Viewer will display ‘Untitled’ instead.

-

Participant Display field - If this field is not available, Relativity will look for a fall back value that includes the ‘email’ value. If that value cannot be found, Relativity will then look for 'account_id'. If neither of those values are available, the Short Message Image Viewer will display ‘Unnamed [id]’, where [id] is the participant.id field.

-

Participant toolbar - If this is not available, Relativity will look for a fall back value that includes the ‘email’ value. If that value cannot be found, Relativity will then look for 'account_id'. If neither of those values are available, the Short Message Image Viewer will display ‘Unnamed [id]’, where [id] is the participant.id field.

-

Filtering - If this is not available, Relativity will look for a fall back value that includes the ‘email’ value. If that value cannot be found, Relativity will then look for 'account_id'. If neither of those values are available, the Short Message Image Viewer will display ‘Unnamed [id]’, where [id] is the participant.id field

## Extracted Text Viewer

RSMF files can also be viewed in the Extracted Text Viewer if data is included in the Body. and the extracted text comes from the EML file. For more information about Extracted Text Viewer, visit Viewer .

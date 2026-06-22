---
title: "Reviewing documents in Relativity"
url: https://help.relativity.com/Server2025/Content/Solutions/Reviewing_documents_in_Relativity.htm
collection: user
fetched_at: 2026-06-22T06:02:46+00:00
sha256: f131cfb969b7522c8b7d8e69e1ee72e0aa86ff3bb4340a9798c4ce25a05820bc
---

Reviewing documents in Relativity

# Reviewing documents in Relativity

This guide walks you through a generic workflow for a first-pass review. To start your first-pass review, log in to Relativity by browsing to your Relativity website. The login screen appears and you can enter your email address and password. After logging in to Relativity, a list of workspaces you have access to appears. To access workspace documents, click on the name of the relevant workspace. The workspace opens with a list of available documents and you can begin your review.

## Accessing documents

Depending on how your project manager has set up the workspace, you can either access documents via the Documents tab or the Review Batches tab, or both. To access a document, click on its identifier link. The document opens in the Viewer , part of the Review Interface.

View how to access a batch

To check out a batch, perform the following steps:

- Navigate to the Review Batches tab.

- Click Edit next to the batch you want to check out. The Batch Edit pop-up displays.

- Select your name from the drop-down menu.

- Click Check Out .

To check in a batch after you’re finished working, perform the following steps:

- Navigate to the Review Batches tab.

- Click Edit next to your batch. The Batch Edit pop-up displays.

- Select one of the options on the Batch Edit pop-up:

- Check In As Pending – Check in the batch as pending.

- Check in As Completed – Check in the batch as completed.

## Coding documents

During a first-pass review, initial coding decisions are made about a document's relevancy to issues related to a particular matter. Most of your time during review is spent working in the Review Interface and interacting with layouts to store your coding decisions.

### Coding permissions

A user must have the following permission to be able to code documents:

Object security Tab Visibility

Documents - View, Edit Documents

### Working with layouts

Layouts can consist of read-only fields, single-choice fields, and multi-choice fields. Read-only fields give static information about the current document. Single-choice fields are denoted by radio buttons or a drop-down menu, depending on what your project manager has set up. You can only select one coding value for a single choice field. Multi-choice fields are denoted by check boxes. You can select more than one coding value with check boxes.

To make your coding decisions about a document, click Edit on the layout. Required fields appear with an orange asterisk next to their name.

Once you make your coding decision, click Save to return to read-only mode, or click Save & Next to save your coding decisions and move to the next document for review. If you click Save & Next without a coding decision being made, This field is required will display near any required fields.

If your project manager enabled Copy from Previous, you can use this function to copy your coding decisions from the previous document to the current document.

### Using the Viewer

When you open a document from the document list for the first time, Relativity loads that document in the Native Viewer. The Native Viewer provides options for navigating through a single document and between documents in a document set for text searching, highlighting, zooming, arranging, and saving pages you review.

The Review Interface screen consists of the following areas:

- Viewer tabs

- Viewer

- Navigation

- Coding card

- Related items and History cards

- Persistent Highlight card

View document viewing options

You can move through a set of documents by using the navigation menu located in the upper-right corner of the Review Interface.

You can type a number into the textbox and press Enter on your keyboard to move to that document. You can also use the navigation arrows:

Top of first page Previous page Next page Last page

You cannot browse past the last document in your returned set. For example, in the above screen shot, you cannot use the navigation arrows to get to document 1,001. To navigate to document 1,001 change your returned browsable set on the Documents tab. The maximum number of documents in a set displayed in the Review Interface is set to 1,000 by default. This value can be changed using the FluidReviewQueueSize instance setting.

View Native Viewer icons

- Zoom Out/In —zooms out and in on the current document in increments of 10% within a range of 10% to 4,000%. Your zoom setting persists as you navigate through a document set. This

To specify a zoom percentage without using the zoom out/in toolbar buttons, type the number in the percentage field and press the Enter key.

- Reset Zoom —resets the zoom to 100%.

- Fit Width —increases the size of the document to fit the maximum width of the Viewer. This setting persists when you re-size the window.

- Fit Page —fits the entire document into the total size of the page. Clicking this zooms out the document and reduces the font size.

- Fit Actual —fits the document display to the actual size it was in its native application. By default, this resets the zoom percentage to 100%.

- Layout Mode —select one of the following options to determine how documents that are more than one page long display in the Viewer.

- Single —one page of a document will display at a time. Use the page navigation options at the bottom of the Viewer to adjust which page you view.

- Single Continuous —displays the pages in the document stacked vertically so you can scroll up and down to view them.

- Facing Continuous —displays the pages in the document in a row horizontally so you can scroll left and right to view them.

- Show/Hide Hidden Cells —displays or hides all hidden cells in a Microsoft Excel spreadsheet. This functionality is only available for Excel files and does not work on imaged documents because Relativity only images unhidden cells.

- Go To Next/Previous Highlight —moves through previous and next highlighted terms in the document.

- Create PDF —gives you the option of saving the current native document as a PDF file.

- Search Bar —searches for terms in the current document and navigates through the hits.

- Entering a term and either clicking the left or right arrow button or pressing Enter in this text box scrolls to and highlights the text of the next instance of the term from the placement of the cursor.

- Searching in this text box is not case sensitive.

- The Search Bar supports dtSearch and so proximity, fuzziness, and stemming can be used. To learn more about this search functionality, visit dtSearch .

Relativity automatically hides toolbar buttons and controls that are not applicable to the currently loaded document type so that your toolbar isn't cluttered while you are reviewing documents.

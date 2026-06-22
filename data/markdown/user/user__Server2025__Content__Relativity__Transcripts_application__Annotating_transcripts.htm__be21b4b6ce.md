---
title: "Annotating transcripts"
url: https://help.relativity.com/Server2025/Content/Relativity/Transcripts_application/Annotating_transcripts.htm
collection: user
fetched_at: 2026-06-22T06:08:57+00:00
sha256: 23864485e8f1fa5a18fa01c362383656946aa7e37626429dfe546f3b91afedf9
---

Annotating transcripts

# Annotating transcripts

When you open a transcript in the Viewer, you can add the following annotations:

- Notes

- Designations

- Exhibits

- URLs

You can also use the same functionality that you use with other file types in the Viewer. See Viewer .

If you want to see the full document while using Case Dynamics, you can open the document in the pop-out viewer and still use the coding panel.

## Transcripts layout

These annotations are logged in the Transcripts layout and are called out by page and line numbers. If you click on the line number, this takes you to the exact place the annotation is located on the transcript. Clicking on the Exhibit hyperlink opens the document in the Viewer. Clicking on the Note hyperlink sends you directly to the Notes object under the Transcripts tab. The objects on the tabs are sorted by the Created On field. The newest object created is listed first. See Transcripts tab .

## Adding notes

To add a note:

- Select text and right-click.

- Select Add Note . A pop-up appears in the margins.

- Type your note.

- Click Save .

You can then edit, delete, or comment on the note. Other users can comment on your note as well with the ability to create comment threads by replying. You can edit or delete your comments.

Comments and replies are time stamped along with the name of the user who left the comment.

### Expanding notes

Sometimes there are many notes on a single page of a transcript and you cannot read the text all at once.

You can choose to expand or collapse all the notes in a page at once.

To expand/collapse notes, click on the expand/collapse notes icon ( ) along the top of the Transcripts Viewer. When notes are expanded, they will appear on the left side of the transcript text. Each note indicates which page and line number it is tied to.

## Adding designations inline

To add a designation:

- Select text and right-click.

- Select Add Designation .

- Click to add a Designation Type or choose an existing designation type. The list of designations are alphabetized.

You can also edit or delete an existing designation.

Deleting a designation removes all instances of the designation. You receive a warning notifying you before you delete.

- A bracket appears in the margins. You can change the color of the bracket for all designations of that type by right-clicking on the bracket and selecting the drop-down arrow next to the designation type under Change Designation . You can also change the designation type or remove the designation by right-clicking.

When you add a Designation Type, a pop-up window appears where you can select up to two colors.

You can add designations over existing designation types. The brackets appear in the order the designations are created with the inner bracket being the first addition.

## Uploading designations

You can upload a CSV file containing designations and then view those designations in the Viewer alongside any existing designations that were already on the transcript.

The CSV file must have the following columns:

- Transcript name - The name of the transcript.

- Page From - The page number on the transcript where the designation starts.

- Line From - The line number on the transcript where the designation starts.

- Page To - The page number on the transcript where the designation ends.

- Line To - The line number on the transcript where the designation ends.

- Designation - The designation.

To upload designations from a CSV file:

- Go to the Designations tab and click Upload Designations .

- Drag and drop your CSV file into the pop-up window or click browse for a file and select your CSV file.

- Verify that Relativity auto-mapped your columns correctly and click Next .

- Verify that Relativity auto-mapped your transcripts correctly and click Next .

- Click Upload .

The field for uploaded designations is the same field as designations that are added inline. This means that you will not be able to differentiate in the Viewer of the Review Interface between uploaded designations and designations added inline. To verify that your designations uploaded, look at the System created on field for designations.

### Resolving upload designations warnings and errors

When you upload designations, two types of warnings and errors can occur - warnings related to missing data or data type errors in the CSV and import errors.

Uploading designations warnings occur when the CSV file has missing data or data in an invalid format. To resolve the warnings:

- In the Upload Designations window, click the Preview # Errors link.

The Preview Errors pop-up window will open. The Preview Errors pop-up window tells you the location of cells that have warnings attached to them in the CSV file.

- Locate the cells that have warnings in the CSV file and resolve them by either entering the missing data or revising the data format to meet column requirements.

- Upload the revised CSV.

When an import error occurs, go to the Errors tab to find our more information about the error.

## Linking to exhibits

To link to an exhibit:

- Select text and right-click.

- Hover over Link Exhibit .

- Select one of the following:

- Link This Occurrence - Links exhibit only to the selected text.

- Link All Occurrences - Links exhibit to all occurrences of the selected text in the Transcript.

When you select Link All Occurrences, you will see the progress as each occurrence is saved and you can continue working and completing other actions.

- A pop-up appears. Select the document you would like to link and click Set .

You can remove the link by right-clicking and selecting Remove Link . If you click on the link, the document opens in another tab.

You can also link exhibits on the Transcripts layout without directly linking to a line on the transcript:

- Navigate to the Exhibits tab on the layout.

- Click Link .

- Select the exhibit(s) you would like to link.

- Click Add .

- Click Set .

## Linking to URLs

To link to a URL:

- Select text and right-click.

- Select Link URL . A pop-up appears.

- Enter the URL.

- Click Link URL .

You can remove the link by right clicking and selecting Remove Link . If you click on the link, the URL opens in a new tab.

## Working with Case Dynamics

You can create and link Case Dynamics items when viewing transcripts or through the Case Dynamics coding pane on the Transcripts layout. See Case Dynamics .

Case Dynamics items are highlighted with a corresponding color.

The Transcripts Viewer provides a legend to identify Case Dynamics items. To expand the legend, click along the bottom right corner of the Viewer.

You can hide the legend by clicking .

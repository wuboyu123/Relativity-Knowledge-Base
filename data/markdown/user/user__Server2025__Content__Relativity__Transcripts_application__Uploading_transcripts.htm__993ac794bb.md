---
title: "Uploading transcripts"
url: https://help.relativity.com/Server2025/Content/Relativity/Transcripts_application/Uploading_transcripts.htm
collection: user
fetched_at: 2026-06-22T06:08:54+00:00
sha256: a8b5f841216f3049e58842dc49bd438e8a1eab9e8a698e3e7d0006a197256aba
---

Uploading transcripts

# Uploading transcripts

When uploading transcripts, Relativity automatically creates a folder to house all transcripts with sub folders named after the Deponent Name field. Transcripts are stored in these folders, along with any corresponding attachments. When exhibit folders are uploaded with a transcript, the naming convention includes an underscore (_). If there are no exhibits, an exhibit folder is not created.

## Special considerations

Special considerations include:

- The Transcripts application supports transcript files up to 10GB. The upload can be a mix of transcript files, exhibits and video files.

-

The Transcripts application does not support transcript files that contain footers. For example, the .txt transcript file below is not supported because it contains a footer.

See Uploading transcripts .

-

The Transcripts application does not support Transcript files that contain a word index before they are uploaded to Relativity. For example, the .txt transcript file below is not supported because it contains a word index.

See Word index .

- Transcripts are ordered alphabetically in the document list. See below for example:

- Exhibit 1

- Exhibit 10

- Exhibit 11

- Exhibit 12

- Exhibit 2

- Exhibit 20

- Exhibit 21

- The Transcripts application doesn't support uploading a draft version of a transcript and then later replacing it with the final version of the transcript. You can import both transcripts to Relativity, but one will not override the other and annotations aren't carried over.

## Upload a transcript from the Documents tab

Once uploaded, native files can be seen in the Native Viewer. All non-native files can be seen in the Extracted Text Viewer instead.

To upload a new transcript to a workspace from the Documents tab:

- Navigate to the Documents tab.

-

Click the arrow on the right side of the Simple File Upload icon to open a drop-down menu, and then select New Transcript .

- Click Choose File or drag and drop your file to upload. When the transcript imports successfully, a green check mark appears.

If you uploaded a bundle of files, Relativity extracts the transcript file and displays the extra files as exhibits. Supported bundle file types include .lef and .xmef. See Supported file types for the Transcripts application . To ensure the files are uploaded, the Transcript file name and the file extension must be 200 characters or less.

Once they are uploaded, you can find the exhibits as document references in the transcripts layout. They will not have a page or line number unless they are directly linked to a page and line on the transcript. Existing links to exhibits in transcripts files will be visible in the Viewer once they are uploaded to Relativity.

- Click Select File to upload exhibits. To upload and link additional exhibits to a transcript, use Simple File Upload and then link the exhibits using the Transcripts layout. For more information, see Simple File Upload and Linking to exhibits .

Only 20 exhibits can be linked to a transcript upon initial upload. By modifying the SFUMaxFilesToUpload instance setting, administrators can increase the number of files you can upload up to 100 files.

- Fill out the fields:

- Control Number - choose the file name or a enter a control number.

- Deponent Name - enter the name of the deponent.

- Upload Files - click Select to choose which exhibit files you would like to add along with the transcript.

- Deponent Type - select Fact, Expert, or Character deponent.

- Deposition Date - enter the date of the transcript's creation.

- Volume - enter the volume of the transcript you are reviewing.

- Status - select Draft or Final.

- Transcript Source - select Hearing, Trial, Or Deposition.

- Taking Attorney - enter the name of the taking attorney.

- Defending Attorney - enter the name of the defending attorney.

- Party - select Plaintiff or Defendant.

- Lines per page - enter the number of lines per page reflected on original transcript file taken by the respective court reporter.

- Comments - add custom comments to the transcript being imported in this custom field.

- (Optional) If you want to change the number of lines per page, type the number of lines per page that you want into the Lines Per Page box and then hit enter on your keyboard. Click Reset in the upper right corner to revert the number of lines per page.

- (Optional) If you want the transcript to have a different starting line, click Select Starting Line and then click the line of the transcript that you want to be the first line. Click Clear in the upper right corner to revert the starting line.

- Click Upload .

A tool tip indicates that the Deponent Name will be the name of the transcripts folder created.

### Uploading a video of an interview

Transcripts load files often come with a video of the interview. The video can be played in the Viewer in sync with the text of the transcript. To learn more, see Supported file types for the Transcripts application .

You must import videos at the same time you are uploading transcripts or the video and transcript cannot sync.

To upload a video using a .txt file:

-

Click New Transcript . A pop-up appears.

- Click Choose File or drag and drop your .txt file to upload.

- Multiple attachments will appear uploaded along with the transcript. Make sure that you keep the .mp4 check box selected.

- Fill out the relevant fields. See Uploading transcripts with Simple File Upload .

- Click Upload .

To upload a video using a .mp4 file:

- Click New Transcript . A pop-up appears.

- Upload your transcript file.

- Next to Upload Files click Select.

- Navigate to your .mp4 file and upload it.

- Fill out the relevant fields. See Uploading transcripts with Simple File Upload .

- Click Upload .

Videos are not documents and are not stored in the document list in Relativity. Videos are stored as a file field within a transcript. To access a video, you will need to open it from the Viewer or find it in the folder browser. To distinguish videos from transcripts, videos will have an icon ( ) next to them.

To open the video player in the Viewer, click the video icon ( ) in the bottom, left side of the Viewer.

To go directly to a specific line of the transcript in the video:

- Hover your cursor over the desired line number.

- Right-click and select Go to video from this line .

To give yourself more room to annotate the transcript, click , which will pop the video player out of the viewer. To pop the video player back in the viewer, click .

## Mass importing transcripts with the Relativity Desktop Client

Since a transcript is a document file, you can mass import transcripts using the Relativity Desktop Client, specifically by selecting the appropriate Document object to import.

See Importing through the RDC .

When transcripts are imported using Relativity Desktop Client, they are initially created as native documents. When you view the native documents in the Viewer, the transcript is processed and all of the transcript data is populated.

You can use a relative or absolute path when importing transcripts using the RDC. An example of a load file is provided below.

## Reading transcripts with page number

There may be situations where you only upload a portion of a transcript, or split up a witness transcript in volumes.

Page numbers will appear on transcripts to indicate the page number for the whole transcript, and not the imported portion. The Viewer will still show page number based on the uploaded amount of pages.

## Supported file types

The Transcripts application supports a number of different file types. To learn more, see Supported file types for the Transcripts application .

## Editing the Transcripts Import Layout

To edit the Transcripts Import Layout:

- Navigate to the Layouts tab.

- Click on the Transcripts Import Layout .

- Click Build Layout .

-

Customize your layout by dragging and dropping fields into the Transcript Fields category. Certain fields will not display as options when you're customizing the Transcripts Import Layout because they are set during the import process of a transcript file. These fields include:

-

Control Number

-

Extracted Text

-

File Extension

-

File Name

-

File Size

-

Is Transcript

-

Transcript Bundle

-

Transcript Deponent Name

-

Transcript Document Type

-

Transcript Metadata

-

Transcript Name

-

Transcript OI Metadata

-

Transcript Viewer Text

-

Transcript Word Index

See Layouts .

- Click Save .

The Transcript Information category does not change and includes the following fields:

- Control Number

- Deponent Name

If you upgrade, your customized layout does not change.

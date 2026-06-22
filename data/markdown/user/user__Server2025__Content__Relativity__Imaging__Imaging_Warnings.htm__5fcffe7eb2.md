---
title: "Imaging Warnings"
url: https://help.relativity.com/Server2025/Content/Relativity/Imaging/Imaging_Warnings.htm
collection: user
fetched_at: 2026-06-22T06:14:15+00:00
sha256: e81f16688944a58b611f8d74a1eef43624a2d9ee014c4b85b53ba543e6cab59e
---

Imaging Warnings

# Imaging Warnings

The Imaging Warnings object identifies possible cut-off content on imaged MSG or EML files and stores that information.

Though MSG, P7M, P7S, ICS, VCF, EML, EMLX, and TNEF email file types are supported for imaging only EML and MSG file types are supported for imaging warnings.

To view a list of documents that have Imaging Warnings, go to the Imaging Warnings tab. You can also add Imaging Warning fields to a Core Reviewer layout or Document view.

## Special considerations

Keep in mind the following special considerations when working with Imaging Warnings:

- If you delete an image, the Imaging Warnings associated with the deleted image will still exist.

- If you delete a document that has associated Imaging Warnings, the warnings will no longer be visible and cannot be searched for later.

- Relativity will not perform the warning detection process on images uploaded using the image replacement feature in the Document viewer.

- Relativity will not perform the warning detection process on images longer than 25 pages. Documents longer than 25 pages will be marked as Cut-off Detection Not Performed in the Warning Type field.

## Imaging Warnings tab

The Imaging Warnings tab displays information related to current Imaging Warnings.

Historic imaging warning information is not preserved. If a document with an Imaging Warning is re-imaged, the previous Imaging Warning is deleted.

### Imaging Warning layout

When you click on the Imaging Warning field for a particular document, the Imaging Warning layout opens.

The Imaging Warning layout cannot be accessed from the Documents tab. Access the Imaging Warning layout from the Imaging Warnings tab or from the Core Reviewer layout by clicking on the Imaging Warning field for a particular document.

The Imaging Warning layout has the following fields:

- Relativity Document Identifier - the control number of the document imaged along with a link to that document in the Viewer.

- Imaging Warning - a description of the problem detected. Description options are:

- Possible cut-off embedded image detected.

- Possible cut-off text detected.

- Cut-off detection not performed.

- Split performed on table larger than page width.

- Possible missing or invalid Rich Text Format content detected in the email body.

-

Possible invalid character coding detected.

For more information, see All imaging warnings .

- Warning Type - a predefined list of options that facilitates searching when trying to group warnings. This field has better searching performance than a text-based field, such as Imaging Warning. Warning Types include:

- Cut-Off Text.

- Cut-Off Embedded Image.

- Cut-Off Detection Not Performed.

- Table Split.

- Missing or Invalid Rich Text Format Content.

-

Character Encoding Mismatch.

- Warning Details - additional information related to the problem found, such as the page range where problems are detected.

- Imaging Method - Basic or Native.

- Native Type - the Relativity supported file type of the document before it was imaged.

- Job Type - the method used to create the image. Job Types are:

- On-the-fly.

- Mass imaging.

- Imaging Set.

- Imaging Set - links to the Imaging Set that the image was produced through if the image was created via an Imaging Set.

- Notes - a space for you to enter notes.

Except for the Notes field, you cannot modify the Imaging Warning fields, and you cannot link or unlink Imaging Warnings to documents.

### Warning Type pivot table

In the Imaging Warnings tab, you can create a pivot table based on the Warning Type field and then export the pivot or dashboard. See Running Pivot reports and Dashboards .

You can only create the Warning Type pivot in the Imaging Warnings tab. The Warning Type field is not available for widgets on the Documents tab.

## All imaging warnings

The following table lists the all the imaging warnings:

Imaging Warning Type Why the warning occurred Next step

Character Encoding Mismatch

Text in this document could be encoded in a way that may produce invalid or unreadable characters when imaged. Specifically, email metadata indicates that the message body is encoded in <format>, but part of the body text was also encoded in <another format>. Example formats include:

- utf-8

- Windows-1252

- us-ascii

Create a saved search with this warning type as a search condition and manually QC the returned documents. See Creating or editing a saved search .

Cut-Off Detection Not Performed Email that is greater than 25 pages cannot have cut-off detection performed on it. See Special considerations . Create a saved search with this warning type as a search condition and manually QC the returned documents. See Creating or editing a saved search .

Cut-Off Embedded Image Embedded images within a table go beyond the boundaries of the page. Use different imaging profile options, such as landscape, auto-fit tables, split tables and auto-fit images. See Imaging profiles .

Cut-Off Text Text within a table goes beyond the boundaries of the page. Use different imaging profile options, such as landscape, auto-fit tables, and split tables. See Imaging profiles .

Missing or Invalid Rich Text Format Content.

Rich Text Data within the email is possibly missing or incorrect. As a result, text in the email body may be missing from the image generated.

Create a saved search with this warning type as a search condition and manually QC the returned files. See Creating or editing a saved search .

Table Split

Tables that go beyond the boundaries of the page have been split and re-printed on a new line.

Create a saved search with this warning type as a search condition and manually QC the returned files. See Creating or editing a saved search .

Table Split Not Completed Tables that are beyond boundaries of the page could not be split. Reasons for this include an abnormally wide first column, when there are rows that span across multiple columns, or a table within a table. The exact page where the table begins will be reported.

Use different Imaging Profile options, such as landscape, auto-fit tables, and split tables. See Imaging profiles .

## Core Reviewer layouts

To facilitate the QC of documents, you can link the Imaging Warnings layout to a Review layout. See Adding and editing an object list and Imaging Warning layout .

You can also add Imaging Warnings fields to a Core Reviewer layout. The Core Reviewer layout can be configured to show Imaging Warning details or create pop-ups with that information. See Layouts .

Imaging Warnings fields that you can add to a layout include:

- Imaging Warning - a description of the problem detected. Description options are:

- Possible cut-off embedded image detected.

- Possible cut-off text detected.

- Cut-off detection not performed.

- Split performed on table larger than page width.

- Possible missing or invalid Rich Text Format content detected in the email body.

-

Possible invalid character coding detected.

- Warning Type - a predefined list of options that facilitates searching when trying to group warnings. This field has better searching performance than a text-based field, such as Imaging Warning. Warning Types are:

- Cut-Off Text.

- Cut-Off Embedded Image.

- Cut-Off Detection Not Performed.

- Table Split.

- Missing or Invalid Rich Text Format Content.

-

Character Encoding Mismatch.

- Warning Details - additional information related to the problem found, such as the page range where problems are detected.

## Re-imaging emails with tables

You can image large tables in emails without the table being cut-off in the resulting image by setting the Split tables to fit page width field in the Native imaging profile to Yes. When this field is set to Yes, wide tables are split and re-printed on a new line when they are imaged with no content lost.

The following screen shot shows an imaged email where the Split tables to fit page width field was set to No on the imaging profile.

This screen shot shows an imaged email where the Split tables to fit page width field was set to Yes on the imaging profile.

Selecting the Split tables to fit page width field will slow down your imaging time. As a result, you may want to image documents without the field set to Yes first and then re-image all of the documents that acquire an Imaging Warning.

To re-image documents that have an imaging warning:

- Create a saved search that brings back documents with Imaging Warnings.

- Select Imaging Warning from the Add Condition drop-down menu. A pop-up window will open.

- Select these conditions from the Operator.

- Click Add Condition and select Imaging Warning::Warning Type .

- Select any of these from the Operator drop down.

- Move Cut-Off Embedded Image and Cut-Off Text from Available to Selected and click Apply .

(Click to expand image)

- Click Apply .

For more information, see Creating or editing a saved search .

- Delete the images in documents that have Imaging Warnings.

- Filter on the saved search you just created.

- Select Delete from Mass Operations.

- Select Delete only images from selected documents .

- Click Delete .

- Create a Native Imaging Profile, and in the Email Options tab, set the Split tables to fit page width field to Yes . For more information, see Imaging sets .

- Create an Imaging Set.

- Select the saved search you just created for Data Source.

- Select the native imaging profile you just created for Imaging Profile.

- Click Save .

For more information, see Imaging sets .

- Open the Imaging Set.

- Click Image Documents from the Imaging Sets console.

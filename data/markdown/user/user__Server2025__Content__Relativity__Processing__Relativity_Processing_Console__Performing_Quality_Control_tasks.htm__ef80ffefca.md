---
title: "Performing Quality Control tasks"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Relativity_Processing_Console/Performing_Quality_Control_tasks.htm
collection: user
fetched_at: 2026-06-22T06:13:54+00:00
sha256: 4361feeec97d31f0e7df8f2c8bbef0113336a08a755f97c23f6af764e993a5ff
---

Performing Quality Control tasks Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Performing Quality Control tasks

You can view extracted text and imaged documents, as well as perform other quality control tasks in the Matter Inspector.

In the Matter Inspector you can:

- View all metadata for a selected file.

- Inspect multiple jobs.

- Apply filters to inspect specific files.

- View native files.

There is no option for batching out documents for QC.

To QC documents:

- In the Data Stores window, drill down to the import job that you want to review.

- Right-click the import job, and click Inspect .

- From the Matter Inspector window, click Refresh Needed to display a list of documents in the grid box.

In the Matter Browser, click the column heading to sort the list of documents. An indented file is child of the file above it. Only one level of the parent-child hierarchy is displayed in the grid, but the database records the full hierarchy.

You're unable to add more columns to the Matter Browser.

## Performing automatic QC

The RPC's QC process uses a check-in/check-out system, multiple users can work with the same document at the same time. Automatic QC automatically checks out a document when navigating to it, and checks it back in when it moves on the next one. Automatic QC is especially useful when you have to perform QC on a large import job, as it presents you with a steady, controllable stream of images to inspect.

To perform automatic QC on a data set's documents:

- In the Matter Browser, click the Automatic QC icon.

- If needed, in the Image Viewer, increase or decrease the length of the delay before the RPC moves to the next image. Clicking the plus sign increases the delay and offers you more time to view the image and clicking the minus sign shortens the delay, thus making the QC process move faster.

- In the Image Viewer, click the play button to start the automatic advancement of images.

- Perform QC on the images as they automatically appear, one at a time, in the Image Viewer.

- The RPC only flips through each image and presents them to you for your manual QC, it doesn't perform the QC for you.

- A Placeholder is a document that the RPC couldn't image and thus automatically made a placeholder for.

You can't actually configure a placeholder in the RPC; you can only generate a blank placeholder through the Generate Placeholder right-click option in the Matter Browser, or you can upload a PDF file created outside of the RPC for the Custom placeholder PDF option in the OCR/Image tab of the Job Settings window.

- If you need more time on a single image, click to pause on that image.

- When you're finished QC-ing, select the documents you want to mark as finalized and click the Finalize QC button.

- Note that the documents you marked as QC'd are green in the Matter Browser.

See Matter Inspector window and Image Viewer window for more QC options.

Alternatively, you can right-click on a file in the Matter Browser to display a pop-up menu. This menu includes options for generating placeholders, displaying intermediate folders, and others.

## Non-image QC

The RPC gives you the option of performing QC on non-image files. You can do this in either the Extracted Text or the Page Text viewers in the Image Viewer pane.

To perform non-image QC, follow these steps:

- In the Matter Browser, select Exclude the following and select Has Images . Doing this will include only non-image files from the import in the viewer.

- Click the Refresh Needed text when it appears. This will update the file list in the Matter Browser to meet the criteria you've just set.

- Open the Extracted Text or Page Text Viewer to perform QC on each file you select.

- Once you've finished QCing a document, click the Finalize QC icon. Files for which you've finished QC appear green in the Matter Browser.

Once you've QC'd images, you can filter the data. See Filtering data .

On this page

- Performing Quality Control tasks

- Performing automatic QC

- Non-image QC


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

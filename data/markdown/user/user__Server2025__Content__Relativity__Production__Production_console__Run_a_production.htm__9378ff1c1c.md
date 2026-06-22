---
title: "Run a production"
url: https://help.relativity.com/Server2025/Content/Relativity/Production/Production_console/Run_a_production.htm
collection: user
fetched_at: 2026-06-22T06:08:47+00:00
sha256: 2c96e8fb4d2bb72c850264e52d1f9a614015904398bf3ad81964064f09338187
---

Run a production

# Run a production

To run a production, click Run Production in the production console. After you click Run Production, the status bar updates with the following stages and fields as the documents produce:

- Cleaning Existing Files - deletes placeholder files (slip sheets) and any produced image files from a prior run production, if necessary.

- Creating Placeholder Images - creates placeholder images based on the production data source.

- Creating and Applying Bates numbers - creates and applies Bates numbers based on your production numbering.

- Creating Branding Queue Records - creates branding queue records for later review.

In the viewer, you can view the produced images by selecting the Production mode. You can view the images exactly as they were produced.

## Checking production status

During the production step, a report is available in the Status section. Use this report to quickly identify the number of documents, images, redacted documents, etc.

### Production Summary fields

Production Summary fields include:

- Begin Bates - lists the Bates number of the first document in the production set.

- End Bates - lists the Bates number of the last document in the production set.

- Total Docs - lists the number of documents included in the production set.

- Total Images - lists the number of images included in the production set.

- Docs with Images - lists the number of documents that include images included in the production set.

- Docs with Placeholders - lists the number of documents that include placeholders included in the production set.

- Docs with Redactions - lists the number of documents that include redactions included in the production set.

Production does not include any redactions applied to native documents when using Relativity Redact, only redactions applied using the image viewer and markup set contained on images will be included.

- Total Image size in GB - lists the size of images in GB.

- Run Date - lists the date of when the production was run.

### Branding Summary fields

Branding Summary fields include:

- Start Time - lists the start time of branding.

- Branding Completion - lists the time of completion for branding.

- Completion Rate - lists the progress of branding.

- Estimated Time Remaining - lists the amount of time left in branding.

### Post Production Summary fields

Post Production fields include:

- Copy Bates to Document Fields - lists the progress of step

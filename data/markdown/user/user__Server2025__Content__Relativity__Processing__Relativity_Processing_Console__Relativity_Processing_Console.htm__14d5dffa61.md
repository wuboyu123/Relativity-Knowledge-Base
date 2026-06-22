---
title: "Relativity Processing Console"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Relativity_Processing_Console/Relativity_Processing_Console.htm
collection: user
fetched_at: 2026-06-22T06:05:44+00:00
sha256: 7ca72663bb97d703b6f7502d20d9dbd5cc946b7e937e8eae149da5d6a43326e6
---

Relativity Processing Console

# Relativity Processing Console

The Relativity Processing Console is a desktop application that lets you control complex processing jobs on a granular level. The RPC offers power processing users to extend the full capabilities of Processing .

See these related topics:

- Installing the RPC

- RPC user interface

- Importing data

- Extracting text

- Indexing data

- Filtering data

- Running standard reports

- Generating images

- Performing Quality Control tasks

- Exporting data

- Managing workers and jobs

- Field mappings

- Maintenance tasks

- RPC known issues

## RPC features

The RPC includes, but is not limited to the following features:

- Granular worker and job control – prioritize worker servers into work groups, which you can allocate to work on specific jobs or processing functions.

- Selective import of data – choose specific folders and files to import for a given custodian, import or exclude specific files by extension, De-NIST documents.

- Extract text - able to extract text directly from documents, images, or files with embedded images OCR’d automatically.

- Indexing options - uses the dtSearch as its full-text search engine, automatically indexes all metadata along with extracted text to ensure nothing is overlooked.

- Filter options - multiple filtering options, including date/time, de-dupe with extremely flexible options, cross reference, expression, and full text.

- Reporting – create several reports, including de-dupe filter, error, summary, search filter.

- Generate images – render documents as PDFs without the need for print drivers, significantly improving performance. Imaging jobs are also multi-threaded, and you can monitor worker activities.

- QC Functionality – preview all images and extracted text - or a random sample - track progress, auto-advance images, and flag them for further review or replacement.

- Full metadata access – all extracted metadata fields are identified and stored in individual fields for potential use.

- Robust export options:

- Numerous filtering options, including date/time, cross reference, expression, and full text.

- Customize and brand/endorse the images for export.

- Select metadata fields.

- Format fields – for example, specify date or date/time for date fields.

- Variable substitution – for example, specifying the return of a variable in a specific field.

- Build switch statements – for example, similar to a v-lookup, "when x is found return y".

- Track status.

## Running an RPC job

There are many ways to run a job using the RPC. Below is a typical workflow. Note that you're free to deviate from it as necessary to meet your own needs. Click a step to navigate to a topic.

Depending on your needs, you can re-order or skip some of these steps completely. For example, if the filtering you require doesn't include keyword searching, you have the option of skipping indexing. You can also skip extracting text, indexing, and filtering and jump directly to imaging, and you'll still be able to export text. Image generation also creates page-level text by default, which you can export either on a page or document level, as needed.

It's important, however, to know the prerequisite steps for the tasks you intend to perform. The following table breaks down those prerequisites.

Desired RPC task Prerequisite

Extracting text

Imported data

- Can be done immediately after import

Generating images

Imported data

- Can be done immediately after import

Indexing data Either text extraction or image generation

Full-text search filtering An indexed import

All other filtering

Imported data

- Can be done immediately after import

- No text extraction or imaging is required

Exporting metadata

Imported data

- Can be done immediately after import

Exporting images or page level text Image generation

Exporting doc level text Either text extraction or image generation

Exporting native files

Imported data

- Can be done immediately after import

Exporting PDF files Image generation

## Special considerations

You can use the RPC in conjunction with Processing, or as a standalone tool. For example, you might use the RPC to monitor and troubleshoot jobs that you kick off from Processing, or run disparate jobs solely in the RPC.

However, consider the following when using the RPC in conjunction or disparately from Processing.

- The Inventory feature only exists in Processing.

- The ingestion filtering feature only exists in Processing because Inventory only exists in Processing. However, it is still possible to De-NIST an import or include/exclude specific file extensions from an import job using the RPC.

- You can't direct export to Relativity for review at this time.

- Reports are different than Processing reports.

- You can't cancel a job in the RPC.

- You can use the RPC to track a processing job in Processing, however, the RPC doesn't capture the following in Relativity:

- Re-leveling

- Retrying and/or clearing errors

- Altering document extracted text

- Changing the parent/child document relationship

- Changing the following RPC settings on a processing job may cause unexpected behavior in Processing as there may be conflicting settings on the same data sets:

- Adding store-level settings

- Adding project-level settings

## Logging in to the RPC

To provide visibility into who has accessed the RPC and for how long, Relativity requires you to provide user authentication to log in to the RPC. Any active Relativity user can log in to the RPC with their Relativity credentials.

This functionality was introduced in Relativity 9.4.398.62 .

To log in, click on your instance of the RPC to bring up the login screen, enter your Relativity username, and click Continue .

Enter your password and click Login . If you use RSA authentication to log in to the RPC, make sure that the server on which the RPC is installed is configured for RSA, or you won't be able to log in.

If you don't see the login screen, or your login attempt(s) fail, go to the machine on which the RPC is installed, get the identity server URL, open a browser on the machine where the RPC is installed, enter the identity server URL, and attempt to log in again. The identity server URL is case sensitive.

You now have access to all RPC functionality.

To log out of the RPC, navigate to the File tab and click Logout & Exit .

Relativity records RPC logins and logouts in the user's audit history; however, it doesn't designate those actions as being RPC-specific. In this case, you could see duplicate records for "Login" and "Logout" in your audit history, one for Relativity and another for the RPC.

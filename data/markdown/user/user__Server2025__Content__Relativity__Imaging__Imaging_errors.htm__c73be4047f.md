---
title: "Imaging errors"
url: https://help.relativity.com/Server2025/Content/Relativity/Imaging/Imaging_errors.htm
collection: user
fetched_at: 2026-06-22T06:14:14+00:00
sha256: 33b23a5acb12b1b73da9e2a2a9576a2a6a20b75581b394f4a6826ce8f0df6e9d
---

Imaging errors

# Imaging errors

Document level imaging errors are common when you run an imaging set, and you may encounter several of them when you go to check the progress of your set.

If you upgrade to Server 2025 and your environment contained imaging sets with errors, the Retry errors button on the Imaging Set console is disabled, and you won't be able to retry those errors in Relativity 9.0. You will, however, be able to re-run the imaging set that contains the errors after you upgrade to Server 2025 .

## Viewing imaging errors

To view document level imaging errors, go to the Imaging Document Error tab. The Imaging Document Error tab contains all imaging error history, including errors that are resolved. The error name provides succinct descriptions for easy understanding and resolution, these include:

- Document Type is not supported.

- OI EXOpenExport failed - 11: file is password protected or encrypted.

- OI EXOpenExport failed - 4: no filter available for this file type.

- OI EXOpenExport failed - 9: file is corrupt.

- OI EXOpenExport failed - 10: file is empty.

Legacy errors in the system before upgrading to 9.7.229.5 stay in the Show Errors pop-up dialogue and do not migrate to the Imaging Document Errors tab.

To learn more about an imaging error, click the Name field for a document on the Imaging Document Error tab. The Imaging Document Error Layout will open. Layout fields include:

- Relativity Document Identifier - the document identifier of the document.

- Status - the status of the imaging error - Ready to retry, Retried, or Resolved.

- Imaging Method - the method that was used to image the document – Basic or Native.

- Native Type - the file type of the item in error as identified by the native imaging engine.

- Job Type - the method used to image the document - Imaging Set, Mass Imaging, or Image on the fly.

- Imaging Set - the imaging set that the document belongs to if the Job Type is Imaging Set. If you click on the Imaging Set, you will be taken to the Imaging Set Layout.

- Notes - space to record any notes that you have about the imaging error.

You can also navigate to the Imaging Document Error Layout from the

- Imaging Sets tab .

- Documents tab .

- Review Interface .

### Imaging Sets tab

To see imaging errors via the Imaging Sets tab:

- Go to the Imaging Sets tab.

- Click on an Imaging Set. The Imaging Set Layout will open.

- Click View Document Errors on the Imaging Set console. This brings up the Imaging Document Error tab with a list of the errors that occurred during the job. By default, this action will add a filter to the Imaging Document Error tab to show only errors with a status of Ready to retry.

- Click on the Name field for a document to obtain more information about the error. The Imaging Document Error Layout will open.

### Documents tab

To see documents with imaging errors via the Documents tab:

- Go to the Documents tab.

- Create a new view.

Fields Conditions Sort

- Originating Imaging Document Error

- Has Images, any of these: Error

- NA

- Select the view you just created from the View bar.

- In the Document list, click on the Originating Imaging Document Error link for a document. The Imaging Document Error layout will open.

### Review Interface

To see imaging errors on the Review Interface layout:

- Click on the Layout.

- Add the Originating Imaging Document Error field to the Layout.

- Click Save and Close .

- In the layout, click on the Originating Imaging Document Error link for a document that has an imaging error. The Imaging Document Error layout will open.

## Imaging error scenarios

Errors will occur in your imaging job in any of the following scenarios:

- The Native Imaging engine attempts to render a corrupted native file.

- The Native Imaging engine attempts to render a password-protected native file that doesn't have a valid corresponding entry listed in the password bank tab. For more information, see Password Bank in imaging workflow .

- The Native Imaging engine attempts to render a document when the native file for that document is deleted from the repository.

- The Native Imaging engine attempts to render a native file when the FileShare repository is unavailable (access is denied).

- The Native Imaging queue service is stopped when the user attempts to run an imaging job.

- The Native Imaging queue service becomes disabled in the middle of an imaging job.

- The Native Imaging engine attempts to render a native file when there is no hard drive space in the file share repository.

- The Native Imaging engine is installed but the imaging job is not pointing to a valid server because the Native Imaging URL in the instance setting table is incorrect or invalid.

- The conversion request failed.

- The imaging request is no longer tracked. Something occurred on the server that resulted in a request key getting wiped out. This error is only visible in the population table and not in the Errors tab. This is usually the result of an IIS reset. This applies to running an imaging set, mass image, and image-on-the-fly jobs.

- The request key has become invalid because Invariant was attempting to report on a conversion or imaging job that Relativity isn't tracking anymore because Invariant failed to recognize that the job timed out. This could be caused by an IIS reset. This applies to running an imaging set, mass image, and image-on-the-fly jobs.

When Relativity Native Imaging encounters an error, it retries the imaging job one time. Relativity logs additional errors in the error report.

## Error email notification

When errors occur in an imaging set, an email is sent to all users included in the Email Notification Recipients field for that imaging set. The email notification summarizes the errors and directs you to the Imaging Document Errors tab in Relativity.

## Retrying imaging errors

To retry errors that occurred during the completion of your imaging set, click Retry Errors, View Document Errors on the console.

When you retry imaging errors, you are simply imaging those documents again. Thus, the retry errors button changes to Stop Imaging once the retry job begins and reaches a status of Initializing. Click Stop Imaging to stop the error retry job.

## Password Bank in imaging workflow

The following steps depict how the Password Bank typically fits into the imaging cycle.

- You create a password bank that includes a list of passwords that correspond with the files you intend to image. See Creating or deleting a Password Bank entry .

- You create an imaging set with the data source that contains the encrypted documents. See Creating and editing an imaging set .

- You start imaging the documents in the imaging set by clicking Image Documents in the Imaging Set console. See Running an imaging set .

- All passwords you supplied to the password bank become synced via an agent and accompany the job as it goes to the imaging engine.

- The imaging engine images the files in the imaging set and refers to the passwords provided in the password bank. It then sends the imaged files back to Relativity.

- Once the imaging status changes to Completed, you review and release images from QC review. See Monitoring imaging status and QC Review .

- The imaged documents become available for review in the workspace, along with all the other previously-encrypted documents whose passwords you provided.

To view and resolve password-protection errors:

- Click View Document Errors in the Imaging Set console after you run an imaging set. See Imaging errors .

- Outside of Relativity, locate the passwords designated to unlock those files.

- Return to Relativity, go to the Password Bank, and create entries for every password that corresponds with the errored files. See Creating or deleting a Password Bank entry .

- Click Retry Errors in the Imaging Set console to retry imaging the files that previously resulted in password-protection errors. See Retrying imaging errors .

For more information, see Password bank .

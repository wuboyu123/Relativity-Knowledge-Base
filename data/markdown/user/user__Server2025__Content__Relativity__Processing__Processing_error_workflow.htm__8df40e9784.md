---
title: "Processing error workflow"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Processing_error_workflow.htm
collection: user
fetched_at: 2026-06-22T06:05:55+00:00
sha256: e4ba68df78a6d8b47111263a461d2788e0c7cf56fccbed59f9b465a483aff7f1
---

Processing error workflow

# Processing error workflow

This topic provides information on working with errors that may occur during processing jobs.

The content on this site is based on the most recent monthly version of Relativity, which contains functionality that has been added since the release of the version on which Relativity's exams are based. As a result, some of the content on this site may differ significantly from questions you encounter in a practice quiz and on the exam itself. If you encounter any content on this site that contradicts your study materials, please refer to the What's New and/or the Release Notes for details on all new functionality.

## Required security permissions

The following security permissions are required to perform actions on File Errors:

Object Security Tab Visibility

-

Discovered File - View, Edit

-

Download and Replace files with processing errors

-

Processing

-

Files

The following security permissions are required to perform actions on Job Errors:

Object Security Tab Visibility

-

Job Error - View, Edit

-

Processing Error - View, Edit

-

Processing

-

Job Error

For more information on permissions, see Workspace permissions .

## Processing errors tabs

The Files and Job Errors tabs allow you to easily locate issues that may have occurred in any processing sets. These errors are notified to you through the processing set page upon job completion.

### Files tab

The Files tab contains all error information associated to specific files that have occurred during the discovery, publish, and deletion phases of processing. The Current Errored Files and All Errored Files views are tailored to error workflow by only containing information pertaining to the errors that have occurred.

-

The Current Errored Files view displays all outstanding errors from processing jobs. This is your primary location for workflows like error retry, ignore, and file replacement.

-

The All Errored Files view is primarily utilized for historical reporting of errors from processing sets. This view displays any file that has encountered an error, regardless of whether it was resolved or not. It is a good reference to export an error report out of Relativity for a given collection or set of custodians.

For more information on these views, see Files tab.

### Job Errors tab

The Job Errors tab contains all errors that occurred on processing sets run in your workspace. These errors are usually not associated with any specific files within a processing set, but rather to the entire set itself.

#### Job Error views

The Current Job Errors view in the Job errors tab displays all unresolved job errors while the All Job Errors view displays any job error that has occurred throughout the lifecycle of the matter. Both views contain the following fields:

- Error Identifier - the unique identifier of the error as it occurs in the database. When you click this message, you are taken to the error details layout, where you can view the stack trace and other information. Note that for Unresolvable errors, the console is disabled because you can't take any actions on that error from inside Relativity. For more information, see Processing error workflow .

- Error Status - the status of the error. This is most likely Unresolvable.

- Message - the cause and nature of the error. For example, "Error occurred while trying to overlay deduplication details. Please resolve publish error or republish documents from data source below. DataSource Artifact Id: 1695700".

- Custodian - the custodian associated with the data source containing the file on which the error occurred.

- Processing Set - the name of the processing set in which the error occurred.

- Data Source - the data source containing the file on which the error occurred.

- Error Created On - the date and time at which the error occurred during the processing job.

- Republish Required - the error must be retried in order to be successfully published.

- Notes - any manually added notes associated with the error.

Errors occurring during inventory are always represented as Job Errors. For more information, see Inventory Errors .

### Job Error layout

Clicking on the job error identifier value brings you to the Job Error Details layout.

Note that the Error Actions console is disabled for unresolvable job errors, since you can't retry or ignore job errors the way you can document errors.

To see the job error's stack trace, click on the Advanced tab of the error details layout and view the value in the Stack Trace field.

#### Job-level error workflow

See an overview diagram of the job error workflow

The following diagram depicts the standard workflow that occurs when Relativity encounters a job-level error during processing.

## Useful error field information

The following sections provide information on error-specific fields and views that you can use in your processing workflow.

### Combined error fields

The Files tab displays a single error associated to a file.

This error displays through the Error Message , Error Category , Error Phase , and Error Status fields. However, multiple errors can be associated to a single file at the same time as issues can occur during different phases of Processing. Relativity determines the displayed error based on a set precedence of Processing phases that could potentially block content from being published. The precedence is as follows:

-

Delete – a document was deleted from Relativity, but encountered an issue, potentially affecting recalculation of deduplication.

-

Publish – a document was supposed to be promoted to review but encountered an error and was held back.

-

Discover –a file may have encountered an issue during expansion and may not have extracted a child record and/or associated metadata.

-

Text Extraction – a file encountered an issue during text extraction and is missing some or all associated text.

### Error status information

The Error Status field provides information on where the file is in error remediation.

This is helpful to determine if any further actions are required on a file or to see if an error had ever occurred on a record. When a file has all its errors resolved, the Error Message , Error Category , and Error Phase fields no longer display any content, but the Error Status field keeps a status of Resolved to indicate that it was a record that initially encountered issues but have since been fixed. The statuses of errors are as follows:

-

Not Resolved – The error is still outstanding.

-

Resolving – The error was submitted or in the process of being retried.

-

Resolved – The error was resolved.

-

Ignored – The error was ignored. See File error actions .

### Error Category list

The Error Category field provides insight into the nature of the errors that have occurred during processing.

The following table provides a listing of all values on the Error Category field, along with a description of what kinds of issues those values bring back if filtered.

Category name Description

Corrupt Container

These errors are exclusive to container files that have encountered corruption when attempting to open and locate files within the container itself. When containers have these errors associated to them, you will not see any extracted loose files . These errors are usually either ignored or downloaded offline for an investigation on whether the corruption can be remediated and then subsequently replaced and retried.

Corrupt File These errors are exclusive to non-container files that have found elements of corruption during Processing. These errors are either ignored or downloaded offline for an investigation on whether the corruption can be remediated and then subsequently replaced and retried.

Could Not Identify Relativity Processing was unable to identify the file during Discovery. This may indicate corruption in the file but was unable to be determined at the time of discovery.

Environmental These errors are caused by issues in the Relativity Processing environment. These should be retried and resolved when encountered.

File Read / Write Failure These errors are a subset of Environmental issues specifically caused by file system issues. These should be retried and resolved when encountered.

Missing Attachment An attachment from a document or email was not able to be extracted from its file.

Missing File Metadata A file is missing a piece of metadata.

Missing Extracted Text These errors represent issues that occurred during Text Extraction jobs that have caused a file to be missing some or all associated text. A specific root cause was unable to be readily identified, but they should be retried and resolved where possible.

Partially Corrupted Container These errors are exclusive to container files that have encountered corruption during extraction of specific records. When containers have these errors associated to them, you may see some files extracted, but not all . These errors are usually either ignored or downloaded offline for an investigation on whether the corruption can be remediated and then subsequently replaced and retried.

Password Protected Container

These errors are exclusive to container files that have encountered some form of password protection or encryption security measures. These errors are not resolved unless the proper passwords or encryption keys are placed in the Password Bank. For more information, see Password Bank .

When investigating publish errors, if you see five password protected errors associated with an .MSG file, but the email and all of its contents opens and displays correctly in the viewer, it means a password-protected container was attached to the email.

Password Protected File These errors are exclusive to non-container files that have encountered some form of password protection or encryption security measures. These errors are not resolved unless the proper passwords or encryption keys are placed in the Password Bank. For more information, see Password Bank .

Relativity Field Configuration These errors represent issues with Field Mapping during publish jobs. They are usually associated to a specific setting like length or an Associative Object Type. When encountered, the field settings should be resolved according to the error message and resolved.

Unsupported Relativity Processing has determined that these files are unsupported and was unable to obtain metadata or text from them. These files can be published to your workspace, but they may be inaccessible from the Viewer.

### Details modal

You can open the Details modal of a file by clicking to see uncompressed file and content metadata not visible by default in the Files view.

The Details modal provides you with supplemental information about errors that have occurred on records during discovery and publish.

You can also see a summary and history of all Processing Errors and retries in this modal. When you click the Processing Errors tab, you're presented with the following breakdown of the current errors and error history of the selected file:

- The Error History section represents all errors that have ever occurred on a file. This acts as a timeline of the record’s errors, showing when they occurred, what they were about, and if any are still active. This includes errors resulting from retries of previous errors and contains category, phase, date/time, and message information. All times are kept in UTC format.

-

The Error Summary section displays a count of all active errors along with their associated category and phase. This is especially important when investigating errors relating to container files, as there can be many associated to the parent container during file extraction. This helps determine the level of impact the issue has as it may affect many files originating from it.

### Pivotable error fields

By default, all relevant processing error fields are available to group by and pivot on in the Current Errored Files and All Errored Files views of the Files tab.

For descriptions of all the fields available for Pivot, see the Files tab.

## File error actions

Action can be taken on file errors from the Processing Set page or from the mass operations available on the Files tab.

### Processing Set error retry

You can retry file errors within the Processing Set by using the Retry File Errors button located under the Processing Set console on the right-hand side of the page.

A confirmation message pops up reminding you of the errors you are about to retry. Click Retry to proceed or Cancel to return to the processing set layout.

Only file errors with a high chance of success will be retried. The probability of success is determined by the error category associated with the file. Error categories such as Corruption or Password Protection will not be retried as they are not likely to be resolved without manual intervention (for example, adding passwords or replacing a corrupt file). A full list of what will and will not be retried can be found below:

Error

Category

Included in

Retry Button

Corrupt Container No

Corrupt File No

Could Not Identify No

Environmental Yes

File Read/Write Issue Yes

Missing Attachment Yes

Missing child items due to password protection No

Missing Extracted Text Yes

Missing File Metadata Yes

Partially Corrupted Container No

Password Protected Container No

Password Protected File No

Relativity Field Configuration No

Unsupported No

## Files tab error actions

From the Files tab, you can take action on your errored files through the mass operations view.

Mass operation Description

Export as CSV This exports the list of processing errors as a CSV file.

Republish

Gives you the option of republishing the files that the errors occurred on. Once you resolve the errors listed, you can use this option, and if the republish is successful, the files will be available in the Documents list, and no errors will be displayed in the Current Errored Files view.

For details on how to republish files from the Files tab, see Republishing files .

Retry Errors

This action provides the ability to resolve issues occurring during discover and publish. These issues can be found on the Current Errored Files and All Errored Files views within the Files tab. For details on how to retry errors from the Deleted Documents view in the Files tab, see Retrying delete errors .

-

You must have Edit permissions on the Discovered Files object to be able to retry file errors.

-

Note the following regarding retrying errors:

-

Auto-publish is not enabled when you retry errors. If any discover or text extraction errors are resolved, you will need to manually publish them into your workspace by navigating back to the processing set and clicking the Retry button.

-

Not all errors reported in the discovery process can be resolved. This is expected as processing reports all issues it encounters through an error.

-

The discovery retry of errors process has a longer timeout period than the initial discovery process. It is not uncommon for the retry process to run longer than the initial discovery process.

-

You should always resolve all publish errors as these errors represent data not in review.

-

If an error occurs on a loose file during discovery, Relativity still attempts to publish it. For example, if a Password Protected error occurs on a PDF during discovery, that file still has the ability to be published in its current state. The resulting record may have metadata and/or extracted text missing depending on the issue, but it can still be referenced during review.

-

Relativity automatically retries all publish errors for a set when any error within that set is retried.

-

Multiple retry attempts cannot be worked on simultaneously. If a secondary retry is submitted while the initial one is still in progress, the second retry will wait in a queue until the first retry is completed.

-

Only errors with an Error Status of Not Resolved can be submitted in a retry job.

Ignore Errors

This provides the ability to set a file’s Error Status to Ignored, which will remove it from the Current Errored Files view. The record will still be visible in the All Files and All Errored Files views.

Undo Ignore Errors This provides the ability to set a file’s Error Status field back to its original value after it had previously been ignored.

Download / Replace

-

This provides the ability to download a file to your local machine for investigation. It will also provide the ability to replace an original file with a new version that has been fixed during error remediation.

-

Note the following regarding downloading and replacing files:

-

you can only download / replace a single file at a time.

-

you can only perform these actions on files with an Error Status of Not Resolved.

-

there is no limitation for downloading files.

-

there is a limitation of one gigabyte for uploading replacement files.

-

performing a replacement of a file will automatically retry its associated errors once completed.

-

after uploading a new document, when you select Replace & Retry, the native file is updated before you republish.

-

the retry action for job errors will only retry errors in a Ready to Retry state.

For more information on the Download / Replace mass action, see Download and Replace on the Files tab page.

The following mass operations are available:

## Common workflows

### Identifying and resolving errors

You have completed discovery or publish on your processing set and noticed that it had encountered some errors. You want to investigate and resolve those errors quickly so you can get all possible data into your workspace. Starting from your processing set, perform the following steps:

-

On the right-hand side of the page under Links, select File Errors to go directly to the Current Errored Files view on the Files tab. Automatic filtering takes you to the files in the previously viewed processing set.

-

On the Files tab you can optionally filter down on the errored files that are the most important to resolve. Some common filters are the following:

-

Error Category - to group issues of a similar type.

-

Error Phase - to group issues that occurred during a particular part of Processing.

-

Custodian -if you have a priority Custodian that requires all records to be investigated first.

-

Sort Date - to retry files within the matter's relevant date range.

-

Once a group of records is identified to resolve, select the Retry Errors mass action to begin the process. Alternatively, you can retry all errored files without filtering.

-

You can now track your progress of the error retry through the processing set page’s progress bar or by navigating to the Worker Monitoring page in Home mode .

For more information on Worker Monitoring, see Processing Administration .

### Replacing a corrupted file

Sometimes, files reach processing in a corrupted state. Here is a workflow to replace corrupted files with non-corrupted versions so you can get the most out of your data. This works on encrypted documents as well.

For more information on replacement considerations, see Download / Replace .

Starting from your processing set, perform the following steps:

-

On the right-hand side of the page under Links, select File Errors to go directly to the Current Errored Files view on the Files tab. Automatic filtering takes you to the errored files in the previously viewed processing set.

-

Locate the file you need to replace. Common techniques are:

-

Filter Error Category for Corrupted File or Corrupted Container.

-

Filter by specific file names.

-

Filter for specific error messages.

-

Select the appropriate checkbox on the left-hand column of the view.

-

Select the Download / Replace option in the mass action menu.

-

From here, two options are available:

-

to inspect and/or repair your container, select the download button

-

once you are in possession of your replacement container, drag and drop it into the modal or select browse for files to locate your container

-

Once the replacement file has been added to the modal, it automatically uploads to Relativity. A quick verification process will let you know if any issues were found or if there were any significant differences between the original and replaced files.

-

Select the Replace & Retry button to complete the replacement and retry any Discovery related errors.

When replacing a file, the metadata associated with the new file overwrites any metadata associated with the original file. For example, if a file had an Author of Steve Bruhle in the original file, but has an Author of Dave Crews in the replaced file, the metadata in Relativity will have Dave Crews filled out.

You can create a field and map it to the 'All Fields - Replaced Extracted Text' non-system field. In this way, you can easily use the field to determine if the document contains an extracted text placeholder. For more information on field mapping, see Mapping processing fields .

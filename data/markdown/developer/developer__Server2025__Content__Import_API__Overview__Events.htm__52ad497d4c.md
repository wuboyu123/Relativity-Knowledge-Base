---
title: "Import API events"
url: https://platform.relativity.com/Server2025/Content/Import_API/Overview/Events.htm
collection: developer
fetched_at: 2026-06-22T06:30:01+00:00
sha256: ee4b5ebf7842fd41545a7af7ebe2db09e6fd80079593ae919c6d382e78e797c9
---

Import API events

# Import API events

The Import API raises events that display information about the progress of an import job and any errors that occur.

## OnComplete

This OnComplete event occurs when an import job is finished. A JobReport object is passed with detailed information about the job. A completed job may have errors if the data wasn't imported properly. JobReport has the following public properties:

- StartTime – a DateTime object containing the time the import began.

- EndTime – a DateTime object containing the time the import terminated.

- FieldMap – for document imports with native files, this property contains a List of all fields in the source data, and the fields to which they are mapped in the Relativity workspace.

- TotalRows – the number of rows that were processed.

- ErrorRowCount – the number of rows that contained errors.

- ErrorRows – a List of rows with errors. This property includes the row number, message, and document identifier.

- FatalException – this exception is available when a fatal exception causes the import to terminate.

## OnError

OnError contains a single parameter named Row, which is declared as an IDictionary. This event is raised when an error occurs while importing a row of data. The MaximumErrorCount is a configurable setting available on all import jobs that determines the number of errors to return.

If you are using the ImportBulkArtifactJob class, the Row parameter contains the following key-value pairs for each record that causes an error and fails to be imported:

- Line number – the row number from the SourceData that caused an error. It is a 1-based index. (The first row of a SourceData contains data rather than column names.)

- Identifier – the value in the identifier field for the document that errored, which is the control number in Relativity, by default.

- Message – an error message indicating why the record errored. This message is similar to those in the Relativity Desktop Client.

If you are using the ImageImportBulkArtifactjob class, the Row parameter contains the following key-value pairs for each record that causes an error and fails to be imported:

- Line number – the row number from the SourceData that caused an error. It is a 1-based index. (The first row of a SourceData contains data rather than column names.)

- FileID – the identifier of the image file that errored.

- DocumentID – the value in the identifier field of the document associated with the image that errored.

- Message – an error message indicating why the record errored. This message is similar to those used in the Relativity Desktop Client.

## OnFatalException

The OnFatalException event is raised when an import job encounters a fatal exception caused by invalid import settings or other issues. It passes a JobReport object with detailed information about the exception.

## OnMessage

The OnMessage event is used to programmatically monitor the progress of an import job. It contains a Status parameter, which contains a Message property. The Message property returns values that indicate the progress of the import job, and can be displayed to users. This message is similar to those used in the Relativity Desktop Client.

## OnProgress

The OnProgress event is raised for each row found in a data set:

- After processing each line in a load file (even if an error occurred while processing that line)

- Before processing any lines in a load file when there are no records in it

- Before processing the first item in an image file

- After validating each line in an image file

- Before processing each line in an image file

- After processing all items in an image file

The event reports the line number of the row in the load file or image file.

## OnProcessProgress

You can attach the OnProcessProgess event to import jobs. The OnProcessProgess event is triggered at the same rate as the OnMessage event, but instead of the single Message property of the Status object provides detailed information about the underlying import process as the properties of the FullStatus object.

The properties include:

- ProcessID – the operating system process ID of the import job.

- StartTime – the start time of the import job.

- EndTime – the end time of the import job.

- TotalRecords – the number of records in the import job. The value is an integer.

- TotalRecordsProcessed – the number of processed records. The value is an integer.

- TotalRecordsProcessedWithWarnings – the number of processed records with warnings.

- TotalRecordsProcessedWithErrors – the number of processed records with errors.

- TotalRecordsDisplay – the number of records in the import job. The value is a string.

- TotalRecordsProcessedDisplay – the number of processed records. The value is a string.

- MetadataThroughput – the throughput for transferring document metadata measured in bytes per second.

- FilesThroughput – the throughout for transferring files measured in bytes per second.

- StatusSuffixEntries – the status suffix.

You can use the event in more complex workflows, for example, to get information across multi-threaded imports or create a progress bar.

Example use:

Copy

```text
1
2
3
4
5
6
7
8
9
10
importJob.OnProcessProgress += status => Console.Writeline(status.StartTime);

importJob.OnProcessProgress += status => Console.Writeline(status.EndTime);

importJob.OnProcessProgress += status => Console.Writeline(status.ProcessID);

importJob.OnProcessProgress += status => Console.Writeline(status.TotalRecords);

importJob.OnProcessProgress += status => Console.Writeline(status.TotalRecordsProcessed);

importJob.OnProcessProgress += status => Console.Writeline(status.TotalRecordsProcessedWithWarnings);

importJob.OnProcessProgress += status => Console.Writeline(status.TotalRecordsProcessedWithErrors);

importJob.OnProcessProgress += status => Console.Writeline(status.TotalRecordsDisplay);

importJob.OnProcessProgress += status => Console.Writeline(status.TotalRecordsProcessedDisplay);

importJob.OnProcessProgress += status => Console.Writeline(status.StatusSuffixEntries);
```

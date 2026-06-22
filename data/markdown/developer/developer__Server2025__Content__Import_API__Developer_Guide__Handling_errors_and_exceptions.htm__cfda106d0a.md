---
title: "Handle Import API errors and exceptions"
url: https://platform.relativity.com/Server2025/Content/Import_API/Developer_Guide/Handling_errors_and_exceptions.htm
collection: developer
fetched_at: 2026-06-22T06:30:07+00:00
sha256: f43c3794d97d8e10885c346b605a9766129fdce605f1d3b840c448756fde4d40
---

Handle Import API errors and exceptions Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Handle Import API errors and exceptions

The Import API provides support for handling errors and exceptions. You can register for events that the Import API raises when an error occurs. In addition, you can also throw exceptions when a property isn't set or a field isn't populated during an import job.

## Handle errors

To identify errors that occurred during an import job, register for both the OnComplete and OnFatalException events. These events are available on the ImportBulkArtifactJob and ImageImportBulkArtifactJob classes, and they take a parameter of the JobReport type, which is a class used for error handling. The delegate signatures for these events are as follows:

- OnCompletedelegate void Copy

```text
1
2

OnCompleteHandler(JobReport jobReport);
```

- OnFatalException Copy

```text
1
2

delegate void OnFatalExceptionHandler(JobReport jobReport);
```

The JobReport class contains all of the information about an import job, including all of the errors that may have occurred. Use these guidelines when using the JobReport class to analyze errors:

- An exception caused the import to abort – Review the JobReport.Exception, which contains the exception.

- A row failed during import – Review the ErrorRows property, which is a collection of RowError objects. Each object contains information about the failure of a specific row.

When an import completes successfully, it indicates that all rows were processed but not that all rows were imported successfully.

The properties for the JobReport class are listed in the following table:

Property name Data type Description

EndTime DateTime Import finish time

ErrorRowCount Integer Total number of non-fatal errors that occurred

ErrorRows IList<RowError> Collection of non-fatal row-level errors that occurred

FatalException Exception Exception that resulted in the OnFatalException event

FieldMap IList<FieldMapEntry> Collection of field map entries. They indicate the mapping of source fields to destination fields in the workspace.

StartTime DateTime Import start time

TotalRows Integer Total number of processed rows. This value indicates only the number of processed rows instead of the number of successful rows.

The FieldMapEntry class provides information about the mapping between the source and destination fields. Its properties are listed in the following table.

Property name Data type Description

SourceField String Name of the source field that was mapped

WorkspaceField String Name of the destination field that the source was mapped to

The RowError class provides information about a specific row that contains an error and a related error message. Its properties are listed in the following table.

Property name Data type Description

Identifier String Value for the identifier field in a row

Message String Error message

RowNumber Long Row number containing the error. The first row is line 1 rather than 0.

## Handle exceptions

The Import API provides the following exceptions that may be thrown during an import job:

- ImportSettingsException – This exception is thrown when a required parameter isn't set. It contains the Setting and AdditionalInfo properties. The AdditionalInfo property has a value only as applicable, such as when one of two interdependent properties isn't set.

- ImportSettingsConflictException – This exception is thrown a property is set to a value that conflicts with another property. It contains properties that identify the initial setting and the conflictSetting (that is the property causing the conflict). The exception message contains additional information about the conflict.

### FieldValueImportException for Document Import API

The FieldValueImportException object is thrown when a field can't be populated with incoming data during a document import job. This exception returns the following properties:

- RowNumber – a Int64 containing the number of the row in the data fail that caused an import failure.

- FieldName – a string containing the display name of the Relativity field that wasn't set.

- InnerException – a lower-level exception object containing detailed information about the exception type, such as NullReferenceException, or InvalidCastException.

In addition, the Message property also displays information about an exception as illustrated in the following example:

Copy

```text
1
Error in row {row number} , field {field name}. {Message from inner exception};
```

### InsufficientPermissionsForImportException

The InsufficientPermissionsForImportException error occurs for non-admin users if the Import API configuration is changed to disable auditing. To resolve the error:

- Re-enable auditing for the Import API by setting the AuditLevel to ImportAuditLevel.FullAudit: Copy

```text
1
importJob.Settings.AuditLevel = ImportAuditLevel.FullAudit;
```

- Make sure the user is a member the System Administrators group in Relativity.

## Logging for Import API applications

On the client-side, you have the following options for setting up logging when you call the Import API:

- Relativity logging - use the LogFactory class to instantiate a logger, and then assign the logger to a singleton. See the following code sample. For additional information, see Configure logging . Copy

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
Relativity.Logging.LoggerOptions loggerOptions = new Relativity.Logging.LoggerOptions

{

    Application = "<App-Guid-Goes-Here>",

    ConfigurationFileLocation = Path.Combine(System.IO.Directory.GetCurrentDirectory(), "LogConfig.xml"),

    System = "<System-Goes-Here>",

    SubSystem = "<SubSystem-Goes-Here>"

};

Relativity.Logging.Log.Logger = Relativity.Logging.Factory.LogFactory.GetLogger(loggerOptions);
```

- Custom logging - create a custom class that implements Relativity.Logging.ILog in the Relativity.Logging.Interfaces assembly. Assign your ILog instance to a logging singleton as illustrated in the following code: Copy

```text
1
Relativity.Logging.Log.Logger = instance;
```

Next, implement your own custom logging functionality that is performed through this custom ILog class.

On the server-side, the Relativity API Helpers configure logging automatically, making it available for use. You don’t need to perform any additional steps when using the Import API on the server-side, such as calling it from an agent.

## Write to an error log

You can use the ExportErrorReport() method on the ImportBulkArtifactJob and ImageImportBulkArtifactJob classes to write an error log. This method takes a filePathAndName parameter, which specifies the location for the error log. It exports an empty file when a job doesn't generate any errors, and overwrites the existing error log. The Import API generates detailed error messages as illustrated in the following example:

Copy

```text
1
Error in row 6, field "sampledecimalfield". Input string was not in a correct format.
```

On this page

- Handle Import API errors and exceptions

- Handle errors

- Handle exceptions

- FieldValueImportException for Document Import API

- InsufficientPermissionsForImportException

- Logging for Import API applications

- Write to an error log


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use

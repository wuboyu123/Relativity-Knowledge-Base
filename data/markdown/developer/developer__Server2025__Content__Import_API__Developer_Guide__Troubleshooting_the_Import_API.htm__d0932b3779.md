---
title: "Troubleshooting the Import API"
url: https://platform.relativity.com/Server2025/Content/Import_API/Developer_Guide/Troubleshooting_the_Import_API.htm
collection: developer
fetched_at: 2026-06-22T06:30:05+00:00
sha256: 8dd67e0dd826627536367fac588e6c944b3afb3e4fb0003163b5ae6e77694818
---

Troubleshooting the Import API Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Troubleshooting the Import API

You can troubleshoot an import job by using the information in the error message to identify the cause of a failure. Most non-fatal errors are RowError objects that are a part of the JobReport.ErrorRows property.

## BadImageImportFormatException error

When you attempt to build a project, you receive the following BadImageImportFormatException message:

This error occurs when you attempt to build your application against wrong target platform. If you see this error, you must target x64. In Visual Studio, select the appropriate configuration for your target platform in the Configuration Manager dialog as illustrated here:

For more information, see Set up a development environment .

## Extracted text file causes error during import

If you attempt to import a large, extracted text file, an error may occur because the file exceeds the size limit. We currently don't support importing extracted text files larger than 2 GB.

## Missing child object

A non-fatal error occurs when a file can't be found during import. The following error message is displayed:

Copy

```text
1
Could not find file ‘{filename}’.
```

{filename} indicates the value supplied in the image file path.

## Missing file

A fatal error occurs when a file can't be found during import. The following error message is displayed:

Copy

```text
1
Could not find file ‘{filename}’.
```

{filename} indicates the value supplied in the image file path.

## Missing file path

A fatal error occurs when an image import is performed with DisableImageLocationValidation set to True and no image file path has been supplied. The following error message is displayed:

Copy

```text
1
The path is not of a legal form.
```

To resolve this error, confirm that a valid path is specified and is accessible by the Import API.

## Missing file specified for a document

When an image import is performed with DisableImageLocationValidation set to False and an image file is missing, the following error message is displayed:

Copy

```text
1
One of the files specified for this document does not exist.
```

To resolve this error, confirm that the file exists and is accessible by the Import API.

## Missing text file

When the ExtractedTextFieldContainsFilePath setting is enabled, and the extracted text file for a row can't be found, the following error message is displayed:

Copy

```text
1
Error in line {number}, column “{column}”. Error: full text file specified does not exist.
```

This error message points to the column for extracted text. {number} indicates the line number where the error occured, and {column} indicates the column order, such as A, B, C, and so on. To resolve this error, verify that the extracted text file exists and that it can be accessed by the Import API. Make sure that the path doesn't contain any typographical or other errors.

## File already exists

An I/O error indicating that a file already exists is thrown when importing documents or images:

Copy

```text
1
FatalException: System.IO.IOException: The file exists
```

To resolve this error, delete the contents in the C:\Users\relserviceaccount\AppData\Local\Temp directory on the agent server.

## Unexpected import behavior

If you experience unexpected import behavior, you may be using Import API .dlls that don't match the version of Relativity installed in your environment. To resolve this issue, check the version of the kCura.Relativity.ImportAPI.dll. Right-click the file and select Properties . Click the Details tab in the dialog.

If you have mismatched versions, download the most recent version directly from NuGet. For more information, see Set up a development environment

## Unexpected import behavior with choices

When importing new choices, you may experience the following unexpected behaviors:

- Errors occur when importing choices

- Import job for choices is slow

To resolve these issues, limit the number of choices in a single import job to 100. This number indicates the maximum of new values in all choice type fields across the entire set of records.

## Reference to a nonexistent ArtifactID

When an invalid ArtifactID is specified by the ObjectFieldIdListContainsArtifactId setting for valid single or multiple object field, the following error message is displayed:

Copy

```text
1
 An object field references an artifact ID which doesn’t exist for the object.
```

To resolve this error, confirm that the ArtifactID maps to a valid single or multiple object instance.

## SQL exceptions occur when importing many fields

When importing a large number of fields, you may receive one of the following messages indicating an SQL exception:

Copy

```text
1
2
System.Data.SqlClient.SqlException (0x80131904): Internal error: Server stack limit has been reached. Please look

for potentially deep nesting in your query, and try to simplify it.
```

Copy

```text
1
2
System.Data.SqlClient.SqlException: The query processor ran out of stack space during query optimization.

Please simplify the query.
```

To resolve these issues, limit the number of fields in a single import job to 100.

## Warning message thrown when processing batches

When the Import API throws an error while processing batches, you may receive a warning message similar to the following:

Copy

```text
1
Processing sub-batch of size 900. 0 of 1000 in the original batch processed
```

To resolve this warning, increase the MassImportSqlTimeout value in the Instance setting table. This value applies only to batches of files imported using the Import API. You also may want to confirm if you have enabled batch resize and experienced timeout error. You can lower the batch size limits by 100 and retry the import.

For more information, see Instance settings' descriptions on the Relativity Server 2025 Documentation site.

On this page

- Troubleshooting the Import API

- BadImageImportFormatException error

- Extracted text file causes error during import

- Missing child object

- Missing file

- Missing file path

- Missing file specified for a document

- Missing text file

- File already exists

- Unexpected import behavior

- Unexpected import behavior with choices

- Reference to a nonexistent ArtifactID

- SQL exceptions occur when importing many fields

- Warning message thrown when processing batches


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

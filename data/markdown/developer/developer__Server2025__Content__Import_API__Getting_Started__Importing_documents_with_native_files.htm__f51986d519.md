---
title: "Import documents with native files"
url: https://platform.relativity.com/Server2025/Content/Import_API/Getting_Started/Importing_documents_with_native_files.htm
collection: developer
fetched_at: 2026-06-22T06:29:54+00:00
sha256: 26b1891495bfd71e003c48ce5cba4fe8bca9cd7337f79c14b3d58c53b6c6ec2c
---

Import documents with native files Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Import documents with native files

You can use the Import API to add documents to a workspace programmatically by using the methods available on the ImportAPI class. You can also import document metadata, native files, and extracted text associated with documents.

On GitHub, you can find can comprehensive samples illustrating how to import native documents, images, objects, and productions. For additional code samples, see the Server Import API samples repository.

## Create a document import job

When importing documents to a workspace, you instantiate the ImportAPI class and call its NewNativeDocumentImportJob() method. You use a DataTable object as the data source for a document import job. This sample code illustrates how to perform these tasks, as well as references the following code samples that demonstrate how to write messages and create a DataTable object.

If your environment is configured to use RSA authentication, then you can enter your Relativity account username, and RSA passcode when instantiating the ImportAPI class.

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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
static void ImportDocument()

{

     Int32 workspaceArtifactID = 1015495;

     Int32 identifyFieldArtifactID = 1003667;



     String relativityUserName = "jane.doe@relativity.com";

     String relativityPassword = "<your password>";

     String relativityWebAPIUrl = "http://localhost/Relativitywebapi/";



     ImportAPI iapi = new ImportAPI(relativityUserName, relativityPassword, relativityWebAPIUrl);



     var importJob = iapi.NewNativeDocumentImportJob();



     importJob.OnMessage += ImportJobOnMessage;

     importJob.OnComplete += ImportJobOnComplete;

     importJob.OnFatalException += ImportJobOnFatalException;

     importJob.Settings.CaseArtifactId = workspaceArtifactID;

     importJob.Settings.ExtractedTextFieldContainsFilePath = false;



     // Indicates file path for the native file.

     importJob.Settings.NativeFilePathSourceFieldName = "Native File";



     // Indicates the column containing the ID of the parent document.

     importJob.Settings.ParentObjectIdSourceFieldName = "Parent Document ID";

     // Indicates the column containing the ID of the Data Grid records already created for the documents.

     importJob.Settings.DataGridIDColumnName = "Data Grid ID";

     // The name of the document identifier column must match the name of the document identifier field

     // in the workspace.

     importJob.Settings.SelectedIdentifierFieldName = "Doc ID Beg";

     importJob.Settings.NativeFileCopyMode = NativeFileCopyModeEnum.CopyFiles;

     importJob.Settings.OverwriteMode = OverwriteModeEnum.Append;



     // Specify the ArtifactID of the document identifier field, such as a control number.

     importJob.Settings.IdentityFieldId = identifyFieldArtifactID;



     importJob.SourceData.SourceData = GetDocumentDataTable().CreateDataReader();



     Console.WriteLine("Executing import...");



     importJob.Execute();

}
```

The importJob.Settings.DataGridIDColumnName property is used on append and overlay to create a mapping between the document and the records in Data Grid when an external system, for example, Invariant already populated the Data Grid records and you want to share them with Relativity. For overlay, the GUID specified in the load file replaces the current mapping.

## Write messages and errors

You can use these methods to display messages about the status of an import job and any errors that may occur during it. The previous code sample uses these methods for capturing this information.

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
11
12
13
14
15

static void ImportJobOnMessage(Status status)

{

     Console.WriteLine("Message: {0}", status.Message);

}



static void ImportJobOnFatalException(JobReport jobReport)

{

     Console.WriteLine("Fatal Error: {0}", jobReport.FatalException);

}



static void ImportJobOnComplete(JobReport jobReport)

{

     Console.WriteLine("Job Finished With {0} Errors: ", jobReport.ErrorRowCount);

}
```

## Create a DataTable object for a document import job

You can create a DataTable object that includes metadata required to import documents to Relativity, such as an document identifier and a file path. The GetDocumentDataTable() method illustrates how to create and populate this table object, which is referenced in a previous code sample.

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
11
12
13
14

public static DataTable GetDocumentDataTable()

{

     DataTable table = new DataTable();



     // The document identifer column name must match the field name in the workspace.

     table.Columns.Add("Doc ID Beg", typeof(string));

     table.Columns.Add("Native File", typeof(string));

     table.Columns.Add("Parent Document ID", typeof(string));

     table.Rows.Add("video", "C:\\video.wmv", "");

     table.Rows.Add("text", "C:\\text.txt", "video");



     return table;

}
```

## Upload custom assemblies

In the Relativity, upload any custom assemblies for your application and the Import API assemblies as resource files. You must manually add the Import API assemblies in order for your custom application to function properly. For more information, see Resource files on the Relativity Documentation site.

On this page

- Import documents with native files

- Create a document import job

- Write messages and errors

- Create a DataTable object for a document import job

- Upload custom assemblies


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

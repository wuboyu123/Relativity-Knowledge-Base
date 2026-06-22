---
title: "Import produced images"
url: https://platform.relativity.com/Server2025/Content/Import_API/Getting_Started/Importing_produced_images.htm
collection: developer
fetched_at: 2026-06-22T06:29:53+00:00
sha256: a8470a8588fb0d927d7279edcf5fe591dfe3b99fe95d96c1161da6a14cb0ceb6
---

Import produced images

# Import produced images

You can add produced images to a production set in Relativity by using the methods available on the ImportAPI class.

On GitHub, you can find can comprehensive samples illustrating how to import native documents, images, objects, and productions. For additional code samples, see the Server Import API samples repository.

## Create a production import job

When importing produced images, you pass the ArtifactID of the target production set to the NewProductionImportJob() method on the ImportAPI class. You use a DataTable object as the data source for a production import job. This sample code illustrates how to perform these tasks, as well as references the following code samples that demonstrate how to write messages and create a DataTable object.

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
44
45
46
47

static void ImportProduction()

{

     Int32 workspaceArtifactID = 1015495;

     Int32 identityFieldArtifactID = 1003667;

     String productionSetName = "TestProduction";

     String relativityUserName = "<your Relativity username>";

     String relativityPassword = "<your password>";

     String relativityWebAPIUrl = "http://localhost/Relativitywebapi/";

     ImportAPI iapi = new ImportAPI(relativityUserName, relativityPassword, relativityWebAPIUrl);

     //Pass the ArtifactID of a workspace to retrieve a collection of production sets.

     var productionList = iapi.GetProductionSets(workspaceArtifactID);

     //Select a production. You add the production sets to this production.

     var desiredProduction = productionList.Single(p => p.Name.Equals(productionSetName, StringComparison.InvariantCultureIgnoreCase));

     var importJob = iapi.NewProductionImportJob(desiredProduction.ArtifactID);

     importJob.OnMessage += ImportJobOnMessage;

     importJob.OnComplete += ImportJobOnComplete;

     importJob.OnFatalException += ImportJobOnFatalException;

     //Specify the ArtifactID of the document identifier field, such as a control number.

     importJob.Settings.IdentityFieldId = identityFieldArtifactID;

     importJob.Settings.AutoNumberImages = false;

     // You can use the Bates number as an identifier for an image.

     importJob.Settings.BatesNumberField = "Bates";

     importJob.Settings.CaseArtifactId = workspaceArtifactID;

     // Use this code for grouping images associated with a document.

     importJob.Settings.DocumentIdentifierField = "Doc";

     importJob.Settings.ExtractedTextFieldContainsFilePath = false;

     // Indicates file path for an image.

     importJob.Settings.FileLocationField = "FileLoc";

     importJob.Settings.NativeFileCopyMode = NativeFileCopyModeEnum.CopyFiles;

     importJob.Settings.OverwriteMode = OverwriteModeEnum.Overlay;

     importJob.SourceData.SourceData = GetProductionDataTable();

     Console.WriteLine("Executing import...");

     importJob.Execute();

}
```

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

## Create a DataTable object for a production

You can create a DataTable object that includes metadata required to import images to Relativity, such as an identifier for associating images with a specific document, and a file path. The GetProductionDataTable() method illustrates how to create and populate this table object, which is referenced in a previous code sample.

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

public static DataTable GetProductionDataTable()

{

     DataTable table = new DataTable();

     // Column names don't need to correspond to field names.

     table.Columns.Add("Bates");

     table.Columns.Add("Doc", typeof(string));

     table.Columns.Add("FileLoc", typeof(string));

     //Group three images under A_1 document.

     table.Rows.Add("A_1", "A_1", "C:\\VOL01\\IMAGES\\IMG001\\Test000001.tif");

     table.Rows.Add("A_2", "A_1", "C:\\VOL01\\IMAGES\\IMG001\\Test000002.tif");

     table.Rows.Add("A_3", "A_1", "C:\\VOL01\\IMAGES\\IMG001\\Test000003.tif");

     //Group two images under B_1 document.

     table.Rows.Add("B_1", "B_1", "C:\\VOL01\\IMAGES\\IMG001\\SDF000001.tif");

     table.Rows.Add("B_2", "B_1", "C:\\VOL01\\IMAGES\\IMG001\\SDF000002.tif");

     return table;

}
```

The value of Bates field for the first image in a set must be identical to the value of document identifier (as shown in the code sample above). If you specify different values, no exception is thrown and no images are imported.

## Upload custom assemblies

In the Relativity, upload any custom assemblies for your application and the Import API assemblies as resource files. You must manually add the Import API assemblies in order for your custom application to function properly. For more information, see Resource files on the Relativity Documentation site.

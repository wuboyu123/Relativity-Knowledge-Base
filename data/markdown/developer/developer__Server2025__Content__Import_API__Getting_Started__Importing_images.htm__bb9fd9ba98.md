---
title: "Import images"
url: https://platform.relativity.com/Server2025/Content/Import_API/Getting_Started/Importing_images.htm
collection: developer
fetched_at: 2026-06-22T06:29:52+00:00
sha256: bfffaa80e44f80e210a0b9dfef7c21f8aa16dad25d63cf7e85446504390cb060
---

Import images Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Import images

You can use the Import API to add images to Relativity programmatically by using the methods available on the ImportAPI class.

On GitHub, you can find can comprehensive samples illustrating how to import native documents, images, objects, and productions. For additional code samples, see the Server Import API samples repository.

## Create an image import job

When you create an image import job, you instantiate the ImportAPI class and call its NewImageImportJob() method. You use a DataTable object as the data source for an image import job. This sample code illustrates how to perform these tasks, as well as references the following code samples that demonstrate how to write messages and create a DataTable object.

You can set the DestinationFolderArtifactID property to the ArtifactID of the folder used for an image import job. When it is set, the Import API imports all images in the job to the target folder. See Specify folders for import jobs .

Also note the use of ImportJob.Settings.OverwriteMode parameter to specify the mode for importing files. In this case the value is set AppendOverlay, meaning you import all files and update duplicates to the new version of the files. Setting the value to Append (import all files) can cause duplicates and import errors.

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

static void ImportImage()

{

     Int32 workspaceArtifactID = 1015495;

     Int32 identifyFieldArtifactID = 1003667;



     String relativityUserName = "<your Relativity username>";

     String relativityPassword = "<your password>";

     String relativityWebAPIUrl = "http://localhost/Relativitywebapi/";



     ImportAPI iapi = new ImportAPI(relativityUserName, relativityPassword, relativityWebAPIUrl);



     var importJob = iapi.NewImageImportJob();



     importJob.OnMessage += ImportJobOnMessage;

     importJob.OnComplete += ImportJobOnComplete;

     importJob.OnFatalException += ImportJobOnFatalException;



     importJob.Settings.AutoNumberImages = false;



     // You can use the Bates number as an identifier for an image.

     importJob.Settings.BatesNumberField = "Bates";

     importJob.Settings.CaseArtifactId = workspaceArtifactID;



      // Use this code for grouping images associated with a document.

     importJob.Settings.DocumentIdentifierField = "Doc";



     // Indicates filepath for an image.

     importJob.Settings.FileLocationField = "File";

     //Indicates that the images must be copied to the document repository

     importJob.Settings.CopyFilesToDocumentRepository = true;



     // Specifies the ArtifactID of a document identifier field, such as a control number.

     importJob.Settings.IdentityFieldId = identifyFieldArtifactID;

     importJob.Settings.OverwriteMode = OverwriteModeEnum.AppendOverlay;

     importJob.SourceData.SourceData = GetImageDataTable();



     Console.WriteLine("Executing import...");



     importJob.Execute();

     iapi = null;

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

## Create a DataTable object

You can create a DataTable object that includes metadata required to import images to Relativity, such as an identifier for associating images with a specific document, and a file path. The GetImageDataTable() method illustrates how to create and populate this table object, which is referenced in a previous sample code.

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

public static DataTable GetImageDataTable()

{

     DataTable table = new DataTable();



     // Column names don't need to correspond to field names.

     table.Columns.Add("Bates", typeof(string));

     table.Columns.Add("Doc", typeof(string));

     table.Columns.Add("File", typeof(string));



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

The value of Bates field for the first image in a set must be identical to the value of document identifier (for example, as shown in the code sample above). If you specify different values, no exception is thrown and no images are imported.

## Upload custom assemblies

In the Relativity, upload any custom assemblies for your application and the Import API assemblies as resource files. You must manually add the Import API assemblies in order for your custom application to function properly. For more information, see Resource files on the Relativity Documentation site.

On this page

- Import images

- Create an image import job

- Write messages and errors

- Create a DataTable object

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

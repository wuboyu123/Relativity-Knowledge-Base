---
title: "Import data into RDOs"
url: https://platform.relativity.com/Server2025/Content/Import_API/Getting_Started/Importing_data_into_RDOs.htm
collection: developer
fetched_at: 2026-06-22T06:29:50+00:00
sha256: 66bbfde2db201cc39e5db5f53adceefccd3e7bad351ece863289de842a45aea0
---

Import data into RDOs

# Import data into RDOs

You can use the Import API to import data programmatically into Relativity Dynamic Objects (RDOs) that already exist in a workspace. The ImportAPI class contains methods for this purpose.

On GitHub, you can find can comprehensive samples illustrating how to import native documents, images, objects, and productions. For additional code samples, see the Server Import API samples repository.

## Create an RDO import job

When importing RDOs to a workspace, you pass the ID of ArtifactType for the RDO to the GetUploadableArtifactTypes() on the ImportAPI class. You use a DataTable object as the data source for an RDO import job. This sample code illustrates how to perform these tasks, as well as references the following code samples that demonstrate how to write messages and create a DataTable object.

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

static void ImportObject()

{

     Int32 workspaceArtifactID = 1015495;

     Int32 identityFieldArtifactID = 1038772;

     String artifactTypeName = "TestObject";

     String relativityUserName = "<your Relativity username>";

     String relativityPassword = "<your password>";

     String relativityWebAPIUrl = "http://localhost/Relativitywebapi/";

     ImportAPI iapi = new ImportAPI(relativityUserName, relativityPassword, relativityWebAPIUrl);

     // Pass the ArtifactID of the workspace. You add your RDOs to this workspace.

     var artifactTypeList = iapi.GetUploadableArtifactTypes(workspaceArtifactID);

      // Use this code to choose type of object that you want to add.

     var desiredArtifactType = artifactTypeList.Single(at => at.Name.Equals(artifactTypeName));

     var importJob = iapi.NewObjectImportJob(desiredArtifactType.ID);

     importJob.OnComplete += ImportJobOnComplete;

     importJob.OnFatalException += ImportJobOnFatalException;

     // Use this setting for Name field of the object.

     importJob.Settings.SelectedIdentifierFieldName="Name";

     // Specifies the ArtifactID of a document identifier field, such as a control number.

     importJob.Settings.IdentityFieldId = identityFieldArtifactID;

     importJob.Settings.CaseArtifactId = workspaceArtifactID;

     importJob.Settings.OverwriteMode = OverwriteModeEnum.AppendOverlay;

     importJob.SourceData.SourceData = GetObjectDataTable().CreateDataReader();

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

## Create a DataTable object

You can create a DataTable object that includes the Field name of each RDO that you want to import to a workspace. The GetObjectDataTable() method illustrates how to create and populate this table object, which is referenced in a previous sample code .

Import only the columns that you need in any order.

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

public static DataTable GetObjectDataTable()

{

     DataTable table = new DataTable();

     // Column names must match the object field name in the workspace.

     table.Columns.Add("Name", typeof(string));

     table.Rows.Add("TestObject");

     return table;

}
```

## Upload custom assemblies

In the Relativity, upload any custom assemblies for your application and the Import API assemblies as resource files. You must manually add the Import API assemblies in order for your custom application to function properly. For more information, see Resource files on the Relativity Documentation site.

---
title: "ImportAPI class"
url: https://platform.relativity.com/Server2025/Content/Import_API/Overview/ImportAPI_class.htm
collection: developer
fetched_at: 2026-06-22T06:26:35+00:00
sha256: 31da350997dadae8f3774c8a9c0a95857b4ec1456b7a7f1196da63c7b6b2cef7
---

ImportAPI class

# ImportAPI class

The ImportAPI class is a top-level class that includes functionality for importing documents, images, production sets, and Relativity Dynamic Objects (RDOs). It includes methods for performing these import jobs, as well as other methods for retrieving Workspace, Field, and other objects. This class resides in the kCura.Relativity.ImportAPI namespace.

- The ImportAPI class isn't thread-safe. Attempting to use this object from multiple threads or tasks can lead to intermittent fatal exceptions.

- The Import API doesn't support long paths. For information about path support on Windows operating systems, see Maximum Path Length Limitation on the Microsoft website.

## Instantiate the ImportAPI class

The ImportAPI class includes overloaded constructors, which take a combination of authentication information and a web service URL. All of the services in the ImportAPI class require authentication, so it is performed when you instantiate the class. If authentication fails, an exception is thrown.

When developing custom applications using the Import API, call the CreateByRsaBearerToken() method to create the ImportAPI object. The RSA token is then automatically used for authentication. For sample code, see Bearer token authentication .

The following code sample illustrates how to create an instance of the ImportAPI class.

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

using kCura.Relativity.ImportAPI;

ImportAPI _importAPI = null;

try {

     _importAPI = new ImportAPI("relativity.username@relativity.com", "RelativityPassword");

} catch (Exception ex) {

     Console.WriteLine("Login Failure: {0}", ex.Message);

}
```

In addition, you can programmatically set a value for the web service URL, which the Import API uses to communicate with the Relativity WebAPI. For example, you could specify the location of the WebAPI using the following URL:

Copy

```text
1
2

https://relativity.relativity.com/relativitywebapi
```

If you don't specify the location of the WebAPI programmatically, the Import API attempts to resolve the server name by using the following process:

- Reads the WebServiceURL key set by an application in the local app.config file. See Optional app.config file . If this attempt fails, it checks the Windows Registry.

- Reads the location from Windows Registry set by the RelativityDesktop Client. If this attempt fails, the DataReaderClient generates an error.

The Windows registry key named WebServiceURL is of type REG_SZ and is located in the HKCU\Software\kCura\Relativity node.

In this code sample, an instance of the ImportAPI class is created by using the constructor that takes a username, password, and a web service URL.

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

using kCura.Relativity.ImportAPI;

ImportAPI _importAPI = null;

try {

     _importAPI = new ImportAPI("relativity.username@relativity.com", "RelativityPassword", "http://myServer.relativity.com/relativitywebapi/");

} catch (Exception ex) {

     Console.WriteLine("Login Failure: {0}", ex.Message);

}
```

## Use methods on the ImportAPI class

The ImportAPI class includes methods for retrieving Workspaces, Fields, ProductionSets, and other objects. It also includes methods for performing image, document, and production set import jobs. For more information, see the kCura.Relativity.ImportAPI Namespace in the Import API class library.

### Workspaces() method

The Workspaces() method returns an enumerable collection of Workspace objects containing all of the workspaces accessible to the current user. The Workspace class contains a variety of properties, including Name and ArtifactID as illustrated in the following code sample.

Copy

```text
1
2
3
4
5
6

IEnumerable<Workspace> workspaces = _importAPI.Workspaces();

foreach(Workspace ws in workspaces) {

     Console.WriteLine("Workspace: {0} ID: {1}", ws.Name, ws.ArtifactID);

}
```

### GetProductionSets() method

The GetProductionSets() method returns an enumerable collection of ProductionSet objects. Each object represents an existing production set available for use with an ImageImportBulkArtifactJob. This method returns only production sets that meet these requirements:

- The production set must be in staging and not have any existing documents added.

- The production set must be produced with the associated Imported field value set to Yes.

The following code sample illustrates how to use the GetProductionSets() method.

Copy

```text
1
2
3
4
5
6
7

const int myWorkspaceId = 1015024;

IEnumerable<ProductionSet> productionSets = _importAPI.GetProductionSets(myWorkspaceId);

foreach(ProductionSet production in productionSets) {

     Console.WriteLine("Production: {0} ID: {1}", production.Name, production.ArtifactID);

}
```

### GetWorkspaceFields() method

The GetWorkspaceFields() method takes a workspace ID and ArtifactTypeID. It returns an enumerable collection of Field objects, which represent mappable fields in a workspace for the specified ArtifactTypeID. The returned collection is identical to fields that the RelativityDesktop Client displays, with the addition of those fields with a FieldType of File. You can use all the returned Field objects with the Import API, except for fields with the FieldType of File. The RelativityServices API can be used to populate these fields.

The following code sample illustrates how to use the GetWorkspaceFields() method.

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

const int documentArtifactType = 10;

const int myWorkspaceId = 1015024;

IEnumerable<Field> fields = _importAPI.GetWorkspaceFields(myWorkspaceId, documentArtifactType);

foreach(Field field in fields) {

     Console.WriteLine("Field: {0} Category: {1}", field.Name, field.FieldCategory);

}
```

### NewImageImportJob() method

The NewImageImportJob() method returns an ImageImportBulkArtifactJob object that you can use for image imports. Since this job is already authenticated, it doesn't required a username and password in the job settings.

### NewNativeDocumentImportJob() method

The NewNativeDocumentImportJob() method returns an object used for importing native documents. Since this job is already authenticated, it doesn't required a username and password in the job settings.

### NewProductionImportJob() method

The NewProductionImportJob() method takes ArtifactID property from a ProductionSet object, which represents the destination production set in Relativity. It returns an ImageImportBulkArtifactJob object. This method also pre-populates the Settings.ForProduction, and Settings.ProductionArtifactID properties required for performing a production import. Use the GetProductionSets() method to retrieve the ArtifactID of the destination production set as illustrated in the following code sample.

Copy

```text
1
2
3
4
5
6

const int myWorkspaceId = 1015024;

IEnumerable<ProductionSet> productionSets = _importAPI.GetProductionSets(myWorkspaceId);

ProductionSet destinationProductionSet = productionSets.Single(p => p.Name.Equals("My Destination Production Set"));

ImageImportBulkArtifactJob productionJob = _importAPI.NewProductionImportJob(destinationProductionSet.ArtifactID)
```

### GetFileUploadMode() method

The GetFileUploadMode() takes an integer specifying the workspace ArtifactID, and returns an upload mode only applicable to this workspace. The mode is returned as an UploadTypeEnum enumeration with one of the following values:

- Web – indicates the standard mode, which uploads files through the web server.

- Direct – provides significantly faster uploads, and requires a connection to the network hosting the data. It also requires specific Windows group permissions. If an upload in this mode fails, the system reverts to Web mode.

### NewObjectImportJob() method

The NewObjectImportJob() method takes an ArtifactTypeID, and returns a new ImportBulkArtifactJob that it uses to import data into instances of an ArtifactType. Use the GetUploadableArtifactTypes() method to retrieve the required ArtifactType, and then pass the ArtifactType.ID property to the NewObjectImportJob() method. For more information, see the code sample for the GetUploadableArtifactTypes() method .

### GetUploadableArtifactTypes() method

The GetUploadableArtifactTypes() method takes an integer specifying the workspace ArtifactID. It returns an enumerable collection of ArtifactType objects applicable only to the current workspace. This collection represents only ArtifactTypeIDs that meet the following criteria:

- The object with the associated ArtifactTypeID can accept data.

- The authenticated user has permissions to upload to the object with the associated ID.

The following code sample illustrates how to use the GetUploadableArtifactTypes() method.

Copy

```text
1
2
3
4
5
6

const int myWorkspaceId = 1015024;

IEnumerable<ArtifactType> artifactTypes = _importAPI.GetUploadableArtifactTypes(myWorkspaceId);

ArtifactType desiredArtifactType = artifactTypes.Single(a => a.Name.Equals("My Custom Object Type"));

ImportBulkArtifactJob objectImportJob = _importAPI.NewObjectImportJob(desiredArtifactType.ID);
```

---
title: "Document Viewer Services (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Document_Viewer/Document_Viewer_Services_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:01+00:00
sha256: a1bda30387a4cdfcd5cc64df1978f02b42ef68c4ed9f1c7362106638a26c6f70
---

Document Viewer Services (.NET)

# Document Viewer Services (.NET)

The Document Viewer Services API provides functionality for requesting the conversion of documents to viewer types supported by Relativity, such as native, image, production, and transcript types. You can also convert files contained in File fields on a Relativity Dynamic Objects (RDOs). These files are converted to their native format on the fly, and then displayed in the standalone viewer.

The following sample use cases illustrate how you can use these cache entries to create custom viewers or workflows for displaying documents:

- Convert documents and save their locations in the cache. Next, create a custom application that retrieves native documents and displays them in a user-friendly format through a browser.

- Create a custom page or workflow that requests a document on-the-fly for immediate display in the viewer. Send a notification when the document is converted and available for viewing.

In addition, you can use the Document Viewer API through the REST API. For more information, see Document Viewer Services (REST) .

## Fundamentals for the Document Viewer Services API

Review the following information to learn about the methods, classes, and enumerations used by the Document Viewer Services API.

Methods

The Document Viewer Services API includes the following method available on the IDocumentViewerServiceManager interface in the Relativity.DocumentViewer.Services.Versioned.<VersionNumber> namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- GetViewerContentKeyAsync() method - sends a request to convert documents. It supports requests for native, image, production, and transcript conversion types. This method takes a GetViewerContentKeyRequest object that includes information about how to convert a document, such as its conversion type, priority, and other options. For on-the-fly requests, it returns a request key for documents that are currently undergoing conversion, and a cache entry ID for converted documents. See Convert documents and Convert files contained in File fields on RDOs .

Classes and enumerations

The Document Viewer Services API uses the following classes and enumerations:

- GetViewerContentKeyRequest class - represents a conversion request that is passed to the GetViewerContentKeyAsync() method. It includes properties for the conversion type, the priority of the request, the ID of the workspace containing documents for conversion, and the Artifact IDs of these documents. It also contains an Options property, which references a GetViewerContentKeyOptions object.

- GetViewerContentKeyOptions class - includes specialized conversion properties used for productions and mass conversions. It includes the ForceConversion property used to indicate that a previously converted document should be reconvert, and the ClientId used to indicate indicates the client ID of the application caller, such as DocumentViewer.Conversion.PreConvert. For File field conversion, you can set the FileId property, which provides the identifier for the RDO with an associated File field.

- ViewerContentKey class - represents a response from a conversion job. It contains a request key for documents that are currently undergoing conversion, and a cache entry ID for converted documents. An object of this type is returned by the GetViewerContentKeyAsync() method.

- ConversionType enumeration - indicates how the documents should be converted. It contains None, Native, Image, Production, and Transcript members.

- PriorityLevel enumeration - indicates the precedence of a conversion job. It contains None, OnTheFly, ConvertAhead, and MassConvert members.

## Best practices for the conversion requests

Use the following guidelines when calling the GetViewerContentKeyAsync() method:

- Import the Relativity.DocumentViewer.Services.V2 namespace by adding a using directive at the top of your class.

- Verify that you are passing valid parameters to it. If you pass an invalid workspace ID or other parameter, the service throws a ValidationException.

- For production conversions, set the ProductionId property on the Options property of the request object. See GetViewerContentKeyOptions class in Classes and enumerations .

- For mass conversions, you can create a mass operations resource table to store multiple document IDs. Include the name of the resource table on DocumentSetID property on the Options property of the request object. See GetViewerContentKeyOptions class in Classes and enumerations .

## Convert documents

Use the GetViewerContentKeyAsync() method to convert documents to native, image, production, or transcript type. You can obtain the request key for documents currently undergoing conversion from the ViewerContentKey object returned by this method. It also returns the cache entry ID for converted documents. For jobs with lower priorities, Relativity uses batching to pre-convert documents in a specific workspace.

The following code samples illustrates how to perform these general tasks:

- Use helper classes to create the proxy and select an appropriate authentication type. See Relativity API Helpers .

- Create the Services API proxy within a using block in your code.

- Create a GetViewerContentKeyRequest object.

- Call the GetViewerContentKeyAsync() method within a try-catch block.

- Use await/async design pattern.

- Use the logging framework for troubleshooting and debugging purposes. See Log from a Relativity application .

Convert documents to their native format

To convert documents to their native format on the fly, set the following properties on the GetViewerContentKeyRequest instance as follows:

- Set the ConversionType property to Native.

- Set the Priority property to OnTheFly.

Pass the request to the GetViewerContentKeyAsync() method.

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
public async Task<ViewerContentKey> GetViewerContentKeyAsync(int workspaceId, List<int> documentIds)

{

    ViewerContentKey viewerContentKey = null;

    using (IDocumentViewerServiceManager proxy = helper.GetServicesManager().CreateProxy<IDocumentViewerServiceManager>(ExecutionIdentity.CurrentUser))

    {

        GetViewerContentKeyOptions options = new GetViewerContentKeyOptions();

        options.ForceConversion = false;

        GetViewerContentKeyRequest request = new GetViewerContentKeyRequest();

        request.WorkspaceID = workspaceId;

        request.DocumentIDs = documentIds;

        request.ConversionType = ConversionType.Native;

        request.Priority = PriorityLevel.OnTheFly;

        request.Options = options;

        try

        {

            viewerContentKey = await proxy.GetViewerContentKeyAsync(request);

        }

        catch (Exception exception)

        {

            _logger.LogError(exception, "Document Viewer Service GetViewerContentKeyAsync call failed for Workspace ID {0}", workspaceId);

        }

    }

    return viewerContentKey;

}
```

Convert documents in a production set

To convert documents in a production set, implement your code as follows:

- On the GetViewerContentKeyOptions instance, set the ProductionId property to the Artifact ID of a production set.

- On the GetViewerContentKeyRequest instance, set the ConversionType property to Production.

Pass the request to the GetViewerContentKeyAsync() method.

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
public async Task GetViewerContentKeyAsync(int workspaceId, List<int> documentIds, int productionId)

{

    using (IDocumentViewerServiceManager proxy = helper.GetServicesManager().CreateProxy<IDocumentViewerServiceManager>(ExecutionIdentity.CurrentUser))

    {

        GetViewerContentKeyOptions options = new GetViewerContentKeyOptions();

        options.ForceConversion = false;

        options.ProductionID = productionId;

        GetViewerContentKeyRequest request = new GetViewerContentKeyRequest();

        request.WorkspaceID = workspaceId;

        request.DocumentIDs = documentIds;

        request.ConversionType = ConversionType.HTMLProduction;

        request.Priority = PriorityLevel.ConvertAhead;

        request.Options = options;

        try

        {

            await proxy.GetViewerContentKeyAsync(request);

        }

        catch (Exception exception)

        {

            _logger.LogError(exception, "Document Viewer Service GetViewerContentKeyAsync call failed for Workspace ID {0}", workspaceId);

        }

    }

}
```

Pre-convert images

To pre-convert images, implement your code as follows:

- On the GetViewerContentKeyOptions instance, set the DocumentSetId property to the name of an SQL table.

- On the GetViewerContentKeyRequest instance, set the ConversionType property to Image and the Priority property to MassConvert.

Pass the request to the GetViewerContentKeyAsync() method.

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
public async Task GetViewerContentKeyAsync(int workspaceId, string massOpTableDocumentSetId)

{

    using (IDocumentViewerServiceManager proxy = helper.GetServicesManager().CreateProxy<IDocumentViewerServiceManager>(ExecutionIdentity.CurrentUser))

    {

        GetViewerContentKeyOptions options = new GetViewerContentKeyOptions();

        options.ForceConversion = true;

        options.DocumentSetID = massOpTableDocumentSetId;

        GetViewerContentKeyRequest request = new GetViewerContentKeyRequest();

        request.WorkspaceID = workspaceId;

        request.ConversionType = ConversionType.HTMLImage;

        request.Priority = PriorityLevel.MassConvert;

        request.Options = options;

        try

        {

            await proxy.GetViewerContentKeyAsync(request);

        }

        catch (Exception exception)

        {

            _logger.LogError(exception, "Document Viewer Service GetViewerContentKeyAsync call failed for Workspace ID {0}", workspaceId);

        }

    }

}
```

## Convert files contained in File fields on RDOs

You can convert files contained in File fields on a Relativity Dynamic Objects (RDOs) for display in the standalone viewer. These files are converted to their native format on the fly.

Like document conversion, pass a GetViewerContentKeyRequest instance to the GetViewerContentKeyAsync() method. Follow these guidelines for setting properties on the GetViewerContentKeyRequest instance for converting File fields:

- Set the ConversionType property to Native.

- Set the Priority property set to OnTheFly.

- Optionally, set the FileId property on the GetViewerContentKeyOptions instance to the identifier for the RDO with the associated File field.

On the GetViewerContentKeyRequest instance, the DocumentIds property contains only the FieldArtifactID when it's used for converting a file contained in a File field.

You can obtain the request key for File fields currently undergoing conversion from the ViewerContentKey object returned by this method. It also returns the cache entry ID for converted files. For jobs with lower priorities, Relativity uses batching to pre-convert file fields in a specific workspace.

View code sample

The following code sample illustrates how to convert a file contained in a File field. For information about general tasks performed in this code, see Convert documents .

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
public async Task<ViewerContentKey> GetViewerContentKeyAsync(int workspaceId, List<int> documentIds, int? fileId = null)

{

    ViewerContentKey viewerContentKey = null;

    using (IDocumentViewerServiceManager proxy = helper.GetServicesManager().CreateProxy<IDocumentViewerServiceManager>(ExecutionIdentity.CurrentUser))

    {

        GetViewerContentKeyOptions options = new GetViewerContentKeyOptions();

        options.ForceConversion = false;

        options.FileID = fileId;

        GetViewerContentKeyRequest request = new GetViewerContentKeyRequest();

        request.WorkspaceID = workspaceId;

        request.DocumentIDs = documentIds;

        request.ConversionType = ConversionType.Native;

        request.Priority = PriorityLevel.OnTheFly;

        request.Options = options;

        try

        {

            viewerContentKey = await proxy.GetViewerContentKeyAsync(request);

        }

        catch (Exception exception)

        {

            _logger.LogError(exception, "Document Viewer Service GetViewerContentKeyAsync call failed for Workspace ID {0}", workspaceId);

        }

    }

    return viewerContentKey;

    }

}
```

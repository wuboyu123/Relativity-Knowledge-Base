---
title: "Document File Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Model/Document_File_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:24:18+00:00
sha256: 801e5621acf333f65a988bf1de004bd089502c8ffac2fb92bcdf42c4361be1ce
---

Document File Manager (REST)

# Document File Manager (REST)

The Document File Manager service exposes endpoints for downloading native, image, and produced image files associated with documents in Relativity. You can download a file by specifying its GUID, or you can download a native file by specifying the Artifact ID of the document associated with it. The Document File Manager service also supports retrieving file information, such as GUID, name, type, size, and others.

Sample use cases for the Document File Manager API include the implementing the following functionality:

- A custom agent that downloads native audio files, transcribes them, and writes the text back to Relativity.

- A custom page that displays the names, sizes, and types for a subset of documents.

You can also use the Document File Manager API through .NET. For more information, see Document File Manager (.NET) .

## Guidelines for the Document File Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to download a native file with the Artifact ID for a document:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/documents/{documentID}/native-file
```

Set the path parameters as follows:

- {versionNumber} to the version of the service, such as v1.

- {workspaceID} to the Artifact ID of the workspace containing the document.

- {documentID} to the Artifact ID of the document.

## Client code sample

You can use the following .NET code as a sample client for downloading a native file. This code illustrates how to perform the following tasks:

- Instantiate an HttpClient object for sending requests to the Document File Manager service.

- Set the required headers for the request.

- Initialize variables with the values for the workspace and document Artifact IDs.

- Set the url variable to the URL for downloading a native file.

- Use the GetAsync() method to send a GET request.

- Return the results of the request as a Stream object.

- Save the file on disk using the file name specified in the ContentDisposition header.

View code sample Copy

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
public static async Task DownloadAndSaveFileHttpExample()

{

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword!")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("https://localhost");

        int workspaceID = 1016883;

        int documentArtifactID = 1038029;

        string url = $"/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/documents/{documentArtifactID}/native-file";

        using (HttpResponseMessage response = await client.GetAsync(url))

        {

            response.EnsureSuccessStatusCode();

            using (Stream responseStream = await response.Content.ReadAsStreamAsync())

            using (Stream fileStream = File.Create($"C:\\RelativityDocuments\\{(response.Content.Headers.ContentDisposition.FileName).Replace("\"", "")}"))

            {

                await responseStream.CopyToAsync(fileStream);

            }

        }

    }

}
```

## Retrieve document file information

You can retrieve information about the files associated with a document, including the file name, GUID, page orientation and others.

To retrieve the file information for a document, you must have rights to view it in the workspace. Additionally, you must have access rights to view a production for its associated files to be include in the results.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/documents/{documentID}/file-info
```

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- Guid - a unique universal identifier for the file.

- Filename - the name of the file.

- Order - an integer value indicating the position of a file in a set of files with the same file type. Only OriginalImage and ProducedImage file types have a non-zero value for this field.

- FileType - the type of the file. It supports these types:

- Native

- OriginalImage

- ProducedImage

- PDF

- Size - the size of the file in bytes.

- Rotation - the orientation used to display the file. It supports these types:

- NotSet

- ZeroDegrees

- NinentyDegrees

- OneHundredEightyDegrees

- TwoHundredSeventyDegrees

The response contains arrays of the DocumentFile object.

View a sample JSON response Copy

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
[

  {

    "Guid": "d52141e9-8144-47af-b2f9-635045c313fc",

    "Filename": "MyDocument.docx",

    "Order": 0,

    "FileType": "Native",

    "Size": 20912,

    "Rotation": "NotSet"

  },

  {

    "Guid": "e03a9a5f-e398-46b2-a7d0-4c3ec1cd4541",

    "Filename": "MyDocument.tif",

    "Order": 0,

    "FileType": "OriginalImage",

    "Size": 944,

    "Rotation": "NinentyDegrees"

  },

  {

    "Guid": "e1fa1d9a-62c8-4826-a649-d6eb43c51210",

    "Filename": "placeholder.tif",

    "Order": 0,

    "FileType": "ProducedImage",

    "Size": 2417,

    "Rotation": "ZeroDegrees",

    "ProductionArtifactID": 1042144

  }

]
```

## Download files

You can download native, image, and produced image files associated with documents in Relativity using the following endpoints:

- DownloadFile - downloads the file based on a GUID that you specify. See Download a file by GUID .

- DownloadNativeFile - provides the same functionality as calling the DownloadFile endpoint with the GUID for a native file, except that you specify the Artifact ID of a document. See Download a native file by Document Artifact ID .

These endpoints return the binary data of a file.

The response contains these headers with the following settings:

- Transfer-Encoding - this heading is set to chunked.

- Content-Type - the extension of the file determines the value of this header.

- Content-Disposition - the name of the file as defined within Relativity determines the filename in attachment; filename= .

For native and image files, you must have permissions to the document in the workspace. For produced image files, you must have permissions to both the document and the production that includes the produced images.

### Download a file by GUID

You can download a native, image, or produced image file by specifying its GUID in a call to the DownloadFile endpoint. To obtain the GUID of a file for download, use the GetFileInfo endpoint. See Retrieve document file information .

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/documents/{fileGuid}/file
```

Set the path parameters as follows:

- {workspaceID} to the Artifact ID of the workspace containing the document.

- {fileGuid} to the GUID for the file, such as d6d94ed0-c46b-427d-b702-2682f1e43cf5.

The request body is empty.

When the request is successful, the response returns the status code of 200, and the file is saved to disk using the file name specified in the Content-Disposition header.

### Download a native file by Document Artifact ID

You can download a native file by specifying the Artifact ID of the document associated with it. This convenience endpoint functions similarly to calling the DownloadFile endpoint with the GUID for a native file, except that you specify the Artifact ID of a document.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/documents/{documentID}/native-file
```

The request body is empty.

When the request is successful, the response returns the status code of 200, and the file is saved to disk using the file name specified in the Content-Disposition header.

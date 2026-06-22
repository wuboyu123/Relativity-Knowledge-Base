---
title: "Document File Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Model/Document_File_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:16+00:00
sha256: 2b0e84ebb02231f915864679f12fbbca4995d43a529b4245f7f8746d58d24dd4
---

Document File Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Document File Manager (.NET)

The Document File Manager API exposes methods for downloading native, image, and produced image files associated with documents in Relativity. You can download a file by specifying its GUID, or you can download a native file by specifying the Artifact ID of the document associated with it. The Document File Manager API also supports retrieving file information, such as GUID, name, type, size, and others.

Sample use cases for the Document File Manager API include the implementing the following functionality:

- A custom agent that downloads native audio files, transcribes them, and writes the text back to Relativity.

- A custom page that displays the names, sizes, and types for a subset of documents.

You can also use the Document File Manager API through REST. For more information, see Document File Manager (REST) .

## Fundamentals for the Document File Manager API

Review the following information to learn about the methods, classes, and enumerations used by the Document File Manager API.

Methods

The Document File Manager API includes the following methods available on the IDocumentFileManager interface in the Relativity.ObjectModel.<VersionNumber>.Document namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- GetFileInfoAsync() method - retrieves information about the files associated with a document in Relativity. Its parameters include the Artifact IDs of a workspace and Document object. This method returns a list of DocumentFile objects. See Retrieve document file information .

You can download a native file by making a call to the DownloadNativeFileAsync() method and specifying the Artifact ID of the document associated with it. This convenience method functions similarly to calling the DownloadFile endpoint with the GUID for a native file, except that you specify the Artifact ID of a Document object.

- DownloadFileAsync() method - downloads a native, image, or produced image file based on the specified GUID. Its parameters include the Artifact ID of a workspace containing the document, and the GUID for the file to download. It returns a stream containing the file. See Download a file by GUID .

- DownloadNativeFileAsync() method - downloads a native file by specifying the Artifact ID of the Document object associated with it. Its parameters include the Artifact IDs of a workspace and Document object. It returns a stream containing the file. See Download a native file by Document Artifact ID .

Classes and enumerations

The Document File Manager API includes the following class and enumerations:

- DocumentFile class - represents information about a native, image, or produced image file.The GetFileInfoAsync() method returns an object of this type.

- Guid - a unique universal identifier for the file.

- Filename - the name of the file.

- Identifier - a unique string used to identify the file. The following sample JSON doesn't include this field.

- Order - an integer value indicating the position of a file in a set of files with the same file type. Only OriginalImage and ProducedImage file types have a non-zero value for this field.

- FileType - the type of the file. Set this property with a DocumentFileType enum.

- Size - the size of the file in bytes.

- Rotation - the orientation used to display the file. Set this property with a DocumentFileRotation enum.

- ProductionArtifactID - the Production Set ArtifactID associated with a produced image.

- DocumentFileType enum - indicates whether a document file type is of the native, original image, or produced image type. It supports these types:

- Native

- OriginalImage

- ProducedImage

- PDF

- DocumentFileRotation - provides set of valid rotation values for a document file. It supports these types:

- NotSet

- ZeroDegrees

- NinentyDegrees

- OneHundredEightyDegrees

- TwoHundredSeventyDegrees

## Retrieve document file information

You can retrieve information about the files associated with a document, including the including their file names, identifier, order, and others.

To retrieve the file information for a document, you must have permissions to view it in the workspace. Additionally, you must have access permissions to view a production for its associated files to be included in the results.

The following code sample illustrates how to pass the Artifact IDs of a workspace and Document object to the GetFileInfoAsync(). The method returns a list of DocumentFile objects, and the total count is written to the console.

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
public static async Task GetFileInfo()

 {

    int workspaceArtifactID = 1016883;

    int documentArtifactID = 1038018;

    ServiceFactory factory = Helper.GetServiceFactory();

    using (Relativity.ObjectModel.V1.Document.IDocumentFileManager documentFileManager = factory.CreateProxy<Relativity.ObjectModel.V1.Document.IDocumentFileManager>())

    {

        List<DocumentFile> documentFiles = await documentFileManager.GetFileInfoAsync(workspaceArtifactID, documentArtifactID);

        Console.WriteLine(documentFiles.Count);

    }

}
```

## Download files

You can download a native, image, or produced image file by specifying its GUID in a call to the DownloadFileAsync() method. To obtain the GUID of a file for download, use the GetFileInfoAsync() method.

The response contains these properties with the following settings for HTTP headers:

- ContentType - the extension of the file determines the value of this header.

- ContentDisposition - the name of the file as defined within Relativity determines the filename in attachment; filename= . See Download a file by GUID

For native and image files, you must have rights to the document in the workspace. For produced image files, you must have rights to both the document and the production that includes the produced images.

### Download a file by GUID

You can download a native, image, or produced image file by specifying its GUID in a call to the DownloadFileAsync() method. To obtain the GUID of a file for download, use the GetFileInfoAsync() method. See Retrieve document file information .

The following code sample illustrates how to pass the Artifact ID of a workspace and a GUID for a file to the DownloadFileAsync() method. This method returns a stream containing the file. It saves the file to disk using the file name specified in the ContentDisposition header.

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
public static async Task DownloadFile()

{

    int workspaceArtifactID = 1016883;

    Guid fileGuid = new System.Guid("d6d94ed0-c46b-427d-b702-2682f1e43cf5");

    ServiceFactory factory = Helper.GetServiceFactory();

    using (Relativity.ObjectModel.V1.Document.IDocumentFileManager documentFileManager = factory.CreateProxy<Relativity.ObjectModel.V1.Document.IDocumentFileManager>())

    using (IKeplerStream keplerStream = await documentFileManager.DownloadFileAsync(workspaceArtifactID, fileGuid))

    {

        System.Net.Http.Headers.ContentDispositionHeaderValue headerValue = System.Net.Http.Headers.ContentDispositionHeaderValue.Parse(keplerStream.ContentDisposition);

        string fileName = headerValue.FileName.Replace("\"", "");

        string fileDestination = @"C:\RelativityDocuments\" + fileName;

        using (Stream fileStream = await keplerStream.GetStreamAsync())

        using (Stream destinationStream = File.Create(fileDestination))

        {

            await fileStream.CopyToAsync(destinationStream);

        }

    }

}
```

### Download a native file by Document Artifact ID

You can download a native file by making a call to the DownloadNativeFileAsync() method and specifying the Artifact ID of the document associated with it. This convenience method functions similarly to calling the DownloadFile endpoint with the GUID for a native file, except that you specify the Artifact ID of a Document object.

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
public static async Task DownloadNativeFile()

{

    int workspaceArtifactID = 1016883;

    int documentArtifactID = 1037999;

    string fileDestination = @"C:\RelativityDocuments\mynativefile" + documentArtifactID;

    ServiceFactory factory = Helper.GetServiceFactory();

    using (Relativity.ObjectModel.V1.Document.IDocumentFileManager documentFileManager = factory.CreateProxy<Relativity.ObjectModel.V1.Document.IDocumentFileManager>())

    using (IKeplerStream keplerStream = await documentFileManager.DownloadNativeFileAsync(workspaceArtifactID, documentArtifactID))

    using (Stream fileStream = await keplerStream.GetStreamAsync())

    using (Stream destinationStream = File.Create(fileDestination))

    {

        await fileStream.CopyToAsync(destinationStream);

    }

}
```

On this page

- Document File Manager (.NET)

- Fundamentals for the Document File Manager API

- Retrieve document file information

- Download files

- Download a file by GUID

- Download a native file by Document Artifact ID


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

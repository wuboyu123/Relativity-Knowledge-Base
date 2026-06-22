---
title: "Resource File (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Resource_File_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:40+00:00
sha256: 409b843a6f27383a307876da6c8d84d69d5ca02a1acb7bd26cdd7b4c19594175
---

Resource File (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Resource File (.NET)

The Resource File API allows clients to manage resource files for the Relativity applications in the environment. It includes the following features:

- Supports create, read, update, delete and download resource files.

- Update/upload file content and metadata.

- Secondary methods allows the client to read all eligible applications.

You can also interact with the Resource File API through the REST API. See Resource File service .

## Guidelines for the Resource File API

Review the following guidelines for working with the Resource File API.

### Admin-level context

The value for the workspaceID parameter in the path should always be -1. Any other value will return an error.

### Sample use cases

The Resource File API can be used by R1 Operations or ISVs to manage third-party applications in their Relativity instances.

### Endpoints

The Resource File API includes the following endpoints. To set up a proxy to interact with the IResourceFile API, call the CreateProxy() method on the object returned by the GetServiceManager() method.

Create a proxy using CreateProxy() Copy

```text
1
2
3
4
5
6
7
Client.SamplesLibrary.Helper.IHelper helper;



// Create a proxy

using (IResourceFileManager ResourceFileManager= helper.GetServicesManager().CreateProxy<IResourceFileManager>(ExecutionIdentity.User))

{

    // Add your custom code ...

}
```

## CreateAsync

The following code samples illustrate how to use this endpoint to add/create new resource files in the environment.

### Permissions

The following permissions are required to call this endpoint:

- Instance - Object - Resource File - Create

- Instance - Object - Library Application - View

- Instance - Admin Operations - View Admin Repository

Create/Add new Resource File Copy

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
public async Task CreateAsync(ResourceFileRequest resourceFileRequest, string fileContent)

{

    byte[] contents = Encoding.UTF8.GetBytes(fileContent);

    MemoryStream memoryStream = new MemoryStream(contents)

    {

        Position = 0

    };

    KeplerStream keplerStream = new KeplerStream(memoryStream);



    try

    {

        ResourceFileResponse response = await ResourceFileManager.CreateAsync(resourceFileRequest, keplerStream);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Create/Add new Resource File with previously uploaded content Copy

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
public async Task CreateAsync(string fileName, string fileContent)

{

    ContentsResponse uploadContentsResponse = null;

    ResourceFileRequest request = new ResourceFileRequest

    {

        Application = TestAppIdentifier,

        FileName = fileName,

        Keywords = string.Empty,

        Notes = string.Empty

    };



    MemoryStream memoryStream = new MemoryStream(Encoding.UTF8.GetBytes(fileContent))

    {

        Position = 0

    };



    using (KeplerStream keplerStream = new KeplerStream(memoryStream))

    {

        //Upload Contents

        uploadContentsResponse = await ResourceFileManager.UploadContentsAsync(keplerStream, fileName);

    }



    //Create ResourceFile with uploaded contents

    try

    {

        ResourceFileResponse createResponse = await ResourceFileManager.CreateAsync(request, uploadContentsResponse.ContentsKey);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## ReadAsync

The following code sample illustrate how to use this endpoint to retrieve advanced metadata for a resource file, including its name, application, and other properties.

- IncludeMetadata - A Boolean value indicating whether to return extended resource file metadata in the response.

- IncludeActions - A Boolean value indicating whether to return a list of operations eligible to the current user of this resource file.

### Permissions

The following permissions are required to call this endpoint:

- Instance - Object - Resource File - View

- Instance - Admin Operations - View Admin Repository

Additional permissions are required to view the application name and consume the Edit and Delete actions:

- Instance - Object - Resource File - Delete

- Instance - Object - Resource File - Edit

- Instance - Object - Library Application - View

Read Resource File with resourceFileId Copy

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
public async Task ReadAsync(int resourceFileID, bool includeMetadata, bool includeActions )

{

    try

    {

        ResourceFileResponse response =

            await ResourceFileManager.ReadAsync(resourceFileID, includeMetadata, includeActions);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## UpdateAsync

The following code samples illustrate how to use this endpoint to allow the client to update/modify resource file metadata and file content.

### Permissions

The following permissions are required to call this endpoint:

- Instance - Object - Resource File - View

- Instance - Object - Resource File - Edit

- Instance - Admin Operations - View Admin Repository

Update Resource File metadata Copy

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
public async Task UpdateMetadataAsync(int resourceFileID, string keywords, string notes)

{

    ResourceFileResponse readResponse =

        await ResourceFileManager.ReadAsync(resourceFileID);

    readResponse.Keywords = keywords;

    readResponse.Notes = notes;



    try

    {

        ResourceFileResponse response =

            await ResourceFileManager.UpdateAsync(resourceFileID, readResponse);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Update Resource File contents Copy

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
public async Task UpdateContentsAsync(int resourceFileID, string  fileContent)

{

    byte[] contents = Encoding.UTF8.GetBytes(fileContent);

    MemoryStream memoryStream = new MemoryStream(contents)

    {

        Position = 0

    };



    KeplerStream keplerStream = new KeplerStream(memoryStream);



    try

    {

        ResourceFileResponse response =

            await ResourceFileManager.UpdateAsync(resourceFileID, keplerStream);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Update Resource File metadata and contents Copy

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
public async Task UpdateMetadataAndContentsAsync(string fileName, string fileContent, string keywords, string notes)

{

    ResourceFileRequest request = new ResourceFileRequest

    {

        Application = TestAppIdentifier,

        FileName = fileName,

        Keywords = string.Empty,

        Notes = string.Empty

    };

    request.Keywords = keywords;

    request.Notes = notes;



    MemoryStream memoryStream = new MemoryStream(Encoding.UTF8.GetBytes(fileContent))

    {

        Position = 0

    };

    KeplerStream stream = new KeplerStream(memoryStream);



    try

    {

        ResourceFileResponse response =

            await ResourceFileManager.UpdateAsync(TestAppIdentifier.ArtifactID, request, stream);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Update Resource File with last modified date Copy

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
public async Task UpdateContentsWithKeyAsync(int resourceFileID, string fileContent, DateTime lastModifiedOn)

{

    ContentsResponse uploadContentsResponse = null;



    ResourceFileResponse readResponse =

        await ResourceFileManager.ReadAsync(resourceFileID);



    MemoryStream memoryStream = new MemoryStream(Encoding.ASCII.GetBytes(fileContent))

    {

        Position = 0

    };



    using (KeplerStream keplerStream = new KeplerStream(memoryStream))

    {

        //Upload Contents

        uploadContentsResponse = await ResourceFileManager.UploadContentsAsync(keplerStream, readResponse.FileName);

    }



    try

    {

        ResourceFileResponse response =

            await ResourceFileManager.UpdateAsync(resourceFileID, readResponse, uploadContentsResponse.ContentsKey, lastModifiedOn);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

The following code samples illustrate how to use this endpoint to modify properties of a resource file using a previously uploaded contents. The contents must have been previously uploaded using the UploadContentsAsync endpoint.

Update Resource File with contents key Copy

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
public async Task UpdateMetadataAndContentsWithKeyAsync(string fileName, string fileContent, string keywords, string notes)

{

    ContentsResponse uploadContentsResponse = null;



    ResourceFileRequest request = new ResourceFileRequest

    {

        Application = TestAppIdentifier,

        FileName = fileName,

        Keywords = string.Empty,

        Notes = string.Empty

    };



    request.Keywords = keywords;

    request.Notes = notes;



    MemoryStream memoryStream = new MemoryStream(Encoding.ASCII.GetBytes(fileContent))

    {

        Position = 0

    };



    using (KeplerStream keplerStream = new KeplerStream(memoryStream))

    {

        //Upload Contents

        uploadContentsResponse = await ResourceFileManager.UploadContentsAsync(keplerStream, fileName);

    }



    try

    {

        ResourceFileResponse response =

            await ResourceFileManager.UpdateAsync(TestAppIdentifier.ArtifactID, request, uploadContentsResponse.ContentsKey);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Update Resource File with contents key and last modified date Copy

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
public async Task UpdateMetadataWithKeyAsync(int resourceFileID, string keywords, string notes, Guid contentsKey, DateTime lastModifiedOn)

{

    ResourceFileResponse readResponse =

        await ResourceFileManager.ReadAsync(resourceFileID);



    readResponse.Keywords = keywords;

    readResponse.Notes = notes;



    try

    {

        ResourceFileResponse response =

            await ResourceFileManager.UpdateAsync(resourceFileID, readResponse, contentsKey, lastModifiedOn);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## DeleteAsync

The following code samples illustrate how to use this endpoint to delete the Resource File.

### Permissions

The following permissions are required to call this endpoint:

- Instance - Object - Resource File - View

- Instance - Object - Resource File - Delete

- Instance - Admin Operations - View Admin Repository

Delete Resource File Copy

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
public async Task DeleteAsync(int resourceFileID)

{

    try

    {

        await ResourceFileManager.DeleteAsync(_resourceFile.ObjectIdentifier.ArtifactID);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## DownloadContentsAsync

The following code samples illustrate how to use this endpoint to download the contents associated with a resource file.

### Permissions

The following permissions are required to call this endpoint:

- Instance - Object - Resource File - View

- Instance - Admin Operations - View Admin Repository

Download the file contents Copy

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
public async Task DownloadContentsAsync(int resourceFileID)

{

    try

    {

        using (IKeplerStream stream =

            await ResourceFileManager.DownloadContentsAsync(_resourceFile.ObjectIdentifier.ArtifactID)) ;

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## UploadContentsAsync

The following code sample illustrate how to use this endpoint to upload the file contents. This endpoint is used in conjunction with CreateAsync and UpdateAsync to implement workflows where the file contents are uploaded before creating the resource file. The resource file is NOT created or updated until a subsequent call to CreateAsync or UpdateAsync.

### Permissions

The following permissions are required to call this endpoint:

- Instance - Object - Resource File - View

- Instance - Admin Operations - View Admin Repository

Upload the file contents Copy

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
public async Task UploadContentsAsync(IKeplerStream contents, string fileName)

{

    try

    {

        ContentsResponse response = await ResourceFileManager.UploadContentsAsync(contents, fileName);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## UpsertAsync

The following code samples illustrate how to use this endpoint to create a resource file if it doesn't exist or update properties of an existing resource file. The uniqueness of a resource file is determined by the combination of Application GUID and File Name.

### Permissions

The following permissions are required to call this endpoint:

- Instance - Object - Resource File - Create

- Instance - Object - Resource File - View

- Instance - Object - Resource File - Edit

- Instance - Object - Resource File - Delete

- Instance - Object - Library Application - View

- Instance - Admin Operations - View Admin Repository

Create or update Resource File Contents Copy

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
public async Task UpsertAsync_keplerStream(ObjectIdentifier applicationIdentifier, string fileName)

{

    string FileContents = "File content goes here ..";



    Stream stream = new MemoryStream(Encoding.ASCII.GetBytes(FileContents));

    KeplerStream keplerStream = new KeplerStream(stream);



    try

    {

        ResourceFileResponse response =

            await ResourceFileManager.UpsertAsync(applicationIdentifier, fileName, keplerStream);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

Create or update Resource File Contents with contents key Copy

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
public async Task UpsertAsync_ContentsKey(ObjectIdentifier applicationIdentifier, string fileName)

{

    string FileContents = "File content goes here ..";



    Guid ContentsKey = await UploadContentsAsync(FileContents);



    async Task<Guid> UploadContentsAsync(string fileContents)

    {

        using (Stream stream = new MemoryStream(Encoding.ASCII.GetBytes(fileContents)))

        using (KeplerStream keplerStream = new KeplerStream(stream))

        {

            ContentsResponse response = await ResourceFileManager.UploadContentsAsync(keplerStream, fileName);

            return response.ContentsKey;

        }

    }



    try

    {

        ResourceFileResponse response =

            await ResourceFileManager.UpsertAsync(applicationIdentifier, fileName, ContentsKey);

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## GetEligibleApplicationsAsync

The following code sample illustrate how to use this endpoint to retrieve a list of applications that can be associated to a resource file. It is used in the Relativity UI to populate a list for the user to choose from. The values returned in the list are subject to item-level security.

### Permissions

The following permissions are required to call this endpoint:

- Instance - Object - Library Application - View

- Instance - Admin Operations - View Admin Repository

GetEligibleApplications for new Resorce File Copy

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
public async Task GetEligibleApplicationsAsync()

{

    try

    {

        SecurableList<EligibleApplication> eligibleApps =

            await ResourceFileManager.GetEligibleApplicationsAsync();

    }

    catch (Exception ex)

    {

        string exception = $"An error occurred: {ex.Message}";

        Console.WriteLine(exception);

    }

}
```

## PushResourceFiles

The Push Resource File method allows callers to upload one or more resource files using local file paths.

PushResourceFilesAsync code sample Copy

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
public async Task  PushResourceFilesAsync()

{

    string[] resourceFileNames =

    {

        "PushResourceFiles.txt",

        "PushResourceFiles.xml",

        "PushResourceFiles.dll"

    };



    List<string> resourceFilePaths = resourceFileNames

        .Select(x => TestContext.CurrentContext.TestDirectory + @"\Environment\V1\ResourceFile\PushResourceFiles\" + x)

        .ToList();



    // The underlying implementation uses Upsert.  The following should create 3 new files.

    List<ResourceFileResponse> createResponses = await ResourceFileManager.PushResourceFilesAsync(TestAppIdentifier, resourceFilePaths);

}
```

On this page

- Resource File (.NET)

- Guidelines for the Resource File API

- Admin-level context

- Sample use cases

- Endpoints

- CreateAsync

- Permissions

- ReadAsync

- Permissions

- UpdateAsync

- Permissions

- DeleteAsync

- Permissions

- DownloadContentsAsync

- Permissions

- UploadContentsAsync

- Permissions

- UpsertAsync

- Permissions

- GetEligibleApplicationsAsync

- Permissions

- PushResourceFiles


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

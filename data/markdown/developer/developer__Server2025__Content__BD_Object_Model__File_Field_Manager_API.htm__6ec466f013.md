---
title: "File Field Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Model/File_Field_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:33+00:00
sha256: e3bcd155b2194e9d1ac3f00a7f59e62f3822a49b35b9f54a769dc6a190ec869f
---

File Field Manager (.NET)

# File Field Manager (.NET)

The File Field Manager API exposes a service for uploading and downloading files linked to file fields. For uploads, the overloaded UploadAsync() method supports the use of progress indicators and cancellation tokens.

As a sample use case, you might leverage this service to create a custom page with links for downloading files from Relativity.

You can also use File Field Manager API through REST. However, this service doesn't support cancellation tokens or progress indicators. For more information, see File Field Manager (REST) .

## File Field Manager API fundamentals

Review the following information to learn about the methods, classes, and enumerations used by the File Field Manager API.

Methods

The File Field Manager API includes the following methods available on the IFileFieldManager interface in the Relativity.ObjectModel.<VersionNumber>.File namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- DownloadAsync() method - downloads the contents of a file referenced by a file field in a specified workspace. See Downloading files from file fields .

- UploadAsync() method - uploads the contents of a file to temporary storage. This method returns a reference to the Field object linked to the uploaded file. You can optionally pass a progress indicator, or a progress indicator and a cancellation token to this overloaded method. See Uploading files to file fields .

Use an object of type System.IProgress or System.Threading.CancellationToken provided by the .NET framework for progress and cancellation functionality respectively.

Classes

The File Field Manager API includes the following classes:

- FileRequest class - represents a request for uploading or downloading a file.

- FileResponse class - represents the results of a download operation on a file.

## Sample workflow for file fields

The sample workflow outlines how you might use the Object Manager API in conjunction to the File Field Manager API to add files to Relativity:

- Load a sample file from disk into a Kepler stream.

- Upload a file as the value for the File field. Use the File Field Manager API to upload this file.

- Use the Object Manager API to update the object's File Field value.

After you upload a file to Relativity via the File Field Manager API, it is temporarily stored in the workspace's default file location until the RDO with the File field is saved. If the RDO with the File field and associated file are not saved, the server deletes it after about twenty-four hours based on the FileUploadExpirationHours instance setting.

## Downloading files from file fields

To download a file from a file field, pass the following arguments to the DownloadAsync() method:

- workspaceID - the Artifact ID of the workspace that contains the file field.

Set the {workspaceId} to -1 to indicate the admin-level context.

- fileRequest - an object that contains the data used to retrieve the file to be streamed.

The DownloadAsync() method returns an IKeplerStream that contains the content of the file.

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
public async Task<bool> DownloadAsync(IHelper helper)

{

    var objectArtifactId = this.SampleRDO_ID;

    var fieldArtifactId = this.SampleField_File_ID;

    var workspaceID = this.SampleWorkspace_ID;

    var relativityObject = new ObjectIdentifier

    {

        ArtifactID = objectArtifactId

    };

    var field = new FieldRef() { ArtifactID = fieldArtifactId };

    FileRequest request = new FileRequest()

    {

        Field = field,

        ObjectIdentifier = relativityObject

    };

    bool success = false;

    using (Relativity.ObjectModel.V1.File.IFileFieldManager proxy = helper.GetServicesManager().CreateProxy<Relativity.ObjectModel.V1.File.IFileFieldManager>(ExecutionIdentity.User))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", nameof(DownloadAsync), false);

        try

        {

            IKeplerStream stream = await proxy.DownloadAsync(workspaceID, request);

            Stream file = stream.GetStreamAsync().Result;

            success = stream.GetStreamAsync().Status == TaskStatus.RanToCompletion;

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

    }

    return success;

}
```

## Uploading files to file fields

To upload a file to a file field, pass the following arguments to the UploadAsync() method:

- workspaceID - the Artifact ID of the workspace that contains the file field.

Set the {workspaceId} to -1 to indicate the admin-level context.

- fileRequest - a request that contains the data used to retrieve the file to be streamed.

- file - a stream representing the content of the file.

You can also pass an optional progress indicator, or a progress indicator and a cancellation token to the UploadAsync() method.

The UploadAsync() method returns a FileResponse object that contains the name and GUID for the uploaded file.

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
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
public async Task<bool> UploadAsync(IHelper helper)

{

    var success = false;

    var objectArtifactId = this.SampleRDOList_IDs[0];

    var fieldArtifactId = this.SampleField_File_ID;

    var workspaceID = this.SampleWorkspace_ID;

    var fileName = "LoremIpsum.docx";

    var relativityObject = new ObjectIdentifier

    {

        ArtifactID = objectArtifactId

    };

    var field = new Relativity.Shared.V1.Models.FieldRef() { ArtifactID = fieldArtifactId, Name = fileName };

    var filePath = string.Format("{0}\\SampleFiles\\{1}", Directory.GetCurrentDirectory(), fileName);

    FileRequest request = new FileRequest()

    {

        Field = field,

        ObjectIdentifier = relativityObject,

        Filename = fileName

    };

    FileResponse uploadedFile = null;

    using (Relativity.ObjectModel.V1.File.IFileFieldManager proxy = helper.GetServicesManager().CreateProxy<Relativity.ObjectModel.V1.File.IFileFieldManager>(ExecutionIdentity.System))

    {

        Logging.ISampleLogger logger = _logger.ForContext("MethodName", nameof(UploadAsync), false);

        try

        {

            var keplerStream = new KeplerStream(File.OpenRead(filePath));

            uploadedFile = await proxy.UploadAsync(workspaceID, request, keplerStream);

        }

        catch (Exception ex)

        {

            logger.LogError(ex, "Unhandled Exception");

        }

    }

    if (uploadedFile?.UploadedFileGuid != null)

        using (IObjectManager objectManager = helper.GetServicesManager().CreateProxy<IObjectManager>(ExecutionIdentity.System))

        {

            var fieldValuePair = new FieldRefValuePair

            {

                Field = new Relativity.Services.Objects.DataContracts.FieldRef() { ArtifactID = fieldArtifactId, Name = fileName },

                Value = uploadedFile

            };

            var updateRequest = new UpdateRequest

            {

                Object = new RelativityObjectRef

                {

                    ArtifactID = objectArtifactId

                },

                FieldValues = new List<FieldRefValuePair> { fieldValuePair }

            };

            try

            {

                var result = await objectManager.UpdateAsync(workspaceID, updateRequest);

                return result.EventHandlerStatuses.TrueForAll(x => x.Success);

            }

            catch (Exception exception)

            {

                _logger.LogError(exception, "The Relativity Object is not valid for updating.");

            }

        }

    return success;

}
```

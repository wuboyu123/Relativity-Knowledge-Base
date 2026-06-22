---
title: "File Field Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Model/File_Field_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:24:36+00:00
sha256: 37955e863fb9b2e8d5d0a6133f79a58474fa454b9a4e6dfd604b32dd157f74c9
---

File Field Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# File Field Manager (REST)

The File Field Manager service includes endpoints for uploading and downloading files linked to file fields. As a sample use case, you might leverage this service to create a custom page with links for downloading files from Relativity.

You can also use the File Field Manager through .NET. It supports the use of progress indicators and cancellation tokens in .NET. For more information, see File Field Manager (.NET) .

## Guidelines for the File Field Manager service

Review the following guidelines for working with this service.

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the service. To download the sample file, click File Field Manager Postman file .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Client code sample

You can use the following .NET code as a sample client to download and save a file from a file field.

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
public static async Task DownloadAndSaveFileHttpExample()

{

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword!")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("https://localhost");

        int workspaceID = 1017660;

        int relativityObjectID = 104211;

        int fieldArtifactID = 1042124;



        string url = $"/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/files/download";

        string inputJSON = $@"{{""fileRequest"": {{""objectidentifier"": {{""ArtifactID"": {relativityObjectID}}},""field"": {{""ArtifactID"": {fieldArtifactID}}}}}}}";

        using (HttpResponseMessage response = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json")))

        {

            response.EnsureSuccessStatusCode();

            using (Stream responseStream = await response.Content.ReadAsStreamAsync())

            using (Stream fileStream = File.Create($"C:\\Temp\\{(response.Content.Headers.ContentDisposition.FileName).Replace("\"", "")}"))

            {

                await responseStream.CopyToAsync(fileStream);

            }

        }

    }

}
```

## Uploading files to file fields

To upload a file to a file field, use a URL with the following general format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceId}/files/upload
```

Set the {workspaceId} to -1 to indicate the admin-level context.

The request must include the following:

- FileRequest - contains the data required to upload a file from a file field.

- ObjectIdentifier - identifies the Relativity object, which will contain the uploaded file, by ArtifactID or GUID.

- ArtifactID - the Artifact ID of the object.

- Field - a reference to the field that you want associated with the uploaded file.

- ArtifactID - the Artifact ID of the field.

The request content is a bit stream representing the file that you are uploading. See the following sample JSON:

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
{

    "FileRequest": {

        "ObjectIdentifier": {

            "ArtifactID": 1234567

        },

        "field": {

            "ArtifactID": 5678912

        },

        "FileName": "SampleFile"

    }

}
```

The response contains the following fields:

- FileID - the file identifier. This value will always be 0 for any newly uploaded file.

- UploadedFileGuid - the GUID used to identify the uploaded file in temporary storage.

- Filename - the name of the file that you uploaded.

Copy

```text
1
2
3
4
5
{

    "FileID": 0,

    "Filename": "SampleFile",

    "UploadedFileGuid": "d5e48d89-c21f-44da-b2f5-717ae0e107b8"

}
```

## Downloading files from file fields

To download a file from a file field, use a URL with the following general format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceId}/files/download
```

Set the {workspaceId} to -1 to indicate the admin-level context.

The request must include the following:

- FileRequest - contains the data required to download a file from a file field.

- ObjectIdentifier - identifies the Relativity object, which contains the file being requested for download, by ArtifactID or GUID.

- ArtifactID - the Artifact ID of the object.

- Field - a reference to the field containing the file that you want to download.

- ArtifactID - the Artifact ID of the field.

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
{

    "FileRequest": {

        "ObjectIdentifier": {

            "ArtifactID": 1234567

        },

        "Field": {

            "ArtifactID": 5678912

        }

    }

}
```

The response is a bit stream representing the file that you are downloading.

On this page

- File Field Manager (REST)

- Guidelines for the File Field Manager service

- Postman sample file

- Client code sample

- Uploading files to file fields

- Downloading files from file fields


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

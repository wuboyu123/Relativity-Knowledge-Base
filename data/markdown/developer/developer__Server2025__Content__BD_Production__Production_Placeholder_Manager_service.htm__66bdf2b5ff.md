---
title: "Production Placeholder Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Production/Production_Placeholder_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:27:46+00:00
sha256: 58474fa5405f5c618d12bc228b64e07cbca5f68c0debafc6c942588303f54fe7
---

Production Placeholder Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Production Placeholder Manager (REST)

In Relativity, a placeholder is an image or custom text that you can add to a production. It may indicate that content is withheld due to privilege or it may contain additional information about a document. For general information, see Production placeholders on the Relativity Server 2025 Documentation site.

The Production Placeholder Manager API supports the following functionality:

- CRUD operations on placeholders

- Retrieving default field values for a placeholder

You can also use the Production Placeholder Manager API through .NET. For more information, see Production Placeholder Manager (.NET) .

See these related pages:

- Production

- Production Manager (REST)

- Production Data Source Manager (REST)

- Re-production Job Manager (REST)

- Production Queue Manager (REST)

## Guidelines for productions in REST

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

The following example illustrates how to set the path parameters when deleting a data source, but the same convention applies to all URLs in the Production APIs:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/production-data-sources/{DataSourceID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {WorkspaceID} to the Artifact ID of the workspace that contains the data source.

- {DataSourceID} to the Artifact ID of a specific data source.

## Create a placeholder

To add a new placeholder to Relativity, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/production-placeholders
```

View field descriptions for a request

The request must contain the following fields:

- placeholder - a ProductionPlaceholder object including the following fields:

- Name - a user-friendly name for the placeholder.

- ArtifactTypeID - the Relativity artifact type ID of the placeholder.

- PlaceholderType - the type of the placeholder. The PlaceholderType enumeration defined valid values for this property as follows:

- 0 - indicates custom text with formatting. If you set the PlaceholderType property to Custom, you must also set the CustomText property. You can create a blank placeholder by setting the CustomText property to an empty string. For more information, see Production Placeholder Manager (.NET) .

- 1 - indicates image files. Relativity supports TIF, JPEG, PNG, BMP, and GIF files. If you set the PlaceholderType property to Image, you must also set the FileData and Filename properties. The FileData property must contain raw Base64 encoded image data.

- FileData - the contents of the placeholder image.

- Filename - the file name of the placeholder image.

- FileSize - the size of the uploaded file.

- FileID - the internal identifier for the placeholder preview image.

- CustomText - the custom HTML text of the placeholder.

- Tokens - the JSON-encoded tokens for the placeholder.

View a sample JSON request Copy

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
{

    "placeholder":{

        "Name":"Test Placeholder",

        "ArtifactTypeID":1000035,

        "PlaceholderType":0,

        "FileData":"",

        "Filename":"",

        "FileSize":"",

        "FileID":"",

        "CustomText":"Hello",

        "Tokens":""

    }

}
```

When the placeholder is successfully created, the response contains its Artifact ID.

Copy

```text
1
1051085
```

## Retrieve a placeholder

To read a placeholder, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/production-placeholders/{PlaceholderID}
```

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- ArtifactTypeID - the Relativity artifact type ID of the placeholder.

- PlaceholderType - the type of the placeholder. The PlaceholderType enumeration defined valid values for this property as follows:

- 0 - indicates custom text with formatting.

- 1 - indicates image files.

- FileData - the contents of the placeholder image.

- Filename - the file name of the placeholder image.

- FileSize - the size of the uploaded file.

- FileID - the internal identifier for the placeholder preview image.

- CustomText - the custom HTML text of the placeholder when the PlaceholderType is Custom.

- ArtifactID - the Artifact ID of the placeholder.

- Name - a user-friendly name for the placeholder.

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
{

    "ArtifactTypeID": 1000035,

    "PlaceholderType": "Image",

    "FileData": "/9j/4AAQSkZJRgABAQEASABIAAD/4QBwRXhpZgAATU0AKgAAAAgABQMBAAUAAAABAAAASgMCAAIAAAAWAAAAUlEQAAEAAAABAQAAAFERAAQAAAABAAALE1ESAAQAAAABAAALEwAAAAAAAYagAuu0DYrO",

    "Filename": "Gipsy_Danger.jpg",

    "FileSize": 74304,

    "FileID": 7,

    "CustomText": "",

    "ArtifactID": 1045521,

    "Name": "Image Dummy"

}
```

## Update a placeholder

To modify a placeholder, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/reproduction-jobs/{ReproductionJobID}/stage-and-run
```

View field descriptions for a request

The request must contain the following fields:

- placeholder - a ProductionPlaceholder object including the following fields:

- ArtifactID - the Artifact ID of the placeholder.

- Name - a user-friendly name for the placeholder.

- ArtifactTypeID - the Relativity artifact type ID of the placeholder.

- PlaceholderType - the type of the placeholder. The PlaceholderType enumeration defined valid values for this property as follows:

- 0 - indicates custom text with formatting. If you set the PlaceholderType property to Custom, you must also set the CustomText property. You can create a blank placeholder by setting the CustomText property to an empty string. For more information, see Production Placeholder Manager (.NET) .

- 1 - indicates image files. Relativity supports TIF, JPEG, PNG, BMP, and GIF files. If you set the PlaceholderType property to Image, you must also set the FileData and Filename properties. The FileData property must contain raw Base64 encoded image data.

- FileData - the contents of the placeholder image.

- Filename - the file name of the placeholder image.

- FileSize - the size of the uploaded file.

- FileID - the internal identifier for the placeholder preview image.

- CustomText - the custom HTML text of the placeholder.

- Tokens - the JSON-encoded tokens for the placeholder.

View a sample JSON request Copy

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
{

    "placeholder":{

        "ArtifactID":1051085,

        "Name":"Test Placeholder",

        "ArtifactTypeID":1000035,

        "PlaceholderType":0,

        "FileData":"",

        "Filename":"",

        "FileSize":"",

        "FileID":"",

        "CustomText":"Hello World",

        "Tokens":""

    }

}
```

When the placeholder is successfully updated, the response returns a status code of 200.

## Delete a placeholder

To remove a placeholder from Relativity, send DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/production-placeholders/{PlaceholderID}
```

The request body is empty.

When the placeholder is successfully deleted, the response returns a status code of 200.

## Retrieve default field values for a placeholder

To retrieve default field values for a placeholder, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{workspaceID}/production-placeholders/defaults
```

This endpoint doesn't return empty or null fields.

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- field object - an object for each field associated with the data source. It contains the following fields:

- Guid - the GUID for the field.

- ID - the Artifact ID for the field.

- DefaultValue - depends on the field type. For example, a single choice field returns the Artifact ID of a choice for its default value.

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
{

    "Type": {

        "Guid": "31b6e843-c417-4930-94eb-61bb14a31666",

        "ID": 1038914,

        "DefaultValue": {

            "ID": 1038915,

            "Name": "Image"

        }

    }

}
```

On this page

- Production Placeholder Manager (REST)

- Guidelines for productions in REST

- URLs

- Create a placeholder

- Retrieve a placeholder

- Update a placeholder

- Delete a placeholder

- Retrieve default field values for a placeholder


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

---
title: "Production Data Source Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Production/Production_Data_Source_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:27:41+00:00
sha256: aa65a37f6971b85887dec2700fe7a23d574bc5360c439033cf68a06678799bb3
---

Production Data Source Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Production Data Source Manager (REST)

A production data source associates a production with a set of documents returned by a saved search. The save search is used to identify the documents to be produced for distribution to legal counsel. For general information, see Production data source on the Relativity Server 2025 Documentation site.

The Production Data Source Manager service supports the following functionality:

- CRUD operations on data sources

- Retrieving default field values for a data source

You can also use the Production Data Source Manager service through .NET. For more information, see Production Data Source Manager (.NET) .

See these related pages:

- Production

- Production Manager (REST)

- Production Placeholder Manager (REST)

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

## Create a data source

To create a data source, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/production-data-sources
```

View field descriptions for a request

The request must contain the following fields:

- datasource - includes the following fields:

- ArtifactTypeID - the Relativity artifact type ID of the data source.

- ProductionType - the type of production that applies to this data source. The ProductionType enumeration defines valid values for this property.

- SavedSearch - includes the following fields:

- ArtifactID - the Artifact ID of the saved search.

- Name - the user-friendly name of the saved search.

- UseImagePlaceholder - describes how to use the image placeholder as follows:

- NeverUseImagePlaceholder - never use image placeholder.

- AlwaysUseImagePlaceholder - always use the image placeholder, even if image exists.

- WhenNoImageExists - only use image placeholder when images don't exist.

- Placeholder - includes the following fields:

- ArtifactID - the Artifact ID of the placeholder.

- Name - the user-friendly name of the placeholder.

- MarkupSet - includes the following fields:

- ArtifactID - the Artifact ID of the markup set.

- Name - the user-friendly name of the markup set.

- BurnRedactions - a Boolean value indicating whether to burn redactions when producing image type productions.

- PlaceholderFilename - the name of the placeholder file.

- PlaceholderFileSize - an integer representing the size of the placeholder file.

- Name - the user-friendly name of the data source.

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
15
16
17
18
19
20
21
22
23
{

    "datasource":{

        "ArtifactTypeID": 1000034,

        "ProductionType": "ImagesOnly",

        "SavedSearch": {

            "ArtifactID": 1045335,

            "Name": "Beck's Search"

        },

        "UseImagePlaceholder": "WhenNoImageExists",

        "Placeholder": {

            "ArtifactID": 1045523,

            "Name": "Custom 1"

        },

        "MarkupSet": {

            "ArtifactID": 1034197,

            "Name": "Primary"

        },

        "BurnRedactions": true,

        "PlaceholderFilename": "",

        "PlaceholderFileSize": 0,

        "Name": "Data Test"

    }

}
```

The response contains the Artifact ID of the new data source.

Copy

```text
1
1051307
```

## Retrieve a data source

To read a data source, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/production-data-sources/{DataSourceID}?withPlaceholderImage={WithPlaceholderImage}}
```

You can pass an optional variable called withPlaceholderImage to return placeholder images for a data source as follows:

- withPlaceholderImage = true - populates values for read-only placeholder image properties on the data source. The placeholder image is available only for data sources with produced productions.

- withPlaceholderImage = false - doesn't populate any placeholder image properties. The default setting is false.

The request body is empty.

The response for a read operation contains the same fields as a request for a create operation. See the field descriptions in Create a data source . Additionally, the read response contains the Artifact ID of the data source.

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

    "ArtifactTypeID": 1000034,

    "ProductionType": "ImagesOnly",

    "SavedSearch": {

        "ArtifactID": 1045335,

        "Name": "Beck's Search"

    },

    "UseImagePlaceholder": "AlwaysUseImagePlaceholder",

    "Placeholder": {

        "ArtifactID": 1045546,

        "Name": "New Custom"

    },

    "MarkupSet": {

        "ArtifactID": 0,

        "Name": ""

    },

    "BurnRedactions": false,

    "PlaceholderFilename": "",

    "PlaceholderFileSize": 0,

    "ArtifactID": 1051307,

    "Name": "Data"

}
```

## Update a data source

To update a data source, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/production-data-sources
```

The request for an update operation contains the same fields as a request for a create operation. See the field descriptions in Create a data source . Additionally, the update request contains the Artifact ID of the data source.

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
{

    "datasource":{

        "ArtifactTypeID": 1000034,

        "ProductionType": "ImagesOnly",

        "SavedSearch": {

            "ArtifactID": 1045335,

            "Name": "Beck's Search"

        },

        "UseImagePlaceholder": "WhenNoImageExists",

        "Placeholder": {

            "ArtifactID": 1045523,

            "Name": "Custom 1"

        },

        "MarkupSet": {

            "ArtifactID": 1034197,

            "Name": "Primary"

        },

        "BurnRedactions": true,

        "PlaceholderFilename": "",

        "PlaceholderFileSize": 0,

        "ArtifactID": 1051307,

        "Name": "Data Test"

    }

}
```

When the data source is successfully updated, the response returns the status code of 200.

## Delete a data source

To delete a data source, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/production-data-sources/{DataSourceID}
```

The request body is empty.

When the data source is successfully deleted, the response returns the status code of 200.

## Retrieve default field values for a data source

To retrieve default field values for a data source, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{workspaceID}/production-data-sources/defaults
```

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- field object - an object for each field associated with the data source. In the sample JSON, these objects are UseImagePlaceholder and BurnRedactions.

- Guid - the GUID for the field

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
11
12
13
14
15
{

    "UseImagePlaceholder": {

        "Guid": "57c93e40-6b6c-4d76-b761-ef49ff3f0279",

        "ID": 1039203,

        "DefaultValue": {

            "ID": 1039206,

            "Name": "Never Use Image Placeholder"

        }

    },

    "BurnRedactions": {

        "Guid": "6a1b0978-634d-424b-af43-da3121d09112",

        "ID": 1038909,

        "DefaultValue": true

    }

}
```

On this page

- Production Data Source Manager (REST)

- Guidelines for productions in REST

- URLs

- Create a data source

- Retrieve a data source

- Update a data source

- Delete a data source

- Retrieve default field values for a data source


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

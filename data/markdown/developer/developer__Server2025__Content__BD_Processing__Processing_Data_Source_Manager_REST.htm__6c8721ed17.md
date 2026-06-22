---
title: "Processing Data Source Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Processing_Data_Source_Manager_REST.htm
collection: developer
fetched_at: 2026-06-22T06:27:26+00:00
sha256: 336bc236e061947eecff014dd157957f6dc4369789b7e9afdee28879b91c9790
---

Processing Data Source Manager (REST)

# Processing Data Source Manager (REST)

This topic describes the data-sources endpoint, which is used to access the Processing Data Source Manager service. The Processing Data Source Manager service supports read and save operations on data source objects.A data source contains the path used to specify the location of the files that you want to discover during processing. For more information, see Processing sets on the Relativity Documentation site.

See the topic Get started with the Processing API for general guidance on the Processing API, and links to documentation for the other interfaces and services in this API.

## Create a processing data source

To create a processing data source, send a POST request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/data-sources
```

Request Body Example

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
"processingDataSource":

    {

        "Custodian": 1085430,

        "DocumentNumberingPrefix":"test",

        "Order":100,

        "OcrLanguages":["English"],

        "DestinationFolder":1003697,

        "TimeZone":1037890,

        "InputPath":"/my/input/path",

        "ProcessingDataSourceID": 0,

        "Name":"testds",

        "ProcessingSet":{

            "ProcessingSetID": 1085429

        }

    }
```

The request must contain an InputPath field that specifies a file path, which the resource pool in the workspace can access. For more information, see Resource Pools on the Relativity Server 2025 Documentation site. It may also contain the StartNumber and IsStartNumberVisible properties.

The response returns the Artifact ID of the data source that was created or updated, such as the integer 1046822.

## Read a processing data source

To retrieve a processing data source, send a GET request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/data-sources/{your data source Artifact ID}
```

## Update a processing data source

To update a processing data source, send a PUT request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/data-sources/{your data source Artifact ID}
```

Request Body Example

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
"processingDataSource":

    {

        "Custodian": 1085430,

        "DocumentNumberingPrefix":"updated doc prefix",

        "Order":100,

        "OcrLanguages":["English"],

        "DestinationFolder":1003697,

        "TimeZone":1037890,

        "InputPath":"/my/input/path",

        "ProcessingDataSourceID": 0,

        "Name":"testds",

        "ProcessingSet":{

            "ProcessingSetID": 1085429

        }

    }

}
```

## Validate a processing data source for deletion

To check if the specified processing data source is safe to be deleted, send a GET request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/data-sources/{your data source Artifact ID}/delete-validation
```

The response includes the following fields:

- CanDelete – returns true if the data source can be deleted.

- Reasons – the reason(s) why the data source cannot be deleted. This will be empty if the data source is able to be deleted.

## Retrieve processing source location paths

To retrieve processing source location paths, send a GET request to the following URL

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/data-sources/source-location-paths
```

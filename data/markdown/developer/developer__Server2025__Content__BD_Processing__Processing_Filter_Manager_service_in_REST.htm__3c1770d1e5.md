---
title: "Processing Filter Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Processing_Filter_Manager_service_in_REST.htm
collection: developer
fetched_at: 2026-06-22T06:24:21+00:00
sha256: 461b06cc7114ef2644709e744284f958ef666b2e2b3b536e0fe5ed769d4fc278
---

Processing Filter Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing Filter Manager (REST)

Processing filters provide functionality to view and select processed documents before publishing them to Relativity. The Processing Filter Manager service exposes endpoints for programmatically creating, updating, and deleting filters. It supports applying these filters to data and retrieving the filtered data. Additionally, this service exposes helper endpoints for retrieving filters associated with a data source or available in a specific workspace. For more general information, see Filtering data .

As a sample use case, you may want to implement a simplified processing workflow by programmatically adding complex criteria to filters applied to processing jobs in Relativity. This approach eliminates the need to manually enter filter criteria through the UI, which may be time consuming and error prone. Similarly, you can also use the Processing Filter Manager service to modify the settings on these or other complex filters implemented in your environment.

The Processing Filter Manager service also supports the same functionality through .NET. For more information, see Processing Filter Manager .

## Client code sample

To use the Processing Filter Manager service, send an HTTP request to the target URL. Use PostAsync() for POST requests, GetAsync() for GET requests, and PutAsync() for PUT requests. You specify query conditions in the body of the request. See the base URL for this service:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/
```

You can use the following .NET code as a sample client for deleting a processing filter or for performing other operations. This code illustrates how to perform the following tasks:

- Instantiate an HttpClient object for sending requests to the Processing Filter Manager service.

- Set the required headers for the request. For information on setting headers, see HTTP headers .

- Set the url variable to the endpoint for deleting a processing filter. See Delete a processing filter .

- Set the JSON input required for the operation. The request for a delete operation requires the Artifact ID of a workspace and the identifier for a filter.

- Use the PostAsync() method to send a POST request.

- Return the results of the request and parse the JSON returned as the result.

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
30
31
32
33
34
35
public ProcessingFilterData GetFilterResult(int workspaceId, long filterID, int skip, int top)

{

    string endpoint = $"relativity-processing/v1/workspaces/{workspaceId}/filters/results/{filterID}?skip={skip}&top={top}";

    HttpResponseMessage response = SendProcessingKeplerGetRequest(endpoint);

    string responseContent = response.Content.ReadAsStringAsync().ConfigureAwait(false).GetAwaiter().GetResult();

    ProcessingFilterData filterData = JsonConvert.DeserializeObject<ProcessingFilterData>(responseContent);

    if (!response.IsSuccessStatusCode)

    {

        string genericErrorMessage = "Failed to get filter data.";

        throw ConstructHttpException(genericErrorMessage, response);

    }

    return filterData;

}

private HttpResponseMessage SendProcessingKeplerGetRequest(string apiEndpoint)

{

    string relativityRestApi = ExtensionPointServiceFinder.ServiceUriProvider.RestUri().AbsoluteUri;

    string fullEndpoint = $"{relativityRestApi}/{apiEndpoint}";

    HttpClient client = new HttpClient();

    Credentials credentials = new BearerTokenCredentials(ClaimsPrincipal.Current.Claims.AccessToken());

    string credentialParameter = credentials.GetAuthenticationHeaderValue().Replace("Bearer ", "");

    client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", credentialParameter);

    client.DefaultRequestHeaders.Add(“X-CSRF-Header”, "");

    return SendGetRequest(client, fullEndpoint);

}

private HttpResponseMessage SendGetRequest(HttpClient client, string fullEndpoint)

{

    HttpResponseMessage response = client.GetAsync(fullEndpoint).ConfigureAwait(false).GetAwaiter().GetResult();

    if (response.StatusCode == HttpStatusCode.NotFound)

    {

        throw new HttpException("Unable to complete GET Processing request, service is not up or unreachable.");

    }

    return response;

}
```

## Guidelines for the Processing Filter Manager service

Review the following guidelines for working with this service.

### Access rights

Verify that you have access to the workspace where you want make calls to the Processing Filter Manager service.

### Helper endpoints

Use the GetFiltersByDataSourceAsync or GetFiltersAsync helper endpoints to get the name, identifier, and type for a filter. See Retrieve processing filters and Retrieve processing filters for a data source .

### Filter expressions

To create or update a processing filter, use the expression types, operators, and properties supported by the Processing Filter Manager service for this purpose. For more information on objects used to build expressions, see Processing Filter Manager .

#### Expression types

The following types of expressions are supported:

- Composite expression - several shorter expressions that are combined by using the AND and OR operators. See Operators .

- Conditional expression - expressions that use Boolean conditions for evaluation. See Operators .

- Empty expression - an empty expression object used to create expressions. See Create a processing filter .

#### Operators

The following operators are supported in expressions:

- Constraint operators - Is, IsNot, IsIn, and IsNotIn.

- Composite operators - AND and OR.

#### Properties

Click the following drop-down link to view a list of properties supported for use in expressions.

- ContainerExtension

- ContainerFileId

- ContainerName

- DocumentError

- FileExtension

- FileName

- FileType

- IsDeleted

- OriginalPath

- ParentDocumentId

- ProcessingFileId

- ProcessingFolderPath

- SourcePath

- StorageError

- StorageId

- TextExtractionMethod

- VirtualPath

## Create a processing filter

Use the CreateExpressionFilterAsync endpoint to add a new processing filter to Relativity. Send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/filters
```

The body of the request must contain the following fields unless specifically identified as optional:

- request - represents a request to add a new processing filter to Relativity. It contains the following fields:

- FilterName - the user-friendly name of the filter.

- DataSourceArtifactIDs - an array of Artifact IDs for data sources to associate with the filter.

- Expression - the criteria used to select a subset of documents. The documents are filtered by this criteria. In this field, you set the type of expression (see Filter expressions ). For an empty expression, use \"Type\" : \"EmptyExpression\"

- IncludeFamily - a Boolean value indicating whether to include parent and child documents in the results of the filtering process.

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
{

    "request":

    {

        "FilterName" : "FileIdNot123",

        "DataSourceArtifactIds": [1042573],

        "Expression" : "{\"Type\":\"CompositeExpression\",\"Expressions\":[{\"Type\":\"ConditionalExpression\",\"Property\":\"IsDeleted\",\"Constraint\":\"Is\",\"Value\":false},{\"Type\":\"ConditionalExpression\",\"Property\":\"ProcessingFileId\",\"Constraint\":\"Is\",\"Value\":123}],\"Operator\":\"And\"}",

        "IncludeFamily": "true"

    }

}
```

The response contains the following fields:

- FilterId - the identifier assigned to a processing filter.

- FilterName - the user-friendly name of the processing filter.

- Type - indicates the filter type, such as an Expression filter.

Copy

```text
1
2
3
4
5
{

    "FilterId": 10,

    "FilterName": "FileIdNot1",

    "Type": "Expression"

}
```

## Apply a processing filter

To apply a filter to the documents in a data set, send a POST request to the following URL. The value for {your filter Artifact ID} is the identifier assigned to a processing filter. You obtain the identifier for a filter by calling the GetFilterByDataSourceAsync or GetFiltersAsync endpoints. See Retrieve processing filters or Retrieve processing filters for a data source .

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/filters/{your filter Artifact ID}/apply
```

The body of the request must contain the following fields unless specifically identified as optional:

- request - represents a request to apply a specific filter to a data set:

- Priority - an integer value indicating the precedence of the filtering job. Jobs with the lowest values are processed first.

Copy

```text
1
2
3
4
5
6
{

    "request":

    {

        "Priority" : 100

    }

}
```

When the request is successful, the response contains a value of type long, which is the ID for the job that was executed.

Copy

```text
1
2
3
{

    13242

}
```

## Update a processing filter

To modify a processing filter, send a PUT request to the following URL. The value for {your filter Artifact ID} is the identifier assigned to a processing filter. You obtain the identifier for a filter by calling the GetFilterByDataSourceAsync or GetFiltersAsync endpoints. See Retrieve processing filters or Retrieve processing filters for a data source .

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/filters/{your filter Artifact ID}
```

The body of the request must contain the following fields unless specifically identified as optional:

- request - represents a request to update a processing filter. It contains the following fields:

- FilterName - the user-friendly name of the filter.

- DataSourceArtifactIDs - an array of Artifact IDs for the data sources to associate with the filter.

- Expression - the criteria used to select a subset of documents. The documents are filtered by this criteria. In this field, you set the type of expression (see Filter expressions ). For an empty expression, use \"Type\" : \"EmptyExpression\"

- IncludeFamily - a Boolean value indicating whether to include parent and child documents in the results of the filtering process.

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
{

    "request":

    {

        "FilterName" : "FileIdNot123",

        "DataSourceArtifactIds": [1042573],

        "Expression" : "{\"Type\":\"CompositeExpression\",\"Expressions\":[{\"Type\":\"ConditionalExpression\",\"Property\":\"IsDeleted\",\"Constraint\":\"Is\",\"Value\":false},{\"Type\":\"ConditionalExpression\",\"Property\":\"ProcessingFileId\",\"Constraint\":\"Is\",\"Value\":123}],\"Operator\":\"And\"}",

        "IncludeFamily": "true"

    }

}
```

The response contains the following fields:

- FilterId - the identifier assigned to a processing filter.

- FilterName - the user-friendly name of the processing filter.

- Type - indicates the filter type, such as an Expression filter.

Copy

```text
1
2
3
4
5
{

    "FilterId": 3,

    "FilterName": "My Filtered Files",

    "Type": "Expression"

}
```

## Delete a processing filter

Use the DeleteFilterAsync endpoint to remove a filter from Relativity. Send a DELETE request to the following URL. The value for {your filter Artifact ID} is the identifier assigned to a processing filter. You obtain the identifier for a filter by calling the GetFilterByDataSourceAsync or GetFiltersAsync endpoints. See Retrieve processing filters or Retrieve processing filters for a data source .

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/filters/{your filter Artifact ID}
```

When the filter is successfully deleted, the response returns the status code of 200.

## Retrieve discovered documents

After you apply a processing filter, you can use the documents endpoint to retrieve the filtered discovered documents. Send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/filters/documents
```

The body of the request must contain the following fields unless specifically identified as optional:

- request - represents a request to retrieve filtered discovered documents. It contains the following fields:

- StartingPointOfResult - the index of the first row in the result set to return. The result set uses a zero-based index.

- NumberOfResults - the total number of rows in the result set to return. The value in the StartingPointOfResult field indicates the first row of the result set to return.

- Expression - the criteria used to select a subset of documents. The documents are filtered by this criteria. In this field, you set the type of expression, as indicated by \" Type \" : \" ConditionalExpression \". See Filter expressions .

Click the following drop-down link to view a table of constraint values supported based on data type.

- Constraint values

Columns marked with "Yes" are supported with mapped constraint. IsIn and IsNotIn constraints expect arrays.

Field

Is

IsNot

IsIn

IsNotIn

IsSet

IsNotSet

IsLike

IsNotLike

IsLessThan

IsLessThanOrEqualTo

IsGreaterThan

IsGreaterThanOrEqualTo

Boolean

ContainerExtension

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

ContainerID

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

ContainerName

CustodianArtifactId

Yes

Yes

Yes

Yes

DataSourceArtifactId

Yes

Yes

Yes

Yes

DiscoverGroupId

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

DocumentErrorMessage

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

ExtractedTextLocation

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

FileExtension

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

FileName

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

FileSize

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

FileType

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

FolderPath

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

ImportSource

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

IngestionError

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

IsContainer

Yes

Yes

Yes

Yes

Yes

Yes

IsEmbedded

Yes

Yes

Yes

Yes

Yes

Yes

LogicalPath

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

MD5Hash

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Numeric

OfficeEmbeddedItems

Yes

Yes

Yes

Yes

Yes

Yes

OriginalPath

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

ParentDocumentId

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

ProcessingFileId

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Rel Object

SHA1Hash

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

SHA256Hash

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

String

TextExtractionMethod

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

VirtualPath

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Unprocessable

Yes

Yes

Yes

Yes

Yes

Yes

- SortingOptions - the priority of sorting applied after retrieval of discovered documents. The array contains the following fields:

- Property - represents a sortable property of discovered documents. Available property values are listed in the constraint values table.

- Order - the method of sorting applied to discovered documents. The value can be Ascending or Descending.

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
{

    "request":

    {

        "StartingPointOfResult": 0,

        "NumberOfResults": 10, "Expression":"{\"Type\":\"CompositeExpression\",\"Expressions\":[{\"Type\":\"ConditionalExpression\",\"Property\":\"IsDeleted\",\"Constraint\":\"Is\",\"Value\":false},{\"Type\":\"ConditionalExpression\",\"Property\":\"ProcessingFileId\",\"Constraint\":\"Is\",\"Value\":123}],\"Operator\":\"And\"}",

        "ExcludeTotalCount":false,

        "SortingOptions":[]

    }

}
```

View the JSON response containing the filtered data Copy

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
{

    "FilterId": -1,

    "TotalCount": 11,

    "Results": [

        {

            "ContainerExtension": "",

            "ContainerID": 0,

            "ContainerName": "",

            "CustodianArtifactId": 1040723,

            "CustodianName": "Shah, Yash",

            "DataSourceArtifactId": 1040724,

            "DataSourceName": "Shah, Yash - 1040724",

            "DiscoverGroupId": 2,

            "DocumentErrorMessage": "",

            "ExtractedTextLocation": "",

            "FileExtension": "BIN",

            "FileName": "1.txt",

            "FileSize": 0,

            "FileType": "Empty zero byte file",

            "FolderPath": "",

            "ImportSource": "\\\\P-DV-VM-EVE7CUT\\processingsource\\1.txt",

            "IngestionError": "",

            "IsContainer": false,

            "IsEmbedded": false,

            "LogicalPath": "",

            "MD5Hash": "D41D8CD98F00B204E9800998ECF8427E",

            "OfficeEmbeddedItems": false,

            "OriginalPath": "",

            "ParentDocumentId": 0,

            "ProcessingFileId": 1,

            "SHA1Hash": "DA39A3EE5E6B4B0D3255BFEF95601890AFD80709",

            "SHA256Hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",

            "Unprocessable": true,

            "VirtualPath": ""

        },

        {

            "ContainerExtension": "7Z",

            "ContainerID": 2,

            "ContainerName": "10TextFiles_LZMA2Compression.7z",

            "CustodianArtifactId": 1040727,

            "CustodianName": "Regan, Robert",

            "DataSourceArtifactId": 1040728,

            "DataSourceName": "Regan, Robert - 1040728",

            "DiscoverGroupId": 9,

            "DocumentErrorMessage": "",

            "ExtractedTextLocation": "\\\\P-DV-VM-EVE7CUT\\fileshare\\EDDS1017804\\Processing\\1040728\\INV1017804\\INTERMEDIATE\\0\\3.TXT",

            "FileExtension": "TXT",

            "FileName": "TextFile1.txt",

            "FileSize": 6497,

            "FileType": "Text - Western European",

            "FolderPath": "10TextFiles_LZMA2Compression.7z\\10 Text Files",

            "ImportSource": "",

            "IngestionError": "",

            "IsContainer": false,

            "IsEmbedded": false,

            "LogicalPath": "10TextFiles_LZMA2Compression.7z\\10 Text Files",

            "MD5Hash": "B98A72D799731A07334D2EFF845F0D93",

            "OfficeEmbeddedItems": false,

            "OriginalPath": "",

            "ParentDocumentId": 2,

            "ProcessingFileId": 3,

            "SHA1Hash": "ACC7C604E020001C6F726CC19F8577891AF88CE4",

            "SHA256Hash": "75265C2E912D0882FB4BB7ABF60EA5DE60BB13568A2C3A4404CDC7C5B888C0A6",

            "TextExtractionMethod": "Native",

            "Unprocessable": false,

            "VirtualPath": "10TextFiles_LZMA2Compression.7z\\10 Text Files"

        }

    ]

}
```

## Retrieve filtered data

After you apply a processing filter, you can send a POST request to the following URL to retrieve the filtered data. The value for {your filter Artifact ID} is the identifier assigned to a processing filter. You obtain the identifier for a filter by calling the GetFilterByDataSourceAsync or GetFiltersAsync endpoints. See Retrieve processing filters or Retrieve processing filters for a data source .

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/filters/results/{your filter Artifact ID}?skip=0&top=10
```

View the JSON response containing the filtered data Copy

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
{

    "FilterId": 2,

    "TotalCount": 10,

    "Results": [

        {

            "ContainerExtension": "7Z",

            "ContainerID": 2,

            "ContainerName": "10TextFiles_LZMA2Compression.7z",

            "CustodianArtifactId": 1040727,

            "CustodianName": "Regan, Robert",

            "DataSourceArtifactId": 1040728,

            "DataSourceName": "Regan, Robert - 1040728",

            "DiscoverGroupId": 9,

            "DocumentErrorMessage": "",

            "ExtractedTextLocation": "\\\\P-DV-VM-EVE7CUT\\fileshare\\EDDS1017804\\Processing\\1040728\\INV1017804\\INTERMEDIATE\\0\\4.TXT",

            "FileExtension": "TXT",

            "FileName": "TextFile10.txt",

            "FileSize": 9113,

            "FileType": "Text - Western European",

            "FolderPath": "10TextFiles_LZMA2Compression.7z\\10 Text Files",

            "ImportSource": "",

            "IngestionError": "",

            "IsContainer": false,

            "IsEmbedded": false,

            "LogicalPath": "10TextFiles_LZMA2Compression.7z\\10 Text Files",

            "MD5Hash": "C61FAF7FE97EC3BE0A5B6FC50570CE8F",

            "OfficeEmbeddedItems": false,

            "OriginalPath": "",

            "ParentDocumentId": 2,

            "ProcessingFileId": 4,

            "SHA1Hash": "1E4E46F2D0D1A114F1F1E9FADC298DB5B1103B23",

            "SHA256Hash": "3D8B8B6B053B7B13F04A82E46A86CD72C9E6CBDE2D1519059DCD3D6BCB01FDDC",

            "TextExtractionMethod": "Native",

            "Unprocessable": false,

            "VirtualPath": "10TextFiles_LZMA2Compression.7z\\10 Text Files"

        },

        {

            "ContainerExtension": "7Z",

            "ContainerID": 2,

            "ContainerName": "10TextFiles_LZMA2Compression.7z",

            "CustodianArtifactId": 1040727,

            "CustodianName": "Regan, Robert",

            "DataSourceArtifactId": 1040728,

            "DataSourceName": "Regan, Robert - 1040728",

            "DiscoverGroupId": 9,

            "DocumentErrorMessage": "",

            "ExtractedTextLocation": "\\\\P-DV-VM-EVE7CUT\\fileshare\\EDDS1017804\\Processing\\1040728\\INV1017804\\INTERMEDIATE\\0\\5.TXT",

            "FileExtension": "TXT",

            "FileName": "TextFile2.txt",

            "FileSize": 4331,

            "FileType": "Text - Western European",

            "FolderPath": "10TextFiles_LZMA2Compression.7z\\10 Text Files",

            "ImportSource": "",

            "IngestionError": "",

            "IsContainer": false,

            "IsEmbedded": false,

            "LogicalPath": "10TextFiles_LZMA2Compression.7z\\10 Text Files",

            "MD5Hash": "BACD97CA8B90595FAB6350DFB7E8165A",

            "OfficeEmbeddedItems": false,

            "OriginalPath": "",

            "ParentDocumentId": 2,

            "ProcessingFileId": 5,

            "SHA1Hash": "DC9B65C5AEC375AFCCB2EF41653E084B62AFB6DA",

            "SHA256Hash": "4DE4A5ED7979900CBA63F50868AE2228B3036C54D7BE61EAB7E34FC538FCC945",

            "TextExtractionMethod": "Native",

            "Unprocessable": false,

            "VirtualPath": "10TextFiles_LZMA2Compression.7z\\10 Text Files"

        }

    ]

}
```

## Retrieve processing filters

You can retrieve processing filters for a data source by sending a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/filters
```

The response contains the following fields:

- FilterId - the identifier assigned to a processing filter.

- FilterName - the user-friendly name of the processing filter.

- Type - indicates the filter type, such as an Expression filter.

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
[

    {

        "FilterId": 2,

        "FilterName": "ConditionalTest",

        "Type": "Expression"

    },

    {

        "FilterId": 3,

        "FilterName": "Empty3files",

        "Type": "Expression"

    },

    {

        "FilterId": 1,

        "FilterName": "Emptyyy",

        "Type": "Expression"

    },

    {

        "FilterId": 6,

        "FilterName": "FileSizeGreaterThanBegins",

        "Type": "Expression"

    },

    {

        "FilterId": 5,

        "FilterName": "TextExtractionMethodBegins",

        "Type": "Expression"

    }

]
```

## Retrieve processing filters for a data source

You can retrieve processing filters for a data source by sending a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/filters/data-sources/{your data source Artifact ID}/filters
```

The response contains the following fields:

- FilterId - the identifier assigned to a processing filter.

- FilterName - the user-friendly name of the processing filter.

- Type - indicates the filter type, such as an Expression filter.

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
[

    {

        "FilterId": 2,

        "FilterName": "ConditionalTest",

        "Type": "Expression"

    },

    {

        "FilterId": 3,

        "FilterName": "Empty3files",

        "Type": "Expression"

    },

    {

        "FilterId": 6,

        "FilterName": "FileSizeGreaterThanBegins",

        "Type": "Expression"

    },

    {

        "FilterId": 5,

        "FilterName": "TextExtractionMethodBegins",

        "Type": "Expression"

    }

]
```

## Pivot on discovered documents

After you apply a processing filter, you can use the pivot-discovered-documents endpoint to retrieve filtered discovered documents on pivot. Send a POST request to the following URL:

Copy

```text
1
2
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/filters/pivot-discovered-documents<![CDATA[

]]>
```

The body of the request must contain the following fields unless specifically identified as optional:

- request - represents a request to retrieve processing filters for a data source. It contains the following fields:

- Expression - the criteria used to select a subset of documents. The documents are filtered by this criteria. In this field, you set the type of expression, as indicated by \" Type \" : \" ConditionalExpression \". See Filter expressions . Click the following drop-down link to view a table of constraint values supported based on data type.

- Constraint values

Columns marked with "Yes" are supported with mapped constraint. IsIn and IsNotIn constraints expect arrays.

Field

Is

IsNot

IsIn

IsNotIn

IsSet

IsNotSet

IsLike

IsNotLike

IsLessThan

IsLessThanOrEqualTo

IsGreaterThan

IsGreaterThanOrEqualTo

BeginsWith DoesNotBeginWith EndsWith DoesNotEndWith

Boolean

ContainerExtension

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

ContainerID

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

ContainerName

CustodianArtifactId

Yes

Yes

Yes

Yes

DataSourceArtifactId

Yes

Yes

Yes

Yes

DiscoverGroupId

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

DocumentErrorMessage

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

ExtractedTextLocation

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

FileExtension

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

FileName

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

FileSize

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

FileType

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

FolderPath

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

ImportSource

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

IngestionError

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

IsContainer

Yes

Yes

Yes

Yes

Yes

Yes

IsEmbedded

Yes

Yes

Yes

Yes

Yes

Yes

LogicalPath

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

MD5Hash

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

Numeric

OfficeEmbeddedItems

Yes

Yes

Yes

Yes

Yes

Yes

OriginalPath

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

ParentDocumentId

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

ProcessingFileId

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Rel Object

SHA1Hash

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

SHA256Hash

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

String

TextExtractionMethod

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

VirtualPath

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes

Yes Yes Yes Yes

Unprocessable

Yes

Yes

Yes

Yes

Yes

Yes

- PivotOnOption - the total number of rows in the result set to return. The value in the StartingPointOfResult field indicates the first row of the result set to return.

- GroupByProperty - the name of the property to perform group by on.

- GroupByOrdering - the method of sorting applied to the group by condition. The value can be Ascending (1) or Descending (0).

- GroupByCount - the integer value used to select the number of top or bottom rows to group by. The default value is 0.

- PivotOnProperty - (optional) the string representation of the property to perform pivot on.

- PivotOnOrdering - (optional) the method of sorting applied to the pivot on condition. The value can be Ascending (1) or Descending (0).

- PivotOnCount - (optional) the number of pivot results. The default value is 0.

Sample PivotOn request with conditional expression: Copy

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

    "request":

    {

"Expression":"{\"Type\":\"CompositeExpression\",\"Expressions\":[{\"Type\":\"ConditionalExpression\",\"Property\":\"IsDeleted\",\"Constraint\":\"Is\",\"Value\":false},{\"Type\":\"ConditionalExpression\",\"Property\":\"ProcessingFileId\",\"Constraint\":\"Is\",\"Value\":123}],\"Operator\":\"And\"}",

        "PivotOnOption":

        {

            "GroupByProperty": "ContainerID",

            "GroupByOrdering": "Ascending",

            "GroupByCount": "0",

            "PivotOnProperty": "CustodianArtifactID",

            "PivotOnOrdering": "Ascending",

            "PivotOnCount": "0"

        }

    }

}
```

When the request is successful, the response will return a List of GetDiscoveredDocumentsWithPivotOnResponse objects.

The response contains the following fields:

- GroupByIdentifier - the value of the property that is being grouped by.

- PivotOnIdentifier - the value of the property that is being pivoted on.

- ResultCount - the total of each property.

View the JSON response for a request without PivotOn fields populated Copy

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
[

    {

        "GroupByIdentifier": "Q1_Result",

        "PivotOnIdentifier": "",

        "ResultCount": 2

    },

    {

        "PropertyValue": "Q2_Result",

        "PivotOnIdentifier": "",

        "ResultCount": 4

    },

    {

        "PropertyValue": "Q3_Result",

        "PivotOnIdentifier": "",

        "ResultCount": 3

    }

]
```

View the JSON response for a request with PivotOn fields populated Copy

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
[

    {

        "GroupByIdentifier": "Q1_Result",

        "PivotOnIdentifier": "1",

        "ResultCount": 2

    },

    {

        "PropertyValue": "Q2_Result",

        "PivotOnIdentifier": "2",

        "ResultCount": 4

    },

    {

        "PropertyValue": "Q3_Result",

        "PivotOnIdentifier": "3",

        "ResultCount": 3

    }

]
```

## Get discovered documents IDs

You can retrieve discovered document IDs by sending a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/filters/document-ids
```

Request Body Sample

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
{

    "request":

    {

        "StartingPointOfResult": 0,

        "NumberOfResults": 10, "Expression":"{\"Type\":\"CompositeExpression\",\"Expressions\":[{\"Type\":\"ConditionalExpression\",\"Property\":\"IsDeleted\",\"Constraint\":\"Is\",\"Value\":false},{\"Type\":\"ConditionalExpression\",\"Property\":\"ProcessingFileId\",\"Constraint\":\"Is\",\"Value\":123}],\"Operator\":\"And\"}",

        "ExcludeTotalCount":false,

        "SortingOptions":[]

    }

}
```

## Prepare discovered documents list

Prepare discovered documents list by sending a POST request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/filters/csvs
```

Request Body Sample

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
"request":

    {

        "FileIDs":[1],

        "Expression":"",

        "Columns":[

            {

                "Property":"ProcessingFileId",

                "Header":"Id"

            }

        ],

        "SortingOptions":[]

    }
```

## Download discovered documents list

Download discovered documents list by sending a GET request to the following URL:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-processing/v1/workspaces/{your workspace id}/filters/csvs/{request GUID generated by prepare API}
```

On this page

- Processing Filter Manager (REST)

- Client code sample

- Guidelines for the Processing Filter Manager service

- Access rights

- Helper endpoints

- Filter expressions

- Create a processing filter

- Apply a processing filter

- Update a processing filter

- Delete a processing filter

- Retrieve discovered documents

- Retrieve filtered data

- Retrieve processing filters

- Retrieve processing filters for a data source

- Pivot on discovered documents

- Get discovered documents IDs

- Prepare discovered documents list

- Download discovered documents list


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

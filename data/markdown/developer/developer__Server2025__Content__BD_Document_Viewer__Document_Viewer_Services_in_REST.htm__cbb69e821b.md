---
title: "Document Viewer Services (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Document_Viewer/Document_Viewer_Services_in_REST.htm
collection: developer
fetched_at: 2026-06-22T06:24:02+00:00
sha256: c45da7bf45b57680ba2c5c7b0212bd91a8ac904eafc5ec9e405e33c50de33ae2
---

Document Viewer Services (REST)

# Document Viewer Services (REST)

The Document Viewer Services API provides functionality for requesting the conversion of documents to viewer types supported by Relativity, such as native, image, production, and transcript types. You can also convert files contained in File fields on a Relativity Dynamic Objects (RDOs). These files are converted to their native format on the fly, and then displayed in the standalone viewer.

The following sample use cases illustrate how you can use these cache entries to create custom viewers or workflows for displaying documents:

- Convert documents and save their locations in the cache. Next, create a custom application that retrieves native documents and displays them in a user-friendly format through a browser.

- Create a custom page or workflow that requests a document on the fly for immediate display in the viewer. Send a notification when the document is converted and available for viewing.

You can also use the Document Viewer Services through .NET. For more information, see Document Viewer Services (.NET) .

## Guidelines for using the Document Viewer Services

Review the following guidelines for working with the Document Viewer Services.

### URLs

The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set {versionNumber} to the version of the API, using the format lowercase v and the version number , such as v2 .

- Set other path parameters in the URLs to the Artifact ID of a given entity as necessary.

For example, you can use the following URL to convert documents in a workspace:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/viewer-content-key
```

Set the path parameter as follows:

- {versionNumber} to the version of the service, such as v2 .

For more information about this endpoint, see Convert documents .

## Client code samples

To use the Document Viewer Services, send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/viewer-content-key
```

The viewer-content-key endpoint supports different conversion types and priorities. You can use the following .NET code samples as REST clients for requesting conversions. They illustrate how to perform conversions for native formats, productions, and images with various priorities. Additionally, they all perform the following common tasks:

- Instantiate an HttpClient object for sending requests and responses using the URL for the Document Viewer Service.

- Set the required headers for the request.

- Set the BaseAddress variable to the Host Url.

- Set the string represented by parameters variable to the JSON input required to request a conversion.

- Use Newtonsoft to serialize the request object into JSON.

- Use the PostAsync() method to send a post request.

- Return the results of the request and deserialize it.

View sample code for requesting a conversion to a native format

This conversion request has the priority level set to OnTheFly, which indicates a high priority and is serviced before other requests.

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
36
37
ViewerContentKey viewerContentKey = null;

//Set up the client.

HttpClient httpClient = new System.Net.Http.HttpClient();

httpClient.BaseAddress = new Uri("http://localhost/");

//Set up the required headers.

httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

httpClient.DefaultRequestHeaders.Add("Authorization", "Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA");

//Set up the required parameters.

GetViewerContentKeyOptions options = new GetViewerContentKeyOptions();

options.ClientID = "Relativity.Documentation.Sample";

GetViewerContentKeyRequest parameters = new GetViewerContentKeyRequest();

parameters.WorkspaceID = 1015349;

parameters.DocumentIDs = new int[]{ 1015352 };

parameters.ConversionType = ConversionType.Native;

parameters.Priority = PriorityLevel.OnTheFly;

parameters.Options = options;

dynamic requestParameters = new ExpandoObject();

requestParameters.request = parameters;

string jsonParameters = Newtonsoft.Json.JsonConvert.SerializeObject(requestParameters);

System.Net.Http.StringContent parameterStringContent = new System.Net.Http.StringContent(jsonParameters, System.Text.Encoding.UTF8, "application/json");

//Make the HTTP request.

String dvsUrl = "Relativity.REST/api/relativity-documentViewer/v2/viewer-content-key";

HttpResponseMessage response = await httpClient.PostAsync(dvsUrl, parameterStringContent);

//Parse the result with Json.NET.

if (response.IsSuccessStatusCode)

{

     string json = await response.Content.ReadAsStringAsync();

     viewerContentKey = Newtonsoft.Json.JsonConvert.DeserializeObject<ViewerContentKey>(json);

}

     return viewerContentKey;
```

View sample code for requesting production conversion

This conversion request has the priority level set to ConvertAhead, which indicates a medium priority.

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
//Set up the client.

HttpClient httpClient = new System.Net.Http.HttpClient();

httpClient.BaseAddress = new Uri("http://localhost/");

//Set up the required headers.

httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

httpClient.DefaultRequestHeaders.Add("Authorization", "Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA");

//Set up the required parameters.

GetViewerContentKeyOptions options = new GetViewerContentKeyOptions();

options.ForceConversion = false;

options.ProductionId = 1015123;

options.ClientID = "Relativity.Documentation.Sample";

GetViewerContentKeyRequest parameters = new GetViewerContentKeyRequest();

parameters.WorkspaceID = 1015349;

parameters.DocumentIDs = new int[]{ 1015350, 1015351, 1015352 };

parameters.ConversionType = ConversionType.HtmlProduction;

parameters.Priority = PriorityLevel.ConvertAhead;

parameters.Options = options;

dynamic requestParameters = new ExpandoObject();

requestParameters.request = parameters;

string jsonParameters = Newtonsoft.Json.JsonConvert.SerializeObject(requestParameters);

System.Net.Http.StringContent parameterStringContent = new System.Net.Http.StringContent(jsonParameters, System.Text.Encoding.UTF8, "application/json");

//Make the HTTP request.

String dvsUrl = "Relativity.REST/api/relativity-documentViewer/v2/viewer-content-key";

HttpResponseMessage response = await httpClient.PostAsync(dvsUrl, parameterStringContent);

OpenView sample code for requesting an image conversion
```

View sample code for requesting an image conversion

This conversion request has the priority level set to MassConvert, which indicates a low priority.

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
//Set up the client.

HttpClient httpClient = new System.Net.Http.HttpClient();

httpClient.BaseAddress = new Uri("http://localhost/");

//Set up the required headers.

httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

httpClient.DefaultRequestHeaders.Add("Authorization", "Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA");

//Set up the required parameters.

GetViewerContentKeyOptions options = new GetViewerContentKeyOptions();

options.ForceConversion = true;

options.DocumentSetID = "c10478fc-b30e-4e13-a68b-d388938ef3b4";

options.ClientID = "Relativity.Documentation.Sample";

GetViewerContentKeyRequest parameters = new GetViewerContentKeyRequest();

parameters.WorkspaceID = 1015349;

parameters.ConversionType = ConversionType.HtmlImage;

parameters.Priority = PriorityLevel.MassConvert;

parameters.Options = options;

dynamic requestParameters = new ExpandoObject();

requestParameters.request = parameters;

string jsonParameters = Newtonsoft.Json.JsonConvert.SerializeObject(requestParameters);

System.Net.Http.StringContent parameterStringContent = new System.Net.Http.StringContent(jsonParameters, System.Text.Encoding.UTF8, "application/json");

//Make the HTTP request.

String dvsUrl =  "Relativity.REST/api/relativity-documentViewer/v2/viewer-content-key";

HttpResponseMessage response = await httpClient.PostAsync(dvsUrl, parameterStringContent);
```

## Convert documents

To convert documents in a workspace, send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/viewer-content-key
```

View field descriptions for a request

The following fields on the request object are required unless specifically identified as optional:

- WorkspaceID - the Artifact ID of the workspace that contains the documents for conversion.

- ConversionType - the output type for the documents undergoing conversion. The conversion types include Native, Image, Production, and Transcript. For general information about supported types, see Viewer on the Relativity Documentation site.

- DocumentIds - an array of Artifact IDs for the documents that you want to convert.

- Priority - the precedence of a conversion job. The priority levels from highest to lowest precedence include: OnTheFly, ConvertAhead, and MassConvert.

- Options - additional fields required for specific types of conversion jobs. These options include:

- ProductionID - the Artifact ID of a production set. This field is only required when the conversion type is Production.

- DocumentSetID - the name of an SQL table on the workspace database that contains the Artifact IDs of the documents that you want to convert. This field is only required when the conversion type is MassConvert.

- ForceConversion - a Boolean value indicating whether to reconvert a previously converted document. This field is only required when you want to reconvert documents. It must be set to true for this purpose.

- ClientID - a string value that indicates the client ID of the application caller. It is used to identify the usage of the Document Viewer Service. This field is required and must have a value. It must not be null or empty.

View a sample JSON for a native format request Copy

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

   "request":{

      "WorkspaceId":1015349,

      "ConversionType":"Native",

      "DocumentIds":[

         1015350

      ],

      "Priority":"OnTheFly",

      "Options":{

         "ClientId":"Relativity.Documentation.Sample"

      }

   }

}
```

View a sample JSON for a production request Copy

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
{

   "request":{

      "WorkspaceId":1015349,

      "ConversionType":"HtmlProduction",

      "DocumentIds":[

         1015350,

         1015351,

         1015352

      ],

      "Priority":"ConvertAhead",

      "Options":{

         "ProductionID":1015123,

         "ForceConversion":false,

         "ClientId":"Relativity.Documentation.Sample"

      }

   }

}
```

View a sample JSON for a mass image conversion request Copy

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
{

   "request":{

      "WorkspaceId":1015349,

      "ConversionType":"HtmlImage",

      "Priority":"MassConvert",

      "Options":{

         "DocumentSetId":"c10478fc-b30e-4e13-a68b-d388938ef3b4",

         "ForceConversion":true,

         "ClientID":"Relativity.Documentation.Sample"

      }

   }

}
```

View sample JSON responses

A conversion response includes a ViewerContentKey object. This object may contain the DocumentArtifactId, CacheEntryId, ConversionVersion, and RequestKey fields. For more information, see Document Viewer Services (.NET) .

If the document currently undergoing conversion, the JSON response contains the following fields:

- RequestKey - a unique value associated with a conversion request. You can use this field to track the progress of the conversion. If this property is set, SignalR sends a notification message after conversion has completed.

- DocumentArtifactId - the Artifact ID of a document that is undergoing conversion.

Copy

```text
1
2
3
4
{

   "RequestKey":"180eab41-2af8-48b6-b098-cb8746c140ea",

   "DocumentArtifactId":1015350

}
```

If the conversion of a document has completed, the JSON response contains the following fields:

- DocumentArtifactId - the Artifact ID of a document that has been converted and is available for retrieval.

- CacheEntryId - the identifier for the cached document. This field is only set when the document is available in the cache.

- ConversionVersion - the version number of the converted document.

Copy

```text
1
2
3
4
5
{

   "DocumentArtifactId":1015350,

   "CacheEntryId":40918,

   "ConversionVersion":"2017.3.3.13"

}
```

## Convert files contained in File fields on RDOs

You can convert a file contained in a File field on a Relativity Dynamic Object (RDO) for display in the standalone viewer. This file is converted to its native format. Like document conversion, this process uses the viewer-content-key endpoint.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/viewer-content-key
```

View field descriptions for a request

The following fields on the request object are required unless specifically identified as optional:

- WorkspaceID - the Artifact ID of the workspace that contains the file for conversion.

- ConversionType - the output type for the file undergoing conversion should always be set to Native.

- DocumentIds - an array containing one value, which is translated to the FieldArtifactId.

- Priority - the precedence of a conversion job. For File field conversion, this field must be set to OnTheFly.

- Options - additional fields required for specific types of conversion jobs. These options include:

- ForceConversion - a Boolean value indicating whether to reconvert a previously converted file. This field is only required when you want to reconvert files. It must be set to true for this purpose.

- FileID - the unique identifier for the RDO that the File field is associated with.

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

   "request":{

      "WorkspaceID":1018492,

      "DocumentIDs":[

         1038275

      ],

      "ConversionType":"Native",

      "Priority":"OnTheFly",

      "Options":{

         "ForceConversion":false,

         "FileID":1

      }

   }

}
```

The JSON responses for converting File fields contain the same fields as those returned for document conversion. See View sample JSON responses .

---
title: "Annotations Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Document_Viewer/Annotations_Manager__REST_.htm
collection: developer
fetched_at: 2026-06-22T06:22:36+00:00
sha256: 6086d2e5d66f8bb3f31ad3807fcbca9e01cd4d27502aec6adf82111525ab22c9
---

Annotations Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Annotations Manager (REST)

In Relativity, markups refer to redactions and highlights that you can add to document images as part of the review process in the Image Viewer. A redaction obscures confidential content in an image, while a highlight visually emphasizes content. You can define the colors and styles used to add markups to a document image. For more information, see ImageViewer and Markups in the Relativity Documentation site.

The Annotations Manager service exposes functionality for programmatically redacting and highlighting document images. It contains methods for creating, updating, retrieving, and deleting redactions and highlights.

As a sample use case, you might use the this service in application that provides custom functionality for adding redactions or highlights to document images. You might include the ability to delete multiple redactions in a single operation.

You can also use the Annotations Manager service through .NET. For more information, see Annotations Manager (.NET) .

The following content uses the term annotations to reference redactions or highlights added to document images through the Image Viewer.

## Guidelines for using the Annotations Manager service

Review the following guidelines for working with the Annotations Manager service.

### URLs

The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set {versionNumber} to the version of the API, using the format lowercase v and the version number , such as v2 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, such as {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

For example, you can use the following URL to retrieve an annotation:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspaces/{workspaceID}/annotations/{documentID}/{markUpSetID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the service, such as v2 .

- {workspaceID} to the Artifact ID of the workspace containing the document image.

- {documentID} to the Artifact ID of the document image.

- {markUpSetID} to the Artifact ID of the markup set used to add the annotation.

## Client code sample

To use the Annotations Manager service, send requests by making calls with the required HTTP methods. You can use the following .NET code as a sample client for retrieving annotations.

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
public async Task<string> GetAnnotations(int workspaceId, int documentId, int markupsetId)

{

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("<user login>:<user password>")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("http://localhost/");

        string url = $"/Relativity.rest/api/relativity-documentViewer/v2/workspaces/{workspaceId}/annotations/{documentId}/{markupsetId}";



        HttpResponseMessage response = await client.GetAsync(url);

        response.EnsureSuccessStatusCode();



        string content = await response.Content.ReadAsStringAsync();

        return content;

    }

}
```

## Create or update annotations

To create or update an annotation, send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/Relativity-DocumentViewer/{versionNumber}/workspaces/{workspaceID}/annotations/save
```

Set the ID property on each Annotation object when making an update request.

View field descriptions for a create or update request

The body of a request contains the following fields:

- BorderA - an integer representing the degree of transparency for the border color. This property can be null.

- BorderB - an integer representing blue in the RGB color model for the border. This property can be null.

- BorderG - an integer representing green in the RGB color model for the border. This property can be null.

- BorderR - an integer representing red in the RGB color model for the border. This property can be null.

- BorderSize - an integer representing the width of the border in pixels. This property can be null.

- BorderStyle - an integer representing the style of the border. This property can be null.

- DocumentArtifactID - the Artifact ID of the document.

- DrawCrossLines - a Boolean value indicating whether cross lines should be drawn.

- FillA - an integer representing the degree of transparency for the fill color. This property can be null.

- FillB - an integer representing blue in the RGB color model for the fill. This property can be null.

- FillG - an integer representing green in the RGB color model for the fill. This property can be null.

- FillR - an integer representing red in the RGB color model for the fill. This property can be null.

- FontA - an integer representing the degree of transparency for the font color. This property can be null.

- FontB - an integer representing blue in the RGB color model for the font. This property can be null.

- FontG - an integer representing green in the RGB color model for the font. This property can be null.

- FontR - an integer representing red in the RGB color model for the font. This property can be null.

- FontName - a string representing the name of the font.

- FontStyle - an integer representing the font style. This property can be null.

- FontSize - an integer indicating the font size in points. This property can be null.

- Guid - a string representing a GUID identifying the image.

- Height - an integer representing the height of a redaction in pixels.

- ID - integer IDs representing an annotation.

- ImageHeight - an integer indicating the image height in pixels.

- ImageWidth - an integer indicating the image width in pixels.

- PageHeight - an integer representing the page height in the Image Viewer.

- PageNumber - an integer representing the page number of a specific document image.

- PageWidth -an integer representing the page width in the Image Viewer.

- MarkupSetArtifactID - the Artifact ID of the markup set used to draw the annotations.

- MarkupSubType - an integer representing the subtype of the markup.

- MarkupType - an integer representing the type of markup.

- ModifiedBy - the Artifact ID for the user who last updated the annotation.

- Text - a string representing any text added to the annotation.

- ValuesAreScaledToDB - a Boolean value indicating whether values are scaled to the database.

- Width - an integer representing the width of a redaction in pixels.

- WorkspaceID - the Artifact ID of the workspace containing the image.

- X - a decimal representing the x-coordinate of the annotation.

- Y - a decimal representing the y-coordinate of the annotation.

- ZOrder - an integer representing the order of overlapping two-dimensional objects.

View a sample JSON request to create annotations Copy

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
{

    "annotations": [

        {

            "X": 52.983,

            "Y": 311.0057,

            "Width": 297,

            "Height": 112,

            "MarkupType": 2,

            "MarkupSubType": 7,

            "DrawCrossLines": false,

            "FillA": 0,

            "FillR": 128,

            "FillG": 255,

            "FillB": 128,

            "BorderStyle": 1,

            "BorderSize": 1,

            "Guid": "55081997-9cd1-4ac6-9d6a-fb6446048aa0",

            "PageNumber": 1,

            "PageHeight": 816,

            "PageWidth": 768,

            "ImageHeight": 1700,

            "ImageWidth": 1600,

            "WorkspaceID": 1970388,

            "DocumentArtifactID": 1038449,

            "MarkupSetArtifactID": 1034197

        }

    ]

}
```

View a sample JSON request to update annotations

Make sure that you set the ID property on each Annotation object when making an update request.

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
{

    "annotations": [

        {

            "ID": 3073,

            "X": 52.983,

            "Y": 311.0057,

            "Width": 297,

            "Height": 112,

            "MarkupType": 2,

            "MarkupSubType": 7,

            "DrawCrossLines": false,

            "FillA": 0,

            "FillR": 128,

            "FillG": 255,

            "FillB": 128,

            "BorderStyle": 1,

            "BorderSize": 1,

            "Guid": "55081997-9cd1-4ac6-9d6a-fb6446048aa0",

            "PageNumber": 1,

            "PageHeight": 816,

            "PageWidth": 768,

            "ImageHeight": 1700,

            "ImageWidth": 1600,

            "WorkspaceID": 1970388,

            "DocumentArtifactID": 1038449,

            "MarkupSetArtifactID": 1034197

        }

    ]

}
```

View field descriptions for a create and update response

The response contains the same fields for both create and update requests:

- AnnotationIDs - an array of integer IDs representing the annotations that were added or updated on a document.

- Success - a Boolean value indicating whether the annotation was created or updated without errors.

- ErrorCode - a string representing the error code returned when the create or update operation for an annotation fails.

View a sample JSON response Copy

```text
1
2
3
4
5
6
7
{

  "AnnotationIDs": [

    3073

  ],

  "Success": true,

  "ErrorCode": 0

}
```

## Retrieve annotations on a document

To retrieve an annotation, send a GET request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspaces/{workspaceID}/annotations/{documentID}/{markUpSetID}
```

The request body is empty.

The response for a get operation contains the same fields as those for a create or update request. See the field descriptions for the request in View field descriptions for a create or update request .

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
{

  "1": {

    "Annotations": [

      {

        "ID": 3072,

        "X": 81.2146,

        "Y": 162.5119,

        "PageNumber": 1,

        "Height": 995.8333,

        "Width": 327.0833,

        "MarkupType": 1,

        "MarkupSubType": 6,

        "DrawCrossLines": false,

        "FillA": 1,

        "FillR": 0,

        "FillG": 0,

        "FillB": 0,

        "ZOrder": -2147483648,

        "Text": "",

        "ImageWidth": 1600,

        "ImageHeight": 1700,

        "Guid": "55081997-9cd1-4ac6-9d6a-fb6446048aa0",

        "WorkspaceID": 0,

        "PageHeight": 0,

        "PageWidth": 0,

        "ValuesAreScaledToDB": false,

        "DocumentArtifactID": 0,

        "MarkupSetArtifactID": 1034197,

        "ModifiedBy": 0

      },

      {

        "ID": 3069,

        "X": 247.8812,

        "Y": 214.5952,

        "PageNumber": 1,

        "Height": 543.7500,

        "Width": 425.0000,

        "MarkupType": 2,

        "MarkupSubType": 11,

        "DrawCrossLines": false,

        "FillA": 110,

        "FillR": 162,

        "FillG": 0,

        "FillB": 255,

        "ZOrder": 0,

        "Text": "",

        "ImageWidth": 1600,

        "ImageHeight": 1700,

        "Guid": "55081997-9cd1-4ac6-9d6a-fb6446048aa0",

        "WorkspaceID": 0,

        "PageHeight": 0,

        "PageWidth": 0,

        "ValuesAreScaledToDB": false,

        "DocumentArtifactID": 0,

        "MarkupSetArtifactID": 1034197,

        "ModifiedBy": 0

      }

    ]

  }

}
```

## Delete annotations from a document

To remove annotations, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/relativity-documentViewer/{versionNumber}/workspaces/{workspaceID}/annotations/{documentID}/{markUpSetID}
```

View field descriptions for a delete request

The body of a request contains the following field:

- AnnotationIDs - an array of integer IDs representing the annotations that should be deleted.

View a sample JSON request to delete annotations Copy

```text
1
2
3
{

  "AnnotationIDs": [101, 202, 303]

}
```

When the annotations are successfully deleted, the response returns the status code of 200.

On this page

- Annotations Manager (REST)

- Guidelines for using the Annotations Manager service

- URLs

- Client code sample

- Create or update annotations

- Retrieve annotations on a document

- Delete annotations from a document


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

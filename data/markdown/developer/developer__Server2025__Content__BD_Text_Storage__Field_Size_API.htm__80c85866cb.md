---
title: "Field Size API"
url: https://platform.relativity.com/Server2025/Content/BD_Text_Storage/Field_Size_API.htm
collection: developer
fetched_at: 2026-06-22T06:30:48+00:00
sha256: a81227ae2573760ec3be0be07616bb094b514fdbcfafceb5c193d50ff5b86bb3
---

Field Size API

# Field Size API

When interacting with Relativity data, you can use the RESTful Text Field Size Service to return the size of text in any fixed length or long text field. The API returns the size of the text in UTF-16 bytes, and you don't have to retrieve the contents of the field to calculate it. For example, this functionality can be used to identify documents of certain size. You can use the API to interact with the text in both Data Grid and the Relativity SQL database.

## Service URL

To use the Structured Analytics Manager service, send an POST request to the following base URL:

Copy

```text
1
https://<relativity>/Relativity.Rest/api/kCura.DataGrid.Services.DataGridRecordManager.IDataGridRecordModule/Text%20Field%20Size%20Service/GetFieldSize
```

## Request headers

Like other Relativity REST APIs, the Text Field Size Service uses basic authorization.

You must also include the X-CSRF header and a content type of application/json .

Copy

```text
1
2
3
Authorization: Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA==

Content-Type: application/json

X-CSRF-Header: -
```

## Request body

The request body must include the following fields:

- workspaceArtifactId - the workspace containing the objects associated with the fields.

- objectArtifactIds - the artifact IDs of the objects associated with the fields, for example, documents or RDOs.

- fieldArtifactIds - the Artifact IDs of the fields.

- objectArtifactTypeId - the Artifact ID of the object type of the object associated with the fields. For example, 10 specifies a Document.

Copy

```text
1
2
3
4
5
6
{

    "workspaceArtifactId": 1708661,

    "objectArtifactIds": [1108195, 1108199],

    "fieldArtifactIds": [1003668,1038866],

    "objectArtifactTypeId": 10

}
```

## Response

A successful response returns a collection of objects representing field sizes with the following properties:

- ObjectArtifactId - The value of this property will be one of the values from request.objectArtifactIds

- FieldArtifactId - The value of this property will be one of the values from request.fieldArtifactIds

- ByteSize - The size, in bytes, of the UTF-16-encoded text. For example, the text "hello" is 10 bytes.

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

    "ObjectArtifactId": 1108195,

    "FieldArtifactId": 1003668,

    "ByteSize": 2634

  },

  {

    "ObjectArtifactId": 1108199,

    "FieldArtifactId": 1003668,

    "ByteSize": 80928

  },

  {

    "ObjectArtifactId": 1108195,

    "FieldArtifactId": 1038866,

    "ByteSize": 1

  },

  {

    "ObjectArtifactId": 1108199,

    "FieldArtifactId": 1038866,

    "ByteSize": 1

  }

]
```

All success responses will have an HTTP 200 response code.

## Error handling

### HTTP return code

Most Text Field Size Service errors produce an HTTP 400 response code caused by invalid data passed in by the client.

Certain request can produce an HTTP 500 response code caused by the server error.

Both 400 and 500 error types are fatal and should not be retried.

### Error message

The error response includes an error type and a detailed message, for example:

Copy

```text
1
2
3
4
{

  "ErrorType": "kCura.DataGrid.Services.Interfaces.DataGrid.Exceptions.FieldMissingException",

  "Message": "Certain requested fields do not exist"

}
```

### Error types

The Text Field Size Service error types are as follows:

- kCura.DataGrid.Services.Interfaces.DataGrid.Exceptions.FieldMissingException - A requested field could not be found.

- kCura.DataGrid.Services.Interfaces.DataGrid.Exceptions.MissingObjectException - A requested object could not be found.

- kCura.DataGrid.Services.Interfaces.DataGrid.Exceptions.ObjectCountException - Too many objects or fields have been requested. Split into multiple requests.

- kCura.DataGrid.Services.Interfaces.DataGrid.Exceptions.WorkspaceMissingException - The requested workspace does not exist.

- kCura.DataGrid.Services.Interfaces.DataGrid.Exceptions.UnsupportedFieldException - A requested field is not a text field.

For security reasons, there is no visible difference between an item being missing and an item being secured from the user by permissions.

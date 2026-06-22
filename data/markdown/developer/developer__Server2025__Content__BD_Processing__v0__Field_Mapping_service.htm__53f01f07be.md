---
title: "Field Mapping (REST v0)"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/v0/Field_Mapping_service.htm
collection: developer
fetched_at: 2026-06-22T06:30:33+00:00
sha256: 4d7236cc3699c174b695d2957bb289e92974f0f58124b047452eeea827c69a99
---

Field Mapping (REST v0) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Field Mapping (REST v0)

This content refers to Version 0 of the Processing APIs. For documentation on the latest version of this API, see Get started with the Processing SDK

The Field Mapping service available in the REST API supports multiple operations required to map fields in Relativity to fields in an external data source. You can use this service to retrieve a list of fields that are available for mapping from an external data source, and to retrieve a list of fields in Relativity that are already mapped. Additionally, you can use it to update and read existing field mappings.

Currently, this service supports only managing the mappings between fields in Relativity and Invariant. This functionality supports the processing feature available in Relativity. For more information, see Processing on the Relativity Documentation site.

For example, you can use this service to populate a custom dialog in your application with fields for available for mapping.

The Relativity Services API also provides functionality for mapping fields from Invariant to those in Relativity. For more information, see Field Mapping Manager .

## Client code sample

You interact with the Field Mapping service by sending an HTTP request that uses the POST method. You specify query conditions in the body of the request. See the base URL for this service:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.Services.FieldMapping.IFieldMappingModule/FieldMappingService/
```

You can use the following .NET code as the REST client for executing field mapping calls. The code illustrates how to perform the following tasks:

- Instantiate an HttpClient object for sending requests and responses using the URL for the Field Mapping service.

- Set the required headers for the request.

- Set the url variable to the URL for the operation that you want to perform.

- Set the string represented by payload variable to the JSON input required for your operation.

- Use the PostAsJsonAsync() method to send a post request.

- Return the results of the request.

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
public async Task<MappableSourceField[]> GetMappableFields()

{

    Task<MappableSourceField[]> result = null;

    using (HttpClient httpClient = new HttpClient())

    {



        httpClient.BaseAddress = new Uri("http://localhost/relativity.rest/api/Relativity.Services.FieldMapping.IFieldMapping/");



        //Set the required headers.

        httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        httpClient.DefaultRequestHeaders.Add("Authorization", "Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA==");



        string url = " GetInvariantFieldsAsync ";



        int workspaceArtifactId = 1234567;

        bool catalogFieldsOnly = true;



        var payload = @"{

                    workspaceArtifactID:{0},

                    catalogFieldsOnly:{1}

}";



        result = await httpClient.PostAsJsonAsync(url, string.Format(workspaceArtifactId, catalogFieldsOnly);

    }

    return result;

}
```

## Check field mapping availability

Before attempting to map fields, you can make a REST API call that checks for the availability of an external data source.

The Field Mapping service currently only supports field mapping between Invariant and Relativity. You can use the IsFieldMappingAvailableAsync() method on the service to confirm that Invariant is running.

To check data source availability, send a request to this URL for the Field Mapping service:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.Services.FieldMapping.IFieldMappingModule/FieldMappingService/IsFieldMappingAvailableAsync
```

The request must have the Artifact ID of the workspace where you want to map fields.

Copy

```text
1
2
3
{

    "workspaceArtifactId":1046331

}
```

The response contains a value of true or false. When this method returns false, your data source isn't currently available. You may want to contact your system admin to troubleshoot this issue.

## Retrieve mapped Relativity fields

To retrieve a list of Relativity fields mapped to a corresponding field in the data source, send a request to this URL for the Field Mapping service:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.Services.FieldMapping.IFieldMappingModule/FieldMappingService/GetAllMappedFieldsAsync
```

The request must have the following fields:

- workspaceArtifactId – the Artifact ID of the workspace that contains the mapped Relativity fields.

- fieldsToAppend – a list of GUIDs corresponding to Relativity fields, which have field data returned for them regardless of whether they are mapped to a data source. Only Invariant currently uses this field. For general use, send in the empty set ([]) for this parameter.

- dataSourceId – the Artifact ID of the processing data source used to populate the mapped fields.

Set this value only if you want an audit of the mapped fields added to the corresponding data source in Relativity. In all other cases, pass the integer 0 as the parameter.

Copy

```text
1
2
3
4
5
{

    "workspaceArtifactId": 1046331,

    "fieldsToAppend": [],

    "dataSourceId": 0

}
```

The following list contains information about fields in a response that have specialized functions or usage requirements:

- MappingId – the identifier of the database record that contains the mapping between a Relativity field and a data source field.

- FieldGuid – the GUID of the field in Relativity. This property won't have a value unless the associated field is part of a Relativity application.

- RelativityFieldName – the name of the field as it appears in Relativity.

- FieldTypeID – the value that corresponds to the kCura.Relativity.Client.FieldType enumeration.

- EnabledDataGrid – a flag indicating whether a field is enabled for Data Grid. This flag is valid only for text fields.

- ExternalFieldName – the name of the field in the external data source.

- ExternalFieldSource – the name of the external data source associated with the mapping. Currently, this fields should always be set to "Invariant".

- FriendlyName – the user-friendly name of the source field. The service populates this field only for members of the Field Catalog. The Field Catalog is a collection of industry best practice fields used with processing. It currently includes 127 fields consistently populated with document metadata. For more information, see Mapping processing fields on the Documentation Server 2025 site.

- UseUnicodeEncoding – indicates that the field uses Unicode encoding. This setting only applies to text fields. The service only maps a text field if this value is true.

- CatalogLength – the maximum length for a fixed-length catalog field.

- CurrentLength – the current maximum length of a fixed-length field in the Relativity database.

- ObjectType – the integer representing the field’s object type. This value corresponds to the kCura.Relativity.Client.ArtifactType enumeration. The service uses this value for validation. Only Artifact Type 10, which corresponds to the Document object, is valid for field mapping.

- IsArtifactBaseField – a Boolean flag indicating whether the field is a base field. A base field is a type of system field, and isn't valid for field mapping.

- FieldCategory – an integer indicating the category of the field. This value corresponds to the kCura.Relativity.Client.FieldCategory enumeration. The following field categories are system fields, which aren't valid for field mapping: AutoCreate, Batch, FolderName, FullText, GenericSystem, MarkupSetMarker, ParentArtifact, ProductionMarker, Reflected, and MultiReflected.

- AssociativeArtifactTypeID – the Artifact Type of an associated object. If the associated ArtifactTypeID is equal to Batch (8), the field isn't valid for field mapping.

The JSON response includes only fields containing values. The response doesn't include any fields with nullable objects.

View a JSON response for mapped Relativity fields Copy

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
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
[

  {

    "MappingId": 1016,

    "FieldArtifactId": 1035380,

    "FieldGuid": "8bb7059c-07cc-453a-8b84-981296d7263d",

    "RelativityFieldName": "Number of Attachments",

    "FieldTypeId": 1,

    "EnableDataGrid": false,

    "ExternalFieldName": "AttachmentCount",

    "ExternalFieldSource": "Invariant",

    "FriendlyName": "Number of Attachments",

    "UseUnicodeEncoding": false,

    "CatalogLength": 0,

    "ObjectType": 10,

    "IsArtifactBaseField": false,

    "FieldCategory": 0

  },

  {

    "MappingId": 1004,

    "FieldArtifactId": 1058862,

    "RelativityFieldName": "Author",

    "FieldTypeId": 0,

    "EnableDataGrid": false,

    "ExternalFieldName": "Author",

    "ExternalFieldSource": "Invariant",

    "FriendlyName": "Author",

    "UseUnicodeEncoding": true,

    "CatalogLength": 50,

    "CurrentLength": 50,

    "ObjectType": 10,

    "IsArtifactBaseField": false,

    "FieldCategory": 0

  },

  {

    "MappingId": 1019,

    "FieldArtifactId": 1035373,

    "FieldGuid": "4946a783-90e3-4acb-8171-f915e5b6fe5a",

    "RelativityFieldName": "Bates Beg Attach",

    "FieldTypeId": 0,

    "EnableDataGrid": false,

    "ExternalFieldName": "BatesBeginAttach",

    "ExternalFieldSource": "Invariant",

    "FriendlyName": "",

    "UseUnicodeEncoding": true,

    "CurrentLength": 50,

    "ObjectType": 10,

    "IsArtifactBaseField": false,

    "FieldCategory": 0

  },

  {

    "MappingId": 1018,

    "FieldArtifactId": 1037987,

    "RelativityFieldName": "Attachment Name",

    "FieldTypeId": 4,

    "EnableDataGrid": false,

    "ExternalFieldName": "Email/x-attach-name",

    "ExternalFieldSource": "Invariant",

    "FriendlyName": "",

    "UseUnicodeEncoding": true,

    "ObjectType": 10,

    "IsArtifactBaseField": false,

    "FieldCategory": 0

  },

  {

    "MappingId": 1021,

    "FieldArtifactId": 1035356,

    "FieldGuid": "8bf21905-fa72-47c8-bd04-070d451a3c3d",

    "RelativityFieldName": "Delivery Receipt",

    "FieldTypeId": 3,

    "EnableDataGrid": false,

    "ExternalFieldName": "EmailDeliveryReceiptRequested",

    "ExternalFieldSource": "Invariant",

    "FriendlyName": "Delivery Receipt Requested",

    "UseUnicodeEncoding": false,

    "CatalogLength": 0,

    "ObjectType": 10,

    "IsArtifactBaseField": false,

    "FieldCategory": 0

  },

  {

    "MappingId": 1005,

    "FieldArtifactId": 1035360,

    "FieldGuid": "6e891164-cb1c-4c1d-8172-a39c27110747",

    "RelativityFieldName": "Control Number Beg Attach",

    "FieldTypeId": 0,

    "EnableDataGrid": false,

    "ExternalFieldName": "RelativityBegAttach",

    "ExternalFieldSource": "Invariant",

    "FriendlyName": "Control Number Beg Attach",

    "UseUnicodeEncoding": true,

    "CatalogLength": 50,

    "CurrentLength": 255,

    "ObjectType": 10,

    "IsArtifactBaseField": false,

    "FieldCategory": 0

  }

]
```

## Retrieve Invariant fields available for mapping

To retrieve Invariant fields that are available for mapping, send a request to this URL for the Field Mapping service:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.Services.FieldMapping.IFieldMappingModule/FieldMappingService/GetInvariantFieldsAsync
```

The request must have the Artifact ID of the workspace that contains the Invariant fields available for mapping.

Copy

```text
1
2
3
{

    "workspaceArtifactId":1046331

}
```

The response always returns the following fields:

- Category – the category of the metadata stored in the field, such as child, email, matter, and others.

- SourceName – the name of the field used by the external data source.

- DataType – the type of data stored in the field, such as fixed-length text, whole number, or others.

The JSON response includes only fields containing values. The response doesn't include any fields with nullable objects.

View a JSON response for available Invariant fields Copy

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
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
[

    {

        "Category": "Child",

        "SourceName": "AttachmentCount",

        "FriendlyName": "Number of Attachments",

        "Description": "Number of files attached to a parent document.",

        "DataType": "Whole Number"

    },

    {

        "Category": "Matter (Common)",

        "SourceName": "AttachmentNumber",

        "DataType": "Int32"

    },

    {

        "Category": "Email",

        "SourceName": "Author",

        "FriendlyName": "Author",

        "Description": "Original composer of document or sender of email message.",

        "DataType": "Fixed-Length Text",

        "MappedFields": [

            "Author"

        ]

    },

    {

        "Category": "Child",

        "SourceName": "BatesBeginAttach",

        "FriendlyName": "Control Number Beg Attach",

        "Description": "The identifier of the first page of the first document in a family group. This is used for page-level numbering schemes.",

        "DataType": "Fixed-Length Text",

        "MappedFields": [

            "A long"

        ]

    },

    {

        "Category": "Matter (Common)",

        "SourceName": "BatesBeginDoc",

        "DataType": "String"

    },

    {

        "Category": "Child",

        "SourceName": "BatesEndAttach",

        "FriendlyName": "Control Number End Attach",

        "Description": "The identifier of the last page of the first document in a family group. This is used for page-level numbering schemes.",

        "DataType": "Fixed-Length Text"

    },

    {

        "Category": "Matter (Common)",

        "SourceName": "BatesEndDoc",

        "DataType": "String"

    },

    {

        "Category": "Matter (Common)",

        "SourceName": "BatesPageNumber",

        "DataType": "String"

    },

    {

        "Category": "Child",

        "SourceName": "ChildFileNames",

        "FriendlyName": "Attachment List",

        "Description": "Attachment file names of all child items in a family group, delimited by semicolon, only present on parent items.",

        "DataType": "Long Text"

    },

    {

        "Category": "Child",

        "SourceName": "ChildMD5Hashes",

        "FriendlyName": "Child MD5 Hash Values",

        "Description": "Attachment MD5 Hash values of all child items in a family group, delimited by semicolon, only present on parent items.",

        "DataType": "Long Text"

    },

    {

        "Category": "Child",

        "SourceName": "ChildRelativityControlNumbers",

        "FriendlyName": "Attachment Document IDs",

        "Description": "Attachment document IDs of all child items in family group, delimited by semicolon, only present on parent items.",

        "DataType": "Long Text"

    },

    {

        "Category": "Child",

        "SourceName": "ChildSHA1Hashes",

        "FriendlyName": "Child SHA1 Hash Values",

        "Description": "Attachment SHA1 Hash values of all child items in a family group, delimited by semicolon, only present on parent items.",

        "DataType": "Long Text"

    },

    {

        "Category": "Child",

        "SourceName": "ChildSHA256Hashes",

        "FriendlyName": "Child SHA256 Hash Values",

        "Description": "Attachment SHA256 Hash values of all child items in a family group, delimited by semicolon, only present on parent items.",

        "DataType": "Long Text"

    },

    {

        "Category": "General",

        "SourceName": "Comments",

        "FriendlyName": "Comments",

        "Description": "Comments extracted from the metadata of the native file.",

        "DataType": "Long Text"

    },

    {

        "Category": "Matter (Common)",

        "SourceName": "ContainerExtension",

        "DataType": "String"

    },

    {

        "Category": "Matter (Common)",

        "SourceName": "ContainerID",

        "DataType": "Int64"

    },

    {

        "Category": "Matter (Common)",

        "SourceName": "ContainerName",

        "DataType": "String"

    },

    {

        "Category": "Email",

        "SourceName": "ConversationFamily",

        "FriendlyName": "Conversation Family",

        "Description": "Relational field for conversation threads.  This is a 44-character string of numbers and letters that is created in the initial email.",

        "DataType": "Fixed-Length Text"

    },

    {

        "Category": "General",

        "SourceName": "CreatedOn",

        "FriendlyName": "Date Created",

        "Description": "Date and time from the Date Created property extracted from the original file or email message.",

        "DataType": "Date",

        "MappedFields": [

            "Date Created"

        ]

    },

    {

        "Category": "Matter (Common)",

        "SourceName": "DataGridDocMetadataId",

        "DataType": "Int32"

    },

    {

        "Category": "Matter (Common)",

        "SourceName": "DataGridId",

        "DataType": "Guid"

    },

    {

        "Category": "General",

        "SourceName": "DeDupedCustodians",

        "FriendlyName": "DeDuped Custodians",

        "Description": "Custodians associated with the de-duped records of this document.",

        "DataType": "Multiple Object"

    },

    {

        "Category": "General",

        "SourceName": "DeDupedPaths",

        "FriendlyName": "DeDuped Paths",

        "Description": "Folder structure and paths to this document's duplicates. Each path will contain the associated custodian.",

        "DataType": "Long Text"

    },

    {

        "Category": "(Saved Fields)",

        "SourceName": "DedupeHash",

        "DataType": "String"

    }

...

]
```

## Retrieve an external field mapping

To retrieve an external field mapping for a field with the specified Artifact ID, send a request to this URL for the Field Mapping service:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.Services.FieldMapping.IFieldMappingModule/FieldMappingService/ReadExternalMappingAsync
```

The request must have the following fields:

- workspaceArtifactId – the Artifact ID of the workspace that contains the field for retrieval.

- fieldArtifactId – the Artifact ID of the field with a mapping that you want to retrieve.

- fieldSource – the string that identifies the field source. This service currently supports only Invariant as the field source.

Copy

```text
1
2
3
4
5
{

    "workspaceArtifactId":1046331,

    "fieldArtifactId":1039415,

    "fieldSource":"Invariant"

}
```

For descriptions of specialized fields in the following JSON response, see Retrieve mapped Relativity fields .

The JSON response includes only fields containing values. The response doesn't include any fields with nullable objects.

View a JSON response for an external field mapping Copy

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

    "MappingId": 4,

    "FieldArtifactId": 1039415,

    "RelativityFieldName": "Other Properties",

    "FieldTypeId": 4,

    "EnableDataGrid": false,

    "ExternalFieldName": "OtherProps",

    "ExternalFieldSource": "Invariant",

    "FriendlyName": "Other Props",

    "UseUnicodeEncoding": true

}
```

## Update an external field mapping

To modify or add field mapping data, send a request to this URL for the Field Mapping service:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.Services.FieldMapping.IFieldMappingModule/FieldMappingService/UpdateExternalMappingAsync
```

The request must have the following fields:

- workspaceArtifactId – the Artifact ID of the workspace where you want to update the mapped fields.

- model – an ExternalMapping object with the updated data. For descriptions of specialized fields in the model, see Retrieve mapped Relativity fields .

On the model, you must set the following properties to make a successful UpdateExternalMappingAsync() method call:

- ExternalFieldName - the name of the field in the external data source. Set this property to null if you want to remove the field mapping.

- ExternalFieldSource - the name of the external data source associated with the mapping. Currently, this fields should always be set to "Invariant".

- FieldArtifactId - the Artifact ID of the Relativity field being mapped.

In addition, you should also set specific fields that are used for validation. If you don't set these fields correctly, the field mapping may not update. The following list includes fields used for validation:

- CurrentLength - For fixed-length catalog fields, you must set this property to a minimum field length required for validation. For example, if the CurrentLength property is set to 0 when you attempt to map a fixed-length catalog field, the validation fails.

- FieldTypeId - The service validates the property against the data type that Invariant uses for the field source. For example, you may want to map a source field that Invariant identifies as a Date type. If you set the FieldTypeId property to 0 indicating a fixed-length text field, then the validation fails and the field isn't mapped. The values for this property correspond to the kCura.Relativity.Client.FieldType enumeration.

- ObjectType - You must set this property to 10.

- UseUnicodeEncoding - For text fields, you must set this property to true.

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
{

    workspaceArtifactId: 1046331,

    model: {

        "FieldArtifactId": 1039415,

        "RelativityFieldName": "Parent Document ID",

        "FieldTypeId": 0,

        "EnableDataGrid": true,

        "ExternalFieldName": "ParentRelativityControlNumber",

        "ExternalFieldSource": "Invariant",

        "UseUnicodeEncoding": true,

        "CurrentLength": 50,

        "ObjectType": 10,

        "IsArtifactBaseField": false,

        "FieldCategory": 0

    }

}
```

The response returns the status code of 200. The Relativity UI displays the field update, such as an ExternalFieldName called BCC Address, which is renamed to BatesBeginDoc.

## Retrieve GUIDs for automapped fields

During a publish operation, Invariant automatically maps certain processing system fields. The GetAutomappedFieldGuidsAsync() method retrieves a list of GUIDs that Invariant uses to identify these fields.

To retrieve this list of GUIDs, send a request to this URL for the Field Mapping service:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.Services.FieldMapping.IFieldMappingModule/FieldMappingService/GetAutomappedFieldGuidsAsync
```

The request must have the Artifact ID of the workspace where you want to map fields.

Copy

```text
1
2
3
{

    "workspaceArtifactId": 1046331

}
```

The response returns a list of GUIDs for the corresponding ExternalMapping objects. These objects represent mappings between Relativity and an external data source fields. For more information, see Field Mapping Manager .

View a JSON response for an external field mapping Copy

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
[

    "a37f5152-2354-4102-88bd-09e2387a0c83",

    "ab44a773-e968-454f-92d7-a29f4f61dc9f",

    "9876411c-1e32-436a-bedf-19267b590c17",

    "2a3f1212-c8ca-4fa9-ad6b-f76c97f05438",

    "8ac3cec2-cebe-4c11-9e5a-e934df45aaf5",

    "1618195a-b7f1-4732-a57d-b2b5efd4d2db",

    "ef3210e4-a53b-4498-ada4-7183607eeeb4",

    "1aba1dc9-69ca-4eb6-a044-7ad8d01ed9c1",

    "aecaee0a-76ba-4860-ba55-d63b97525d41",

    "58d35076-1b1d-43b4-bff4-d6c089de51b2",

    "adb35bd6-9ffb-426f-ae71-4c2bf923ff81",

    "42bbfad4-f0fd-441b-bea7-79319976bcce",

    "61020401-15e7-4101-8082-d5276a60430a",

    "192c52b2-869e-4262-95f0-2c6a3f056610",

    "93e1cfeb-f21e-4386-adc3-846066525fe8",

    "b68a1fe7-f8df-4461-afae-4fb3e1169e6e",

    "6130fe12-5dba-46c9-8918-217329942da9",

    "a5768969-ead6-4160-a8d9-22aa9bae413a",

    "3163e7fc-b01e-4048-8423-c6f6eaff6114"

]
```

## Clear cached data

The ClearCachedDataAsync() method removes all cached data from Relativity, Invariant, and the Field Catalog. You can use this method for testing purposes, and for clearing cached data that may be corrupt.

To clear the cache, send a request to this URL for the Field Mapping service:

Copy

```text
1
<host>/Relativity.Rest/api/Relativity.Services.FieldMapping.IFieldMappingModule/FieldMappingService/ClearCachedDataAsync
```

You don't need to provide any information in the body of the request. The response returns the status code of 200.

On this page

- Field Mapping (REST v0)

- Client code sample

- Check field mapping availability

- Retrieve mapped Relativity fields

- Retrieve Invariant fields available for mapping

- Retrieve an external field mapping

- Update an external field mapping

- Retrieve GUIDs for automapped fields

- Clear cached data


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

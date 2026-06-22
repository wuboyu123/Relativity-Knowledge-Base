---
title: "Production Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Production/Production_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:58+00:00
sha256: 1ae333bf99a1efe25ce986cd6bac00b6dd155393842f6961d63f54cd250879a9
---

Production Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Production Manager (REST)

A production is a group of non-privileged documents delivered to opposing counsel as part of a legal proceeding. Relativity uses a production set to define the markup set for redactions, numbering, and other settings applied to the documents during a production job. For general information, see Production and Production sets on the Relativity Server 2025 Documentation site.

The Production Manager API exposes endpoints that provide the following functionality for productions:

- Creating, deleting, staging, running, and performing other tasks with production sets

- Retrieving default fields on a production

- Setting and removing production restrictions defined in a workspace

- Retrieving information about production jobs, such as status, progress, and production results

- Retrieving information about production errors and document conflicts

- Retrieving, running, staging, and canceling re-production jobs

You can also use the Production Manager service through .NET. For more information, see Production Manager (.NET) .

See these related pages:

- Production

- Production Data Source Manager (REST)

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

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the Document Conflicts service. To download the sample file, click Production Manager Postman file .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Production sets and jobs

This section contains code samples that illustrate how to create, stage, run, and perform other tasks with productions.

### Create a production set

To add a new production set to a Relativity workspace, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions
```

View field descriptions for a request

The request may contain the following fields:

- DataSources - an array of ProductionDataSource objects with the following fields:

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

- Details - contains the following fields:

- EmailRecipients - a string containing the emails of recipients who are notified about the status of the production.

- BrandingFont - a string indicating the font used for branding.

- BrandingFontSize - an integer indicating the font size used for branding.

- ScaleBrandingFont - a Boolean value indicating whether to scale the branding font.

- WrapBrandingText - a Boolean value indicating whether to wrap the branding text when it may overlap with adjacent headers or footers.

- PlaceholderImageFormat - the file type of image used for the placeholder. Set this field to Tiff or Jpeg .

- FirstBatesValue - a string indicating the initial Bates number for the completed production.

- LastBatesValue - a string indicating the final Bates number for the completed production.

- DateProduced - an optional the date and time field to store data about the production.

- Numbering - contains the following fields:

- BatesPrefix - a string used to define the prefix for a Bates number.

- BatesSuffix - a string used to define the suffix for a Bates number.

- BatesStartNumber - an integer indicating the initial Bates number for the production.

- NumberOfDigitsForDocumentNumbering - an integer representing the number of digits used for document-level numbering. The range is from 1 to 7.

- NumberingType - the document number type as defined in the NumberingType enumeration. Values include PageLevel, DocumentLevel, OriginalImage, ExistingProduction, and DocumentField.

- AttachmentRelationalField - contains the following information:

- ArtifactID - the Artifact ID for the field.

- ViewFieldID - the field ID for the view.

- Guids - an array of GUIDs for the field.

- Name - the user-friendly name of the field.

- SortOrder - an array of Sort objects with properties indicating the direction of the sort as ascending or descending, and the name of the field to sort on. These objects determine how the documents in the production are sorted. A maximum of five Sort objects can be specified.

- Headers - contain the following fields:

- Left - defines the left header with the following fields:

- Type - indicates the header types as defined in the HeaderFooterType enumeration. Values include None, ProductionBatesNumber, Field, FreeText, OriginalImageNumber, DocumentIdentifierAndPageNumber, and AdvancedFormatting.

- Field - specifies the document field used in header. If the Type field is set to Field, the following values must be specified:

- ArtifactID - the Artifact ID for the field.

- ViewFieldID - the field ID for the view.

- Guids - an array of GUIDs for the field.

- Name - the user-friendly name of the field.

- FreeText - specifies the text used in header, which may include a combination of text, tokens, and carriage returns. If the Type field is set to FreeText, this field specifies the text.

- AdvancedFormatting - specifies formatting using a subset of HTML. If the Type field is set to AdvancedFormatting, this field specifies the formatting.

- FriendlyName - a descriptive name for the header.

- Right - see the descriptions in Left field.

- Center - see the descriptions in Left field.

- Footers - contains the following the Left, Right, and Center fields. See the descriptions in Left field under the Header.

- Keywords - optional words or phrases used to describe the production.

- Notes - an optional description or other information about the production.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The production set is linked to the applications in this array. If the array is empty, then the production set isn't linked to any application.

- ShouldCopyInstanceOnWorkspaceCreate - a Boolean value indicating whether instances of this production are copied when a new workspace is created.

- Name - a user-friendly name for the production set.

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
{

  "production": {

    "dataSource": [

      {

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

    ],

    "Details": {

      "EmailRecipients": "",

      "BrandingFont": "Arial",

      "BrandingFontSize": 10,

      "ScaleBrandingFont": false,

      "WrapBrandingText": false,

      "PlaceholderImageFormat": "Tiff",

      "FirstBatesValue": "PRE0000001",

      "LastBatesValue": "PRE0000007",

      "DateProduced": "2020-10-23T19:23:40.233"

    },

    "Numbering": {

      "BatesPrefix": "PRE",

      "BatesSuffix": "",

      "BatesStartNumber": 1,

      "NumberOfDigitsForDocumentNumbering": 7,

      "NumberingType": "PageLevel",

      "AttachmentRelationalField": {

        "ArtifactID": 0,

        "ViewFieldID": 0,

        "Guids": [],

        "Name": ""

      }

    },

    "SortOrder": [],

    "Headers": {

      "Left": {

        "Type": "None",

        "Field": {

          "ArtifactID": 0,

          "ViewFieldID": 0,

          "Guids": [],

          "Name": ""

        },

        "FreeText": "",

        "AdvancedFormatting": "",

        "FriendlyName": "Left Header"

      },

      "Right": {

        "Type": "None",

        "Field": {

          "ArtifactID": 0,

          "ViewFieldID": 0,

          "Guids": [],

          "Name": ""

        },

        "FreeText": "",

        "AdvancedFormatting": "",

        "FriendlyName": "Right Header"

      },

      "Center": {

        "Type": "None",

        "Field": {

          "ArtifactID": 0,

          "ViewFieldID": 0,

          "Guids": [],

          "Name": ""

        },

        "FreeText": "",

        "AdvancedFormatting": "",

        "FriendlyName": "Center Header"

      }

    },

    "Footers": {

      "Left": {

        "Type": "None",

        "Field": {

          "ArtifactID": 0,

          "ViewFieldID": 0,

          "Guids": [],

          "Name": ""

        },

        "FreeText": "",

        "AdvancedFormatting": "",

        "FriendlyName": "Left Footer"

      },

      "Right": {

        "Type": "None",

        "Field": {

          "ArtifactID": 0,

          "ViewFieldID": 0,

          "Guids": [],

          "Name": ""

        },

        "FreeText": "",

        "AdvancedFormatting": "",

        "FriendlyName": "Right Footer"

      },

      "Center": {

        "Type": "None",

        "Field": {

          "ArtifactID": 0,

          "ViewFieldID": 0,

          "Guids": [],

          "Name": ""

        },

        "FreeText": "",

        "AdvancedFormatting": "",

        "FriendlyName": "Center Footer"

      }

    },

    "Keywords": "",

    "Notes": "",

    "RelativityApplications": [],

    "ShouldCopyInstanceOnWorkspaceCreate": false,

    "Name": "Production 1 (1) (1) (1)"

  }

}
```

When the production set is successfully created, the response contains its Artifact ID.

Copy

```text
1
1048147
```

### Retrieve a production set

To retrieve a production set, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}?dataSourceReadMode={dataSourceReadMode}
```

The request body is empty.

The response for a read operation contains the many of the same fields as a request for a create operation. See the field descriptions in Create a production set .

The read operation also returns several additional fields.

View additional field descriptions for a response

The response also contains these fields:

- ProductionMetadata - contains the following fields created and updated by Relativity:

- RestrictionOverrideBy - tracks production restrictions for internal use only.

- RestrictionOverrideOn - tracks production restrictions by date and time for internal use only.

- Status - indicates the status as defined in the Production Status enumeration.

- Imported - a Boolean value indicating whether this production was imported through the Relativity Desktop Client.

- LegacyProductionSet - a Boolean value indicating whether this production is a legacy production set.

- DocumentsHaveRedactions - a Boolean value indicating whether documents have redactions after they are produced.

- SystemCreatedBy - contains the following fields:

- Secured - indicates whether the current user has permission to view the setting in the Value field.

- Value - the Artifact ID and name of the user who created the production.

- SystemCreatedOn - the date and time when the production was added to Relativity. See the description of the Secured field in SystemCreatedBy.

- SystemLastModifiedBy - contains the Artifact ID and name of the user who recently updated the production. See the description of the Secured field in SystemCreatedBy.

- SystemLastModifiedOn - the date and time when the production was most recently modified. See the description of the Secured field in SystemCreatedBy.

- LastRunError - a string representing a status message for the most recent error.

- LastRunStatus - a string representing a status message for the most recent run.

- BrandingPercentageComplete - a decimal indicating the percentage of the branding completed on the production.

- ImagingPercentageComplete - a decimal indicating the percentage of the imaging completed on the production.

- TotalDocumentCount - an integer representing the total number of documents in the production.

- TotalImagesCount - an integer representing the total number of images in the production.

- DocumentsWithImages - an integer representing the total number of documents with images.

- DocumentsWithNatives - an integer representing the total number of documents with native files.

- DocumentsWithPlaceholders - an integer representing the total number of documents with placeholders.

- DocumentsWithRedactions - an integer representing the total number of documents with redactions.

- TotalProducedImageSize - an integer representing the total image size in GBs.

- ProductionSavedSearch - contains the following fields:

- ArtifactID - the Artifact ID of the saved search used by the production.

- Name - the user-friendly name of the saved search used by the production.

- ProductionID - the Artifact ID of the production

- Name - the user-friendly name of the production.

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
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
{

    "DataSources": [

        {

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

            "ArtifactID": 1048148,

            "Name": "Data (1) (1) (1)"

        }

    ],

    "Details": {

        "EmailRecipients": "",

        "BrandingFont": "Arial",

        "BrandingFontSize": 10,

        "ScaleBrandingFont": false,

        "WrapBrandingText": false,

        "PlaceholderImageFormat": "Tiff",

        "FirstBatesValue": "PRE0000001",

        "LastBatesValue": "PRE0000007",

        "DateProduced": "2020-10-23T19:23:40.233"

    },

    "Numbering": {

        "BatesPrefix": "PRE",

        "BatesSuffix": "",

        "BatesStartNumber": 1,

        "NumberOfDigitsForDocumentNumbering": 7,

        "NumberingType": "PageLevel",

        "AttachmentRelationalField": {

            "ArtifactID": 0,

            "ViewFieldID": 0,

            "Guids": [],

            "Name": ""

        }

    },

    "SortOrder": [],

    "Headers": {

        "Left": {

            "Type": "None",

            "Field": {

                "ArtifactID": 0,

                "ViewFieldID": 0,

                "Guids": [],

                "Name": ""

            },

            "FreeText": "",

            "AdvancedFormatting": "",

            "FriendlyName": "Left Header"

        },

        "Right": {

            "Type": "None",

            "Field": {

                "ArtifactID": 0,

                "ViewFieldID": 0,

                "Guids": [],

                "Name": ""

            },

            "FreeText": "",

            "AdvancedFormatting": "",

            "FriendlyName": "Right Header"

        },

        "Center": {

            "Type": "None",

            "Field": {

                "ArtifactID": 0,

                "ViewFieldID": 0,

                "Guids": [],

                "Name": ""

            },

            "FreeText": "",

            "AdvancedFormatting": "",

            "FriendlyName": "Center Header"

        }

    },

    "Footers": {

        "Left": {

            "Type": "None",

            "Field": {

                "ArtifactID": 0,

                "ViewFieldID": 0,

                "Guids": [],

                "Name": ""

            },

            "FreeText": "",

            "AdvancedFormatting": "",

            "FriendlyName": "Left Footer"

        },

        "Right": {

            "Type": "None",

            "Field": {

                "ArtifactID": 0,

                "ViewFieldID": 0,

                "Guids": [],

                "Name": ""

            },

            "FreeText": "",

            "AdvancedFormatting": "",

            "FriendlyName": "Right Footer"

        },

        "Center": {

            "Type": "None",

            "Field": {

                "ArtifactID": 0,

                "ViewFieldID": 0,

                "Guids": [],

                "Name": ""

            },

            "FreeText": "",

            "AdvancedFormatting": "",

            "FriendlyName": "Center Footer"

        }

    },

    "Keywords": "",

    "Notes": "",

    "RelativityApplications": [],

    "ShouldCopyInstanceOnWorkspaceCreate": false,

    "ProductionMetadata": {

        "RestrictionOverrideBy": {

            "ArtifactID": 0,

            "Name": ""

        },

        "RestrictionOverrideOn": "0001-01-01T00:00:00",

        "Status": "Produced",

        "Imported": false,

        "LegacyProductionSet": false,

        "DocumentsHaveRedactions": false,

        "SystemCreatedBy": {

            "Secured": false,

            "Value": {

                "ArtifactID": 9,

                "Name": "Admin, Relativity"

            }

        },

        "SystemCreatedOn": {

            "Secured": false,

            "Value": "2020-10-23T19:23:27.607"

        },

        "SystemLastModifiedBy": {

            "Secured": false,

            "Value": {

                "ArtifactID": 9,

                "Name": "Admin, Relativity"

            }

        },

        "SystemLastModifiedOn": {

            "Secured": false,

            "Value": "2020-10-23T19:23:53.107"

        },

        "LastRunError": "",

        "LastRunStatus": "",

        "BrandingPercentageComplete": 100.0,

        "ImagingPercentageComplete": 100.0,

        "TotalDocumentCount": 7,

        "TotalImagesCount": 7,

        "DocumentsWithImages": 0,

        "DocumentsWithNatives": 0,

        "DocumentsWithPlaceholders": 7,

        "DocumentsWithRedactions": 0,

        "TotalProducedImageSize": 12,

        "ProductionSavedSearch": {

            "ArtifactID": 1048156,

            "Name": ""

        }

    },

    "ProductionID": 1048147,

    "Name": "Production 1 (1) (1) (1)"

}
```

### Delete a production set

To remove a production set from Relativity, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}
```

The request body is empty.

When the production is successfully deleted, the response returns the status code of 200.

### Stage a production

To stage a production, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/stage
```

The request must contain the following field:

- automaticallyRun - a Boolean value indicating whether to immediately run the staged production. The default value is false.

Copy

```text
1
2
3
{

    "automaticallyRun": false

}
```

View field descriptions for a response

The response contains a ProductionJobResult object with the following fields:

- JobID - the ID for the production job.

- Errors - an array of strings providing error messages if the job wasn't created.

- Messages - an array of strings providing additional information about the job.

- Warnings - an array of strings providing warnings about the job.

- WasJobCreated - a Boolean value indicating whether the production job was created.

- ProductionID - the Artifact ID of the production.

- WorkspaceID - the Artifact ID of the workspace containing the production.

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
{

    "JobID": 121,

    "Errors": [],

    "Messages": [],

    "Warnings": [],

    "WasJobCreated": true,

    "ProductionID": 1053233,

    "WorkspaceID": 1017955

}
```

### Run a production job

To run a production job, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/run
```

The request must contain the following fields:

- suppressWarnings - a Boolean value indicating whether to suppress warning messages.

- overrideConflicts - a Boolean value indicating whether to override production conflicts.

Copy

```text
1
2
3
4
{

    "suppressWarnings": true,

    "overrideConflicts": false

}
```

The response contains the same fields as a response for a staging operation. See the field descriptions in Stage a production .

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

    "JobID": 122,

    "Errors": [],

    "Messages": [

        "There is no specified Production Restriction for this workspace."

    ],

    "Warnings": [],

    "WasJobCreated": true,

    "ProductionID": 1053233,

    "WorkspaceID": 1017955

}
```

### Stage and run multiple production jobs

You can stage and run multiple productions in a workspace. If the production is already staged, this method only runs it.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/stage-and-run
```

The request must contain the following field:

- productionIDs - an array of Artifact IDs for the productions that the you want to stage and run.

Copy

```text
1
2
3
4
5
6
{

    "productionIDs": [

        101,

        102

    ]

}
```

The response contains a ProductionJobResult object for each production in the request. See the field descriptions in Stage a production .

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
[

    {

        "JobID": 1,

        "Errors": [],

        "Messages": [],

        "Warnings": [],

        "WasJobCreated": true,

        "ProductionID": 101,

        "WorkspaceID": 200

    },

    {

        "JobID": 2,

        "Errors": [

            "One or more productions in this request could not be run, so this production will not run either. Please check all errors.",

            "Production specified is invalid."

        ],

        "Messages": [],

        "Warnings": [],

        "WasJobCreated": false,

        "ProductionID": 102,

        "WorkspaceID": 200

    }

]
```

### Re-run a production

To re-run a production, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/re-run
```

The request body is empty.

When the production is successfully marked for re-running, the response returns the status code of 200.

## Default fields and restrictions for productions

This section contains code samples that illustrate how to retrieve default field values, and how to set and remove production restrictions.

### Retrieve default field values for a production

You can retrieve default field values for a production. This method doesn't return empty or null fields.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{workspaceID}/productions/defaults
```

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- field object - an object for each field associated with the data source. In the sample JSON, these objects are ScaleBrandingFont, BrandingFont, and others.

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
{

    "ScaleBrandingFont": {

        "Guid": "058e1081-2d70-46b5-8cf7-a08d0ee624a0",

        "ID": 1038763,

        "DefaultValue": false

    },

    "BrandingFont": {

        "Guid": "59404f41-98ef-42b7-b0b1-9573331ad25a",

        "ID": 1039439,

        "DefaultValue": {

            "ID": 1039448,

            "Name": "Verdana"

        }

    },

    "BrandingFontSize": {

        "Guid": "96554098-79f2-4cfb-b851-366e88923a74",

        "ID": 1038762,

        "DefaultValue": 12

    },

    "PlaceholderImageFormat": {

        "Guid": "4be69bed-fed5-426d-bfbc-57596926ac26",

        "ID": 1039174,

        "DefaultValue": {

            "ID": 1039176,

            "Name": "JPEG"

        }

    },

    "CopyProductionOnWorkspaceCreate": {

        "Guid": "71bc6045-e2fe-4f12-80f6-aee298b124f7",

        "ID": 1038899,

        "DefaultValue": false

    },

    "WrapBrandingText": {

        "Guid": "229b331d-c560-4805-90c9-875214be23c8",

        "ID": 1039449,

        "DefaultValue": true

    },

    "NumberingType": {

        "Guid": "3eb821b5-01b4-48d4-a3ab-26b2cfa5d236",

        "ID": 1038764,

        "DefaultValue": {

            "ID": 1038765,

            "Name": "Page level numbering"

        }

    },

    "StartNumber": {

        "Guid": "859851d2-efc6-4510-8bcb-5e4df1db53bd",

        "ID": 1038771,

        "DefaultValue": 1

    },

    "NumberOfDigitsForDocumentNumbering": {

        "Guid": "4d29f986-0399-4534-922a-e4c19719415b",

        "ID": 1038772,

        "DefaultValue": {

            "ID": 1038779,

            "Name": "7"

        }

    },

    "IncludePageNumbers": {

        "Guid": "67ba287e-f468-4c55-ae65-3dea3f6a804d",

        "ID": 1038827,

        "DefaultValue": false

    },

    "DocumentPageSeparator": {

        "Guid": "c180f1cb-a500-4e67-9016-1323649e9713",

        "ID": 1038828,

        "DefaultValue": {

            "ID": 1038829,

            "Name": "_ (underscore)"

        }

    },

    "NumberOfDigitsForPageNumbering": {

        "Guid": "d435d806-963d-45f2-b629-45b675776ace",

        "ID": 1038832,

        "DefaultValue": {

            "ID": 1038836,

            "Name": "4"

        }

    },

    "StartNumberOnSecondPage": {

        "Guid": "a517d142-3569-46a5-8c58-ccd145be3b75",

        "ID": 1039172,

        "DefaultValue": false

    },

    "MergeExistingSet": {

        "Guid": "12092f60-6c0a-4df0-8326-1ff41aab26b2",

        "ID": 1038840,

        "DefaultValue": false

    },

    "SortOrderAscDesc1": {

        "Guid": "06100bff-a79c-459b-a151-9780034bb018",

        "ID": 1038851,

        "DefaultValue": {

            "ID": 1038852,

            "Name": "Ascending"

        }

    },

    "SortOrderAscDesc2": {

        "Guid": "efa4082d-3fab-4245-b597-baa59c00679a",

        "ID": 1038854,

        "DefaultValue": {

            "ID": 1038855,

            "Name": "Ascending"

        }

    },

    "SortOrderAscDesc3": {

        "Guid": "0e4eab9e-a42a-4531-b958-b0657d5a76f6",

        "ID": 1038857,

        "DefaultValue": {

            "ID": 1038858,

            "Name": "Ascending"

        }

    },

    "SortOrderAscDesc4": {

        "Guid": "899e7fa0-5725-4b66-b753-a83b66ebd07f",

        "ID": 1038860,

        "DefaultValue": {

            "ID": 1038861,

            "Name": "Ascending"

        }

    },

    "SortOrderAscDesc5": {

        "Guid": "eeb4ce8e-871e-4eec-9efd-a42d06d23140",

        "ID": 1038863,

        "DefaultValue": {

            "ID": 1038864,

            "Name": "Ascending"

        }

    }

}
```

### Set production restrictions on a workspace

To add a production restriction to a workspace, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/production-restriction
```

The request must contain the following field:

-

productionRestrictionSearchID - the Artifact ID of a saved search in the workspace if this value isn't already set. If the value is set, this endpoint replaces the current production restriction with a new one.

Use 0 as the ID for a saved search if you want to clean up the current production restriction.

Copy

```text
1
2
3
{

    "productionRestrictionSearchID" : 1039456

}
```

When the production restriction is successfully added, the response returns the status code of 200.

### Retrieve the ID of a save search used for production restrictions

You can retrieve the ID of a save search used for production restrictions in a workspace. This endpoint returns 0 if a production restriction hasn't been set.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/production-restriction
```

The response contains the Artifact ID of the saved search.

Copy

```text
1
1041865
```

## Production job status, progress, and other information

This section contains code samples that illustrate how to retrieve information about production jobs, including status, progress, production results, and others.

### Retrieve the job status of a production

To retrieve the job status of a production, send a GET request with a URL in the following format:

Copy

```text
1
Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/job-status?includePercentages={includePercentages}&numberOfBrandingErrors={numberOfBrandingErrors}
```

The request body is empty.

View field descriptions for a response

The response contains a ProductionJobStatusResult object with the following fields:

- BrandingErrors - an array of branding error messages.

- NumberOfBrandingErrors - an integer representing the total number of branding errors in the job.

- JobStatus - indicates the status of the job based on the ProductionJobStatus enumeration :

- NotRunning - the job is currently not running.

- Running - the job is currently running.

- Errored - the job isn't running and is errored.

- Complete - the job is currently isn't running and is completed.

- Status - the status of the production, such as New, Staging, Branding and others. See the Production Status .

- PercentageImaging - a decimal representing the percentage completed of the branding process.

- PercentageProducing - a decimal representing the percentage completed of the producing process.

- LastRunStatus - a string representing a status message for the most recent run.

- LastRunError - a string representing a status message for the most recent error.

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
{

    "BrandingErrors": [

        "Redaction ID 1 is outside the bounds of the image. Please move the redaction and rerun the production.",

        "Redaction ID 2 is outside the bounds of the image. Please move the redaction and rerun the production."

    ],

    "NumberOfBrandingErrors": 2,

    "JobStatus": "Errored",

    "Status": "Error",

    "PercentageImaging": 0.0,

    "PercentageProducing": 0.0,

    "LastRunStatus": "There was an error producing/branding the production.",

    "LastRunError": "There were errors during Branding for Production 1050464, please check the branding errors tab."

}
```

### Retrieve progress details for a production

To retrieve progress details for a production, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/progress
```

The request body is empty.

View field descriptions for a response

The response contains a ProductionProgress object with the following fields:

- Status - a string indicating the status of the production.

- StartTime - the date and time that the production began running.

- CurrentBrandingQueueLength - a long indicating the number of incomplete branding jobs.

- TotalImages - a long indicating the total number of images in the production.

- ImagesToBeBranded - a long indicating the number of images to be branded.

- ImagesWithErrors - a long indicating the number of images with branding errors.

- TotalDocuments - a long indicating the total number of documents in the production.

- DocumentsWithImages - a long indicating the total number of documents with images.

- DocumentsWithPlaceHolders - a long indicating the total number of documents with placeholders.

- DocumentsWithRedactions - a long indicating the total number of documents with redactions.

- DocumentsWithNatives - a long indicating the total number of documents with native files.

- ImageSizeInGb - the total size of the all the images in GBs.

- ProductionRunDate - the date and time that the production was produced.

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
{

    "Status": "Staged",

    "StartTime": "0001-01-01T00:00:00",

    "CurrentBrandingQueueLength": 0,

    "TotalBrandingQueueLength": 0,

    "TotalImages": 1,

    "ImagesToBeBranded": 0,

    "ImagesBranded": 0,

    "ImagesWithErrors": 0,

    "TotalDocuments": 1,

    "DocumentsWithImages": 0,

    "DocumentsWithPlaceHolders": 1,

    "DocumentsWithRedactions": 0,

    "DocumentsWithNatives": 0,

    "ImageSizeInGb": 0.0,

    "ProductionRunDate": "0001-01-01T00:00:00"

}
```

### Retrieve production status details

To retrieve production status details, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/status-details
```

The request body is empty.

The response contains a ProductionJobStatusResult object. For field descriptions, see Retrieve the job status of a production .

### Retrieve results for produced image files

You can retrieve produced image files by using paging or document IDs.

View a request and response using paging

To retrieve images by using paging, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/production-images/token?top={top}&skip={skip}
```

Set the path parameters in the URL as follows:

- {WorkspaceId} - the Artifact ID of workspace containing productions to retrieve.

- {ProductionID} - the Artifact ID of the production containing the images.

- {top} - an integer representing the number of images to be returned.

- {skip} - an integer representing the number of images to omit before retrieving the results.

The request body is empty.

The response contains PagedImageFilesResult object with the following fields:

- TotalResultSet - an integer indicating the number of results for this request.

- ResultCount - an integer indicating the number of results returned in the current page.

- ImageFiles - an array of objects representing an image file. The files aren't in any specific order. Each produced file has the following fields:

- DocumentID - the Artifact ID of a document.

- FileID - an ID for the file.

- PageNumber - an integer indicating the page number of this file in the document. The page numbers are 0-indexed.

- HasRedactions - a Boolean value indicating whether this image file has redactions.

- FileGuid - a GUID for the file.

- Errors - an array of errors associated with the current page.

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
{

    "TotalResultSet": 7,

    "ResultCount": 7,

    "ImageFiles": [

        {

            "DocumentID": 1045081,

            "FileID": 13704,

            "PageNumber": 0,

            "HasRedactions": false,

            "FileGuid": "40b546c1-ad51-4857-a695-84e72fb70e24"

        },

        {

            "DocumentID": 1045082,

            "FileID": 13705,

            "PageNumber": 0,

            "HasRedactions": false,

            "FileGuid": "0ce86285-4865-45af-b77d-1dedda3fb114"

        },

        {

            "DocumentID": 1045083,

            "FileID": 13706,

            "PageNumber": 0,

            "HasRedactions": false,

            "FileGuid": "676fcdbd-2ef7-4270-b75c-173bd6fd052c"

        },

        {

            "DocumentID": 1045084,

            "FileID": 13707,

            "PageNumber": 0,

            "HasRedactions": false,

            "FileGuid": "dd718d91-833f-4166-a77d-fda4630af226"

        },

        {

            "DocumentID": 1045085,

            "FileID": 13708,

            "PageNumber": 0,

            "HasRedactions": false,

            "FileGuid": "b164bd13-0824-497f-98ac-3904a3bf3e33"

        },

        {

            "DocumentID": 1045086,

            "FileID": 13709,

            "PageNumber": 0,

            "HasRedactions": false,

            "FileGuid": "c5c9721d-64d4-4ac1-a62e-974146c9afe7"

        },

        {

            "DocumentID": 1045087,

            "FileID": 13710,

            "PageNumber": 0,

            "HasRedactions": false,

            "FileGuid": "c7a15e16-7d80-4b78-877c-67e1a037e1a8"

        }

    ],

    "Errors": []

}
```

View a request and response using document IDs

To retrieve images by using document IDs, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/production-images
```

The request must contain the following field:

- documentIDs - the Artifact IDs of the documents with images to be retrieved.

Copy

```text
1
2
3
4
5
6
{

    "documentIDs":[

       1045081,

       1045082

    ]

}
```

The response contains an ImageFilesResult object with the following fields:

- Count - an integer representing the total number of files returned.

- ImageFiles - an array of objects representing an image file. Each image file has the following fields:

- DocumentID - the Artifact ID of a document.

- FileID - an ID for the file.

- PageNumber - an integer indicating the page number of this file in the document. The page numbers are 0-indexed.

- HasRedactions - a Boolean value indicating whether this image file has redactions.

- FileGuid - a GUID for the file.

- Errors - an array of errors associated with this result.

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
{

    "Count": 2,

    "ImageFiles": [

        {

            "DocumentID": 1045081,

            "FileID": 13704,

            "PageNumber": 0,

            "HasRedactions": false,

            "FileGuid": "40b546c1-ad51-4857-a695-84e72fb70e24"

        },

        {

            "DocumentID": 1045082,

            "FileID": 13705,

            "PageNumber": 0,

            "HasRedactions": false,

            "FileGuid": "0ce86285-4865-45af-b77d-1dedda3fb114"

        }

    ],

    "Errors": []

}
```

### Retrieve all productions in a workspace

To retrieve all productions in a workspace, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceId}/productions?{datasourceMode}
```

Set the path parameters in the URL as follows:

- {WorkspaceId} - the Artifact ID of workspace containing productions to retrieve.

- {datasourceMode} - an optional parameter based on the DataSourceReadMode enumeration. Set with an integer value as follows:

Name Value Description

None 0 Don't return data sources or placeholders.

OnlyDataSources 1 Return only data sources.

DataSourcesAndPlaceholders 2 Return both data sources and placeholders.

The request body is empty.

The response contains a ProductionJobStatusResult object. For field descriptions, see Retrieve the job status of a production .

### Retrieve produced productions for documents

You can retrieve produced productions for documents by using document IDs or a mass operation token.

View a request using document IDs

To retrieve produced productions by using document IDs, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/produced-production
```

The body of the request must include the following fields:

- documentIDs -an array of Artifact IDs for the documents with produced productions to retrieve.

- excludeNonReproducible - a Boolean value indicating whether to return non-reproducible productions. The default value is false.

Copy

```text
1
2
3
4
5
6
"documentIDs":[

             {{documentID}},

             {{documentID}}

      ],

    "excludeNonReproducible": {{excludeNonReproducible}}

}
```

View a request using a mass operation token

To retrieve produced productions for a collection of documents by using a mass operation token, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/tokens/{token}/produced-production?{excludeNonReproducible}
```

Set the path parameters in the URL as follows:

- {workspaceID} - the Artifact ID of workspace containing produced productions to retrieve.

- {token} - a GUID used as database token to represent the collection of documents with produced productions.

- { excludeNonReproducible} - a Boolean value indicating whether to return non-reproducible productions. The default value is false.

The request body is empty.

The response contains a ProductionJobStatusResult object. For field descriptions, see Retrieve the job status of a production .

### Retrieve a token for paging through images

To retrieve a unique token associated with this call to page through images, send a GET request with a URL in the following format:

Copy

```text
1
<host>//Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/production-images/token
```

The request body is empty.

The response contains the GUID for the token as a string.

Copy

```text
1
29591b23-f692-4a9e-b10c-0be5b52d6b1a
```

## Production errors and document conflicts

This section contains code samples that illustrate how to retrieve information about production errors and document conflicts.

### Retrieve conflicts, errors, and other production information

To retrieve document conflicts, production errors, and information about whether the production can be run, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/prerun-check
```

The request body is empty.

View field descriptions for a response

- ConflictMessage - a message providing information about document conflicts.

- ProductionErrors - an array of error messages for the production.

- CanContinue - a Boolean value indicating whether the production is able to continue running.

- ContinueMessage - a string providing information about the ability of the production to continue running.

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
{

    "ConflictMessage": "There are 2 conflicts between the documents in this Production and the Production Restriction.",

    "ProductionErrors": [

        "Trying to produce documents as Images, but there are documents in the data source that do not have Images."

    ],

    "CanContinue": false,

    "ContinueMessage": "CannotContinue"

}
```

### Retrieve staging errors for a production

To retrieve staging errors for a production, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{workspaceID}/productions/{productionID}/staging-errors
```

The request body is empty.

View field descriptions for a response

- ErroredDocumentCount - an integer representing the number of documents that errored during staging.

- DuplicateDocuments - contains the following fields:

- Name - the name of a document found to be a duplicate.

- DataSourceNames - an array of data sources where the document was found to be duplicated.

- ErrorMessage - a message with information about the documents that errored during staging.

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
[

  {

    "ErroredDocumentCount": 0,

    "DuplicateDocuments": [

      {

        "Name": "string",

        "DataSourceNames": [

          "string"

        ]

      }

    ],

    "ErrorMessage": "string"

  }

]
```

### Retrieve branding errors for a production

To retrieve branding errors for a production, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{workspaceID}/productions/{productionID}/branding-errors
```

The request body is empty.

View field descriptions for a response

The response contains a specified number of branding errors for a production. The MaxListItems instance setting controls the number of branding errors returned.

This method returns an empty list if the production isn't in an errored state or if the user doesn't have permission to view the errored documents.

The response contains an array of BrandingError objects that contain the following fields:

- DocumentName - a string identifying the errored document.

- DocumentID - the Artifact ID of the document.

- FileID - the ID of the file that wasn't branded. It is provided for documents with multiple pages.

- ErrorMessage - a string contains branding error messages.

### Retrieve documents conflicting with production restrictions

To retrieve a list of documents that conflict with production restrictions, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/document-conflicts
```

The request body is empty.

View field descriptions for a response

- ProductionRestrictions - contains the following fields:

- SavedSearchID - the Artifact ID of the saved search used for the production restriction on the workspace. If no restriction exists, this field is 0.

- SavedSearchName - the user-friendly name of the saved search. If no restriction exists, this field is an empty string.

- DocumentIDs - an array of Artifact IDs for documents that conflict with the production restriction on the workspace. If no restriction exists, this list is empty.

- HasOverridePermission - a Boolean value indicating whether the user has permission to override conflicts. This field returns true when the user has edit permissions for productions and override permissions to restrictions.

The response is a status code of 200 for productions with a Staged or Starting status. Other production statuses return a code of 400 with validation errors.

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

    "ProductionRestrictions": {

        "SavedSearchID": 1038052,

        "SavedSearchName": "All Documents"

    },

    "DocumentIDs": [

        1040682

    ],

    "HasOverridePermission": true

}
```

### Remove documents conflicting with production restrictions

You can remove documents from a production that conflict with the restrictions set on a workspace. This endpoint deletes documents from a production with a status of Staged or ErrorStartingProduction . The user must have edit permission to the production set.

Send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/{ProductionID}/document-conflicts
```

The request body is empty.

When the document conflicts are successfully deleted, the response returns the status code of 200.

## Re-production jobs

This section contains code samples that illustrate how to retrieve, run, stage, and cancel re-production jobs.

### Retrieve productions eligible for re-production

To retrieve productions eligible for re-production based on the production type, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspace/{workspaceID}/database-tokens/{databaseToken}/reproduction-types/{reproductionType}/eligible-re-productions
```

Set the path parameters in the URL as follows:

- {workspaceID} - the Artifact ID of workspace containing the productions eligible for re-production.

- {databaseToken} - a GUID used as database token.

-

{reproductionType} - set an integer value for one of the following re-production types:

Reproduction Type Input

Reproduce document 0

Replace document with placeholder 1

Replace placeholder with document 2

The request body is empty.

View field descriptions for a response

- BeginBates - a string representing the beginning Bates number for the production.

- EndBates - a string representing the ending Bates number for the production.

- DateProduced - the date and time that the production was produced.

- ProductionID - the Artifact ID for the production

- Name - the user-friendly name of the production.

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
[

    {

        "BeginBates": "0000001",

        "EndBates": "0000003",

        "DateProduced": "1/1/2020 12:00:00 AM",

        "ProductionID": 1040044,

        "Name": "Eligible Production"

    }

]
```

### Retrieve re-productions for a specific production

To retrieve all the re-productions performed on a specific production, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{workspaceID}/productions/{productionID}/re-productions
```

The request body is empty.

This endpoint requires production view permission.

View field descriptions for a response

- Name - the user-friendly name of the re-production.

- ProductionID - the Artifact ID of the re-production. If the re-production has been deleted, this field is -1.

- IsDeleted - a Boolean value indicating whether the re-production has been deleted.

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
[

    {

        Name: "Re-production One",

        ProductionID: 1017598,

        IsDeleted: false

    },

    {

        Name: "Deleted Re-production",

        ProductionID: -1,

        IsDeleted: true

    }

]
```

### Stage and run a re-production job

To stage and run a re-production job, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/reproduction-jobs/{ReproductionJobID}/stage-and-run
```

The request body is empty.

View field descriptions for a response

The response contains a result object for each production in the re-production job. Each object contains the following fields:

- JobID - the ID of the re-production job.

- Errors - an array of strings providing error messages for a re-production job.

- Messages - an array of strings providing warning messages about the re-production job.

- Warnings - an array of strings providing warnings about the job.

- WasJobCreated - a Boolean value indicating whether the job was created.

- ProductionID - the Artifact ID of the production run in this job.

- WorkspaceID - the Artifact ID of workspace containing the re-production.

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
[

    {

        "JobID": 318,

        "Errors": [],

        "Messages": [],

        "Warnings": [],

        "WasJobCreated": true,

        "ProductionID": 1039838,

        "WorkspaceID": 1024649

    },

    {

        "JobID": 319,

        "Errors": [],

        "Messages": [],

        "Warnings": [],

        "WasJobCreated": true,

        "ProductionID": 1039840,

        "WorkspaceID": 1024649

    }

]
```

### Cancel jobs for a re-production

To cancel all jobs for a re-production, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-productions/{versionNumber}/workspaces/{WorkspaceID}/productions/reproduction-jobs/{ReproductionJobID}/cancel
```

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- NumberOfJobsRequestedForCancel - the total number of production queue jobs requested for the operation.

- NumberOfJobsCancelWasRequestedSuccessfully - the total number of jobs successfully operated on.

- CancelJobResults - an array containing the results for each requested job cancellation. Each job contains the following fields:

- WorkspaceID - the Artifact ID of the workspace containing the production.

- ProductionID - the Artifact ID of the production.

- JobID - the Artifact ID of the production job.

- CancelSuccessfullySent - a Boolean value indicating whether the cancel request was successfully sent.

- Errors - an array of errors that occurred during the cancel operation.

- Errors - an array of error messages for the overall operation.

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
{

    "NumberOfJobsRequestedForCancel": 2,

    "NumberOfJobsCancelWasRequestedSuccessfully": 1,

    "CancelJobResults": [

        {

            "WorkspaceID": 100,

            "ProductionID": 200,

            "JobID": 1,

            "CancelSuccessfullySent": true,

            "Errors": []

        },

        {

            "WorkspaceID": 100,

            "ProductionID": 201,

            "JobID": 2,

            "CancelSuccessfullySent": false,

            "Errors": [

                "This production cannot be canceled."

            ]

        }

    ],

    "Errors": []

}
```

On this page

- Production Manager (REST)

- Guidelines for productions in REST

- URLs

- Postman sample file

- Production sets and jobs

- Create a production set

- Retrieve a production set

- Delete a production set

- Stage a production

- Run a production job

- Stage and run multiple production jobs

- Re-run a production

- Default fields and restrictions for productions

- Retrieve default field values for a production

- Set production restrictions on a workspace

- Retrieve the ID of a save search used for production restrictions

- Production job status, progress, and other information

- Retrieve the job status of a production

- Retrieve progress details for a production

- Retrieve production status details

- Retrieve results for produced image files

- Retrieve all productions in a workspace

- Retrieve produced productions for documents

- Retrieve a token for paging through images

- Production errors and document conflicts

- Retrieve conflicts, errors, and other production information

- Retrieve staging errors for a production

- Retrieve branding errors for a production

- Retrieve documents conflicting with production restrictions

- Remove documents conflicting with production restrictions

- Re-production jobs

- Retrieve productions eligible for re-production

- Retrieve re-productions for a specific production

- Stage and run a re-production job

- Cancel jobs for a re-production


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

---
title: "View Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Data_Visualization/View_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:32+00:00
sha256: ddec45eab1ce8f2e70026b226059f78b885826344c6ed63992bbaf6b6a19e4bc
---

View Manager (REST)

# View Manager (REST)

You can use the View Manager service to create, read, and update Relativity views through REST. It also includes helper endpoints for retrieving the following information:

- A user's permissions on a view and the fields used in the search conditions on the view.

- A list of workspace users who can be assigned ownership of a view.

- A list of object types in a workspace. When creating a view, you can use this list to assign an object type to a view based on the objects that you want displayed in it.

As a sample use case, you could use the View Manager API to add or modify views used in a custom application or through the Relativity UI. For example, you might want to create a view that uses a specific set of search criteria to display custom objects in an application.

You can also use the View Manager service through .NET. For more information, see View Manager (.NET) .

## Guidelines for the View Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve a view:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/views/{viewID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {workspaceID} to the Artifact ID of the workspace that contains the view.

- {viewID} to the Artifact ID of a specific view.

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the View Manager service. To download the sample file, click View Manager Postman file .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Client code sample

To use the View Manager service, send requests by making calls with the required HTTP methods. You can use the following .NET code as a sample client for making calls with the View Manager service. This code illustrates how to perform the following tasks:

- Instantiate an HttpClient object for sending requests and responses using the URL for the View Manager service.

- Set the required headers for the request.

- Set the string represented by inputJSON variable to the JSON input required for your operation.

- Set the url variable to the URL for the operation that you want to perform. This example creates a view.

- Use the PostAsync() method to send a post request.

- Return the results of the request.

View client code sample Copy

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
public async Task<int?> CreateViewExample()

{

    int? result = null; using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization",

            "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("https://localhost/");

        string

            inputJSON = "{"viewRequest":{"ArtifactTypeID":10,"ObjectType":{"Secured":false,"Value":{"ArtifactTypeID":10}},"Order":9999,"VisibleInDropdown":true,"QueryHint":"","RelativityApplications":[],"Owner":{"Secured":false,"Value":{"Name":"Public","ArtifactID":0,"Guids":[]}},"Name":"View

            Name","Fields":[{"ArtifactID":1003667,"Name":"Control

            Number","ViewFieldID":1000186},{"ArtifactID":1035375,"Name":"File

            Size","ViewFieldID":1000574}],"Sorts":[],"Dashboard":null,"GroupDefinitionFieldArtifactID":null,"SearchCriteria":null}}";

        var url = "/Relativity.REST/API/relativity-data-visualization/v1/workspaces/-1/views/";

        var response = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json"));

        response.EnsureSuccessStatusCode();

        var content = await response.Content.ReadAsStringAsync();

        result = JsonConvert.DeserializeObject<int>(content);

    }

    return result;

}
```

## Create a view

To create a new view, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/views
```

View the descriptions of fields required to create a view

The body of the request must contain a viewRequest field, which represents a request for creating a view. The following fields are required unless specifically identified as optional:

- ArtifactTypeID - the Artifact Type ID of the object that the view is assigned to. For example, the Artifact Type ID for a view assigned to the Document object is 10.

- ObjectType - contains information about the object type associated with the view. It includes these fields:

- Secured - indicates whether the current user has permissions to view the setting in the Value field.

- Value - contains the following fields:

- Name - the name of the object type.

- ArtifactTypeID - the ID for the artifact type of the object.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs for the object type.

- Order - the position of the view in the view drop-down list. For more information, see Views on the Relativity Documentation site.

- VisibleInDropdown - a Boolean value indicating whether the view is visible in the view drop-down list.

- QueryHint - a string parameter used to optimize the view. For more information, see Views on the Relativity Documentation site.

- RelativityApplications - the Relativity applications associated with the view.

- Owner - an object identifier for the user who owns the view. It contains the following fields:

- Secured - indicates whether the current user has permissions to view the settings in the Value field.

- Value - contains the following fields:

- Name - the name of the owner

- ArtifactID - the Artifact ID of the user who owns the view. An ArtifactID set to 0 indicates that the view is public.

- Guids - an array of GUIDs for the owner.

- Name - a user-friendly name for the view.

- Fields - the fields that you want included in the view result set. You must include at least one field in the view. It has the following fields:

- ArtifactID - the Artifact ID of the field. You can omit this field if you specify the Name or ViewFieldID.

- Name - a user-friendly name for the field, such as Control Number or File Size. You can omit this field if you specify the ArtifactID or ViewFieldID.

- ViewFieldID - a unique identifier used to reference a field. You can omit this field if you specify the ArtifactID or Name.

- Sorts - the sort order for view results specified as a collection of Sort objects. This field is optional.

The Sorts object contains the following fields:

- FieldIdentifier - includes the Artifact ID for the view field, and the Name of the field. You can omit the Artifact ID if you specify the Name, and vice versa.

- Direction - indicates whether the data is sorted in ascending or descending order.

- Order - the position of the view in the view drop-down list. For more information, see Views on the Relativity Documentation site.

- Dashboard - a Dashboard object contains properties, such as the Artifact ID of the dashboard, its name, and a list of GUIDs associated with it.

- GroupDefinitionFieldArtifactID - indicates the field used for grouping a list. It used only for the Document object type. This field is optional and can be set to null.

- SearchCriteria - the optional conditions specified for a query used by the view.

To search for data, you can use a variety of query options, including conditions, fields, sorts, and relational fields. These query options have a specific syntax for defining the for defining query conditions. For information about query conditions and options, see Query for resources .

The SearchCriteria field contains the following fields based on the query provided in the sample JSON request listed in this section:

- Conditions - an array of Condition objects. The Condition objects includes the following fields:

- FieldIdentifier - includes the Artifact ID for the field, and the Name of the field. You can omit the Artifact ID if you specify the Name, and vice versa.

- ConditionType - a field condition, such as Criteria.

- Operator - a comparison operator such as GreaterThan.

- NotOperator - a Boolean value used to indicate whether a condition is negated.

- Value - a value used for comparison with a field, such as 2000.

- BooleanOperator - an operator used to join multiple conditions.

View the JSON request for creating a view Copy

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
{

    "viewRequest": {

        "ArtifactTypeID": 10,

        "ObjectType": {

            "Secured": false,

            "Value": {

                "ArtifactTypeID": 10

            }

        },

        "Order": 9999,

        "VisibleInDropdown": true,

        "QueryHint": "",

        "RelativityApplications": [],

        "Owner": {

            "Secured": false,

            "Value": {

                "Name": "Public",

                "ArtifactID": 0,

                "Guids": []

            }

        },

        "Name": "View Name",

        "Fields": [

            {

                "ArtifactID": 1003667,

                "Name": "Control Number",

                "ViewFieldID": 1000186

            },

            {

                "ArtifactID": 1035375,

                "Name": "File Size",

                "ViewFieldID": 1000574

            }

        ],

        "Sorts": [],

        "Dashboard": null,

        "GroupDefinitionFieldArtifactID": null,

        "SearchCriteria": null

    }

}
```

The response contains the Artifact ID of the newly created view.

## Retrieve information about a view

To retrieve the properties of a view, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/views/{viewID}
```

The body of the request is empty.

View the field descriptions for a response

- ObjectIdentifier - contains the following fields:

- Name - the user-friendly name of a view.

- ArtifactID - the Artifact ID of the view.

- ObjectType - contains information about the object type associated with the view. It includes these fields:

- Secured - indicates whether the current user has permissions to view the settings in the Value field.

- Value - contains the following fields:

- ArtifactTypeID - the ID for the artifact type of the object.

- Name - the name of the object type.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs for the object type.

- Owner - an object identifier for the user who owns the view. It contains the following fields:

- Secured - indicates whether the current user has permissions to view the settings in the Value field.

- Value - contains the following fields:

- Name - the name of the owner.

- ArtifactID - the Artifact ID of the user who owns the view. An ArtifactID set to 0 indicates that the view is public.

- Guids - an array of GUIDs for the owner.

- Order - the position of the view in the view drop-down list. For more information, see Views on the Relativity Documentation site.

- VisibleInDropdown - a Boolean value indicating whether the view is displayed in the view drop-down list.

- QueryHint - a string parameter used to optimize the view. For more information, see Views on the Relativity Documentation site.

- RelativityApplications - a list of identifiers representing Relativity applications that contain the current view. It includes these fields:

- HasSecuredItems - indicates whether the list contains one or more items that aren't accessible to the current user.

- ViewableItems - an array of items (accessible to the current user) that describe the applications that contain the current view.

- SearchCriteria - the optional conditions specified for a query used by the view.

The SearchCriteria field contains the following fields based on the query provided in the sample JSON request listed in this section:

- Conditions - an array of Condition objects. The Condition objects includes the following fields:

- FieldIdentifier - includes the Artifact ID for the field, and the Name of the field. You can omit the Artifact ID if you specify the Name, and vice versa.

- ConditionType - a field condition, such as Criteria.

- Operator - a comparison operator such as GreaterThan.

- NotOperator - a Boolean value used to indicate whether a condition is negated.

- Value - a value used for comparison with a field, such as 2000.

- BooleanOperator - an operator used to join multiple conditions.

- Fields - the fields included in the view result set. This fields are specified as a collection of FieldRef objects.

- HasSecuredItems - indicates whether the list contains one or more items that aren't accessible to the current user.

- ViewableItems - an array of items (accessible to the current user) that describe the fields for the current view.

- ArtifactID - the Artifact ID of the field.

- ViewFieldID - a unique identifier used to reference a field.

- Guids - an array of GUIDs for the field.

- Name - a user-friendly name for the field.

- Sorts - the sort order for view results specified as a collection of Sort objects. This field indicates whether the results are sorted in ascending or descending order, identifies a field by Artifact ID and GUID, and specifies a sort order.

- FieldIdentifier - includes the Artifact ID for the field, and the Name of the field. You can omit the Artifact ID if you specify the Name, and vice versa.

- Order - the position of the view in the view drop-down list. For more information, see Views on the Relativity Documentation site.

- Direction - indicates whether the data is sorted in ascending or descending order.

- CreatedBy - the name and unique identifier for the user who created the view.

- Secured - - indicates whether the current user has permissions to view the setting in the Value field.

- Value - contains the following fields:

- Name - the name of the user.

- ArtifactID - the Artifact ID of the user.

- Guids - an array of GUIDs for the user.

- LastModifiedBy - the name and unique identifier for the user who last updated the view. See field descriptions for the CreatedBy field.

- IsVisible - a Boolean value indicating whether the view is visible in the system.

- IsSystemView - a Boolean value indicating whether the view is a system view. Relativity contains system views that are provided as part of the application by default. You can't edit all system views, such as the workspace system view. For more information, see Views on the Relativity Documentation site.

- IsRelationalFieldView - a Boolean value indicating whether the view is used to display relational fields.

- Dashboard - a Dashboard object contains properties that includes the following properties:

- Secured - - indicates whether the current user has permissions to view the settings in the Value field.

- Value - contains the following fields:

- Name - the name of the dashboard.

- ArtifactID - the Artifact ID of the dashboard.

- Guids - an array of GUIDs for the dashboard.

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
{

    "ObjectIdentifier": {

        "Name": "All Workspaces",

        "ArtifactID": 112

    },

    "ObjectType": {

        "Secured": false,

        "Value": {

            "ArtifactTypeID": 8,

            "Name": "Workspace",

            "ArtifactID": 0,

            "Guids": []

        }

    },

    "Owner": {

        "Secured": false,

        "Value": {

            "Name": "",

            "ArtifactID": 0,

            "Guids": []

        }

    },

    "Order": 1,

    "VisibleInDropdown": true,

    "QueryHint": "",

    "RelativityApplications": {

        "HasSecuredItems": true,

        "ViewableItems": []

    },

    "SearchCriteria": {

        "Conditions": [

            {

                "Condition": {

                    "ConditionType": "Criteria",

                    "Operator": "IsLike",

                    "FieldIdentifier": {

                        "ArtifactID": -1,

                        "ViewFieldID": 50,

                        "Guids": [],

                        "Name": "Client Name"

                    },

                    "NotOperator": true,

                    "Value": "Relativity Template"

                },

                "BooleanOperator": "Or",

                "HasPermission": true

            },

            {

                "Condition": {

                    "ConditionType": "Criteria",

                    "Operator": "Is",

                    "FieldIdentifier": {

                        "ArtifactID": 1016319,

                        "ViewFieldID": 46,

                        "Guids": [],

                        "Name": "Name"

                    },

                    "NotOperator": false,

                    "Value": "Smoke TestCase"

                },

                "BooleanOperator": "None",

                "HasPermission": true

            }

        ],

        "BooleanOperator": "None"

    },

    "Fields": {

        "HasSecuredItems": false,

        "ViewableItems": [

            {

                "ArtifactID": -1,

                "ViewFieldID": 53,

                "Guids": [],

                "Name": "Edit"

            },

            {

                "ArtifactID": 1017488,

                "ViewFieldID": 1000562,

                "Guids": [

                    "0a813d44-a3bf-4e4e-a73d-82c89322260a"

                ],

                "Name": "Pin"

            },

            {

                "ArtifactID": 1016319,

                "ViewFieldID": 46,

                "Guids": [],

                "Name": "Name"

            },

            {

                "ArtifactID": -1,

                "ViewFieldID": 50,

                "Guids": [],

                "Name": "Client Name"

            },

            {

                "ArtifactID": -1,

                "ViewFieldID": 54,

                "Guids": [],

                "Name": "Matter Name"

            },

            {

                "ArtifactID": -1,

                "ViewFieldID": 1000563,

                "Guids": [],

                "Name": "Instance Name"

            }

        ]

    },

    "Sorts": [

        {

            "FieldIdentifier": {

                "ArtifactID": 1016319,

                "ViewFieldID": 46,

                "Guids": [],

                "Name": "Name"

            },

            "Order": 0,

            "Direction": "Descending"

        }

    ],

    "CreatedBy": {

        "Secured": false,

        "Value": {

            "Name": "Admin, Relativity",

            "ArtifactID": 9,

            "Guids": []

        }

    },

    "LastModifiedBy": {

        "Secured": false,

        "Value": {

            "Name": "Service Account, Relativity",

            "ArtifactID": 777,

            "Guids": []

        }

    },

    "IsVisible": true,

    "IsSystemView": false,

    "IsRelationalFieldView": false,

    "Dashboard": {

        "Secured": true

    }

}
```

## Update a view

To modify the properties of a view, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/views
```

View field descriptions for a request

The body of the request must contain a viewRequest field, which represents a request for creating a view. The following fields are required unless specifically identified as optional:

- ArtifactID - the Artifact ID of the view that you want to update.

- ArtifactTypeID - the Artifact Type ID of the object that the view is assigned to. For example, the Artifact Type ID for a view assigned to the Document object is 10.

- Order - the position of the view in the view drop-down list. For more information, see Views on the Relativity Documentation site.

- VisibleInDropdown - a Boolean value indicating whether the view is visible in the view drop-down list.

- QueryHint - a string parameter used to optimize the view. For more information, see Views on the Relativity Documentation site.

- RelativityApplications - the Relativity applications associated with the view.

- Owner - the user who owns the view. The Owner object has the following fields:

- ArtifactID - the Artifact ID of the user who owns the view. An ArtifactID set to 0 indicates that the view is public.

- Name - the string used to identify the owner. For example, Public is the name assigned to a view visible to all users. This field is optional.

- Name - a user-friendly name for the view.

- Fields - the fields that you want included in the view result set. You must include at least one field in the view. It has the following fields:

- ArtifactID - the Artifact ID of the field. You can omit this field if you specify the Name or ViewFieldID.

- Name - a user-friendly name for the field, such as Control Number or File Size. You can omit this field if you specify the ArtifactID or ViewFieldID.

- ViewFieldID - a unique identifier used to reference a view field. You can omit this field if you specify the ArtifactID or Name.

- Sorts - the sort order for view results specified as a collection of Sort objects. This field is optional.

The Sorts object contains the following fields:

- FieldIdentifier - includes the Artifact ID for the view field, and the Name of the field. You can omit the Artifact ID if you specify the Name, and vice versa.

- Direction - indicates whether the data is sorted in ascending or descending order.

- Order - the position of the view in the view drop-down list. For more information, see Views on the Relativity Documentation site.

- GroupDefinitionFieldArtifactID - indicates the field used for grouping a list. It used only for the Document object type. This field is optional and can be set to null.

- SearchCriteria - the optional conditions specified for a query used by the view.

The SearchCriteria object contains the following fields based on the query provided in the sample JSON request listed in this section:

- Conditions - an array of Condition objects. The Condition objects includes the following fields:

- FieldIdentifier - includes the Artifact ID for the field, and the Name of the field. You can omit the Artifact ID if you specify the Name, and vice versa.

- ConditionType - a field condition, such as Criteria.

- Operator - a comparison operator such as GreaterThan.

- NotOperator - a Boolean value used to indicate whether a condition is negated.

- Value - a value used for comparison with a field, such as 2000.

- BooleanOperator - an operator used to join multiple conditions.

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
{

    "viewRequest": {

        "ArtifactID": 1039692,

        "ArtifactTypeID": 10,

        "Order": 100,

        "VisibleInDropdown": true,

        "QueryHint": "",

        "RelativityApplications": [],

        "Owner": {

            "ArtifactID": 0,

            "Name": "Public"

        },

        "Name": "My View",

        "Fields": [

            {

                "ArtifactID": 1003667,

                "Name": "Control Number",

                "ViewFieldID": 1000186

            },

            {

                "ArtifactID": 1035375,

                "Name": "File Size",

                "ViewFieldID": 1000574

            }

        ],

        "Sorts": [

            {

                "FieldIdentifier": {

                    "ViewFieldID": 1000574,

                    "Name": "File Size"

                },

                "Direction": "Descending",

                "Order": 10

            }

        ],

        "GroupDefinitionFieldArtifactID": null,

        "SearchCriteria": {

            "Conditions": [

                {

                    "Condition": {

                        "FieldIdentifier": {

                            "ArtifactID": 1035375,

                            "Name": "File Size"

                        },

                        "ConditionType": "Criteria",

                        "Operator": "GreaterThan",

                        "NotOperator": false,

                        "Value": 2000

                    },

                    "BooleanOperator": "None"

                }

            ],

            "BooleanOperator": "None"

        }

    }

}
```

The response for an update operation contains the same fields as those for a read response. See the field descriptions for the response in Retrieve information about a view .

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
{

    "ObjectIdentifier": {

        "Name": "My View",

        "ArtifactID": 1039692

    },

    "ObjectType": {

        "Secured": false,

        "Value": {

            "ArtifactTypeID": 10,

            "Name": "Document",

            "ArtifactID": 0,

            "Guids": []

        }

    },

    "Owner": {

        "Secured": false,

        "Value": {

            "Name": "",

            "ArtifactID": 0,

            "Guids": []

        }

    },

    "Order": 100,

    "VisibleInDropdown": true,

    "QueryHint": "",

    "RelativityApplications": {

        "HasSecuredItems": true,

        "ViewableItems": []

    },

    "SearchCriteria": {

        "Conditions": [

            {

                "Condition": {

                    "ConditionType": "Criteria",

                    "Operator": "GreaterThan",

                    "FieldIdentifier": {

                        "ArtifactID": 1035375,

                        "ViewFieldID": 1000574,

                        "Guids": [

                            "1287c045-cf79-44b6-8a0a-0c8d7d60d745"

                        ],

                        "Name": "File Size"

                    },

                    "NotOperator": false,

                    "Value": 2000.0

                },

                "BooleanOperator": "None",

                "HasPermission": true

            }

        ],

        "BooleanOperator": "None"

    },

    "Fields": {

        "HasSecuredItems": false,

        "ViewableItems": [

            {

                "ArtifactID": 1003667,

                "ViewFieldID": 1000186,

                "Guids": [

                    "2a3f1212-c8ca-4fa9-ad6b-f76c97f05438"

                ],

                "Name": "Control Number"

            },

            {

                "ArtifactID": 1035375,

                "ViewFieldID": 1000574,

                "Guids": [

                    "1287c045-cf79-44b6-8a0a-0c8d7d60d745"

                ],

                "Name": "File Size"

            }

        ]

    },

    "Sorts": [

        {

            "FieldIdentifier": {

                "ArtifactID": 1035375,

                "ViewFieldID": 1000574,

                "Guids": [

                    "1287c045-cf79-44b6-8a0a-0c8d7d60d745"

                ],

                "Name": "File Size"

            },

            "Order": 0,

            "Direction": "Descending"

        }

    ],

    "CreatedBy": {

        "Secured": false,

        "Value": {

            "Name": "Admin, Relativity",

            "ArtifactID": 9,

            "Guids": []

        }

    },

    "LastModifiedBy": {

        "Secured": false,

        "Value": {

            "Name": "Admin, Relativity",

            "ArtifactID": 9,

            "Guids": []

        }

    },

    "IsVisible": true,

    "IsSystemView": false,

    "IsRelationalFieldView": false,

    "Dashboard": {

        "Secured": true

    }

}
```

## Retrieve the access status of a user

To retrieve a list of users with View permissions to a view and the fields used in the criteria for the search conditions on it, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/views/{viewID}/access-status
```

The request body is empty.

The response returns the following fields:

- Exists - a Boolean value indicating whether the specified view exists.

- CanView - a Boolean value indicating whether a user has View permissions on the specified view. For more information, see Security and Permissions on the Relativity Server 2025 Documentation site.

- CanViewCriteriaFields - a Boolean value indicating whether a user has View permissions on all fields used in the criteria for a search conditions on the view.

Copy

```text
1
2
3
4
5
{

 "Exists": true,

 "CanView": true,

 "CanViewCriteriaFields": true

}
```

## Retrieve users for view ownership

You can retrieve a list of users eligible to be view owners in a specific workspace. You can then use this list to assign owners to a view. To be designated as an owner, a user must have View permissions for views. For more information, see Security and Permissions on the Relativity Documentation site.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/views/{viewID}/eligible-owners
```

The request body is empty.

The response is an array of UserRef objects containing the following fields:

- Name - the name of the user.

- ArtifactID - the Artifact ID of a user. An ArtifactID set to 0 indicates that the view is public.

- Guids - an array of GUIDs for the user.

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
[

    {

        "Name": "Public",

        "ArtifactID": 0,

        "Guids": []

    },

    {

        "Name": "Admin, Relativity",

        "ArtifactID": 9,

        "Guids": []

    },

    {

        "Name": "Service Account, Relativity",

        "ArtifactID": 777,

        "Guids": []

    }

]
```

## Retrieve a list of object types in a workspace

You can retrieve a list of object types in a specific workspace. You can select an object type from this list that is used for populating the ObjectType field for the View object.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-data-visualization/{versionNumber}/workspaces/{workspaceID}/eligible-object-types
```

The request body is empty.

The response is an array of ObjectTypeRef objects containing the following fields:

- ArtifactTypeID - the ID for the artifact type of the object.

- Name - the name of the object type.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs for the object type.

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
[

 {

 "ArtifactTypeID": 0,

 "Name": "Analytics Categorization Result",

 "ArtifactID": 0,

 "Guids": []

 },

 {

 "ArtifactTypeID": 0,

 "Name": "Analytics Categorization Set",

 "ArtifactID": 0,

 "Guids": []

 },

 ....

]
```

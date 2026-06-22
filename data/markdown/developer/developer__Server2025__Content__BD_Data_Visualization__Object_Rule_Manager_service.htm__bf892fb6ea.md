---
title: "Object Rule Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Data_Visualization/Object_Rule_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:22:52+00:00
sha256: 4531ba3ff0742b884cb04790134616d51c9c9d415abe4af4cd1aadb9b339688f
---

Object Rule Manager (REST)

# Object Rule Manager (REST)

You can use object rules to further customize the behavior of the object types that you create. The Object Rule Manager service simplifies this process by supporting CRUD operations on object rules. It also provides helper methods for retrieving information about associative objects, layouts, choices and choice fields used when creating or updating an object rule.

You can also work with this service through .NET. For more information, see Object Rule Manager (.NET) .

## Postman sample files

You can use the Postman sample files to become familiar with making calls to endpoints on the services. To download the sample files, click V1 Object Rule postman_collection.zip .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Guidelines for the Object Rule Manager service

Review the following guidelines for the Object Rule Manager service:

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

## Fundamentals for Object Rule Manager service

- Use the Object Rule Manager service to work with the same object rule types available through the Relativity UI. For general information about object rules, see Adding an object rule View a list of available object rules

- Choice behavior - controls whether the users can add or delete choices for fields.

- Custom single object add link visibility - controls the availability of the Add link button used to add RDO instances to existing custom single objects from a layout.

- Default layout - determines whether the user sees the default or any layout for the object type.

- Default layout on new - determines the layout displayed when a user creates a new custom object.

- Global button visibility - controls the visibility of specific buttons or action options for an object type.

- Mass action visibility - controls the visibility of buttons for the mass operations for an object type.

- New button override - overrides the page displayed when the New button is clicked by specifying a custom button label and page URL.

- Sub-list button visibility - controls the display of the buttons for child and associative object lists.

- Override edit link URL - overrides the page displayed when the Edit link is clicked by specifying custom link text and a page URL.

- Override view link URL - overrides the page displayed when the View link is clicked by specifying custom link text and a page URL.

- Use helper endpoints to retrieve information that you need when creating or updating an object rule. See the following table for suggested uses.

Create or update this object rule Use these helper endpoints Compares to this UI field

Choice Behavior

availablechoicefields Field

Default Layout

availablelayouts Action

availablechoicefields Field

availablechoices Value

Default Layout on New

availablelayouts Action

Sub-List Button Visibility

availablechoicefields Field

availablechoices Value

availableassociatedobjects Associative/Child Object

- If a call to a helper endpoint returns an empty array, you can't create that object rule on the object type.

- To attach an object rule, the object type must be an RDO and non-system object, or a document object type.

- Use -1 for the workspace ID when you want to indicate the admin-level context.

- To retrieve the Artifact ID of an object rule, use the Object Manager Service. For more information, see Object Manager (REST) .

## Create an object rule

You can create object rules by sending a POST request to the appropriate URL for the rule type. For general information about these object rules, see Adding an object rule .

Click the following drop-down links to view URLs and sample requests for sub-list visibility, choices, and layouts rules. You can find the URLs and JSON request formats for other object type rules in the Postman file provided for this service. For more information, see Postman sample files .

For the URLs in these examples, set the {WorkspaceID} variable to the Artifact ID of the workspace containing the object type, or use -1 to indicate the admin-level context.

View a list of URLs for all create endpoints

- Choice behavior Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/choice-behavior
```

- Custom single object add link visibility Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/custom-single-object-add-link-visibility
```

- Default layout Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/default-layout
```

- Default layout on new Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/default-layout-on-new
```

- Global button visibility Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/global-button-visibility
```

- Mass action visibility Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/mass-action-visibility
```

- New button override Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/new-button-override
```

- Sub-list button visibility Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/sub-list-button-visibility
```

- Override edit link URL Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/override-edit-link
```

- Override view link URL Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/override-view-link
```

View a JSON request for creating a rule for sub-list button visibility

To create a sub-list visibility rule, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/sub-list-button-visibility
```

The body of the request must contain the following fields unless specifically identified as optional:

- objectRuleRequest - request to create or update a rule. It contains the following fields:

- Name - the user-friendly name of the rule.

- ObjectType - contains the Artifact ID of the object type.

- Field - contains a Value specifying the Artifact ID of the field, which affects the button visibility.

- Choice - contains a Value specifying the Artifact ID of the choice, which affects the button visibility.

- SubListObject - contains a Value specifying the Artifact ID of the associative object list controlled by the rule.

- ShowNew - a Boolean value indicating whether to display the New button on the associative object list. The default value is true.

- ShowLink - a Boolean value indicating whether to display the Link button on the associative object list. The default value is true.

- ShowUnlink - a Boolean value indicating whether to display the Unlink button on the associative object list. The default value is true.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The object rule is linked to the applications in this array. If the array is empty, then the object rule isn't linked to any application.

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
{

    "objectRuleRequest":{

         "Name": "Sample rule for sublist button",

         "ObjectType": {

            "ArtifactID": 1042378

        },

        "Field": {

            "Value": {

                "ArtifactID": 1042566

            }

        },

        "Choice": {

            "Value": {

                "ArtifactID": 1042568

            }

        },

        "SubListObject": {

            "Value": {

                "ArtifactID": 1042586

            }

        },

        "ShowNew": true,

        "ShowLink": false,

        "ShowUnlink": false,

        "RelativityApplications": []

    }

}
```

View a JSON request for creating a choice rule

To create a choice rule, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/choice-behavior
```

The body of the request must contain the following fields unless specifically identified as optional:

- objectRuleRequest - request to create or update a rule. It contains the following fields:

- Name - the user-friendly name of the rule.

- ObjectType - contains the Artifact ID of the object type.

- AllowAdd - a Boolean value indicating whether the user can mass copy choices.

- AllowDelete - a Boolean value indicating whether the user can mass delete choices.

- AllowRename - a Boolean value indicating whether the user can rename a choice.

- Field - contains a Value specifying the Artifact ID of the field, which affects the choice behavior.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The object rule is linked to the applications in this array. If the array is empty, then the object rule isn't linked to any application.

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
{

    "objectRuleRequest":{

        "Name": "Sample Rule One",

        "ObjectType": {

            "ArtifactID": 1042378

        },

        "AllowAdd": true,

        "AllowDelete": true,

        "AllowRename": true,

        "Field": {

            "Value": {

                "ArtifactID": 1042565

            }

        },

        "RelativityApplications": []

      }

}
```

View a JSON request for creating a layout rule

To create a layout rule, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/default-layout
```

The body of the request must contain the following fields unless specifically identified as optional:

- objectRuleRequest - request to create or update a rule. It contains the following fields:

- Name - the user-friendly name of the rule.

- ObjectType - contains the Artifact ID of the object type.

- Field - contains a Value specifying the Artifact ID of the field, which controls the layout behavior.

- Layout - contains a Value specifying the Artifact ID of the layout.

- Choice - contains a Value specifying the Artifact ID of the choice, which controls the layout behavior.

- AllowLayoutChange - a Boolean value indicating whether the user can select another layout. The default value is false.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The object rule is linked to the applications in this array. If the array is empty, then the object rule isn't linked to any application.

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
{

    "objectRuleRequest":{

        "Name": "Sample rule for layout",

        "ObjectType": {

            "ArtifactID": 1042378

        },

        "Field": {

            "Value": {

                "ArtifactID": 1042566

            }

        },

        "Layout": {

            "Value": {

                "ArtifactID": 1042594

            }

        },

        "Choice": {

            "Value": {

                "ArtifactID": 1042569

            }

        },

        "AllowLayoutChange": false,

        "RelativityApplications": []

    }

}
```

When the request is successful, the response contains the Artifact ID of the new object rule. It also returns the status code of 200.

## Read an object rule

You can retrieve basic information about an object rule or extended information, which also includes operations that you have permissions to perform on the object rule.

- Retrieve basic metadata for an object rule - send a GET request with a URL in the following general format: Copy

```text
1
<host>/Relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/{ObjectRuleId}
```

- Retrieve extended metadata for an object rule - send a GET request with a URL in the following general format: Copy

```text
1
<host>/Relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/{ObjectRuleId}?includeMetadata=true&includeActions=true
```

For both requests, set the {WorkspaceID} variable to the Artifact ID of a workspace or use -1 to indicate the admin-level context. Set the {ObjectRuleId} variable to the Artifact ID of the object rule that you want to read, and leave the body of the request empty.

View descriptions of fields in the response

- Behavior - indicates the type of object rule, such as sub-list visibility, or choice behavior. See Create an object rule .

- Field - contains the following fields:

- Secured - indicates whether the current user has permission to view the settings in the Value field.

- Value - contains the following fields:

- Name - the user-friendly name of the field.

- ArtifactID - the Artifact ID of the field.

- Guids - an array of GUIDs used to identify the field.

- Layout - contains the following fields:

- Secured - indicates whether the current user has permission to view the settings in the Value field.

- Value - contains the following fields:

- Name - the user-friendly name of the layout.

- ArtifactID - the Artifact ID of the layout.

- Guids - an array of GUIDs used to identify the layout.

- Choice - contains the following fields:

- Secured - indicates whether the current user has permission to view the settings in the Value field.

- Value - contains the following fields:

- Name - the user-friendly name of the choice.

- ArtifactID - the Artifact ID of the choice.

- Guids - an array of GUIDs used to identify the choice.

- SubListObject - contains the following fields:

- Secured - indicates whether the current user has permission to view the settings in the Value field.

- Value - contains the following fields:

- Name - the user-friendly name of the associated object. This is the name of the field that connects the associated object type.

- ObjectTypeName - the name of the object type that the associated object is an instance.

- If the list type is ChildObject, it returns the object type name of the child object.

- If the list type is MultipleObjectField, it returns the object type name of the multiple object field.

- If the list type is SingleObjectField, it returns the object type name of the single object field.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- ArtifactID - the artifactID of the field associating the objects.

- Guids - an array of GUIDs used to identify the associated object.

- ListType - the type of associative objects that the list contains. View list of ListType values

The ListType field contains one of the following values:

- ChildObject - indicates that the list contains associated child objects.

- MultipleObjectField - indicates that the list contains associated multiple object field types.

- SingleObjectField - indicates that the list contains associated single object field types.

- AllowAdd - a Boolean value indicating whether the user can mass copy choices.

- AllowDelete - a Boolean value indicating whether the user can mass delete choices.

- AllowRename - a Boolean value indicating whether the user can rename choices.

- ShowDelete - a Boolean value indicating whether the Delete button is available for global or sub-list button visibility. For example, it controls whether the button displays for mass operations or on the detail view of an object.

- ShowAddLink - a Boolean value indicating whether the Add link button is available for custom single object add link visibility. For example, it controls whether the Add link button can be used to add RDO instances to existing custom single objects from a layout.

- AllowLayoutChange - a Boolean value indicating whether the user can select another layout. The default value is false.

- ShowNew - a Boolean value indicating whether to display the New button on the associative object list. The default value is true.

- ShowLink - a Boolean value indicating whether to display the Link button on the associative object list. The default value is true.

- ShowUnlink - a Boolean value indicating whether to display the Unlink button on the associative object list. The default value is true.

- ShowMassCopy - a Boolean value indicating whether to display the Copy option for mass operations on an object. The mass action visibility rule controls this behavior.

- ShowMassEdit - a Boolean value indicating whether to display the Edit option for mass operations on an object. The mass action visibility rule controls this behavior.

- ShowMassReplace - a Boolean value indicating whether to display the Replace option for mass operations on an object. The mass action visibility rule controls this behavior.

- ShowMassTally - a Boolean value indicating whether to display the Tally/Sum/Average option for mass operations on an object. The mass action visibility rule controls this behavior.

- RelativityApplications - contains the following fields:

- HasSecuredItems - a Boolean value indicating whether the application contains items that the current user doesn't have permission to access.

- ViewableItems - an array of identifier objects for items that are accessible to the current user. For example, an object in this array would contain the name, Artifact IDs, and GUIDs for an application.

- ObjectType - represents the object type that the rule is assigned to. It contains the following fields:

- Name - the user-friendly name for the object type.

- ArtifactTypeID - an identifier used to specify an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs used to identify the object type.

- Meta - provides additional information available as extended metadata. It includes the following fields:

- Unsupported - an array of properties that indicate functionality not available on the current instance of this object rule.

- ReadOnly - an array of object type properties that can't be modified, such as the type of rule.

- Actions - an array of Action objects indicating operations that you have permissions to perform on this object rule. For example, you may not have permissions to modify an object rule. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the object rule, such as delete, update, and so on.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this object rule.

- Reason - an explanation for the unavailability of an action.

- LastModifiedOn - the date and time when the object rule was most recently modified.

- LastModifiedBy - contains the Artifact ID and name of the user who recently updated the object rule. It also contains an array of GUIDs used to identify the user.

- CreatedOn - the date and time when the object type was added to Relativity.

- CreatedBy - contains the Artifact ID and name of the user who created the object type. It also contains an array of GUIDs used to identify the user.

- Name - the user-friendly name for the object rule.

- ArtifactID - the Artifact ID of the object rule.

- Guids - an array of GUIDs used to identify the object rule.

View the JSON response for a basic metadata request Copy

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
{

    "Behavior": "SubListButtonVisibility",

    "Field": {

        "Secured": false,

        "Value": {

            "Name": "Custom Single Choice Field",

            "ArtifactID": 1042566,

            "Guids": []

        }

    },

    "Choice": {

        "Secured": false,

        "Value": {

            "Name": "Green",

            "ArtifactID": 1042568,

            "Guids": []

        }

    },

    "SubListObject": {

        "Secured": false,

        "Value": {

            "Name": "Associated object example",

            "ArtifactTypeID": 1000051,

            "ArtifactID": 1042586,

            "Guids": [],

            "ListType": "ChildObject"

        }

    },

    "AllowAdd": false,

    "AllowDelete": false,

    "AllowRename": false,

    "ShowDelete": false,

    "ShowAddLink": false,

    "AllowLayoutChange": false,

    "ShowNew": true,

    "ShowLink": false,

    "ShowUnlink": false,

    "ShowMassCopy": false,

    "ShowMassEdit": false,

    "ShowMassReplace": false,

    "ShowMassTally": false,

    "RelativityApplications": {

        "HasSecuredItems": false,

        "ViewableItems": []

    },

    "ObjectType": {

        "Name": "Custom Object Type",

        "ArtifactTypeID": 1000048,

        "ArtifactID": 1042378,

        "Guids": []

    },

    "Actions": [],

    "LastModifiedOn": "2019-02-22T19:22:49.927",

    "LastModifiedBy": {

        "Name": "Doe, Jane",

        "ArtifactID": 1023652,

        "Guids": []

    },

    "CreatedOn": "2019-02-22T17:40:24.7",

    "CreatedBy": {

        "Name": "Doe, Jane",

        "ArtifactID": 1023652,

        "Guids": []

    },

    "Name": "Updated object rule",

    "ArtifactID": 1042590,

    "Guids": []

}
```

View the JSON response for an extended metadata request Copy

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
{

    "Behavior": "SubListButtonVisibility",

    "Field": {

        "Secured": false,

        "Value": {

            "Name": "Custom Single Choice Field",

            "ArtifactID": 1042566,

            "Guids": []

        }

    },

    "Layout": {

        "Secured": false,

        "Value": {

            "Name": "Custom Layout",

            "ArtifactID": 1042594,

            "Guids": []

        }

    },

    "Choice": {

        "Secured": false,

        "Value": {

            "Name": "Custom Choice",

            "ArtifactID": 1042569,

            "Guids": []

        }

    },

    "SubListObject": {

        "Secured": false,

        "Value": {

            "Name": "Associated object example",

            "ArtifactTypeID": 1000051,

            "ArtifactID": 1042586,

            "Guids": [],

            "ListType": "ChildObject"

        }

    },

    "AllowAdd": false,

    "AllowDelete": false,

    "AllowRename": false,

    "ShowDelete": false,

    "ShowAddLink": false,

    "AllowLayoutChange": false,

    "ShowNew": false,

    "ShowLink": false,

    "ShowUnlink": false,

    "ShowMassCopy": false,

    "ShowMassEdit": false,

    "ShowMassReplace": false,

    "ShowMassTally": false,

    "RelativityApplications": {

        "HasSecuredItems": false,

        "ViewableItems": []

    },

    "ObjectType": {

        "Name": "Custom Object Type",

        "ArtifactTypeID": 1000048,

        "ArtifactID": 1042378,

        "Guids": []

    },

    "Meta": {

        "Unsupported": [],

        "ReadOnly": [

            "RuleType"

        ]

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-data-visualization/{versionNumber}/workspaces/2342954/object-rules/1042595",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-data-visualization/{versionNumber}/workspaces/2342954/object-rules/Default-Layoutobjectrules/1042595",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ],

    "LastModifiedOn": "2019-02-22T17:55:04.253",

    "LastModifiedBy": {

        "Name": "Doe, Jane",

        "ArtifactID": 1023652,

        "Guids": []

    },

    "CreatedOn": "2019-02-22T17:55:04.253",

    "CreatedBy": {

        "Name": "Doe, Jane",

        "ArtifactID": 1023652,

        "Guids": []

    },

    "Name": "Sample rule for layout",

    "ArtifactID": 1042595,

    "Guids": []

}
```

## Update an object rule

You can update object rules by sending a PUT request to the appropriate URL for the rule type. For general information about object rules, see Adding an object rule .

Click the following drop-down links to view URLs and sample requests for sub-list visibility, choices, and layouts rules. You can find the URLs and JSON request formats for other object type rules in the Postman file provided for this service. For more information, see Postman sample files .

For the URLs in these examples, set the {WorkspaceID} variable to the Artifact ID of the workspace containing the object type, or use -1 to indicate the admin-level context. Set the {ObjectRuleId} variable to the Artifact ID of the object type.

View a list of URLs for all update endpoints

- Choice behavior Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/choice-behavior/{ObjectRuleId}
```

- Custom Single Object Add Link Visibility Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/custom-single-object-add-link-visibility/{ObjectRuleId}
```

- Default Layout Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/default-Layout/{ObjectRuleId}
```

- Default Layout on New Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/default-layout-on-new/{ObjectRuleId}
```

- Global Button Visibility Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/global-button-visibility
```

- Mass Action Visibility Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/mass-action-visibility/{ObjectRuleId}
```

- New Button Override Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/new-button-override/{ObjectRuleId}
```

- Sub-List Button Visibility Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/sub-list-button-visibility/{ObjectRuleId}
```

- Override edit link URL Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/override-edit-link/{ObjectRuleId}
```

- Override view link URL Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/override-view-link/{ObjectRuleId}
```

View the JSON request for updating a sub-list visibility rule

To update a sub-list visibility rule, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/sub-list-button-visibilityobjectrules/{ObjectRuleId}
```

The body of the request must contain the following fields unless specifically identified as optional:

- objectRuleRequest - request to create or update a rule. It contains the following fields:

- Name - the user-friendly name of the rule.

- ObjectType - contains the Artifact ID of the object type.

- Field - contains a Value specifying the Artifact ID of the field, which affects the button visibility.

- Choice - contains a Value specifying the Artifact ID of the choice, which affects the button visibility.

- SubListObject - contains a Value specifying the Artifact ID of the associative object list controlled by the rule.

- ShowNew - a Boolean value indicating whether to display the New button on the associative object list. The default value is true.

- ShowLink - a Boolean value indicating whether to display the Link button on the associative object list. The default value is true.

- ShowUnlink - a Boolean value indicating whether to display the Unlink button on the associative object list. The default value is true.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The object rule is linked to the applications in this array. If the array is empty, then the object rule isn't linked to any application.

- LastModifiedOn - the date and time when the object rule was most recently modified. This field is only required if you want to restrict the update of an object rule to the date that it was last modified. The value must match the LastModifiedOn date for the object rule stored in Relativity. Otherwise, you receive a 409 error, indicating that the object has been modified.

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
{

    "objectRuleRequest":{

         "Name": "Updated object rule",

         "ObjectType": {

            "ArtifactID": 1042378

        },

        "Field": {

            "Value": {

                "ArtifactID": 1042566

            }

        },

        "Choice": {

            "Value": {

                "ArtifactID": 1042568

            }

        },

        "SubListObject": {

            "Value": {

                "ArtifactID": 1042586

            }

        },

        "ShowNew": true,

        "ShowLink": false,

        "ShowUnlink": false,

        "RelativityApplications": []

    },

        "LastModifiedOn": "2019-02-22T19:33:57.89"

}
```

View the JSON request for updating a choice rule

To update a choice rule, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/choice-behaviorobjectrules/{ObjectRuleId}
```

The body of the request must contain the following fields unless specifically identified as optional:

- objectRuleRequest - request to create or update a rule. It contains the following fields:

- Name - the user-friendly name of the rule.

- ObjectType - contains the Artifact ID of the object type.

- AllowAdd - a Boolean value indicating whether the user can mass copy choices.

- AllowDelete - a Boolean value indicating whether the user can mass delete choices.

- AllowRename - a Boolean value indicating whether the user can rename a choice.

- Field - contains a Value specifying the Artifact ID of the field, which affects the choice behavior.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The object rule is linked to the applications in this array. If the array is empty, then the object rule isn't linked to any application.

- LastModifiedOn - the date and time when the object rule was most recently modified. This field is only required if you want to restrict the update of an object rule to the date that it was last modified. The value must match the LastModifiedOn date for the object rule stored in Relativity. Otherwise, you receive a 409 error, indicating that the object has been modified.

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
{

    "objectRuleRequest":{

        "Name": "Update choice behavior",

        "ObjectType": {

            "ArtifactID": 1042378

        },

        "AllowAdd": true,

        "AllowDelete": false,

        "AllowRename": true,

        "Field": {

            "Value": {

                "ArtifactID": 1042565

            }

        },

        "RelativityApplications": []

      },

        "LastModifiedOn": "2019-02-22T19:33:57.89"

}
```

View the JSON request for updating a layout rule

To update a layout rule, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/default-Layoutobjectrules/{ObjectRuleId}
```

The body of the request must contain the following fields unless specifically identified as optional:

- objectRuleRequest - request to create or update a rule. It contains the following fields:

- Name - the user-friendly name of the rule.

- ObjectType - contains the Artifact ID of the object type.

- Field - contains a Value specifying the Artifact ID of the field, which controls the layout behavior.

- Layout - contains a Value specifying the Artifact ID of the layout.

- Choice - contains a Value specifying the Artifact ID of the choice, which controls the layout behavior.

- AllowLayoutChange - a Boolean value indicating whether the user can select another layout. The default value is false.

- RelativityApplications - an array of Relativity applications represented by ObjectIdentifier objects, which contain the Artifact ID and GUIDs for an application. The object rule is linked to the applications in this array. If the array is empty, then the object rule isn't linked to any application.

- LastModifiedOn - the date and time when the object rule was most recently modified. This field is only required if you want to restrict the update of an object rule to the date that it was last modified. The value must match the LastModifiedOn date for the object rule stored in Relativity. Otherwise, you receive a 409 error, indicating that the object has been modified.

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
{

    "objectRuleRequest":{

        "Name": "Updated rule for default layout",

        "ObjectType": {

            "ArtifactID":1042378

        },

        "Field": {

            "Value": {

                "ArtifactID": 1042566

            }

        },

        "Layout": {

            "Value": {

                "ArtifactID": 1042594

            }

        },

        "Choice": {

            "Value": {

                "ArtifactID": 1042569

            }

        },

        "AllowLayoutChange": false,

        "RelativityApplications": []

    },

        "LastModifiedOn": "2019-02-22T19:33:57.89"

}
```

When an update request is successful, the response returns the status code of 200.

## Delete an object rule

To remove an object rule, send a DELETE request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/objectrules/{ObjectRuleId}
```

The body of the request is empty. When the object rule is successfully deleted, the response returns the status code of 200.

## Delete multiple object rules

You can remove multiple object rules on the same object type and across different object types by making a single call to the mass-delete endpoint. Send a POST request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/mass-delete
```

The body of the request must contains an array of object rules with the following fields:

- ArtifactID - the Artifact ID of the object rule.

- GUID - an array of GUIDs used to identify the object rule. This array can be empty.

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
{

   "ObjectRules":[

      {

         "ArtifactID":1039509,

         "GUID":[

         ]

      },

      {

         "ArtifactID":1039525,

         "GUID":[

         ]

      },

      {

         "ArtifactID":1039630,

         "GUID":[

         ]

      }

   ]

}
```

When the object rules are successfully deleted, the response returns the status code of 200.

## Retrieve choices, choice fields, layouts, or associated objects

When you create or update an object rule, you must provide the Artifact ID of any associative objects, layouts, choices and choice fields that it references. The Object Rule Manager service provides several helper endpoints that you can use to retrieve the Artifact ID, name, and other information about these objects. For most objects, it includes endpoints for the following types of requests:

- GET request - use the endpoint for this request if you have the Artifact ID for an object type.

- POST request - use the endpoint for this request if you have the user-friendly name of the object type, but not its Artifact ID.

For more information, see Guidelines for the Object Rule Manager service .

Associated object endpoints

Use the following endpoints to retrieve associated objects for a specific object type:

- Retrieve with Artifact ID - send a GET request with a URL in the following general format: Copy

```text
1
<host>/Relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/available-associated-objects/{ObjectTypeArtifactId}
```

- Retrieve with Artifact ID or name - send a POST request with a URL in the following general format: Copy

```text
1
<host>/Relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/available-associated-objects
```

The body of the request contains the following fields:

- ObjectTypeID - represents identification information for an object. It contains the following fields:

- ArtifactID - the Artifact ID of the object type. If you specify a name, this field is optional.

- Name - the user-friendly name of the associated object. If you specify an Artifact ID, this field is optional.

Copy

```text
1
2
3
4
5
6
{

    "ObjectTypeID" : {

       "ArtifactID": 1036417,

       "Name": "Analytics Example"

    }

}
```

The response for both the GET and POST request contains the following fields:

- Name - the user-friendly name of the associated object.

- ArtifactTypeID - an identifier used to specify an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs used to identify the object type.

- ListType - the type of associative objects that the list contains. This field contains one of the following values:

- ChildObject - indicates that the list contains associated child objects.

- MultipleObjectField - indicates that the list contains associated multiple object field types.

- SingleObjectField - indicates that the list contains associated single object field types.

If no associated objects are available for the object type, this endpoint returns an empty array.

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
[

    {

        "Name": "Category Example",

        "ArtifactTypeID": 1000017,

        "ArtifactID": 1036424,

        "Guids": [

            "f611b0e4-6d92-4ff6-a247-46e87685bfc9"

        ],

        ListType: "ChildObject"

    }

]
```

Single choice field endpoints

Use the following endpoints to retrieve single choice fields for a specific object type:

- Retrieve with Artifact ID - send a GET request with a URL in the following general format: Copy

```text
1
<host>/Relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/available-single-choice-fields/{ObjectTypeArtifactId}
```

-

Retrieve with Artifact ID or name - send a POST request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/available-single-choice-fields
```

The body of the request contains the following fields:

- ObjectTypeID - represents identification information for an object. It contains the following fields:

- ArtifactID - the Artifact ID of the object type. If you specify a name, this field is optional.

- Name - the user-friendly name of the associated object. If you specify an Artifact ID, this field is optional.

Copy

```text
1
2
3
4
5
6
{

    "ObjectTypeID" : {

       "ArtifactID": 1042378,

       "Name": "Custom Object Type"

    }

}
```

The response for both the GET and POST request contains the following fields:

- Name - the user-friendly name of the associated object.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs used to identify the object type.

If no associated single choice fields are available for the object type, this endpoint returns an empty array.

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
[

    {

        "Name": "Custom Single Choice Field",

        "ArtifactID": 1042566,

        "Guids": []

    },

    {

        "Name": "Single Choice Field",

        "ArtifactID": 1042564,

        "Guids": []

    }

]
```

Choice field endpoints

Use the following endpoints to retrieve single and multiple choice fields for a specific object type:

- Retrieve with Artifact ID - send a GET request with a URL in the following general format: Copy

```text
1
<host>/Relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/available-choice-fields/{ObjectTypeArtifactId}
```

-

Retrieve with Artifact ID or name - send a POST request with a URL in the following general format:

Copy

```text
1
<hostRelativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/available-choice-fields/
```

The body of the request contains the following fields:

- ObjectTypeID - represents identification information for an object. It contains the following fields:

- ArtifactID - the Artifact ID of the object type. If you specify a name, this field is optional.

- Name - the user-friendly name of the associated object. If you specify an Artifact ID, this field is optional.

Copy

```text
1
2
3
4
5
6
{

    "ObjectTypeID" : {

       "ArtifactID": 1042378,

       "Name": "Custom Object Type"

    }

}
```

The response for both the GET and POST request contains the following fields:

- Name - the user-friendly name of the associated object.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs used to identify the object type.

If no choice fields are available for the object type, this endpoint returns an empty array.

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

        "Name": "Custom Single Choice Field",

        "ArtifactID": 1042566,

        "Guids": []

    },

    {

        "Name": "Multiple Choice Field",

        "ArtifactID": 1042565,

        "Guids": []

    },

    {

        "Name": "Single Choice Field",

        "ArtifactID": 1042564,

        "Guids": []

    }

]
```

Choice endpoint

To retrieve a list of choices for an object type, send a GET request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/available-choices/{{FieldId}}
```

The response contains the following fields:

- Name - the user-friendly name of the associated object.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs used to identify the object type.

If no choice are available for the object type, this endpoint returns an empty array.

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

        "Name": "Blue",

        "ArtifactID": 1042569,

        "Guids": []

    },

    {

        "Name": "Green",

        "ArtifactID": 1042568,

        "Guids": []

    },

    {

        "Name": "Orange",

        "ArtifactID": 1042570,

        "Guids": []

    }

]
```

Layout endpoints

Use the following endpoints to retrieve layouts for a specific object type:

- Retrieve with Artifact ID - send a GET request with a URL in the following general format: Copy

```text
1
<host>/Relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/available-layouts/{ObjectTypeArtifactId}
```

-

Retrieve with Artifact ID or name - send a POST request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.rest/api/relativity-data-visualization/{versionNumber}/workspaces/{WorkspaceID}/object-rules/available-layouts
```

The body of the request contains the following fields:

- ObjectTypeID - represents identification information for an object. It contains the following fields:

- ArtifactID - the Artifact ID of the object type. If you specify a name, this field is optional.

- Name - the user-friendly name of the associated object. If you specify an Artifact ID, this field is optional.

Copy

```text
1
2
3
4
5
6
{

    "ObjectTypeID" : {

        "ArtifactID": 1042378,

        "Name" : "Custom Object Type"

    }

}
```

The response for both the GET and POST request contains the following fields:

- Name - the user-friendly name of the associated object.

- ArtifactID - the Artifact ID of the object type.

- Guids - an array of GUIDs used to identify the object type.

If no layouts are available for the object type, this endpoint returns an empty array.

Copy

```text
1
2
3
4
5
6
7
[

    {

        "Name": "Custom Object Type Layout",

        "ArtifactID": 1042377,

        "Guids": []

    }

]
```

---
title: "Field Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Model/Field_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:24:10+00:00
sha256: 9e8e322f42b031dd73c769b6c9b4e6936a9cf73635ef862fc8bef445254a4951
---

Field Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Field Manager (REST)

The Field Manager service provides multiple endpoints for programmatically working with field types supported by Relativity, including multiple choice, fixed-length text, date, and others. This service supports create, read, update, and delete operations on fields. Additionally, it includes helper endpoints for retrieving the following information:

- Object types available to create fields on.

- Associative object types for creating single object fields.

- Associative object types for creating multiple object fields.

- Views available for a specific object type.

- Keyboard shortcuts that are currently defined in a workspace.

- Keys that are valid for use in a keyboard shortcut.

- Fields available for use with propagation.

- Order of relational field icons in the Related Items pane of the core reviewer interface.

Sample use cases for the Field Manager service include programmatically adding new fields to a custom application as data requirements change, or creating new keyboard shortcuts for fields to support modified workflows for users.

You can also use the Field Manager service through .NET. For more information, see Field Manager (.NET) .

## Guidelines for the Field Manager service

Review the following guidelines for the Field Manager service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to delete a field:

Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/{fieldArtifactID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the service, such as v1.

- {WorkspaceID} variable to the Artifact ID of a workspace, or use -1 to indicate the admin-level context.

- {fieldArtifactID} variable to the Artifact ID of the field that you want to delete.

### Supported field types

Use the Field Manager service to work with the same field types available through the Relativity UI. For general information about fields, see Fields on the Relativity Documentation site.

View a list of available field types

- Currency

- Date

- Decimal

- File

- Fixed-length text

- Long text

- Multiple choice

- Multiple object

- Single choice

- Single object

- User

- Whole number

- Yes/No

### Helper endpoints

Use the helper endpoints to facilitate creating fields.

View a table with examples of helper endpoints used when creating fields

Field type Links to helper endpoint information

Date

- Retrieve available object types

Fixed-length text field

- Retrieve available object types

- Retrieve available views for an object type

- Retrieve keyboard shortcuts

- Retrieve valid keys

Multiple choice

- Retrieve available object types

Single object

- Retrieve available object types

- Retrieve object types for a single object field

- Retrieve available views for an object type

- Retrieve available fields for propagation

### Relational fields

To edit properties for relational fields, the IsRelational field must be set to true. You can then edit the FriendlyName, ImportBehavior, PaneIcon, Order, and RelationalView properties. Set these fields as follows:

- Set the ImportBehavior property to one of the following values:

- None - indicates that no import behavior is specified.

- LeaveBlankValuesUnchanged - indicates that the values for the fields are imported as blank.

- ReplaceBlankValuesWithIdentifier - indicates that blank relational fields are updated with an identifier.

- Set the properties on a PaneIcon object as follows:

- Optionally, set the value for the FileName field for the pane icon.

- Set the ImageBase64 property to the base64 format.

### Overlay behavior

Set the value for the OverlayBehavior property to one of the following values. For more information, see the OverlayBehavior enumeration in the Relativity.ObjectModel.{versionNumber}.Field.Models namespace.

- ReplaceValues - replaces existing field values with the new ones from the load file.

- MergeValues - merges existing values with the new ones from the load file.

### Filter types

Set the FilterType property to one of the following values. For more information, see the FilterType enumeration in the Relativity.ObjectModel.{versionNumber}.Field.Models namespace.

- None - used for all field types.

- List - used for currency, decimal, fixed-length text, multiple choice, single choice, user, and whole number field types.

- MultiList - used for single choice, multiple choice, and multi-object field types.

- Popup - used for single choice, multiple choice, single object, and multiple object field types. Only usable when the FilterType property is set to Popup.

- Boolean - used for Yes/No field types.

- TextBox - used for currency, date, decimal, fixed-length text, long text, single object, multiple object, and whole number field types.

- Custom - used for currency, date, decimal, fixed-length text and whole number field types.

- DatePicker - used for date field types.

#### Filter types for date and user fields

The Field Manager API currently sets the filter type for the date and user fields as follows. See the following descriptions:

- Date field - You can now set the FilterType for this field to DatePicker through the API. However, the field type displays a TextBox filter when you access it.

- User field - You can now set the FilterType for this field to MultiList through the API. However, the field type displays a List filter when you access it.

### Source property

Only use the Source property for mapping processing fields on the Document object.

### Formatting fields

Set the Formatting property to one of the following values. For more information, see the Formatting enumeration in the Relativity.ObjectModel.{versionNumber}.Field.Models namespace.

- None - used for all field types except currency or date.

- Formatted - used for decimal and whole number field types.

- Date - used for the date field type.

- DateTime - used for the date field type.

- Currency - used for the currency field type.

## Client code sample

To use the Field Manager service, send requests by making calls with the required HTTP methods. See the following base URL for this service:

Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/
```

You can use the following .NET code as a sample client for creating a fixed-length text field. This code illustrates how to perform the following tasks:

- Instantiate an HttpClient object for sending requests to the Field Manager service.

- Set the required headers for the request. For information on setting headers, see HTTP headers .

- Initialize variables with the values for the field to create.

- Set the url variable to the URL for the workspace where the field is to be added. For more information, see Create a field .

- Set the JSON input required for the operation.

- Use the PostAsync() method to send a POST request.

- Return the results of the request and deserialize it.

View sample client code Copy

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
//Create a fixed-length field.

public async Task<int?> CreateFixedLengthField(")"{

   "int? result = null;

    using (HttpClient client = new HttpClient())"{

      "client.DefaultRequestHeaders.Add(""X-CSRF-Header",

      "-"");

        client.DefaultRequestHeaders.Add(""Authorization",

      "Basic "+ Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1"").GetBytes(""test@test.com:SomePassword"")));

        client.DefaultRequestHeaders.Add(""X-Kepler-Version",

      "2.0"");

        client.BaseAddress = new Uri(""https://localhost/");



        int workspaceId = 1018486;

        string fieldName ="Field Name"int objectTypeArtifactId= 1035231;

        int objectTypeArtifactTypeId = 34;

        string objectTypeName ="Object Type Name"int length = 255;

        int fieldArtifactId = 1927383;

        int choiceArtifactId = 1274939;

        int associatedObjectTypeArtifactId = 1293759;

        int objectViewArtifactID = 1023847;

        string friendlyName ="Friendly Name""string imageFilename =""Image File Name"string imageBase64 ="iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAIpSURBVDjLddM9aFRBFIbh98zM3WyybnYVf4KSQjBJJVZBixhRixSaShtBMKUoWomgnaCxsJdgIQSstE4nEhNREgyoZYhpkogkuMa4/3fuHIu7gpLd00wz52POMzMydu/Dy958dMwYioomIIgqDa+VnWrzebNUejY/NV6nQ8nlR4ufXt0fzm2WgxUgqBInAWdhemGbpcWNN9/XN27PPb1QbRdgjEhPqap2ZUv5+iOwvJnweT1mT5djZKjI6Ej/udz+wt1OJzAKYgWyDjJWyFghmzFsbtcY2gsTJwv09/Vc7RTgAEQgsqAKaoWsM8wu/z7a8B7vA8cHD3Fr+ktFgspO3a+vrdVfNEulJ/NT4zWngCBYY1oqSghKI465fvYwW+VAatPX07IZmF7YfrC0uDE8emPmilOFkHYiBKxAxhmSRPlZVVa2FGOU2Ad2ap4zg92MDBXJZczFmdflx05VEcAZMGIIClZASdesS2cU/dcm4sTBArNzXTcNakiCb3/HLRsn4Fo2qyXh3WqDXzUlcgYnam3Dl4Hif82dbOiyiBGstSjg4majEpl8rpCNUQUjgkia0M5GVAlBEBFUwflE{versionNumber}2b/Hig6SmA1iDtzhcsE6eP7LIxAchAtwNVxc1MnhprN/+lh0txErxrPZVdFdRDEEzHT6LWpTbtq+HLSDDiOm2o1uqlyOT37bIhHdKaXoL6pqhq24Dzd96/tUYGwPSBVv7atFglaFIu5KLuPxeX/xsp7aR6AAAAAElFTkSuQmCC";

        int order = 150;

        string shortcutKey ="PageDown"";



        string inputJSON = $""{\n\t\"fieldRequest\":{\n\t    \"Name\": {{fieldName}},\n\t\t\"ObjectType\": {\n\t            \"ArtifactID\": {{objectTypeArtifactId}},\n\t            \"ArtifactTypeID\": {{objectTypeArtifactTypeId}},\n\t            \"Name\": {{objectTypeName}}\n\t    },\n\t    \"Length\": {{length}},\n\t    \"Source\": \"\",\n\t    \"IsRequired\": false,\n\t    \"IncludeInTextIndex\": false,\n\t    \"HasUnicode\": false,\n\t    \"AllowHtml\": false,\n\t    \"OpenToAssociations\": false,\n\t    \"PropagateTo\": [],\n\t    \"IsLinked\": false,\n\t    \"FilterType\": \"None\",\n\t    \"AllowSortTally\": false,\n\t    \"Width\": null, \n\t    \"AllowGroupBy\": false,\n\t    \"AllowPivot\": false,\n\t    \"Wrapping\": false,\n\t    \"IsRelational\": true,\n\t\t\"FriendlyName\": {{friendlyName}},\n\t\t\"ImportBehavior\": \"None\",\n\t\t\"PaneIcon\": {\n\t\t\t\"FileName\": {{imageFilename}},\n\t\t\t\"ImageBase64\": {{imageBase64}}\n\t\t},\n\t\t\"Order\": {{order}},\n\t\t\"RelationalView\":{\n\t    \t\"Value\":{\n\t    \t\t\"ArtifactID\": {{objectViewArtifactID}},\n\t    \t\t\"Guids\": {{guids}}\n\t    \t}\n\t    },\n\t    \"Shortcut\":{\n\t       \"ModifierKeys\": [],\n\t       \"MainKey\": \"\",\n\t},\n\t     \"RelativityApplications\": [],\n\t    \"Keywords\": \"\",\n        \"Notes\": \"\"\n\t}\n}"";

        var url = $@""/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{{workspaceID}}/fields/fixed-length"";

        var response = await client.PostAsync(url",

      "new StringContent(inputJSON",

      Encoding.UTF8,

      "application/json""));

        response.EnsureSuccessStatusCode();

        var content = await response.Content.ReadAsStringAsync();

        result = JsonConvert.DeserializeObject<int>(content);"

   }"return result;"

}
```

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on Field Manager service. To download the sample file, click FieldAPIPostmanFile.zip .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Create a field

You can create a field by sending a POST request to the appropriate URL for the field type. For general information about fields, see Fields on the Relativity Documentation site.

Click the following drop-down links to view URLs and sample requests for fixed-length text, multiple choice, single object, and date fields. You can find the URLs and JSON request formats for other field types in the Postman file provided for this service. For more information, see Postman sample file .

View a list of URLs for all create endpoints

- Currency Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/currency
```

- Date Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/date
```

- Decimal Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/decimal
```

- File Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/file
```

- Fixed-length text Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/fixed-length
```

- Long text Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/long-text
```

- Multiple choice Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/multiple-choice
```

- Multiple object Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/multiple-object
```

- Single choice Copy

```text
1
<host>Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/single-choice
```

- Single object Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/single-object
```

- User Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/user
```

- Whole number Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/whole-number
```

- Yes/No Copy

```text
1
<host>/Relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/yes-no
```

View a list of all field descriptions

Depending on the field type, a request used for creating or updating a field may contain a combination of the following fields:

- AllowGroupBy - a Boolean value indicating whether the field is available for grouping in Pivot.

- AllowHtml - a Boolean value indicating whether HTML formatted text can be displayed in the field.

- AllowPivot - a Boolean value indicating whether a pivot can be performed on this field.

- AllowSortTally - a Boolean value indicating whether the document list is sorted on the field.

- AssociateObjectType - the object type associated with the field. A single object field defines a one-to-many relationship between the object type that the field is added to, and the object type specified here. A multiple object field defines many-to-many relationship between the object types. The AssociateObjectType field contains the following information:

- Name - the user-friendly name of the object type.

- ArtifactTypeID - the integer value for the Artifact Type ID of an ObjectType. For example, the Artifact Type ID for a Document object is 10. See the ArtifactType enumeration in the Class library reference .

- ArtifactID - the Artifact ID of an object type.

- Guids - an array of GUIDs used to identify the object type.

- AvailableInFieldTree - a Boolean value indicating that the field appears in Field Tree browser in the workspace.

- AvailableInViewer - a Boolean value indicating that the field appears in the viewer.

- AutoAddChoices - a Boolean value indicating whether all the choices associated with a single or multiple choice field should be added to an application.

The requests for multiple and single choice fields have an AutoAddChoices property. If you change this property from No to Yes on a specific field, and applications in your workspace use this field, you must re-add the field to each application to include the choices. The RelativityApplications property on these requests lists the applications containing the field. See RelativityApplications in this list.

- DisplayValueFalse - the text displayed for the false value of a Yes/No field.

- DisplayValueTrue - the text displayed for the true value of a Yes/No field.

- EnableDataGrid - a Boolean value indicating whether data in long text fields can be imported to Data Grid.

- FieldTreeView - a view used to display items available in a field tree. It contains the following fields:

- Secured - indicates whether the current user has permission to view the settings in the Value field.

- Value - contains the name, Artifact ID, and GUIDs used to identify the view.

- FieldType - the type of the field, such as date, fixed-length text, long text, or others.

- FilterType - indicates the type of filter used for the field, such as list, text box, multi-list, and others.

- Formatting - indicates the format used to display date and whole number fields only.

- FriendlyName - the user-friendly name for the field displayed in the Relativity UI.

- HasUnicode - a Boolean value indicating that Unicode characters can be used in this field.

- ImportBehavior - indicates how blank values are handled when running an import job through the Relativity Desktop Client. This field must be set to LeaveBlankValuesUnchanged or ReplaceBlankValuesWithIdentifier when the IsRelational field is set to true.

- IncludeInTextIndex - a Boolean value indicating that the field values are added to the SQL text index for the workspace, making the field searchable via keyword search.

- IsIdentifier - a Boolean value indicating whether the field is a unique identifier for a workspace. Relativity doesn't enforce this setting.

- IsLinked - a Boolean value indicating whether a hyperlink for the field is available.

- IsRelational - a Boolean value indicating whether the field is relational, which means that it is used to identify a group of related documents, such as families, duplicates, or near duplicates. You can only set this field to true on Document objects. When the field is true, you must also set the FriendlyName, ImportBehavior, PaneIcon, and Order fields.

- IsRequired - a Boolean value indicating the user must set a value on this field.

- Key - indicates the alphanumeric or other key used in combination with a CTRL, ALT, or SHIFT key to act as a keyboard shortcut. You can only set this field when the parent object is a document.

- Keywords - optional words or phrases used to describe the field.

- Length - an integer value indicating the number of characters in a fixed-length text field. The default value is 255 characters.

- Name - the name of the field.

- Notes - an optional description or other information about the field.

- ObjectType - contains the following fields:

- ArtifactID - the Artifact ID of an object type.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- Name - the user-friendly name of the object type that you are adding the field to.

- Guids - an array of GUIDs used to identify the object type.

- OpenToAssociations - a Boolean value indicating whether the field information can be displayed on an associated object field.

- Order - an integer value used to indicate the order for the pane icons at the bottom of the Related Items pane.

- OverlayBehavior - indicates whether the values in multiple object or multiple choice fields are replaces or merge when imported from a load file.

- PaneIcon - an icon displayed in the Related Items pane of the core reviewer interface. It contains the following fields:

- FileName - the name of the icon file. It must be in one of the following formats: gif, jpg, jpeg, png, bmp, or tiff. This field is optional.

- ImageBase64 - the string representing the Base64 encoding of the image. The length of the string must be a multiple of 4.

- PopupPickerView - a view used to display items available in a pop-up picker. It contains the following fields:

- Secured - indicates whether the current user has permission to view the settings in the Value field.

- Value - contains the name, Artifact ID, and GUIDs used to identify the view.

- PropagateTo - contains the following fields:

- HasSecuredItems - a Boolean value indicating whether the application contains items that the current user doesn't have permission to access.

- ViewableItems - an array of identifier objects for items that are accessible to the current user. For example, an object in this array would contain the name, Artifact IDs, and GUIDs on fields available for propagation.

On the response object, the PropagateTo field contains the HasSecuredItems and ViewableItems fields. The ViewableItems field contains identifiers for a list of fields, which only includes unsecured items. On the request object, the PropagateTo field populates with an array of fields that the user can access. After making an update request, this array is merged with the list of fields that are secured. The secured fields aren't accessible to the user.

- RelationalView - indicates the view used in the Related Items pane. It contains the following field:

- Value - contains the Artifact ID and GUIDs used to identify the view. These values can be null.

- RelativityApplications - contains the following fields:

- HasSecuredItems - a Boolean value indicating whether the application contains items that the current user doesn't have permission to access.

- ViewableItems - an array of identifier objects for items that are accessible to the current user. For example, an object in this array would contain the name, Artifact IDs, and GUIDs for an application.

On the response object, the RelativityApplications field contains the HasSecuredItems and ViewableItems fields. The ViewableItems field contains identifiers for a list of applications, which only includes unsecured items. On the request object, the PropagateTo field populates with an array of applications that the user can access. After making an update request, this array is merged with the list of applications that are secured. The secured applications aren't accessible to the user.

- Shortcut - contains the following fields:

- MainKey - indicates the alphanumeric or other key used in combination with a CTRL, ALT, or SHIFT key to act as a keyboard shortcut. You can only set this field when the parent object is a document.

- ModifierKeys - A list of the enum ObjectModel.V1.Shared.Models.ModifierKey that represents CTRL, ALT, or SHIFT to act as part of the keyboard shortcut. You can only set this field when the parent object is a document.

- Source - the name of a field in the Field Catalog, which you want to map your field to. This field is used when you want to map processing fields on the Document object.

- Width - the number of pixels used for the column width of a field when it is displayed in the view.

- Wrapping - a Boolean value indicating whether text wraps in this field.

View the JSON request for creating a fixed-length text field

To create a fixed-length text field, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/fixed-length
```

The following JSON sample illustrates how to create a fixed-length text field, and set values for a relational field and keyboard shortcuts.

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
{{

   "fieldRequest":{

      "Name":"My Custom Fixed-length Field",

      "ObjectType":{

         "ArtifactID":1035231,

         "ArtifactTypeID":10,

         "Name":"Document"

      },

      "Length":100,

      "Source":"",

      "IsRequired":false,

      "IncludeInTextIndex":false,

      "HasUnicode":false,

      "AllowHtml":false,

      "OpenToAssociations":false,

      "PropagateTo":[



      ],

      "IsLinked":false,

      "FilterType":"None",

      "AllowSortTally":false,

      "Width":null,

      "AllowGroupBy":false,

      "AllowPivot":false,

      "Wrapping":false,

      "IsRelational":true,

      "FriendlyName":"My Custom Fixed-length Field",

      "ImportBehavior":"LeaveBlankValuesUnchanged",

      "PaneIcon":{

         "FileName":"DuplicateIcon.png",

         "ImageBase64":"iVBORw0KGgoAAAANSUhEUgAAABcAAAAdCAYAAABBsffGAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAB3RJTUUH4wUHEggE2SVNSgAAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbiB0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERpc2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWHRTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRUaXRsZQCo7tInAAAAKElEQVRIie3MQQ0AAAgEILV/5zOFDzcIQCdJHZmrWC6Xy+VyuVz+Pl8ueQQ2b6MCqAAAAABJRU5ErkJggg=="

      },

      "Order":150,

      "RelationalView":{

         "Value":{

            "ArtifactID":null,

            "Guids":null

         }

      },

      "Shortcut":{

         "ModifierKeys":[

            "Alt",

            "Ctrl",

            "Shift"

         ],

         "MainKey":"Home"

      },

      "RelativityApplications":[



      ],

      "Keywords":"",

      "Notes":""

   }

}
```

View the JSON request for creating a multiple choice field

To create a multiple choice field, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/multiple-choice
```

The following JSON sample illustrates how to create a multiple choice field, and set values for applications.

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
{

    "fieldRequest":{

        "Name": "My Multiple Choice Field",

        "ObjectType": {

                "ArtifactID": 1042378,

                "ArtifactTypeID": 1000048,

                "Name": "Custom Object Type"

        },

        "Source": "",

        "IsRequired": true,

        "HasUnicode": true,

        "AvailableInFieldTree": false,

        "OpenToAssociations": false,

        "OverlayBehavior": "ReplaceValues",

        "PropagateTo": [],

        "IsLinked": false,

        "FilterType": "None",

        "AllowSortTally": false,

        "Width": null,

        "AllowGroupBy": false,

        "AllowPivot": false,

        "Wrapping": false,

        "RelativityApplications": [

           {

            "ArtifactID": 1045231

           }

         ],

        "AutoAddChoices": false,

        "Keywords": "",

        "Notes": ""

    }

}
```

View the JSON request for creating single object field

To create a single object field, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/single-object
```

The following JSON sample illustrates how to create a single object field.

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
{

    "fieldRequest":{

        "Name": "My Single Object Field",

        "ObjectType": {

                "ArtifactID": 1042378,

                "ArtifactTypeID": 1000048,

                "Name": "Custom Object Type"

        },

        "AssociativeObjectType": {

                "ArtifactID": 1042580,

                "ArtifactTypeID": 1000051,

                "Name": "Custom Object Type Two"

        },

        "Source": "",

        "IsRequired": true,

        "AvailableInFieldTree": false,

        "FieldTreeView":{

            "Secured": false,

            "Value": {

                "ArtifactID": null

            }

        },

        "OpenToAssociations": false,

        "PropagateTo": [],

        "IsLinked": false,

        "FilterType": "Popup",

         "PopupPickerView":{

            "Secured": false,

            "Value": {

                "ArtifactID": null

            }

        },

        "AllowSortTally": false,

        "Width": null,

        "AllowGroupBy": false,

        "AllowPivot": false,

        "Wrapping": false,

        "RelativityApplications": [],

        "Keywords": "",

        "Notes": ""

    }

}
```

View the JSON request for creating a date field

To create a date field, send a POST request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/date
```

The following JSON sample illustrates how to create a date field, and set values for Source and Formatting fields.

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

    "fieldRequest":{

        "Name": "My Custom Date Field",

        "ObjectType": {

                "ArtifactID": 1042378,

                "ArtifactTypeID": 1000048,

                "Name": "Custom Object Type"

        },

        "Source": "Source Name",

        "IsRequired": false,

        "Formatting": "Date",

        "OpenToAssociations": false,

        "PropagateTo": [],

        "IsLinked": false,

        "FilterType": "None",

        "AllowSortTally": false,

        "Width": null,

        "AllowGroupBy": false,

        "AllowPivot": false,

        "Wrapping": false,

        "Shortcut": {

           "ModifierKeys": [],

           "MainKey": ""

        },

        "RelativityApplications": [],

        "Keywords": "",

        "Notes": ""

    }

}
```

When a request is successful, the response contains the Artifact ID of the new field. It also returns the status code of 200.

## Read a field

You can retrieve basic or extended metadata for a field. The extended metadata also includes operations that user has permissions to perform on the field.

- Retrieve basic metadata for a field - send a GET request with a URL in the following general format: Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/{fieldArtifactID}
```

- Retrieve extended metadata for a field - send a GET request with a URL in the following general format: Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/{fieldArtifactID}?includeMetadata=true&includeActions=true
```

The request body is empty.

View field descriptions for a response

Depending on the field type, a read operation returns a combination of the fields listed in Create a field . A read operation also returns the following fields:

- Actions - an array of Action objects indicating operations that you have permissions to perform on this field. For example, you may not have permissions to modify a field that is part of a locked application. Each Action object contains the following fields that are available as extended metadata:

- Name - name of an operation available through REST for the object type, such as delete, update, and so on.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this object type.

- Reason - provides an explanation for the unavailability of an action.

- ArtifactID - the Artifact ID for the field.

- CreatedBy - contains the Artifact ID and name of the user who created the field. It also contains an array of GUIDs used to identify the user.

- CreatedOn - the date and time when the field was added to Relativity.

- Guids - an array of GUIDs used to identify the field.

- LastModifiedOn - the date and time when the field was most recently modified.

- LastModifiedBy - contains the Artifact ID and name of the user who recently updated the field. It also contains an array of GUIDs used to identify the user.

- Meta - provides additional information available as extended metadata. It includes the following fields:

- Unsupported - an array of properties that indicate functionality not available on the current instance of this field. For example, if the field isn't displayed in the field tree, then the AvailableInFieldTree would be listed here.

- ReadOnly - an array of field properties that can't be modified, such its object or field type.

- Name - the user-friendly name of the field.

- Source - indicates the processing field that is mapped to the current field.

- SourceName - the name identifying the source field.

- FriendlyName - the user-friendly name of the source field.

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
{

   "ObjectType":{

      "Name":"Document",

      "ArtifactTypeID":10,

      "ArtifactID":1035231,

      "Guids":[

         "15c36703-74ea-4ff8-9dfb-ad30ece7530d"

      ]

   },

   "Source":{

      "SourceName":"LastSavedDateTime",

      "FriendlyName":"Last Saved Date/Time"

   },

   "FieldType":"Date",

   "Length":0,

   "IsRequired":false,

   "IncludeInTextIndex":false,

   "HasUnicode":false,

   "IsIdentifier":false,

   "AvailableInViewer":false,

   "AvailableInFieldTree":false,

   "AllowHtml":false,

   "Formatting":"DateTime",

   "OpenToAssociations":false,

   "OverlayBehavior":"ReplaceValues",

   "EnableDataGrid":false,

   "PropagateTo":{

      "HasSecuredItems":false,

      "ViewableItems":[

         {

            "Name":"Family",

            "ArtifactID":1003671,

            "Guids":[

               "1f036749-a691-4aa8-8cf7-5eeb80c36caf"

            ]

         }

      ]

   },

   "IsLinked":false,

   "FilterType":"None",

   "AllowSortTally":true,

   "Wrapping":true,

   "AllowGroupBy":false,

   "AllowPivot":false,

   "Shortcut": {

      "ModifierKeys": [



      ],

      "MainKey": ""

   },

   "RelativityApplications":{

      "HasSecuredItems":false,

      "ViewableItems":[



      ]

   },

   "AutoAddChoices":false,

   "CreatedOn":"2019-04-03T21:30:50.197",

   "CreatedBy":{

      "Name":"Doe, Jane",

      "ArtifactID":1023652,

      "Guids":[



      ]

   },

   "LastModifiedBy":{

      "Name":"Doe, Jane",

      "ArtifactID":1023652,

      "Guids":[



      ]

   },

   "LastModifiedOn":"2019-04-03T21:30:50.197",

   "Keywords":"",

   "Notes":"",

   "Name":"My New Field",

   "ArtifactID":1043204,

   "Guids":[



   ]

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
{

   "ObjectType":{

      "Name":"Document",

      "ArtifactTypeID":10,

      "ArtifactID":1035231,

      "Guids":[

         "15c36703-74ea-4ff8-9dfb-ad30ece7530d"

      ]

   },

   "Source":{

      "SourceName":"LastSavedDateTime",

      "FriendlyName":"Last Saved Date/Time"

   },

   "FieldType":"Date",

   "Length":0,

   "IsRequired":false,

   "IncludeInTextIndex":false,

   "HasUnicode":false,

   "IsIdentifier":false,

   "AvailableInViewer":false,

   "AvailableInFieldTree":false,

   "AllowHtml":false,

   "Formatting":"DateTime",

   "OpenToAssociations":false,

   "OverlayBehavior":"ReplaceValues",

   "EnableDataGrid":false,

   "PropagateTo":{

      "HasSecuredItems":false,

      "ViewableItems":[

         {

            "Name":"Family",

            "ArtifactID":1003671,

            "Guids":[

               "1f036749-a691-4aa8-8cf7-5eeb80c36caf"

            ]

         }

      ]

   },

   "IsLinked":false,

   "FilterType":"None",

   "AllowSortTally":true,

   "Wrapping":true,

   "AllowGroupBy":false,

   "AllowPivot":false,

   "Shortcut": {

      "ModifierKeys": [



      ],

      "MainKey": ""

   },

   "RelativityApplications":{

      "HasSecuredItems":false,

      "ViewableItems":[



      ]

   },

   "AutoAddChoices":false,

   "CreatedOn":"2019-04-03T21:30:50.197",

   "CreatedBy":{

      "Name":"Doe, Jane",

      "ArtifactID":1023652,

      "Guids":[



      ]

   },

   "LastModifiedBy":{

      "Name":"Doe, Jane",

      "ArtifactID":1023652,

      "Guids":[



      ]

   },

   "LastModifiedOn":"2019-04-03T21:30:50.197",

   "Keywords":"",

   "Notes":"",

   "Meta":{

      "Unsupported":[

         "Length",

         "IncludeInTextIndex",

         "AllowHtml",

         "AvailableInViewer",

         "EnableDataGrid",

         "DisplayValueTrue",

         "DisplayValueFalse",

         "AvailableInFieldTree",

         "HasUnicode",

         "AutoAddChoices",

         "OverlayBehavior",

         "AssociativeObjectType",

         "PopupPickerView",

         "FieldTreeView"

      ],

      "ReadOnly":[

         "ObjectType",

         "FieldType",

         "AssociativeObjectType",

         "IsIdentifier"

      ]

   },

   "Actions":[

      {

         "Name":"Delete",

         "Href":"Relativity-Object-Model/{versionNumber}/workspaces/2342954/fields/1043204",

         "Verb":"DELETE",

         "IsAvailable":true,

         "Reason":[



         ]

      },

      {

         "Name":"Update",

         "Href":"Relativity-Object-Model/{versionNumber}/workspaces/2342954/fields/1043204",

         "Verb":"PUT",

         "IsAvailable":true,

         "Reason":[



         ]

      }

   ],

   "Name":"My New Field",

   "ArtifactID":1043204,

   "Guids":[



   ]

}
```

## Update a field

You can update a field by sending a PUT request to the appropriate URL for the field type. For general information about fields, see on the Relativity Documentation site.

Click the following drop-down links to view URLs and sample requests for fixed-length text, multiple choice, single object, and date fields. You can find the URLs and JSON request formats for other field types in the Postman file provided for this service. For more information, see Postman sample file .

To view a list of field descriptions, see Create a field .

When you want to ensure you only update a field if it hasn't been modified since you read it, provide the LastModifiedOn field. The update will fail if the field has been changed in the meantime and return a 409 error. You can get the value of this property from an FieldResponse object, which is returned by the ReadAsync() method.

View a list of URLs for all update endpoints

- Currency Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/currency/{fieldArtifactID}
```

- Date Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/date/{fieldArtifactID}
```

- Decimal Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/decimal/{fieldArtifactID}
```

- File Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/file/{fieldArtifactID}
```

- Fixed-length Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/fixed-length/{fieldArtifactID}
```

- Long text Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/long-text/{fieldArtifactID}
```

- Multiple choice Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/multiple-choice/{fieldArtifactID}
```

- Multiple object Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/multiple-object/{fieldArtifactID}
```

- Single choice Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/single-choice/{fieldArtifactID}
```

- Single object Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/single-object/{fieldArtifactID}
```

- User Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/user/{fieldArtifactID}
```

- Whole number Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/whole-number/{fieldArtifactID}
```

- Yes/No Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/yes-no/{fieldArtifactID}
```

View the JSON request for updating a fixed-length field

To update a fixed-length text field, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/fixed-length/{fieldArtifactID}
```

The following JSON illustrates a sample request:

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
{

    "fieldRequest":{

        "Name":  "Updated Fixed-length Field",

       "ObjectType": {

"Value": {

"ArtifactID": 1035231,

"ArtifactTypeID": 10,

"Name": "Document"

}

},

        "Length": 100,

        "Source": "",

        "IsRequired": false,

        "IncludeInTextIndex": false,

        "HasUnicode": false,

        "AllowHtml": false,

        "OpenToAssociations": false,

        "PropagateTo": [],

        "IsLinked": false,

        "FilterType": "None",

        "AllowSortTally": false,

        "Width": null,

        "AllowGroupBy": false,

        "AllowPivot": false,

        "Wrapping": false,

        "IsRelational": true,

        "FriendlyName": "My Custom Fixed-length Field",

        "ImportBehavior": "LeaveBlankValuesUnchanged",

        "PaneIcon": {

            "FileName": "DuplicateIcon.png",

            "ImageBase64": "iVBORw0KGgoAAAANSUhEUgAAABcAAAAdCAYAAABBsffGAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAB3RJTUUH4wUHEggE2SVNSgAAAAd0RVh0QXV0aG9yAKmuzEgAAAAMdEVYdERlc2NyaXB0aW9uABMJISMAAAAKdEVYdENvcHlyaWdodACsD8w6AAAADnRFWHRDcmVhdGlvbiB0aW1lADX3DwkAAAAJdEVYdFNvZnR3YXJlAF1w/zoAAAALdEVYdERpc2NsYWltZXIAt8C0jwAAAAh0RVh0V2FybmluZwDAG+aHAAAAB3RFWHRTb3VyY2UA9f+D6wAAAAh0RVh0Q29tbWVudAD2zJa/AAAABnRFWHRUaXRsZQCo7tInAAAAKElEQVRIie3MQQ0AAAgEILV/5zOFDzcIQCdJHZmrWC6Xy+VyuVz+Pl8ueQQ2b6MCqAAAAABJRU5ErkJggg=="

        },

        "Order": 150,

        "RelationalView":{

            "Value":{

                "ArtifactID": null,

                "Guids": null

            }

        },

        "Shortcut": {

           "ModifierKeys": [



           ],

           "MainKey": ""

        },

        "RelativityApplications": [],

        "Keywords": "",

        "Notes": "Updated the field"

    }

}
```

View the JSON request for updating a multiple choice field

To update a multiple choice field, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/multiple-choice/{fieldArtifactID}
```

The following JSON illustrates a sample request:

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

    "fieldRequest":{

        "Name": "My Updated Choice Field",

        "ObjectType": {

                "ArtifactID": 1042378,

                "ArtifactTypeID": 1000048,

                "Name": "Custom Object Type"

        },

        "Source": "",

        "IsRequired": true,

        "HasUnicode": true,

        "AvailableInFieldTree": false,

        "OpenToAssociations": false,

        "OverlayBehavior": "MergeValues",

        "PropagateTo": [],

        "IsLinked": false,

        "FilterType": "None",

        "AllowSortTally": false,

        "Width": null,

        "AllowGroupBy": false,

        "AllowPivot": false,

        "Wrapping": false,

        "RelativityApplications": [],

        "AutoAddChoices": false,

        "Keywords": "",

        "Notes": ""

    }

}
```

View the JSON request for updating single object field

To update a single object field, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/single-object/{fieldArtifactID}
```

The following JSON illustrates a sample request:

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
{

    "fieldRequest":{

        "Name":  "Updated Single Object Field",

        "ObjectType": {

                "ArtifactID": 1042378,

                "ArtifactTypeID": 1000048,

                "Name":"Custom Object Type"

        },

        "AssociativeObjectType": {

                "ArtifactID": 1042580,

                "ArtifactTypeID": 1000051,

                "Name": "Custom Object Type Two"

        },

        "Source": "",

        "IsRequired": true,

        "AvailableInFieldTree": false,

        "FieldTreeView":{

            "Secured": false,

            "Value": {

                "ArtifactID": null

            }

        },

        "OpenToAssociations": false,

        "PropagateTo": [],

        "IsLinked": false,

        "FilterType": "Popup",

         "PopupPickerView":{

            "Secured": false,

            "Value": {

                "ArtifactID": null

            }

        },

        "AllowSortTally": false,

        "Width": null,

        "AllowGroupBy": false,

        "AllowPivot": false,

        "Wrapping": false,

        "RelativityApplications": [

           {

               "ArtifactID":1042630,

               "Guids":[]

           }

        ],

        "Keywords": "",

        "Notes": "Updated single object field."

    }

}
```

View the JSON request for updating a date field

To update a date field, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/date/{fieldArtifactID}
```

The following JSON illustrates a sample request:

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
{

    "fieldRequest":{

        "Name":  "Updated Custom Date Field",

        "ObjectType": {

                "ArtifactID": 1042378,

                "ArtifactTypeID":1000048,

                "Name":  "Custom Object Type"

        },

        "Source": "",

        "IsRequired": false,

        "Formatting": "Date",

        "OpenToAssociations": false,

        "PropagateTo": [],

        "IsLinked": false,

        "FilterType": "None",

        "AllowSortTally": false,

        "Width": null,

        "AllowGroupBy": false,

        "AllowPivot": false,

        "Wrapping": false,

        "Shortcut": {

           "ModifierKeys": [



           ],

           "MainKey": ""

        },

        "RelativityApplications": [

           {

               "ArtifactID":1042630,

               "Guids":[]

           }

            ],

        "Keywords": "",

        "Notes": "Updated data field"

    }

}
```

When the field is successfully updated, the response returns the status code of 200.

## Delete a field

To remove a field from Relativity, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/relativity.rest/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/{fieldArtifactID}
```

The request body is empty.

When the field is successfully deleted, the response returns the status code of 200.

## Retrieve available object types

You create fields on object types available in a workspace. To retrieve parent object types in a specific workspace, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/available-object-types
```

The request body is empty.

The response contains the following fields for each object type:

- Name - the user-friendly name of the object type.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- ArtifactID - the Artifact ID of an object type.

- Guids - an array of GUIDs used to identify the object type.

View the JSON response containing available object types Copy

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
[

    {

        "Name": "Custom Object Type",

        "ArtifactTypeID": 1000048,

        "ArtifactID": 1042378,

        "Guids": []

    },

    {

        "Name": "Custom Object Type Two",

        "ArtifactTypeID": 1000051,

        "ArtifactID": 1042580,

        "Guids": []

    },

    {

        "Name": "Custom Page",

        "ArtifactTypeID": 1000023,

        "ArtifactID": 1036920,

        "Guids": []

    },

    {

        "Name": "Dashboard",

        "ArtifactTypeID": 1000033,

        "ArtifactID": 1037793,

        "Guids": [

            "de1b78ff-b4c3-4e10-b01f-7065bcffa4b8"

        ]

    },

    {

        "Name": "Document",

        "ArtifactTypeID": 10,

        "ArtifactID": 1035231,

        "Guids": [

            "15c36703-74ea-4ff8-9dfb-ad30ece7530d"

        ]

    },

    {

        "Name": "Filter Set",

        "ArtifactTypeID": 1000034,

        "ArtifactID": 1037985,

        "Guids": [

            "25d34209-0930-488a-9295-8a5f398fb3f2"

        ]

    },

    {

        "Name": "Relativity Application",

        "ArtifactTypeID": 1000011,

        "ArtifactID": 1035572,

        "Guids": []

    },

    {

        "Name": "Relativity Time Zone",

        "ArtifactTypeID": 1000022,

        "ArtifactID": 1036668,

        "Guids": [

            "bc411c4d-285a-466b-8824-e084fd981f8b"

        ]

    },

    {

        "Name": "Search Terms Report",

        "ArtifactTypeID": 1000006,

        "ArtifactID": 1035313,

        "Guids": [

            "481e9acf-368b-4341-b6b5-a21153ad9950"

        ]

    },

    {

        "Name": "Search Terms Result",

        "ArtifactTypeID": 1000007,

        "ArtifactID": 1035324,

        "Guids": [

            "f1d86fc1-638a-48b3-a1ef-5fce03b40ce4"

        ]

    },

    {

        "Name": "Transform",

        "ArtifactTypeID": 1000005,

        "ArtifactID": 1035296,

        "Guids": [

            "c5a7f07a-2b12-4bc5-8e7d-e51526a9cf30"

        ]

    },

    {

        "Name": "Transform Set",

        "ArtifactTypeID": 1000004,

        "ArtifactID": 1035285,

        "Guids": [

            "6ffa970a-e8b0-4f53-a674-12ffaf4c60d4"

        ]

    }

]
```

## Retrieve available views for an object type

You can retrieve a list of available views for a specific object type that you can then use when creating or updating a new field. The following endpoint is used to retrieve this information for the field tree, pop-up picker, and relational views. The relational view is available only for documents. For more information, see on the RelativityDocumentation site.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/available-object-type-views
```

The request contains the following fields:

- ObjectType - contains the following fields:

- ArtifactID - the Artifact ID of the object type on which you are adding the field.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- Name - the user-friendly name of the object type.

Copy

```text
1
2
3
4
5
6
7
{

   "ObjectType":{

      "ArtifactID":1035231,

      "ArtifactTypeID":10,

      "Name":"Document"

   }

}
```

The response contains the following fields for each view:

- Secured - indicates whether the current user has permission to view the settings in the Value field.

- Value - contains the following fields:

- Name - the user-friendly name of the view.

- ArtifactID - the Artifact ID of the view.

- Guids - an array of GUIDs used to identify the view.

View the JSON response with available views for an object type Copy

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
[

    {

        "Secured": false,

        "Value": {

            "Name": "CaseMap Fields View",

            "ArtifactID": 1034267,

            "Guids": []

        }

    },

    {

        "Secured": false,

        "Value": {

            "Name": "Default Search View",

            "ArtifactID": 1003691,

            "Guids": []

        }

    },

    {

        "Secured": false,

        "Value": {

            "Name": "Documents",

            "ArtifactID": 1003684,

            "Guids": [

                "67f18ef0-2da2-4980-9519-a49392a321b3"

            ]

        }

    },

    {

        "Secured": false,

        "Value": {

            "Name": "Duplicates Documents",

            "ArtifactID": 1036632,

            "Guids": [

                "94c640e3-783c-484d-b9d1-758f76460a90"

            ]

        }

    },

    {

        "Secured": false,

        "Value": {

            "Name": "Family Documents",

            "ArtifactID": 1036633,

            "Guids": [

                "8b9dc379-ef1d-4aaf-a0c5-a647879943c9"

            ]

        }

    },

    {

        "Secured": false,

        "Value": {

            "Name": "Link Pane View",

            "ArtifactID": 1035254,

            "Guids": []

        }

    },

    {

        "Secured": false,

        "Value": {

            "Name": "Linked",

            "ArtifactID": 1035245,

            "Guids": []

        }

    },

    {

        "Secured": false,

        "Value": {

            "Name": "OCR Documents",

            "ArtifactID": 1035427,

            "Guids": [

                "98c0e1eb-828d-4004-af9c-8046893cebcb"

            ]

        }

    },

    {

        "Secured": false,

        "Value": {

            "Name": "Production Documents",

            "ArtifactID": 1003692,

            "Guids": []

        }

    },

    {

        "Secured": false,

        "Value": {

            "Name": "Search Results Pane View",

            "ArtifactID": 1034263,

            "Guids": []

        }

    }

]
```

## Retrieve available fields for propagation

When creating a field, you can determine whether coding values propagate to a specific group of related items. For more information about propagation, see on the Relativity Documentation site.

To retrieve the fields used for propagation in a workspace, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/available-propagate-to-fields
```

The request body is empty.

The response contains the following fields:

- Name - the user-friendly name of the relational field, such as Duplicates or Family.

- ArtifactID - the Artifact ID of the field.

- Guids - an array of GUIDs used to identify the field.

View the JSON response containing fields available for propagation Copy

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
[

    {

        "Name": "Duplicates",

        "ArtifactID": 1003669,

        "Guids": [

            "a426bc5e-3420-47b4-a293-4c4848a237d7"

        ]

    },

    {

        "Name": "Family",

        "ArtifactID": 1003671,

        "Guids": [

            "1f036749-a691-4aa8-8cf7-5eeb80c36caf"

        ]

    }

]
```

## Retrieve object types for a single object field

You can retrieve an array of object types that you can use to create a single object field type. For more information about single object fields, see on the Relativity Documentation site.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/available-single-associative-object-types
```

The request contains the following fields:

- ObjectType - contains the following fields:

- ArtifactID - the Artifact ID of the object type on which you are adding the field.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- Name - the user-friendly name of the object type.

Copy

```text
1
2
3
4
5
6
7
{

   "ObjectType":{

      "ArtifactID":1035231,

      "ArtifactTypeID":10,

      "Name":"Document"

   }

}
```

The response contains the following fields for each object type:

- Name - the user-friendly name of the object type.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- ArtifactID - the Artifact ID of an object type.

- Guids - an array of GUIDs used to identify the object type.

View the JSON response for containing compatible associative object types Copy

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
[

    {

        "Name": "Analytics Example",

        "ArtifactTypeID": 1000020,

        "ArtifactID": 1036417,

        "Guids": [

            "1f61cd9a-dacc-4e05-a5a3-8bf25baf7c22"

        ]

    },

    {

        "Name": "Custom Object Type",

        "ArtifactTypeID": 1000048,

        "ArtifactID": 1042378,

        "Guids": []

    },

    {

        "Name": "Custom Object Type Two",

        "ArtifactTypeID": 1000051,

        "ArtifactID": 1042580,

        "Guids": []

    },

    {

        "Name": "Custom Page",

        "ArtifactTypeID": 1000023,

        "ArtifactID": 1036920,

        "Guids": []

    },

    {

        "Name": "Dashboard",

        "ArtifactTypeID": 1000033,

        "ArtifactID": 1037793,

        "Guids": [

            "de1b78ff-b4c3-4e10-b01f-7065bcffa4b8"

        ]

    },

    {

        "Name": "Document",

        "ArtifactTypeID": 10,

        "ArtifactID": 1035231,

        "Guids": [

            "15c36703-74ea-4ff8-9dfb-ad30ece7530d"

        ]

    },

    {

        "Name": "Filter Set",

        "ArtifactTypeID": 1000034,

        "ArtifactID": 1037985,

        "Guids": [

            "25d34209-0930-488a-9295-8a5f398fb3f2"

        ]

    },

    {

        "Name": "Imaging Document Error",

        "ArtifactTypeID": 1000044,

        "ArtifactID": 1039765,

        "Guids": [

            "eb546506-1014-487c-959e-3c4cbff7e3f5"

        ]

    },

    {

        "Name": "Imaging Profile",

        "ArtifactTypeID": 1000015,

        "ArtifactID": 1035671,

        "Guids": [

            "c6fac105-3493-4551-b956-4757066e622f"

        ]

    },

    {

        "Name": "Imaging Set",

        "ArtifactTypeID": 1000016,

        "ArtifactID": 1035691,

        "Guids": [

            "ba574e88-7408-4434-a688-2324ecfc769e"

        ]

    },

    {

        "Name": "Imaging Warning",

        "ArtifactTypeID": 1000046,

        "ArtifactID": 1040023,

        "Guids": [

            "cfc3e5b9-b0dd-4c54-8937-a74334d33830"

        ]

    }

]
```

## Retrieve object types for a multiple object field

You can retrieve an array of associative object types that you can use to create a multiple object field. For more information about multiple object fields, see on the Relativity Documentation site.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/available-multi-associative-object-types
```

The request contains the following fields:

- ObjectType - contains the following fields:

- ArtifactID - the Artifact ID of the object type on which you are adding the field.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- Name - the user-friendly name of the object type.

Copy

```text
1
2
3
4
5
6
7
{

   "ObjectType":{

      "ArtifactID":1035231,

      "ArtifactTypeID":10,

      "Name":"Document"

   }

}
```

The response contains the following fields for each object type:

- Name - the user-friendly name of the object type.

- ArtifactTypeID - an integer value used as an identifier for an object type supported by Relativity. For example, the Artifact Type ID for a Document object is 10.

- ArtifactID - the Artifact ID of an object type.

- Guids - an array of GUIDs used to identify the object type.

View the JSON response containing compatible associative object types Copy

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
[

    {

        "Name": "Analytics Example",

        "ArtifactTypeID": 1000020,

        "ArtifactID": 1036417,

        "Guids": [

            "1f61cd9a-dacc-4e05-a5a3-8bf25baf7c22"

        ]

    },

    {

        "Name": "Custom Object Type",

        "ArtifactTypeID": 1000048,

        "ArtifactID": 1042378,

        "Guids": []

    },

    {

        "Name": "Custom Object Type Two",

        "ArtifactTypeID": 1000051,

        "ArtifactID": 1042580,

        "Guids": []

    },

    {

        "Name": "Custom Page",

        "ArtifactTypeID": 1000023,

        "ArtifactID": 1036920,

        "Guids": []

    },

    {

        "Name": "Dashboard",

        "ArtifactTypeID": 1000033,

        "ArtifactID": 1037793,

        "Guids": [

            "de1b78ff-b4c3-4e10-b01f-7065bcffa4b8"

        ]

    },

    {

        "Name": "Document",

        "ArtifactTypeID": 10,

        "ArtifactID": 1035231,

        "Guids": [

            "15c36703-74ea-4ff8-9dfb-ad30ece7530d"

        ]

    },

    {

        "Name": "Repeated Content Filter",

        "ArtifactTypeID": 1000013,

        "ArtifactID": 1035630,

        "Guids": [

            "e978b89b-2111-441e-8771-0cf42a41a8f6"

        ]

    },

    {

        "Name": "Search Terms Report",

        "ArtifactTypeID": 1000006,

        "ArtifactID": 1035313,

        "Guids": [

            "481e9acf-368b-4341-b6b5-a21153ad9950"

        ]

    },

    {

        "Name": "Search Terms Result",

        "ArtifactTypeID": 1000007,

        "ArtifactID": 1035324,

        "Guids": [

            "f1d86fc1-638a-48b3-a1ef-5fce03b40ce4"

        ]

    },

    {

        "Name": "Transform",

        "ArtifactTypeID": 1000005,

        "ArtifactID": 1035296,

        "Guids": [

            "c5a7f07a-2b12-4bc5-8e7d-e51526a9cf30"

        ]

    },

    {

        "Name": "Transform Set",

        "ArtifactTypeID": 1000004,

        "ArtifactID": 1035285,

        "Guids": [

            "6ffa970a-e8b0-4f53-a674-12ffaf4c60d4"

        ]

    }

]
```

## Retrieve keyboard shortcuts

You can retrieve a list of keyboard shortcuts currently defined in a workspace. In the Relativity UI, this list is displayed when you click the Keyboard Shortcuts Legend icon. For more information, see Keyboard shortcuts on the Relativity Documentation site.

Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/available-keyboard-shortcuts
```

The request body is empty.

View the JSON response for existing keyboard shortcuts Copy

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
[

    {

        "Shortcut": "Alt+Down Arrow",

        "Action": "Next Highlight",

        "ViewerMode": "Long Text, Viewer",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+E",

        "Action": "Switch to Long Text Mode",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+End",

        "Action": "Last Document",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+Enter",

        "Action": "Save and Next",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+Home",

        "Action": "First Document",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+I",

        "Action": "Switch to Image Mode",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+Left Arrow",

        "Action": "Page Up/Previous Image",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+M",

        "Action": "Toggle Modes (Draft/Normal/Preview)",

        "ViewerMode": "Long Text, Viewer",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+N",

        "Action": "Switch to Native Mode",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+P",

        "Action": "Switch to Productions Mode",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+Page Down",

        "Action": "Next Document",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+Page Up",

        "Action": "Previous Document",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+Right Arrow",

        "Action": "Page Down/Next Image",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+S",

        "Action": "Save",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+Shift+Z",

        "Action": "Copy From Previous",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+Space",

        "Action": "Edit",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+Up Arrow",

        "Action": "Previous Highlight",

        "ViewerMode": "Long Text, Viewer",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+V",

        "Action": "Switch to Viewer Mode",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Alt+Z",

        "Action": "Cancel",

        "ViewerMode": "All",

        "Category": "System"

    },

    {

        "Shortcut": "Ctrl+A",

        "Action": "Select All",

        "ViewerMode": "All",

        "Category": "Browser"

    },

    {

        "Shortcut": "Ctrl+C",

        "Action": "Copy",

        "ViewerMode": "All",

        "Category": "Browser"

    },

    {

        "Shortcut": "Ctrl+F",

        "Action": "Find",

        "ViewerMode": "All",

        "Category": "Browser"

    },

    {

        "Shortcut": "Ctrl+P",

        "Action": "Print",

        "ViewerMode": "All",

        "Category": "Browser"

    },

    {

        "Shortcut": "Ctrl+Shift+T",

        "Action": "Reopen Last Tab",

        "ViewerMode": "All",

        "Category": "Browser"

    },

    {

        "Shortcut": "Ctrl+T",

        "Action": "New Tab",

        "ViewerMode": "All",

        "Category": "Browser"

    },

    {

        "Shortcut": "Ctrl+V",

        "Action": "Paste",

        "ViewerMode": "All",

        "Category": "Browser"

    },

    {

        "Shortcut": "Ctrl+X",

        "Action": "Cut",

        "ViewerMode": "All",

        "Category": "Browser"

    }

]
```

## Retrieve valid keys

When creating or updating a field on a Document object, you can assign a keyboard shortcut to it. The shortcut key is a combination of a CTRL, ALT, or SHIFT key, and an alphanumeric or other key. For more information, see on the Relativity Documentation site.

You can use the following endpoint to retrieve all keys available for use when creating a keyboard shortcut. Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/valid-keys
```

The request body is empty.

View the JSON response for available keys Copy

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
[

    "Return",

    "Space",

    "PageUp",

    "PageDown",

    "End",

    "Home",

    "LeftArrow",

    "UpArrow",

    "RightArrow",

    "DownArrow",

    "A",

    "B",

    "C",

    "D",

    "E",

    "F",

    "G",

    "H",

    "I",

    "J",

    "K",

    "L",

    "M",

    "N",

    "O",

    "P",

    "Q",

    "R",

    "S",

    "T",

    "U",

    "V",

    "W",

    "X",

    "Y",

    "Z",

    "0",

    "1",

    "2",

    "3",

    "4",

    "5",

    "6",

    "7",

    "8",

    "9"

]
```

## Retrieve the order of relational field icons

You can retrieve the current order for relational field icons displayed in the Related Items pane of the core reviewer interface. The order assigned to a relational field icon determines its position relative to other icons in the Related Items pane. A relational field icon with a lower order number is displayed on the left, while those with the same order number are sorted alphanumerically.

In the Relativity UI, you can add or edit fields in the Fields layout, which contains the View Order button for relational field properties. Click this button to display the current order for icons in the Related Items pane. For more information, see Fields on the Relativity Documentation site.

To retrieve the current display order for the icons of relational fields available in a specific workspace, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Object-Model/{versionNumber}/workspaces/{workspaceID}/fields/available-relational-order
```

The request body is empty.

The response contains the following fields:

- Name - the user-friendly name of the relational field

- Type - a string indicating the type of the field, such as GroupIdentifier, MD5Hash, or others.

- Order - an integer representing the position of a relational field icon in the Related Items pane of the core reviewer interface.

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

        "Name": "Family",

        "Type": "GroupIdentifier",

        "Order": 0

    },

    {

        "Name": "Duplicates",

        "Type": "MD5Hash",

        "Order": 1

    },

    {

        "Name": "My Test Relational",

        "Type": "TestRelational",

        "Order": 10

    }

]
```

On this page

- Field Manager (REST)

- Guidelines for the Field Manager service

- URLs

- Supported field types

- Helper endpoints

- Relational fields

- Overlay behavior

- Filter types

- Source property

- Formatting fields

- Client code sample

- Postman sample file

- Create a field

- Read a field

- Update a field

- Delete a field

- Retrieve available object types

- Retrieve available views for an object type

- Retrieve available fields for propagation

- Retrieve object types for a single object field

- Retrieve object types for a multiple object field

- Retrieve keyboard shortcuts

- Retrieve valid keys

- Retrieve the order of relational field icons


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

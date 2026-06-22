---
title: "Script Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Extensibility/Script_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:05+00:00
sha256: f89cd8402381d283922fd3563f2d354ba58b1119ffc004ead6ca64e00af947c4
---

Script Manager (REST)

# Script Manager (REST)

In Relativity, you can execute SQL scripts through the UI that act on the databases backing an instance. You can implement these scripts to customize and extend Relativity functionality. For more information, see Scripts on the Relativity Documentation site.

If you use a Relativity script in a custom development project, it is recommended to make a copy of the script and use the copied script in your project. Software updates may modify the scripts provided by Relativity, which could cause unintended results if you use the Relativity-provided scripts directly in your custom development projects.

The Relativity Script Manager API service exposes endpoints for interacting with scripts as follows:

- Using CRUD operations on a script

- Retrieving script input parameters

- Previewing a script and its input parameters

- Importing a scripting

- Running jobs on a script, such as retrieving its status, exporting results, and others.

Use this service to create standalone applications that manage scripts across multiple environments or across workspaces in a single environment.

You can also use the Script service through .NET. For more information, see Script Manager API .

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the Script Manager service. To download the sample file, click Script Manager Postman file .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Guidelines for the Script Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to update a script:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/{scriptID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {workspaceID} to the Artifact ID of the workspace that contains the script.

- {scriptID} to the Artifact ID of a script.

## Client code sample

To use the Script Manager service, send requests by making calls with the required HTTP methods. You can use the following .NET code as a sample client for creating a script.

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
18
19
20
21
22
public async Task<int> CreateScriptAsync()

{

    int scriptID = 0;

    using (Relativity.Extensibility.{versionNumber}.Scripts.IScriptManager scriptManager = serviceFactory.CreateProxy<Relativity.Extensibility.{versionNumber}.Scripts.IScriptManager>())

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("<user login>:<user password>")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

        client.BaseAddress = new Uri("http://<host name>/");

        string inputJSON = @"{""ScriptRequest"":{""ScriptBody"":""<script><name>My script Name</name><description>About my script</description><category></category><input> <constant id=\""count\"" name=\""Rows\"" type=\""number\"" /></input><display type =\""itemlist\""/><action returns =\""table\""><![CDATA[ SELECT TOP(CAST(#count# AS INT)) * FROM [eddsdbo].[Artifact] ]]></action></script>"",""RelativityApplications"": []}}";

        string url = "/Relativity.rest/api/relativity-extensibility/{versionNumber}/workspaces/-1/scripts";

        HttpResponseMessage response = await client.PostAsync(url, new StringContent(inputJSON, Encoding.UTF8, "application/json"));

        response.EnsureSuccessStatusCode();

        string content = await response.Content.ReadAsStringAsync();

        scriptID = Int32.Parse(content);

    }

    return scriptID;

}
```

## Create a script

View code sample

To create a new relativity script in the specified workspace, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts
```

The request must contain the following fields:

- ScriptRequest - a request object containing the data required to create a new script.

- ScriptBody - the body of Relativity script to create in XML format.

- RelativityApplications - a list of applications, identified by Artifact ID or GUID, to associate with the new script.

- ArtifactID - the Artifact ID of an application.

- Guids - a list of GUIDs used to identify the application.

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
{

    "ScriptRequest":

    {

        "ScriptBody": "<script><name>My script Name</name><description>About my script</description><category></category><input> <constant id=\"count\" name=\"Rows\" type=\"number\" /></input><display type =\"itemlist\"/><action returns =\"table\"><![CDATA[ SELECT TOP(10) * FROM[eddsdbo].[Artifact] ]]></action></script>",

        "RelativityApplications": [

            {

                "ArtifactID": 123456

            }

        ]

    }

}
```

The response is an integer representing the Artifact ID of the created script.

Copy

```text
1
123456
```

## Read a script

View code sample

To retrieve information, including script body, about specified script, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/{scriptID}
```

If you would need to retrieve metadata and actions in addition to the script information, you can modify the endpoint as follows:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/{scriptID}/true/true
```

The body of the request is empty.

The response contains the following fields:

- Category - contains any text specified in the category section of the script body.

- Description - contain any text specified in the description section of the script body.

- IsLinkedScript - indicates whether this script is linked to a script in the admin script library.

- Key - the value used to lock a script within Relativity. You cannot modify a locked script.

- ReportGroupURL - a custom page URL used to create new tabs for displaying scripts of the same category.

- ScriptBody - the XML body of script.

- Version - the internal version of the script.

- CreatedOn - the date and time when the script was created.

- CreatedBy - the name and unique identifier for the user who created the script.

- LastModifiedBy - the name and unique identifier for the user who last updated the script.

- LastModifiedOn - the date and time when the script was last updated.

- Meta - provides additional information available as extended metadata. It includes the following fields:

- Unsupported - a listed of fields not supported on the current instance of this user.

- ReadOnly - an array of user properties that cannot be modified.

- Actions - an array of Action objects indicating operations that you have permissions to perform on this user. Each Action object contains the following fields that are available as extended metadata:

- Name - the name of an operation available through REST for the user, such as delete, update, and others.

- Href - the URL used to make an HTTP request for the operation.

- Verb - the name of the HTTP method for the operation.

- IsAvailable - a Boolean value indicating whether you have permissions to perform the operation on this user.

- Reason - provides an explanation for the unavailability of an action.

- Name - the name of the script as specified in the script body.

- ArtifactID - the Artifact ID of script.

- Guids - a list of GUIDs associated with the script.

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
{

    "Category": "",

    "Description": "About my script",

    "IsLinkedScript": false,

    "Key": "",

    "ReportGroupURL": "%ApplicationPath%/Case/RelativityScript/Run.aspx?%AppID%&%SystemID%&category=",

    "ScriptBody": "<script>\r\n\t<name>My script Name</name>\r\n\t<description>About my script</description>\r\n\t<category></category>\r\n\t<input />\r\n\t<display type=\"itemlist\" />\r\n\t<action returns=\"table\"><![CDATA[\n\t\t\t\t\t\t\n\t\t\t\t\t\t\tSELECT TOP(10) * FROM [eddsdbo].[Artifact]\n\t\t\t\t\t\t]]></action>\r\n</script>",

    "Version": "",

    "CreatedOn": "2020-06-12T19:51:49.79",

    "CreatedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9,

        "Guids": []

    },

    "LastModifiedBy": {

        "Name": "Admin, Relativity",

        "ArtifactID": 9,

        "Guids": []

    },

    "LastModifiedOn": "2020-06-12T19:51:49.79",

    "Meta": {

        "Unsupported": [

            "RelativityApplications"

        ],

        "ReadOnly": []

    },

    "Actions": [

        {

            "Name": "Delete",

            "Href": "relativity-extensibility/{versionNumber}/workspaces/-1/scripts/1021654",

            "Verb": "DELETE",

            "IsAvailable": true,

            "Reason": []

        },

        {

            "Name": "Update",

            "Href": "relativity-extensibility/{versionNumber}/workspaces/-1/scripts/1021654",

            "Verb": "PUT",

            "IsAvailable": true,

            "Reason": []

        }

    ]

    "Name": "My script Name",

    "ArtifactID": 1021654,

    "Guids": []

}
```

## Update a script

View code sample

To modify an existing script, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/{scriptID}
```

See the following sample JSON request:

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
{

    "ScriptRequest":

    {

        "ScriptBody": "<script><name>My script Name</name><description>About my script</description><category></category><input /><display type =\"itemlist\"/><action returns =\"table\"><![CDATA[ SELECT TOP(10) * FROM[eddsdbo].[Artifact] ]]></action></script>",

        "RelativityApplications": [

            {

                "ArtifactID": 123456

            }

        ]

    }

}
```

When the script is successfully updated, the response contains the status code of 200. If an error occurred parsing the script body or the Artifact ID is invalid, a status code of 400 is returned.

## Delete a script

View code sample

To delete an existing script, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/{scriptID}
```

Deleting a script from the admin library also removes delete any copies imported into workspaces.

The request body is empty.

When the script is successfully deleted, the response contains the status code of 200. If the workspace ID or the Artifact ID is invalid, a status code of 400 is returned.

## Import a script

View code sample

To import a script from the admin library to the workspace script library, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/import
```

The request must contain the following fields:

- ScriptImportRequest - contains information needed for script import.

- LibraryScript - identifies the script in the admin script library by Artifact ID or GUID. This script is imported into workspace script library.

- RelativityApplications - identifies applications that you want to associate with the script by Artifact ID or GUID.

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
{

    "ScriptImportRequest":{

        "LibraryScript":{

            "ArtifactID": 123456

        },

        "RelativityApplications": [

            {

                "ArtifactID": 789123

            }

        ]

    }

}
```

When a script is successfully imported, the response contains the Artifact ID of the script in the target workspace that was specified in the endpoint.

Copy

```text
1
456789
```

## Get script parameters

View code sample

To retrieve a list of the input parameters defined a script, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/{scriptID}/parameters
```

The request body is empty.

The response contains the following fields:

- Name - the name of the input parameter. The Relativity UI displays this name when it prompts the user for a value required to run the script.

- Identifier - the parameter identifier. In the SQL body, the identifier refers to a parameter.

- IsRequired - indicates whether a user must provide a value when running the script.

- Type - indicates type of parameter.

- Attributes - information specific to the parameter type.

- PossibleValues - a set of values the user must select when running the script. List these values in this field.

- Identifier - the identifier for the script parameter as defined in the script body.

- DisplayValue - the name of the value selection displayed in the UI when script runs.

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
[

    {

        "Name": "Rows",

        "Identifier": "count",

        "IsRequired": true,

        "Type": "Number",

        "Attributes": {

            "precision": "18",

            "scale": "0"

        },

        "PossibleValues": []

    }

]
```

## Preview a script body and input values

View code sample

To preview a script body with input values before running it, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/{scriptID}/preview
```

The request must contain the following fields:

- Inputs - an array of data providing a value for each parameter defined in the script.

- Identifier - an input parameter identifier. This value is case-sensitive.

- Value - value to use for parameter when generating SQL preview.

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
{

    "Inputs": [

        {

            "Identifier": "count",

            "Value": "25"

        }

    ]

}
```

When a preview request is successful, the response contains a string representing the SQL executed when the script runs, and the input parameters applied.

Copy

```text
1
"EXECUTE sp_executesql N'SELECT TOP(CAST(@count AS INT)) * FROM [eddsdbo].[Artifact]', N'@count DECIMAL(18,0)', 22"
```

## Run script jobs and reports

This section contains endpoints and JSON samples that illustrate how to run jobs, query for results, export results, and clean up script jobs.

You should call the CleanupRunJobAsync method once querying the results of your script job has finished.

- Enqueue run job

- Read run job

- Query action job results

- Export action results

- Export script report

- Clean up run job

### Enqueue run job

View code sample

To queue a script for running, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/{scriptID}/run
```

The request must contain the following fields:

- Inputs - an array of data with a value for each parameter defined in the script.

- Identifier - an input parameter identifier. This value is case-sensitive.

- Value - a value used for specifying an input parameter.

- TimeZoneOffset - the time zone offset for use in the script. Reference this value in the script body using the format #TimeZoneOffset#.

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

    "Inputs": [

        {

            "Identifier": "count",

            "Value": "25"

        }

    ],

    "TimeZoneOffset": 0

}
```

When an enqueue request is successful, the response contains a unique script run job identifier used for checking job status, and querying and exporting script results.

Copy

```text
1
"RunJobID": "a081c453-ae0d-44f4-a204-def5e556a396"
```

### Read run job

View code sample

To return the status of the script run job and each action contained in the script, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/run-jobs/{runJobID}
```

The runJobID is a GUID.

The request body is empty.

The response contains the following fields about the state of the script job and the individual actions:

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
{

    "Status": "Completed",

    "ActionJobs": [

        {

            "Name": "",

            "ReturnType": "Table",

            "AllowHtmlTagsInOutput": false,

            "ErrorMessage": "",

            "Columns": [

                {

                    "Name": "ArtifactID",

                    "DataType": "Number"

                },

            ...

            ],

            "RowsAffected": 0,

            "Status": "Completed"

        }

    ],

    "ErrorMessage": ""

}
```

### Query action job results

View code sample

To return completed script action results that match query filter and sort criteria, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/run-jobs/{runJobID}/actions/{actionIndex}/query-results
```

Set the path parameters as follows:

- workspaceID - the Artifact ID of the workspace containing the script.

- runJobID - a GUID identifying the job.

- actionIndex - the zero-based index of the script action to query. All scripts contain at least one action section, but they can multiple action sections that execute in sequence. A value of 0 refers to the first action in the script, 1 refers to the second action, and so on. The action 0 always works. An error is returned when a value of 1 is entered for a script with only a single action section.

The request must contain the following fields:

- Inputs - an array of data providing a value for each parameter defined in the script.

- Condition - criteria used to filter returned results.

- Sorts - criteria used to sort results.

- ColumnNames - specific column names to return in results. Use an asterisk ("*") to return all columns.

- Start - used for pagination. Zero-index of first row in the response.

- Length - used for pagination. Number of rows in response. If this value is 0 (or not set) it will default to 10,000. Values larger than 10,000 results will be respected if specified.

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

    "ActionQueryRequest":

    {

        "Condition":"'TextIdentifier' LIKE 'important'",

        "Sorts":

            [

                {

                    "ColumnName": "TextIdentifier",

                    "Direction": "Ascending"

                }

            ],

        "ColumnNames":

            [

                "TextIdentifier"

                "ArtifactID"

            ]

    },

    "Start": 0,

    "Length": 10

}
```

A successful query action job request returns all the results from the specified script run action that meet the query criteria in the request.

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

    "TotalCount": 25,

    "Rows": [

        {

            "Values": [

                "Active",

                662

            ]

        },

        {

            "Values": [

                "Admin Mode",

                -1

            ]

        },

    ...

        {

            "Values": [

                "WorkspacesOnPicker",

                359

            ]

        }

    ],

    "Columns": [

        {

            "Name": "TextIdentifier",

            "DataType": "Text"

        },

        {

            "Name": "ArtifactID",

            "DataType": "Number"

        }

    ],

    "CurrentStartIndex": 0,

    "ResultCount": 25

}
```

### Export action results

View code sample

To export completed script action results that match query filter/sort conditions, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/run-jobs/{runJobID}/actions/{actionIndex}/export-results
```

Set the path parameters as follows:

- workspaceID - the Artifact ID of the workspace containing the script.

- runJobID - a GUID identifying the job.

- actionIndex - the zero-based index of the script action to query. All scripts contain at least one action section, but they can multiple action sections that execute in sequence. A value of 0 refers to the first action in the script, 1 refers to the second action, and so on. The action 0 always works. An error is returned when a value of 1 is entered for a script with only a single action section.

The request must contain the following fields:

- Inputs - an array of data providing a value for each parameter defined in the script.

- Condition - criteria used to filter returned results.

- Sorts - criteria used to sort results.

- ColumnNames - specific column names to return in results. Use an asterisk ("*") to return all columns.

export-results does not provide 'start' and 'length' parameters, and it will always return all rows returned by the SQL script. For performance reasons, you may want to use query-results instead and use paging by specifying the 'start' and 'length' parameters in query-results.

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

    "ActionExportRequest": {

        "QueryRequest": {

            "Condition": "",

            "Sorts": [

                {

                    "ColumnName": "TextIdentifier",

                    "Direction": "Ascending"

                }

            ],

            "ColumnNames": [

                "*"

            ]

        }

    }

}
```

A successful export action job request returns all the specified results from the script action as a CSV text file.

Copy

```text
1
2
3
4
5
6
7
"ArtifactID","ArtifactTypeID","ParentArtifactID","AccessControlListID","AccessControlListIsInherited","CreatedOn","LastModifiedOn","LastModifiedBy","CreatedBy","TextIdentifier","ContainerID","Keywords","Notes","DeleteFlag",

"662","7","62","1","True","1/1/2007 12:00:00 AM","1/1/2007 12:00:00 AM","9","9","Active","62"," "," ","False",

"'-1","8","62","1","False","9/29/2014 3:32:47 PM","9/29/2014 3:32:47 PM","9","9","Admin Mode","62","","Admin Workspace - to be used for admin permissions only","False",

...

"359","4","62","1","True","1/1/2007 12:00:00 AM","8/5/2008 12:38:34 AM","9","9","WorkspacesOnPicker","62","","","False",
```

### Export script report

View code sample

To return completed script results (for all actions) that match query filter/sort conditions, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/run-jobs/{runJobID}/export-report
```

The runJobID is a GUID.

The request must contain the following fields:

- Inputs - an array of data providing a value for each parameter defined in the script.

- FileType - format of returned file. Available options are HTML, CSV, PDF, XLS, XLSX, RTF, PNG.

Copy

```text
1
2
3
4
5
6
{

    "ScriptExportRequest":

    {

        "FileType": "PDF"

    }

}
```

A successful export script report request returns the script results in the specified file format.

### Clean up run job

View code sample

To clean up all temporary tables created as part of a script run job, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-extensibility/{versionNumber}/workspaces/{workspaceID}/scripts/run-jobs/{runJobID}
```

The runJobID is a GUID.

The request body is empty.

There is no response body.

After you call this endpoint, the script results are no longer available for query or export.

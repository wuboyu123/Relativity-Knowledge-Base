---
title: "Instance Setting Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Instance_Setting_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:22:59+00:00
sha256: f7645edf6176bf5b247497449db3e7302e4eb43ba1e0fc6e8751724d40a05fc8
---

Instance Setting Manager (REST)

# Instance Setting Manager (REST)

The Instance Setting Manager service supports create, read, update, and delete operations in a Relativity environment. With the create endpoint, you can set the value for the instance setting, and its initial or default value. For general information, see Instance settings on the Relativity Documentation site.

Sample use cases for the Instance Setting Manager service include:

- Updating instance setting values to support behavior implemented by a custom application. You might implement a custom application that sends out email notifications and want to programmatically update the From and To fields on the messages by setting the EmailFrom and EmailTo instance settings.

- Updating instance setting values to modify or customize existing Relativity behavior. For example, you might want to programmatically change the time frame for running off hour agents by updating the AgentOffHourEndTime and AgentOffHourStartTime instance settings.

You can also use the Instance Setting Manager service through .NET. For more information, see Instance Setting Manager (.NET) .

## Guidelines for the Instance Setting Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to retrieve an instance setting:

Copy

```text
1
<host>/Relativity.REST/api/relativity-environment/{versionNumber}/workspaces/-1/instance-settings/{instanceSettingID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {instanceSettingID} to the Artifact ID of a specific instance setting.

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the Instance Setting Manager service. To download the sample file, click Instance Setting Manager Postman file .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Client code sample

To use the Instance Setting Manager service, send requests by making calls with the required HTTP methods. See the following base URL for this service:

Copy

```text
1
<host>/Relativity.REST/api/relativity-environment/{versionNumber}/workspaces/-1/instance-settings/
```

You can use the following .NET code as a sample client for creating an instance setting. This code illustrates how to perform the following tasks:

- Instantiate an HttpClient object for sending requests to the Instance Setting Manager service.

- Set the required headers for the request. For information on setting headers, see HTTP headers .

- Set the url variable to the URL for the admin-level context where the instance setting is to be added. For more information, see Create an instance setting .

- Set the JSON payload required for the operation.

- Use the PostAsync() method to send a POST request.

- Return the results of the request as a string.

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
private HttpClient GetHttpClient()

{

    HttpClient httpClient = new HttpClient();

    httpClient.BaseAddress = new Uri("https://localhost/");

    httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

    httpClient.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword")));

    return httpClient;

}

public async Task<int> Create()

{

    string url = "/Relativity.REST/api/Relativity.InstanceSettings/workspace/-1/instancesettings/";

    string payload = @"{{

        ""instanceSetting"": {{

            ""Name"": ""Sample Instance Setting name"",

            ""Section"": ""Sample Instance Setting section"",

            ""Machine"": """",

            ""ValueType"": 1,

            ""Value"": ""Sample text value!"",

            ""InitialValue"": ""Sample initial value"",

            ""Encrypted"": false,

            ""Description"": ""Sample description"",

            ""Keywords"": ""Sample keywords"",

            ""Notes"": ""Sample notes""

        }}

    }}";

    var content = new StringContent(payload, Encoding.UTF8, "application/json");

    HttpClient httpClient = GetHttpClient();

    HttpResponseMessage response = await httpClient.PostAsync(url, content);

    string result = await response.Content.ReadAsStringAsync();

    if (response.StatusCode != HttpStatusCode.OK)

    {

        throw new Exception($"Failed to create: {result}");

    }

    int artifactID = int.Parse(result);

    _logger.LogDebug($"REST call was successful. Created Instance Setting with artifact ID {artifactID}.");

    return artifactID;

}
```

## Create an instance setting

Instance settings are used to control specific behavior in Relativity, such as query time outs, time frames for running certain agents, and other configuration options. For more information and a list of available settings, see Instance settings on the Relativity Documentation site.

To create an instance setting, send a POST request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-environment/{versionNumber}/workspaces/-1/instance-settings
```

View required permissions

To use this endpoint, the caller must have the following:

- Add permissions for the instance setting set at the instance level. See Instance security on the Relativity Documentation site.

View field descriptions for a create request

The body of the request contains the following fields:

- instanceSetting - represents an Instance Setting object. It contains the following fields:

- Name - the name of the instance setting.

- Section - the name of the section in the Instance setting table where the instance setting is being added. For more information, see Instance setting table on the Relativity Documentation site.

- Machine - the name of the machine that value of the instance setting applies to. An empty string as a default value indicates that the instance setting applies to all machines in a Relativity instance.

- ValueType - indicates the type of the value for the instance setting. View a list of available values for the ValueType field

Name

Value

Description

Text value "Text" Indicates that the value should be treated as text.

32-bit integer value "Integer32" Indicates that the value be treated as a whole number from -2147483648 to 2147483647.

64-bit integer value "Integer64" Indicates that the value should be treated as a whole number from -9223372036854775808 to 9223372036854775807.

32-bit non-negative integer value "NonNegativeInteger32" Indicates that the value should be treated as a whole number from 0 to 2147483647.

64-bit non-negative integer value "NonNegativeInteger64" Indicates that the value should be treated as a whole number from 0 to 9223372036854775807.

32-bit positive integer value "PositiveInteger32" Indicates that the value should be treated as a whole number from 1 to 2147483647.

64-bit positive integer value "PositiveInteger64" Indicates that the value should be treated as a whole number from 1 to 9223372036854775807.

Boolean value "TrueFalse" Indicates that the value should be treated as a Boolean with only True or False valid values.

- Value - the value of the instance setting. Pass the value as a string.

- InitialValue - the initial value of the instance setting. Pass the value as a string.

- Encrypted - a Boolean value indicating whether the instance setting should be encrypted. Set this value to true if you want it encrypted.

- Description - a description of the instance setting.

- Keywords - optional words or phrase used to describe the instance setting.

- Notes - additional information about the instance setting.

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

   "instanceSetting":{

      "Name":"Sample Instance Setting name",

      "Section":"Sample Instance Setting section",

      "Machine":"",

      "ValueType":"Text",

      "Value":"Sample text value!",

      "InitialValue":"Sample initial value",

      "Encrypted":false,

      "Description":"Sample description",

      "Keywords":"Sample keywords",

      "Notes":"Sample notes"

   }

}
```

When a request is successful, the response contains the Artifact ID of the new instance setting, such as 1040499. It also returns the status code of 200.

## Read an instance setting

To read an instance setting, send a GET request for the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-environment/{versionNumber}/workspaces/-1/instance-settings/{instanceSettingID}
```

View required permissions

To use this endpoint, the caller must have the following:

- View permissions for instance settings set at the instance level. See Instance security on the Relativity Documentation site.

The request body is empty.

The response for a read operation contains the same fields as those for a create request body. See View field descriptions for a create request .

View additional field descriptions for a response

The response for a read operation also includes the following fields:

- CreatedBy - contains the Artifact ID and name of the user who created the instance setting. It also contains an array of GUIDs used to identify the user.

- CreatedOn - the date and time when the instance setting was added to Relativity.

- LastModifiedOn - the date and time when the instance setting was most recently modified.

- LastModifiedBy - contains the Artifact ID and name of the user who recently updated the instance setting. It also contains an array of GUIDs used to identify the user.

- ArtifactID - the Artifact ID for the instance setting.

- Guids - an array of GUIDs used to identify the instance setting.

View the JSON response for a read operation Copy

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

   "Section":"Sample Instance Setting section",

   "Machine":"",

   "Value":"Sample text value!",

   "InitialValue":"Sample initial value",

   "Description":"Sample description",

   "ValueType":"Text",

   "Encrypted":false,

   "Keywords":"Sample keywords",

   "Notes":"Sample notes",

   "CreatedOn":"2019-04-04T15:42:47.743",

   "CreatedBy":{

      "Name":"Admin, Relativity",

      "ArtifactID":9,

      "Guids":[

      ]

   },

   "LastModifiedOn":"2019-04-04T15:42:47.743",

   "LastModifiedBy":{

      "Name":"Admin, Relativity",

      "ArtifactID":9,

      "Guids":[

      ]

   },

   "Name":"Sample Instance Setting name",

   "ArtifactID":1023057,

   "Guids":[

   ]

}
```

## Update an instance setting

To update an instance setting, send a PUT request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-environment/{versionNumber}/workspaces/-1/instance-settings
```

View required permissions

To use this endpoint, the caller must have the following:

- Edit permissions for instance settings set at the instance level. See Instance security on the Relativity Documentation site.

The JSON request for the update operation contains the same fields as those for a create request. See View field descriptions for a create request .

View additional field descriptions for a request

A request also includes these fields:

- ArtifactID - the identifier for the instance setting to update.

- LastModifiedOn - the date and time when the instance setting was most recently modified. This field is only required if you want to restrict the update of an instance setting to the date that it was last modified. The value must match the LastModifiedOn date for the instance setting stored in Relativity. Otherwise, you receive a 409 error, indicating that the object has been modified.

You can only update the Machine, Value, Encrypted, Keywords and Notes fields. All other fields must have the same values as those specified in the create request or returned by a read request.

View sample JSON request Copy

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

   "instanceSetting":{

      "ArtifactID":1023057,

      "Name":"Sample Instance Setting name",

      "Section":"Sample Instance Setting section",

      "Machine":"",

      "ValueType":1,

      "Value":"Sample text value!",

      "InitialValue":"Sample initial value",

      "Encrypted":false,

      "Description":"Sample description",

      "Keywords":"Sample keywords",

      "Notes":"Sample notes"

   }

}
```

When the instance setting is successfully updated, the response returns the status code of 200.

## Delete an instance setting

To remove an instance setting from Relativity, send a DELETE request with a URL in the following general format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-environment/{versionNumber}/workspaces/-1/instance-settings/{instanceSettingID}
```

View required permissions

To use this endpoint, the caller must have the following:

- Delete permissions for instance settings set at the instance level. See Instance security on the Relativity Documentation site.

The request body is empty.

When the instance setting is successfully deleted, the response returns the status code of 200.

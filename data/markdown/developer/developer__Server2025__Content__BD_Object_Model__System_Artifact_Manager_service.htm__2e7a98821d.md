---
title: "System Artifact Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Object_Model/System_Artifact_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:28:20+00:00
sha256: c546ebe6bf3874a1953c9fa292f80715f556617468c13da10e4e6c176cad47d4
---

System Artifact Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# System Artifact Manager (REST)

The System Artifact Manager service exposes an endpoint used to retrieve the Artifact ID of a system artifact. Use this endpoint when you want to create top-level tabs or object types in a custom application. The System Artifact ID retrieved by this endpoint is passed to create requests as the parent of the new object that you want to create.

You can also use System Artifact Manager service through .NET. For more information, see System Artifact Manager (REST) .

## Guidelines for the System Artifact Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

## Client code sample

You can use the following .NET code as a sample client for retrieving the Artifact ID of a system artifact.

View code sample. Copy

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
using (HttpClient client = new HttpClient())

{

    client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

    client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("< user name >:< password >")));

    client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");

    client.BaseAddress = new Uri("https://localhost/");

    int workspaceID = 1022092;

    string identifier = "System";

    int artifactID;



    string url = $"/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/system-artifacts/{identifier}/artifact-id";

    using (HttpResponseMessage response = await client.GetAsync(url))

    {

        response.EnsureSuccessStatusCode();

        artifactID = Int32.Parse(await response.Content.ReadAsStringAsync());

    }

}
```

## Read system artifact ID

To retrieve the Artifact ID of a system artifact, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-object-model/{versionNumber}/workspaces/{workspaceID}/system-artifacts/{Identifier}/artifact-id
```

Set the path parameters as follows:

- {workspaceID} - the workspace containing the system artifact.

- {Identifier} - the string identifier for the system artifact.

Use -1 to reference the admin workspace.

A successful request returns an integer value representing the artifact ID of the specified system artifact.

Copy

```text
1
{ 1003663 }
```

On this page

- System Artifact Manager (REST)

- Guidelines for the System Artifact Manager service

- URLs

- Client code sample

- Read system artifact ID


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

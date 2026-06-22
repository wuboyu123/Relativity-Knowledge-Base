---
title: "Error Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Error_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:08+00:00
sha256: 2b4728304b868d5683b72ec3b5534236ad12dc60bfaa3e33f49ef2e16df4c2cb
---

Error Manager (REST)

# Error Manager (REST)

Relativity provides a logging mechanism called Errors. Through the REST API, the Error Manager API exposes a single endpoint for creating errors, which can be displayed in the Error tab in Relativity.

You can use this to create a single error log which can be found on the Error tab in Relativity using a returned ArtifactID.

## Guidelines for the Error Manager service

Review the following guidelines for working with this service.

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the Error Manager service. To download the sample file, click Error Manager Postman file .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Create an error log

To create an error log, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/api/relativity-environment/{versionNumber}/workspaces/-1/errors
```

The request body contains the following fields

- createErrorRequest - an object with the following fields:

- Message - (required) brief summary of what the error log is about.

- FullError - (optional) long message, call stack or exception details.

- Server - (optional) server name of where the error occurred.

- URL - (optional) URL of the resource where the error occurred (if CustomPage or Kepler service).

- StepsToReproduce - (optional) a few words what user can do to reproduce this error.

- Workspace - (optional) workspace name

- ArtifactID - (optional) with which workspace you want to associate this error.

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
{

    "createErrorRequest": {

        "Message": "Error message",

        "FullError": "Full error message (i.e. exception message)",

        "Server": "Server name",

        "Source": "Source name",

        "URL": "http://relativity.com",

        "StepsToReproduce": "1. Step one, 2. Step two",

        "Workspace": {

            "ArtifactID":-1

        }

    }

}
```

The newly created ArtifactID of the error log will be returned in the response.

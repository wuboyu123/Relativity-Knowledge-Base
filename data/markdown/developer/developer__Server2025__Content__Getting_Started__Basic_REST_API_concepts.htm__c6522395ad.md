---
title: "Basic REST API concepts"
url: https://platform.relativity.com/Server2025/Content/Getting_Started/Basic_REST_API_concepts.htm
collection: developer
fetched_at: 2026-06-22T06:25:11+00:00
sha256: 3c72a7ee7bd818464887cfb5baaad998c9574cd57c69e5eeee2ffe249aaa5cde
---

Basic REST API concepts Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Basic REST API concepts

Relativity provides access to many REST endpoints so you can easily make API calls from different coding languages and tools, such as cURL or Postman. REST calls are made over HTTP, providing language agnostic programming and a high level of flexibility. REST calls operate by providing a URL, an HTTP method, headers, and in some cases, a body. After you make a call, the server returns a status code, headers, and a body.

## Tools

You can easily test REST calls with tools like cURL , Postman , or ARC. These tools simplify setting headers and changing request bodies. They provide a quick way to test REST calls, so you can easily see the results of changing your request. In this tutorial, the screen shots are taken from Postman.

## URL

In Relativity, REST URLs consist of the following parts:

- Host

The host is the address of the server where your Relativity instance is hosted. If you go to http://mycompany.com/Relativity to access Relativity through the browser, then your host is http://mycompany.com.

- REST surface

The REST surface in the URL tells the Relativity server to expect a REST request. The REST APIs built on the Kepler framework include this information: /Relativity.REST/api/.

- Business domain and version

Business domains are used to group REST APIs built on the Kepler framework . Additionally, the APIs in a specific domain are versioned as they are updated. The URLs contain this information in the format: /<some-business-domain>/v<version number>/.

Each REST service has a related .NET API. The .NET APIs are also group by business domain and similarly versioned. They are then added to a NuGet package with the same name as the business domain. For more information, see Relativity Server APIs .

- Resource

The resource indicates to the Relativity server which REST endpoint that you are using. It specifies the Relativity object you are requesting. In this example, the resource indicates that you want to interact with a tab having the Artifact ID 26591409 contained in the workspace with the Artifact ID 26274927.

## Methods

REST services use HTTP methods when making requests to the server. These methods provide instructions for the action that you want to the server to perform on the data. Relativity REST APIs commonly use the following HTTP methods:

- GET

The GET method is used for reading data. GET requests don't contain a body rather they provide instructions for the server in the URL. You can use GET requests to obtain data on individual objects and on types of objects.

In this example, the request asks the server to provide information about the tab with the Artifact ID 26591409 contained in the workspace with the Artifact ID 26274927.

This request asks the server to return a list of all tabs in the workspace with the Artifact ID 1015349, which the calling user can access.

- POST

POST requests are commonly used for creating resources and querying. These requests use the POST method in combination with a request body containing information about the resource to create or the query to perform.

This request asks the server to create a new tab inside a workspace with the Artifact ID 1015349 and it includes a request body containing information needed to create the new tab.

For information on querying for document and Relativity Dynamic Object (RDOs), see Object Manager (REST) .

- PUT

PUT requests are used to update existing data. A PUT request uses a request body to provide the information needed to modify the resource.

This request tells the server to update the tab with the Artifact ID 26591409 contained in the workspace with the Artifact ID 26274927. It also indicates that the request body contains the information that the server should use to update the tab.

- DELETE

DELETE requests are used for removing an object from Relativity. DELETE requests include all the information required by the server in the URL, so they don't include a body.

This request tells the server to delete the tab with the Artifact ID 26591409 contained in the workspace with the Artifact ID 26274927.

Not all REST services use each of these HTTP methods. For more information, see the specific services listed on the Relativity Server APIs page.

## Headers

You can use headers to send additional information in a REST call without the need for a body. In Relativity, REST API calls require the following headers:

- X-CSRF-Header

The Cross-Site Request Forgery (CSRF) header is required in a request and must be set it to blank (empty string) or a single "-". This field provides basic security by preventing malicious parties from scanning your REST endpoint.

- Authorization

The Authorization header is required if you are using basic or Active Directory authentication. More information on this header can be found in Authentication .

- Content-Type

The Content-Type header provides the server with information about the format of the data. The Content-Type should be set to application/json, which means the body is in JSON format.

## Body

In Relativity services, request bodies for REST calls are typically used for POST and PUT methods and they are formatted in JSON. The structure of the JSON depends on the specific API being used. While they may be structured differently, some features of the JSON format are consistent across APIs.

- Query

For queries, Relativity typically supports specifying a condition, sort order, and the fields returned.

- Condition

You use the condition to declare the specific objects you want to query for. This condition is determined by a “condition” property in the JSON body.

- Sorts

You can indicate the order in which the objects are returned. This order is determined by a “sorts” property in the JSON body.

- Fields

You can also indicate the fields on the object that are returned from the query. These fields are determined by a “fields” property in the JSON body. To return all fields, include an asterisk (*).

Returning all fields is useful for testing, but it can dramatically decrease performance. We recommend returning only the fields you need.

- Create/Update

For creating and updating resources, you provide a JSON representation of the object you want to create or update.

The values set for fields in the JSON make up the new object in Relativity after the create or update completes. The following JSON illustrates how to create or update a single object field. For more information, see Field Manager (REST) .

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

## Authentication

Authentication is handled via the Authorization header. The REST APIs support the following authentication methods:

- Basic authentication

You authenticate with your Relativity username and password when using basic authentication. Your username and password must be computed into the Base64 encoding. If you are using Postman, you can type your username and password into the Authorization tab.

Postman sets the Authorization head with the encoded username and password prepended by the word Basic .

- Cookie authentication

When you log in to Relativity, a RelAuth cookie is issued to the browser. This encrypted cookie contains information that validates the logged in user. It can be passed to the REST APIs instead of an HTTP authorization header. If the encrypted cookie is valid, the call is authenticated under the credentials of the user who logged in via the web.

Applications that use custom pages often call Relativity APIs. For example, a custom page might make AJAX calls to a REST API. The RelAuth cookie is automatically added to any AJAX calls from the browser. This process enables most custom page applications to make their AJAX calls to the REST APIs and "piggy-back” on the browser’s authentication that is automatically handled by Relativity.

You don't need to include an Authorization header when using cookie authentication from JavaScript within Relativity. The browser performs the authentication.

-

Active Directory authentication

You can use Active Directory authentication with the REST APIs by setting AuthenticationData for users through the Relativity UI.

After configuring AuthenticationData in Relativity, follow the same process for sending credentials as that used by basic authentication.

- Bearer Token Authentication

When using bearer token authentication, clients access the API with an access token. The Relativity identity service issues this token based on a consumer key and secret obtained through an OAuth2 client. This OAuth2 client is set up via the UI. In Postman, you can input your access token using the Oauth 2.0 type.

Postman sets the Authorization head with the token information so you can make the call.

## Response

A response contains a response code and response body described as follows:

- Response code

A response code indicates the type of response sent by the server. For additional information, see HTTP response status codes on the MDN web site.

Relativity commonly uses the following response codes:

- 200 OK – Success.

-

400 Bad Request – Usually an issue with the body.

-

401 Unauthorized – Usually an authentication issue.

-

403 Forbidden – Usually a permissions issue.

-

404 Not Found – Usually an issue with the URL.

-

500 Internal Server Error – Could be an issue with the body.

- Response body

A response body from a REST API is JSON that contains information based on the type of request. For read and query requests, the response contains the objects and fields requested in a JSON body.

## Use Cases

Common use cases for REST APIs include creating documents and RDOs and submitting queries. For more information about these tasks, see Object Manager (REST) .

## Troubleshooting

To troubleshoot an unsuccessful REST call, review the response code sent by the server. When using REST API, a common error that may occur is an improperly formatted request body. You can locate information for a specific REST service on the Relativity Server APIs page and then use the JSON request examples to verify the format of your request body. For additional information, you can also use these resources:

- In Chrome DevTools, open the network tab when you execute an event in the UI. It captures the REST body used for this event and provides an example illustrating to structure it programmatically.

- Troubleshoot REST API errors

On this page

- Basic REST API concepts

- Tools

- URL

- Methods

- Headers

- Body

- Authentication

- Response

- Use Cases

- Troubleshooting


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

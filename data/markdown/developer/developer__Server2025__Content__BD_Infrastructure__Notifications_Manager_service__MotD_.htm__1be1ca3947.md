---
title: "Notifications Manager (MotD) - (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Infrastructure/Notifications_Manager_service__MotD_.htm
collection: developer
fetched_at: 2026-06-22T06:23:35+00:00
sha256: cb1c95bb899cae0dc2837c188385b40d8eacadce65a5337bac0bf31ee7d5ae8f
---

Notifications Manager (MotD) - (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Notifications Manager (MotD) - (REST)

The Message of the Day (MotD) is a message displayed to all users when they log in to Relativity. The MotD is commonly used to inform users of planned system maintenance. For more information, see Adding and editing a Message of the Day on the Relativity Documentation site.

The Notifications Manager API exposes methods for reading, updating, and dismissing the MotD. It also includes methods for determining whether the MotD has been dismissed, and whether it is displayed as plain text or HTML.

You can also use the Notifications Manager service through .NET. For more information, see Notifications Manager (MotD) - (.NET) .

## Guidelines for the Notifications Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

For example, you can use the following URL to dismiss a MotD:

Copy

```text
1
<host>/Relativity.REST/api/relativity-infrastructure/{versionNumber}/workspaces/-1/notifications/dismiss/{userID}
```

Set the path parameters as follows:

- {versionNumber} to the version of the API, such as v1 .

- {userID} to the Artifact ID of a specific user.

## Postman sample file

You can use the Postman sample file to become familiar with making calls to endpoints on the Notifications Manager service. To download the sample file, click Notifications Manager Postman file .

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman .

- Import the Postman sample file for the service. For more information, see Working with data files on the Postman web site.

- Select an endpoint. Update the URL with the domain for your Relativity environment and any other variables.

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- See the following sections on this page for more information on setting required fields for a request.

- Click Send to make a request.

## Client code sample

To use the Notifications Manager service, send requests by making calls with the required HTTP methods. You can use the following .NET code as a sample client for reading the properties of a MotD.

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
//Set up the REST client.

HttpClient httpClient = new HttpClient();

httpClient.BaseAddress = new Uri("http://localhost/");



//Set the required headers.

httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

httpClient.DefaultRequestHeaders.Add("Authorization",

    "Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA==");



//Call Read.

string url = "Relativity.Rest/API/relativity-infrastructure/v1/workspaces/-1/notifications";

HttpResponseMessage response = await httpClient.GetAsync(url);

string result = await response.Content.ReadAsStringAsync();

bool success = HttpStatusCode.OK == response.StatusCode;



//Parse the result with Json.NET.

JObject resultObject = JObject.Parse(result);
```

The -1 in the URLs for the Notification Manager service indicates the admin-level context.

## Read a MotD

To retrieve the properties of a MotD, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-infrastructure/{versionNumber}/workspaces/-1/notifications
```

The body of the request is empty.

The response includes the following fields:

- Message - a string representing the message displayed to users at login.

- Enabled - a Boolean value indicating whether MotD is enabled.

- AllowDismiss - a Boolean value indicating whether MotD can be dismissed.

Copy

```text
1
2
3
4
5
{

   "Message":"New Message of the Day",

   "Enabled":false,

   "AllowDismiss":true

}
```

## Update a MotD

To modify a MotD, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-infrastructure/{versionNumber}/workspaces/-1/notifications
```

The body of the request must contain the following fields:

- Message - a string representing the message displayed to users at login.

- Enabled - a Boolean value indicating whether MotD is enabled.

- AllowDismiss - a Boolean value indicating whether MotD can be dismissed.

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

   "request":{

      "message":"New Message of the Day",

      "enabled":false,

      "allowDismiss":true

   }

}
```

The response for an update operation contains the same fields as those for an update request. See the field descriptions for the request.

Copy

```text
1
2
3
4
5
{

   "Message":"New Message of the Day",

   "Enabled":false,

   "AllowDismiss":true

}
```

## Dismiss a MotD

To dismiss or close the MotD, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-infrastructure/{versionNumber}/workspaces/-1/notifications/dismiss/{userID}
```

Set {userID} to the Artifact ID of the user who is dismissing the MotD. The body of the request is empty.

When the MotD is successfully dismissed, the response returns the status code of 200. The response body is empty.

## Check for the dismissal of a MotD

To determine whether a user has previously dismissed the MotD, send a GET request with a URL in the following format:

Copy

```text
1
2
<host>/Relativity.REST/api/relativity-infrastructure/{versionNumber}/workspaces/-1/notifications/has-dismissed/{userID}<![CDATA[

]]>
```

Set {userID} to the Artifact ID of the user who is dismissing the MotD. The body of the request is empty.

The response returns a Boolean value indicating whether the user has dismissed the current MotD.

Copy

```text
1
false
```

## Check for text or HTML format of a MotD

To determine whether the MotD can display HTML or only text, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/relativity-infrastructure/{versionNumber}/workspaces/-1/notifications/is-text-only
```

The body of the request is empty.

The response returns a Boolean value indicating whether the MotD can display only text. In this example, the response of false indicates that the MotD can also display HTML.

Copy

```text
1
false
```

For more information about formatting the MotD, see the MOTDTextOnly instance setting in the Instance settings' descriptions page on the Relativity Documentation site.

On this page

- Notifications Manager (MotD) - (REST)

- Guidelines for the Notifications Manager service

- URLs

- Postman sample file

- Client code sample

- Read a MotD

- Update a MotD

- Dismiss a MotD

- Check for the dismissal of a MotD

- Check for text or HTML format of a MotD


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

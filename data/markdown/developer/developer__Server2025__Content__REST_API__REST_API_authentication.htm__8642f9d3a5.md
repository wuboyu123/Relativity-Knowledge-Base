---
title: "Relativity REST API authentication"
url: https://platform.relativity.com/Server2025/Content/REST_API/REST_API_authentication.htm
collection: developer
fetched_at: 2026-06-22T06:29:46+00:00
sha256: efab6ed7dc52f74048ad2b468ca5d8bc4464aa58c40ff6a58fe1de1f93af13b4
---

Relativity REST API authentication

# Relativity REST API authentication

The Relativity REST APIs support multiple authentication methods so that you can choose the best one for your environment and application requirements. To provide secure communication between a client and a Relativity endpoint, it supports basic authentication over HTTPS and Active Directory authentication.

An authentication header is required for all calls to the REST endpoint.

The Authorization field in the HTTP header is used to pass user credentials. When authentication fails, the error code 401 (Unauthorized) is returned with additional information in the WWW-Authenticate header of the response.

If a request doesn't include an authentication header, the error code 401 is returned with the header: Bearer realm="Relativity.REST". If you set DeveloperMode instance setting is set to True, this error isn't returned. For more information, see Basic authentication .

See the following related page:

- Identity (authentication and user accounts)

## Basic authentication

When using basic authentication over HTTPS, you should send authentication credentials with every REST request, since the service doesn't include an explicit login method or track a session token.

To include credentials in the HTTP header, you must supply a username and password that are concatenated into a string, using the format username:password . You must also compute the Base64 encoding for this string. The following code sample illustrates this process:

Copy

```text
1
2
3
4
5
6
public void SetAuthorizationHeader(string username, string password, HttpClient request)

{

     string usernamePassword = string.Format("{0}:{1}", username, password);

     string base64usernamePassword = Convert.ToBase64String(Encoding.ASCII.GetBytes(usernamePassword));

     request.DefaultRequestHeaders.Add("Authorization", "Basic " + base64usernamePassword);

}
```

A request includes the basic authentication header with the Authorization field followed by the word Basic (indicating the type of authentication), and the encoded user credentials:

Copy

```text
1
Authorization: Basic bXkudXNlckBrY3VyYS5jb206Q250VGNoVGhzMTIzNCE=
```

When an invalid basic authentication header is supplied on the request, a error code of 401 is returned with the following header:

Copy

```text
1
WWW-Authenticate: Bearer realm="Relativity.REST"
```

For more information about header fields, see HTTP headers .

## Cookie authentication

When a user logs into Relativity, the RelAuth cookie is issued to the browser. This encrypted cookie contains the information that validates the user. This cookie can be passed to REST service call instead of an HTTP authorization header. If the encrypted cookie is valid, the call will be authenticated under the credentials of the user who logged in via the web.

Applications that use custom pages often call REST services: a typical example can be a custom page that makes AJAX calls to a REST endpoint. The RelAuth cookie is automatically added to any AJAX calls from the browser. This enables most custom page applications to simply make their AJAX calls to the REST service and "piggy-back” on top of the browser’s authentication that is automatically handled by Relativity. For more information about custom pages, see Customize the UI .

### Cookie authentication from JavaScript

You don't need to include an additional Authorization header when using cookie authentication from JavaScript within Relativity. The browser performs the authentication. See the following code sample:

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
<script type = "text/javascript" >

    $(document).ready(function() {

        $.ajax({

                url: "http://localhost/Relativity.REST/Relativity/User",

                type: "GET",

                contentType: "application/json"

            })

            .done(function(data) {

                alert("success");

                var userCount = data.ResultCount;

                var retVal = "userCount: " + userCount;

                $("#result").text(retVal);

            })

            .fail(function(xhr, status, error) {

                alert("Status: " + status);

                alert("Error: " + error);

                alert("ResponseText: " + xhr.responseText);

            })

            .always(function() {

                alert("complete");

            });

    });
```

## Active Directory authentication

You can use Active Directory authentication with a REST service by setting AuthenticationData for users through the Relativity UI. For more information, see Fields on the Users page of the Relativity Documentation site.

After configuring AuthenticationData in Relativity, follow the same process for sending credentials as that used by basic authentication . Compute the Base64 encoding for the username and Active Directory password, and add this string to the Authorization header.

Active Directory authentication uses Basic as the authorization method in the HTTP header.

## Bearer token authentication

You can also connect to the REST services using bearer token authentication. When using bearer token authentication, clients access the service with an access token issued by the Relativity identity service based on a consumer key and secret obtained through an OAuth2 client.

When multiple web servers are hosted behind a load balanced route, you can't programmatically retrieve an authentication token. You must use a direct route to one of the web servers to retrieve the authentication token.

To get an access token:

- Create a Relativity OAuth2 client:

- OAuth2 Flow must be Client Credentials .

- The context user must be a member of the Relativity Administrators group.

For more information, see OAuth2 clients on the RelativityOne Documentation site. You can also interact with OAuth2 clients programmatically .

- Make a POST request to the following URL: Copy

```text
1
https://[host]/Relativity/Identity/connect/token
```

The request content type must be x-www-form-urlencoded .

The request must include these parameters:

- client_id – the ID of the OAuth2 client.

- client_secret – The secret of the OAuth2 client.

- scope – SystemUserInfo .

- grant_type – client_credentials .

This is a cURL example of a token request :

Copy

```text
1
2
3
4
curl -X POST \

  https://[host]/Relativity/Identity/connect/token \

  -H 'content-type: application/x-www-form-urlencoded' \

  -d 'client_id=t348bff173b12ok36d6d5ab80id&client_secret=69f2c71d25e464fba614e19fcc1430d5b256b7a2&scope=SystemUserInfo&grant_type=client_credentials'
```

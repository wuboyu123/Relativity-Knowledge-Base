---
title: "Proxies and authentication"
url: https://platform.relativity.com/Server2025/Content/Kepler_framework/Proxies_and_authentication.htm
collection: developer
fetched_at: 2026-06-22T06:31:08+00:00
sha256: b893572ed0f778ae0d6ba419f5f33be011dcb01941bd0bf2b44439a6da5721c3
---

Proxies and authentication Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Proxies and authentication

The Kepler framework uses a proxy to handle client requests. It exposes a factory class that you can use to create the a client proxy by passing URIs to the required services and credentials. The following sections outline this process and available authentication methods.

## ServiceFactory class

Use the ServiceFactory class to create proxies for Kepler services. The T CreateProxy<T>() method is used to create the proxy, which takes and returns the following:

- Generic type T - the service contract, which is the interface defining the service.

- Proxy - a .NET object that implements the contract returned by the method.

Use the following parameters to construct a ServiceFactory object, which is available through the ServiceFactorySettings class:

- REST base URI - used to construct the full URI to Kepler services. It uses the following format: Copy

```text
1
<scheme>://<machine name>/Relativity.Rest/api
```

- Credentials - see Authentication for Kepler services .

The following code sample illustrates how to create a proxy. For sample usage, see Client .NET proxy .

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
Uri relativityRestUri = new Uri(@"http://localhost/relativity.rest/api");

ServiceFactorySettings settings = new ServiceFactorySettings(relativityRestUri, new BearerTokenCredentials(GetBearerToken().AccessToken)); // see code sample for BearerTokenCredentials

ServiceFactory factory = new ServiceFactory(settings);

// Create a proxy for a Kepler service

IExampleService proxy = factory.CreateProxy<IExampleService>();

bool serviceOkay = await proxy.PingAsync();
```

### Create a proxy using username and password

The following code sample illustrates how to create a proxy using username and password. For sample usage, see Client .NET proxy .

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
Uri relativityRestUri = new Uri(@"http://localhost/relativity.rest/api");

Credentials credentials = new UsernamePasswordCredentials("username", "password");

ServiceFactorySettings settings = new ServiceFactorySettings(relativityRestUri, credentials);

ServiceFactory factory = new ServiceFactory(settings);

// Create a proxy for a Kepler service

IExampleService proxy = factory.CreateProxy<IExampleService>();

bool serviceOkay = await proxy.PingAsync();
```

## Client .NET proxy

Use the client .NET proxy to interact with a Kepler service as a set of .NET objects. This proxy is created using the ServiceFactory class. The proxy type is the same as the Kepler service interface, and each member method becomes a service endpoint.

When you call a member method, the proxy makes a corresponding HTTP request to the respective service endpoint, using the appropriate URL, HTTP headers, and verbs. The response from the endpoint has the return type of the proxy method that was called.

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
// ServiceFactory used to create a proxy object. (Omitting constructor parameters for simplicity.)

var factory = new ServiceFactory(...);

// Create client-side service proxy.

var proxy = factory.CreateProxy<IExampleService>();

// Use the proxy to exercise a Kepler service as .NET object.

bool serviceOK = await proxy.PingAsync();

// Use the service responses

if (serviceOK) {

    Console.WriteLine("Service is okay.");

}
```

## Authentication for Kepler services

The Kepler framework uses methods that take credentials for OAuth2 and basic authentication. It also supports cookie authentication through the browser. See the following sections for more information:

- Credentials

- Cookie authentication

### Credentials

The Kepler framework supports the following credential types:

Bearer Token is recommended rather than using username and password

- BearerTokenCredentials() method - takes credentials used for OAuth2 authentication. For more information, see Bearer token authentication and Client Credentials on the Oauth website. Below are code snippets using IdentityModel (deprecated) or Duende.IdentityModel: Copy code snippet using https://www.nuget.org/packages/IdentityModel (deprecated)

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
//import https://www.nuget.org/packages/IdentityModel

//Get Access token

HttpClient httpClient = new HttpClient();

ClientCredentialsTokenRequest tokenRequest = new ClientCredentialsTokenRequest() {

    Address = "https://[host]/Relativity/Identity/connect/token",

    ClientId = "client_id",

    ClientSecret = "secret",

    Scope = "UserInfoAccess"

};

TokenResponse response = httpClient.RequestClientCredentialsTokenAsync(tokenRequest).ConfigureAwait(false).GetAwaiter().GetResult();
```

Copy code snippet using https://www.nuget.org/packages/Duende.IdentityModel

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
//import https://www.nuget.org/packages/Duende.IdentityModel

using System;

using System.Net.Http;

using Duende.IdentityModel.Client;

// Get access token (synchronously, to match the original style)

HttpClient httpClient = new HttpClient();

var tokenRequest = new ClientCredentialsTokenRequest {

    Address      = "https://[host]/Relativity/Identity/connect/token",

    ClientId     = "client_id",

    ClientSecret = "secret",

    Scope        = "UserInfoAccess"

};

var response = httpClient

    .RequestClientCredentialsTokenAsync(tokenRequest)

    .ConfigureAwait(false)

    .GetAwaiter()

    .GetResult();

if (response.IsError) {

    throw new Exception(response.Error);

}

string accessToken = response.AccessToken;
```

Copy Async code snippet using https://www.nuget.org/packages/Duende.IdentityModel

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
//import https://www.nuget.org/packages/Duende.IdentityModel

using System.Net.Http;

using Duende.IdentityModel.Client;

HttpClient httpClient = new HttpClient();

var response = await httpClient.RequestClientCredentialsTokenAsync(new ClientCredentialsTokenRequest {

    Address      = "https://[host]/Relativity/Identity/connect/token",

    ClientId     = "client_id",

    ClientSecret = "secret",

    Scope        = "UserInfoAccess"

});

if (response.IsError) throw new Exception(response.Error);

var accessToken = response.AccessToken;
```

- UserNamePasswordCredentials() method - takes credentials used for basic authentication. For more information, see Basic authentication . Copy

```text
1
2
// Pass in the username and password to this method.

Credentials credentials = new UsernamePasswordCredentials(username, password);
```

### Cookie authentication

When a user logs into Relativity, the RelAuth cookie is issued to the browser. This encrypted cookie contains the information that validates the user. This cookie can be passed to REST service call instead of an HTTP authorization header. If the encrypted cookie is valid, the call will be authenticated under the credentials of the user who logged in via the web. For more information, see Cookie authentication .

Cookie authentication only apples to browser-based calls, such as those made through JavaScript, to Kepler services.

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

</script>
```

On this page

- Proxies and authentication

- ServiceFactory class

- Create a proxy using username and password

- Client .NET proxy

- Authentication for Kepler services

- Credentials

- Cookie authentication


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

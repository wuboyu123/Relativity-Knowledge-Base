---
title: "Error Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Environment/Error_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:07+00:00
sha256: 577bcf37326956ff32226101744a556f4cbdb7dfed4659af2351c24256d455f2
---

Error Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Error Manager (.NET)

The Error Manager API exposes a single endpoint for creating errors, which can be displayed in the Error tab in Relativity.

You can also interact with the Error Manager API through the REST API. See Error Manager service .

## Guidelines for Error Manager API

Review the following guidelines for working with this service.

- Set {versionNumber} to the version of the API, using the format lowercase v and the version number , such as v1 .

## Fundamentals for using Error Manager

### Key concepts or other explanatory information

Review the following information to learn about the methods, classes, and other entities used by the Agent Manager service.

The Relativity.Environment.{versionNumber}.Error namespace contains the IErrorManager interface that exposes the following methods:

- CreateAsync() method - adds a new error log to a database. It returns the Artifact ID of the new error log.

The Relativity.Environment.{versionNumber}.Error.Models namespace contains the following class used by the Error Manager API:

- CreateErrorRequest class - represents information about an error log.

### Guidelines or best practices

- To set up a proxy to interact with the Error Manager API, call the CreateProxy() method on the object returned by the GetServiceManager() method.

- If you plan to use Error Manager API using the IErrorManager interface in your RAP application, remember to add the Relativity.Environment.SDK package to your RAP definition.

- In order to use Error Manager endpoints, you need to import the Relativity.Environment.SDK package. The Error Manager interface is found under the Relativity.Environment.{versionNumber}.Error namespace.

- Every Error log has its own ArtifactID (returned as a response of CreateAsync() method), enabling you to easily find it on the Error tab.

## Create an error log

Create the CreateErrorRequest object and pass it through IErrorManager.CreateAsync() method.

Please remember that all properties except Message are optional. The method returns single integer.

### Create an error log using service manager (recommended)

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
using Relativity.Environment.{versionNumber}.Error;

using Relativity.Environment.{versionNumber}.Error.Models;



Client.SamplesLibrary.Helper.IHelper helper;



// Create a proxy

using (IErrorManager errorManager = helper.GetServicesManager().CreateProxy<IErrorManager>(ExecutionIdentity.User))

{

    var createErrorRequest = new CreateErrorRequest

        {

            Message = "Single line message",

            FullError = "Detailed error message", // exception.ToString()

            Server = System.Environment.MachineName,

            Source = "Name of my agent",

            StepsToReproduce = string.Empty,

            URL = "URL to your custom page or kepler",

            Workspace = new ObjectIdentifier { ArtifactID = -1 },

        };

    int errorLogArtifactID = errorManager.CreateAsync(createErrorRequest);

}
```

You can also use an HttpClient directly if you do not use the Relativity.Environment.SDK nuget package.

### Create an error log using an HTTP client

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
using System.Net.Http;

using Newtonsoft.Json;



private HttpClient GetHttpClient()

{

    HttpClient httpClient = new HttpClient();



    httpClient.BaseAddress = new Uri("https://localhost/");

    httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

    httpClient.DefaultRequestHeaders.Add("Authorization", "Basic " +

        Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes("test@test.com:SomePassword")));



    return httpClient;

}



const string errorManagerEndpoint = "Relativity.Rest/api/relativity-environment/{versionNumber}/workspaces/-1/errors";



var payloadObject = new

{

    createErrorRequest = new

    {

        Message = "Single line message",

        FullError = "Detailed error message", // exception.ToString()

        Server = System.Environment.MachineName,

        Source = "Name of my agent",

        StepsToReproduce = string.Empty,

        URL = "URL to your custom page or kepler",

        Workspace = new

        {

            ArtifactID = -1

        }

    }

};



StringContent payload = new StringContent(JsonConvert.SerializeObject(payloadObject), Encoding.UTF8, "application/json");

HttpResponseMessage response = await GetHttpClient().PostAsync(errorManagerEndpoint, payload);



string responseMessage = await response.Content.ReadAsStringAsync();

int artifactID = Convert.ToInt32(responseMessage);
```

On this page

- Error Manager (.NET)

- Guidelines for Error Manager API

- Fundamentals for using Error Manager

- Key concepts or other explanatory information

- Guidelines or best practices

- Create an error log

- Create an error log using service manager (recommended)

- Create an error log using an HTTP client


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

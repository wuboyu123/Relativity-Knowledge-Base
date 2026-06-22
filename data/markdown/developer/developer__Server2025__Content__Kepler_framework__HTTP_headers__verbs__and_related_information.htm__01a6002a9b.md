---
title: "HTTP headers, verbs, and related information"
url: https://platform.relativity.com/Server2025/Content/Kepler_framework/HTTP_headers__verbs__and_related_information.htm
collection: developer
fetched_at: 2026-06-22T06:23:45+00:00
sha256: 55cedaa03b6944f5276014e1ca19aff1d55b243095dc95d9928ca849728bcbc0
---

HTTP headers, verbs, and related information

# HTTP headers, verbs, and related information

You can customize a Kepler service by overriding the default status codes, using attributes to specify HTTP verbs, and modifying REST responses. The following information illustrates how to implement these and other customizations to your Kepler service.

## X-CSRF-Header

The Kepler framework requires X-CSRF-Header to prevent CSRF attacks. For more information, see Cross-Site Request Forgery (CSRF) on the OWASP website.

You can set the X-CSRF-Header to any value except an empty string. Some HTTP clients and web browsers remove this header if it isn't set. See the following example:

Copy

```text
1
x-CSRF-Header: -
```

In general, the header value is set to a dash (-). Don't leave this header value blank.

To make Kepler service calls, you must include the X-CSRF-header as illustrated in the following samples:

- REST call via .NET code Copy

```text
1
2
HttpClient client = new HTTPClient();

client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");
```

The X-CSRF-Header is automatically applied when you use the .Net proxy to make calls to Kepler services. For more information, see Client .NET proxy .

-

REST call via JavaScript

Copy

```text
1
2
requestOptions = {}

requestOptions["X-CSRF-Header"] = "-"
```

## HTTP verbs

The Kepler framework uses C# attributes to specify the HTTP verb associated with service endpoints. By default, an undecorated service method uses the POST verb. For more information, see Attributes (C#) on the Microsoft website, and HTTP method requests on MDN web docs.

The Kepler framework makes the following verbs available in the Relativity.Kepler.Services namespace:

- GET

- POST

- PUT

- DELETE

- PATCH

The following code sample illustrates how to use of an HTTP verb attribute.

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
using Relativity.Kepler.Services;

// Service contract

namespace Product.Feature.Service

{

    [WebService("MyKeplerService")]

    [ServiceAudience(Audience.Public)]

    public interface IExampleService : IDisposable

    {

        [HttpGet]

        Task<bool> PingAsync();

        [HttpDelete]

        Task DeleteAsync(int artifactID);

    }

}
```

## Status Codes

In a Kepler service, you can control status codes as follows:

- Override the default status code for all responses of an endpoint, such as Default: HTTPStatusCode.OK, 200 . Decorate the method for the service endpoint with a status code using the HttpSuccessStatusCode attribute: Copy

```text
1
2
[HttpSuccessStatusCode(System.Net.HttpStatusCode.Created)]

Task<MyModel> DoAsync();
```

- Throw a Kepler exception that has a FaultCode attribute set with a given status code. For more information, see Exceptions . Copy

```text
1
2
3
4
[FaultCode(HttpStatusCode.Ambiguous)]

public class MyCustomException : ServiceException

{

}
```

- Set status codes on the response of a KeplerStream object. For more information, see Streaming . Copy

```text
1
2
3
4
5
6
7
8
public async Task<IKeplerStream> DownloadStream()

{

    Stream s = new MemoryStream(TEST_BYTES);

    return await Task.FromResult(new KeplerStream(s)

    {

        StatusCode = HttpStatusCode.Accepted

    });

}
```

- Set status codes using a ResponseController object. The response controller is dependency injected into the constructor of the service and it can be used to alter the status code per the request or response. For more information, see ResponseController class . Copy

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
private IResponseController _response;

public TestService(IResponseController responseController)

{

    _response = responseController;

}

public Task ModifyStatusCode()

{

    _response.StatusCode = HttpStatusCode.Accepted;

    return Task.CompletedTask;

}
```

## ResponseController class

You can use the ResponseController class to customize the REST response for a service request. The Kepler framework injects a new ResponseController object into the service constructor each time a call is made to that service. You can then use it to alter the HTTP status code or header information as illustrated in the following samples. For more information, see Client-side interactions with a Kepler service and Status Codes .

- Modified HTTP status code for a response Copy

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
private IResponseController _response;

public TestService(IResponseController responseController)

{

    _response = responseController;

}

public Task ModifyStatusCode()

{

    _response.StatusCode = HttpStatusCode.Accepted;

    return Task.CompletedTask;

}
```

- Modified response header Copy

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
private IResponseController _response;

public TestService(IResponseController responseController)

{

    _response = responseController;

}

public Task ModifyHeader()

{

    _response.Headers.Add("MyTestHeader", "MyValue");

    return Task.CompletedTask;

}
```

## Localization

The Kepler framework handles localization through the ActiveCulture property of the ServiceFactory class class. This property references a CultureInfo object, which the consumer uses to specify a language code in HTTP requests. For more information, see CultureInfo Class on the Microsoft website.

- Set the ActiveCulture property of the ServiceFactory class class. This language is used to populate the Accept-Language header. If it isn't set before creating the client proxy, the Accept-Language header won't be present on out-bound calls. For more information, see Accept-Language on MDN web docs.

- Call the CreateProxy<T> method.

While the Accept-Language header can specify multiple languages, you can only set a single language through the ServiceFactory object. This practice avoids the possibilty of content negotiation by the server and makes the language used by both parties unambiguous.

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
...

ServiceFactorySettings settings = new ServiceFactorySettings(relativityServicesUri, relativityRestUri, credentials);

ServiceFactory factory = new ServiceFactory(settings);

// Specify culture or language.

factory.ActiveCulture = new CultureInfo("fr-FR");

// Create proxy to for the sample Kepler service.

IExampleService proxy = factory.CreateProxy<IExampleService>();

// Outbound calls now sent with header:  Accept-Language: fr-FR
```

## Query Parameters

Query parameters are key-value pairs added to the of a URL to refine a request when sorting, filtering, paging, or performing other actions. For more information, see Query Parameters on MDN web docs.

Use the following guidelines when query parameters with Kepler services:

- Make sure query parameters are optional.

- List default values for the query parameters in the method signature for the endpoint. They must have default values.

- Make sure that the query parameters can be listed in any order in the request.

- Specify query parameters in the route definition similarly to how they are defined in a request. Add a question mark (?) to the end of the route, and then separate the query parameters name by using an ampersand (&).

- List default values for the query parameters in the method signature for the endpoint.

The following code sample illustrates an endpoint on a Kepler service, which has query parameters.

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
// Specify qQuery parameters by adding a question mark (?).

// Specify the default value in the endpoint method.

// http://.../Product.Feature.Service.IExampleModule/MyKeplerService/ResouceType/22

// Returns an array of 10 ResponseDTOs indexed 0-9.

// http://.../Product.Feature.Service.IExampleModule/MyKeplerService/ResouceType/22?firstIndex=20&lastIndex=29

// Returns an array of 10 ResponseDTOs indexed 20-29.

[HttpGet]

[Route("ResouceType/{resourceType}?{firstIndex}&{lastIndex"})]

public Task<ResponseDTO[]> RequestResourceAsync(int resourceType, int firstIndex = 0, int lastIndex = 9)

{

      ...

}
```

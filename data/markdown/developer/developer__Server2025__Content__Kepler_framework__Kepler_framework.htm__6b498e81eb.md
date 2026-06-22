---
title: "Kepler framework"
url: https://platform.relativity.com/Server2025/Content/Kepler_framework/Kepler_framework.htm
collection: developer
fetched_at: 2026-06-22T06:24:04+00:00
sha256: d5f5631b1bc89558e9f1575ffd461b322de2fc65df8c15223e5cd7effb93a8ad
---

Kepler framework

# Kepler framework

The Relativity Kepler framework provides you with the ability to build custom REST EndPoints via a .NET interface. You build a Kepler service using standard .NET contracts, which the Kepler framework uses to build HTTP endpoints. Your Kepler service is then deployed in Relativity as part of a custom application built on the Application Deployment System (ADS). Additionally, the Kepler framework includes a client proxy that you can use when interacting with the services through .NET.

Kepler services offer these advantages:

- Easily hosts endpoints for your application.

- A lightweight framework as compared to packaging DLLs used by custom pages and Web API endpoints.

- Ability to create web and C# endpoints simultaneously.

- Endpoints are automatically protected by Relativity authentication.

## Basic concepts and implementation workflow for a Kepler service

Use the information in this section to become familiar with the basic concepts and implementation workflow for a Kepler service. The outline of this workflow includes both the server-side implementation of a service, and the client-side interactions with it. See the following sections:

- Server-side implementation of Kepler service

- Client-side interactions with a Kepler service

For code samples, see Kepler service structure and components .

### Server-side implementation of Kepler service

The implementation of a Kepler service includes defining the service contract, implementing the required functionality, and organizing the service by module. The following sections provide a high-level description of each step in this workflow:

Service module

A service module is a simple unit of code used to organize your services within the Kepler framework. All Kepler services belong to a single Kepler module. For more information, see Kepler service structure and components .

Use the following design guidelines when implementing the module for your service:

- ServiceModule attribute - decorate your module with the ServiceModule attribute.

- RoutePrefix attribute - decorate your module with the RoutePrefix attribute to provide a RESTful route. For more information, see Routing .

The RoutePrefix attribute has certain naming limitations. Don't use the word Relativity in the string for this attribute. For example, Relativity.MyManager and MyRelativityService are reserved for Relativity use only.

- Namespace usage - make sure that module interfaces and services exist within the same namespace.

- Organize your modules - don't add a new module for each new Kepler service. Instead, consider the type of module where you would expect the service to belong, and then organize your modules accordingly. In general, keep the number of service modules small and expand your modules only as necessary.

- Deploy your service - deploy your Kepler service as part of a custom ADS application. For more information, see Build applications and Deploy Kepler services through ADS .

In general, an ADS application has a single root module, but you may need to divide your services into two or more modules as your application grows.

Service contract

A contract defines the programming interface for your service. This interface is exposed through .NET and it determines the functionality that your service provides.

Implement your contract as a simple .NET interface. Use the following design guidelines when implementing the interface for your service:

- Visual Studio project setup - add your contract to its own Visual Studio project and DLL. Follow this best practice because the contract is shared with other users of your service.

- WebService attribute - decorate your interface with this attribute, which indicates to the Kepler framework that you want this interface hosted as a service. Set the WebService attribute to a user-friendly display name for your service.

- ServiceAudience attribute - decorate your interface with this attribute, which indicates to the Kepler framework who the consumer of this API is. For more information, see ServiceAudience attribute .

For example, possible settings for the audience or consumer include:

- Public - indicates that this API is intended for general use. Document your public APIs and minimize breaking changes to them.

- Private - indicates that this API is specific to your application and isn't intended for general use. A private API may have a very specific use case, such supporting a custom UI.

- IDisposable interface - make sure that your interface inherits from the IDisposable interface. The methods on this interface are used to dispose of client proxies when calling a Kepler service. For more information, see IDisposable Interface on the Microsoft website.

- Task or Task<T> object types - all methods on your interface must return Task or Task<T> object types.

- Async naming conventions - use the Microsoft naming convention for async methods by adding the suffix Async to all the methods on your interface.

Service implementation

After you define your contract, implement the functionality exposed through your interface. Add your implementation class to its own Visual Studio project and DLL. Follow this best practice because the implementation class runs on the server and shouldn't be visible to other users of your service.

### Client-side interactions with a Kepler service

You can interact with a Kepler service by making calls through a .NET client or by submitting HTTP calls similar to those used for other RESTful services. The following sections outline how to make calls to your service:

Kepler .NET client

You can access your Kepler service from any .NET language using the client library provided as part of the Kepler framework. For client code samples, see the documentation for existing services listed on Relativity Server APIs .

The following steps provide a high-level overview describing how to configure a .NET proxy used to call the server:

- Add the following DLL references to your client code:

- DLL containing your service interface

- Relativity.Services.ServiceProxy.dll - To reference this DLL, you can install the Relativity.Kepler package in your Visual Studio project. See NuGet package for the Kepler framework .

- Access Kepler services via a proxy object. This proxy object uses the same interface as your DLL. If you have an IFooManager interface, your client-side service proxy is typed as an IFooManager object.

- To get a client proxy, complete these steps:

- Create a credentials objects used to authenticate to the service. See Authentication for Kepler services .

- Create a proxy factory that points at your server URL. See ServiceFactory class .

- Create a proxy via the factory. See Client .NET proxy .

HTTP clients

You can make calls to a Kepler service using any standard REST or HTTP client, because all Kepler APIs are exposed over the HTTP protocol. By default, Kepler service calls use the POST method, but other HTTP methods are available. For more information, see HTTP headers, verbs, and related information .

Complete these steps to a call to an endpoint:

- Set the required headers for a Kepler service call:

- X-Kepler-Version header - defines the wire protocol version for the Kepler call and defaults to the current standard.

- X-CSRF-header - prevents cross-site request forgery (CSRF) attacks in the browser. You must set this header, but you can assign any value to it. In general, the header value is set to a dash(-). For more information, see X-CSRF-Header .

Don't leave this header value blank. Some browsers remove empty headers.

The Kepler framework returns a 404 status code when the X-CSRF-header isn't submitted. If unexpected 404 status code is returned, make sure that you have included the proper header.

- Content-Type header - indicates the content-type of the request made to the Kepler service. This header must be set to application/json because the Kepler framework only uses JSON payloads.

- Make a call using the URL generated through Kepler framework. It has the following general format: Copy

```text
1
<host>/Relativity.REST/api/{ModuleName}/{InterfaceName}/{MethodName}
```

This basic URL template includes the following tokens for the endpoints generated by the Kepler framework:

- {ModuleName} - the name of the module that the interface for your service is associated with. See Service module .

- {InterfaceName} - the name of the interface or contract exposed for your service. See Service contract .

- {MethodName} - the name of the method on your interface used for the functionality that you want to access.

For detailed route information, see Kepler service structure and components

- Build a JSON payload. When you call a Kepler service, your arguments are sent in the body of a POST call. The arguments are structured as a JSON object that matches the parameters of your service.

For example, you have a service call with the following signature:

Copy

```text
1
Task DoStuffAsync(int a, int b, string name);
```

Your JSON payload would have the following format:

Copy

```text
1
2
3
4
5
{

   "a":42,

   "b":99,

   "name":"Ziggy"

}
```

Use valid JSON with the appropriate data types in the payload. The following formatting rules apply to certain data types:

- Enumeration - represented via their .NET string name instead of an integer value.

- DateTime - represented as a string using ISO8601 format, such as 2009-02-15T00:00:00Z .

- GUID - represented represented as a string with 32 digits separated by hyphens, such as 00000000-0000-0000-0000-000000000000 .

- Empty argument - leave the POST body empty.

- Progress and cancellation - use GUIDs at the JSON layer.

## NuGet package for the Kepler framework

You can add the assemblies for the Kepler framework as a NuGet package to your Visual Studio projects. You can download the Nuget package from https://relativitypackageseastus.jfrog.io/ui/native/server-nuget-remote-cache/Relativity.Server.Kepler.Client.SDK.2.15.6.nupkg . You can also explore the Kepler Client SDK .NET API Reference for the SDK.

## Kepler FAQs

Review these FAQs for answers to general questions related to the Kepler framework.

Which Relativity versions are compatible with custom Kepler services?

RelativityOne and Relativity Server 10.3 and higher support custom Kepler services.

Where do I obtain a Relativity.Kepler.dll?

The Relativity.Kepler.dll is available as a NuGet package that you can install in your Visual Studio project. For more information, see NuGet package for the Kepler framework .

Does auditing automatically occur when a user accesses an endpoint?

No auditing is performed when an endpoint is accessed. RelativityOne environments collect APM metrics, but they aren't currently available to third-party developers. However, you can set the logging level, so that you can view calls to an endpoint. For more information, see Logging and Log from a Relativity application .

What type of authentication should a Kepler service use?

A Kepler service must use bearer token authentication. The bearer token is obtained through an OAuth2 client. For more information, see Authentication for Kepler services .

How do I determine if my service is being hosted? What the status of a Kepler service is?

To determine if your service is hosted, check its status by making a call to the following endpoint. For more information about the URI format, see Routing

Copy

```text
1
<host>/Relativity.REST/api/{FullyQualifiedModuleName}/{UserFriendlyInterfaceName}/GetKeplerStatusAsync
```

If the service is hosted, this call returns the following response:

Copy

```text
1
2
3
{

   "Status":"OK"

}
```

## Version History

### Relativity.Kepler.Client.SDK

v5000.0.2

##### Release Notes

- Initial version for Server 2024 release

##### Supported Relativity Version Range

Lowest Version Highest Version

Server 2024 Server 2025

v2.15.6

##### Release Notes

- Initial version for Server 2023 release.

##### Supported Relativity Version Range

Lowest Version Highest Version

Server 2023 Server 2024

### Relativity.Kepler.SDK

v5000.0.2

##### Release Notes

- Initial version for Server 2024 release

##### Supported Relativity Version Range

Lowest Version Highest Version

Server 2024 Server 2025

v2.15.6

##### Release Notes

- Initial version for Server 2023 release.

##### Supported Relativity Version Range

Lowest Version Highest Version

Server 2023 Server 2024

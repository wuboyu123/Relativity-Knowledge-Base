---
title: "Troubleshooting Kepler services"
url: https://platform.relativity.com/Server2025/Content/Kepler_framework/Troubleshooting_Kepler_services.htm
collection: developer
fetched_at: 2026-06-22T06:31:15+00:00
sha256: a49731bd4da0accc945d1449f6cc38dd624b2c857441cf205742865bbb221992
---

Troubleshooting Kepler services Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Troubleshooting Kepler services

Use the following information troubleshoot your custom Kepler services.

## Assembly doesn't contain service module

You must bundle a given set of Kepler services in a module before you add them to an ADS application in Relativity. If the services aren't added to a module, you receive the following error listing the services:

Copy

```text
1
Assembly does not contain service module.
```

This error also occurs when the ServiceModule attribute hasn't been added to the service module class. For more information, see Modules .

## Deleted applications

An application continues to be hosted in a Relativity environment even after you deleted it from the both Application Library and any workspaces where it was installed.

## GET endpoint fails

If you implement an endpoint with HttpGet attribute but don't also use a Route attribute, it won't function properly. The Kepler framework automatically adds the FromBody attribute on all parameters that aren't route parameters. For more information, see Routing .

## Invalid RoutePrefix attribute causes 404 error

If you set your RoutePrefix attribute with an empty string(""), a 404 status code is returned indicating an error:

Copy

```text
1
[RoutePrefix("", VersioningStrategy.None)]
```

For more information, see Routing .

## Invalid WebService attribute causes 500 error

If you set your WebService attribute an empty string(""), a 500 status code is returned indicating an error:

Copy

```text
1
[WebService("")]
```

For more information, see Routing .

## Missing or no endpoints on a service

Relativity won't host a Kepler service with the following endpoint implementation issues. It also returns a 404 status code when you attempt to the call the service with these issues:

- Missing endpoints

- No endpoints

- Endpoints without the public qualifier in the service implementation

If you implement a service that isn't public, and it has any of the issues listed above, the EventViewer contains the following error message:

Copy

```text
1
Error: Value cannot be null. Parameter name: element
```

## Multiple modules error

If your ADS application has several modules within the same namespace used to bundle a set of Kepler services, you won't be able to import it into Relativity. The following error appears listing the affected services:

Copy

```text
1
Assembly contains more than one service module for namepsace My.Random.Kepler: MyServiceModule, ServiceModule
```

## Multiple service implementations error

You can only import a single implementation of a specific service to Relativity as either a single standalone RAP file, or a resource file associated with an ADS application. If you attempt to import multiple implementations, the following error message appears listing the affected assemblies:

Copy

```text
1
2
Cannot have more than one service implementation for a given service. List of assemblies containing implementations of the service

IRandomService: My.Random.Kepler.Service.Implementation.One, My.Random.Kepler.Service.Implementation.Two
```

## Namespace doesn't exist error message

Don't create a service in the Services namespace. When a service is loaded that has a module and interface implemented in Services.Interfaces namespace, the following error message appears:

Copy

```text
1
2
(555) Kepler bootstrapping failed: The type or namespace name 'Interfaces' does not exist in the namespace

'Relativity.Kepler.Services' (are you missing an assembly reference?)
```

## ServiceAudience error

You must decorate your service interface with the ServiceAudience attribute. If this attribute is missing, the following error appears:

Copy

```text
1
(555) One or more Kepler services has errors: ITestService: Service Audience is not specified
```

For more information, see ServiceAudience attribute .

On this page

- Troubleshooting Kepler services

- Assembly doesn't contain service module

- Deleted applications

- GET endpoint fails

- Invalid RoutePrefix attribute causes 404 error

- Invalid WebService attribute causes 500 error

- Missing or no endpoints on a service

- Multiple modules error

- Multiple service implementations error

- Namespace doesn't exist error message

- ServiceAudience error


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

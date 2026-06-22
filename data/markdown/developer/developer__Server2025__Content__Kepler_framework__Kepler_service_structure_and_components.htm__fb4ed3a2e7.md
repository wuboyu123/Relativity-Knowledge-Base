---
title: "Kepler service structure and components"
url: https://platform.relativity.com/Server2025/Content/Kepler_framework/Kepler_service_structure_and_components.htm
collection: developer
fetched_at: 2026-06-22T06:29:09+00:00
sha256: 89b856a21ad0a7a6461f741c25539464b623fcabd2c0d4575c1db1a00cc3b7dd
---

Kepler service structure and components

# Kepler service structure and components

Use the following information to learn about how the Kepler framework uses modules, routing, exceptions, and other key components required to build custom services. It also includes information about how to version your services and deprecate outdated ones.

## Modules

A Kepler module is a required interface that denotes a logical collection of related services. The Kepler framework uses the module to detect a service in your code.

A service module automatically includes all of the services that are defined in the same root namespace or deeper. It works by using convention over configuration , which means that services aren't directly assigned to a module. When the Kepler framework is initialized, it scans all of the classes in your DLL to detect the modules and services that you have defined in your code.

Use the following guidelines to implement your module:

- Decorate the module with the ServiceModule attribute. Copy

```text
1
2
3
4
5
6
7
namespace Product.Feature.Service

{

    [ServiceModule("MyKeplerModule")]

    public interface IExampleModule

    {

    }

}
```

- Make sure that module interfaces and services exist within the same namespace. For more information, see Versioning for Kepler APIs . Copy

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
/Project

    /Feature_1

        /IExampleService1.cs

        /IExampleModule1.cs

    /Feature_2

        /IExampleModule2.cs

        /Service_2A

            /IExampleService2_A.cs

        /Service_2B

            /IExampleService2_B.cs
```

- Decorate the module with the RoutePrefix attribute to provide a RESTful route. For more information, see Routing . Copy

```text
1
2
3
4
5
6
7
8
namespace Product.Feature.Service

{

    [ServiceModule("MyKeplerModule")]

    [RoutePrefix("MyKeplerService.RoutePrefix")]

    public interface IExampleModule

    {

    }

}
```

## Routing

The Kepler framework supports RESTful routing, which uses the RoutePrefix attribute.

The RoutePrefix attribute has certain naming limitations. Don't use the word Relativity in the string for this attribute. For example, Relativity.MyManager and MyRelativityService are reserved for Relativity use only.

The RoutePrefix attribute is used at the following levels:

- Module - this sample illustrates how the RoutePrefix attribute decorates a service module. Copy

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
// Service module

namespace Product.Feature.Service

{

    [ServiceModule("MyKeplerModule")]

    [RoutePrefix("Examples"]

    public interface IExampleModule

    {

        // Empty

    }

}
```

- Service - the RoutePrefix attribute decorates the interface or contract for the service. See the code sample under endpoint.

- Endpoint - this sample illustrates how the RoutePrefix attribute decorates the interface and the methods on it. Copy

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
// Service contract

namespace Product.Feature.Service

{

    [WebService("MyKeplerService")]

    [ServiceAudience(Audience.Public)]

    [RoutePrefix("Service")]

    public interface IExampleService : IDisposable

    {

        [Route("Ping")]

        Task<bool> PingAsync();

        [Route("Data/Request")]

        Task<ResponseDTO > DataRequestAsync(RequestDTO requestObj);

    }

}
```

For RESTful routing, the Kepler framework constructs the following endpoints for this service:

- Endpoint for the PingAsync() method Copy

```text
1
/Examples/Service/Ping
```

- Endpoint for the DataRequestAsync() method Copy

```text
1
2

/Examples/Service/Data/Request
```

## ServiceAudience attribute

To indicate the consumer of a Kepler service, decorate your implementation with the ServiceAudience attribute. Set this attribute using an Audience enum as listed below:

Copy

```text
1
2
3
4
public enum Audience{

    Private,

    Public

};
```

These enums are defined as follows:

- Private - the service is intended for internal consumption.

- Public - the service is intended for public consumption.

## Interfaces

You define your service contract as an interface exposed through .NET. It determines the functionality that your service exposes.

View general guidelines for implementing an inteface

To implement your contract as a simple .NET interface, use the following design guidelines when implementing the interface for your service:

- Visual Studio project setup - add your contract to its own Visual Studio project and DLL. Follow this best practice because the contract is shared with other users of your service.

- WebService attribute - decorate your interface with this attribute, which indicates to the Kepler framework that you want this interface hosted as a service. Set the WebService attribute to a user-friendly display name for your service.

- ServiceAudience attribute - decorate your interface with this attribute, which indicates to the Kepler framework who the consumer of this API is. For more information, see ServiceAudience attribute .

For example, possible settings for the audience or consumer include:

- Public - indicates that this API is intended for general use. Document your public APIs and minimize breaking changes to them.

- Private - indicates that this API is specific to your application and isn't intended for general use. A private API may have a very specific use case, such supporting a custom UI.

- IDisposable interface - make sure that your interface inherits from the IDisposable interface. The methods on this interface are used to dispose of client proxies when calling a Kepler service. For more information, see IDisposable Interface on the Microsoft website.

- Task or Task<T> object types - all methods on your interface must return Task or Task<T> object types.

- Async naming conventions - use the Microsoft naming convention for async methods by adding the suffix Async to all the methods on your interface.

The following code snippet illustrates how the service contract must be decorated with the WebService and ServiceAudience attributes. It must also inherit from the IDisposable interface.

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
// Service contract

namespace Product.Feature.V1.Service

{

    [WebService("MyKeplerService")]

    [ServiceAudience(Audience.Public)]

    public interface IExampleService : IDisposable

    {

        Task<bool>; PingAsync();

        Task<ResponseDTO>; DataRequestAsync(RequestDTO requestObj);

    }

}
```

You must implement all methods on your interface so that they return Task or Task<T> object types as illustrated in the following code sample. By default, these sample methods define a POST method, but you have the option to use other HTTP methods by adding a verb attribute. For more information, see HTTP verbs .

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
// Service

namespace Product.Feature.V1.Service

{

    public class ExampleService : IExampleService

    {

        public Task<bool> PingAsync()

        {

            return Task.FromResult(true);

        }

        public Task<ResponseDTO> DataRequestAsync(RequestDTO requestObj)

        {

            var response = new ResponseDTO();

            response.Data = "ABC";

            response.ID = 42;

            return Task.FromResult(response);

        }

    }

}
```

## Exceptions

The Kepler framework has defined exceptions with HTTP status code attributes, which you can use in your server implementation.

- In .NET, you can use a catch block of an exception type, which contains statements needed to handle that exception type.

- In REST, you can find the status code for an exception in an HTTP response.

See the following list of exceptions:

Status code Exception type* Description

500 ServiceException The base class for any exception from a service. Inherit from this class and override the status code.

400 ServiceSerializationException An exception thrown for a serialization or deserialization error.

400 ValidationException An exception that occurs during data validation.

403 NotAuthorizedException An exception that occurs during scope validation.

404 NotFoundException An exception that occurs when a resource isn't found.

404 ServiceNotFoundException An exception raised when the service endpoint can't be found.

409 DataConcurrencyException An exception indicating that the request can't be completed because of a conflict on the server.

409 ConflictException An exception indicating that the request can't be completed because of a conflict on the server.

*The exceptions listed in this table reside in the Relativity.Services.Exceptions namespace.

The following code sample illustrates how to throw an exception:

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
public class ExampleService : IExampleService

{

    public Task<ResponseDTO> DataRequestAsync(RequestDTO dto)

    {

        if (dto.ID >= 15 && dto.ID <= 20)

        {

            throw new ValidationException("ID is deprecated.");

        }

        // Additional code

    }

}
```

Exceptions can differ in namespace, such as client versus server contracts. Set the ExceptionIdentifier attribute with a GUID used to link client and server exceptions. See the following sample code:

Copy

```text
1
2
3
4
5
[ExceptionIdentifier("4E246FDB-E8D2-4379-AE09-008EB4B304C4")]

[FaultCode(HttpStatusCode.Ambiguous)]

public class MyCustomException : ServiceException

{

}
```

## Versioning for Kepler APIs

The Kepler framework supports the creation of versioned APIs. It uses namespace versioning, which requires services to be organized by version within the namespace starting at the module. As a best practice, version your APIs.

Use the following guidelines to version your APIs:

- Enable API versioning - add the VersioningStrategy enum to the RoutePrefix attribute on the service module. See the following sample code: Copy

```text
1
2
3
4
5
6
7
8
namespace Product.Feature.Service

{

    [ServiceModule("MyKeplerModule")]

    [RoutePrefix("ModulePrefix", VersioningStrategy.Namespace)]

    public interface IExampleModule

    {

    }

}
```

- Organize services - organize services by version within the namespace starting at the module. See the following sample organization: Copy

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
/Project

    /Feature

        /v1

            /Models

                /RequestDTO.cs

                /ResponseDTO.cs

            /Exceptions

            /Helpers

            /Services

                /IExampleService.cs

                /ExampleService.cs

        /v2

            /Models

                /RequestDTO.cs

                /ResponseDTO.cs

            /Exceptions

            /Helpers

            /Services

                /IExampleService.cs

                /ExampleService.cs

        /MyModule.cs
```

### Example of a versioned service

The Kepler framework appends the version number to the end of the module prefix. See the following format for a versioned service route:

Copy

```text
1
/ModulePrefix/v[major_version_number_here]/Service/Endpoint
```

Kepler service - version 1

The following code illustrates the implementation for the first version of a Kepler service:

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
namespace Project.Feature.v1.Services

{

    [WebService("MyKeplerService")]

    [RoutePrefix("MyService")]

    [ServiceAudience(Audience.Public)]

    public interface IExampleService : IDisposable

    {

        [HttpPost]

        Task<Project.Feature.v1.Models.ResponseDTO> DataRequestAsync(Project.Feature.v1.Models.RequestDTO request);

    }

}
```

The versioned route for this service has the following format:

Copy

```text
1
/ModulePrefix/v1/MyService/DataRequestAsync
```

Kepler service - version 2

The following code illustrates the implementation for the second version of a Kepler service:

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
namespace Project.Feature.v2.Services

{

    [WebService("MyKeplerService")]

    [RoutePrefix("MyService")]

    [ServiceAudience(Audience.Public)]

    public interface IExampleService : IDisposable

    {

        [HttpPost]

        Task<Project.Feature.v2.Models.ResponseDTO> DataRequestAsync(Project.Feature.v2.Models.RequestDTO request);

    }

}
```

The versioned route for this service has the following format:

Copy

```text
1
/ModulePrefix/v2/MyService/DataRequestAsync
```

## Obsolete attribute

You can decorate your implementation of a Kepler API with the ObsoleteAttribute to indicate that it's obsolete or deprecated. For more information, see ObsoleteAttribute Class on the Microsoft website.

We strongly recommend using the Obsolete attribute when you release a new version of your API. Add the attribute to the previous version of the API version to indicate that it's deprecated. For more information, see Versioning for Kepler APIs

### Deprecate a service

To deprecate a service, decorate the interface with the Obsolete attribute and add an explanatory message. See the following code sample:

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
namespace Product.Feature.Service

{

    [WebService("MyKeplerService")]

    [ServiceAudience(Audience.Public)]

    [Obsolete("ExampleService has been deprecated. Please use MoreExampleServices.")]

    public interface IExampleService : IDisposable

    {

        Task<bool> PingAsync();

        Task<ResponseDTO> DataRequestAsync(RequestDTO requestObj);

    }

}
```

### Deprecate an endpoint

To deprecate an endpoint, decorate the specific method with the Obsolete attribute and add an explanatory message. See the following code sample:

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
namespace Product.Feature.Service

{

    [WebService("MyKeplerService")]

    [ServiceAudience(Audience.Public)]

    public interface IExampleService : IDisposable

    {

        Task<bool> PingAsync();

        [Obsolete("DataRequestAsync has been deprecated. Please use LoadDataAsync.")]

        Task<ResponseDTO> DataRequestAsync(RequestDTO requestObj);

        Task<ResponseDTO> LoadDataAsync(RequestDTO requestObj);

    }

}
```

A deprecate method continues to execute. However, the HTTP response contains a header stating that the method is obsolete. See the following examples:

- Deprecated endpoint with default message

The following method is decorated with the Obsolete attribute only:

Copy

```text
1
2
[Obsolete]

Task<ResponseDTO> DataRequestAsync(RequestDTO requestObj);
```

The HTTP response displays the default message:

Copy

```text
1
Warning:299 localhost DataRequestAsync is obsolete
```

- Deprecated endpoint with custom message

The following method is decorated with the Obsolete attribute and a custom message:

Copy

```text
1
2
[Obsolete("DataRequestAsync is deprecated and will be removed in the 3.0 release of this API. Please use the DataRequestAsync method in 2.0 instead.")]

Task<ResponseDTO> DataRequestAsync(RequestDTO requestObj);
```

The HTTP response displays the custom message:

Copy

```text
1
Warning:299 localhost DataRequestAsync is deprecated and will be removed in the 3.0 release of this API. Please use the DataRequestAsync method in 2.0 instead.
```

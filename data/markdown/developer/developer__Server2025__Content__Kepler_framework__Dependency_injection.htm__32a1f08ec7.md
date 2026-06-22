---
title: "Dependency Injection"
url: https://platform.relativity.com/Server2025/Content/Kepler_framework/Dependency_injection.htm
collection: developer
fetched_at: 2026-06-22T06:31:12+00:00
sha256: 8f6af7f32409f2f0ebf40b9fe1a1a29bd1c12c2d4201f21222193d136d4fc4ff
---

Dependency Injection Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Dependency Injection

The Kepler framework supports dependency injection, which you can use to facilitate testing the classes implemented for your custom services. It is integrated with the Castle Windsor framework to provide this functionality. The Kepler framework follows the common practice of using a constructor for the injection of a dependent object. For general information, see Dependency injection on Wikipedia, and Castle Windsor on GitHub.

## Dependency injection in the Kepler

In the Kepler framework, the dependency injection occurs through your service controller. Your dependency objects must be registered with the injection framework, so they can be supplied to your controllers. Use the following steps to register your dependent objects through Windsor installer:

- Create a class that implements the IWindsorInstaller interface. This class is now a Windsor installer. For more information, see Windsor installers on GitHub.

- Perform the registration in an Install method on this class. For more information, see Registering components one-by-one on GitHub.

The Kepler framework installs all Windsor installers in your service assemblies to the dependency injection framework. When an inbound request instantiates a service controller, the dependency injection framework works as follows:

- It instantiates any objects specified as an input parameters to the constructor for the controller.

- It injects these parameters into the controller for use during a service call.

The following code samples illustrate the implementation of the ExampleService that has a dependency on the IService interface. The helper is registered in a Windsor installer and injected into the constructor of ExampleService.

- Windsor installer class Copy

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

using Castle.MicroKernel.Registration;

// The iInstaller class must be public.

public class MyWindsorInstaller : IWindsorInstaller

{

    // Installers must have public default constructors.

    // IWindsorInstaller contains only one method.

    public void Install(IWindsorContainer container, IConfigurationStore store)

    {

        // Register an implementation for a dependency's interface.

        container.Register(

            Component.For<IService>()

                .ImplementedBy<MyService>()

                    .LifeStyle.Transient;

                    // In most cases, use LifeStyle.Transient.

    }

}
```

- Dependency interface Copy

```text
1
2
3
4
5
// Dependency interface

public interface IService

{

    void GetHelp();

}
```

- Dependency implementation Copy

```text
1
2
3
4
5
// Dependency implementation

public class MyService : IService

{

    GetHelp() { // do something }

}
```

- Dependent service Copy

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
// Dependent service

public class ExampleService : IExampleService

{

    private readonly IService Service;

    // The dependency injection framework sees the dependency on IService

    // and injects an instance of MyService.

    public ExampleService(IService service)

    {

        Service = service;

    }

}
```

## Assemblies without a Kepler service

In certain use cases, you may want to run the Windsor installer on an assembly that doesn't contain a Kepler service. You must add the following attribute to your assembly for the Kepler framework to detect it:

Copy

```text
1
[assembly: Relativity.Kepler.Services.KeplerServiceDependency]
```

When this attribute is missing, the Kepler framework doesn't detect your assembly and won't run the Windsor installer for it.

## Dependency injection through ADS

The dependency injection framework provides Kepler services hosted in Relativity with several utility objects. Add any of the following interfaces to the constructor of your service controller to obtain an implementation of that interface:

- ILog - in Relativity Server, you can write messages, warnings, and errors to SQL in the eddsdbo.RelativityLogs table.

- IHelper - use the helper to get an instance of the ADS IHelper, which provides several objects that simplify programming against Relativity. See the following examples:

- Get an IDBContext object to interact with SQL via the GetDBContext() method. See Obtain a database context .

-

Get an ISecretStore object via the GetSecretStore() method, which is used as a client to interact with the Secret Store for Relativity. See Work with the Secret Store .

For more information, see Relativity API Helpers .

The following code sample illustrates how to access utility objects:

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
private readonly ILog _logger;

private readonly IHelper _helper;

//use the DI helper

public ExampleService(ILog logger, IHelper helper)

{

    _logger = logger.ForContext<ExampleService>();

    _helper = helper;

}
```

On this page

- Dependency Injection

- Dependency injection in the Kepler

- Assemblies without a Kepler service

- Dependency injection through ADS


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

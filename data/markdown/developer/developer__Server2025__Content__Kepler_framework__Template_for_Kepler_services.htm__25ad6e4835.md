---
title: "Template for Kepler services"
url: https://platform.relativity.com/Server2025/Content/Kepler_framework/Template_for_Kepler_services.htm
collection: developer
fetched_at: 2026-06-22T06:31:06+00:00
sha256: b07754feb01cadfac83f69854459d861b67b73d201e164a2f05ef35037196662
---

Template for Kepler services

# Template for Kepler services

To jump start your Kepler service implementation, use the Visual Studio template for building services. It provides the required files for building a service, so you can focus on implementing the custom functionality that your users need. The template includes the following features designed to facilitate your implementation tasks:

- Includes required files for building a service.

- Includes implementation for a simple service that you can compile and deploy to Relativity.

## Before you begin

Complete the following tasks to before you begin implementing a custom Kepler service:

- Obtain access to an instance of Relativity used for development purposes.

- Verify that you have Visual Studio 2017 or higher as required by the Relativity Kepler Project Template.

- Set up your development environment and enable Developer mode in Relativity.

- Install a tool to submit REST requests to an API. This tutorial uses the Postman app. However, you can use any REST tool or browser.

## Install the Relativity Kepler Project Template

Download and install the Relativity Templates from Visual Studio Marketplace. For instructions, see Install the Relativity templates .

## Create a new Kepler service solution

When you create a new solution with the Relativity Kepler Project Template, it automatically includes a simple service that you can run. You can then add your new custom service to the solution that you created from the template.

To create a new Kepler service solution, use the following steps:

- Open Visual Studio 2017.

- Click File > New > Project to display the new Project dialog.

- In the left-hand pane, click Installed > Visual C# > Relativity > Kepler .

- In the center pane, locate Relativity Kepler Project Template .

- Enter the name of your project and browse for a location.

- Click OK to create your new project from the template.

- In the template wizard dialog, enter values for the following fields:

- Service Module - enter the name that you want to use for the service module, which is use to organize your services. For more information, see Modules .

- Service Name - enter a name for your service.

- Verify that the NuGet package for Relativity.Kepler was installed with the template. If it wasn't installed, complete step 8. Otherwise, continue with step 9.

- To open the NuGet Package Manager, click Tools > NuGet Package Manager > Manage NuGet Packages for Solution . Select and install the NuGet package for Relativity.Kepler .

- Compile the project to generate the assemblies for the sample service that it includes. See the following for more information about the structure of Kepler services:

- Kepler framework

- Modules

- Routing

- Interfaces

- HTTP headers, verbs, and related information

- Deploy the assemblies (.dll files) containing the sample Kepler service to Relativity. For more information, see Lesson 3 - Create a RESTful API or Deploy Kepler services through ADS .

## Send requests to a service

You can optionally send requests to a service through Postman, which is a tool that supports call to RESTful endpoints.

To get started with Postman, complete these steps:

- Obtain access to a Relativity environment. You need a username and password to make calls to your environment.

- Install Postman . For more information, see the Postman web site .

- Select POST for the HTTP method.

- Enter the URL with the domain for your Relativity environment and the endpoint information.

- Review sample routes in the code comments generated when you created the project. In the Solution Explorer, navigate to the file added to the RouteBase folder. For example, if you named entered MyService for the service name in the template wizard, these comments would be added to RouteBase >IMyService.cs.

- The structure for the URL depends on how you have implemented routing for your service, such as whether you have used a route prefix or versioning. For more information, see Routing and Versioning for Kepler APIs .

- In the Authorization tab, set the Type to Basic Auth , enter your Relativity credentials, and click Update Request .

- Set the X-CSRF-Header to with any value except an empty string. In general, the header value is set to a dash(-). Don't leave this header value blank. For more information, see X-CSRF-Header .

- Set any required fields for the request.

- Click Send to make a request.

## Uninstall the Relativity Kepler Project Template

To uninstall the template, use the following steps:

- In Visual Studio, click Tools > Extensions and Updates .

- Under the Installed section, search on Relativity Templates .

- Click Uninstall .

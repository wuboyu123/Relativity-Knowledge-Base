---
title: "Relativity Integration Points"
url: https://platform.relativity.com/Server2025/Content/Relativity_Integration_Points/Get_started_with_integration_points.htm
collection: developer
fetched_at: 2026-06-22T06:23:55+00:00
sha256: 377a9d85958d53a3d0f9eb58d0b2219ad9cbf8e2fc26b92f0425862db2f58231
---

Relativity Integration Points Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Relativity Integration Points

Relativity Integration Points provides a robust framework that you can use to develop custom providers for importing data to Relativity Dynamic Objects (RDOs) or other types of objects. It supports the integration of custom providers that ingest data in XML, JSON, SQL databases, or other formats. This framework leverages the standard features available in the Application Deployment System (ADS), such as custom pages and event handlers. Because you use the ADS to build your custom integration points, you can easily deploy them to multiple workspaces and Relativity environments. You can also manipulate this data just like any other content because it lives in Relativity object types. Additionally, Relativity Integration Points includes a fully implemented UI that you extend by adding your own custom page, which contains only those fields requiring user input for your provider. For information about administrative tasks, see Relativity Integration Points on the user documentation site.

See these related pages:

- Best practices for integration point development

- Build your first integration point

- Build an advanced integration point

- Troubleshoot integration points

## Understand the Relativity Integration Points framework

The Relativity Integration Points framework streamlines the process of creating custom functionality for importing data. This framework lets you focus on how your code interacts with a data source and on the usability of your client interface. The following diagram illustrates the workflow for creating an integration point.

This diagram includes the following steps:

- The user clicks the New Integration Point button to start the Create Integration Point wizard.

- The user selects a source provider and destination RDO and optionally schedules the import.

- The Integration Points framework invokes the custom page that you developed for your custom source provider. The custom page displays the required settings for the page, and the users enter input values as necessary.

- The user maps provider source fields to destination RDO fields and clicks Save.

The Integration Points framework provides these key features to facilitate this workflow and your development process:

- Adds an Integration Points tab in the workspace where you deploy your custom Integration Points application. When users click this tab, they see a list of integration points created in the workspace.

- Includes a wizard that users run to create a new integration point in a workspace. This wizard automatically provides these and other features:

- Adds your new Integration Points provider to the list of available source providers.

- Displays your custom page so that users can enter required settings. See the following sample custom page:

- Offers a user-friendly interface for mapping fields in your custom data source to those in a Relativity workspace.

- Displays the settings that you selected when creating the integration point on the details view.

- Provides optional scheduling features that users can set when navigating through the wizard.

## Basic concepts for integration point development

Integration Points provides a framework for hosting your custom application, which contains or utilizes the following key components:

- Provider – includes the custom backend functionality that you develop to ingest a specific type of data, such as XML or JSON. Your provider pulls data from your data source and passes it to Relativity Integration Points, which creates and updates objects in Relativity with this content.

- Custom page – used to expose fields that require input from users, such as a file location or authentication method. When users select your source provider, your custom page appears in the Connect to Source layout in the Integration Points wizard. You reference the Relativity.CustomPages.dll as you develop the client interface, which offers this functionality available through the ADS.

- Relativity application – used as the framework for building custom source providers. You build your custom source provider as a Relativity application, supported by the ADS. This framework provides you with support for custom page, event handler, and agent development. It also ensures the portability of your source provider, so that you can deploy it to multiple workspaces and environments.

- Integration Point agent – used to batch data from your source provider and to call the Import API, which can programmatically add data to RDOs.

- Import API – used as the underlying functionality for Relativity Integration Points.

- Event handlers – added to source providers for use when registering them with Relativity and uninstalling them from workspaces. The Relativity Integration Points API extends certain event handler classes available through the ADS for working with source providers.

### Workflow for importing data

The following workflow illustrates how the Integration Points framework uses an agent for importing data:

This diagram includes the following steps:

- Your custom source provider ingests a specific type of data, such as XML, JSON, or others. It uses the settings selected by the user on the your custom page. The Create Integration Point wizard invokes your custom page. See the Understand the Relativity Integration Points framework section in this topic for more information.

- The Integration Point agent batches data from your source provider and calls the Import API.

- The Relativity Import API programmatically adds your data to Relativity dynamic objects (RDOs).

- In Relativity, you use the RDOs to access the imported data.

## Relativity Integration Points API

The Relativity Integration Points API includes the following namespaces with classes and interfaces that you can use to interact with components of this framework:

- Relativity.IntegrationPoints.Contracts – includes classes and interfaces for building the data source provider and deploying the provider in its own application domain.

- Relativity.IntegrationPoints.Services.Interfaces.Private – includes interfaces that your provider class must implement. The methods on these interfaces control the batching and importing of unique identifiers for data entries, and batching and importing the actual data.

- Relativity.IntegrationPoints.SourceProviderInstaller – includes classes and delegates for registering the provider with Relativity and uninstalling the provider from a workspace. When you develop event handlers for these purposes, you extend the IntegrationPointSourceProviderInstaller and IntegrationPointSourceProviderUninstaller classes.

## Integration Points SDK files

You can download the Relativity Server Integration Points SDK from Relativity.IntegrationPoints.SDK .

After downloading the Integration Points SDK, extract its contents to a folder on your local machine. It contains the following folders:

- Web – includes JavaScript files that you must reference when developing your custom page:

- frame-messaging.js – we developed this proprietary code to communicate between iFrames used in the custom pages of your application and the Integration Points framework.

- jquery-postMessage.js and jquery-3.6.0.js – standard jQuery files are provided as part of the Integration Points SDK for your convenience.

- Provider – includes the following assemblies:

- Relativity.IntegrationPoints.Contracts.dll and Relativity.IntegrationPoints.SourceProviderInstaller.dll – reference these .dll files in your Visual Studio project when developing your code for importing data. For more information, see Set up your Visual Studio solution .

- Remaining assemblies - add them as resource files to Relativity. You also need to add them if you want to upgrade a source provider built on an earlier Relativity version. For more information, see Upload required .dll files and Upgrade integration points for use in Relativity 9.4 and above .

- Examples - includes the sample code for the following source providers:

- My First Provider application illustrates how to load data from an XML file into RDOs. See Build your first integration point .

- The JSON Loader application demonstrates how to load JSON into RDOs. See Build an advanced integration point .

For information about adding these files to a project, see Best practices for integration point development and Set up your Visual Studio solution .

On this page

- Relativity Integration Points

- Understand the Relativity Integration Points framework

- Basic concepts for integration point development

- Workflow for importing data

- Relativity Integration Points API

- Integration Points SDK files


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

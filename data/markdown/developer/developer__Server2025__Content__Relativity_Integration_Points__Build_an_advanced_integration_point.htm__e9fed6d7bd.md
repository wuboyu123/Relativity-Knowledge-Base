---
title: "Build an advanced integration point"
url: https://platform.relativity.com/Server2025/Content/Relativity_Integration_Points/Build_an_advanced_integration_point.htm
collection: developer
fetched_at: 2026-06-22T06:30:11+00:00
sha256: c9fd1383adf527c27e7fac6627fb52f188da34fd30c57301d67f2361f98f7cc0
---

Build an advanced integration point Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Build an advanced integration point

The JSON Loader is a sample application that demonstrates how you can load data formatted using JSON into Relativity Dynamic Objects (RDOs). The source code for this integration point illustrates how to perform the following tasks:

- Implement a provider that ingests JSON-formatted data.

- Create a custom page for the client.

- Use dependency injection in your unit tests for your custom code.

## View the source code

You can view the source code for the JSON Loader application to learn how to develop custom integration points for different data formats. Download and extract the Relativity Integration Points SDK. Navigate to the \Integration Points SDK\Examples\JsonLoader folder. Open the JsonLoader.sln file in Visual Studio 2015.

If you want to build the solution, you must add the .dll files for event handlers, custom pages, and the Integration Points framework. See Build the JSON Loader in Visual Studio .

## Build the JSON Loader in Visual Studio

Before you can build the JSON Loader solution, you must add the required assemblies to it. They include .dll files for event handlers, custom pages, and the Integration Points framework.

Use the following steps to add assemblies to your solution:

- Download and run the Relativity SDK installer. For more information, see Download the SDKs .

- Download and unzip the Integration Points SDK. For more information, see Integration Points SDK files .

- Navigate to the \Integration Points SDK\Examples\JsonLoader folder.

- Open the JsonLoader.sln file in Visual Studio 2015.

You must use Visual Studio 2015 to develop integration points for Relativity 9.4 or above.

- To add the .dll file for custom pages, right-click References under the JsonWeb project. Click Add Reference . Navigate to the folder where you installed the Relativity SDK, and select the Relativity.CustomPages.dll file.

- To add the .dll file for event handlers, right-click References under the JsonLoader project, and then click Add Reference on the menu. Navigate to the folder where you installed the Relativity SDK, and select the kCura.EventHandler.dll file. Click Add .

- Navigate to the folder where you extracted the Integration Points SDK. Repeat the previous step to select the .dll files called Relativity.IntegrationPoints.Contracts.dll , Relativity.IntegrationPoints.SourceProviderInstaller.dll , and Relativity.IntegrationPoints.Services.Interfaces.Private . Click Add .

- On the Visual Studio menu, click Build > Build Solution .

On this page

- Build an advanced integration point

- View the source code

- Build the JSON Loader in Visual Studio


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

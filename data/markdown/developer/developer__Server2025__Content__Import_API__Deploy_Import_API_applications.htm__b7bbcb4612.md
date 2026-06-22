---
title: "Deploy Import API applications"
url: https://platform.relativity.com/Server2025/Content/Import_API/Deploy_Import_API_applications.htm
collection: developer
fetched_at: 2026-06-22T06:30:04+00:00
sha256: 26d88339fd6acb61185f9a22cb110a43e46dd54984130f7218a01f4ee47c90db
---

Deploy Import API applications Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Deploy Import API applications

The Application Deployment System (ADS) provides the functionality used to deploy your custom Import API applications. It automatically deploys a subset of the .NET assemblies files used by an application, such as OAuth2, logging, and telemetry. At this time, you do need to manually post specific assemblies but enhancements to this process are planned for future releases.

While you can implement a variety of custom import utilities, the Import API doesn't support calls made to it from within event handlers.

## General deployment guidelines

Verify that your application follows these general guidelines before deploying it to Relativity:

- Verify that the NuGet package for the Relativity.Server.Import.SDK is installed in your Visual Studio project. See Get started with the Import API .

The NuGet package installation lists all the required dependencies for this SDK as shown in the following screenshot:

- Verify that you can export your application from your development environment as a RAP file for deployment in production environments. By building your custom application through the Application Deployment System (ADS), you can ensure all the dependencies, including the Import API SDK with all required dlls, are included in the RAP file. See Build applications and Step 10 - Finalize and export application .

## Required .NET assemblies and binaries

The following table lists the .NET assemblies and binaries that are required for a custom Import API application based on how it is deployed to Relativity.

.NET assemblies and binaries Deployment Method

Custom Page* Agent* .NET application**

Relativity.Server.Import.SDK Required Required Required

Relativity.Server.Transfer.SDK Required Required Required

Outside In binaries Required Required

*Indicates that you are deploying a custom application through an agent or a custom page built on the ADS framework.

**Indicates that you are deploying a custom application built outside of ADS, such as a console or desktop application, web service, or other implementation.

### Additional information about .NET assemblies and binaries

Review the following sections for additional information about how to ensure that your specific type of custom application includes the required .NET assemblies and binaries.

#### Custom pages

When you deploy your custom application through a custom page, your .NET project should reference the SDK package, which ensures all required assemblies and native binaries are copied to the target folder. Use the information in the following sections to verify that your custom page includes all the required .NET assemblies and binaries.

To locate the required assemblies, compile your Visual Studio project. Navigate to <OutPath> for your .NET project. For example, if you compile a release build, these files are located in this path:

Copy

```text
1
<Path to .NET custom page project>\<OutPath>
```

Next, verify the .NET assemblies and native binaries as described in the following sections are in your custom page project.

#### Agents

When you deploy your custom application through an agent, you need to add the required assemblies listed in the following sections as resource files. For more information, see Resource files on the Relativity Documentation site.

#### .NET applications

For custom .NET applications using the Import API, you need to add the required assemblies listed in the following sections as resource files. For more information, see Resource files on the Relativity Documentation site.

On this page

- Deploy Import API applications

- General deployment guidelines

- Required .NET assemblies and binaries

- Additional information about .NET assemblies and binaries


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

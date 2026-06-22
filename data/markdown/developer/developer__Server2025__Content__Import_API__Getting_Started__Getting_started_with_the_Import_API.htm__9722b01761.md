---
title: "Get started with the Import API"
url: https://platform.relativity.com/Server2025/Content/Import_API/Getting_Started/Getting_started_with_the_Import_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:15+00:00
sha256: 6b21352dcedc7abcc4ab4a352275f91878bac073bc18c488420bcb42556bf23f
---

Get started with the Import API Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Get started with the Import API

You can quickly begin importing documents, images, and Relativity Dynamic Objects (RDOs) by setting up your development environment and reviewing code samples that illustrate how to perform basic import tasks

On GitHub, you can find can comprehensive samples illustrating how to import native documents, images, objects, and productions. For additional code samples, see the Server Import API samples repository.

See these related topics:

- Import documents with native files

- Import data into RDOs

- Import images

- Import produced images

- Deploy Import API applications

## Import API dependencies

The Import API requires the following software:

- Microsoft .NET 4.6.2 or above

- Set the platform target to x64 to support images. For more information, see Set up a development environment

- Redistributables listed in the following table:

Operating System VC++2010 (x86) VC++2010 (x64) VC++2017 (x86) VC++2017 (x64)

32-bit ü ü

64-bit ü ü ü ü

## Set up a development environment

To develop with the Import API, you can use NuGet packages to simplify the initial setup and upgrades, and to ensure all required platform dependencies are installed.

### Before you begin

Complete the following tasks before you set up your development environment:

- Add the NuGet package called Relativity.Server.Import.SDK to your Visual Studio projects used for import applications. For detailed steps, see Set up your environment .

For information about compatible versions of the NuGet package and Relativity, see Import API

### Set up your environment

Use the following steps to set up a Visual Studio project:

- Create a new Console Application in Visual Studio.

- Open the Solution Explorer.

- Confirm that the Target framework is . NET Framework 4.6.2 . (In the Solution Explorer, expand your project and right-click Properties . Click Open to display the Application tab in the left pane. Select . NET Framework 4.6.2 in the Target framework box.)

- Click the Build tab and set the platform target to x64. ( Build > Configuration Manager ).

- Add the NuGet package reference called Relativity.Server.Import.SDK . (In the Solution Explorer, right-click References > Manage NuGet Packages . Type the package identifier.)

- Use the Relativity.Server.Import.SDK package in any new projects.

- The Import API NuGet package includes all required third-party .NET dependencies and the custom scripts used to copy the native libraries to the target path.

- Add your custom code to the project. For sample code, see this list of related topics .

- You may need to include additional assemblies (such as Outside In (OI) binaries to your project, based on how it is deployed to Relativity. See the topic Deploy Import API applications for more details.

## Import API endpoint URL

The Relativity WebAPI is the web service for accessing the Import API. Use the following format for the WebAPI URL:

Copy

```text
1
2

https://<Relativity host>/relativitywebapi
```

For example:

Copy

```text
1
2

https://relativity.relativity.com/relativitywebapi
```

The WebAPI URL can be set programmatically when you create an instance of the ImportAPI class. For more information, see ImportAPI class. It can also be set as the optional WebServiceURL property in the app.config file. The Import API generates an error when it is unable to resolve the location of the Relativity WebAPI.

## Transfer modes

The Import API is integrated with the Transfer API to support these data transfer modes:

- Web - uses the HTTP client. This is the default mode. Because of the limitations of the HTTP protocol and varying network bandwidth, it is the slowest.

- Direct - uses the file share client. Direct mode provides the fastest transfer speed.

Before data transfer is performed, the underlying Transfer API (TAPI) queries the resource server configurations and automatically selects the optimal available mode for the transfer job. This significantly improves the performance of import jobs. The import speed is also improved by asynchronous retry logic.

You can use configuration properties in the optional app.config file to force the Import API to use a specific transfer mode.

### Direct mode

Direct mode provides faster performance, but it requires a connection to the network hosting the data, as well as specific Windows group permissions. Direct mode has direct access to write to the file repository, which bypasses the need to go through the web server in order to ingest the data, saving a significant amount of time.

#### Requirements

The following conditions must be met in order to load data using direct mode into Relativity Server instance:

- The Active Directory account running the load must have direct access to the Relativity File Repository.

The Import API automatically uses the TapiForceBcpHttpClient app.config setting when the BCP share isn't accessible.

- The loaded data must be located on the Relativity system network/domain.

- The computer running the application that uses the Import API must be located on the Relativity system network/domain.

- The group of users responsible for uploading documents through the Win Relativity component (Relativity Upload Users) must have Full Control in the Document Repository Share. This allows members of this group to import and export in Direct mode. Non-members can only import and export in Web mode.

## Optional app.config file

You can optionally add an app.config file to the Visual Studio project used for development with the Import API. You can specify various configuration settings in this file, including the location of the WebAPI. For more information, see Configuring the RDC on the Relativity Server 2025 Documentation site.

In the Import API, you can programmatically configure several settings required for an import application through the Settings property on the ImageImportBulkArtifact and ImportBulkArtifactJob classes. You can’t programmatically set the batch size, but you can update the ImportBatchSize value in the app.config, which has a default value of 1000 when not specified for an application. For more information, see ImportBulkArtifactJob class .

## Zero byte files

By default, the Import API imports only metadata for native files with the size of 0 KB. In the viewer, users see extracted text when it exists for the file. If the file has no extracted text, users see a blank placeholder, and no viewer options will be available.

Alternately, you can configure the Import API to not import metadata for an empty file. To do this, add the following line to the <Relativity.DataExchange> section in the app.config file:

Copy

```text
1
2

<add key="CreateErrorForEmptyNativeFile" value="True" />
```

For more information, see Configuring the RDC on the Relativity Server 2025 Documentation site.

## Data encoding

The Import API allows you to specify the character encoding of extracted text. However, all object metadata are imported as UTF-16.

## ADS deployment considerations

After building your custom application, you need to add it to Relativity. For information on this process, see Deploy Import API applications .

On this page

- Get started with the Import API

- Import API dependencies

- Set up a development environment

- Before you begin

- Set up your environment

- Import API endpoint URL

- Transfer modes

- Direct mode

- Optional app.config file

- Zero byte files

- Data encoding

- ADS deployment considerations


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

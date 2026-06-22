---
title: "Get started with the Processing SDK"
url: https://platform.relativity.com/Server2025/Content/BD_Processing/Get_started_with_the_Processing_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:40+00:00
sha256: 1af3f3bce1023a3b39961633bfd0d0e459e5172a78b06cd99a4bde8c93fbce32
---

Get started with the Processing SDK Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Get started with the Processing SDK

The Processing SDK supports the automation of your processing workflows. You can programmatically use this API to create and update custodians, data sources, processing sets, and profiles required for processing. It provides an alternative to manually creating them through the Relativity UI. You also can use the Processing API to run inventory, discovery, and publishing jobs.

Use the information on this page to learn about Processing API fundamentals. It includes prerequisites for developing with this API, and code samples for common operations. Additional resources to help you get started with the Processing API include:

- Processing on the Relativity Documentation site - provides general information about how Relativity supports processing.

See these related pages:

- Processing API services for REST

- Troubleshooting Processing API errors

## Processing API fundamentals

The Processing application provides system admins with the ability to ingest raw data directly into a workspace for review. When you set up a processing workflow, you create a processing profile. This profile specifies settings that control how the processing engine ingests the data. You create or reference the following items:

- A custodian who is a user associated with the data included in a processing job.

- A data source that contains the path used to specify the location of the files that you want to discover.

You also create a processing set that links a processing profile to one or more data sources. When you run a discovery job, the processing engine discovers files in the data source based on the values specified in the processing set. For more information, see Processing on the Relativity Documentation site

The Processing API provides interfaces and objects that you can use to automate many of the tasks in a processing workflow. It includes the following interfaces that you can use to access services, which interact with custodian, data source, and processing set objects:

- IProcessingCustodianManager*: used to access the Processing Custodian Manager service.

- IProcessingDataSourceManager*: used to access the Processing Data Source Manager service.

- IProcessingDocumentManager: used to access the Processing Document Manager service.

- IProcessingFilterManager: used to access the Processing Filter Manager service.

- IProcessingJobManager: used to access the Processing Job Manager service.

- IProcessingSetManager*: used to access the Processing Set Manager service.

- IFieldMappingManager: used to access the Field Mapping Manager service.

*These interfaces provide a CreateAsync() and UpdateAsync() method, which you can use to create, update, or retrieve processing objects.

### Common processing workflows

The Processing API also includes the IProcessingJobManager interface. You can use this interface to access the Processing Job Manager service for running inventory, discovery, and publishing jobs. It includes the following methods:

- SubmitInventoryJobsAsync() method – used for excluding irrelevant files from a data set prior to running a discovery job, such as eliminating NIST file types. The InventoryJob class includes properties for the workspace artifact and processing set IDs required to submit a job.

- SubmitDiscoveryJobsAsync() method – used for submitting data sources to the processing engine for discovery. The DiscoveryJob class includes properties for the workspace artifact and processing set IDs required to submit a job.

- SubmitPublishJobsAsync() method – used to publish the processed data to a workspace after discovery, so that reviewers can access it. The PublishJob class includes properties for the workspace artifact and processing set IDs required to submit a job.

Common workflows for processing include inventorying, discovering, and then publishing data, or just discovering and then publishing data. You can only inventory files that haven’t been discovered. Additionally, you can only publish files after Relativity has completed discovery.

In Relativity, you want to enable the auto-publish option on the processing profile, so that the discovered files are automatically added to the workspace. See Relativity environment setup .

## Processing API prerequisites

Complete the following prerequisites to begin development with the Processing API:

SDK downloads

You can download the SDKs required for automating processing workflows from the Relativity Community. For more information, see Download the SDKs .

After you download the following SDKs, install or extract their contents to folders on your local machine:

- Relativity SDK

- Processing SDK

Relativity environment setup

- Obtain access to an instance of Relativity Server 2025 used for development purposes.

You must install the Processing application on this Relativity instance.

- Enable Developer mode in your development instance of Relativity to simplify troubleshooting.

- In the Relativity UI, ensure that the Auto-publish set field is set to Yes on the processing profile that the processing set references in your code. For more information about this field, see Processing profiles in the Relativity Documentation site.

Required Artifact IDs

You need to obtain the Artifact IDs of several items that the classes in the Processing API reference. Use these steps to obtain this information from the workspace database:

- Log in to Relativity.

- On the Workspace tab, locate the workspace that you want to use for automating a processing workflow. Note the Case Artifact ID for the workspace.

- On your database server for Relativity, open Microsoft SQL Server Management Studio.

- In the Object Explorer, expand Databases .

- Use the Case Artifact ID with the prefix EDDS to find the database for your workspace, such as EDDS1014823.

- Expand your workspace to display a list of tables. Reference these tables to obtain the required Artifact IDs:

- EDDSDBO.Folder – Locate the Artifact ID for the destination folder that you want your data source to reference.

- EDDSDBO.ProcessingProfile – Locate the Artifact ID for the processing profile that you want your processing set to reference.

- EDDSDBO.RelativityTimeZone – Locate the Artifact ID for the time zone that you want your data source to reference.

You must install the Processing application in your Relativity environment in order to view the table for time zones and processing profiles.

## Development guidelines for the Processing API

Use these guidelines when automating workflows with the Processing API:

- Add the following DLL references to your Visual Studio project. For additional information, see Prerequisites for Processing API development .

- Relativity.Processing.Services.Interfaces.dll (in the Processing API SDK)

- kCura.Relativity.Client.dll (in the Relativity SDK)

- Relativity.Kepler.dll (in the Relativity SDK)

- Use the Relativity API helpers to establish a connection with the Processing API and set the context used for your code execution. All code samples on this page illustrate how to use the helper classes to connect with the Processing API. For more information, see Using Relativity API Helpers.

- Call the CreateAsync() method on any processing object that you create, or UpdateAsync() that you modify. Your changes won't be added to the database until you make this call.

- Use a try-catch block around your code for creating, updating, and reading objects. Also, use it when submitting jobs. Catch any ServiceExceptions raised by your code as exemplified in the following code samples.

- Use logging to help troubleshoot your code as exemplified in the following code samples.

On this page

- Get started with the Processing SDK

- Processing API fundamentals

- Common processing workflows

- Processing API prerequisites

- Development guidelines for the Processing API


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

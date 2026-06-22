---
title: "Platform change log Archive"
url: https://platform.relativity.com/Server2025/Content/What_s_new/Platform_change_log_Archive.htm
collection: developer
fetched_at: 2026-06-22T06:22:22+00:00
sha256: c8b76a26ed79a169dd5db63330fd673e13b8dd51758e5db6de4c7f663c038caa
---

Platform change log Archive Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

Version: RelativityOne Server 2025 Server 2024

☰

# Platform change log (Archive)

This change log represents changes before 2019-01-01 that may affect Relativity Developers, such as changes to APIs, deprecation of APIs, new APIs and other developer-focused changes. See the User Guide for version release notes .

You can use the following table to find changes for a specific Relativity version, API, or other value. To filter the data in the table, select a value from a drop-down in the column header (Release, Type, and Feature) or type in the Search field. To sort, click the column name.

For changes since 2019-01-01, please refer to the Platform change log

Date Release Type Feature Change

Date Release Type Feature Change

2018-09-26 9.7.229.5 Enhancement Services API The Export API now supports exporting document fields, including complete long text fields such as extracted text. The IObjectManager interface exposes three new methods to support the export workflow. The InitializeExportAsync() sets up an export job; the RetrieveNextResultsBlockFromExportAsync() method retrieves successive blocks of document fields; and the StreamLongTextAsync() method streams text when it exceeds a specific size limit. Additionally, the Relativity.Services.DataContracts.DTOs.Results namespace includes the ExportInitializationResults class used to provide information about data that is ready for export. For more information, see Export API in Object Manager (.NET) .

2018-09-26 9.7.229.5 Enhancement REST API Through REST, the Export API now supports export functionality. It includes the following new endpoints for this functionality: initializeexportasync, retrievenextresultsblockfromexportasync, and streamlongtextasync. It uses the same export workflow as .NET. For more information, see Export API in Object Manager (REST) .

2018-09-26 9.7.229.5 Enhancement Import API In the Import API, OnProcessProgess event now provides information about the throughput for transferring files and document metadata in bytes per second. This enhancement is the result of the new FilesThroughput and MetadataThroughput properties added to the FullStatus class, which represents status information provided to the OnProcessProgess event. This class is available in the kCura.Relativity.DataReaderClient namespace of the Import API. For more information, see Import API events .

2018-09-26 9.7.229.5 Enhancement Services API The Object Manager API now supports mass operations for creating, updating, and deleting Relativity Dynamic Objects (RDOs). It also supports mass operations for updating and deleting Document objects. In the Relativity.Services.Objects namespace, the IObjectManager interface exposes the new overloaded versions of the CreateAsync(), UpdateAsync(), and DeleteAsync() methods for these operations. Additionally, the Relativity.Services.Objects.DataContracts namespace includes several new classes for making mass operation requests and returning results. For more information, see Object Manager (.NET) .

2018-09-26 9.7.229.5 Enhancement REST API Through the REST API, the Object Manager service supports mass operations with its existing endpoints for update and delete on Document objects and RDOs, and create on RDOs. It does require new JSON request formats for mass operations. For more information, see Object Manager (REST) .

2018-06-30 9.6.202.10 Enhancement RelativityOne Sandbox

Sandbox is an add on feature that provides you a dedicated instance for testing customizations and applications in RelativityOne.

Sandbox provides the ability to further differentiate and customize your RelativityOne offering, enables you to test your customizations and applications without interrupting your production environment, and prepares your organization for the latest RelativityOne functionality and how it will impact custom applications and integrations

Administrators can grant access to Sandbox instances by simply adding users to a Sandbox group in your RelativityOne production instance. Sandbox environments are accessed through Federated Instance Manager (.NET) in the User dropdown.

2018-04-28 9.6.134.78 Breaking change Imaging API In the Imaging API, the StopImagingSetAsync() method has been deprecated for use through .NET. Similarly, the StopImagingSetAsync endpoint has been deprecated for use through REST. Upgrade your custom code to use the StopImagingJobAsync method or endpoint for compatibility with RelativityOne 9.6.110.36 and above, and Relativity Server 9.6.134.78 and above. For more information, see Imaging (.NET) .

2018-04-28 9.6.134.78 Enhancement Relativity Integration Points API Relativity Integration Points API now supports secured configurations for data source providers. The new DataSourceProviderConfiguration class includes properties for storing both general and secured configurations set by a user. The method signatures on the IDataSourceProvider interface have been updated to include a DataSourceProviderConfiguration object as a parameter rather than configuration JSON as used in previous releases. For compatibility with RelativityOne 9.6.110.36 and above, upgrade any custom source providers by referencing the new DLLs provided in the Relativity Integration Points SDK 9.6.33.7. For sample code, see Use secured configurations for sensitive information .

2018-04-28 9.6.134.78 Enhancement Services API New operators for text conditions have been added to enhance querying for objects, and creating views and saved searches. The TextConditionEnum enumeration includes the new IsLessThanOrEqualTo and IsGreaterThanOrEqualTo members. This enumeration is available in the Relativity.Services namespace. Additionally, the CriteriaConditionEnum enumeration includes the new StartsWith and EndsWith members. This enumeration is available in the Relativity.Services.Search namespace. For more information, see Class library reference .

2018-04-28 9.6.134.78 Enhancement API Helpers Relativity API helpers now provide the InstanceSettingsBundle interface for interacting with instance settings from agents, event handlers, and custom pages. The interface includes synchronous and asynchronous methods for refreshing cached instance settings and reading values of different data types. For more information, see Work with instance settings .

2018-04-28 9.6.134.78 Enhancement Data Grid Audit API We have updated the Data Grid Audit API to follow the query pattern of the underlying Object Manager API. You can now use the queryslim endpoint to return a condensed version of the payload to conserve network bandwidth. The request input parameters and response structure have also changed to follow the changes in the Object Manager API. For more information, see Legacy Audit API.

2018-04-28 9.6.134.78 Breaking change Data Grid Audit API The query/withdetails endpoint of the Data Grid Audit API has been deprecated.

2018-02-03 9.6.50.31 Enhancement Event Handlers The new List Page Interaction Event Handler API is a collection of JavaScript APIs, which are now exposed specifically for use with list pages. You can interact with list pages by implementing a ListPageInteractionEventHandler and writing separate JavaScript files that contain custom code. This custom code must use the new List Page Interaction Event Handler API developed specifically for this purpose. For more information, see List Page Interaction event handlers and List Page Interaction Event Handler API .

2018-02-03 9.6.50.31 Enhancement REST API The Object Manager service now makes POST method calls for all its endpoints. It also offers the QuerySlim endpoint, which streamlines querying by returning a smaller payload than the Query endpoint. All the URLs for the existing endpoints have been updated. Additionally, the format for the JSON requests now require request objects, and include various changes to the fields. For more information, see Object Manager (REST) .

2018-02-03 9.6.50.31 Breaking change REST API In the Object Manager service, the URLs for each endpoint have been deprecated, and replaced with ones using a new format. The format for the JSON requests has also been modified, requiring a request object as well as other changes. For more information, see Object Manager (REST) .

2018-02-03 9.6.50.31 Enhancement Services API The Object Manager API now includes the new Relativity.Services.Objects.DataContracts namespace, which contains the majority of classes and enumerations needed to interact with this service. The new Relativity.Services.Objects.Extensions namespace includes classes that contain methods used for working with hydrated objects, such as Choice, Field, Layout, and RelativityObject types. The new QuerySlimAsync() method streamlines querying by returning a smaller payload then the QueryAsync() method. Additionally, the methods on the IObjectManager interface now have updated signatures that require you to pass a request object for a specific operation. For more information, see Relativity Server 2025 Developer News and Object Manager (.NET) .

2018-02-03 9.6.50.31 Breaking change Services API In the Object Manager API, the Relativity.Services.Objects.Models.WebContent namespace and all of its contents have been deprecated. Multiple classes in the Relativity.Services.Objects.Models and Relativity.Services.Field namespace have also been deprecated. In the Relativity.Services.Objects namespace, all existing method signatures have been deprecated and replaced with new ones that require a request object. For more information, see Object Manager (.NET) .

2018-02-03 9.6.50.31 Enhancement Processing API The Processing API now includes the new Processing Profile Manager service that supports CRUD operations on processing profiles. The new IProcessingProfileManager interface exposes the SaveAsync(), ReadAsync(), and DeleteAsync() methods. It includes the new ProcessingProfile class, which has multiple properties for specifying numbering, deNISTing, extraction, and deduplication settings. Additional classes and enumerations have been added to support this functionality. For more information, see Get started with the Processing SDK and Processing API services for REST .

2018-01-06

9.5.411.4

Enhancement Imaging API The Imaging API now includes the new ImageDocumentAsync() method, which is used to image a single document on the fly. It takes an instance of the new ImageDocumentJob class, which contains the properties for the workspace, document, and profile IDs. The Imaging API also includes the new StopImagingJobAsync() method, which is used cancel any type of imaging job, including imaging set jobs and jobs for imaging on the fly. The new StopImagingJobRequest and StopImagingJobResponse classes interact with the StopImagingJobAsync() method. The Imaging API services available through REST also support the new ImageDocumentAsync and StopImagingJobAsync endpoints. For more information, see Imaging (.NET) and Imaging API (REST) .

2017-12-02 9.5.370.136 Enhancement Structured Analytics API The Structured Analytics API now includes the new RunAsync() method used to execute an analysis; the RunAnalysisPreparationAsync() method used to generate fields before running an analysis; the GetValidTasksAsync() method used to retrieve valid operations for a structured analytics set; the RunCopyToLegacyAsync() method used to copy results to legacy document fields; and the CancelCopyToLegacyAsync() method used to cancel a copy operation. It includes the new AnalysisSettings class used to represent a configuration for running an analysis; the ValidTaskResult class used to represent valid operations for a structured analytics set; and the OperationState class used to provide information about an operation status. In addition, it includes the new StructuredAnalyticsTask enumeration, which contains members used to represent valid operations for a set. For more information, see Structured Analytics (.NET) and Structured Analytics Manager (REST).

2017-12-02

9.5.370.136

Breaking change Structured Analytics API In the Structured Analytics API, the RunFullAsync() and the RunIncrementalAsync() methods have been deprecated. The RunAsync() method replaces these deprecated methods for running an analysis of a structured analytics set. In addition, the ExecutionOperation enumeration has been deprecated. The new StructuredAnalyticsTask enumeration now replaces it.

2017-12-02

9.5.370.136

Enhancement Imaging API The new Imaging API supports programmatically executing imaging jobs in Relativity. It includes the imaging job service, which you can use to run, cancel, and retry imaging jobs. The Imaging API provides services for imaging profiles, imaging sets, and application field codes that support all CRUD operations. The imaging set service offers additional functionality used to hide and release images during a quality control review, while the native type service includes functionality for reading native file types supported by Relativity. It also exposes endpoints through REST that support the same functionality as available in .NET. For more information, see Imaging (.NET) and Imaging API (REST) .

2017-10-28 9.5.342.116 Breaking change Application Deployment System To improve system security, we have made changes to the way the Relativity HTML sanitizer component parses embedded HTML code in HTML-enabled and custom text fields and labels.

2017-10-28 9.5.342.116 Enhancement REST API The View Manager service now supports the functionality for associating a dashboard with a view. When you can create or update a view, you can optionally include a Dashboard object in the JSON request. For more information, see View Manager (REST) .

2017-10-28 9.5.342.116 Enhancement Services API In the View Manager API, the View class now has a new property called DashboardRef, which is used to associate a dashboard with a view. This property contains the Artifact ID, name, and any GUIDs for the Dashboard instance. This class is available in the Relativity.Services.View namespace. For more information, see View Manager (.NET) .

2017-10-28 9.5.342.116 Breaking change Services API In the Object Manager API, the QueryAsync() method signature now includes an ObjectTypeRef object rather than an Int32 when referencing an artifact type for a query. This method is available on the IObjectManager interface in the Relativity.Services.Objects namespace.

2017-10-28 9.5.342.116 Breaking change REST API On the Object Manager service, the QueryAsync endpoint now requires the JSON request to contain a DescriptorArtifactTypeID or a Guids field set to an identifier for the artifact type that you want to query on.

2017-10-28 9.5.342.116 Enhancement Services API The Object Manager service now includes the new DeleteSingleAsync() method, which is used for deleting Document objects and all their associated files, as well as RDOs. The new ObjectDeleteResult class represents the results of a delete operation, and contains a DeleteReport property. The new DeleteReport class provides the results of a delete operation as a collection of DeleteItems objects. The new DeleteItems class contains information about each item removed during a delete operation, such as the type of object deleted, the number of objects, and other details.

2017-10-28 9.5.342.116 Enhancement REST API The Object Manager service now includes the DeleteSingleAsync endpoint, which supports deleting Document objects and all their associated files, as well as RDOs.

2017-12-02 9.5.370.136 Enhancement Document Viewer Services API The new Document Viewer Services API includes functionality for converting documents to viewer types supported by Relativity, including native, image, production, and transcript types. It includes the GetViewerContentKeyAsync() method that provides this functionality. This method takes a GetViewerContentKeyRequest object that includes information about how to convert a document, such as its conversion type, priority, and other options. The Document Viewer Services API also exposes an endpoint through REST that supports this functionality. For more information, see Document Viewer Services (.NET) .

2017-10-28 9.5.342.116 Enhancement Relativity SDK

We no longer provide the 32-bit version of the SDK. All custom development for RelativityOne must be performed using the 64-bit version.

2017-10-28 9.5.342.116 Enhancement Invariant API

You can now use the DocumentManager RESTful service of the Invariant API to troubleshoot the errors related to the metadata of documents in processing sets.

2017-09-02 9.5.292.12 Breaking change Relativity Integration Points API For the Relativity Integration Points API, the kCura.SourceProviderInstaller.dll file has been renamed to kCura.IntegrationPoints.SourceProviderInstaller.dll.

2017-09-30 9.5.309.48 Enhancement Field Size API When interacting with Relativity data, you can now use the RESTful Text Field Size Service to return the size of text in any fixed length or long text field. The API returns the size of the text in UTF-16 bytes, and you don't have to retrieve the contents of the field to calculate it. You can use this functionality to identify documents of a certain size, and use the API to interact with the text in both Data Grid and the Relativity SQL database. For more information, see Field Size API .

2017-09-30 9.5.287.43 Enhancement Import API We have significantly improved the performance of the Import API by integrating it with the Relativity Transfer API. The Transfer API queries the target Relativity workspace and, depending on how it is set up, automatically selects an optimal transfer mode: Aspera, direct, or web. Import jobs are now faster, and we have provided additional configuration properties that give you more control of the import and export process. For more information, see Get started with the Import API .

2017-09-30 9.5.309.48 Enhancement Invariant Monitoring API You can now use the SetWorkgroupAsync endpoints of the Worker Manager and Job Manager RESTful services of the Invariant API to change the workgroup for workers and jobs. We have added the SetPriorityAsync endpoint to the Job Manager service that enables you to set job priority. You can also use the new RemoveWorkerAsync endpoint of the Worker Manager service to delete processing workers.

2017-09-30 9.5.309.48 Enhancement Production API We have made enhancements to the Production API to allow you to select the production placeholder image format. For more information, see Production Manager (.NET) and Production Data Source Manager (.NET) .

2017-09-30 9.5.309.48 Enhancement Services API In the Object Query Manager service, the Query class now has a new QueryHint property, which is used to optimize the view. When you call the QueryAsync() method, you can optionally set this property on the Query instance that you pass to this method. The Query class is available in the Relativity.Services.ObjectQuery namespace.

2017-09-30 9.5.309.48 Enhancement REST API In the Object Query Manager service, the Query object can now optionally include the QueryHint field in a JSON request on the QueryAync endpoint. The optional QueryHint field is used to optimize the view.

2017-09-30 9.5.309.48 Enhancement Services API The Object Manager service now includes the new CreateSingleAsync() method, which is used for creating Relativity Dynamic Objects (RDOs) and setting values on their associated fields. The new ObjectCreateResult class represents objects returned by this method. The new Relativity.Services.Objects.Models.WebContent namespace contains classes used to provide event handlers with information about the context in which they are called. Two new overloaded QueryAsync() methods include the options to monitor the progress of a query and to request its cancellation. The Query class now has a new QueryHint property, which is used to optimize the view. The ReadSingleAsync() and UpdateAsync() methods now support identifying fields by name.

2017-09-30 9.5.309.48 Breaking change Services API In the Object Manager service, the signatures of the ReadSingleAsync() and UpdateAsync() methods now require a CallingContext object. The Query object can now optionally include the QueryHint field in a JSON request on the QueryAync endpoint.

2017-09-30 9.5.309.48 Breaking change Services API The Services API now supports retrieval of Data Grid-enabled fields with Read() and ReadSingle() operations.

2017-09-30 9.5.309.48 Breaking change Services API The Services API Update() and UpdateSingle() operations with both SQL and Data Grid-enabled fields now generate a single audit record. The oldValue and newValue audit for large text fields are now truncated at 1,000,000 characters for both types of field. For more information, see Work with data grid .

2017-09-30 9.5.309.48 Breaking change Services API You can now programmatically associate saved searches with Relativity dashboards.

2017-09-30 9.5.309.48 Enhancement REST API The Object Manager service now includes the CreateSingleAsync endpoint, which supports creating Relativity Dynamic Objects (RDOs) and setting values on their associated fields. Additionally, the ReadSingleAsync() and UpdateAsync() endpoints now support identifying fields by name.

2017-09-30 9.5.309.48 Breaking change REST API In the Object Manager service, the JSON requests for the ReadSingleAsync() and UpdateAsync() endpoints now require a CallingContext field.

2017-09-30 9.5.309.48 Enhancement REST API You can now use the REST API to associate saved searches with dashboards. See Keyword Search Manager (REST) for saved searches .

2017-09-30 9.5.309.48 Enhancement Transfer API We are making the Transfer API (TAPI) available to third-party developers as a technology preview. You can use TAPI to build application components that connect to a Relativity instance and stream the data into Relativity from external data sources using different transfer protocols, for example, HTTP, SMB, and Aspera. You can find the TAPI libraries and documentation in GitHub ( https://github.com/relativitydev/transfer-api-samples ).

2017-07-29 9.5.253.62 Enhancement Application Deployment System We have enhanced the application upgrade process to purge assembly resource files (DLLs) no longer associated to the newer application version. This also removes agent types, event handlers, and application services associated with the application objects. For more information, see Application resource file purge .

2017-07-29 9.5.253.62 Enhancement REST API When using the GetFilteredSearchContainerTreeAsync endpoint in the Search Container Manager REST service, you can now specify the saved search tree filtering condition as the object with matching properties, such as created by user, created date, and matching the text in the search and folder names.

2017-07-29 9.5.253.62 Enhancement REST API The Search Container Manager REST service now includes the new GetAdvancedSearchViewInfoAsync, GetAdvancedSearchViewUniqueCreatedByAsync, GetAdvancedSearchViewUniqueModifiedByAsync, and GetAdvancedSearchViewUniqueOwnersAsync endpoints for working with the Advanced Search View fields. For more information, see Keyword Search Manager (.NET) for saved searches

2017-07-29 9.5.253.62 Enhancement Services API We have added an overloaded to the GetFilteredSearchContainerTreeAsync() method that allows you to specify the saved search tree filtering condition as the SearchContainerTreeFilter object. The condition is a set of object properties, such as created by user, created date, and matching the text in the search and folder names.

2017-07-29 9.5.253.62 Enhancement Services API The ISearchContainerManager interface provides GetAdvancedSearchViewInfoAsync(), GetAdvancedSearchViewUniqueCreatedByAsync(), GetAdvancedSearchViewUniqueModifiedByAsync(), and GetAdvancedSearchViewUniqueOwnersAsync() methods for working with the Advanced Search View fields.F

2017-09-30 9.5.309.48 Enhancement Processing API The Processing API now includes the new SubmitCancelJobAsync() method and CancelJob class. You can use this method to cancel inventory, discovery, and publishing jobs for a specific processing set. The Processing Services REST API also supports the new SubmitCancelJobAsync endpoint. For more information, see Get started with the Processing SDK .

2017-07-01 9.5.219.30 Enhancement Services API The DefaultFileLocation property of the Workspace DTO now contains a ResourceServer object. You can set it by specifying the resource server ArtifactID as the choice ArtifactID.

2017-07-01 9.5.219.30 Enhancement Application Deployment System The Application Deployment System removes the no longer used event handlers from the associated object types upon application upgrade. For more information, see Advanced functionality for the application framework .

2017-06-29 9.5.196.102 Enhancement Developer environment setup You must upgrade your Relativity development environment to .NET 4.6.2.

2017-07-01 9.5.219.30 Enhancement Analytics Index Manager API

We have refactored the Analytics Index Manager API to be part of the Analytics application and provide more advanced features for interacting with Analytics indexes. The API now includes the functionality for creating, reading, updating, and deleting indexes, and also retrieving index status and submitting and canceling index jobs. In addition, the Analytics Index Manager API exposes endpoints through REST that provide similar functionality. You must install the Analytics application in your Relativity workspace before you can automate workflows with this API. For more information, see Analytics Index Manager(.NET).

2017-06-29 9.5.196.102 Enhancement Services API The Object Manager service supports updating and reading fields on Document objects and Relativity Dynamic objects (RDOs). It also supports querying for Workspaces, Documents, RDOs and system types. These methods are available on the new IObjectManager interface in the Relativity.Services.Objects namespace. Additionally, the new Relativity.Services.Objects.Models namespace contains the following classes used by this service: ObjectUpdateResult, ObjectReadResult, ObjectQueryResultSet, Query, RelativityObject, and EventHandlerStatus classes. The new Relativity.Services.Objects.Exceptions namespace contains the EventHandlerFailedException class.

2017-06-29 9.5.196.102 Enhancement REST API The Object Manager service supports updating and reading fields on Document objects and Relativity Dynamic objects (RDOs). The Object Manager service also includes functionality for querying on Workspaces, Documents, RDOs and system types.

2017-05-31 9.5.162.111 Enhancement Services API The View Manager service provides methods for creating, reading, and updating views. It includes the GetViewOwnersAsync() method for retrieving workspaces users who can be assigned ownership of a view, as well as the GetAccessStatusAsync() method for retrieving information about whether a user has View permissions on a view and on the fields used in the search conditions on a view. The GetObjectTypesAsync() method retrieves a list of the object types in a workspace, which you can use to assign an object type to a view based on the objects that you want displayed in it. The new IViewManager interface is available in the Relativity.Services.View namespace. For more information, see View Manager (.NET) .

2017-05-31 9.5.162.111 Enhancement REST API The View Manager service supports creates, reads, and updates views. It retrieves workspaces users who can be assigned ownership of a view. It retrieves information about whether a user has View permissions on a view and on the fields used in the search conditions on a view. This service retrieves a list of the object types in a workspace, which you can use to assign an object type to a view based on the objects that you want displayed in it. For more information, see View Manager (REST) .

2017-04-26 9.5.133.118 Enhancement Services API You can now use the Services API to create, read, update, delete and query admin-level RDOs.

2017-04-26 9.5.133.118 Enhancement Services API The CopySingleAsync() method is now available in the IAnalyticsSearchManager, IdtSearchManager, and IKeywordSearchManager interfaces. The method allows you to create a copy of a specified saved search in the same folder.

2017-04-26 9.5.133.118 Enhancement Services API You can now use the GetAccessStatusAsync() helper method to return the information about the user's ability to access a saved search or a document folder. The method is available on the IAnalyticsSearchManager, IdtSearchManager, IKeywordSearchManager, and IFolderManager interfaces.

2017-04-26 9.5.133.118 Enhancement Services API The MoveAsync() method in the IAnalyticsSearchManager, IdtSearchManager, IKeywordSearchManager, and ISearchContainerManager interfaces now allows you to move a saved search or a saved search folder to a different saved search folder.

2017-04-26 9.5.133.118 Enhancement REST API The Analytics Search Manager, dtSearch Manager, and Keyword Search Manager REST services now include the CopySingleAsync endpoint. The endpoint allows you to create a copy of a specified saved search in the same folder.

2017-04-26 9.5.133.118 Enhancement REST API The GetAccessStatusAsync endpoint in the Analytics Search Manager, dtSearch Manager, Keyword Search Manager, and Folder Manager REST services now allows you to return the information about the user's ability to access a saved search or a document folder.

2017-04-26 9.5.133.118 Enhancement REST API You can use the new MoveAsync endpoint in the Analytics Search Manager, dtSearch Manager, Keyword Search Manager, and Search Container Manager REST services to move a saved search or a saved search folder to a different saved search folder.

2017-04-26 9.5.133.118 Enhancement Relativity Integration Points API The FieldEntry class has a new property called Type, which is a string that indicates the Relativity field type. This class is available in the kCura.IntegrationPoints.Contracts.Models namespace.

2017-02-22 9.5.69.85 Defect REST API Fixed an issue with the ARM API where move jobs could not be updated.

2017-02-22 9.5.69.85 Defect REST API Fixed validation of “Existing Target Database” field when creating restore jobs via the ARM API.

2017-02-22 9.5.69.85 Defect REST API Groups can now be auto-mapped when restoring via the ARM API.

2017-02-22 9.5.69.85 Enhancement REST API The ARM API now supports specifying the Analytics server to restore for ARM restore jobs when the archive contains Analytics data.

2017-02-22 9.5.69.85 Enhancement Structured Analytics API The new Structured Analytics API includes functionality for automating a full or incremental analysis of a structured analytics set, checking the status of the analysis, retrieving document and other errors, and performing additional tasks. It contains the IStructuredAnalyticsManager interface that exposes the overloaded RunFullAsync(), RunIncrementalAsync(), GetErrorsAsync(), and other methods. The Structured Analytics API also exposes endpoints through REST, which support similar functionality. For more information, see Structured Analytics (.NET).

2017-02-22 9.5.69.85 Enhancement Services API In the Services API, the Folder Manager service now includes the new MoveFolderAsync() method, which you can use to move a folder and its children, including subfolders and documents. It also includes the new FolderMoveResultSet class. The MoveFolderAsync() method returns an object of this type that provides information about the status of the move operation.

2017-02-22 9.5.69.85 Enhancement REST API In the REST API, the Folder Manager service now supports the MoveFolderAsync() endpoint, which you can use to move a folder and its children, including subfolders and documents.

2017-01-25 9.5.41.87 Breaking change Relativity Database Relativity has deprecated support for the EDDSResource database. Mass Operation handlers that reference tables in this database won’t function properly. Instead, update these handlers to reference the new location under the workspace database with the [Resource] schema qualifier.

2017-01-25 9.5.41.87 Enhancement Services API In the Services API, the Object Query Manager service now includes the new overloaded QueryUniqueFieldValuesAsync() method used to query for unique values in fixed-length text fields. It also includes the new ObjectQueryUniqueFieldValuesResult class. The QueryUniqueFieldValuesAsync() method returns an object of this type, which contains the list of unique field values.

2017-01-25 9.5.41.87 Enhancement REST API The new ARM API provides a REST service that supports multiple operations required to archive, restore, and move Relativity workspace data. For more information, see .

2017-01-25 9.5.41.87 Enhancement REST API In the REST API, the Object Query Manager service now supports the new QueryUniqueFieldValuesAsync endpoint used to query for unique values in fixed-length text fields.

2016-11-30 9.4.378.21 Enhancement Services API Use the SendBulkInvitationAsync method of the ILoginProfileManager interface to send invitation emails to multiple users. Before sending the emails, you can test whether the users are properly configured with the VerifyBulkInvitationAsync method. For more information, see Login Profile Manager (.NET) .

2016-11-30 9.4.378.21 Enhancement REST API The Login Profile Manager service now provides the SendBulkInvitationAsync and VerifyBulkInvitationAsync endpoints for sending out invitation to multiple users. For more information, see Login Profile Manager (REST)

2016-11-30 9.4.378.21 Enhancement Services API The Services API now includes the Logging Configuration Manager, the Logging Rule Manager, and the Logging Sink Manager services. These services support programmatically interacting with the Relativity logging framework. The interfaces used to access these services are available in the Relativity.Services.LoggingConfig namespace. This namespace also includes the Configuration, Rule, and Sink classes used in conjunction with the new services.

2016-11-30 9.4.378.21 Enhancement REST API The REST API now includes logging configuration services for creating and retrieving configurations, rules, and sinks used in the Relativity logging framework. It also provides endpoints for deleting configurations and rules. This new coverage includes the Logging Configuration Manager, the Logging Rule Manager, and the Logging Sink Manager services.

2016-11-30 9.4.378.21 Enhancement Relativity Scripts We have added the timezone input constant for specifying time zone offset in Relativity scripts. For more information, see constant .

2016-11-15 9.4.361.1 Enhancement Services API Added the overloaded CreateAsync method to the IOAuth2ClientManager interface to accept an OAuth2Client object for creating an OAuth2 client with a specified, rather than an autogenerated, ID. For more information, see OAuth2 Client Manager (.NET) .

2016-11-15 9.4.361.1 Enhancement REST API You can now use the OAuth2 Client Manager REST service to create OAuth2 clients with a specified ID. For more information, see OAuth2 Client Manager (REST) .

2016-11-15 9.4.361.1 Enhancement Data Grid You can now use the LUCENESEARCH operator for data grid-enabled fields in the following search conditions.

2016-11-15 9.4.361.1 Enhancement Services API The Password Bank Manager service retrieves document passwords from the password bank used by processing and imaging. It includes the GetAllPasswordsAsync() method to retrieve passwords. For more information, see Password Bank Manager (.NET).

2016-11-15 9.4.361.1 Enhancement REST API The Password Bank Manager service retrieves document passwords from the password bank used by processing and imaging. It includes the GetAllPasswordsAsync endpoint to retrieve passwords. For more information, see Password Bank Manager (REST).

2016-10-04 9.4.321.2 Breaking change Relativity Database Relativity is phasing out support for the EDDSResource database as January 2017. Mass Operation handlers that reference tables in this database won’t function properly. Instead, update these handlers to reference the new location under the workspace database with the [Resource] schema qualifier.

2016-10-04 9.4.321.2 Enhancement Invariant API Relativity 9.4.321.2 includes general enhancements to Invariant. Due to these enhancements, you must update the reference to the Invariant.core.dll in custom Invariant plugins used in Relativity 9.4.321.2 .

2016-10-04 9.4.321.2 Enhancement REST API The REST API now support the LUCENESEARCH operator for searching text in the Data Grid using the Object Query Manager service. For more information, see Work with data grid .

2016-10-04 9.4.321.2 Enhancement Services API

You can now use Lucene syntax when searching Data Grid-enabled fields through Relativity Object Queries. For more information, see Work with data grid .

2016-08-31 9.4.284.1 Enhancement Services API

Support for programmatic access to OAuth2 clients to authenticate against Relativity in a secure manner. The API allows you to create, read, update, and delete OAuth2 clients, and regenerate secrets for certain types of clients. You can perform the operations using the IOAuth2ClientManager interface. For more information, see OAuth2 Client Manager (.NET) .

2016-08-31 9.4.284.1 Enhancement Services API

You can create, read, update, and delete federated instances using the IFederatedInstanceManager interface. For more information, see Federated Instance Manager (.NET) .

2016-08-31 9.4.284.1 Enhancement REST API

Coverage for OAuth2 clients through REST. The API allows you to create, read, update, and delete OAuth2 clients, and regenerate secrets for certain types of clients. You can perform the operations using the OAuth2 Client Manager REST service. For more information, see OAuth2 Client Manager (.NET) .

2016-08-31 9.4.284.1 Enhancement REST API

You can create, read, update, and delete federated instances using the Federated Instance Manager REST service. For more information, see Federated Instance Manager (.NET) .

2016-08-31 9.4.284.1 Breaking change Relativity Scripts We have removed the foreign keys from the Document and RDO database tables. This includes artifact, single object, and multi-object table relationships. Doing this resolves the previous issues involved with globally locking the artifact and other tables for the entire duration of a deletion job, which could be lengthy and could subsequently delay document review. As a result of removing these foreign keys, the delete process will execute without applying a global lock, allowing the system to then batch delete records without delaying document review in Relativity.

2016-07-27 9.4.254.2 Enhancement Services API The Services API now provides the SendInvitationAsync and SetPasswordAsync methods for working with the Relativity user login profile. Use the methods to send login invitation emails (after creating users) and reset Relativity passwords. For more information, see Login Profile Manager (.NET) .

2016-07-27 9.4.254.2 Enhancement REST API You can now use the Login Profile Manager service SendInvitationAsync and SetPasswordAsync operations to send login invitation emails and resetting Relativity passwords. For more information, see Login Profile Manager (REST) .

2016-07-27 9.4.254.2 Enhancement Processing API The ProcessingDataSource class now includes the new StartNumber property, which represents the value used to begin numbering a sequence of documents published from a specific data source. The new IsStartNumberVisible property determines whether the Relativity UI displays the Start Number field on the Data Source layout. The REST API also supports these properties. For more information, see Get started with the Processing API .

2016-07-27 9.4.254.2 Breaking change Relativity Scripts We have changed the [Redaction] data table to more accurately store information. Changing the datatype of the existing columns could take over an hour on certain large cases, and so instead, the following four nullable decimal columns have been added: Redaction.[X_d], Redaction. [Y_d], Redaction. [Width_d], Redaction. [Height_d].

2016-07-27 9.4.254.2 Defect Import API Production imports through Import API in overlay mode now correctly update existing documents

2016-07-27 9.4.254.2 Defect Import API Dynamic objects created through the Import API are now correctly audited in the audit table.

2016-06-29 9.4.224.2 Enhancement Services API Added support for common authentication protocols, including SAML 2.0, Open ID Connect (OIDC), and OAuth2. Using these protocols, you can now authenticate to Relativity via many popular identity providers, such as Okta or Azure Active Directory. For the authentication overview, see Authentication overview .

2016-06-29 9.4.224.2 Enhancement Services API API coverage has been added around the new authentication model, allowing developers to programatically configure authentication providers and users in Relativity. For the authentication API overview, see Identity (authentication and user accounts) .

2016-06-29 9.4.224.2 Breaking change Services API When using the RSAPI, all authentication-related fields on the User object now have an Obsolete tag. If an application consuming these APIs has “Treat Warnings as Errors” turned on, this will cause a minor compile-time breaking change.

2016-06-29 9.4.224.2 Enhancement Services API The new Field Mapping service maps fields between Relativity and an external data source. For this release, the only external data source supported by this service is Invariant. For more information, see Field mapping for processing .

2016-06-29 9.4.224.2 Defect Services API Relativity Service Catalog now uses one timer to reset data in the service catalog, instead of a new timer for each request.

2016-06-29 9.4.224.2 Enhancement API Helpers You can now use the GetGuid() method of the API helper interfaces to return the GUID of a Relativity artifact from agents, custom pages, and event handlers. For more information, see Basic concepts for Relativity API Helpers .

2016-06-29 9.4.224.2 Enhancement REST API The new Field Mapping service maps fields between Relativity and an external data source. For this release, the only external data source supported by this service is Invariant. For more information, see Field mapping .

2016-06-29 9.4.224.2 Enhancement Invariant API The Invariant API now includes the GetAutoMappedGuids() method for internal use only. The IDataSources interface in the Invariant namespace contains this method.

2016-06-29 9.4.224.2 Enhancement Relativity Integration Points API The kCura.IntegrationPoints.Contracts namespace now includes the new ProviderFactoryBase class, which simplifies the implementation of dependency injection. For more information, see Update the use of dependency injection . This namespace also includes the new SourceProviderConfiguration class, which includes optional properties that control source provider behavior, such as whether Relativity copies native files to a repository. For sample code, see Display source provider settings selected by users and Build an advanced integration point .

2016-06-29 9.4.224.2 Enhancement Relativity Integration Points API The FieldEntry class has the new ActualName property, which is the name used for the field in the source code. This class is available in the kCura.IntegrationPoints.Contracts.Models namespace.

2016-06-29 9.4.224.2 Enhancement Relativity Integration Points API The kCura.IntegrationPoints.Contracts.Provider namespace now includes the new ProviderReadDataException class, which represents an error thrown by an IDataReader when a read failure occurs.

2016-06-29 9.4.224.2 Enhancement Relativity Integration Points API The kCura.IntegrationPoints.SourceProviderInstaller namespace includes an update to the SourceProvider class, which has the new Configuration property. This property is used to get or set a list of optional properties that control source provider behavior.

2016-06-29 9.4.224.2 Deprecation Relativity Integration Points API The kCura.IntegrationPoints.Contracts.Synchronizer namespace has been deprecated. The DefaultProviderFactory class, IProviderFactory interface, and PluginBuilder class in the kCura.IntegrationPoints.Contracts namespace have also been deprecated. In addition, the FieldMap class and FieldMapTypeEnum enumeration in the kCura.IntegrationPoints.Contracts.Models namespace have been deprecated. For upgrade information, see Upgrade integration points for use in Relativity 9.4 .

2016-05-25 9.3.418.9 Enhancement Services API The Services API allows you to programmatically interact with production data sources. For more information, see Production Data Source Manager (REST) .

2016-05-25 9.3.418.9 Enhancement Services API The REST now allows you to programmatically interact with production data sources. For more information, see Production Data Source Manager (REST) in the REST API reference.

2016-05-25 9.3.418.9 Enhancement REST API You can now create productions using the CreateSingleAsync() method of the IProductionsManager interface. For more information, see Production Manager (.NET) .

2016-05-25 9.3.418.9 Enhancement REST API You can now create productions using the CreateSingleAsync endpoint of the Production Manager Service. For more information, see Production Manager (REST) .

2016-05-25 9.3.418.9 Enhancement Services API Separate CreateSingleAsync() and UpdateSingleAsync() methods of the IProductionPlaceholder have been added for creating and updating production placeholders. The SaveSingleAsync() method of the IProductionPlaceholder interface has been deprecated. For more information, see Production Placeholder Manager (.NET) .

2016-05-25 9.3.418.9 Deprecation REST API Separate CreateSingleAsync and UpdateSingleAsync endpoints have been added to the Production Placeholder Manager service for creating and updating production placeholders. The SaveSingleAsync endpoint has been deprecated. For more information, see Production Placeholder Manager (REST) .

2016-05-25 9.3.418.9 Enhancement Services API Use the GetAllAsync() method of the IProductionManager to return a list of all productions in a workspace. GetAllProductionsAsync() has been deprecated. For more information, see Production Manager (.NET) .

2016-05-25 9.3.418.9 Deprecation REST API Use the GetAllAsync endpoint of the Production Manager service to return a list of all productions in a workspace. GetAllProductionsAsync has been deprecated. For more information, see Production Manager (REST) .

2016-05-25 9.3.418.9 Enhancement Services API The suppressWarnings parameter has been added to the RunProductionAsync() method of the IProductionManager interface to indicate whether a production should fail if there are warning messages. For more information, see Production Manager (.NET) .

2016-05-25 9.3.418.9 Enhancement REST API The suppressWarnings parameter has been added to the RunProductionAsync endpoint of the Production Manager service to indicate whether a production should fail if there are warning messages. For more information, see Production Manager (REST) .

2016-05-25 9.3.418.9 Enhancement Services API The TextCondition class now supports the IS SET and IS NOT SET operators for querying text in the Data Grid. For more information, see Work with data grid .

2016-05-25 9.3.418.9 Enhancement REST API The REST API now support the IS SET and IS NOT SET operators for querying text in the Data Grid. For more information, see Work with data grid .

2016-05-25 9.3.418.9 Enhancement Services API You can now use the MonthOf operator in the Services API date queries.

2016-05-25 9.3.418.9 Enhancement REST API You can now use the MonthOf operator in the REST API date queries.

2016-04-27 9.3.389.9 Enhancement Processing API In the Processing API, the ProcessingCustodian class now includes a CustodianType and Name property. The CustodianType property identifies the custodian as an individual or an entity who owns data in a processing set. The Name property corresponds to the Full Name field on a Custodian object in Relativity. For more information, see Get started with the Processing API .

2016-04-27 9.3.389.9 Enhancement Processing API The Processing API now includes the GetDocumentAggregates() method on the IProcessingSetManager interface. This method retrieves a list of processing sets and related document aggregate information. It also includes the addition of the GetDocumentAggregatesRequest, ProcessingSetDocumentInfoSummary, and ProcessingSetDocumentInfo classes, which the GetDocumentAggregates() method uses during the retrieval of the required processing sets. For more information, see Get started with the Processing API .

2016-04-27 9.3.389.9 Enhancement Processing API The Processing API now includes the GetDocumentAggregates endpoint on Processing Set Manager service available through Relativity REST API. It provides the same functionality that is available through the GetDocumentAggregates() method on the IProcessingSetManager interface. For more information, see Processing API services for REST .

2016-04-27 9.3.389.9 Defect Services API Saved search queries in FluidUI have been updated to return the full range of the date-time values in search conditions instead of just the starting time.

2016-04-27 9.3.389.9 Defect Services API Relativity Services API has been updated to allow you to write to data grid-enabled fields.

2016-04-27 9.3.389.9 Enhancement Services API The ObjectQueryManager service now supports multi-reflected multiple choice fields in the response returned on a query.

2016-04-27 9.3.389.9 Enhancement REST API The ObjectQueryManager service now supports multi-reflected multiple choice fields in the response returned on a query.

2016-03-30 9.3.362.9 Defect Services API The ObjectQueryResultSet class name has been updated with the correct spelling.

2016-03-30 9.3.362.9 Enhancement Services API Relativity admins can now create RDOs in the Admin Mode area. For more information, see Relativity Objects .

2016-03-02 9.3.332.21 Enhancement Services API The Services API now enables you to programmatically interact with the Relativity productions. For more information, see Production Manager (.NET) in the DTO reference.

2016-03-02 9.3.332.21 Enhancement Services API You can use the Services API to create, update, and delete production placeholders. For more information, see Production Placeholder Manager (.NET) .

2016-03-02 9.3.332.21 Enhancement REST API The REST API now allows you to programmatically interact with the Relativity productions. For more information, see Production Manager (REST) in the REST API reference.

2016-03-02 9.3.332.21 Enhancement REST API You can use the REST API to create, read, update, and delete production placeholders. For more information, see Production Placeholder Manager (REST) .

2016-03-02 9.3.332.21 Enhancement Processing API The Processing API includes the new SubmitInventoryJobsAsync() and SubmitPublishJobsAsync() methods used to perform inventory jobs and publish discovered data to a workspace respectively. See Get started with the Processing API .

2016-03-02 9.3.332.21 Enhancement Services API The DataResult object returned by the Object Query Manager service now contains the Includes property, which indicates the Field that was used to determine any related items added to your result set.

2015-11-23 9.3.242.6 Enhancement Processing API The new Processing API includes the Processing Custodian Manager, Processing Data Source Manager, Processing Set Manager, and Processing Job Manager services used to automate processing workflows. See Get started with the Processing API .

2015-11-23 9.3.242.6 Enhancement Services API The new Object Query Manager service queries for Document objects and Relativity Dynamic Objects (RDOs) in workspaces.

2015-11-23 9.3.242.6 Enhancement REST API The new Object Query Manager service queries for Document objects and Relativity Dynamic Objects (RDOs) in workspaces.

2015-11-23 9.3.242.6 Enhancement Services API The new Search Provider Manager service retrieves a list of active search providers in a workspace, which can be displayed in the Relativity UI framework.

2015-11-23 9.3.242.6 Enhancement REST API The new Search Provider Manager service retrieves a list of active search providers in a workspace, which can be displayed in the Relativity UI framework.

2015-11-23 9.3.242.6 Enhancement Services API The new Folder Manager service supports multiple operations for manipulating folder structures in the Relativity UI framework.

2015-11-23 9.3.242.6 Enhancement REST API The new Folder Manager service supports multiple operations for manipulating folder structures in the Relativity UI framework.

2015-11-23 9.3.242.6 Enhancement Services API Enhancements to the Pivot API include the new CreateProfileAsync() and UpdateProfileAsync() methods for creating or updating a pivot profile respectively. Additionally, the PivotIdToDisplayValueMap property on the PivotResultSet class is used to map column values to display values used in the Relativity UI when rendering data.

2015-11-23 9.3.242.6 Enhancement REST API Enhancements to the Pivot API include the new CreateProfileAsync() and UpdateProfileAsync() methods for creating or updating a pivot profile respectively.

2015-11-23 9.3.242.6 Enhancement Services API The Search Container Manager has the new GetSearchContainerTreeAsync() method used to render an expanded browser tree for a saved search.

2015-11-23 9.3.242.6 Enhancement REST API The Search Container Manager service now supports retrieving information on expanded nodes in a specified search container.

2015-11-23 9.3.242.6 Enhancement Services API The Query <T> class now has the SearchProviderCondition property, which is an object that holds the information necessary to run a query for the search provider used for pivoting on a base set of documents.

2015-11-23 9.3.242.6 Enhancement Event Handlers The event handler framework provides enhanced support for File fields, including a FileValue class, Modified Updated property on the FieldValue class, new properties on the FileFieldValue class, and modified Value property behavior on the FileFieldValue class. You can now access a file stream associated with a File field, so that you can read the contents of the stream, or provide a new stream. For more information, see Support for File fields .

2015-11-23 9.3.242.6 Enhancement REST API The text query condition now supports the Greater than ('Foo' > 'Bar') , Less than ('Foo' < 'Bar') , and Contains ('Foobar' CONTAINS 'Bar') operators.

2015-11-23 9.3.242.6 Enhancement Services API The TextConditionEnum enumeration now supports the Greater than ('Foo' > 'Bar') , Less than ('Foo' < 'Bar') , and Contains ('Foobar' CONTAINS 'Bar') query conditions for text.

2015-11-23 9.3.242.6 Enhancement Services API The CopyInstancesOnParentCopy property of the ObjectType DTO now allows you to set up an ObjectType to automatically copy the instances of an object when its parent object is copied..

2015-11-23 9.3.242.6 Enhancement API Helpers Added the IAPILog interface to API Helpers to enable access to the Relativity logging infrastructure from agents, custom pages, and event handlers. For more information, see Basic concepts for Relativity API Helpers and Logging .

2015-11-23 9.3.242.6 Full support Services API Permissions coverage through the Services API is out of technology preview and is now fully supported. For more information, see Permission Manager (.NET) .

2015-11-23 9.3.242.6 Full support REST API Permissions coverage through the REST API is out of technology preview and is now fully supported. For more information, see Permission Manager (.NET) .

2015-11-23 9.3.242.6 Enhancement Custom Pages To enhance the security of Relativity user interface, we have removed the session variables from custom pages. Instead, use the methods available in the Relativity API helper interfaces to obtain the information such as user context and current workspace ID. For more information, see Basic concepts for Relativity API Helpers .

2015-09-30 9.2.331.10 Defect Services API Corrected a problem with the CreateSingle() method for documents. The operation now correctly returns ArtifactID when creating a document where the identifier contains Unicode.

2015-08-26 9.2.296.16 Enhancement Services API Added the GetItemLevelSecurityListAsync() method of the IPermissionManager interface to return a collection of item-level security settings for a specified list of artifacts. For more information, see Enabling item-level security .

2015-07-29 9.2.271.9 Enhancement Services API Added the GetPermissionSelectedListAsync() method of the IPermissionManager interface to return a collection of permission values for the current user and a specified list of artifacts. For more information, see Read the current user and group permission values .

2015-05-30 9.2.190.9 Enhancement Services API Added a beta implementation of APIs that enable you to manage permissions and security for users, system admins, and individual objects, and to define custom permissions for Relativity Dynamic Objects (RDOs). For more information, see Permission Manager (.NET) .

2015-05-30 9.2.190.9 Enhancement Services API Added asynchronous operations for creating, reading, updating, deleting, and querying Client objects.

2015-05-30 9.2.190.9 Enhancement Services API Added asynchronous operations for creating, reading, updating, deleting, and querying Matter objects.

2015-05-30 9.2.190.9 Enhancement Services API Added asynchronous operations for reading and updating Message of the Day (MotD) objects.

2015-05-30 9.2.190.9 Enhancement Services API Added support for using SavedSearchCondition and ViewCondition conditions in compound queries.

2015-05-30 9.2.190.9 Enhancement Services API Added asynchronous operations for creating, reading, updating, deleting, and querying saved search folders.

2015-05-30 9.2.190.9 Enhancement Services API Added the Relativity.Services.Pivot namespace, which defines methods and classes for creating and running Pivot queries.

2015-05-30 9.2.190.9 Defect Services API Corrected a UTC translation problem in the DateTime query condition. The DateTime condition now evaluates only the date portion of a timestamp expression and ignores the time portion.

2015-05-30 9.2.190.9 Defect Services API Updated the Relativity installer to automatically install net.pipe and net.tcp bindings with WCF non-HTTP activation on agent servers.

2015-05-30 9.2.190.9 Enhancement REST API Added a beta implementation of APIs that enable you to manage permissions and security for users, system admins, and individual objects, and to define custom permissions for Relativity Dynamic Objects (RDOs). For more information, see Permission Manager (REST) .

2015-05-30 9.2.190.9 Enhancement REST API Added operations for creating, reading, updating, deleting, and querying Client objects.

2015-05-30 9.2.190.9 Enhancement REST API Added operations for creating, reading, updating, deleting, and querying Matter objects.

2015-05-30 9.2.190.9 Enhancement REST API Added operations for reading and updating Message of the Day (MotD) objects.

2015-05-30 9.2.190.9 Enhancement REST API Added support for using SavedSearchCondition and ViewCondition conditions in compound queries.

2015-05-30 9.2.190.9 Enhancement REST API Added operations for creating, reading, updating, deleting, and querying saved search folders.

2015-05-30 9.2.190.9 Enhancement REST API Added the Pivot Manager Service, which defines operations and fields for working with custom Pivot queries and Pivot profiles.

2015-05-30 9.2.190.9 Enhancement REST API Added support for the RelAuth cookie to custom pages. Custom pages can now "piggy back” on browser-based authentication when making calls to the REST API.

2015-05-30 9.2.190.9 Defect REST API Corrected the issue that removed white space between words in REST responses.

2015-05-30 9.2.190.9 Enhancement Import API Updated the importJob.Settings.DataGridIDColumnName property to support mapping documents to records in Data Grid.

2015-01-30 9.1.87.5 Enhancement Services API Updated the object hierarchy in the Relativity framework to support multi-tenancy. The Client object is now the parent of Matter, Group, User, and Workspace objects. This means that there is a new workflow for setting the Client property on a Group DTO. In addition, the Parent Artifact property on User and Workspace DTOs is now set to a Client object. For more information, see Client .

2015-01-28 9.0.285.3 Enhancement Services API Added full support for saved search APIs that were initially released in Relativity 9.0.198.5 as a Customer Technology Preview (CTP).

2015-01-28 9.0.285.3 Enhancement Services API Updated the architecture of Services API DLLs to deliver API functionality in multiple DLLs.

2015-01-28 9.0.285.3 Enhancement Services API Added support for accessing saved search APIs from agents, event handlers and custom pages.

2014-11-14 9.0.198.5 Enhancement Application Deployment System Added support for packaging saved searches in Relativity applications and deploying them through the Application Deployment System (ADS).

2014-11-14 9.0.198.5 Enhancement Application Deployment System Added support for assigning custom, user-friendly URLs to Relativity applications.

2014-11-14 9.0.198.5 Enhancement Application Deployment System Deprecated functionality for exporting applications as XML files. You can now export applications only as RAP files. In addition, applications developed in Relativity 9 or above can't be deployed to earlier versions, such as 8.2 or below, of Relativity.

2014-11-14 9.0.198.5 Enhancement Services API Added CTP implementations of APIs for creating, reading, updating, and deleting saved searches.

2014-11-14 9.0.198.5 Enhancement Services API Updated the ServiceFactory class to return proxies for any of the service interfaces in the Services API. You can use the class to create proxies for standalone .NET applications, specifying connection parameters in the associated ServiceFactorySettings class. API Helpers for event handlers, custom pages, and agents can also return any of the service interfaces in the Services API.

2014-11-14 9.0.198.5 Enhancement Services API Updated the Value property of SingleChoiceCondition or MultiChoiceCondition objects to support an array of GUIDs that represent the Choices to compare against, in addition to continuing support for setting the property to a list or an array of Integer values.

2014-11-14 9.0.198.5 Enhancement Services API Added the DefaultCacheLocation property to the Workspace DTO (kCura.Relativity.Client.DTOs namespace). You can use the property to get or set the ArtifactID of a server that’s designated as the default cache location for temporarily storing files for natives, images, and productions that are used by the viewer.

2014-11-14 9.0.198.5 Enhancement Services API Added the DefaultCacheLocation field to the WorkspaceFieldNames class (kCura.Relativity.Client.DTOs namespace). The field stores the Artifact ID of the server used to cache files.

2014-09-24 9.0.198.5 Enhancement Import API Updated various API components to improve performance significantly. You do not need to modify or update any existing code to leverage these enhancements.

2014-09-24 8.2.340.4 Enhancement Import API Significant performance enhancements, which you can leverage without making any modifications to your existing code.

2014-09-24 8.2.340.4 Enhancement Services API The RSAPI now uses HttpContext.Current.Items list instead of using data stored in the Session when making WebAPI and other calls.

2014-08-26 8.2.320.2 Defect Services API The GetRelativityScriptInputs() RSAPI method no longer returns incorrect results for Relativity script inputs.

2014-07-25 8.2.287.4 Defect Application Deployment System Default tabs can now be successfully imported through ADS.

2014-07-25 8.2.287.4 Defect Services API Blank GUID values no longer cause an error to be thrown when using the kCura.Client.DTO.FieldValue.AllFields directive to retrieve all fields.

2014-07-25 8.2.287.4 Defect Services API The admin choice enum has been updated and should be used in conjunction with the GetAdminChoiceTypes method to retrieve Artifact IDs for admin choices.

2014-07-25 8.2.287.4 Enhancement Application Deployment System Relativity applications can now optionally be assigned a short, user-friendly URL.

2014-05-30 8.2.231.1 Deprecation Services API CertificateFindValue property has been deprecated

2014-05-30 8.2.231.1 Enhancement Services API Using a ViewCondition and a Fields value of *SELECTEDFIELDS* in a query returns all expected Fields

2014-05-30 8.2.231.1 Enhancement Services API Using a ViewCondtion to retrieve multiple pages of results returns all values

2014-05-30 8.2.231.1 Enhancement Services API Executing a search with a condition using a GUID or Artifact ID

2014-05-30 8.2.231.1 Enhancement Services API Executing a Saved Search from an agent

2014-05-30 8.2.231.1 Enhancement Services API Querying with a sort containing an invalid Field fails consistently

2014-05-30 8.2.231.1 Enhancement Services API Setting choice values by GUID

2014-05-30 8.2.231.1 Enhancement Services API Querying for admin choices by Choice Type

2014-05-30 8.2.231.1 Enhancement Services API Updating a Client without the appropriate permissions fails with a valid exception

2014-05-30 8.2.231.1 Enhancement Services API Queries on fields recently added to an RDO or Document no longer fail

2014-05-30 8.2.231.1 Enhancement Services API Updating a Group without the proper permissions when no data is changing fails and throws a valid exception

2014-05-30 8.2.231.1 Enhancement Services API Querying a MultiObject Field with an ObjectConditionEnum.EqualTo condition fails with a valid error message

2014-05-30 8.2.231.1 Enhancement Services API Group names are validated consistently

2014-05-30 8.2.231.1 Enhancement Services API User emails addresses are validated consistently

2014-05-30 8.2.231.1 Enhancement Services API Attempting to create an object with an invalid WorkspaceID returns a valid error message

2014-05-30 8.2.231.1 Enhancement Services API Reading a Document with StrictMode disabled no longer returns reflected Batch fields

2014-05-30 8.2.231.1 Enhancement Services API ViewCondition queries are sorted by the View sort

2014-05-30 8.2.231.1 Enhancement Services API Deleting objects respects dependencies

2014-05-30 8.2.231.1 Enhancement Services API ‘User’ field permissions are validated consistently on RDO creation

2014-05-30 8.2.231.1 Enhancement Services API FieldType attribute on ‘Client’ field of User object is consistent

2014-05-30 8.2.231.1 Enhancement Services API FieldType attribute on ‘Object Type’ field is consistent

2014-05-30 8.2.231.1 Enhancement Services API FieldType attribute on ‘System Created By’ and ‘System Last Modified By’ fields is consistent

2014-05-30 8.2.231.1 Deprecation Services API Services API untyped create, read, update, delete, and query operations have been deprecated.

2014-05-30 8.2.231.1 Enhancement Services API A system admin Platform Status tab has been added to monitor and display the status of the Relativity API endpoints.

2014-05-30 8.2.231.1 Enhancement Services API Index methods have been added to the Fields collection so that fields can be easily retrieved by ID, Name, or GUID.

2014-05-30 8.2.231.1 Enhancement Services API A simplified pattern for performing an operation with a single artifact has been added.

2014-05-30 8.2.231.1 Enhancement Services API Using the Services API instead of SQL, users can create, update, and delete choices.

2014-05-30 8.2.231.1 Enhancement Services API Using the Services API instead of SQL, users can create, update, and delete workspaces.

2014-05-30 8.2.231.1 Enhancement Services API A new property for getting back the user ID number for the currently logged in user has been added to the API helpers.

2014-09-22 8.1.491.2 Defect Services API The RSAPI now uses HttpContext.Current.Items list instead of using data stored in the Session when making WebAPI and other calls.

2014-08-26 8.1.474.2 Defect Services API The GetRelativityScriptInputs() RSAPI method no longer returns incorrect results for Relativity script inputs.

2014-07-25 8.1.441.2 Defect Services API Blank GUID values no longer cause an error to be thrown when using the kCura.Client.DTO.FieldValue.AllFields directive to retrieve all fields.

2014-07-25 8.1.441.2 Enhancement Application Deployment System Relativity applications can now optionally be assigned a short, user-friendly URL.

2014-01-29 8.1.264.1 Defect Services API A permission error will now be returned when a non-system admin user queries Relativity Scripts using the Services API.

2014-01-29 8.1.264.1 Defect Services API Deleted workspaces are no longer returned when querying through the Services API before the Case Manager agent runs.

2014-01-29 8.1.264.1 Enhancement Application Deployment System Relativity now supports applications up to 1 GB in size.

2013-12-23 8.1.225.2 Defect Services API Tokens are now removed on a regular interval, instead of every time a Dispose() method is called in the Services API.

2013-12-20 8.1.223.7 Defect Services API Logging in to the Services API via Integrated HTTPS will no longer fail when the client is on a different machine than the server.

2013-12-04 8.1.202.3 Defect Import API Import API folder creation now occurs server-side to avoid folder name collisions.

2013-11-26 8.1.200.2 Defect Services API Previously, a timeout occurred when using the Relativity Services API to update a multi-object field associated with documents in very large workspaces. A WHERE clause has now been added to the query in order to prevent a timeout.

2013-11-26 8.1.200.2 Defect Application Deployment System The "Enable Snapshot Auditing on Delete" property can now be edited, even if the object is part of a locked application.

2013-11-20 8.1.195.1 Defect Services API Self-hosted Services API instances in agents now correctly construct the URI, preventing a failed connection.

2013-11-08 8.1.182.3 Enhancement Application Deployment System A new configuration value,AuditApplicationUninstallEnabled, controls whether or not delete audits are logged when uninstalling an application. Setting this value to No may improve application uninstall speeds in your case.

2013-11-08 8.1.182.3 Enhancement Application Deployment System A new Workspace Create event handler type has been added for use when you want to run custom logic when creating a new workspace.

2013-11-08 8.1.182.3 Enhancement Application Deployment System You can now easily and completely uninstall Relativity applications from a workspace.

2013-11-08 8.1.182.3 Enhancement Application Deployment System You can attach uninstall event handlers to Relativity Applications to perform custom actions prior to the standard application uninstall process.

2013-11-08 8.1.182.3 Enhancement Application Deployment System You can include pre- and post-install event handlers in an application to perform custom actions during the deployment of your application.

2013-11-08 8.1.182.3 Enhancement Application Deployment System You can no longer lock applications that contain errors.

2013-11-08 8.1.182.3 Defect Custom Pages A user can now view a custom page from more than one Relativity session at the same time.

2013-11-08 8.1.182.3 Defect Custom Pages Previously, after upgrading Relativity, library DLLs were not automatically upgraded for custom pages. Now Procuro will automatically reset all applications if the Relativity version changes, and the custom page manager will refresh the library files.

2013-11-08 8.1.182.3 Enhancement Event Handlers A new page interaction event handler has been created, which can be used to insert JavaScript and CSS easily on a page.

2013-11-08 8.1.182.3 Enhancement Import API Performance has been improved for multiple threads using a single Import API.

2013-11-08 8.1.182.3 Enhancement Import API Folder creation now occurs server-side to avoid folder name collisions.

2013-11-08 8.1.182.3 Enhancement Import API An option has been exposed to specify an overlay identifier on import.

2014-06-25 8.0.291.1 Defect Services API Searching by user ID against a user field with an ""is equal to"" condition via the Services API no longer causes a read failed error.

2014-06-25 8.0.219.1 Defect Custom Pages Custom page deployment no longer fails when the default IIS website is not named "Default Web Site."

2014-06-25 8.0.247.1 Defect Application Deployment System When a reflected single-choice field is removed from an application, but the associated field remains, the choices are no longer deleted. Additionally, the application layout will now properly update the list of single-choice fields without requiring a page refresh.

2014-06-25 8.0.247.1 Defect Import API Performance has been improved for multiple threads using a single Import API.

2014-06-25 8.0.260.5 Defect Application Deployment System When exporting an application, the Visible in Dropdown view setting will now be preserved.

2014-06-25 8.0.291.1 Defect Services API Document.Read() now only retrieves the fields and choices specified by the user.

2014-06-25 8.0.302.1 Defect Services API The login database table and cache are now kept in sync to prevent avoid authentication errors when logging back in to the Services API after a period of inactivity.

2014-06-25 8.0.302.1 Defect Services API GenerateRelativityAuthenticationToken now automatically authenticates Services API users.

2014-06-25 8.0.302.1 Defect Import API Native file and object importing has been optimized for the Import API by improving the creation of temporary tables.

2014-06-25 8.0.316.2 Defect Services API Using the RSAPIClient or ArtifactManagerProxy, the channel cache now allows you to connect to more than one Services API server from a single application.

2014-06-25 8.0.233.1 Defect Event Handlers When creating event handlers, checking if values are selected for a multi-object field on a layout now returns the correct result.

2014-06-25 8.0.233.1 Defect Services API The Services API programming samples now point to the correct folders to access third-party DLL files after the Relativity SDK is installed.

2014-06-25 8.0.233.1 Defect Services API The Services API no longer requires HTTPS to be configured on the Services API server when using NetNamedPipes or NetTCP to transmit metadata.

2014-06-25 8.0.291.1 Defect Application Deployment System Fields and objects can now be renamed when upgrading locked applications that conflict with themselves.

2014-01-29 8.0.428.2 Defect Services API A permission error will now be returned when a non-system admin user queries Relativity Scripts using the Services API.

2014-01-29 8.0.428.2 Defect Services API Deleted workspaces are no longer returned when querying through the Services API before the Case Manager agent runs.

2013-12-19 8.0.387.6 Defect Services API Logging into the Services API via Integrated HTTPS will no longer fail when the client is on a different machine than the server.

2013-12-04 8.0.373.1 Defect Import API Import API folder creation now occurs server-side to avoid folder name collisions.

2013-12-04 8.0.373.1 Defect Services API Tokens are now removed on a regular interval, instead of every time a Dispose() method is called.

2013-11-26 8.0.358.1 Defect Services API Previously, a timeout occurred when using the Relativity Services API to update a multi-object field associated with documents in very large workspaces. A WHERE clause has now been added to the query in order to prevent a timeout.

2013-11-26 8.0.358.1 Defect Application Deployment System The "Enable Snapshot Auditing on Delete" property can now be edited, even if the object is part of a locked application.

2013-10-09 8.0.316.2 Defect Services API Using the RSAPIClient or ArtifactManagerProxy, the channel cache now allows you to connect to more than one Services API server from a single application.

2013-09-25 8.0.302.1 Defect Services API GenerateRelativityAuthenticationToken now automatically authenticates Services API users.

2013-09-25 8.0.302.1 Defect Services API The login database table and cache are now kept in sync to prevent avoid authentication errors when logging back in to the Services API after a period of inactivity.

2013-09-25 8.0.302.1 Enhancement Import API Native file and object importing has been optimized for the Import API by improving the creation of temporary tables.

2013-09-13 8.0.291.1 Defect Application Deployment System Fields and objects can now be renamed when upgrading locked applications that conflict with themselves.

2013-09-13 8.0.291.1 Enhancement Services API The Services API has been updated to simplify configuration, increase performance, and provide an easier environment for developers. No code changes are required to take advantage of the new API, but any external applications that package their own client DLL must be recompiled with the new Services API client.

2013-09-13 8.0.291.1 Defect Services API Document.Read() now only retrieves the fields and choices specified by the user.

2013-09-13 8.0.291.1 Defect Services API Searching by user ID against a user field with an "is equal to" condition via the Services API no longer causes a read failed error.

2013-08-14 8.0.260.5 Defect Application Deployment System When exporting an application, the Visible in Dropdown view setting will now be preserved.

2013-07-31 8.0.247.1 Defect Application Deployment System When a reflected single-choice field is removed from an application, but the associated field remains, the choices are no longer deleted. Additionally, the application layout will now properly update the list of single-choice fields without requiring a page refresh.

2013-07-31 8.0.247.1 Defect Import API Performance has been improved for multiple threads using a single Import API.

2013-07-31 8.0.247.1 Defect Import API Folder creation now occurs server-side to avoid folder name collisions.

2013-07-31 8.0.247.1 Defect Import API An option has been exposed to specify an overlay identifier on import.

2013-07-17 8.0.233.1 Defect Services API The Services API no longer requires HTTPS to be configured on the Services API server when using NetNamedPipes or NetTCP to transmit metadata.

2013-07-17 8.0.233.1 Defect Services API The Services API programming samples now point to the correct folders to access third-party DLL files after the Relativity SDK is installed.

2013-07-17 8.0.233.1 Defect Event Handlers When creating event handlers, checking if values are selected for a multi-object field on a layout now returns the correct result.

2013-07-03 8.0.219.1 Defect Custom Pages Custom page deployment no longer fails when the default IIS website is not named "Default Web Site."

2013-07-03 8.0.219.1 Defect Services API Searching by user ID against a user field with an "is equal to" condition via the Services API no longer causes a read failed error.

2013-05-10 8.0.165.3 Enhancement Application Deployment System Assemblies have been renamed to resource files.

2013-05-10 8.0.165.3 Enhancement Application Deployment System You can safely load different versions of third party vendor assemblies in your environment. Each assembly (resource file) you upload must be attached to a Relativity Application. A new application domain will be created for each application type in your environment, and all associated resource files will be isolated from each other.

2013-05-10 8.0.165.3 Enhancement Application Deployment System You can add an application to the master application library directly from your workspace using the new Push to Library button on the Relativity Application console.

2013-05-10 8.0.165.3 Enhancement Event Handlers You can include pre and post install event handlers in an application to perform custom actions during the deployment of your application.

2013-05-10 8.0.165.3 Defect Application Deployment System Fixed an issue where users not in the System Administrator group could not export applications, even if they had the appropriate permissions.

2013-05-10 8.0.165.3 Enhancement Services API Relativity 8 provides a community preview of a new REST API that offers a subset of the functionality of the Services API (RSAPI), but allows for simple, cross-platform development.

2013-05-10 8.0.165.3 Enhancement Services API The ArtifactManagerProxy class now includes a new method for logging in to Relativity that provides functionality for using Relativity credentials with Net.Pipe.

2013-05-10 8.0.165.3 Enhancement Services API The Username/Password authentication scheme is now supported with the Net Named Pipes protocol.

2013-05-10 8.0.165.3 Enhancement Services API The ArtifactManagerProxy class now includes a method for creating objects that populates the Results property with success and failure information, even in the case of a partial failure.

2013-05-10 8.0.165.3 Enhancement Services API The ArtifactManagerProxy class now includes a method for deleting all artifacts of a specific type.

2013-05-10 8.0.165.3 Enhancement Services API The ArtifactManagerProxy class now includes a method for deleting specified artifacts of a specifc type.

2013-05-10 8.0.165.3 Enhancement Services API The ArtifactManagerProxy class now includes a new method for deleting all documents in a workspace.

2013-05-10 8.0.165.3 Enhancement Services API The human readable string for ObjectType's "Artifact Type ID" was changed to "Descriptor Artifact Type ID" to prevent some naming collisions.

2013-05-10 8.0.165.3 Enhancement Services API MassCreate and MassEdit now generate a SqlException of "Some supplied choice ids are invalid" if invalid choice ids are provided.

2013-05-10 8.0.165.3 Enhancement Services API Metadata is now always retrieved over the same endpoint over which client communication takes place.

2013-05-10 8.0.165.3 Enhancement Services API A new Relativity API provides a standard interface for establishing connections to databases and the Services API. This API also includes helper methods and unit testing tools that you can program against when developing agents, custom pages, and event handlers.

2013-05-10 8.0.165.3 Enhancement Services API Relativity 8 provides a newer REST API that offers parity in functionality with the Relativity Services API (RSAPI) but allows simple, fast, cross-platform development.

2013-05-10 8.0.165.3 Enhancement Services API Relativity 8 has a new database configuration value called DeveloperMode. When enabled, this changes the behavior of Relativity in a development environment.

2013-05-10 8.0.165.3 Enhancement Application Deployment System You can include pre and post install event handlers in an application to perform custom actions during the deployment of your application.

2014-08-26 7.5.634.47 Defect Services API The GetRelativityScriptInputs() RSAPI method no longer returns incorrect results for Relativity script inputs.

2014-07-25 7.5.634.30 Defect Services API Blank GUID values no longer cause an error to be thrown when using the kCura.Client.DTO.FieldValue.AllFields directive to retrieve all fields.

2014-06-25 7.5.632.40 Defect Services API Searching by user ID against a user field with an ""is equal to"" condition via the Services API no longer causes a read failed error.

2014-06-25 7.5.632.40 Defect Custom Pages Custom page deployment no longer fails when the default IIS website is not named "Default Web Site."

2014-06-25 7.5.632.58 Defect Application Deployment System When a reflected single-choice field is removed from an application, but the associated field remains, the choices are no longer deleted. Additionally, the application layout will now properly update the list of single-choice fields without requiring a page refresh.

2014-06-25 7.5.632.58 Defect Import API Performance has been improved for multiple threads using a single Import API.

2014-06-25 7.5.632.58 Defect Application Deployment System When exporting an application, the Visible in Dropdown view setting will now be preserved.

2014-06-25 7.5.632.68 Defect Services API Document.Read() now only retrieves the fields and choices specified by the user.

2014-06-25 7.5.632.83 Defect Services API The login database table and cache are now kept in sync to prevent avoid authentication errors when logging back in to the Services API after a period of inactivity.

2014-06-25 7.5.632.92 Defect Services API GenerateRelativityAuthenticationToken now automatically authenticates Services API users.

2014-06-25 7.5.632.92 Defect Import API Native file and object importing has been optimized for the Import API by improving the creation of temporary tables.

2014-06-25 7.5.633.12 Defect Services API Using the RSAPIClient or ArtifactManagerProxy, the channel cache now allows you to connect to more than one Services API server from a single application.

2014-06-25 7.5.630.13 Defect Application Deployment System A new Object Rule Type, ""Mass Action Visiblity"", is available to hide the Edit, Replace, or Copy options from the Mass Actions list for any dynamic Object.

2014-06-25 7.5.630.13 Defect Application Deployment System A new Object Rule Type, ""Custom Single Object Add Link Visibility"", is available to control when the hyperlinked Add option is available on Layouts for Single Object fields.

2014-06-25 7.5.630.13 Defect Application Deployment System Relativity no longer unlinks multiple object instances from custom objects after an application upgrade. Instead, user-set multiple object instances will remain linked to custom objects after upgrading an application, regardless of how instances are linked in the application package.

2014-06-25 7.5.630.13 Defect Application Deployment System Session IDs and authentication tokens are now hashed with the SHA1 hashing algorithm before being stored in the Relativity database.

2014-06-25 7.5.630.13 Defect Application Deployment System Users can now set up contextual help on custom object layout categories.

2014-06-25 7.5.630.13 Defect Application Deployment System The Application Install Manager agent has been renamed to the Custom Page Installation Manager. The ApplicationInstallManagerIsOffHourAgent configuration value has also been renamed to CustomPageInstallationManagerIsOffHourAgent.

2014-06-25 7.5.630.13 Defect Application Deployment System You can now connect to SQL via a database connection property on kCura.Agent.AgentBase.

2014-06-25 7.5.630.13 Defect Application Deployment System Company Name, Copyright, and Description information can now be included on all assemblies, agent types, and event handlers. Company Name and Copyright are attributes that can be added to the assembly itself, while Description information can be added individually to each event handler or agent type in an assembly.

2014-06-25 7.5.630.13 Defect Application Deployment System The Mass Action Visibility object rule now includes an option to hide the "copy" mass action.

2014-06-25 7.5.630.13 Defect Import API The Import API now supports mapping to single-object and multi-object field values by Artifact ID.

2014-06-25 7.5.630.28 Defect Services API The Services API has been updated to allow authentication over HTTP when the CertificateFindValue is set in the app.config file.

2014-06-25 7.5.630.50 Defect Services API The correct data is now returned when querying the Services API for a multi-object field that references objects of the same type, or for documents with relational fields.

2014-06-25 7.5.630.50 Defect Services API The Services API query now filters saved searches correctly using the search text.

2014-06-25 7.5.630.50 Defect Services API Compiling the Relativity SDK sample solution no longer returns NUnit and assembly errors.

2014-06-25 7.5.630.82 Defect Application Deployment System An error is no longer displayed when importing an application with reflected choice fields.

2014-06-25 7.5.630.82 Defect Services API The Relativity Services API no longer displays an error following a first-time installation of 7.5 because of an invalid entry in the web configuration file.

2014-06-25 7.5.630.82 Defect Services API When using the RSAPI to query for artifacts, the artifact ID and GUID are now populated for each field in the query artifact fields collection.

2014-06-25 7.5.630.94 Defect Services API The Services API can now retrieve a Relativity authentication token for use during login.

2014-06-25 7.5.630.94 Defect Services API The Mass Edit command in the Services API no longer returns an error when trying to mass edit Yes/No fields.

2014-06-25 7.5.631.14 Defect Application Deployment System An intermittent HTTP error message no longer occurs when installing a new Relativity Application.

2014-06-25 7.5.631.33 Defect Services API Running a query through the Services API now returns field names with the appropriate spacing.

2014-06-25 7.5.631.33 Defect Services API When StrictMode is set to True, the field names used in fields selection, sorts, and conditions are no longer case-sensitive.

2014-06-25 7.5.631.48 Defect Services API TotalCount is now returned properly when querying objects that do not support paging through the Services API.

2014-06-25 7.5.631.48 Defect Services API An error is no longer returned when executing a saved search via the Services API while using a custom agent.

2014-06-25 7.5.631.63 Defect Services API The Services API no longer allows users to create a batch set based on saved searches they don't have permission to access.

2014-06-25 7.5.631.63 Defect Services API The Services API can now successfully query documents using the ArtifactGUID of a relational field.

2014-06-25 7.5.631.63 Defect Services API The Services API now allows creation of a document or RDO using its ArtifactTypeGUID.

2014-06-25 7.5.631.63 Defect Services API The Services API now correctly creates a document in the folder specified by the ParentArtifactID.

2014-06-25 7.5.631.63 Defect Services API The Services API now validates the FolderID to prevent creation of documents with an invalid FolderID.

2014-06-25 7.5.631.63 Defect Import API The RDC and Application Deployment System using the Import API can now run multiple imports concurrently without an error occurring when the imports create single- or multiple-object fields.

2014-06-25 7.5.631.83 Defect Services API An error is no longer returned when creating an RDO using the ExecuteBatch command.

2014-06-25 7.5.631.83 Defect Services API "The Services API now displays a more intuitive error message for the following actions: • Querying Artifact Type names longer than 50 characters. • Querying object types with a workspace ID equal to -1. • Creating or deleting objects with invalid authentication tokens.

2014-06-25 7.5.632.20 Defect Import API When multiple threads are imported using a single Import API, the temporary folder is no longer shared between all of the threads.

2014-06-25 7.5.632.3 Defect Services API The artifact type for the ParentArtifactID is now validated when creating a child RDO.

2014-06-25 7.5.632.3 Defect Services API When creating a child RDO, the Services API now automatically generates the Parent Object required field using the ParentArtifactID property.

2014-06-25 7.5.632.3 Defect Import API The Import API can now be installed on 32-bit machines using the Relativity SDK installer.

2014-06-25 7.5.632.40 Defect Services API The Services API client no longer leaves connections open if it fails while closing a faulted channel.

2014-01-29 7.5.633.46 Defect Services API Deleted workspaces are no longer returned when querying through the Services API before the Case Manager agent runs.

2014-01-29 7.5.633.46 Defect Services API A permission error will now be returned when a non-system admin user queries Relativity Scripts using the Services API.

2013-12-18 7.5.633.36 Defect Services API Logging into the Services API via Integrated HTTPS will no longer fail when the client is on a different machine than the server.

2013-11-20 7.5.633.28 Defect Services API Previously, a timeout occurred when using the Relativity Services API to update a multi-object field associated with documents in very large workspaces. A WHERE clause has now been added to the query in order to prevent a timeout.

2013-10-09 7.5.633.12 Defect Services API Using the RSAPIClient or ArtifactManagerProxy, the channel cache now allows you to connect to more than one Services API server from a single application.

2013-09-25 7.5.632.92 Enhancement Import API Native file and object importing has been optimized for the Import API by improving the creation of temporary tables.

2013-09-25 7.5.632.92 Defect Services API GenerateRelativityAuthenticationToken now automatically authenticates Services API users.

2013-09-25 7.5.632.92 Defect Services API The login database table and cache are now kept in sync to prevent avoid authentication errors when logging back in to the Services API after a period of inactivity.

2013-09-13 7.5.632.83 Enhancement Services API The Services API has been updated to simplify configuration, increase performance, and provide an easier environment for developers. No code changes are required to take advantage of the new API, but any external applications that package their own client DLL must be recompiled with the new Services API client.

2013-09-13 7.5.632.83 Defect Services API Document.Read() now only retrieves the fields and choices specified by the user.

2013-08-14 7.5.632.68 Defect Application Deployment System When exporting an application, the Visible in Dropdown view setting will now be preserved.

2013-07-31 7.5.632.58 Defect Import API Performance has been improved for multiple threads using a single Import API.

2013-07-31 7.5.632.58 Defect Import API Folder creation now occurs server-side to avoid folder name collisions.

2013-07-31 7.5.632.58 Defect Import API An option has been exposed to specify an overlay identifier on import.

2013-07-31 7.5.632.58 Defect Application Deployment System When a reflected single-choice field is removed from an application, but the associated field remains, the choices are no longer deleted. Additionally, the application layout will now properly update the list of single-choice fields without requiring a page refresh.

2013-07-03 7.5.632.40 Defect Custom Pages Custom page deployment no longer fails when the default IIS website is not named "Default Web Site."

2013-07-03 7.5.632.40 Defect Services API Searching by user ID against a user field with an "is equal to" condition via the Services API no longer causes a read failed error.

2013-07-03 7.5.632.40 Defect Services API The Services API client no longer leaves connections open if it fails while closing a faulted channel.

2013-05-22 7.5.632.3 Defect Import API The Import API can now be installed on 32-bit machines using the Relativity SDK installer.

2013-05-22 7.5.632.3 Defect Services API When creating a child RDO, the Services API now automatically generates the Parent Object required field using the ParentArtifactID property.

2013-05-22 7.5.632.3 Defect Services API The artifact type for the ParentArtifactID is now validated when creating a child RDO.

2013-06-05 7.5.632.20 Defect Import API When multiple threads are imported using a single Import API, the temporary folder is no longer shared between all of the threads.

2013-05-08 7.5.631.83 Defect Services API The Services API now displays a more intuitive error message for the following actions:•Querying Artifact Type names longer than 50 characters.•Querying object types with a workspace ID equal to -1.•Creating or deleting objects with invalid authentication tokens.

2013-05-08 7.5.631.83 Defect Services API An error is no longer returned when creating an RDO using the ExecuteBatch command.

2013-04-24 7.5.631.63 Defect Import API The RDC and applications using the Import API can now run multiple imports concurrently without an error occurring when the imports create single- or multiple-object fields.

2013-04-24 7.5.631.63 Defect Services API The Services API now validates the FolderID to prevent creation of documents with an invalid FolderID.

2013-04-24 7.5.631.63 Defect Services API The Services API now correctly creates a document in the folder specified by the ParentArtifactID.

2013-04-24 7.5.631.63 Defect Services API The Services API now allows creation of a document or RDO using its ArtifactTypeGUID.

2013-04-24 7.5.631.63 Defect Services API The Services API can now successfully query documents using the ArtifactGUID of a relational field.

2013-04-24 7.5.631.63 Defect Services API The Services API no longer allows users to create a batch set based on saved searches they don't have permission to access.

2013-04-10 7.5.631.48 Defect Services API An error is no longer returned when executing a saved search via the Services API while using a custom agent.

2013-04-10 7.5.631.48 Defect Services API TotalCount is now returned properly when querying objects that do not support paging through the Services API.

2013-03-27 7.5.631.33 Defect Services API When StrictMode is set to True, the field names used in fields selection, sorts, and conditions are no longer case-sensitive.

2013-03-27 7.5.631.33 Defect Services API Running a query through the Services API now returns field names with the appropriate spacing.

2013-03-13 7.5.631.14 Defect Application Deployment System An intermittent HTTP error message no longer occurs when installing a new Relativity Application.

2013-02-27 7.5.630.94 Defect Services API The Mass Edit command in the Services API no longer returns an error when trying to mass edit Yes/No fields.

2013-02-27 7.5.630.94 Defect Services API The Services API can now retrieve a Relativity authentication token for use during login.

2013-02-13 7.5.630.82 Defect Services API When using the RSAPI to query for artifacts, the artifact ID and GUID are now populated for each field in the query artifact fields collection.

2013-02-13 7.5.630.82 Defect Services API The Relativity Services API no longer displays an error following a first-time installation of 7.5 because of an invalid entry in the web configuration file.

2013-02-13 7.5.630.82 Defect Application Deployment System An error is no longer displayed when importing an application with reflected choice fields.

2013-01-16 7.5.630.50 Defect Services API Compiling the Relativity SDK sample solution no longer returns NUnit and assembly errors.

2013-01-16 7.5.630.50 Defect Services API The Services API query now filters saved searches correctly using the search text.

2013-01-16 7.5.630.50 Defect Services API The correct data is now returned when querying the Services API for a multi-object field that references objects of the same type, or for documents with relational fields.

2012-12-19 7.5.630.28 Defect Services API The Services API has been updated to allow authentication over HTTP when the CertificateFindValue is set in the app.config file.

2012-11-30 7.5.630.13 Enhancement Import API The Import API now supports mapping to single-object and multi-object field values by Artifact ID.

2012-11-30 7.5.630.13 Enhancement Application Deployment System The Mass Action Visibility object rule now includes an option to hide the "copy" mass action.

2012-11-30 7.5.630.13 Enhancement Application Deployment System Company Name, Copyright, and Description information can now be included on all assemblies, agent types, and event handlers. Company Name and Copyright are attributes that can be added to the assembly itself, while Description information can be added individually to each event handler or agent type in an assembly.

2012-11-30 7.5.630.13 Enhancement Application Deployment System You can now connect to SQL via a database connection property on kCura.Agent.AgentBase.

2012-11-30 7.5.630.13 Enhancement Application Deployment System The Application Install Manager agent has been renamed to the Custom Page Installation Manager. The ApplicationInstallManagerIsOffHourAgent configuration value has also been renamed to CustomPageInstallationManagerIsOffHourAgent.

2012-11-30 7.5.630.13 Enhancement Application Deployment System Users can now set up contextual help on custom object layout categories.

2012-11-30 7.5.630.13 Enhancement Application Deployment System Session IDs and authentication tokens are now hashed with the SHA1 hashing algorithm before being stored in the Relativity database.

2012-11-30 7.5.630.13 Enhancement Application Deployment System Relativity no longer unlinks multiple object instances from custom objects after an application upgrade. Instead, user-set multiple object instances will remain linked to custom objects after upgrading an application, regardless of how instances are linked in the application package.

2012-11-30 7.5.630.13 Enhancement Application Deployment System A new Object Rule Type, "Custom Single Object Add Link Visibility", is available to control when the hyperlinked Add option is available on Layouts for Single Object fields.

2012-11-30 7.5.630.13 Enhancement Application Deployment System A new Object Rule Type, "Mass Action Visiblity", is available to hide the Edit, Replace, or Copy options from the Mass Actions list for any dynamic Object.

On this page

- Platform change log (Archive)


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

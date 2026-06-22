---
title: "Platform change log"
url: https://platform.relativity.com/Server2025/Content/What_s_new/Platform_change_log.htm
collection: developer
fetched_at: 2026-06-22T06:21:49+00:00
sha256: 205d8a574ba2c482765a3ac6f093864697b617fbd1e17373e457fe3db534aa76
---

Platform change log Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Platform change log

This change log represents changes that may affect Relativity Developers, such as changes to APIs, deprecation of APIs, new APIs and other developer-focused changes. See the User Guide for version release notes .

## Released Changes

You can use the following table to find changes for a specific Relativity version, API, or other value. To filter the data in the table, select a value from a drop-down in the column header (Release, Type, and Feature) or type in the Search field. To sort, click the column name. For changes prior to 2019-01-01, please refer to the Platform change log (Archive)

Date Release Type Feature Change

2025-12-15 Server 2025 Change SDK Version Increment See the SDK and API comparison topic for SDK/API versions for RelativityOne, Relativity Server 2025 and Relativity Server 2024.

2025-12-15 Server 2025 Enhancement Import-Export Customized tab icon supported during import and export of workspaces.

2025-12-15 Server 2025 Enhancement RSMF Added RSMF Slicing API to create a new document based on a subset of events in a short message document.

2024-09-06 Server 2024 Enhancement APIs API versions are incremented for Relativity Server 2024. See the topic SDK and API Comparison for version number information.

2024-09-06 Server 2024 Deprecation Local Debugger The Local Debugger Visual Studio extension will no longer be supported effective with the Relativity Server 2024 release. The Local Debugger will still be supported for Relativity Server 2022 and 2023 until official support for each release expires. See this post in the developer group for more information.

2024-05-20 CI/CD Deprecation API Explorer The API Explorer application is no longer supported for RelativityOne nor Relativity Server as of May 20, 2024. All supporting documentation and access to the RAP file has been removed, and no further changes will be made to the application. See this post in the developer group for more information.

2024-01-15 CI/CD Enhancement Documentation The Relativity Server 2023 Developer Documentation site has been significantly updated to better support Relativity developers. See this announcement for more information.

2023-09-15 Server 2023 Enhancement NuGet Packages Effective with the Relativity Server 2023 release, the NuGet packages required to extend core functionality and implement custom applications for Relativity Server are published and maintained separately from the SDKs hosted on the Relativity NuGet Gallery. The latest SDKs for Relativity Server will be hosted in a separate repository, while the Relativity NuGet Gallery is now considered the repository for RelativityOne packages. See the Relativity Server 2023 Developer News topic for more information.

2023-09-15 Server 2023 Deprecation RSAPI RSAPI has been removed in the Relativity Server 2023 release. See RSAPI deprecation process for more information, including the replacement APIs

2023-09-15 Server 2023 Deprecation Classic Viewer

Classic Viewer has been removed in the Relativity Server 2023 release. Viewer extensions that only work with the Classic Viewer will no longer be functional. If you have not already done so, you will need to migrate your classic viewer extension code to the Review APIs. See Viewer Extension Migration Guide for more details.

2022-09-28 N/A Deprecation Imaging Set Scheduler The Imaging Set Scheduler application has been updated to remove RSAPI dependencies, but the application will not be updated further. The source code for Imaging Set Scheduler is now available as an open-source project and available on Github so that you may customize the code to extend your Relativity Server environments. You can access the documentation for Imaging Set Scheduler here .

2022-02-15 Server 2022 Enhancement Search Terms Report Services API The Search Terms Report Services API is now versioned. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.SearchTermsReports.V1.Interfaces. The URLs used through REST also include these updates, as exemplified by relativity-search-terms-report/v1/. This API also includes multiple enhancements, such as methods for create and update operations on search terms. For more information, see Search Terms Report Services (.NET) and Search Terms Report Services (REST) .

2022-03-21 Server 2022 Enhancement Relativity Review API The Review API and Review Extension framework are now compatible with Relativity Server 2022 (Osier 12.1). For more information, see Review API site .

2021-10-23 12.3.149.23 Enhancement Structured Analytics Job Manager API

The Structured Analytics Job Manager is now versioned. The related namespaces have been updated to include the business domain and version number, as exemplified by Relativity.StructuredAnalytics.V1 . The URLs used through REST also include these updates, as exemplified by relativity-structured-analytics/v1 . Additionally,the CancelAndWaitAsync() method and related endpoint in REST are no longer supported. The GetStatusAsync method and related endpoint in REST are now used to check the status of a structured analytics set. The ProgressReport object is no longer supported as a parameter on any methods. For more information, see Structured Analytics Job Manager (.NET) and Structured Analytics Job Manager (REST) .

2021-10-23 12.3.149.23 Deprecation Classic Viewer Classic Viewer is deprecated with the Sundrop release (12.3). Viewer extensions that only work with the Classic Viewer will no longer be accessible. Extension code will need to be migrated to the Review API to remain operational. See the Viewer Extension Migration Guide for more information.

2021-07-31 12.2.168.12 Enhancement Relativity Document Viewer SDK The new Annotations Manager API supports programmatically redacting and highlighting document images. It contains methods for creating, updating, retrieving, and deleting redactions and highlights. This versioned API exposes the methods for annotations on IAnnotationServiceManager interface in the Relativity.DocumentViewer.Services.Versioned.<VersionNumber> namespace. The Annotations Manager service exposes endpoints through REST with same functionality. For more information, see Annotations Manager (.NET) and see Annotations Manager (REST) .

2021-07-31 12.2.168.12 Deprecation RelativityOne SDK As of the Prairie Smoke release, the Relativity SDK MSI installer is no longer available for download. You can obtain the Relativity HTTP APIs by downloading the .NET packages from NuGet, or by using the corresponding REST services

2022-03-21 Server 2022 Enhancement Relativity Document Viewer SDK The new Short Message Viewer Manager API supports programmatically interacting with messages displayed in the Short Message Viewer in the Relativity UI. It exposes methods for retrieving the JSON, attachments, and participant information for short messages. It also provides endpoints for validating the Relativity Short Message Format (RSMF) and creating new documents based on a subset of messages. This versioned API exposes the methods on the IShortMessageViewerManager interface available in the Relativity.DocumentViewer.SDK. The Short Message Viewer Manager service exposes endpoints through REST with the same functionality as available through .NET. For more information, see Short Message Viewer Manager (.NET) and Short Message Viewer Manager (REST) .

2022-03-21 Server 2022 Enhancement Analytics Classification Index API The new Analytics Classification Index API exposes CRUD operations for working with classification indexes used by the Active Learning application. It also supports submitting, canceling, and checking the statuses of index jobs. It exposes these methods on the IClassificationIndexService interface in the Relativity.Analytics.Classification.<VersionNumber>.Services namespace. Additionally, this service exposes endpoints through REST with the same functionality as available through .NET. For more information, see Analytics Classification Index (.NET) and Analytics Classification Index (REST).

2022-03-21 Server 2022 Enhancement Analytics Conceptual Index API The Analytics Conceptual Index API is now versioned. The namespace has been updated to include the business domain and version number, as exemplified by Analytics.Conceptual.V1.Services . The URLs used through REST also include these updates, as exemplified by conceptual-analytics/v1 . For more information, see Analytics Conceptual Index (.NET) and Analytics Conceptual Index (REST).

2022-03-21 Server 2022 Enhancement Audit APIs The Audit APIs are now versioned. The namespaces have been updated to include the business domain and version number, as exemplified by Relativity.Audit.Services.Interfaces.V1 . The URLs used through REST also include these updates, as exemplified by relativity-audit/v1 . For more information, see Audit (.NET) and Audit (REST) .

2022-03-21 Server 2022 Deprecation Password Bank API The Password Bank API is now deprecated.

2022-03-21 Server 2022 Enhancement ObjectModel.

SDK The APIs within the ObjectModel.SDK are now versioned. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.ObjectModel.V1 . The URLs used through REST also include these updates, as exemplified by relativity-object-model/v1 . For more information, see Object Model .

2022-03-21 Server 2022 Enhancement Infrastructure.

SDK The APIs within the Infrastructure.SDK are now versioned. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.Infrastructure.V1 . The URLs used through REST also include these updates, as exemplified by relativity-infrastructure/v1 . For more information, see Infrastructure .

2022-03-21 Server 2022 Enhancement Identity SDK The APIs within the Identity SDK are now versioned. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.Identity.V1.Services . The URLs used through REST also include these updates, as exemplified by relativity-identity/v1 . For more information, see Identity (authentication and user accounts) .

2022-03-21 Server 2022 Enhancement Mass Operations Manager API The Mass Operations Manager API is now versioned. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.Extensibility.V1.MassOperations . The URLs used through REST also include these updates, as exemplified by relativity-Extensibility/v1 . For more information, see Mass Operation Manager (.NET) and Mass Operation Manager (REST) .

2022-03-21 Server 2022 Enhancement Object Rule Manager API The Object Rule Manager API is now versioned. The namespace has been updated to include the business domain and version number, as exemplified by DataVisualization.v1.ObjectRule . The URLs used through REST also include these updates, as exemplified by relativity-data-visualization/v1 . For more information, see Object Rule Manager (.NET) and Object Rule Manager (REST) .

2022-03-21 Server 2022 Enhancement Workspace Manager API The Workspace Manager API is now versioned. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.Environment.V1.Workspace . The URLs used through REST also include these updates, as exemplified by relativity-environment/v1 . For more information, see Workspace Manager (.NET) and Workspace Manager (REST) .

2022-03-21 Server 2022 Enhancement Instance Setting Manager API The Instance Setting Manager API is now versioned. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.Services.Environment.V1.InstanceSetting . The URLs used through REST also include these updates, as exemplified by relativity-environment/v1 . For more information, see Instance Setting Manager (.NET) and Instance Setting Manager (REST) . Due to the versioning of the Instance Setting Manager API, all of the endpoints have been updated with a new format that includes versioning information and the changes in the previous table. Additionally, the REST URLs have been updated to include the integer for the admin-level context part of the URL

In the Instance Setting Manager API, the method signatures on the IInstanceSettingManager interface have been deprecated. They no longer require a workspace ID set to -1 to indicate the admin-level context.

Deprecated methods and their replacements:

- Task<int> CreateAsync( int workspaceID, InstanceSettingRequest instanceSetting ) replaced with Task<int> CreateAsync(InstanceSettingRequest instanceSetting)

- Task DeleteAsync( int workspaceID, int instanceSettingID ) replaced with Task DeleteAsync(int instanceSettingID)

- Task<InstanceSettingResponse> ReadAsync( int workspaceID, int instanceSettingID ) replaced with Task<InstanceSettingResponse> ReadAsync(int instanceSettingID)

- Task UpdateAsync( int workspaceID, InstanceSettingRequest instanceSetting ) replaced with Task UpdateAsync(InstanceSettingRequest instanceSetting)

- Task UpdateAsync( int workspaceID, InstanceSettingRequest instanceSetting, DateTime lastModifiedOn ) replaced with Task UpdateAsync(InstanceSettingRequest instanceSetting, DateTime lastModifiedOn)

2022-03-21 Server 2022 Breaking Change Instance Setting Manager API In the Instance Setting Manager API, the signatures for all methods on the IInstanceSettingManager interface no longer require a workspace ID set to -1 to indicate the admin-level context. The REST URLs include a similar update that makes the integer for the admin-level context part of the URL.

2022-03-21 Server 2022 Enhancement Tab Manager API The Tab Manager API is now versioned. The namespace has been updated to include the business domain and version number, as exemplified by DataVisualization.v1.Tab . The URLs used through REST also include these updates, as exemplified by relativity-data-visualization/v1 . Additionally, new methods include GetEligibleObjectTypesAsync() and GetEligibleParentTabsAsync(). For more information, see Tab Manager (.NET) and Tab Manager (REST) .

2022-03-21 Server 2022 Enhancement Script Manager API Script Manager is now updated to use versioned namespace paths. The namespace has been updated to include the business domain and version number as exemplified by Extensibility.v1.Scripts . The ID parameter in various methods was renamed to Identifier. Additionally, this API contains the following new methods that allow you to:

- Queue a script to run

- Retrieve status of a script

- Query action results

- Export action results

- Export script report

- Clean up script results

For more information, see Script Manager (.NET) and Script Manager (REST) .

2022-03-21 Server 2022 Enhancement Error Manager API Error Manager is now updated to use versioned namespace paths. The namespace has been updated to include the business domain and version number as exemplified by Environment.V1.Error . This API allows you to expose a single endpoint for creating errors.

For more information, see Error Manager (.NET) and Error Manager (REST) .

2022-03-21 Server 2022 Breaking Change Tab Manager API The Tab Manager API contains several methods that have been renamed or deprecated.

- ITabManager.GetAvailableObjectTypesAsync() replaced with GetEligibleObjectTypesAsync()

- ITabManager.GetAvailableParentsAsync() replaced with GetEligibleParentTabsAsync()

- ITabManager.GetDependencyList() replaced with GetDependencyListAsync() on the Object Manager API

Due to the versioning of the Tab Manager API, all of the endpoints have been updated with a new format that includes versioning information and the changes in the list above..

For more information, see Tab Manager (.NET) .

2022-03-21 Server 2022 Enhancement Production API The Production API is now versioned. The namespaces have been updated to include the business domain and version number, as exemplified by Services.V1.IProductionManager . The URLs used through REST also include these updates, as exemplified by relativity-productions/v1 . Additionally, the Production Manager API includes the following new methods: CancelReproductionJobAsync(), CreateSingleAsync(), DeleteSingleAsync(), GetAllAsync(), GetProductionImagesAsync(), GetProductionImagesTokenAsync(), ReadSingleAsync(), RerunProductionAsync(), RunProductionAsync(), and StageProductionAsync(). The Production Data Source Manager API includes the new GetProductionDataSourceDefaultFieldValues() method. The Production Placeholder Manager API includes the new GetProductionPlaceholderDefaultFieldValues() method. The new Production Queue Manager API exposes methods used to cancel a single or multiple production jobs, to retry multiple jobs, and to set the priority for them. These enhancements are available through .NET and REST. For more information, see Production .

2022-03-21 Server 2022 Breaking Change Imaging API The Imaging API contains several methods that have been deprecated and replaced with new functionality.

- IImagingProfileManager.SaveAsync() replaced by CreateBasicImagingProfileAsync(), CreateNativeImagingProfileAsync(), UpdateAsync()

- IImagingSetManager.SaveAsync() replaced by CreateAsync(), UpdateAsync()

- IApplicationFieldCodeManager.SaveAsync() replaced by CreateAsync(), UpdateAsync()

The Imaging API is now a versioned API. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.Imaging.Services.Interfaces.V1 . The URLs used through REST also include these updates, as exemplified by relativity-imaging/v1 .

Due to the versioning of the Imaging API, all of the endpoints have been updated with a new format that includes versioning information and other changes. Although the legacy Imaging API continues to be supported in the Osier release, we recommend that you implement any new functionality with the versioned Imaging API.

The new IDocumentStatusManager interface contains the GetStatusAsync() method, which retrieves status information about the imaging job for a document. The IImagingEnvironmentManager interface contains the CleanupInactiveJobsAsync() method for cleaning up inactive imaging jobs, and the GetMaxMassImagingJobSizeAsync() method for retrieving the size of a mass imaging job. IImagingJobManager interface includes the new MassImageDocumentsByMassProcessIdAsync(), which submits a mass imaging job. These enhancements are also available through the REST services.

For more information, see Imaging (.NET) and Imaging API (REST) .

2022-03-21 Server 2022 Enhancement Batches Manager API The new Batches Manager API supports retrieving information about existing batches, and checking batches in and out. It exposes these methods for interacting with batches on the IBatchesManager interface in the Relativity.Review.Server.Versioned.<Version Number>.BatchSets namespace. Additionally, the Batches Manager service exposes endpoints through REST that provide the same functionality as available through .NET. For more information, see Batches Manager (.NET) . and Batches Manager (REST) .

2022-03-21 Server 2022 Enhancement Batch Sets Manager API The new Batch Sets Manager API exposes CRUD operations for batch sets. It also supports creating and purging batches for a batch set. The Batch Sets Manager API exposes the methods for interacting with batches on the IBatchSetsManager interface in the Relativity.Review.Server.Versioned.<Version Number>.BatchSets namespace. Additionally, the Batch Sets Manager service exposes endpoints through REST that provide the same functionality as available through .NET. For more information, see Batch Sets Manager (.NET) . and Batch Sets Manager (REST) .

2022-03-21 Server 2022 Breaking Change Keyboard Shortcuts Manager API The Keyboard Shortcuts Manager API is now a versioned API. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.Review.Server.Versioned.V1.KeyboardShortcuts . The URLs used through REST also include these updates, as exemplified by relativity-review/v1 . This API now exposes only the ReadAsync() method for retrieving keyboard shortcuts. Through REST, it also now exposes a single endpoint for this purpose.

The overloaded GetKeyboardShortcuts() method has been deprecated. It has been replaced with the new ReadAsync() method on the IKeyboardShortcutsManager interface in the Relativity.Review.Server.Versioned.<VersionNumber>.KeyboardShortcuts namespace.

The legacy endpoint for retrieving keyboard shortcuts through REST has also been deprecated. A new URL for this functionality is now available.

For more information, see Keyboard Shortcuts Manager (.NET) and Keyboard Shortcuts Manager (REST) .

2022-03-21 Server 2022 Enhancement Matter Manager API The Matter Manager API is now a versioned API. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.Environment.V1.Matter . The URLs used through REST also include these updates, as exemplified by relativity-environment/v1 . For more information, see Matter Manager (.NET) and Matter Manager (REST) .

2022-03-21 Server 2022 Enhancement View Manager API The View Manager API is now a versioned API. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.DataVisualization.V1.View . The URLs used through REST also include these updates, as exemplified by relativity-data-visualization/v1 . For more information, see View Manager (.NET) and View Manager (REST) .

2022-03-21 Server 2022 Enhancement Notifications Manager API The Notifications Manager API is now a versioned API. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.Infrastructure.V1.Notifications . The URLs used through REST also include these updates, as exemplified by relativity-infrastructure/v1 . For more information, see Notifications Manager (MotD) - (.NET) and Notifications Manager (MotD) - (REST) .

2022-03-21 Server 2022 Enhancement Layout Manager API The Layout Manager API supports programmatically managing layouts in Relativity. It supports create, read, update, and delete operations on layouts. It also provides a helper method used to retrieve a list of users with permissions necessary to own layouts. The Layout Manager API exposes the methods for interacting with layouts on the ILayoutManager interface. Additionally, the Layout Manager service exposes endpoints through REST that provide the same functionality as available through .NET. For more information, see Layout Manager (.NET) and Layout Manager (REST) .

2022-03-21 Server 2022 Enhancement Resource File API The Resource File API allows clients to manage resource files for the Relativity applications in the environment. It includes the following features:

- Supports create, read, update, delete and download resource files.

- Update/upload file content and metadata.

- Secondary methods allows the client to read all eligible applications.

For more information, see Resource File API .

2022-03-21 Server 2022 Deprecation Invariant API The Invariant API is now private and no longer available for use in custom applications. You can continue to customize applications using the Processing APIs. For more information, see Processing .

2022-03-21 Server 2022 Deprecation HTTP headers content types The HTTP header Content-Type field no longer can be set to application/json;charset/utf-8 or text/json

2022-03-21 Server 2022 Enhancement ARM API The ARM API supports multiple operations required to archive, restore, and move Relativity workspace data. You can also use to view information on currently running ARM jobs or to list available workspaces or ARM archives. For more information, see ARM API .

2022-03-21 Server 2022 Enhancement Kepler framework The Kepler framework now supports the PATCH verb for the HTTP protocol. This feature will continue to undergo enhancements in future releases. For general information, see HTTP headers, verbs, and related information

2022-03-21 Server 2022 Deprecation Services API The Platform Status tab is now deprecated.

2022-03-21 Server 2022 Enhancement Production API The Production API now includes the Get ProductionPlaceholderDefaultFieldValues() method. The method is used to retrieve default field values for a new Production Placeholder object. For more information, see Production API .

2022-03-21 Server 2022 Enhancement Application Install API The Application Install API includes an update to the field Version, which has been renamed to SchemaVersion. For more information, see Application Install API.

2022-03-21 Server 2022 Enhancement dtSearch Manager API The dtSearch Manager API includes an update to the CompressIndexAsync() method. The method contains a new boolean field, activateIndex, which determines if the index is activated after completion of the job. The existing CompressIndexAsync method without the activateIndex field will still exist; it will simply call the new CompressIndexAsync() with the value of true for activateIndex. For more information, see dtSearch Manager API . The dtSearch Manager service includes the same update to the CompressIndexAsync() endpoint.

2022-03-21 Server 2022 Enhancement dtSearch Manager service The dtSearch Manager service includes an update to the CompressIndexAsync() endpoint. The body of the request now includes a new boolean field, activateIndex, which determines if the index is activated after completion of the job. The existing CompressIndexAsync endpoint without the activateIndex field will still exist; it will simply call the new CompressIndexAsync() with the value of true for activateIndex. For more information, see dtSearch Manager Service .

2022-03-21 Server 2022 Enhancement Document Conflicts API The new Document Conflicts API retrieves information on which documents conflict with a workspace's Production Restrictions search. For more information, see Document Conflicts API.

2022-03-21 Server 2022 Enhancement Library Application API The Library Application API includes an update to the ReadAsync() and ReadAllAsync() methods. The methods contain a new field, IsGlobalApplication, which represents whether or not the application is a global application. Global applications are applications that cannot be installed into any workspaces. For more information, see Library Application API .

2022-03-21 Server 2022 Enhancement Production API The Productions API manages productions in a workspace. For more information, see Production API .

2021-03-24 Server 2021 Breaking Change Application Install API The Application Install API includes multiple property enhancements. Three new properties have been added: Details , IsOutOfDate , and ApplicationInstallDetail.Message .

- ConflictCorrelationID : The conflict correlation ID is no longer required when submitting resolutions. It has been removed to clean up the contract.

- Options : Use the new ResolutionOptions property instead.

- RenameField : Use the Rename enumeration value instead.

- ArtifactStatus : The ApplicationInstallDetail.ArtifactStatus property has been replaced with ApplicationInstallDetail.Message .

- ResolutionType : The ResolutionType property has been removed.

The Application Install API includes multiple endpoint enhancements:

- GetAllInstallStatusAsync : endpoint has been removed.

- A new endpoint GetAvailableWorkspacesAsync has been added.

- The endpoints SearchAsync and SearchApplicationAsync have been modified to include a flag called "includeActions". The route for these endpoints have been slightly modified to reflect the addition of this new flag.

For more information, see Application Install API.

2021-03-24 Server 2021 Enhancement Library Application API The Library Application API includes the following enhancements. The property ApplicationGUID has been added, which contains the GUID of the application contained in the package, used to validate Update workflow. Additionally, the property LicenseStatus has been added, which determines the license status of a specified application: NotApplicable , Valid , Expired , or Invalid . For more information, see Library Application API .

2021-03-24 Server 2021 Breaking Change Relativity Integration Points API The Relativity Integration Points API includes now uses jQuery v3.4.1 rather than the previous version 3.3.1. The Integration Points SDK has been updated with this new library.

Namespace changes:

- kCura.IntegrationPoints.Contracts is now Relativity.IntegrationPoints.Contracts

- kCura.IntegrationPoints.Services.Interfaces.Private is now Relativity.IntegrationPoints.Services.Interfaces.Private

- kCura.IntegrationPoints.SourceProviderInstaller is now Relativity.IntegrationPoints.SourceProviderInstaller

For compatibility with Relativity Server Server 2021 and above , update your custom code to use the new namespace names. Additionally, upgrade custom applications by referencing the new DLLs provided for this release. See Relativity Server APIs .

For more information, see Relativity Integration Points .

2021-03-24 Server 2021 Enhancement Object Manager API The Object Manager API is now a versioned API. The namespace has been updated to include the business domain and version number, as exemplified by Relativity.ObjectManager.V1

2021-03-24 Server 2021 Enhancement Processing API The Processing API includes the following new methods:

- The GetSummaryDataAsync method retrieves the processing set summary data in a specific workspace to display to console, such as environment errors, discover and publish status, and more.

- The ValidDeleteAsync method checks if the specified processing data source is safe to be deleted.

These methods are available on the IProcessingModule interface in the Relativity.Processing.Services namespace. The classes supporting this functionality are available in the Relativity.Processing.Services.Interfaces.DTOs namespace. For more information, see Processing API services for REST .

2021-03-24 Server 2021 Enhancement Production API The Production API now includes the MassRetryAsync() method, which is available in the Relativity.Productions.Services namespace. Withe the MassRetryAsync() method, you can retry multiple production jobs in a single call. Through REST, the Production Manager service also includes this new endpoint. For more information, see Production Manager API and Production Manager Service .

2021-03-24 Server 2021 Enhancement Services API The Object Rule Manager API available through the Object Type Manager API now exposes the new MassDeleteAsync() method, which removes multiple object rules across different object types. Its parameters include the Artifact ID of a workspace and a list containing the Artifact ID for each rule that you want to delete. This method is available on the IObjectRuleManager interface in the Relativity.Services.Interfaces.ObjectRules namespace in the Relativity Services API.

2021-03-24 Server 2021 Enhancement REST API In the REST API, the Object Rule Manager service available as part of the Object Type Manager service includes a new mass delete endpoint that supports removing multiple object rules in a single call.

2021-03-24 Server 2021 Enhancement dtSearch Manager API The dtSearch Manager API now includes the RunBuildAsync() method, which is available in the Relativity.Compute.dtSearch.Services.Interfaces namespace. With the RunBuildAsync() method, you can run a build that first initiates an incremental dtSearch index build operation, if possible, or else runs a full dtSearch index build operation. Through REST, the dtSearch Manager service also includes this new endpoint. For more information, see dtSearch Manager (.NET) and dtSearch Manager (REST) .

2021-03-24 Server 2021 Enhancement Services API The Auth Profile Manager API now supports specifying scopes for an OpenID Connect Provider. The OpenIdConnectProviders class has the new Scopes property, which is used to specify a list of scopes that a client can request. This class is available in the Relativity.Services.Security.Models namespace in the Relativity Services API.

2021-03-24 Server 2021 Enhancement REST API The Auth Profile Manager service supports specifying a list of scopes for an OpenID Connect Provider through REST.

2021-03-24 Server 2021 Enhancement REST API The Processing API now includes the GetSummaryDataAsync() method that retrieves processing set summary data in a specific workspace to display to console, such as environment errors, discover and publish status, and more. The ValidDeleteAsync() method is also included in the Processing API. The method checks if the specified processing data source is safe to be deleted.

These methods are available on the IProcessingModule interface in the Relativity.Processing.Services namespace. The classes supporting this functionality are available in the Relativity.Processing.Services.Interfaces.DTOs namespace. Additionally, the new methods are available through REST. For more information, see Processing API services for REST .

2020-01-20 10.3.287.3 Enhancement Document Viewer API The Document Viewer API now returns the status code of 400 - Bad Request instead of a 500 - Internal Server Error for various issues. For guidelines about API errors, see API error handling .

2020-01-20 10.3.287.3 Enhancement Object Manager API The Object Manager API now returns the status codes of 503 - Temporarily Unavailable, 400 - Bad Request, or 422- Unprocessable Entity instead of a 500 - Internal Server Error for a given issue. For guidelines about API errors, see API error handling .

2020-01-20 10.3.287.3 Enhancement View Manager API The View Manager API now returns the status code of 404 - Not Found instead of a 500 - Internal Server Error when the caller doesn't have permissions to a resource. For guidelines about API errors, see API error handling .

2020-01-20 10.3.287.3 Enhancement Relativity Dynamic Objects You can now define a multiple object field between a RDO and a field object, which means that fields can be set as an associative object type when creating a multiple object field.

2020-01-20 10.3.287.3 Enhancement Document Viewer Services API The Document Viewer Services API now allows you to change the default persistent highlight set or terms. Additionally, you can make terms or highlight sets inactive as desired. The SavePersistentHighlightSetState endpoint also supports this functionality through REST. For more information, see the Document Viewer Services API and the Document Viewer Services in REST .

2020-01-20 10.3.287.3 Enhancement REST API As part of the Object Type Manager service, the Object Rule Manager service includes the updated Available Associated Objects endpoint, which now returns a JSON response that contains a ListType field. This field indicates type of associative objects that the list contains, including ChildObject, MultipleObjectField, or SingleObjectField. The updated Read endpoint now returns a JSON response that also contains a SubListObject field.

2020-01-20 10.3.287.3 Enhancement Services API As part of the Object Type Manager API, the Object Rule Manager API includes the updated GetAvailableAssociatedObjectsAsync() method, which returns a list of SubListObjectIdentifier objects. The ObjectRuleResponse class now has a new SubListObject property, which gets or sets a SubListObjectIdentifier object. The new SubListObjectIdentifier class represents a DTO containing information that identifies the type of a sub-list object. The new ListType Enumeration indicates the available types of associated objects in a list, including ChildObject, MultipleObjectField, or SingleObjectField. These updates are available in the Relativity.Services.Interfaces.ObjectRules namespace and Relativity.Services.Interfaces.ObjectRules.Models namespace.

2020-01-20 10.3.287.3 Enhancement Kepler framework With the new Relativity Kepler framework, you can build HTTP services for REST via a .NET interface. You can implement Kepler services using standard .NET contracts, which the framework uses to build HTTP endpoints. Your Kepler service is then deployed in Relativity as part of a custom application built on the Application Deployment System (ADS). Additionally, the Kepler framework includes a client proxy that you can use when interacting with the services through .NET. For more information, see Kepler framework .

2020-01-20 10.3.287.3 Enhancement API Explorer The new API Explorer provides an interactive way for you to reference our APIs. It lists our core Relativity REST services, which are organized into modules that you can use to perform CRUDQ operations on a Relativity resource. Each module contains the URLs for service endpoints, the ability to view fields used in the payload request, and information about fields returned in a response.

2020-01-20 10.3.287.3 Enhancement Search Terms Report API The new Search Terms Report Services API includes methods to generate a search terms report, adding terms to an existing search terms report, retry any errors, and view the build progress of a specific search terms report. For more information, see Search Terms Report Services API .

Additionally, the new Search Terms Report services expose endpoints that support this same functionality through REST. For more information, see Search Terms Report Services in REST .

2020-01-20 10.3.287.3 Enhancement Application Install API The Application Install API now includes the new CancelAllAsync endpoint. This endpoint cancels all pending application installs associated with a specified application. For more information, see Application Install API .

2020-01-20 10.3.287.3 Enhancement Choice Manager API The Choice Manager API exposes multiple operations you can use to programmatically manage choices in your Relativity environment. It includes the following features:

- Supports create, read, update, and delete operations and massive operations on choices.

- Provides helper methods used to retrieve choice types and choice servers. Use these methods to determine if a server supports the choice type that you want to add to it.

For more information, see Choice Manager API .

2020-01-20 10.3.287.3 Enhancement Library Application API The Library Application API now includes these new endpoints:

- UploadPackageAsync - This endpoint uploads a RAP or XML file to a temporary location in Relativity and returns a unique file identifier along with the meta data for the application. If the file is not in a valid format, a validation exception is thrown. This endpoint is used in conjunction with CreateAsync and UpdateAsync to implement workflows where the application's details need to be displayed for final confirmation before installing the application.

- DownloadPackageAsync - This endpoint downloads a RAP or XML file previously uploaded using the UploadPackageAsync endpoint. It takes the unique file identifier as an argument in the URL path and returns a stream of bytes.

- DeletePackageAsync - This endpoint allows clients to delete an RAP file that has been uploaded to a temporary storage location.

For more information, see Library Application API .

2020-01-20 10.3.287.3 Enhancement Production API The Production Manager API now includes the GetProductionStatusDetails() method, which is available in the Relativity.Productions.Services namespace. With the GetProductionStatusDetails() method, you can retrieve the status of production jobs, which include details on document count, image count, and several other metrics to indicate the progress. Through REST, the Production Manager service also includes this new endpoint. For more information, see Production Manager API and Production Manager Service .

2020-01-20 10.3.287.3 Enhancement Production API The Production Manager API now includes the GetProductionsEligibleForReproductionAsync() method, which is available in the Relativity.Productions.Services namespace. With the GetProductionsEligibleForReproductionAsync() method, you can retrieve all the productions that can be re-produced based on a mass operation database token corresponding to document artifact IDs. Through REST, the Production Manager service also includes this new endpoint. For more information, see Production Manager API and Production Manager Service .

2020-01-20 10.3.287.3 Enhancement Production API The Production Manager API now includes the CreateReproductionJobAsync() method, which is available in the Relativity.Productions.Services namespace. With the CreateReproductionJobAsync() method, you can create a re-production job and all associated production sets. For more information, see Production Manager API and Production Manager Service .

2020-01-20 10.3.287.3 Enhancement Production API The Production Manager API now includes the GetReproductionStatusByReproductionJobIDAsync() method, which is available in the Relativity.Productions.Services namespace. With the GetReproductionStatusByReproductionJobIDAsync() method, you can retrieve the status of a re-production job as well as the ArtifactID and Status of productions included in the re-production job. Through REST, the Production Manager service also includes this new endpoint. For more information, see Production Manager API and Production Manager Service .

2020-01-20 10.3.287.3 Enhancement Production API The Production Manager API now includes the GetReproductionJobIDsAsync() method, which is available the Relativity.Productions.Services namespace. With the GetReproductionJobIDsAsync() method, you can retrieve the job ID of every re-production job run in a specified workspace. Through REST, the Production Manager service also includes this new endpoint. For more information, see Production Manager API and Production Manager Service .

2020-01-20 10.3.287.3 Enhancement Production API The Production Manager API now includes the GetProducedProductionsFromDocumentsAsync() method, which is available in the Relativity.Productions.Services namespace. With the GetProducedProductionsFromDocumentsAsync() method, you can retrieve information about productions that have already been produced in a workspace by passing either a list of document Artifact IDs or a mass operation database token corresponding to document Artifact IDs. The endpoints return all productions that have a partial intersection with the list of documents that you passed. Through REST, the Production Manager service also includes this new endpoint. For more information, see Production Manager API and Production Manager Service .

2020-01-20 10.3.287.3 Enhancement Production API The Production Manager API now includes the GetProductionImagesAsync() method, which is available in the Relativity.Productions.Services namespace. With the GetProductionImagesAsync() method, you can retrieve metadata for specific production images within a production in a certain workspace. Through REST, the Production Manager service also includes this new endpoint. For more information, see Production Manager API and Production Manager Service .

2020-01-20 10.3.287.3 Enhancement Production API The Production Manager API now includes the MassStageAndRunProductionsAsync() method, which is available in the Relativity.Productions.Services namespace. With the MassStageAndRunProductionsAsync() method, you can stage and run multiple production jobs in the same workspace with a single call. Through REST, the Production Manager service also includes this new endpoint. For more information, see Production Manager API and Production Manager Service .

2020-01-20 10.3.287.3 Enhancement REST API In REST, the Field Manager service now includes the new availablerelationalorder endpoint. It retrieves information about the order used to display relational field icons in the Related Items pane of the core reviewer interface for a specific workspace. For more information, see Field Manager (REST) .

2020-01-20 10.3.287.3 Enhancement Services API The Field Manager API now includes the new GetRelationalOrderAsync() method. It retrieves information about the order used to display relational field icons in the Related Items pane of the core reviewer interface for a specific workspace. The new RelationalFieldOrder class is returned by this method, and its properties include the name and type of the relational field, and display order of the field icon. The GetRelationalOrderAsync() method is available on the IFieldManager Interface in the Relativity.Services.Interfaces.Field namespace. The RelationalFieldOrder class is available in the Relativity.Services.Interfaces.Field.Models namespace. For more information, see Field Manager (.NET) .

2020-01-20 10.3.287.3 Deprecation Object Query Manager API The Object Query Manager API has been deprecated in the Indigo release. Use the query functionality available through the Object Manager API in your custom code. For more information, see Object Manager (.NET) and Object Manager (REST) .

2020-01-20 10.3.287.3 Deprecation View Fields Manager API The View Fields Manager API is deprecated and will be removed from the Relativity assemblies. The related documentation will no longer be available in the RelativityOne and Relativity Server Developers sites for the Indigo and higher releases. Upgrade any existing custom applications calling this API to ensure they continue to function properly. Consider using similar functionality exposed through the Object Manager API. For more information, see Object Manager (.NET) and Object Manager (REST) .

2020-01-20 10.3.287.3 Enhancement Services API The Auth Profile Manager API now supports specifying scopes for an OpenID Connect Provider. The OpenIdConnectProviders class has the new Scopes property, which is used to specify a list of scopes that a client can request. This class is available in the Relativity.Services.Security.Models namespace in the Relativity Services API.

2020-01-20 10.3.287.3 Enhancement REST API The Auth Profile Manager service supports specifying a list of scopes for an OpenID Connect Provider through REST.

2020-01-20 10.3.287.3 Enhancement Import API The Import API includes multiple enhancements. The Import API is available only as a NuGet package called Relativity.Server.Import.SDK. The Import API will no longer be part of the Relativity Services SDK published in the Community, but you can easily add the NuGet package to your project through Visual Studio. The Relativity.Import.Client NuGet package has now been deprecated. Any existing Import API applications must now be migrated to the Relativity.Server.Import.SDK package. If you don't migrate your applications to this package, they will fail. Additionally, the Import API has a new versioning scheme, so that the package and assembly versions follow Semantic Versioning 2.0.0. The new RelativityNotSupportedException is thrown when the API isn't compatible with the import or export API services provided by Relativity. The Import API is now decoupled from Relativity core, so it no longer has dependencies on these .NET assemblies. If your Import API application uses objects from the kCura.dll or Relativity.dll .NET assemblies, add a reference to the Relativity.Other package to continue using these components. In the Relativity.Server.Import.SDK, this new File Identification API handles the identification of all file types. This API is available in the Relativity.DataExchange.Io API namespace. You must now use the File Identification API because the kCura.OI.FileID assembly is no longer supported. For more information, Get started with the Import API .

2020-01-20 10.3.287.3 Enhancement Review API The Goatsbeard release introduces one change to the Review API. ViewerCollection now raises a vieweractivated event after activating any of its viewers. For more information, see ViewerCollectionEventType enumeration on the Review API site.

2020-01-20 10.3.287.3 Enhancement Services API The Export API available through the Object Manager API now includes the new RetrieveResultsBlockFromExportAsync() method, which retrieves a specific block of document fields from an in-progress export job. The document fields are specified by calling this method with the index ID for a block of records in a batch, the number of records to export, the workspace ID, and the in-progress export ID. This method is available on the IObjectManager interface in the Relativity.Services.Objects namespace. For more information, see Object Manager (.NET) .

2020-01-20 10.3.287.3 Enhancement REST API The Export service available through the Object Manager service now includes the new RetrieveResultsBlockFromExport endpoint, which retrieves a specific block of document fields from an in-progress export job. The document fields are specified by calling this method with the index ID for a block of records in a batch, the number of records to export, the workspace ID, and the in-progress export ID. For more information, see Object Manager (REST) .

2020-01-20 10.3.287.3 Enhancement Services API The new Document File Manager API exposes methods for downloading native, image, and produced image files associated with documents in Relativity. You can download a file by specifying its GUID, or you can download a native file by specifying the Artifact ID of the document associated with it. The Document File Manager API also supports retrieving information about these files, such as GUID, name, type, size, and others. These methods are available on the IDocumentFileManager interface in the Relativity.Services.Interfaces.Document namespace. The class and enumerations supporting this functionality are available in the Relativity.Services.Interfaces.Document.Models namespace. For more information, see Document File Manager (.NET) .

2020-01-20 10.3.287.3 Enhancement REST API Through REST, the new Document File Manager service exposes endpoints for downloading native, image, and produced image files associated with documents in Relativity. You can download a file by specifying its GUID, or you can download a native file by specifying the Artifact ID of the document associated with it. The Document File Manager API also supports retrieving information about these files, such as GUID, name, type, size, and others. For more information, see Document File Manager (REST) .

2020-01-20 10.3.287.3 Enhancement Application Install API The Application Install API allows clients to install applications into one or more workspaces, cancel pending installations, as well as get the status of any specified application installations. Additionally, this API allows support for conflict resolution for any failed application installations. For more information, see Application Install API .

2020-01-20 10.3.287.3 Enhancement Processing API The Processing API now includes the new PivotOnDiscoveredDocumentsAsync method that retrieves discovered documents on pivot in a specific workspace. These methods are available on the new IProcessingFilterManager interface in the Relativity.Processing.Services namespace. The classes supporting this functionality are available in the Relativity.Processing.Services.Interfaces.DTOs namespace. Additionally, the new methods are available through REST and provide the same functionality as available through .NET. For more information, see Processing Filter Manager and Processing Filter Manager (REST) .

2020-01-20 10.3.287.3 Enhancement Library Application API The Library Application API allows clients to read application metadata and RAP files from the library, upload new applications, and update or delete existing applications. For more information, see Library Application API .

2020-01-20 10.3.287.3 Enhancement Matter Manager API The Matter Manager service exposes multiple endpoints that you can use to programmatically manage matters in your Relativity environment. It includes the following features:

- Supports create, read, update, and delete operations on matters.

- Provides helper endpoints used to retrieve available clients and statuses. Use these endpoints to determine the available clients and statuses with which to create or update matters.

For more information, see Matter Manager API .

2020-01-20 10.3.287.3 Breaking Change Services API The Field Manager API now has the new Source property on the FieldResponse class. This property references a FieldSource object, which contains information about mapping the current field to a processing field. The FieldResponse class is available in the Relativity.Services.Interfaces.Field.Models namespace. For more information, see Field Manager (.NET) .

2020-01-20 10.3.287.3 Breaking Change REST API In REST, the Field Manager service also now includes the Source field on the JSON response returned by the read endpoint. For more information, see Field Manager (REST) .

2020-01-20 10.3.287.3 Enhancement Tab Manager API The Tab Manager API now includes several renamed fields with different field types for the TabRequest and TabResponse classes. The TabRequest class modified fields are ObjectType (formerly ObjectArtifactTypeID) and Parent (formerly ParentID). The TabResponse class modified fields are CreatedBy, LastModifiedBy, ObjectType, and Parent. The Tab Manager API also includes new fields on the Parent and ObjectType sub-objects of the Tab object. The new fields on the Parent sub-object include ArtifactID and Guids. The new fields on the ObjectType sub-object include ArtifactTypeID, ArtifactID, Guids, and Name. For additional information, see Tab Manager API and Tab Manager service .

2020-01-20 10.3.287.3 Enhancement Services API The View Manager API now allows you to see each view in a workspace for a specific Artifact ID. The new RetrieveAllViewsAsync() method is available on the IViewManager interface. Additionally, the View Manager API also allows you see each view that is associated with a saved search in a workspace. The new RetrieveAllViewsForSearchAsync() method is available on the IViewManager interface. For more information, see View Manager API and View Manager Service .

2020-01-20 10.3.287.3 Enhancement REST API The View Manager API now allows you to see each view in a workspace for a specific Artifact ID. Additionally, the View Manager API also allows you see each view that is associated with a saved search in a workspace. For more information, see View Manager API and View Manager Service .

2020-01-20 10.3.287.3 Enhancement Document Viewer Services API The Document Viewer Services API now allows you to view information about the persistent highlight sets and terms in a specific document and workspace. The GetPersistentHighlightSets endpoint also supports this functionality through REST. For more information, see Document Viewer Services API and Document Viewer Services in REST .

2019-10-14 10.2.270.1 Enhancement Review API The new Review API is a suite of APIs that you can use to build and maintain Review integrations. Review is an updated Relativity document review application that you can use to review, annotate, and code documents in a workspace. It offers performance and extensibility improvements over the current HTML viewer. The Review API supports the extensibility of Review by providing JavaScript classes and functions. For more information, see Review API .

2019-10-14 10.2.270.1 Enhancement Processing API The Processing API now includes the new GetDocumentMetadataAsync method that retrieves all metadata fields and values for a specific document and the new GetDiscoveredDocumentsAsync method that retrieves discovered documents in a specific workspace. These methods are available on the new IProcessingFilterManager interface in the Relativity.Processing.Services namespace. The classes supporting this functionality are available in the Relativity.Processing.Services.Interfaces.DTOs namespace. Additionally, the new methods are available through REST and provide the same functionality as available through .NET. For more information, see Processing Filter Manager and Processing Filter Manager (REST) .

2019-10-14 10.2.270.1 Breaking Change Relativity Integration Points API The SourceProvider class is now in the kCura.IntegrationPoints.Contracts namespace in the kCura.IntegrationPoints.Contracts.dll. Other updates include the addition of a new assembly called kCura.IntegrationPoints.Services.Interfaces.Private.dll, and the removal of unnecessary DLLs from the SDK. For more information, see Relativity Integration Points .

2019-10-14 10.2.270.1 Enhancement Services API The new Field Manager API includes multiple operations for programmatically working with field types supported by Relativity, including multiple choice, fixed length text, date, and other fields. It exposes methods for create, read, update, and delete operations on fields. It also provides helper methods for retrieving available object types, views, keyboard shortcuts, and other information about properties that can be set on fields. These methods are available on the IFieldManager Interface in the Relativity.Services.Interfaces.Field namespace. The classes and enumerations supporting this functionality are available in the Relativity.Services.Interfaces.Field.Models namespace. For more information, see Field Manager (.NET) .

2019-10-14 10.2.270.1 Enhancement REST API Through REST, the new Field Manager service includes multiple operations for programmatically working with field types supported by Relativity, including multiple choice, fixed length text, date, and other fields. It exposes endpoints for create, read, update, and delete operations on fields. It also provides helper endpoints for retrieving available object types, views, keyboard shortcuts, and other information about properties that can be set on fields. For more information, see Field Manager (REST) .

2019-10-14 10.2.270.1 Enhancement Services API The new Instance Setting Manager API supports create, read, update, and delete operations on instances setting in a Relativity environment. The methods for these operations are available on the IInstanceSettingManager interface in the Relativity.Services.Interfaces.InstanceSetting namespace. The response and request classes, and the enumeration supporting this functionality are available in the Relativity.Services.Interfaces.InstanceSetting.Model namespace. For more information, see Instance Setting Manager (.NET) .

2019-10-14 10.2.270.1 Enhancement REST API The new Instance Setting Manager sevice supports create, read, update, and delete operations on instances setting in a Relativity environment. This service exposes endpoints through REST that provide the same functionality as available through .NET. For more information, see Instance Setting Manager (REST) .

2019-10-14 10.2.270.1 Enhancement Imaging API The Imaging API now supports programmatically updating the priority on an imaging job. The new UpdateJobPriorityAsync() method is available on the IImagingJobManager interface. The Imaging API also includes the new UpdateJobPriorityRequest and UpdateJobPriorityResponse classes. This method and classes are available in the Relativity.Imaging.Services.Interfaces namespace. Additionally, the new UpdateJobPriorityAsync endpoint provides this same functionality through REST. For more information, see Imaging (.NET) and Imaging API (REST) .

2019-10-14 10.2.270.1 Breaking Change Document Viewer Services API In the Document Viewer Services API, the GetViewerContentKeyOptions class now includes a new property called ClientId. This property represents a string value that indicates the client ID of the application caller, such as DocumentViewer.Conversion.PreConvert. Through REST, the Document Viewer Services supports the same functionality. For more information, see Document Viewer Services (REST) .

2019-10-14 10.2.270.1 Enhancement Services API The Object Manager API includes the new UpdateLongTextFromStreamAsync() method for updating a single long text field that exceeds the length limits of an HTTP request. An instance of the new UpdateLongTextFromStreamRequest class is passed as a parameter to this method. This new method and class are available in the Relativity.Services.Object namespace, and the Relativity.Services.Objects.DataContracts namespace respectively. For more information, see Object Manager (.NET) .

2019-10-14 10.2.270.1 Enhancement REST API Through the REST API, the Object Manager service includes the new updatelongtextfromstream endpoint for updating a single long text field that exceeds the length limits of an HTTP request. For more information, see Object Manager (REST) .

2019-10-14 10.2.270.1 Enhancement MoTD API The Message of the Day API now includes the following new methods; DismissMOTDAsync(), HasDismissedMOTDAsync(), and IsTextOnlyMOTDAsync().

2019-10-14 10.2.270.1 Enhancement Relativity Forms API Relativity Forms API updates now provide more flexibility around Yes/No field behavior and sorting behavior on drop down lists. For more information, see Relativity Forms API .

2019-10-14 10.2.270.1 Enhancement Services API The new View Fields Manager API allows you to view the relation between the Artifact IDs of View Fields objects and the Artifact IDs of a production. The new RetrieveViewFieldIDsFromProductionAsync() method is available on the IViewFieldManager interface.

2019-10-14 10.2.270.1 Enhancement REST API The new View Fields Manager API allows you to view the relation between the Artifact IDs of View Fields objects and the Artifact IDs of a production.

2019-10-14 10.2.270.1 Enhancement Audit APIs The new Audit APIs in .NET include methods that programmatically revert, retrieve, and search Relativity audit records stored in Elasticsearch. These services support interactions with both instance-level and workspace-level audit records. The following APIs provide methods for this functionality: Audit Metrics API, Audit Revert API, Audit Pivot API, Reviewer Statistics API, Audit Query API, and Audit Object Manager UI API. Additionally, these new Audit services expose endpoints that support the same functionality through REST. For more information, see Audit (.NET) and Audit (REST) .

2019-03-30 10.1.169.1 Enhancement Services API The new Keyboard Shortcuts Manager API includes the overloaded GetKeyboardShortcuts() method, which retrieves all keyboard shortcuts available in a workspace, or a specific subset of them, such as those assigned to the system, choices, or fields. This method is available on the IKeyboardShortcutsManager interface in the Relativity.Services.KeyboardShortcuts namespace. The Relativity.Services.KeyboardShortcuts.Models namespace contains the KeyboardShortcutsRequest and other classes used to support this method. For more information, see Keyboard Shortcuts Manager (.NET) .

2019-03-30 10.1.169.1 Enhancement REST API Through the REST API, the new Keyboard Shortcuts Manager service exposes the GetKeyboardShortcuts endpoint, which retrieves all keyboard shortcuts available in a workspace, or a specific subset of them, such as those assigned to system, choices, or fields. For more information, see Keyword Search Manager (REST) for saved searches .

2019-03-30 10.1.169.1 Enhancement Processing API The new Processing Filter Manager API exposes methods for programmatically creating, updating, and deleting processing filters. It supports applying these filters to data and retrieving the filtered data. Additionally, this service exposes helper methods for retrieving filters associated with a data source or available in a specific workspace. These methods are available on the new IProcessingFilterManager interface in the Relativity.Processing.Services namespace. The classes supporting this functionality are available in the Relativity.Processing.Services.Interfaces.DTOs namespace. Additionally, the Processing Filter Manager service exposes endpoints through REST that provide the same functionality as available through .NET. For more information, see Processing Filter Manager and Processing Filter Manager (REST) .

2019-03-30 10.1.169.1 Enhancement Relativity Forms API The new Relativity Forms is a new Layout-rendering option, providing the developer with robust JavaScript APIs and a granular front-end page life cycle for easier, more controlled Relativity object customization. For more information, see Relativity Forms API .

2019-03-30 10.1.169.1 Enhancement Services API The new Object Type Manager API to programmatically create custom object types for use in your applications. It supports create, read, update, and delete operations on object types. To simplify creating and deleting object types, it provides helper methods for retrieving parent object types and dependent objects. The Event Handler Manager API includes methods for attaching event handlers to and removing them from object types. It contains helper methods used for retrieving event handlers available in a workspace, and for retrieving event handlers currently attached to an object type. Additionally, the Object Rule Manager API includes methods for creating, updating, reading, or deleting object rules on an object type. It also provides helper methods for retrieving associative objects, layouts, choices, and choice fields used when creating an object rule. The Mass Operation Manager API includes methods for creating, updating, reading, or deleting mass operations on an object type. It also provides helper methods for retrieving available object types, event handlers, and layouts for use with mass operations.

2019-03-30 10.1.169.1 Enhancement REST API Through the REST API, the new Object Type Manager service exposes endpoints for programmatically working with custom object types implemented in your applications. It supports create, read, update, and delete operations on object types. To simplify creating and deleting object types, it provides helper endpoints for retrieving parent object types and dependent objects. The Event Handler Manager service includes endpoints for attaching event handlers to and removing them from object types. It contains helper endpoints used for retrieving event handlers available in a workspace, and for retrieving event handlers currently attached to an object type. The Object Rule Manager service includes endpoints for creating, updating, reading, or deleting object rules on an object type. It also provides helper endpoints for retrieving associative objects, layouts, choices, and choice fields used when creating an object rule. The Mass Operation Manager service includes endpoints for creating, updating, reading, or deleting mass operations on an object type. It also provides helper methods for retrieving available object types, event handlers, and layouts for use with mass operations.

2019-03-30 10.1.169.1 Enhancement Production API The Production API includes the new MassCancelAsync() method for canceling multiple production jobs, and an update to the signature of the CancelJobAsync() method. These methods are available on the IProductionManager interface in the Relativity.Productions.Services namespace Additionally, it includes the new ProductionJobRef, CancelJobResult, and MassCancelResult classes available in the Relativity.Productions.Services.Interfaces.DTOs namespace. For more information, see Production Manager (.NET) .Through REST, the Production Manager service includes the new MassCancelAsync endpoint for canceling multiple production jobs. The CancelJobAsync endpoint now uses an updated format for the JSON request. For more information, see Production Manager (REST) .

2019-03-30 10.1.169.1 Enhancement Event Handlers In the List Page Interaction Event Handler API, the New Item Button API now includes the new buttonApi.getButtons(). this method returns an array of button objects. For more information, see List Page Interaction Event Handler API .

2019-03-30 10.1.169.1 Enhancement REST API The Agent Manager service now supports the ability to add multiple agents to Relativity in a single call through REST. For more information, see Agent Manager (REST) .

2019-03-30 10.1.169.1 Enhancement Services API The Agent Manager API now includes a new overloaded version of the CreateAsync() method that supports adding multiple agents to Relativity in a single call. The signature for this method now includes an additional integer parameter, which specifies the number of agents to add. In the AgentInstanceLimitResult class, the type for AgentServer and ResourcePool properties has been updated to Securable<DisplayableObjectIdentifier>. The AgentResponse class now inherits from the DisplayableObjectIdentifier class, and the type for the AgentServer, AgentType, CreatedBy, and LastModifiedBy properties has been updated to Securable<DisplayableObjectIdentifier>. The AgentTypeResponse class now inherits from the DisplayableObjectIdentifier class. These methods and classes are available in the Relativity.Services.Interfaces.Agent and Relativity.Services.Interfaces.Agent.Models namespaces respectively. For more information, see Agent Manager (.NET) .

2019-03-30 10.1.169.1 Enhancement Services API The new User Information Manager API provides methods for retrieving all users from a workspace or admin-level context. The RetrieveAll() method returns a list of UserInfo objects, which contain the Artifact ID, full name, and email address for each user. The RetrieveUsersBy() methods filters on a list of users with conditions set in a query, and it also supports paging. The interfaces and classes for this services are available in the Relativity.Services.Interfaces.UserInfo and Relativity.Services.Interfaces.UserInfo.Models namespaces. For more information, see User Information Manager (.NET).

2019-03-30 10.1.169.1 Enhancement REST API The REST API provides coverage for the new User Information Manager service. This service has the retrieveall endpoint that returns the Artifact ID, full name, and email address for each user in a workspace or admin-level context. It also includes provides the retrieveusersby endpoint, which supports both filtering on the results, and paging. For more information, see User Information Manager (REST).

2019-03-30 10.1.169.1 Enhancement Services API The new File Field Manager API exposes a service for uploading and downloading files linked to file fields. For uploads, the overloaded UploadAsync() method supports the use of progress indicators and cancellation tokens. The interface for this service is available in the Relativity.Services.FileField namespace. For more information, see File Field Manager (.NET) .

2019-03-30 10.1.169.1 Enhancement REST API Through the REST API, the new File Field Manager service has endpoints for uploading and downloading files linked to file fields. For more information, see File Field Manager (REST) .

2019-03-30 10.1.169.1 Deprecation Data Grid Lucene Search is deprecated as a Search Provider for Index Search in Relativity.

2019-01-05 10.0.161.8 Enhancement Structured Analytics API The Structured Analytics API includes multiple enhancements to support the new name normalization feature available in Relativity. The new NameNormalizationStatistics class provides information about the number of aliases in the headers for a group of email messages, and the number of new aliases added to Relativity. The JobResults class has the new NameNormalizationStatistics property, which references a NameNormalizationStatistics object. The JobPhase enumeration has the new ImportingEntityAndAliases enum, which indicates that the alias and entity results from the Analytics engine are being imported to a workspace database. The JobOperation enumeration has the new NameNormalizationId enum, which indicates that a name normalization job is the type of Analytics job currently executing. Additionally, the Structured Analytics Manager service also supports name normalization through REST. For more information, see Structured Analytics Job Manager (.NET) and Structured Analytics Job Manager (REST) .

2019-01-05 10.0.161.8 Enhancement Services API The new Tab Manager API supports programmatically managing tabs in Relativity. It supports create, read, update, and delete operations on tabs. To simplify working with tabs, it also provides helper methods for retrieving information about the display order of tabs, parent tabs, available object types to associated with tabs, and objects dependent on a specific tab. Additionally, it also supports retrieving workspace-level metadata for admin and system tabs. These methods are on the ITabManager Interface available in the Relativity.Services.Interfaces.Tab namespace. The classes and enumeration supporting this functionality are available in the Relativity.Services.Interfaces.Tab.Models namespace. For more information, see Tab Manager (.NET) .

2019-01-05 10.0.161.8 Enhancement REST API The new Tab Manager server exposes multiple endpoints for programmatically managing tabs in Relativity. It supports create, read, update, and delete operations on tabs. To simplify working with tabs, it also provides endpoints for retrieving information about the display order of tabs, parent tabs, available object types to associated with tabs, and objects dependent on a specific tab. Additionally, it also supports retrieving workspace-level metadata for admin and system tabs. For more information, see Tab Manager (REST) .

2019-01-05 10.0.161.8 Enhancement Services API The new Agent Manager API exposes multiple operations for programmatically managing agents in your Relativity environment. It supports create, read, update, and delete operations on agents. It provides methods for retrieving agent types and agent servers, and for validating whether a create, update, or delete operation violates the maximum or minimum number of required agents. These methods are available on the new IAgentManager interface in the Relativity.Services.Interfaces.Agent namespace. The classes supporting this functionality are available in the Relativity.Services.Interfaces.Agent.Models namespace. For more information, see Agent Manager (.NET) .

2019-01-05 10.0.161.8 Enhancement REST API The new Agent Manager service exposes multiple operations for programmatically managing agents in your Relativity environment. It supports create, read, update, and delete operations on agents. It provides endpoints for retrieving agent types and agent servers, and for validating whether a create, update, or delete operation violates the maximum or minimum number of required agents. For more information, see Agent Manager (REST) .

2019-01-05 10.0.161.8 Enhancement Services API In the Object Manager API, the ReadOptions class now has a new property called FieldTypesToReturnAsString, which returns a list of currency or decimal field types as a string. For more information, see Object Manager (.NET) .

2019-01-05 10.0.161.8 Enhancement REST API In the Object Manager service, the ReadOptions class now has a new property called FieldTypesToReturnAsString, which returns a list of currency or decimal field types as a string through REST. For more information, see Object Manager (REST) .

2019-01-05 10.0.161.8 Enhancement Services API The Object Manager API now supports setting and updating values in file fields. For more information, see Object Manager (.NET) .

2019-01-05 10.0.161.8 Enhancement REST API The Object Manager service now supports setting and updating values in file fields through REST. For more information, see Object Manager (REST) .

2019-01-05 10.0.161.8 Enhancement Services API The Object Manager API now supports the ability to retrieve a list of objects dependent on one or more objects selected for deletion. It includes the new GetDependencyListAsync() method that returns a list of dependent objects and is available on the IObjectManager interface in the Relativity.Services.Objects namespace. The new DependencyListByObjectIdentifiersRequest class represents a request for information about dependent objects and is available in the Relativity.Services.Objects.DataContracts namespace. Additionally, the new Dependency class represents an object dependent on a specific object selected for deletion and is available in the Relativity.Services.Interfaces.Shared namespace. For more information, see Object Manager (.NET) .

2019-01-05 10.0.161.8 Enhancement REST API Through the REST API, the Object Manager service now supports the new dependencylist endpoint used to retrieve a list of objects dependent on one or more objects selected for deletion. For more information, see Object Manager (REST) .

2019-01-05 10.0.161.8 Breaking Change Processing API In the Processing API, the Entity constant in the CustodianType enumeration has been renamed to Other. The value and description of Other remains unchanged. The CustodianType enumeration is available in the Relativity.Processing.Services namespace of the Class library reference reference. For general information, see Get started with the Processing SDK .

2019-01-05 10.0.161.8 Enhancement Document Viewer Services API The Document Viewer Services API now supports converting files contained in File fields on a Relativity Dynamic Objects (RDOs) for display in the standalone viewer. The GetViewerContentKeyOptions class includes the new FileId property, which provides the identifier for an RDO with an associated File field. During File field conversion, the DocumentIds property on the GetViewerContentKeyRequest class contains only the FieldArtifactId for the File field. The GetViewerContentKeyAsync endpoint also supports this functionality through REST. For more information, see Document Viewer Services (.NET) and Document Viewer Services (REST) .

For changes prior to 2019-01-01, please refer to the Platform change log (Archive)

On this page

- Platform change log

- Released Changes


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

---
title: "Instance settings' descriptions"
url: https://help.relativity.com/Server2025/Content/System_Guides/Instance_Setting_Guide/Instance_setting_descriptions.htm
collection: user
fetched_at: 2026-06-22T06:03:31+00:00
sha256: 0e8486ac26a2ff29cc8349f8b8669c3df358bdffa2b5d317d5d19207d812ba91
---

Instance settings' descriptions

# Instance settings

This page provides an alphabetical list of all the instance settings in Relativity.

A number of the instance setting entries listed below should never be modified in your environment, despite the fact that they appear in the EDDS.InstanceSetting table in the database. For these entries, we've included a Do not modify statement at the beginning of the description.

## Instance settings change log

The following table lists all added, removed, and modified instance settings for this Server version.

Type of change Name Section Notes

Added DotNetEventCounterIntervalSeconds Relativity.OpenTelemetry Released in Server 2025

## Instance settings descriptions

Show filters

Hide filters

Section

- Select / Deselect all

- kCura.AssistedReview

- kCura.Audit

- kCura.Audit.Agent

- kCura.Billing

- kCura.Chicago

- kCura.Code.Data

- kCura.Data.RowDataGateway

- kCura.EDDS.Agents

- kCura.ARM

- kCura.EDDS.DBMT

- kCura.EDDS.Procuro

- kCura.EDDS.SqlServer

- kCura.EDDS.TemplateManager

- kCura.EDDS.Web

- kCura.EDDS.Web.Distributed

- kCura.EDDS.WebAPI

- kCura.EDDS.Winform

- kCura.ImagingSetEventHandlers.W

- kCura.LicenseManager

- kCura.Notification

- kCura.Relativity

- kCura.Web.UI.WebControls

- kCura.WorkspacePortal

- Relativity.ApplicationBase

- Relativity.Authentication

- Relativity.Conversion

- Relativity.Conversion.Cache

- Relativity.Core

- Relativity.Core.Log

- Relativity.Core.Logging

- Relativity.Data

- Relativity.DataGrid

- Relativity.DataGridMigrator.Agent

- Relativity.DataTransfer

- Relativity.DocumentViewer

- Relativity.ForgotPassword

- Relativity.Imaging

- Relativity.Production

- Relativity.StructuredAnalytics

- Relativity.ServiceBus

- Relativity.Services.ServiceHost

- Relativity.Telemetry

This instance setting is available only when you install telemetry in your environment.

Hide filters

A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z

## A

- AboutBoxInstanceNameVisible

Section kCura.EDDS.Web

Value True

Description Specifies if the Relativity instance name can be seen in the About box.

- AboutBoxPortalLink

Section kCura.EDDS.Web

Value https://na3.salesforce.com/secur/login_portal.jsp?orgId=00D5000000072uY&portalId=060500000004fqC

Description Identifies the location to which the Relativity Icon Box redirects.

- AboutBoxSupportLink

Section Relativity.Authentication

Value https://www.relativity.com/support/

Description Identifies the location to which the Support link redirects.

- AccessTokenExtraLifetime

Section Relativity.Authentication

Value 240

Description Determines the number of additional minutes the authentication token remains valid after the authentication cookie has expired. You can use this token to access Relativity APIs because it has a longer lifetime than a session cookie. This may execute long running processes requiring tokens. This instance setting supports a maximum value of 600 minutes, or 10 hours, and a minimum value of 240 minutes, or 4 hours. You must reset the IIS for these changes to take effect.

Recommended security value

- Use the default setting.

- It is more secure to limit the life of this token.

Section kCura.LicenseManager

Value UNSETACCOUNT

Description Determines the text that appears in the Account column in the Case Statistics Rollup report.

- AdditionalWorkFactorDefault

Section Relativity.Authentication

Value 0

Description Sets the default value for the AdditionalWorkFactor setting in the Authentication Provider Settings section of the Authentication Provider tab.

Recommended security value

- Use the default setting unless your organization decides more hashing is necessary.

- More hashing means better encryption, but increasing this value should be tested prior to making the change in Production, as it could significantly increase login time.

- AdminsCanSetPasswords

Section Relativity.Authentication

Value (Undefined)

Description Sets the system admin's ability to create passwords for users. If True, they can create the password. If False, they cannot. You must manually create this instance setting because it's not installed by default.

Recommended security value

If this setting exists, either delete it OR set its value to False - this means that only the user knows his or her password.

- AdvancedSearchDefault

Section kCura.EDDS.Web

Value False

Description Controls the default setting for Advanced Search Default when creating new users. If set to True the default setting is public. If set to False, the default setting is private.

- AgentManagerCheckInDelay

Section Relativity.Core

Value 5000

Description Determines the interval at which the Agent Manager updates agent servers.

- AgentOffHourEndTime

Section kCura.EDDS.Agents

Value 5:00:00

Description

Specifies a valid time range when off hour agents should run. This instance setting is used in conjunction with the AgentOffHourStartTime instance setting.

Currently, this only applies to the File Deletion manager, Case Statistics Manager, Case Manager, and Cache Manager. The File Deletion manager immediately stops deleting documents once the time of day passes the AgentOffHourEndTime. The Case Statistics manager and Case Manager continue to process until completion.

To enter a setting, use 24-hour time notation with the format of hh:mm:ss. If the start time is before midnight, you must also set the end time before midnight. For example, a start time of 23:00:00 might have an end time of 23:59:00. If the start time is midnight or later, you can set the end time to any value after the start time. For example, a start time of midnight that is between 00:00:00 and 03:00:00 can have any end time.

- AgentOffHourStartTime

Section kCura.EDDS.Agents

Value 00:00:00

Description

Specifies a valid time range when off hour agents should run. This instance setting is used in conjunction with the AgentOffHourEndTime instance setting.

Currently, this only applies to the File Deletion manager, Case Statistics Manager, Case Manager, and Cache Manager. The File Deletion manager immediately stops deleting documents once the time of day passes the AgentOffHourEndTime. The Case Statistics manager and Case Manager continue to process until completion.

To enter a setting, use 24-hour time notation with the format of hh:mm:ss. If the start time is before midnight, you must also set the end time before midnight. For example, a start time of 23:00:00 might have an end time of 23:59:00. If the start time is midnight or later, you can set the end time to any value after the start time.

- AgentThreadCount

Section kCura.ARM

Value 1

Description Specifies the number of threads each ARM agent can run.

- AllowAddOrEditScripts

Section kCura.EDDS.Web

Value False

Description

Determines whether create/edit is enabled for Relativity Scripts.

Recommended security value

False - setting this to false limits the number of users who can create and edit Relativity scripts. Running a badly written script could potentially affect the entire site.

- AllowADSToShrinkFieldLength

Section Relativity.Core

Value False

Description Indicates whether a field can have its length shortened during application import. Setting this value to True lets field lengths shrink. Setting this value to False prevents field lengths from shrinking.

- AllowChangesToOverwriteProtection

Section kCura.EDDS.Web

Value False

Description Controls whether the Overwrite Protection drop-down menu is editable when editing or creating a layout. If set to True, users can set this property to Disabled and save a document even if another process has modified the document since loading. If set to False, users cannot set this property to Disabled.

- AllowHtmlVisible

Section Relativity.Core

Value False

Description Controls the accessibility of the Allow HTML property on Field objects. If set to False, the Allow HTML property is hidden from the New Field page and its value defaults to No. The Edit Field page displays the property only if the field being edited already has the property's value set to Yes. If set to True, there is unrestricted access to the Allow HTML field property.

Recommended security value

False - this prevents administrators from allowing HTML as inputs into fields. By doing this, attackers cannot input malicious HTML or scripts.

- AllowMaintenanceModeAccessToGroups

Section Relativity.Authentication

Value Text

Description A semicolon delimited list of Artifact IDs of groups allowed access to Relativity while maintenance mode is active. This instance setting is not encrypted. For more information, see InMaintenanceMode setting.

- AllowNativeRedactions

Section kCura.EDDS.Web

Value True

Description Determines whether users can perform redactions within the Native Viewer. If set to True, users can perform redactions within the Native Viewer. If set to False, users cannot perform redactions within the Native Viewer.

- AlreadyMarkedDirtyMinLastAccessedHours

Section Relativity.Conversion.Cache

Value 4

Description The minimum time that must elapse, in hours, before a cached document already marked dirty is added to the job.

- AnalyticsAutoIdLanguages

Section Relativity.Core

Value False

Description Toggles automatic language identification mode for analytics. If set to True, all documents are processed through language identification code, and then processed according to the locale rules for the identified language. By default this is not enabled.

- AnalyticsCategorizationBatchSize

Section Relativity.Core

Value 100000

Description Determines the number of objects per batch of CategoryResult objects created within Relativity once the Analytics engine has categorized them.

- AnalyticsCategorizationCreationBatchSize

Section Relativity.Core

Value 1000

Description Determines the number of objects per batch of CategoryResult objects created within Relativity once the Analytics engine has categorized them.

- AnalyticsCategorizationDeadlockWait

Section kCura.Data.RowDataGateway

Value 30000

Description The amount of time, in milliseconds, a query waits to retry when a deadlock happens during the run of a categorization set.

- AnalyticsCategorizationDeletionBatchSize

Section Relativity.Core

Value 1000

Description Determines the number of objects per batch of CategoryResult objects deleted within Relativity when the user chooses to run a full categorization against a set that has been previously categorized.

- AnalyticsIndexChoiceUpdateBatchSize

Section Relativity.Core

Value 100 KB

Description This instance setting is used after enabling queries on an analytics index. It updates the choice field, Analytics Index, on the Document object.

- AnalyticsIndexExcludeLargeDocuments

Section Relativity.Data

Value True

Description Enables the removal of documents from an Analytics Index before population begins.

- AnalyticsRestTimeout

Section Relativity.Core

Value 200

Description This setting controls the timeout of HTTP requests, in seconds, to CAAT using REST. This cannot be set to 0. Changes to this will require a restart of the service the request is coming from. For example, agents, web, and others.

- AncestorCountWarningLevel

Section kCura.EDDS.Web

Value 50000

Description Determines the number of ancestors that must exist before a warning appears in the Security page. The warning appears when a user changes the item's security more than this number of ancestors. The purpose of the warning is to warn users the database locks for a substantial period of time.

- API Timeout

Section kCura.Relativity

Value 30

Description Sets the Relativity API token expiration time in minutes.

- ApplicationInstallationManagerCacheTimeout

Section Relativity.Core

Value 10

Description The amount of time, in minutes, that the Application Installation Manager agent caches an application's schema, custom pages, assemblies, and resource files in memory. A value of 0 disables the cache.

- ApplicationRestrictedFileTypes

Section Relativity.Core

Value .exe;.com;.pif;.bat;.scr

Description A semicolon-delimited list of file extensions, including periods, indicating file types users are prohibited from uploading as custom pages or resource files. Examples include .exe, .com, and .bat. Also, see RestrictedFileTypes .

Recommended security value

- Use the default values plus any other file extensions your organization deems necessary.

- Add any file extensions to the list that your organization deems unsafe.

- AssignToEntityItemLimit

Section Relativity.StructuredAnalytics

Value 500

Description

This instance setting must be manually added to your environment.

You can create this instance setting to limit the maximum number of aliases that a user can assign to an entity.

- AuditApplicationUninstallEnabled

Section Relativity.Core

Value True

Description Controls whether Relativity writes an entry to the audit log for each component edited or deleted when you uninstall an application. Setting this value to True writes the entries. Setting this value to False does not write the entries.

- AuditCountQueries

Section Relativity.Core

Value False

Description Controls if the SQL count query is written to the History record. For each list that is generated, the system initially runs a count query to get the total number of records that fulfill the criteria. Setting this value to True writes the SQL query to the History record. Setting this value to False does not write the SQL query to the History record.

- AuditDataGridEndPoint

Section kCura.Audit

Value blank

Description Used for Data Grid connection. This value is required to activate Data Grid operation for this Relativity instance, http://client:9200.

This instance setting must be manually added to your environment.

- AuditDeleteBatchSize

Section kCura.Audit

Value 200000

Description Determines the size of the batch that the agent uses when deleting audit records previously migrated to Data Grid.

- AuditingEnabled

Section kCura.Audit

Value True

Description Controls whether auditing is enabled throughout Relativity. Setting this value to True enables auditing. Setting this value to False disables auditing.

Recommended security value True - this keeps detailed logs of all actions that take place in Relativity can protect your organization if there is ever a need to troubleshoot an issue or investigate the actions of a particular user.

- AuditFullQueries

Section Relativity.Core

Value False

Description Controls whether the SQL query that gets the date to fill the rows on the current page is written to the History record. For each list page that is generated, the system initially runs a query to get the data to fill the rows on the current page. Setting this value to True writes the SQL query to the History record. Setting this value to False does not write the query to the History record.

- AuditIdQueries

Section Relativity.Core

Value True

Description Controls whether the SQL queries used to get a batch of Artifact IDs that fulfill the criteria and are needed to populate the current page in the list are written to the History record. Setting this value to True writes the SQL queries to the History record. Setting this value to False doesn’t write the SQL queries to the History record.

- AuditMigrateBatchSize

Section kCura.Audit

Value 50000

Description Determines the size of the batch that the agent uses when reading from SQL and writing to Data Grid.

- AuditPivotColumnRetrievalQueries

Section Relativity.Core

Value True

Description Controls whether the SQL query that gets the unique columns needed to display the data is written to the History record. For each pivot list and chart, a query runs to get the unique columns needed to display the data. Setting this value to True writes the SQL query to the History record. Setting this value to False does not write the SQL query to the History record.

- AuditPivotFullQueries

Section Relativity.Core

Value True

Description Controls whether the SQL query used to get the data for the rows and columns of each pivot list and chart is written to the History record. Setting this value to True writes the SQL query to the History record. Setting this value to False doesn’t write the SQL query to the History record.

- AuditPivotMaxBucketCount

Section kCura.Audit

Value 1000

Description Specifies the maximum number of aggregated groups for audit pivots.

- AuditQueueMaxDocumentErrors

Section kCura.Audit

Value 100

Description Determines the maximum number of errors allowed for a single batch in the Audit Migration Agent before the job is terminated. If this limit is reached, the respective agent will throw an exception saying that the failure limit has been reached.

- AuthenticationEmailFrom

Section kCura.Notification

Value authentication@relativity.com

Description Defines the email address that appears in the From field of email messages that contain authentication information for users.

- AuthenticationTokenLifetimeInMinutes

Section Relativity.Core

Value 5

Description The amount of time, in minutes, an authentication token is valid. Relativity receives a token every time an application other than Relativity is authenticated using Relativity's internal mechanism.

- AuthenticatorRegistrationName

Section Relativity.Authentication

Value N/A

Description The application name used for two-factor authentication Authenticator app. Colons will be removed.

- AutoCreateRate

Section kCura.EDDS.Web

Value 60

Description Determines how often, in minutes, the system attempts to create batches.

- AutoEmailWithCaseStatisticsManager

Section kCura.Billing

Value True

Description Determines the type of file the Case Statistics Manager agent generates to send client billing information to Relativity . If set to True, the Case Statistics Manager agent generates a text file with client billing information which is sent to Relativity . Each time the agent runs, the new text file is sent to Relativity through the SMTP server. If set to False, the Case Statistics Manager generates a zip file with client billing information, which is stored in the location specified in the EDDSFileShare value. Each time the agent runs, a new date-stamped file is created and stored in this folder. Zip files stored in this location can be manually sent to Relativity .

- AutomatedDropColumn

Section Relativity.DataGrid

Value False

Description This instance setting prevents the dropping of the column from the full text index and the document table. If enabled, the user is responsible for dropping this column from the database.

## B

- BackupDirectory

Section kCura.EDDS.SqlServer

Value During Relativity installation

Description

Identifies the path to the backup directory that SQL Server uses. This value should be relative to the server where SQL Server is installed.

- BaseApplicationPath

Section kCura.EDDS.Procuro

Value During Relativity installation

Description Identifies the root path where Procuro looks for required Relativity applications.

- BaseRelativityScriptPath

Section kCura.EDDS.Procuro

Value During Relativity installation

Description Identifies the root path where Procuro looks for its SQL scripts.

- BasicImagingTimeout

Section Relativity.Core

Value 300

Description The amount of time, in seconds, that the basic imaging process waits for a single document to be imaged before killing the export process and moving to the next document.

- BatchExportRateMs

Section Relativity.OpenTelemetry

Value 5000

Description The rate in milliseconds that Open Telemetry exports logs, traces, and metrics.

- BatchTimeoutMs

Section Relativity.OpenTelemetry

Value 10000

Description The maximum waiting time, in milliseconds, for the Open Telemetry's back-end to process each batch.

- BcpShareFolderName

Section kCura.Chicago

Value BCPPath

Description Defines the name of the share used for Bulk Inserts and the Case Statistics manager.

- BinderDocumentDeleteBatchSize

Section Relativity.Core

Value 1000

Description The number of binder documents to delete at a time when starting a new binder build.

- BrandingManagerBatchAmount

Section kCura.EDDS.Agents

Value 100

Description Determines the number of files the Branding Manager brands in a single batch.

- BrandingManagerTimeoutCount

Section Relativity.Production

Value 10

Description The number of times branding managers can be timed out for a single production before all incomplete branding jobs are marked as errored. Set to 0 to disable.

- BrandingRecordCreationBatchSize

Section kCura.EDDS.Agents

Value 10000

Description Determines the maximum number of records inserted into the Branding Queue table in a single batch. Both the Production Manager and users attempting to Resolve Errors in the web use this functionality.

- BufferAcquisitionTimeoutInMilliseconds

Section kCura.EDDS.Web.Distributed

Value 5000

Description The amount of time, in milliseconds, the Distributed site waits to acquire a free buffer to use for downloading before throwing an error.

- BufferCount

Section kCura.EDDS.Web.Distributed

Value 1000

Description Determines the number of buffers that the Distributed site allocates to servicing download requests.

- BufferSize

Section kCura.EDDS.Web.Distributed

Value 81920

Description The maximum size, in bytes, of each buffer that the Distributed site allocates to service download requests. Increasing this may improve file download performance but increases the risk of running the Distributed server out of memory.

- BulkLoadFileFieldDelimiter

Section Relativity.Data

Value þþKþþ

Description The value used to separate fields when loading bulk files into the SQL database. Line delimiters are this value plus a new line.

## C

- CacheLocationLowerThreshold

Section Relativity.Core

Value 30

Description Specifies the lower limit of the cache size as a percentage of the total space available on the drive where the cache is stored. After the Cache Manager agent runs, the size of the cache table is below its lower limit.

Note: If you leave this value blank, Relativity uses the default value of 30.

- CacheLocationUpperThreshold

Section Relativity.Core

Value 70

Description

Specifies the upper limit of the cache size as a percentage of the total space available on the drive where the cache is stored. The cache table must equal or exceed this upper limit before the Cache Manager clears entries from it.

If you leave this value blank, Relativity uses the default value of 70.

- CacheManagerFileDeletionRetry

Section Relativity.Core

Value 3

Description Determines the number of attempts the Cache Manager tries to delete a specific file.

- CacheManagerFileDeletionWait

Section Relativity.Core

Value 1000

Description The amount of time, in milliseconds, that the Cache Manager waits before retrying to delete a file.

- CancelRequestEnabled

Section Relativity.Core

Value True

Description Determines whether the option to cancel requests is available to Relativity users. If set to True, users can see an overlay window with the option to cancel the request and a message indicating that items are loading. If set to False, this functionality is not available.

- CancelRequestInitialPollingInterval

Section Relativity.Core

Value 100

Description The initial time interval, in milliseconds, used for polling the cache on the web server during the first second of a cancel query request. After the first second, the time interval increases to 450 msec.

- CancelRequestTimeDelay

Section Relativity.Core

Value 3

Description The time delay, in seconds, between the initiation of a search request and the appearance of an overlay window with the option to cancel the request.

- CardinalityLimit

Section Relativity.OpenTelemetry

Value 2000

Description The limit for the number of unique attribute values, also known as cardinality, that Open Telemetry tracks for metric signals. High cardinality attributes such as like user IDs or session tokens can negatively impact performance.

- CasesForGroupsViewID

Section kCura.EDDS.Web

Value 900

Description Identifies the ArtifactID of the view that displays the workspaces at the bottom of a group page.

- CaseStatisticsBasedLockout

Section kCura.LicenseManager

Value blank

Description Determines if the Case Statistics based lockout is active. If set to On, the Case Statistics based lockout is active. If set to Off, the Statistics based lockout is inactive.

- CaseStatisticsNotificationIncludeEmails

Section kCura.LicenseManager

Value True

Description Determines whether to show the email and original email address fields in the Case Statistics and User Rollup scripts. If set to True, this instance setting populates the email and original email address fields in the Case Statistics and User Rollup scripts. If set to False, those fields are retrieved as empty.

- CaseStatisticsNotificationList

Section kCura.LicenseManager

Value blank

Description The distribution list for Case Statistics reports. It expects a semicolon-delimited list of email addresses to send the report to. If empty, emails are not sent.

- ChoiceLimitForUI

Section Relativity.Core

Value 200

Description Determines the maximum number of choices and single objects that can be rendered in a checkbox, drop-down menu, or radio button list before switching to a pop-up picker. For the best performance, we recommend setting this value to 15. If this is not set, lists automatically render as pop-up pickers.

- ChunkEnabledQueryChunkSize

Section Relativity.Data

Value 10000

Description Determines the number of artifacts, specifically choices and folders, in a set that the Desktop Client can pull down.

- ClassificationCategorizationDelay

Section Analytics.Core

Value 5

Description The interval, in minutes, at which the Categorization Set agent checks if there are untrained coding decisions. If there is a change in coding decisions, but no new changes since the last interval check, a build will commence.

- ClassificationCategorizationMaxDelay

Section Analytics.Core

Value 20

Description The maximum amount of time, in minutes, the Categorization Set agent will go without categorizing if there is a change in coding decisions.

- ClientBatchSize

Section Relativity.Telemetry

Value 500

Description

The size of batches used for flushing non-aggregated metrics in the client-side queues.

This instance setting is available only when you install telemetry in your environment.

- ClientConfigUpdateInterval

Section Relativity.Telemetry

Value 15

Description

The interval in seconds between updates to the configuration of the client-side metrics queues.

This instance setting is available only when you install telemetry in your environment.

- ClientDomainsFeatureAvailable

Section Relativity.Core

Value False

Description Determines the visibility of the values that allow a client to become a client domain. If set to True, features related to client domains are visible and available inside the environment. If set to False, users do not see anything related to client domains.

- ClientFlushTimeout

Section Relativity.Telemetry

Value 5

Description

The number of seconds between each flush of the client-side queue. When the queue is flushed, the service bulk posts any content that it contained to the Kepler endpoint.

This instance setting is available only when you install telemetry in your environment.

- CloudInstance

Section Relativity.Core

Value False (recommended value)

Type Text

Description

This setting controls cloud specific behavior.

For Relativity Server, we support the configuration where the instance setting is not present, and the configuration where the instance setting is False.

The value of True is only supported in R1 instances, and should never be used for Relativity Server.

- CompareWebAPIPath

Section kCura.EDDS.Web

Value Set during Relativity installation

Description Identifies the Compare Web API path.

- CompressionLevel

Section kCura.ARM

Value 0

Description The compression level to be used for determining zip compression when archiving a workspace using ARM. Set this to 0 if you do not wish to compress the workspace files. For minimum Compression set this to 1 and for maximum compression, set this to 9. You can enter any value in this range to set the level of compression.

- ConcurrentLogin

Section kCura.LicenseManager

Value per system

Description Determines the setting for requiring the Concurrent User Login restriction. A tool that the engineering teams own must change this value; the default value is Off.

- ContentAnalystAdvancedOptionsURLBase

Section Relativity.Core

Value blank

Description Specifies the URL base of the advanced options page for indexes that the Content Analyst web front-end provides. If this is set to an empty string, the value is automatically deduced by looking at the value of ContentAnalystWebServicesURLBase.

- ContentAnalystDefaultDimensions

Section Relativity.Core

Value 100

Description Determines the number of default dimensions specified for new Content Analyst indexes.

- ContentAnalystDefaultNumberOfProcessors

Section Relativity.Core

Value 2

Description Indicates the number of processors that a single Analytics index uses for a build. Increasing the number of processors to a value greater than two may slow the performance of the Analytics server. You must adjust any setting modifications to the requirements of your environment.

- ContentAnalystFileMaxByteThreshold

Section Relativity.Core

Value 524288000

Description

This was deprecated in Relativity 8.1. Changing this value has no effect on the environment.

- ContentAnalystMaximumBatchSize

Section Relativity.Core

Value 1000

Description Determines the maximum number of documents that can be sent to the Content Analyst engine at once. This is one of the variables used to determine when the Content Analyst Index Manager sends a batch of documents to the Content Analyst engine. Increasing this value may lead to better performance, because higher values allow for larger sets of documents to be sent to the Content Analyst engine. At a certain point, this number may become so large that it actually decreases performance because the agent needs to update the status of all the documents in a batch at the same time on the population table. This instance setting has no effect on memory usage.

- ContentAnalystMaxConnectorsPerIndexDefault

Section Relativity.Core

Value 4

Description Determines the default maximum number of connections allowed between the Analytics server and SQL for each index that uses this server.

- ContentAnalystMaxTotalConnectorsDefault

Section Relativity.Core

Value 50

Description Determines the maximum number of connections allowed between the Analytics server and SQL across all indexes using this server.

- ContentAnalystSimilarDocsJobType

Section Relativity.Core

Value 0

Description Determines the default similar documents job type to submit to Content Analyst, comprehensive.

- ContentAnalystSingleRecordMaxByteThreshold

Section Relativity.Core

Value 31457280

Description This setting was deprecated in Relativity 8.1. Changing this value has no effect on the environment.

- ContentAnalystSmartTrainOnByDefault

Section Relativity.Core

Value True

Description

Determines whether Analytics indexes are enabled by default to use the Optimize training set functionality, which automatically excludes conceptually-irrelevant documents from an index's training data source.

If set to True, Analytics indexes use the Optimize training set functionality. If set to False, Analytics indexes do not use the Optimize training set functionality

- ContentAnalystTemporaryDirectory

Section Relativity.Core

Value blank

Description This was deprecated in Relativity 8.1. Changing this value has no effect on the environment.

- ContentAnalystTemporaryDirectory

Section Relativity.StructuredAnalytics

Value blank

Description

This setting was deprecated in Relativity 8.1. Changing this value has no effect on the environment.

- ContentAnalystUpdateBatchSize

Section Relativity.Core

Value 50000

Description Determines the number of documents per batch to update the non-similar documents in the documents table.

- ContentAnalystWebServicesMaxByteThreshold

Section Relativity.Core

Value 31457280

Description This setting was deprecated in Relativity 8.1. Changing this value has no effect on the environment.

- ContentAnalystWebServicesURLBase

Section Relativity.Core

Value http://localhost:8080/CAT/services/

Description This setting was deprecated in Relativity 7.5. Changing this value has no effect on the environment.

- ConversionBatchSize

Section Relativity.Conversion

Value 500

Description Determines the maximum number of documents to submit for conversion at a time when running an imaging set.

This instance setting must be manually added to your environment.

- ConversionConvertAheadThreadCounts

Section Relativity.Core

Value 0

Value type Integer 32-bit

Description The maximum amount of threads that a Conversion Agent - Convert Ahead will use on its agent server.

- ConversionOnTheFlyThreadCounts

Section Relativity.Core

Value 0

Value type Integer 32-bit

Description The maximum amount of threads that a Conversion Agent - On the Fly will use on its agent server.

- ConversionPublishBatchSize

Section Relativity.Conversion

Value 500

Description Determines the maximum number of messages to submit at one time in a given conversion batch.

- ConversionMassConvertThreadCounts

Section Relativity.Core

Value 0

Value type Integer 32-bit

Description The maximum amount of threads that a Conversion Agent - Mass Convert will use on its agent server.

- ConversionRequestTimeout

Section Relativity.Conversion

Value 1

Description The amount of time, in minutes, before Relativity checks to see if Invariant has started working on a conversion job that Relativity sent to it.

- CookieDuration

Section Relativity.Authentication

Value 600

Description Sets the number of minutes that the authentication cookie is valid. This value controls the length of time that the users are logged in to Relativity before the system automatically logs them off and requires them to re-authenticate. This configuration value supports a maximum setting of 1440 minutes, or 24 hours, and a minimum setting of 240, or 4 hours. You must reset the IIS for these changes to take effect.

- CookieHttpOnly

Section Relativity.Authentication

Value True

Description Controls access to cookies. If set to True, this instance setting prevents access to cookies by JavaScript and other client-side elements. This flag is designed to attach to sensitive cookies such as the session cookie ASP.NET_SessionId.

Recommended security value

- Keep at default, unless your organization wants to further limit the amount of time one user’s Relativity session will last.

- Limiting this value decreases the chance an attacker could compromise the authentication cookie.

- CookieSecure

Section Relativity.Authentication

Value True

Description Controls how the web browser sends session information. If set to True, this instance setting forces a web browser to send session information over HTTPS only. This flag is designed to attach to sensitive cookies such as the session cookie ASP.NET_SessionId. When set to True, users cannot log in to Relativity over HTTP.

Recommended security value True - this ensures that, cookies, including sessions cookies, are encrypted over a secure SSL/TLS channel instead of being sent in cleartext. Once set to True, users must always access Relativity over HTTPS instead of HTTP.

- CopyFilesToRepository

Section kCura.EDDS.Winform

Value True

Description Determines the default value that appears in all import and export forms within the Relativity Desktop Client for the copy files to repository value.

- CreateCaseTimeoutValue

Section Relativity.Data

Value 1800

Description The timeout value, in seconds, associated with running queries related to case creation.

- CreateZSRTablesForSTRs

Section Relativity.Core

Value True

Description Controls whether search term reports create ZSR tables. If set to True, search terms reports create ZSR tables, caching the results for future use. This improves performance, but may make rebuilding and deleting indexes take longer. If set to False, building search terms reports may take longer. Fewer tables are left in the database, potentially resulting in faster dtSearch index builds.

- CustomPageDeletionDelay

Section kCura.Relativity.WebProcessing

Value 600

Description The amount of time, in seconds, that the system will wait before removing previous versions of a deployed custom page.

- CustomPageDeploymentManagerSleepTime

Section kCura.Relativity.WebProcessing

Value 0

Description The number of seconds the Custom Page Deployment Manager Agent will wait for a new version to become available.

- CustomPageDeploymentPath

Section kCura.Relativity.WebProcessing

Value blank

Description The server path that a Custom Pages will be deployed to. The MachineName should be set for each web server. If not set, Custom Pages will be deployed relative to the Relativity Web installation path.

- CustomPageManagerIsOffHourAgent

Section kCura.EDDS.Agents

Value True

Description Controls whether the Application Manager agent behaves as an off hour agent. If set to True, applications containing custom components only deploy between the hours set in the AgentOffHourStartTime and AgentOffHourEndTime values. If an application deploys when the AgentOffHourEndTime passes, the current deployment completes and no new deployments occur until the next AgentOffHourStartTime. If set to False, the Application Manager agent runs normally, and applications containing custom pages are identified and deployed in the typical process.

## D

- DatabaseQuery

Section kCura.EDDS.Procuro

Value SELECT CAST(1 AS BIT) AS [ ],

' N/A' as ArtifactID, 'EDDS' as

[Name], @@SERVERNAME as

[Location], 'N/A' as [CaseStatus],

'' as [UpgradeStatus] UNION

SELECT CAST(1 AS BIT) AS [ ],

CAST([Case].[ArtifactID] AS

VARCHAR(20)), [Case].[Name],

[ResourceServer].[Name] as

[Location], [Code].Name as Status,

'' as [UpgradeStatus] FROM

[Case] INNER JOIN [Code] ON [Code].

ArtifactID = [Case].StatusCodeArtifactID

INNER JOIN [Artifact] ON

[Artifact].[ArtifactID] = [Case].

[ArtifactID] AND [Artifact].[DeleteFlag]

= 0 INNER JOIN [ResourceServer] ON

[Case].[ServerID] =

[ResourceServer].[ArtifactID]

Description Defines the query that Procuro uses to determine the list of databases available for upgrading.

- DataCenter

Section kCura.Billing

Value Blank string ("")

Description Identifies the geographical location of the facility where a Relativity instance is housed. The Case Statistics Manager agent includes this location in the RelativityVersion.txt metadata file that it generates. See Case Statistics Manager.

- DataDirectory

Section kCura.EDDS.SqlServer

Value During Relativity installation

Description Identifies the path to the data directory that SQL Server uses. This value should be relative to the server where SQL Server is installed.

- DataFocusModeDefault

Section kCura.EDDS.Web

Value Off

Description Controls the default Interface Mode for users. If set to On, the default Interface Mode for users is Data Focus On. If set to Off, the default Interface Mode for users is Classic (No Data Focus).

- DataGridHttpClientTimeout

Section kCura.Audit

Value 100

Description This value is used to set the default value for the HttpClient timeout value for DataGridHttpClient specified in seconds.

- DataGridHttpClientTimeout

Section Relativity.DataGrid

Value 100

Description The default value, in seconds, for the HttpClient timeout value for DataGridHttpClient.

- DataGridIndexCreationSettings

Section Relativity.DataGrid

Value

"template": "text_*",

"mappings": {

"text": { "_id": {

"path": "artifactID"

}

},

"childtext": {

"_parent": {

"type": "text"

}

}

}

}'

Description Defines a template to create new indexes for Data Grid.

This instance setting must be manually added to your environment.

- DataGridIndexPrefix

Section Relativity.DataGrid

Value relativity

Description Constructs index names for Data Grid to distinguish multiple Relativity instances that write to the same Data Grid cluster.

- DataGridMultiIndexSplitSizeThreshold

Section kCura.Audit

Value 30 GB (32212254720 bytes)

Description Determines the maximum size, in bytes, of each shard in the Data Grid index before Relativity creates a new index. Writing to an index that is over the threshold causes Relativity to create a new index. Set this to 0 to disable the threshold behavior.

- DataGridMultiIndexSplitSizeThreshold

Section Relativity.DataGrid

Value 30GB (32212254720 bytes)

Description Determines the maximum size, in bytes, of each shard in the Data Grid index before Relativity creates a new index. Writing to an index that is over the threshold causes Relativity to create a new index. Set this to 0 to disable the threshold behavior.

- DataGridNumberOfRetries

Section Relativity.DataGrid

Value 3

Description Determines the number of attempts made by the Data Grid to perform an operation before it returns as a failure.

- DataGridNumberOfRetries

Section Relativity.Audit

Value 3

Description Number of attempts made by the Data Grid to perform an operation before it returns a failure.

- DataGridPayloadByteSizeThreshold

Section Relativity.DataGrid

Value 1048576

Description Determines the size, in bytes, of the internal write batch size for Data Grid.

- DataGridRESTservicePort

Section Relativity.DataGrid

Value 9400

Description Defines the port number that is used to connect JAVA CA connector to Data Grid REST service.

- DataGridRetryWaitTime

Section Relativity.DataGrid

Value 50

Description The amount of time, in milliseconds, that Data Grid waits between operation retries.

- DataGridRetryWaitTime

Section Relativity.Audit

Value 50

Description The amount of time, in milliseconds, that Data Grid waits between operation retries.

- DataGridScanScrollBatchSize

Section kCura.Audit

Value 1000

Description Determines the maximum batch size that Data Grid will attempt to read audits while performing an audit export operation. Default batch size set to 1000

- DataGridSearchCacheProviderTimeout

Section Relativity.Data

Value 60

Description The number of seconds that the workspace Last Update Time cache will be used from memory before refreshing with data from the Data Grid. Value 0 means the default value is used.

- DataGridSearchIndex

Section Relativity.DataGrid

Value 0

Description Enumeration specifying the default search index for Data Grid. 0:None, 1:Lucene.

- DataGridSqlTimeout

Section kCura.Audit

Value 30

Description The amount of time, in seconds, that Data Grid waits for SQL read operations to complete.

- DataGridVerification

Section Relativity.DataGrid

Value False

Description This instance setting enables post import data verification.

- DataGridVerificationTimeout

Section Relativity.DataGrid

Value 30

Description Determines the time span upon which post import data verification occurs.

- DeepPagingThreshold

Section kCura.Audit

Value 1000000000

Description If a workspace has a greater number of audits than this threshold, then paging will be restricted to DeepPagingMaxPages.

- DeepPagingMaxPages

Section kCura.Audit

Value 100

Description Maximum number of pages allowed to browse through Audits when a workspace has a number of audits greater than DeepPagingThreshold.

- DefaultCaseDownloadHandlerApplicationPath

Section kCura.EDDS.Web

Value During Relativity installation

Description Defines the value that populates in the Download Handler URL field by default for new cases. If you enter a URL for this value, the protocol must match what is used in the browser. If Relativity is set up to use either HTTP or HTTPS, but not both, you can enter a full URL. If Relativity is set up to use both HTTP and HTTPS, do not specify the protocol in this value.

- DefaultBrandingFont

Section Relativity.Production

Value Arial

Description The default branding font to be used in a production.

- DefaultBrandingFontSize

Section Relativity.Production

Value 10

Description This setting defines default branding font size for production. Font Size must be an integer between 8 and 30. If you set a value less than 8 or more than 30, the value will automatically update to 8 and 30 respectively.

- DefaultOIHiliteStyleID

Section kCura.Code.Data

Value 3

Description Determines the default OIHiliteStyle associated with new choices. Valid values are defined on the OIHiliteStyle table. Look within a workspace database, not the EDDS database.

- DefaultNativeImagingEngineURL

Section Relativity.Core

Value Determined during native imaging installation; manually entered in instance setting

after native imaging installation is completed.

Description This setting was deprecated in Relativity 7.5. Changing this value has no effect on the environment.

- DefaultQueryTimeout

Section kCura.AssistedReview

Value 30

Description The timeout value, in seconds, used by default for all AssistedReview queries.

- DefaultSqlCommandTimeout

Section kCura.Data.RowDataGateway

Value 30

Description The default wait time, in seconds, before terminating the attempt to execute a SQL command and generating an error. The value can be set globally or for a specific machine. The minimum possible value for this setting is 15 seconds and anything below that will result in a 15 second timeout. This value can be overridden by areas of the system where SQL execution is known to take longer. For example, you can use the MaxPDVQueryLength instance setting to configure the timeout value for list view queries.

- DefaultTextRedactionTextSize

Section kCura.EDDS.Web

Value -1

Description Determines the font size when a user draws a text redaction for the first time that session. -1 is auto mode.

- DefaultUseRelativityFormsValue

Section kCura.EDDS.Web

Value False

Description Enables or disables the rendering of Relativity dynamic object pages in a modern architecture. If True, the Object Type will be rendered using Relativity Forms when it has a null value for the Use Relativity Forms field. Otherwise, it will be rendered using Classic.

- DeleteFileErrorsLoggedAsWarnings

Section Relativity.Conversion.Cache

Value False

Description Determines the log level applied to delete file error log entries. If set to True, delete file errors are logged using a Warning log level. If set to False, delete file errors are logged using a Debug log level.

- DeleteFileWorkerBatchSize

Section Relativity.Conversion.Cache

Value 250

Description Specifies the delete file worker batch size to determine the max number of SQL identifiers contained within each message.

- DeleteFileWorkerParallelLinqEnabled

Section Relativity.Conversion.Cache

Value True

Description Determines whether PLINQ is used to optimize enumerating or deleting cached files in parallel.

- DeleteProductionFilesBatchSize

Section Relativity.Production

Value 10000

Description Determines the maximum number of produced files the Production agent can delete in a single batch.

- DeobfuscateMapsFolderPath

Section Relativity.Core

Value \Relativity\EDDS\Maps folder

Description Identifies the folder where the obfuscation map files are stored for use in the Stack Trace Deobfuscation Tool. If not set, the Stack Trace Deobfuscation Tool uses the ..\Relativity\EDDS\Maps folder.

- DeveloperMode

Section Relativity.Core

Value False

Description

Controls developer mode options within an instance of Relativity.

Setting this value to True enables developer mode options. Setting this value to False disables developer mode options. These options include disabling the cross-site request forgery (CSRF) header requirement in the API and returning detailed error messages such as stack traces. Enable this setting only in a development environment.

Recommended security value

False - Setting this value to false will cause Relativity to enforce the cross-site request forgery (CSRF) header requirement in the API and stop sending detailed error messages like stack traces.

- DisabledUserMessage

Section kCura.EDDS.Web

Value Your Relativity Administrator

Description Determines the contact specified within the message that appears when a user does not have access to Relativity.

- DiskSpaceAlertUpperThreshold

Section Relativity.Conversion.Cache

Value 70

Description Specifies the upper limit of the cache size as a percentage of the total space on the drive where the cache is stored. The Conversion Cache Manager creates an alert when the disk usage exeeds this value; otherwise, the alert is removed.

- DisplayDisclaimer

Section Relativity.Authentication

Value False

Description Sets the disclaimer display when users log in to Relativity. If True, displays the disclaimer. If False, does not display the disclaimer. For information on setting up the disclaimer message, see Setting up your workspace .

- DisplayHelpLink

Section Relativity.Core

Value True

Description Controls whether the Help link appears for all non-system admins. Setting this value to False removes the Help link from the UI.

- DisplayLogoInTitleBar

Section kCura.EDDS.Web

Value False

Description Controls whether the company logo appears in the top action bar. If set to True, the company logo appears in the top action bar.

- DistinctBuilderMaxValue

Section Relativity.Data

Value 255

Description The maximum number of values allowed in a choice field before it changes from a picker in the item list to disabled. For non-required fields, null, or empty, values count towards the maximum number.

- DocumentLimitForMassImaging

Section Relativity.Imaging

Value 10,000

Description The maximum number of documents that can be submitted for the Mass Imaging action. If a user attempts to mass image and the number of documents selected exceeds this value, a warning appears to prevent the user from performing this action to suggest creating an Imaging Set as best practice.

- DocumentSkipDefaultBehaviorDefault

Section kCura.EDDS.Web

Value True

Description Determines the default value displayed in the Skip Default Preference field on the Add User form. The UI displays Skip when this instance setting value equals True, and it displays Normal when it equals False. This setting is only valid if DocumentSkipEnabledDefault is set to True.

DocumentSkip

EnabledDefault DocumentSkip

DefaultBehaviorDefault Skip Default Preference field

(UI display)

Enabled True Skip

Enabled False Normal

Disabled Setting Ignored Normal (Read-only)

Force Enabled Setting Ignored Skip (Read-only)

- DocumentSkipEnabledDefault

Section kCura.EDDS.Web

Value Enabled

Description Determines the default value displayed in the Document Skip field on the Add User form. Acceptable values are Enabled, Disabled, and Force Enabled. When this option is Enabled, the value for DocumentSkipDefaultBehaviorDefault controls the default option displayed in the Skip Default Preference field. When this option is set to Disabled, or Force Enabled, the Skip Default Preference field displays the read-only value of Normal or Skip, respectively.

DocumentSkip

EnabledDefault DocumentSkip

DefaultBehaviorDefault Skip Default Preference field

(UI display)

Enabled True Skip

Enabled False Normal

Disabled Setting Ignored Normal (Read-only)

Force Enabled Setting Ignored Skip (Read-only)

- DocumentSkipLookaheadLength

Section kCura.EDDS.Web

Value 1000

Description Determines the progressive number of documents, starting with the current +1, that the system will evaluate against the current view or saved search criteria when Document Skipping is enabled. System default is 1000 documents, set to -1 for all documents.

- DocumentSkipNoMoreDocumentsMessage

Section kCura.EDDS.Web

Value Document Skip is enabled. The remaining documents in your queue no longer meet the conditions of your view or search. If you are done with these records, click \"Return to document list\". If you would like to see the remaining records, change your view from \"Skip\" to \"Normal\".

Description Determines the text in the notification sent to a user when Document Skip is enabled, and no more documents fit the saved search/view criteria.

- DocumentSkipToolTip

Section kCura.EDDS.Web

Value This checkbox will enable you to bypass documents which already meet the criteria of this saved search/view.

Description Determines the text in the document skip tool tip message displayed in the document profile.

- DocumentTimeout

Section kCura.EDDS.Web

Value 120000

Description The amount of time, in milliseconds, until the Viewer will timeout when attempting to retrieve a document.

- DocumentViewerSleepTime

Section Relativity.Core

Value 500

Description Document viewer can load to sleep, in milliseconds, if it encounters a file exception while trying to load the file.

- DomainNameWhiteListUrls

Section kCura.EDDS.Web

Value * (all URLs are accepted)

Description Defines the allowable list of external domains available for navigation or display within a tab. Semicolon-delimited list of whitelisted domains. For example, "google.com;mozilla.org".

- DomainParsingSingleRecordMaxByteThreshold

Section Relativity.Data

Value 1048576

Description The maximum length, in bytes, of a record that the Domain Parsing tool will parse. The Domain Parsing tool will not parse a record with a value that exceeds this length.

- DotNetEventCounterIntervalSeconds

Section Relativity.OpenTelemetry

Value 5

Description The Open Telemetry SDK .NET Framework event counter interval in seconds.

- dtSearchDataGridBufferSize

Section Relativity.Data

Value 16777216

Description The size, in bytes, of the cache used to bulk read non-streamable documents from Data Grid to dtSearch.

- dtSearchDefaultAlphabetFileText

Section Relativity.Core

Value Listed in dtSearch default alphabet file text .

Description Determines the default value of the text for the Alphabet file when creating a new dtSearch index. Acceptable values are listed in the dtSearch default alphabet file text page in our documentation.

- dtSearchDefaultSubIndexFragmentationThreshold

Section Relativity.Core

Value 9

Description Determines the default value for the Sub-index fragmentation threshold field on the dtSearch Index Information screen. The value must be an integer greater than or equal to 1. When the fragmentation level for a sub-index equals or exceeds the threshold level, the system automatically compresses the sub-index during an incremental build.

- dtSearchDefaultSubIndexSize

Section Relativity.Core

Value 250000

Description Determines the maximum number of documents to build into each sub-index. The dtSearch Index Manager uses this value to determine how many sub-indexes will make up the entire index. This value appears by default in the Sub-index size field when creating a dtSearch.

- dtSearchEnableMetricsLogging

Section Relativity.Data

Value 0

Description Determines if dtSearch Metrics gathering should be enabled for Performance testing or Troubleshooting. This is a Bit value.

- dtSearchPopulationLogFilePath

Section Relativity.Core

Value blank

Description Identifies a path to a file on the disk when diagnosing dtSearch problems related to populating indexes. Setting this instance setting causes dtSearch to write debugging information to the disk. This file itself does not need to exist, but the path to it does. Ensure you change this value to blank when you no longer need the file log because it can grow in size very quickly.

- dtSearchQueryLogFilePath

Section Relativity.Core

Value blank

Description Identifies a path to a file on the disk when diagnosing dtSearch problems related to performing searches. Setting this value causes dtSearch to write debugging information to the disk. This file itself does not need to exist, but the path to it does. Ensure you change this value to blank when you no longer need the file log because it can grow in size very quickly.

- dtSearchStreamBufferSize

Section Relativity.Data

Value 1048576

Description Determines the size, in bytes, of the buffer used within the dtSearchStream object. This buffer is allocated into memory as soon as the agent starts. Relativity checks to see if the value has changed between jobs and reallocates the buffer if a change is detected. Increasing this value may slightly improve build times, but requires the agent server to use additional memory.

- dtSearchStreamThresholdInBytes

Section Relativity.Data

Value 1048576

Description Determines the maximum size of all text associated within a document before the text is streamed directly into dtSearch. The dtSearch Index Managers uses this value when populating an index. If the size of all the text associated with a document is larger than this value, the text is streamed directly into dtSearch. Otherwise, the text is converted to bytes and the bytes are sent to dtSearch. Increasing this value may slightly improve build times, but will increase the chance of your agent server running out of memory.

- dtSearchWorkerProgressThreshold

Section Relativity.Data

Value 1000

Description Determines the number of documents a worker agent sends to the dtSearch engine before reporting progress back to the database. Changing this value may have an impact on performance.

- DynamicReviewQueueAutoConvert

Section Relativity.Core

Value True

Description Indicates whether or not documents will be automatically converted when added to a Dynamic Review Queue.

- DynamicReviewQueueInsertBatchSize

Section Relativity.Data

Value 500

Description How many documents to insert into a Dynamic Review Queue at once.

## E

- EDDSFileShare

Section Relativity.Data

Value During Relativity installation

Description Identifies the location used for the primary-level file share. If you change the location, make sure to share the new directory.

- ElasticsearchMajorVersion

Section kCura.Audit

Value 2

Description Specifies the major version of Elasticsearch that the cluster is running

- ElasticValidationInterval

Section kcura.Audit

Value 5

Description

This instance setting must be manually added to your environment.

Validates the elastic search connectivity based on the interval value provided, in seconds. If no value is set, default value is 3600 seconds.

- EmailFrom

Section kCura.Notification

Value blank

Description Determines the email address populated in the From field when sending email notifications. The email address must be valid. Email aliases can be entered in this format: Alias Name <username@example.com>

- EmailLinkURLOverride

Section kCura.EDDS.Web

Value https://relativity.relativity.com

Description Specifies the URL for the server if it’s behind a load balancer or a firewall with HTTPS handled by the firewall or load balancer. Set this instance setting only when the URL used to access Relativity by end users is not the actual URL of the Relativity web server. The Viewer's Email Link to Document functionality uses this setting. Format: https://servername

- EmailTo

Section kCura.Notification

Value blank

Description Determines the email address populated in the To field when sending email notifications. The email address must be valid. Separate multiple email addresses with a semicolon.

This instance setting must be manually added to your environment.

- EnableCustomPageReadinessCheck

Section kCura.Relativity.WebProcessing

Value True

Description When true, the Custom Page Deployment Manager will attempt to invoke an application's custom page readiness endpoint before routing requests to its web pages. The optional readiness endpoint can be configured by application developers to provide a way of performing start up tasks.

- EnableCustomerLockbox

Section Relativity.Core

Value False

Description If this is set to True, users must belong to a security Group with access to the workspace they want to access other than System Administrators to access this workspace. If the instance setting is set to False, the system behaves as it always has and system administrator access is sufficient in order to access any workspace.

- EnableDocumentPreview

Section Relativity.ReviewInterface

Value True

Description If this is set to True, the Viewer is available as a preview panel in the document list for users with appropriate permissions. If the instance setting is set to false, the preview panel is not available in the document list.

- EnableDocumentViewerProgressiveLoad

Section kCura.EDDS.Web

Value True

Description

If this is set to True, the Viewer, which displays the document, will load first. This is followed by the navigation toolbar above the Viewer and the coding pane to the right which contains the layout. If this is set to False, the navigation toolbar and the coding pane begin loading at the same time. The Viewer begins loading as soon as the navigation toolbar has loaded.

- EnableNativeRedactions

Section kCura.EDDS.Web

Value True

Description Determines whether native highlighting, redactions, links, and tagging are enabled. If set to True, these actions are enabled. If set to False, these actions are disabled. Redactions and highlighting can be used on transcripts.

This instance setting must be manually added to your environment.

- EnablePublishErrorAutoRetry

Section Relativity.Core

Value True

Description

Determines whether Processing publishing will automatically reduce the number of threads in use. This only occurs in deadlock or timeout scenarios during publish. Keeping the value at True can impact publish performance.

- EnableSmartPipeline

Section Relativity.Core

Value True

Description Determines whether the ability to use SmartPipeline on Analytics Index is enabled. If set to True, this action is enabled. If set to False, these actions are disabled.

- EnableUserGroupOptimization

Section Relativity.Core

Value False

Description

Allows administrators to turn-off email notifications for when users or groups are added or deleted.

- EnforceHttps

Section Relativity.Authentication

Value Warn

Description

Controls how Relativity Service Host handles HTTP/HTTPS traffic. Values include On, Off, and Warn.

If set to On, this instance setting forces Service Host to use HTTPS only. If set to Off, HTTP traffic is allowed. If Warn, the browser and all API endpoints will allow any traffic but will log a warning. The default value is Warn.

Recommended security value

On - make sure to add a certificate to the Personal certificate store of the Computer Account on all web and agent servers. If the certificate is self-signed, you must add it to both the Personal and the Trusted Root Certification Authorities certificate stores for the Computer Account on all web and agent servers. It is also a requirement that you edit the value of the KeplerServicesUri instance setting and the KeplerServicesUriForAgents instance setting to reflect HTTPS. This requires Service Host traffic to be encrypted with SSL/TLS in order to not send in cleartext.

- EnvironmentData

Section kCura.LicenseManager

Value xxxx

Description Do not modify without advice from Relativity Customer Support. Determines encrypted data about your environment. Changing this shuts down Relativity.

- EnvironmentName

Section kCura.Notification

Value DefaultRelativityEnvironmentName

Description Defines the name of the environment. This value is used when sending notifications. You should update the default value to a setting appropriate for use in your environment.

- EnvironmentPubToken

Section kCura.LicenseManager

Value xxxx

Description Do not modify without advice from Relativity Customer Support. Defines Relativity ODA LLC's public key.

- ESIndexCreationSettings

Section kCura.Audit

Value Click here to view default Data Grid template

```text
{
                "order": 0,
                "index_patterns": ["audit_*"],
                "settings": {
                    "index": {
                    "max_result_window": "2147483647",
                    "analysis": {
                        "filter": {
                        "substring": {
                            "type": "nGram",
                            "min_gram": "1",
                            "max_gram": "20"
                        }
                        },
                        "analyzer": {
                        "lwhitespace": {
                            "filter": [
                            "lowercase"
                            ],
                            "tokenizer": "whitespace"
                        },
                        "str_index_analyzer": {
                            "filter": [
                            "lowercase",
                            "substring"
                            ],
                            "tokenizer": "keyword"
                        },
                        "str_search_analyzer": {
                            "filter": [
                            "lowercase",
                            "substring"
                            ],
                            "tokenizer": "keyword"
                        }
                        }
                    },
                    "number_of_shards": "1",
                    "number_of_replicas": "1"
                    }
                },
                "mappings": {
                    "audit": {
                    "dynamic_templates": [
                        {
                        "details_run_item_as_text": {
                            "path_match": "Details.auditElement.run.item.*",
                            "mapping": {
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                },
                                "type": "text"
                            }
                        }
                        },
                        {
                        "raw": {
                            "match_pattern": "regex",
                            "path_match": "Details\\.auditElement\\..*",
                            "mapping": {
                            "type": "text",
                            "fields": {
                                "raw": {
                                "analyzer": "lwhitespace",
                                "type": "text"
                                }
                            }
                            },
                            "match_mapping_type": "string"
                        }
                        },
                        {
                        "newvalue": {
                            "match_pattern": "regex",
                            "path_match": ".*\\.newValue$",
                            "mapping": {
                            "type": "text",
                            "fields": {
                                "raw": {
                                "analyzer": "lwhitespace",
                                "type": "text"
                                }
                            }
                            }
                        }
                        },
                        {
                        "oldvalue": {
                            "match_pattern": "regex",
                            "path_match": ".*\\.oldValue$",
                            "mapping": {
                            "type": "text",
                            "fields": {
                                "raw": {
                                "analyzer": "lwhitespace",
                                "type": "text"
                                }
                            }
                            }
                        }
                        },
                        {
                        "analytics_text": {
                            "match_pattern": "regex",
                            "path_match": ".*\\.#text$",
                            "mapping": {
                            "type": "text",
                            "fields": {
                                "raw": {
                                "analyzer": "lwhitespace",
                                "type": "text"
                                }
                            }
                            }
                        }
                        }
                    ],
                    "properties": {
                        "Guid": {
                            "type": "keyword"
                        },
                        "ActionName": {
                            "type": "keyword"
                        },
                        "UserName": {
                            "type": "keyword"
                        },
                        "Details.auditElement.field.@id": {
                            "type": "keyword"
                        },
                        "TimeStamp": {
                            "format": "strict_date_optional_time||epoch_millis",
                            "type": "date"
                        }
                    }
                    }
                },
                "aliases": {
                    "{index}_write": {},
                    "{index}_read": {},
                    "{index}_verify": {}
                }
}
```

Description Defines a template to create new indexes for Data Grid.

This instance setting must be manually added to your environment.

- ESIndexPrefix

Section kCura.Audit

Value

Description Constructs index names for Data Grid. This instance setting can be used to distinguish multiple Relativity instances that write to the same Data Grid cluster.

This instance setting must be manually added to your environment.

- ESPayloadSettings

Section kCura.Audit

Value

Description Defines Data Grid settings attached to every payload.

- ExplicitBrowserWhitelist

Section Relativity.Authentication

Value Mozilla/[0-9].[0-9] \(Windows.+; .+; Trident/[7-9].[0-9]; rv:[0-9][0-9].[0-9]\) like Gecko\nMozilla/[0-9].[0-9] \(Windows.+; .+; Trident/[7-9].[0-9]; .+; rv:[0-9][0-9].[0-9]\)

Description Do not modify without advice from Relativity Customer Support. A list of regular expressions which are always allowed to access Relativity even if unsupported. Correct function of browsers added to this list by users is not guaranteed. List separated by \n.

- ExportBatchSize

Section kCura.IntegrationPoints

Value 1000

Description The number of records being exported in a batch through an Integration Points job.

- ExportEscapedFormulasFromItemListDefault

Section Relativity.Core

Value Yes

Description

Yes—escapes excel macro syntax starting characters: [@=+-$] •

No—does not escape excel macro syntax starting characters

Recommended security value

Yes - this will ensure Excel macro syntax starting with [@=+-$] are always escaped.

- ExportLargeAuditDetails

Section kCura.Audit

Value False

Description If True, audit migration will export audit details with byte size exceeding the setting, DataGridMaximumFieldSizeInBytes, to the workspace's Default File Repository folder location.

- ExportSubdirectoryDigitPadding

Section kCura.EDDS.Winform

Value 3

Description Determines the default value that appears in the Relativity Desktop Client export form for the volume subdirectory digit padding value.

- ExportThreadCount

Section kCura.IntegrationPoints

Value 4

Description

This value represents the number of threads the RDC uses to export natives, images, productions, and text. The maximum value is 8.

This setting defines the amount of threads used for parallelization. It does not affect the performance of RIP jobs. The default value is 4, but for more powerful machines it can be increased to 8.

- ExportVolumeDigitPadding

Section kCura.EDDS.Winform

Value 2

Description Determines the default value that appears in the Relativity Desktop Client export form for the export volume digit padding value.

- Export.LoadFile.ErrorNumberOfRetries

Section kCura.IntegrationPoints

Value 2

Description This value controls the number of times the Integration Points retries an operation within an export load file process after a non-IO failure

- Export.LoadFile.ErrorWaitTime

Section kCura.IntegrationPoints

Value 10

Description This value sets the number of seconds the Integration Points waits before retrying an operation within an export load file process after a non-IO failure

- Export.LoadFile.IOErrorNumberOfRetries

Section kCura.IntegrationPoints

Value 2

Description This value controls the number of times the Integration Points retries an operation within an import or export load file process after IO/WebAPI failure occurs

- Export.LoadFile.IOErrorWaitTime

Section kCura.IntegrationPoints

Value 20

Description This value sets the number of seconds the Integration Points waits before retrying an operation within export load file process that encountered an IO/WebAPI failure

- ExternalStylesheetUrls

Section Relativity.Conversion

Value blank

Description Defines the external stylesheets to include in every converted document. These entries are separated by semicolons. By default this is empty.

- ExpireInactiveJobHours

Section Relativity.Conversion.Cache

Value 12

Description The number of hours of job inactivity before an unfinished job is expired.

## F

- FavoritesEnabled

Section Relativity.Core

Value TRUE

Description Determines if Favorites appears in the UI. If set to True, Favorites appears in the UI. If set to False, Favorites does not appear in the UI.

- FileBrowserMaximumElements

Section kCura.EDDS.Agents

Value 1000

Description Determines the maximum number of files or folders that the directory displays in a file browser.

- FileDeleteChunkSizeOnDocumentDelete

Section Relativity.Data

Value 1000

Description Determines the number of records that are deleted at once from associated tables when documents are deleted in mass.

- FileDeletionManagerBatchAmount

Section kCura.EDDS.Agents

Value 100

Description Determines the number of documents that the File Deletion Manager deletes in a single batch.

- FileTypesToDownloadAsAttachments

Section kCura.EDDS.Web.Distributed

Value txt;vsd;vsdx;xls;xlsx;doc;docx;

Description A semicolon-delimited list of file extensions, not including periods, users would like to download as attachments rather than inline from the native viewer. For example, txt;vsd;vsdx;.

- FluidReviewQueueSize

Section Relativity.Data

Value 5000

Description The maximum number of documents in a set displayed in the Review Interface. This is set to 5,000 by default.

- ForceWebClientManagerUpgrade

Section kCura.EDDS.Web

Value False

Description Controls whether Internet Explore compares the user’s web client manager version to the Relativity version. If set to True, Internet Explorer compares the user’s web client manager version to the Relativity version. If the versions do not match, Internet Explorer automatically prompts the user to install a new version of web client manager. If set to False, Internet Explorer does not compare the user’s web client manager version to the Relativity version, and it does not prompt the user to install a new version.

- ForgotPasswordRequestBody

Section Relativity.ForgotPassword

Value <HTML><BODY> <P>We received a request

to reset the password associated with this email address.

Click the link below to reset your password.

This link will expire after 15 minutes

.<BR/><BR/> {RESETLINK}<BR/><BR/>

We recommend opening this link in Internet Explorer.

<BR/><BR/> You can also copy and paste the

following text into your address bar:

<BR/><BR/> {RESETTEXT}<BR/><BR/>

If you did not request this change, contact your system admin.<BR/><BR/> Please do not reply to this email.<BR/><BR/></P></BODY></HTML>

Description Determines the text in the body of the forgotten password request email message.

- ForgotPasswordRequestCompletedBody

Section Relativity.ForgotPassword

Value <HTML><BODY> <P>The password associated

with this email address has been successfully reset.

Click the link below to login.<BR/><BR/>

{LOGINLINK}<BR/><BR/> We recommend

opening this link in Internet Explorer.

<BR/><BR/> You can also copy and paste

the following text into your address bar:<BR/><BR/>

{LOGINTEXT}<BR/><BR/>

If you did not request this change, contact your system admin.<BR/><BR/>

Please do not reply to this email.<BR/><BR/></P>

</BODY></HTML>

Description Determines the text in the body of the forgotten password request email message when the request has been completed.

- ForgotPasswordRequestEmailFrom

Section Relativity.ForgotPassword

Value PasswordReset@relativity.com

Description Determines the value in the From field for the forgotten password request email message.

- ForgotPasswordRequestInvalidBody

Section Relativity.ForgotPassword

Value <HTML><BODY> <P>We received a request

to reset the password associated

with this email address.

<BR/><BR/> Your password cannot be

reset due to a problem with your account.

Contact your system admin for assistance.

<BR/><BR/> If you did not request this change,

contact your system admin.

<BR/><BR/> Please do not reply to this email.<BR/><BR/></P></BODY></HTML>

Description Determines the text in the body of the forgotten password request email message if the user is locked out.

- ForgotPasswordRequestSubject

Section Relativity.ForgotPassword

Value Password reset request

Description Determines the value in the Subject field for the forgotten password request email message.

- FriendlyInstanceName

Section Relativity.Authentication

Value Varies (string value)

Description A friendly name that will display on the user's drop-down menu for the current instance.

- FTDirectory

Section kCura.EDDS.SqlServer

Value During Relativity installation

Description Identifies the path to the full text directory used by SQL Server. This value should be relative to the server where SQL Server is installed.

## G

- GlobalWorkspaceUpgradeLimit

Section Relativity.Data

Value 4

Description Determines the global limit on the maximum number of Workspace Upgrade Worker agents that can access any of the SQL Servers in your Relativity environment. Each SQL Server can have a different number of these agents accessing it, but the maximum number accessing a single server canno exceed the global limit set in this instance setting. To set the number of agents on a specific server, see Servers .

## H

- HeadedLogo

Section kCura.WorkspacePortal

Value https://www.relativity.com/app/themes/kcura/assets/img/logo-kcura.png

Description

The URL of the image you want to show. The value of this instance setting can support relative and absolute paths. For Relative Path, assume your path is preceded by the URL of your instance. For example, http://relativityvm/relativity/.

Absolute path sample: https://www.relativity.com/app/themes/kcura/assets/img/logo-kcura.png

Relative path sample: images/relativityLogin.png

- HeaderLogo

Section kCura.EDDS.Web

Value blank.gif kcura_blue.png

Description Identifies the name of the image file Relativity uses for the header. This file must be located within the Images folder.

- HeaderLogoLarge

Section kCura.EDDS.Web

Value blank.gif kcura_blue_50.png

Description Identifies the name of the large image file Relativity uses for the header. This file must be located within the Images folder.

- HeartbeatCreateIndexRetryWaitTime

Section Relativity.DataGrid

Value 5000

Description Determines the wait time before the final retry attempt at creating new Data Grid index after receiving CreateIndex failed exception

- HelpLinkURL

Section kCura.EEDS.Web

Value https://help.relativity.com/<RELEASE NUMBER>/Content/index.htm

Description

Specifies the URL for the help link in the user drop-down menu.

This instance setting must be manually added to your environment.

-

- HideProcessTranscriptsMassOperation

Section Relativity.Core

Value True

Description Controls the default visibility of the Process Transcripts mass operation. If set to True, the Process Transcripts option will be hidden by default in the Mass Operations menu.

- HostNameSiteUrlOverride

Section Relativity.Authentication

Value myrelativityURL.company.com

Description Optional. Specifies an additional public site URL for use with SAML2 or OpenID Connect authentication providers. Create an additional copy of this instance setting for each web server that is used for the specified URL.

Machine Name - myWebServer

- HoursToRetainConvertedDocuments

Section Relativity.Core

Value 72 hours

Description If the last accessed time is more than the hour limit you select, when UseTimeBasedConvertedCacheManagement is enabled, cache files are deleted.

- HTMLEditorToolbar

Section kCura.Web.UI.WebControls

Value [[ 'fontname', 'space','fontsize', 'space','formatblock', 'space','bold', 'italic', 'underline', 'separator','strikethrough', 'subscript', 'superscript', 'separator','copy', 'cut', 'paste', 'space', 'undo', 'redo' ], [ 'justifyleft', 'justifycenter', 'justifyright', 'justifyfull', 'separator', 'orderedlist', 'unorderedlist', 'outdent', 'indent', 'separator','forecolor', 'hilitecolor', 'textindicator', 'separator','inserthorizontalrule', 'createlink', 'insertimage', 'inserttable']]

Description

A list of options used by the HTMLEditorToolbar. This is used within rich text fields.

- HTMLExternalLinkAllowList

Section Relativity.DocumentViewer

Value Type Text

Description

A space separated list of external URLs embedded in the document to be allowed during conversion. Example: //xyz.corp/ //emttest/

You must manually create this instance setting because it's not installed by default.

## I

- IAPICommunicationMode

Section DataTransfer.Legacy

Value ForceKepler

Description Default communication mode for import, DataTransfer.Legacy.

- IgnoreCertificateErrors

Section Relativity.Authentication

Value False

Description Determines whether Relativity must validate the chain of trust of certificates when running over HTTPs. Setting the value to True is a security vulnerability and should only be done in testing environments. Recommended value is False.

Recommended security value

False - it is not secure to ignore certificate errors in Relativity.

- ImageExportThreshold

Section Relativity.Core

Value 300

Description The amount of time, in seconds, that the TIFNative manager waits for a single document to export before canceling the imaging export process and moving to the next document.

- ImageOnTheFlyJobPriorityDefault

Section Relativity.Core

Value 1

Description The default priority for all image-on-the-fly jobs.

- ImageViewerBufferSize

Section kCura.EDDS.Web

Value 10485760

Description Determines the maximum number of bytes that the Image Viewer will preload into memory.

- ImageViewerContinuousPagingThreshold

Section kCura.EDDS.Web

Value 500

Description Determines the maximum number of pages to view continuously in the Image Viewer before switching to Single Paging Mode.

- ImagingBatchSize

Section Relativity.Imaging

Value 500

Description Determines the maximum number of documents to submit for imaging at a time.

- ImagingBatchSubmitMaxRetries

Section Relativity.Conversion

Value 3

Description The maximum number of times a user can retry each batch of documents for conversion.

- ImagingJobCleanupInterval

Section Relativity.Conversion

Value 1440 60

Description The amount of time, in minutes, between attempts to clean up stalled imaging jobs. The default is 1440 minutes, which is 24 hours.

- ImagingJobPriorityDefault

Section Relativity.Core

Value 100

Description Determines the default priority for all Imaging jobs, excluding image-on-the-fly jobs.

- ImagingRequestTimeout

Section Relativity.Conversion

Value 1

Description The amount of time, in minutes, the system waits before checking an imaging request made to Invariant. The default is 1 minute.

- IngestionTemporaryFileCacheLocation

Section Relativity.DataGrid

Value <<default relativity file share>>/datagrid

Description The location on disk where Relativity writes temporary files while ingesting documents into Data Grid.

- InitialNumberOfViewableDocuments

Section Relativity.Core

Value 1000

Description Determines the initial number of viewable items on list pages. It's the value in the First xxx drop-down menu on the bottom of various list pages.

- InMaintenanceMode

Section Relativity.Authentication

Value False

Description Enables or disables maintenance mode. When you enable maintenance mode, Relativity only allows users in the System Administrators group to log in to the environment. If a user from another group attempts to log in, Relativity displays the following message on login page: Environment is in maintenance mode. You can also give access to specific groups in Relativity by updating the AllowMaintenanceModeAccessToGroups instance setting. The InMaintenanceMode instance setting is not encrypted.

- Instance

Section kCura.LicenseManager

Value UNSETINSTANCE

Description Controls the prefix for several columns in two Relativity scripts. In the Case User Rollup script, this value is the prefix for the Case User ID and Usage ID columns. In the Case Statistics Rollup script, this value is the name of the Instance column, as well as the prefix in the Usage ID, Case ID, and Name column. Changing this value immediately invalidates your Relativity and Processing license.

- InvariantApiKeplerPort

Section Relativity.ApplicationBase

Value 8092

Description The port on the Worker Manager Server that is hosting the Kepler Invariant API.

- InvariantApiWcfPort

Section Relativity.ApplicationBase

Value 6859

Description The port on the Worker Manager Server that is hosting the WCF Invariant API.

- InvariantFileDeletionServiceTimeout

Section Relativity.Core

Value 300

Description The amount of time, in seconds, that must elapse while Invariant returns no files for deletion before the Invariant File Deletion Kepler Service times out.

- InvariantDatabaseServerl

Section kCura.ARM

Value None

Description Name of the primary Invariant SQL Server. For example, the SQL Server on which the Invariant database can be found.

- InvariantFileShare

Section kCura.ARM

Value None

Description Indicates the BCPPath to be used for each Invariant SQL Server. If there are multiple Invariant SQL Servers in the environment, add one entry for each with the machine name set to the SQL Server name.

- InvariantQueueManagerServerDomain

Section Relativity.ApplicationBase

Value relativity.corp

Description The domain name for Invariant's Queue Manager server. This instance setting is created by the Invariant Queue Manager, and used by Relativity when constructing the endpoint for Kepler calls to Invariant.

- InvitationEmailRequestBody

Section Relativity.Authentication

Value <HTML><BODY> <P>Your administrator has configured a Relativity account for you at the following URL:<BR/><BR/> <a href="{LINKTEXT}">Log in to Relativity</a><BR/><BR/> Click this link to access Relativity. You can also copy and paste the following text into your address bar:<BR/><BR/> {LINKTEXT}<BR/><BR/> If you were not expecting this e-mail, please contact your system administrator.<BR/><BR/> Please do not reply to this email.<BR/><BR/></P></BODY></HTML>

Description The Invitation Workflow request email message text. The email text must be formatted as HTML.

- InvitationEmailRequestFrom

Section Relativity.Authentication

Value PasswordReset@relativity.com

Description The Invitation Workflow request email message sender.

- InvitationEmailRequestSubject

Section Relativity.Authentication

Value Welcome to Relativity

Description The Invitation Workflow request email message subject.

- InvitationLinkLifetimeInMin

Section Relativity.Authentication

Value 10080

Description The number of minutes the link sent in the Invitation Email remains valid.

Recommended security value

- Determine how much time your organization is comfortable having links remain valid before sending a new email.

- The longer the link remains viable, the more chance it could be compromised.

- IsOnlineInstance

Section kCura.LicenseManager

Value True

Description Do not modify without advice from Relativity Customer Support. Indicates whether the Relativity instance is enabled to connect to the internet to automatically transmit system usage and billing data to Relativity ODA LLC.

- IsPerformanceEnabled

Section Relativity.Core.Log

Value 10080

Description Do not modify without advice from Relativity Customer Support. Determines whether Relativity logs performance metrics. Set this to True to log performance metrics.

- ItemListPreConvertCacheSize

Section Relativity.Core

Value 10

Description Determines the number of documents to convert, natives and images, sent for mass conversion when the Document list page loads. If value is set to 0 or lower, Item List pre-conversion will be disabled.

## J

- JobCompleteHealthCheckMaxHours

Section Relativity.Conversion.Cache

Value 72

Description Defines the time period in which at least 1 clear conversion cache job per cache location resource server should have successfully completed. This is used by the job completed health check.

- JobCompleteHealthCheckUnsuccessfulJobsBeforeUnhealthy

Section Relativity.Conversion.Cache

Value 5

Description Defines the number of consecutive unsuccessful jobs allowed per cache location resource server before the application is considered unhealthy. This is used by the job completed health check.

## K

- KeplerServicesUri

Section Relativity.Core

Value http://localhost/Relativity.Rest/API/

Description Specifies the URL at which Relativity custom pages and event handlers can access the Services API Kepler services using API helpers. The URL must end in a forward slash.

This instance setting must be manually added to your environment.

Recommended security value

- Change the link from http to https. For example, change http://localhost/Relativity.Rest/API/ to https://localhost/Relativity.Rest/API/ .

- If EnforceHTTPS was set to True, this needs to be set to HTTPS instead of HTTP.

- KeplerServicesUriForAgents

Section Relativity.Core

Value http://127.0.0.1:8990/Kepler

Description Specifies the URL at which Relativity agents can access local Services API Kepler services using API helpers. The default port number, 8990, can be changed if there is a port conflict with some other server application.

Recommended security value

- Change the link from http to https. For example, change http://127.0.0.1:8990/Kepler to https://127.0.0.1:8990/Kepler .

- Set EnforceHTTPS to True if this value is set to HTTPS instead of HTTP.

- KeyboardShortcutsDefault

Section kCura.EDDS.Web

Value True

Description Controls the default value for enabling keyboard shortcuts for new users. If set to True, keyboard shortcuts are enabled for new users. If set to False, keyboard shortcuts are not enabled for new users.

## L

- LastAccessedBatchTimerInterval

Section Relativity.Conversion

Value 10 seconds

Description

The amount of time, in seconds, between updates to the LastAccessed column on the ConvertedCacheFile table associated with the cache IDs for a group of converted documents. Relativity tracks the date and time when a user last converted the document to determine how long to store the document in the cache. To monitor these time intervals, it updates the information stored in this column by batches based on the time interval set in this instance setting or on the number of records set in LastAccessedBatchRecordSizeLimit, depending on which limit is met first. For more information, see LastAccessedBatchRecordSizeLimit .

You can increase the setting for this value and the LastAccessedBatchRecordSizeLimit if your SQL Server experiences a high number of requests for updates. This change causes the web server to retain more data in memory before sending a database request. Alternatively, you can decrease this setting if the web server is running out of memory because it is holding too many documents.

- LastAccessedBatchRecordSizeLimit

Section Relativity.Conversion

Value 500

Description

Determines the maximum number of cache IDs added to a batch before Relativity updates the date and time information stored in the LastAccessed column on the ConvertedCacheFile table for these converted documents.

You can increase the value for this instance setting and the LastAccessedBatchTimerInterval instance setting if your SQL Server experiences a high number of requests for updates. This change causes the web server to retain more data in memory before sending a database request. Alternatively, you can decrease this value if the web server is running out of memory because it’s holding too many documents. For more information, see LastAccessedBatchTimerInterval .

- LdapTemplateUserID

Section kCura.EDDS.Agents

Value 9

Description Do not modify without advice from Relativity Customer Support. Identifies the Relativity User Id to use as a template when the LdapUserManager Agent creates users. This is used when integrating Relativity and Active Directory.

- LDFDirectory

Section kCura.EDDS.SqlServer

Value C:\Logs\

Description Identifies the path to the log file directory that the SQL Server uses. This value should be relative to the server where SQL Server is installed.

- LegacyAuditCutoff

Section kCura.EDDS.Web

Value 7/23/2008 3:16:57 PM

Description Defines the date that the environment was upgraded to 4.20. It's used within messages explaining to the user that audit framework changed.

- LibraryApplicationPath

Section kCura.EDDS.Procuro

Value C:\Program Files\kCura Corporation\Relativity\\Procuro\LibraryApplications\

Description Identifies the root path where Procuro looks for Relativity Library Applications.

- LoadImportedFullTextFromServer

Section Relativity.Data

Value False

Description

Controls whether the Extracted Text field data loads directly from its file path during an import, rather than as part of a client-generated bulk load file. If set to True, the Extracted Text field loads directly from its file path. If set to False, the Extracted Text field loads a part of a client-generated bulk load file.

- LockoutNotificationList

Section

kCura.LicenseManager

Value sales@relativity.com;

Relativitystats@relativity.com

Description Defines the distribution list for emails warning of a case statistics-based or license-based lockout.

- LogEntriesToken

Section kCura.ARM

Value None

Description Token used to write to a log set in Logentries. This is obtained from Logentries in the settings view for a given log set.

- LoggingLevel

Section Relativity.Core.Logging

Value Information

Description Do not modify without advice from Relativity Customer Support. Determines the Log Level for Relativity Application Logging. Possible values are Verbose, Debug, Information, Warning, Error, and Fatal.

- LoggingLevel

Section kCura.ARM

Value 3

Description Controls the logging level for ARM jobs. Possible values for this setting are: all messages (0), trace-level messages and above (1), debug messages (2), info messages (3), warnings (4), errors (5), fatal errors only (6), or no messages (7) The default is to log info messages and above.

- LoggingLocation

Section Relativity.Core.Logging

Value None

Description Do not modify without advice from Relativity Customer Support. Identifies the location for Relativity Application Logging. Possible values are SQLServer, Data Grid, and None.

- LogOutLogo

Section Relativity.Authentication

Value relativityLogin.png

Description Identifies the name of the image file used for the LogOut Page. This must be located within the Images folder.

- LongRunningTimeoutForPublish

Section Relativity.Core

Value 1800

Description The amount of time that you want to allow before a worker terminates an unresponsive publish job.

- LongRunningTimeoutForRetryPublish

Section Relativity.Core

Value 5400

Description The amount of time, in seconds, that you want to allow before a worker terminates an unresponsive publish retry job.

- LongRunningQueryTimeout

Section kCura.Data.RowDataGateway

Value 6000

Description The timeout value, in seconds, associated with long running queries. Various places in the system use this value to time out queries that may run for a significant length of time and potentially lock an associated table. The Production application uses this value throughout the branding and queuing of branding records processes.

- LongRunningCaseStatisticsQueryTimeout

Section kCura.Billing

Value 600

Description Sets a timeout, in seconds, for queries that run in the Case Statistics Manager. If not set or non numeric, the value defaults to 600. A value of 0 is an infinite timeout. If the billing report queries consistently fail, and there are SQL timeout errors in the log, increase the timeout value.

## M

- MassActionUpgradeBatchAmount

Section kCura.EDDS.Web

Value 1000

Description Determines the number of workspaces per batch when you run an Edit Priority, Retry Upgrade, or Cancel Upgrade mass operation on the Workspace Upgrade queue. See Upgrading workspaces .

- MassCleanseBatchAmount

Section kCura.EDDS.Web

Value 1000

Description Determines the number of documents per batch for the mass cleanse process.

- MassCopyBatchAmount

Section kCura.EDDS.Web

Value 100

Description Determines the number of objects per batch when copying Dynamic Objects. Defaults to the current value for the MassDeleteBatchAmount instance setting.

- MassCreateBatchSize

Section kCura.Relativity

Value 500

Description Determines the number of artifacts per batch for the mass create process of the Services API. The Production application uses this value to determine the number of documents per batch of ProductionInformation RDOs to mass create during staging.

- MassCreateWordIndexBatchAmount

Section kCura.EDDS.Web

Value 1000

Description Determines the number of documents per batch for the mass create word index process.

- MassCustomBatchAmount

Section kCura.EDDS.Web

Value 1000

Description Determines the number of items per batch for custom mass operations. This value controls the batch size for all custom mass operations. If set to 0, Relativity skips batch execution.

- MassDeleteBatchAmount

Section kCura.EDDS.Web

Value 100

Description Determines the number of documents per batch for the mass delete process. The Production application uses this value to determine the number of documents per batch of ProductionInformation RDOs to mass delete during staging.

- MassDeleteBatchAmount

Section kCura.Relativity

Value 100

Description

Determines the number of documents per batch for the mass delete process.

The Relativity Services API (RSAPI) does not currently support the mass delete operation. This means that the RSAPI always performs a deletion one artifact at a time, regardless of the value for the MassDeleteBatchAmount instance setting value in the kCura.Relativity section of the table.

- MassEditBatchAmount

Section kCura.EDDS.Web

Value 1000

Description Determines the number of documents per batch for the mass edit process. In processing, this is the number of errors that will be marked as ignored or will be put into retry tables at a time. The Production application uses this value to determine the number of documents per batch of ProductionInformation RDOs to mass edit during staging.

- MassExportBatchAmount

Section kCura.EDDS.Web

Value 100000

Description Determines the number of documents per batch for the mass export process.

- MassImageBatchAmount

Section kCura.EDDS.Web

Value 1000

Description The number of documents per batch for the mass image process.

- MassImportSqlTimeout

Section Relativity.Data

Value 60

Description The timeout value, in seconds, associated with long running queries that any form of mass import runs. This includes image and native.

- MassMoveBatchAmount

Section kCura.EDDS.Web

Value 1000

Description Determines the number of documents per batch for the mass move process.

- MassOperationManagerThreadCount

Section Relativity.MassOperations

Value 0

Description Max number of threads for each Mass Operation Manager. If 0 or less, defaults to Agent server processor count * 2.

- MassProcessTranscriptBatchAmount

Section kCura.EDDS.Web

Value 1000

Description Determines the number of documents per batch for the mass transcript process.

- MassProduceBatchAmount

Section kCura.EDDS.Web

Value 1000

Description Determines the number of documents per batch for the mass produce process.

- MassSaveAsPDFJobPriorityDefault

Section Relativity.Core

Value 100

Description The default priority for all Mass Save as PDF jobs, as displayed on the worker manager server.

- MaximumFileSize

Section Relativity.Core

Value 1048576000

Description Determines the maximum allowed file size, in bytes, that users are allowed to upload to the file fields. If the value is 0, file size will not be validated.

- MaximumAdditionalWorkFactorRestriction

Section Relativity.Authentication

Value 3

Description Sets the maximum additional work factor that can be selected for the Password Provider on the Authentication Provider Settings section of the Authentication Provider tab.

Recommended security value

- Use the default setting unless your organization decides more hashing is necessary.

- More hashing means better encryption, but increasing this value should be tested prior to making the change in Production as it could significantly increase login time.

- MaxAggregatedWorkspaces

Section kCura.Audit

Value 10

Description Sets the maximum number of workspaces aggregated when audit from multiple workspaces are accessed.

- MaxArtifactBatchSizeForExecuteBatch

Section kCura.Relativity

Value 2000

Description Determines the maximum number of artifacts that can be submitted to ExecuteBatch in one batch.

- MaxColumnsForMinWidth

Section kCura.EDDS.Web

Value 20

Description The number of columns in a view that fit your display. If the number of columns in your view exceed this number, Relativity pushes those columns to a scroll view. The system will make optimizations that drastically reduce lag time when working with large views. However, this may result in a suboptimal user experience on views with fewer columns. Reduce this number if users complain that their views are lagging.

- MaxConcurrentAnalysisJobs

Section Relativity.StructuredAnalytics

Value 3

Description The maximum number of concurrent structured analytics jobs in the analysis phase. We recommend 3. We do not recommend using 0, which indicates unlimited concurrent jobs.

- MaxConcurrentExportJobs

Section Relativity.StructuredAnalytics

Value 3

Description The maximum number of concurrent structured analytics jobs in the export phase. We recommend 3. We do not recommend using 0, which indicates unlimited concurrent jobs.

- MaxConcurrentImportJobs

Section Relativity.StructuredAnalytics

Value 5

Description The maximum number of concurrent structured analytics jobs in the import phase. We recommend 5. We do not recommend using 0, which indicates unlimited concurrent jobs.

- MaxConcurrentWorkspaceUpgradesPerApplicationInstallerAgent

Section Relativity.Core

Value 3

Description Reserved for future development.

- MaxErrorListItems

Section Relativity.Data

Value 50000

Description Determines the maximum number of errors that appear on the Error page.

- MaxFilesPerCacheFolder

Section Relativity.Conversion

Value 1000

Description Determines the maximum number of files to store in a single cache folder.

- MaxGridItemsToExport

Section kCura.Audit

Value 5000

Description Maximum number of audits that can be exported from Data Grid.

- MaxJobExpirationHours

Section kCura.Fta

Value 168

Description The maximum period of time, in hours, before a file transfer job expires.

- MaxJobRetryCount

Section kCura.Fta

Value 3

Description The maximum number of times a job is retried before the file transfer job status sets to Error.

- MaxKeplerRetryCount

Section kCura.Fta

Value 5

Description The maximum number of times a Kepler service call is made from a file transfer job before throwing an exception.

- MaximumActionsAllowedForRelativityScript

Section kCura.EDDS.Web

Value 10

Description Determines the maximum number of actions that can be included in the script body for Relativity scripts; 10 is the recommended value.

- MaximumColumnsAllowedForRelativityScriptReport

Section kCura.EDDS.Web

Value 7

Description Determines the maximum number of columns that can render when a Relativity script runs as a report; 7 is the recommended value.

- MaximumDisplayCountForMultiPicker

Section kCura.EDDS.Web

Value 10

Description Determines the maximum number of items to display while editing multi-object and multi-choice fields. Once items exceed this value, a button with "..." replaces the drop-down list.

- MaximumImageCountForViewer

Section kCura.EDDS.Web

Value 1000

Description Determines the maximum number of images in a document for the document to appear in the viewer. Documents that contain more images than this value are not converted and will not appear in the viewer.

- MaxImagingResponseThreads

Section Relativity.Imaging

Value 0

Description The maximum number of threads for each Imaging Response Agent. If this is 0 or less, defaults to Agent server processor count * 2. Our recommendation is 1 Imaging Response Agent thread per 8 Imaging Worker threads at a minimum.

- MaxImagingRequestThreads

Section Relativity.Imaging

Value 0

Description The maximum number of threads for each Imaging Request Agent. If this is 0 or less, defaults to Agent server processor count * 2. Our recommendation is 1 Imaging Request Agent thread per 8 Imaging Worker threads at a minimum.

- MaximumListPageTextLength

Section kCura.EDDS.Web

Value 500

Description Determines the maximum number of characters that the item list displays for a text field.

- MaximumLongTextSizeForExportInCell

Section kCura.EDDS.WebAPI

Value 1048576

Description The maximum length, in characters, of a long-text cell. During export, if the length of a long-text cell is greater than this value, Relativity pulls down a token instead of the text for that cell. When the Desktop Client comes across that cell, it knows to make a separate call to pull down the text for that cell.

- MaximumNativeFileSizeForViewerForMediaFilesinMegabytes

Section kCura.EDDS.Web

Value 1024

Description The maximum size, in megabytes, of a native media file that the Native Viewer attempts to display. If a native media document is greater than this size, the user sees a page explaining that the document is too large to be displayed.

- MaximumNativeSizeForViewerInBytes

Section kCura.EDDS.Web

Value 10485760

Description The maximum size, in bytes, of a native file that the Native Viewer attempts to display. If a native document is greater than this size, the user sees a page explaining that the document is too large to be displayed.

- MaximumNumberOfCharactersSupportedByLongText

Section kCura.EDDS.Web

Value 100000

Description Determines the maximum number of characters, including HTML markup, that can be saved into a long text field from the web.

- MaximumNumberOfImagesForExportChunk

Section kCura.EDDS.WebAPI

Value 10000

Description The maximum number of images, in total bytes, that export in a single set.

- MaximumPasswordAgeDefault

Section kCura.EDDS.Web

Value 0

Description Determines the default value for the maximum password age when creating password authentication providers.

Recommended security value

- Set this value to a number greater than zero so users are encouraged to change their passwords after a certain number of days.

- Password rotation can protect Relativity against passwords that may have been compromised.

- MaximumPasswordLength

Section kCura.EDDS.Web

Value 50

Description Determines the maximum number of characters required for a user password. This value cannot be greater than 50.

- MaximumPasswordLengthDefault

Section Relativity.Authentication

Value 50

Description Sets the default value for the MaximumPasswordLength setting in the Password Provider on the Authentication Provider Settings section of the Authentication Provider tab.

- MaximumPasswordLengthRestriction

Section Relativity.Authentication

Value 50

Description Sets maximum length for a PasswordLength setting in the Password Provider on the Authentication Provider Settings section of the Authentication Provider tab.

- MaximumTextVolumeForExportChunk

Section kCura.EDDS.WebAPI

Value 268435456

Description Determines the maximum total text size, in bytes, that can be exported from a single chunked WebAPI payload. Although the long text length is accounted for within the chunk total, the long text data is retrieved through a separate API.

- MaximumInvalidLoginAttemptsDefault

Section Relativity.Authentication

Value 10

Description Determines the maximum number of login attempts a user can make with a given username before Relativity locks that username.

- MaxListItems

Section Relativity.Data

Value 1000

Description Determines the maximum number of items that appear on the dtSearch/CA error pop-ups, the batch, linked, search, and relational panes within the review tool, and the error list at Home.

- MaxNumberDashboardWidgets

Section kCura.Core

Value 10

Description

Determines the maximum number of widgets that a user can add to a given dashboard..

Add Pivot button is grayed out if amount of Pivot widgets in current dashboard is greater than or equal to set value.

- MaxNumberOfArtfactsToMassCreate

Section kCura.Relativity

Value 1000000

Description Determines the maximum number of artifacts that a user can submit to the MassCreate API function at a time.

- MaxNumberOfArtfactsToMassEdit

Section kCura.Relativity

Value 1000000

Description Determines the maximum number of artifacts that a user can submit to the MassEdit API function at a time.

- MaxNumberOfImagesForPdfJob

Section Relativity.PDF

Value 2500

Description Determines the maximum number of images allowed per PDF job.

- MaxNumPagesSaveAsPDF

Section Relativity.Core

Value 25000

Description Determines the maximum number of images allowed in one Save As PDF request.

- MaximumPasswordHistory

Section Relativity.Core

Value 5

Description Determines how many password changes Relativity examines for duplicate passwords. Setting this to a large value could prevent a user from ever using the same password twice.

Recommended security value

- Determine if your organization wants to limit users from reusing the same passwords they have used in the past.

- This can protect the Relativity environment from a previously compromised password.

- MaximumPasswordHistoryRestriction

Section Relativity.Authentication

Value 5

Description Sets maximum value for the MaximumPasswordHistory setting in the Authentication Provider Settings section of the Authentication Provider tab. Lower values allow users to repeat passwords more frequently. Zero does not keep any password history. Higher values restrict passwords for being used again soon.

- MaxPDVQueryLength

Section Relativity.Core

Value 60

Description The amount of time, in seconds, before running queries related to displaying document lists time out.

- MaxQueryConditionCharacterLength

Section Relativity.Core

Value 100000

Description Determines the maximum number of characters of criterion in the View criteria picker.

- MaxTreeviewChildNodes

Section Relativity.Core

Value 1000

Description Determines the maximum number of nodes under a single parent node that appears in the tree view. If the number of child nodes is exceeded, an error message appears. This improves user experience and avoids memory issues within the browser.

- MigrationAgentBatchSize

Section Relativity.DataGrid.Migration

Value 500

Description Default size of batches for migration

- MigrationFailOnFileCopyErrors

Section Relativity.ApplicationBase

Value True

Description Determines if a Processing Migration job, Archive or Restore, will stop and fail the job if there is a file copy error, when the setting is set to true, or will log a report of the failed file copies, when false.

- MemoryByteSizeThreshold

Section Relativity.DataGridMigrator.Agent

Value 104857600

Description Maximum size that Data Grid Text Migrator agent will attempt load documents in memory. The default value is 104857600 (100MB).

- MetricsTransmissionBasedLockout

Section kCura.LicenseManager

Value blank

Description Stores an encrypted value with the last time a metric was successfully transmitted to Relativity ODA LLC.

- MigrationMaxParallelFileCopyThreads

Section Relativity.DataTransfer

Value 4

Description The maximum number of parallel threads ARM for Processing will use during the file repository copy operation.

- MinimumExcerptTextLength

Section kCura.AssistedReview

Value 120

Description Determines the minimum number of characters required for a text excerpt for designation and issues.

- MinimumPasswordLength

Section kCura.EDDS.Web

Value 8

Description Determines the minimum number of characters required for a user password. This instance setting can be set to a value between 8-50.

- MinimumPasswordLengthDefault

Section Relativity.Authentication

Value 10

Description The default value for the MinimumPasswordLength setting in the Authentication Provider Settings section of the Authentication Provider tab.

- MinimumPasswordLengthRestriction

Section Relativity.Authentication

Value 8

Description Sets minimum length for a PasswordLength setting in the Authentication Provider Settings section of the Authentication Provider tab.

- MinimumSeedInfluence

Section kCura.AssistedReview

Value 25

Description The minimum number of documents required to be categorized by each example document returned in an Assisted Review stratified sample. This is only available if you add it locally.

- MinimumSupportedChromeVersion

Section Relativity.Authentication

Value 35

Description Do not modify without advice from Relativity Customer Support. This instance setting lists the minimum version of Chrome that is compatible with Relativity.

- MinimumSupportedFirefoxVersion

Section Relativity.Authentication

Value 31

Description Do not modify without advice from Relativity Customer Support. This instance setting lists the minimum version of Firefox that is compatible with Relativity.

- MinimumSupportedSafariVersion

Section Relativity.Authentication

Value 6

Description Do not modify without advice from Relativity Customer Support. This instance setting lists the minimum version of Safari that is compatible with Relativity.

- MinimumSupportedVersion

Section Relativity.Authentication

Value 10

Description Do not modify without advice from Relativity Customer Support. This instance setting lists the minimum version of Internet Explorer that is compatible with Relativity.

- MinLogLevel

Section Relativity.OpenTelemetry

Value Information

Description The minimum log level used by the Open Telemetry log provider. This value is completely independent of EDDS/SQL Relativity Logging.

- MissedServerCheckInsBeforeAlert

Section Relativity.Core

Value 3

Description Determines the number of times that a server can fail to check in with Relativity before the application generates an alert indicating that the server is non-responsive. The ServerCheckInInterval instance setting specifies the time interval indicating how frequently the server must check in with Relativity. See ServerCheckInInterval .

- MOTDTextOnly

Section kCura.EDDS.Web

Value False

Description Controls how the message of the day (MOTD) is entered and displayed. If set to True, the MOTD can only be entered and displayed as plain text. If set to False, the MOTD can be entered and displayed using the full HTML editor.

This instance setting must be manually added to your environment.

Recommended security value

- Set the value to True unless you want the ability to use JavaScript in this field.

- By only allowing text in the Message of the Day box, cross-site scripting and cross-frame scripting can be prevented.

## N

- NativeImagingTimeout

Section Relativity.Imaging

Value 300

Value Type Nonnegative Integer 32-bit

Description

The amount of time, in seconds, that the native imaging process waits for a single document to be imaged before killing the export process and moving to the next document.

This timeout is not valid for .cad, .pdf, .txt, .rtf, .nsf, .hwp, .jungum, .bitmap, and .xps files. .cad has its own timeout, and the other files use global Invariant timeout.

- NumberOfDocumentsToAutoPreConvert

Section Relativity.DocumentViewer

Value 1000

Description Determines the number of documents, natives and images, to preconvert upon batch checkout and defaults to 1000. If value is set to 0, preconversion will be disabled.

- NumberOfRelatedDocumentsToPreconvert

Section Relativity.DocumentViewer

Value 25

Description Determines the number of documents, up to a maximum of 25, to automatically preconvert for the Relational List Pane in the document viewer coding panel. Converts both Natives and Images.

## O

- OCRCompilationBatchSize

Section kCura.EDDS.Agents

Value 100

Description Determines the number of updates to the document table, with the OCRed text, that the OCR Manager makes in a single transaction.

- OCRProcessingBatchSize

Section kCura.EDDS.Agents

Value 1000

Description Determines the number of items transferred from OCR_POP tables into OCR_TEXT in a single transaction.

- OCRWorkerBatchAmount

Section kCura.EDDS.Agents

Value 100

Description Determines the number of images a single OCR worker agent pulls and OCRs at a time.

- OCRWorkerInsertBatchSize

Section kCura.EDDS.Agents

Value 500

Description Determines the number of inserts to the OCR Worker table that the OCR Manager agent batches into a single transaction.

- OIDateFormat

Section Relativity.Conversion

Value blank

Description Determines the date format used during native file conversion. Accepted values are MM/DD/YYYY, MM/DD/YY, DD/MM/YYYY, DD/MM/YY, YYYY/MM/DD, YY/MM/DD.

- OtlpExporterLogsEndpointUrl

Section Relativity.OpenTelemetry

Value http://localhost:4318/v1/logs

Description The Open Telemetry Protocol (OTLP) endpoint URL where the exporter submits log telemetry.

- OtlpExporterMetricsEndpointUrl

Section Relativity.OpenTelemetry

Value http://localhost:4318/v1/metrics

Description The Open Telemetry Protocol (OTLP) endpoint URL where the exporter submits metric telemetry.

- OtlpExporterTracesEndpointUrl

Section Relativity.OpenTelemetry

Value http://localhost:4318/v1/traces

Description The Open Telemetry Protocol (OTLP) endpoint URL where the exporter submits trace telemetry.

- OutputStructure

Section Relativity.Conversion

Value Chunked

Description

Determine the data transfer encoding method that Relativity's processing engine uses when converting files into documents that are readable in the viewer. The method can be chunked or streamed. By default, this value is set to Chunked.

- Chunked—Relativity transfers data to the processing engine in a series of chunks. The size of each chunk is sent directly before the chunk itself so that the engine knows when it has finished receiving data for that chunk. Chunked is the default value. Chunked and Flat get similar conversion results.

- Streamed—Relativity transfers data to the processing engine in a steady and continuous stream. If the engine receives the data more quickly than required, it temporarily saves the excess data in a buffer until it's ready to process it. Do not select Streamed. If you select Streamed, you will experience conversion failures.

- OutputUrlPath

Section Relativity.Conversion

Value ./

Description Identifies the relative path to any other resources needed by a converted document. The default value is ./.

- OversizedAuditsFolder

Section kCura.Audit

Value DataGridOversizedAudits

Description The subfolder that stores oversized audits.

## P

- ParameterLoggingMaxLength

Section kCura.Data.RowDataGateway

Value 8000

Description Sets the maximum length of strings in the messages logged at Verbose logging level by System DataLayer.

- PasswordHistoryDefault

Section Relativity.Authentication

Value 5

Description Sets default value for the PasswordHistory setting in the Authentication Provider Settings section of the Authentication Provider tab.

- PasswordNotificationRelativityURL

Section kCura.Relativity

Value blank

Description Identifies the URL for Relativity used in a password notification email. It's used only by the API.

- PasswordResetEmailExpirationInMinutes

Section Relativity.ForgotPassword

Value 15

Description Defines how long, in minutes, password reset links remain valid after the email is sent.

Changing this instance setting affects all subsequent reset password links, after about 30 seconds. It does not affect the links that have already been sent.

Recommended security value

- Your organization should limit the time the password reset link remains valid.

- The longer the link remains active, the more risk it will be compromised by an attacker.

- PasswordResetRequestLimitDefault

Section Relativity.Authentication

Value 10

Description Sets the default value for the PasswordResetRequestLimit setting in the Authentication Provider Settings section of the Authentication Provider tab.

- PasswordResetRequestLimit

Section Relativity.Authentication

Value 10

Description Determines the number of password reset requests, between 10-50 requests, an individual email address can generate. After reaching this number, the email address cannot receive any additional Reset Password emails unless the user clicks the link provided in the email. After the Workspace Housekeeping agent runs again, the Reset Password emails resume. Until the Workspace Housekeeping agent runs, no auditing is logged for the user.

- PasswordWorkFactor

Section Relativity.Authentication

Value 10

Description Controls the strength of the encryption used for password hashing using a bCrypt work factor constant. Any value lower than 10 defaults to 10. Incrementing by 1 doubles the time it takes to hash the password.

- PDVCacheLifetime

Section kCura.Relativity

Value 1000

Description The amount of time, in minutes, the Performance DataView cache exists. Relativity uses this cache for item list population to increase performance.

- PDVDefaultQueryCacheSize

Section kCura.Relativity

Value 10000

Description Determines the default number of artifacts returned during each query cache read.

- PlaceholderImageFormatDefault

Section Relativity.Production

Value TIFF

Description The default placeholder image format that gets applied to new productions. You can set the PlaceholderImageFormatDefault to either TIFF or JPEG. When creating a new production, you can override the default image placeholder format without changing the instance setting.

- PivotMaximumNumberOfColumns

Section Relativity.Data

Value 100

Description Determines the maximum number of columns that appear in pivot.

- PivotMaximumNumberOfRows

Section Relativity.Data

Value 20000

Description Determines the maximum number of rows that appear in pivot.

- PivotNumberOfRowsPerPage

Section kCura.EDDS.Web

Value 15

Description Determines the default number of rows per page in pivot.

- PivotQueryTimeout

Section Relativity.Data

Value 180

Description The timeout value, in seconds, on the pivot query.

- PostLibraryScriptUrls

Section Relativity.Conversion

Value blank

Description A semicolon-delimited list of JavaScript libraries to load after loading Oracle libraries in every converted document. By default, this value is empty.

- PostMigrationPersistencePeriod

Section kCura.Audit

Value 90

Description The amount of time, in days, that audit data remains in SQL after it has been created.

- PreConvertCacheSize

Section kCura.EDDS.Web

Value 3

Description Determines how many documents are pre-converted when the user reviews them in the Review Interface. Pre-conversion occurs for the Native, Image, and Production Viewers.

- PreLibraryScriptUrls

Section Relativity.Conversion

Value blank

Description A semicolon-delimited list of JavaScript libraries to load before loading Oracle libraries in every converted document. By default, this value is empty.

- PreventLoginLinkDisplayOnLogoutPage

Section Relativity.Authentication

Value FALSE

Description Controls the display of the login link on the logout page. If you set the value to false, then the login link appears on the logout page. If you set the value to true, the link does not appear on this page. Set the value to true if you want to prevent users who authenticate with SAML or OpenID Connect from experiencing any confusion caused by seeing the login link displayed when they are logging out of Relativity.

- PrintImageWarningThreshold

Section kCura.EDDS.Web

Value 500

Description Determines the maximum number of images that a user can mass print before a warning message appears. If a user attempts to mass print, and the number of images to be printed exceeds this threshold, a warning appears to let the user know they're attempting to print a large number of documents.

- ProcessingDiscoverJobPriorityDefault

Section Relativity.Core

Value 100

Description Determines the default priority for all Processing Discover jobs.

- ProcessingErrorRetrievalInitialBatchSize

Section Relativity.Core

Value 1000

Description Determines the initial number of errors to pull back from the worker manager server in one call. If this fails, the number is halved until it either succeeds or fails in pulling back one error.

- ProcessingErrorUpdateBatchSize

Section Relativity.Core

Value 1000

Description Determines the number of errors per batch that the processing set manager agent retrieves and sends back to Relativity to display in the Errors tab. If this value is set to a number higher than 1000 and you attempt to republish a processing set that contains 1000 or more publish errors, you will receive an agent error. Retrying errors manually on the Errors tab is not affected by this issue.

- ProcessingExportBatchSize

Section Relativity.Core

Value 4000

Description Determines the number of documents per batch when importing documents during processing.

- ProcessingInventoryJobPriorityDefault

Section Relativity.Core

Value 100

Description Determines the default priority for all Processing Inventory jobs.

- ProcessingMaxPublishJobCountPerRelativitySQLServer

Section Relativity.Core

Value 21

Description

The maximum number of publish jobs per Relativity SQL server that may be worked on in parallel. This puts an absolute limit on the number of publish jobs that occur in parallel for a given SQL server, independent of how many workspaces may be publishing simultaneously. This means that it overrides the limit set by ProcessingMaxPublishSubJobCountPerWorkspace.

For information on configuring this setting, see Throttle settings for distributed publish .

- ProcessingMaxPublishSubJobCountPerWorkspace

Section Relativity.Core

Value 7

Description

The maximum number of publish jobs per workspace that may be worked on in parallel. You cannot allocate more jobs per workspace than what is allowed per SQL server. This means that if this value is set to be higher than the value for the MaxPublishJobCountPerRelativitySQLServer instance setting, then Relativity only allows the maximum of jobs per SQL server.

For information on configuring this setting, see Throttle settings for distributed publish .

- ProcessingPublishJobPriorityDefault

Section Relativity.Core

Value 90

Description Determines the default priority for all Processing Publish jobs.

- ProcessingRetryCount

Section Relativity.Core

Value 3

Description Determines the number of times Relativity retries a processing job before flagging the job as paused.

- ProcessingRetryTimerDuration

Section Relativity.Core

Value 600

Description The amount of time, in seconds, before the Processing Set Manager automatically retries paused jobs.

- ProcessingSetStatusUpdateInterval

Section Relativity.Core

Value 5000

Description The interval, in milliseconds, at which the processing set console updates the status of the processing set.

- ProcessingStatisticsMaxNumberOfRows

Section Relativity.Core

Value 1300

Description Determines the maximum number of rows that the Processing Statistics event handler can return. Each row contains a processing set.

- ProcessingWebAPIPath

Section Relativity.Core

Value <blank>

Description

Identifies the URL that directs to the Relativity token-authenticated endpoints that Invariant uses to process files. Processing requires this URL and a Relativity admin must enter it. This setting cannot be a Windows Authenticated Relativity Web API endpoint; it must use token authentication.

When you upgrade, update your IIS settings by changing the WebAPI to Anonymous Authentication rather than Windows Authentication. You must update this setting to Anonymous Authentication to publish documents to a workspace or process data to Data Grid.

- ProtectedAssemblies

Section Relativity.Core

Value kCura.Relativity.Client.dll;kCura.Relativity.Client40.dll;kCura.EventHandler.dll;Relativity.CustomPages.dll;kCura.Agent.dll

Description A semicolon-delimited string of common DLLs to not write out from the Assembly table when loading Event Handlers, Custom Pages, or Agents.

## Q

- QueryCacheMode

Section Relativity.Data

Value TimeBased

Description

Controls caching for Relativity list pages and queries. Valid values are TimeBased (default; caches results for approximately 30 seconds) or None (disables caching and always reads from SQL). Any other or missing value is not permitted and is treated as TimeBased.

We do not recommend entering any other value because doing so can cause list pages, including the Documents tab, to fail to load.

- QuickNavEnabled

Section Relativity.Core

Value True

Description Controls if the quick nav search box appears. If set to True, the quick nav search box appears. If set to False, the quick nav search box does not appear.

- QuickNavMaxResults

Section Relativity.Core

Value 20

Description Determines the maximum number of results that appear in quick nav. The value must be a number between 2 and 50.

## R

- RecentHistoryEnabled

Section Relativity.Core

Value TRUE

Description Controls if recent history items appear. If set to True, recent history items appear. If set to False, recent history items do not appear.

- RecentHistoryNumberOfItemsDisplayed

Section Relativity.Core

Value 10

Description Determines the number of recent history items that the favorites control stores and displays if Recent History is enabled.

- RedactionBatchSize

Section Relativity.Production

Value 25000

Description Controls how the Branding Manager retrieves redactions

- RelativityInstanceURL

Section Relativity.Core

Value Blank string ("")

Description

Identifies the URL that your Relativity instance uses. For example, you might use https:// Relativity .corp/Relativity as the instance URL for your environment. Any Relativity applications deployed in your environment that need to provide external links to users can use this instance setting. For example, any application that adds a link to a Relativity application in an email message could use this setting.

Do not use localhost as the host name in this instance setting.

- RelativityInternalWebUri

Section Relativity.Core

Value Blank string ("")

Description A URL that overrides the dynamically-generated internal URL for the Relativity application, for example, http://localhost/Relativity. This value should be set when the web server has multiple HTTP bindings, for example, for a specific TLS/SSL setup.

- RelativityMinimumVersion

Section Relativity.Conversion.Cache

Value 12.1.0.0

Description The minimum Relativity version required to install the Relativity Conversion Cache application.

- RelativityScriptPickerViewID

Section kCura.EDDS.Web

Value 902

Description Identifies the View ArtifactID of the Relativity Script Picker.

- RelativityServicesPath

Section Relativity.Core

Value Set during Relativity installation

Description Identifies the URL for the Services API. Event handlers and custom agents use this path. Procuro automatically sets this value on installation.

- RelativityWebAPITimeout

Section kCura.ARM

Value 300,000

Description The timeout for Relativity WebAPI calls made by ARM in milliseconds.

- ReplaceApplicationNameWithArtifactID

Section kCura.Billing

Value True

Description Controls if the Application Name in the billing statistics report is replaced with the Application ArtifcactID. If set to True, the Application Name in the billing statistics scripts is replaced with the Application ArtifactID. By default, the value is set to False, and the Application Name is displayed.

Recommended security value

False - the application name could reveal sensitive information.

- ReplaceCaseNameWithArtifactID

Section kCura.Billing

Value False

Description Controls whether the Case Name in the billing statistics report is replaced with the Case ArtifactID. If set to True, the Case Name in the billing statistics scripts is replaced with the Application ArtifactID. By default, the value is set to False, and the Case Name is displayed.

Recommended security value

False - the case name could reveal sensitive information.

- ReplaceClientNameWithHashValue

Section kCura.Billing

Value False

Description

Controls whether Relativity replaces the client names with hash values in billing information sent manually or automatically. If set to True, Relativity replaces the client name with a unique hash value. If you manually run the billing script, the value you select in the interface overrides this instance setting.

- ReplaceMatterNameWithHashValue

Section kCura.Billing

Value False

Description

Controls whether Relativity replaces the matter names with hash values in billing information sent manually or automatically. If set to True, Relativity replaces the matter name with a unique hash value. If you manually run the billing script, the value you select in the interface overrides this instance setting.

- ReplaceUserNameWithHashValue

Section kCura.Billing

Value False

Description Controls whether Relativity replaces the username portions of user email addresses with hash values in billing information sent manually or sent automatically through the SMTP server. If set to True, Relativity replaces all text preceding the @ symbol in each user email address with a unique hash value. Domains remain unencrypted. If set to False, entire user email addresses appear. If you manually run the billing script, the value you select in the interface overrides this instance setting.

Recommended security value

True - this will hide the usernames and case names in Billing Data sent through the SMTP server.

- ReplaceWebAPIWithExportCore

Section kCura.IntegrationPoints

Value True

Description Determines if the Integration Points Fileshare destination provider, Relativity Export, will use the Export Core, direct usage of Relativity.Core, instead of /RelativityWebAPI web service calls. If you keep this at the default value of True, then Integration Points Export will use the Export Core. If you change this value to False, then Integration Points Export will use the Relativity WebAPI. This setting was added in Relativity 9.4.321.2 .

- RepositoryVolumeMax

Section Relativity.Core

Value 1000

Description Determines the maximum number of files allowed in a repository case sub-directory. The Production application uses this value when creating images during branding to determine whether to create a new folder.

- RerunBrandingErrorsThreshold

Section Relativity.Production

Value 1

Description The maximum percentage of documents that errored during a branding job that the system will automatically retry upon the job's completion. If more than the maximum percentage of documents receive an error, the system will not retry any of the documents.

- ResolutionGuidanceDomainURL

Section Relativity.Alerts

Value https://help.relativity.com/Server2025

Description The ResolutionGuidanceDomainURL instance setting will be added once the Relativity Alerts RAP is installed as part of Environment Watch. This setting determines the URL for the documentation link within Relativity Alerts.

- ResourceUrlPath

Section Relativity.Conversion

Value /Relativity/CustomPages/{viewer application guid}/OracleContent/{version}/

Description Identifies the relative path to Oracle resources for converted documents. In the default value, replace {viewer application guid} with your guid without the curly braces.

- RestrictedFileTypes

Section Relativity.Core

Value .exe;.html;.htm;.js

Description A semicolon-delimited list of file extensions, including dots, that users are prohibited from uploading to file fields, excluding Custom Pages. For example, .exe;.html

See also ApplicationRestrictedFileTypes .

This instance setting must be manually added to your environment.

Recommended security value

- Use the default values plus any other file extensions your organization deems necessary.

- Certain types of files could contain malicious scripts.

- RestrictedNativeFileTypes

Section Relativity.Core

Value HTML;HTM;EXE

Description A semicolon-delimited list of file types users are prohibited from uploading to file fields, excluding Custom Pages. These values are regular expression enabled, so custom validation behavior is also supported.

This instance setting must be manually added to your environment.

Recommended security value

- Use the default values plus any other file extensions your organization deems necessary.

- Certain types of files could contain malicious scripts.

- RestrictReferentialFileLinksOnImport

Section Relativity.Core

Value True

Description

Controls whether non-system administrators can import documents, objects, images, and productions using referential links for files already in a valid, Relativity-accessible location. When set to True, non-system administrators can import only by uploading files. When set to False, all users can import using referential links.

Recommended security value

True - this ensures users cannot import files from workspaces they have no access to.

- RestServicesUri

Section Relativity.Core

Value //localhost/Relativity.Rest/

Description Identifies a path to the REST Services URI.

- RestUriForCAAT

Section Relativity.Core

Value http://mainline-1.testing.kcura.corp/Relativity.Rest/API

Description

Specifies the URL at which CAAT can access the Services API Kepler services using API helpers. This setting is not machine specific and applies to all servers in the environment.

You must enter a valid FQDN of a web or agent server hosting Kepler services. For example, https://client.domain.name/Relativity.REST/API.

- RetainConvertedDocumentsHours

Section Relativity.Conversion.Cache

Value 72

Description If the last accessed time is more than the hour limit you select, cache files are deleted.

- RetainJobRecordsDays

Section Relativity.Conversion.Cache

Value 30

Description The number of days to retain eddsdbo.ClearCacheLocationStatistics records for completed jobs before they're automatically deleted.

- Retries

Section kCura.AssistedReview

Value 3

Description Determines the number of times RAR agents retry upon failure of a given operation. After retries are exhausted, the project has an error status; retries occur every 30 seconds by default.

- Retries

Section Relativity.StructuredAnalytics

Value 3

Description Number of times agents retry upon failure of a given Structured Analytics operation. After retries are exhausted, the project has an error status; retries occur every 30 seconds by default.

- RetryWaitTime

Section kCura.AssistedReview

Value 30

Description The amount of time, in seconds, between Relativity's attempt to retry errors.

- RevertMaxAuditCount

Section kCura.Audit

Value 5000

Description Maximum number of audits that can be present on the item list view for the Revert mass operation. Do not increase this value past 5000.

- RevertThresholdToleranceInMilliseconds

Section kCura.Audit

Value 100

Description Timestamp difference allowed between SQL last modified and Data Grid audits timestamps, in milliseconds, when determining whether an audit can be reverted.

- ReviewQueueBatchSize

Section Analytics.ActiveLearning

Value 150

Description Defines the number of documents that are requested for review from the analytics engine when the number of outstanding documents in a review queue falls under the level defined by the ReviewQueueRefreshThreshold instance setting. The actual number of documents requested is the number of active reviewers on the review multiplied by the ReviewQueueBatchSize value.

- ReviewQueueRefreshThreshold

Section Analytics.ActiveLearning

Value 50

Description The number of documents in a review queue under which Active Learning will request more documents for review from the Analytics Engine. The actual threshold is the number of active reviewers on the review multiplied by the ReviewQueueRefreshThreshold value.

- RichTextEditorFontDefault

Section kCura.EDDS.Web

Value Arial

Description Specifies the default font to be loaded in the rich text editor on page load. Relativity requires one of the following values exactly and defaults to Arial if left blank or otherwise specified: Arial, Arial Black, Comic Sans MS, Courier New, Helvetica, Impact, Tahoma, Trebuchet MS, Times New Roman, Verdana.

- RichTextEditorSpellCheckDefaultState

Section kCura.EDDS.Web

Value True

Description Controls if the spell check button is selected by default when loading the rich text editor. If set to True, the spell check button is selected by default. If set to False, the spell check button is not selected by default.

- RolledSecretExpiration

Section Relativity.Authentication

Value 00:15:00

Description Do not modify. The time interval a rolled secret remains valid before it expiring. Default value is 15 minutes, 00:15:00. For formatting rules, see https://msdn.microsoft.com/en-us/library/3z48198e(v=vs.110).aspx.

- RPCSessionTimeout

Section Relativity.Authentication

Value 00:15:00

Description The time interval a Relativity Processing Console user session remains valid before it is logged out. Default value is 15 minutes, 00:15:00.

- RPCSessionTimeoutDelay

Section Relativity.Authentication

Value 00:00:90

Description The time interval a Relativity Processing Console user session is prompted for inactivity before it is logged out. Default value is 90 seconds, 00:00:90.

- RSAConfigFilePath

Section Relativity.Authentication

Value %RelativityWebInstallDir%\RSA

Description Identifies the location of the sdconf.rec file and optional sdopts.rec file. These files initialize the RSA library when RSA authentication is set up. The value must include the drive letter, for example C:\Program Files\kCura Corporation\Relativity\EDDS\RSA . You cannot use environment variables as part of the path.

- RUMEnable

Section kCura.EDDS.Web

Value True

Description Controls whether Relativity User Metrics collects click data. Setting this value to True lets Relativity User Metrics collect click data. Setting this value to False does not allow Relativity User Metrics to collect click data.

- RUMEndpoint

Section kCura.EDDS.Web

Value https://rum-cloud.relativity.com:443/

Description Identifies the URL for data submission for Relativity User Metrics.

- RUMIdentifier

Section kCura.EDDS.Web

Value A000C182-52A6-417D-A279-BC24F365B20D

Description Identifies the GUID that Relativity uses to identify an instance for Relativity User Metrics

## S

- SamplingStatisticalPopulationResultsLimit

Section kCura.EDDS.Web

Value 300

Description Determines the minimum number of items in a data set required for statistical sampling to be valid. Fewer items than the default value constitutes an insufficient population for reliable statistical sampling and throws an error if the user attempts to sample.

- SaveAsPDFExpiration

Section Relativity.Core

Value 7

Description The maximum length, in days, that a Mass Save as PDF document stays in the cache. The value is ignored if the file is downloaded in the pop-up window. The value is respected if the file is downloaded from an email.

- SaveAsPDFJobPriorityDefault

Section Relativity.Core

Value 100

Description Determines the default priority for all Save as PDF jobs.

- SaveAsPDFStampLengthLimit

Section Relativity.Core

Value 100

Description Determines the maximum number of characters allowed in a Save as PDF stamp identifier. Only the first 100 characters are stamped on the document if the value of the field or text used is longer than this value.

- ScriptRunManagerMaxConcurrentThreads

Section kCura.EDDS.Agents

Value 10

Description Determines the max amount of concurrent script run threads each agent can use, defaults to 10.

- SecretRollFrequency

Section Relativity.Authentication

Value 30 9 * * 2

Description Do not modify. The frequency at which the Secret Agent rolls secrets. The value is in Crontab format.

The Secret Agent must be run more frequently than specified by the value of this instance setting. This setting is parsed and executed based on the server time that the agent is running on.

- SearchAgentServicePort

Section Relativity.Core

Value 6870

Description Identifies the default port that the dtSearchAgent uses to service search requests.

- SearchCacheTableCreationTimeout

Section Relativity.Core

Value 60

Description The timeout value, in seconds, for the creation of a Search Cache table.

This instance setting must be manually added to your environment.

- SearchIndexerLongRunningQueryTimeout

Section Relativity.Data

Value 1200

Description The timeout value, in seconds, associated with long running queries run by dtSearch, Analytics, and Domain Parsing.

- SearchIndexerMaxPopulationErrors

Section SearchIndexerMaxPopulationErrors

Value 5000

Description Determines the maximum number of errors allowed for a single population process in dtSearch or Analytics before the job is terminated. If this limit is reached, the respective agent throws an exception saying that the failure limit has been reached.

- SearchIndexerTextFromSQLChunkSizeInBytes

Section Relativity.Data

Value 1048576

Description Determines the size of the text chunks streamed from SQL to either the dtSearch or Analytics agents when they are writing large files to disk. Increasing this value may improve performance when populating large files. The larger this value becomes, the greater the chance that either the dtSearch or Content Analyst agent will run out of memory.

- SeedingAgentBatchSize

Section Relativity.DataGrid.Migration

Value 500

Description Default size of batches for seeding.

- SendNotificationOnImportCompletion

Section Relativity.Core

Value False

Description Determines whether Relativity sends a notification email to the user running the import when the import completes.

- SendNotificationOnImportCompletionByDefault

Section kCura.EDDS.Winform

Value False

Description Determines whether Relativity sends a notification to the user uploading data on import completion. If set to True, Relativity sends a notification to the user uploading data on import completion. If set to False, Relativity does not send a notification.

- SequenceReservationSize

Section Relativity.ApplicationBase

Value 100

Description Determines the number of IDs that Relativity should reserve to memory at a time.

- ServerCheckInInterval

Section Relativity.Core

Value 60000 msec

Description The time interval, in milliseconds, used to indicate how frequently a server must check in with Relativity.

- ServerManagerRetries

Section kCura.EDDS.Agents

Value 3

Description Determines the number of attempts the Server Manager agent makes to connect to a server before it sets the server status to inactive.

- ServiceBusFullyQualifiedDomainName

Section Relativity.ServiceBus

Value localhost

Description

When using RabbitMQ, ServiceBusFullyQualifiedDomainName specifies the fully-qualified domain name for the machine or load balancer where Relativity can reach the environment’s cluster. The Relativity installer automatically sets this value during an installation or upgrade based on the inputs in the RelativityResponse.txt file.

For more information, see Relativity installation or Upgrading your Relativity Service Bus.

- ServiceHostExclusionList

Section Relativity.Platform.Discovery

Value Text

Description A semi-colon delimited list of GUIDs for services that you want prevented from starting in the Service Host Manager. For more information, see Service Host Manager .

- ServicesAPIHostingOnAgentServersMode

Section kCura.Relativity

Value SelfHosting

Description Determines how agents access the Services API in a Relativity environment. Values include SelfHosting and PredefinedURL .

- ServicesAPIHostingOnAgentServersPredefinedURL

Section kCura.Relativity

Value http://localhost:9997/Relativity.Services/

Description Identifies the URL that agents use to access the Services API server when ServicesAPIHostingOnAgentServersMode setting is set to PredefinedURL .

- ServicesAPIMetadataPortOnAgentServers

Section kCura.Relativity

Value 6867

Description Identifies the TCP port that the self-hosted Services API metadata endpoints use on agent servers.

- SessionTimeoutDelay

Section kCura.EDDS.Web

Value 90000

Description The amount of time, in milliseconds, before a user's session expires that Relativity issues a warning.

- SFUMaxFilesToUpload

Section SFU

Value 100

Description

Determines the maximum number of files you can upload at one time using Simple File Upload. The maximum value you can set is 100.

- ShowAllEmailAddresses

Section Relativity.DocumentViewer

Value True

Description

Controls the default visibility of email address information in the Viewer. If set to True, Email Addresses will be expanded by default. Users can expand and collapse additional email address information by interacting with the expand and collapse toggle with the Viewer.

- ShowDeobfuscateTool

Section kCura.EDDS.Web

Value False

Description Controls whether the deobfuscate tool appears. If set to True, the deobfuscate tool appears. By default this value is set to False, and the deobfuscate tool does not appear.

- ShowStackTraceOnADSInstalls

Section kCura.EDDS.Web

Value False

Description Determines if ADS results will show the full stack trace to system administrators.

- ShowStackTraceOnError

Section kCura.EDDS.Web

Value True

Description Controls whether full stack traces appear to users when an error occurs. If set to True, full stack traces appear to users when an error occurs. If set to False, full stack traces do not appear to users when an error occurs.

Recommended security value

- Set the value to False unless you want all users with access to the Errors tab to see full stack traces for errors. Set to True for active troubleshooting situations.

- It is more secure to hide the details of error messages, so users cannot see more information than is necessary. Without hiding this information, software and server details could be revealed.

- SkipDocumentAuditDuringPublish

Section Relativity.Core

Value False

Description Determines whether Created and Native Created events are recorded in Document History during the publish phase of Processing. Setting the value to False will increase your publish time.

- SMTPPassword

Section kCura.Notification

Value blank

Description Defines the password for the username associated with the credentials of the SMTP server. This password validates against the SMTP authentication.

This instance setting must be manually added to your environment.

- SMTPPort

Section kCura.Notification

Value 25

Description Identifies the port used for SMTP transactions. You can change the default to another port based on the setup of the SMTP server in your environment. It must be an integer value.

This instance setting must be manually added to your environment.

- SMTPServer

Section kCura.Notification

Value blank

Description Identifies the SMTP server used to send notifications. Update the default value with a setting appropriate for your environment.

This instance setting must be manually added to your environment.

- SMTPSSLisRequired

Section kCura.Notification

Value False

Description If set to True, this instance setting forces all SMTP communication over SSL.

Recommended security value

True - this will ensure SMTP server sends encrypted emails.

- SMTPUserName

Section kCura.Notification

Value blank

Description Defines the username associated with the credentials of the SMTP server. It's validated against the SMTP authentication. The SMTPUserName must be associated with the same account as defined in EmailFrom.

This instance setting must be manually added to your environment.

- SQLCommandTimeout

Section kCura.ARM

Value 300

Description This setting controls the default SQLCommand timeout, in seconds, within ARM when executing select queries.

- SQLTimeout

Section kCura.EDDS.Procuro

Value 7200

Description The SQL Timeout value, in seconds, used when executing Procuro scripts..

- SslCertificateThumbprint

Section kCura.Service.ServiceHost

Value N/A

Description

If the Service Host Manager is configured to use HTTPS, you can use this instance setting to override the default automatic certificate selection behavior. The value is the thumbprint of the certificate for SSL bindings. For more information, see Service Host Manager.

This instance setting must be manually added to your environment.

- StopProcessingWhenNotInOffHours

Section Relativity.Conversion.Cache

Value True

Description Determines whether to stop processing when no longer within the off-hours time period.

- SSLOffloaded

Section kCura.EDDS.Web

Value False

Description Controls whether the native document viewer requests downloads with the protocol that the web browser uses to communicate with Relativity. This functionality is designed for use in environments that include an SSL Offloading server. If set to True, the native document viewer requests downloads with the protocol that the web browser uses to communicate with Relativity. If set to False, the native document viewer does not request downloads with the protocol that the web browser uses to communicate with Relativity.

- StatisticsOutputFileSizeLimit

Section Relativity.Core

Value 512

Description The maximum size, in kilobytes, for a file aggregated by a statistics event handler. This file size is per event handler in a given workspace. For example, the case statistics manager collects data added to this type of file.

- StratifiedSamplingAlgorithm

Section kCura.AssistedReview

Value FastSample

Description

Determines which cluster algorithm to use with Stratified sampling. Allowed values are FastSample and SmartSample.

FastSample, is a replacement algorithm for SmartSample that is much faster. Its parameters, operation and output is the same as SmartSample, except that it randomly picks each primary document. This randomness makes the results of FastSample non-deterministic, so its results will change from run to run, but it still produces excellent results.

- StratifiedSamplingCoverage

Section kCura.AssistedReview

Value .8

Description Determines the percentage of categorization coverage the sample set will provide. This is a decimal value.

- STRParallelizationFactor

Section Relativity.Core

Value 10

Description STR Parallel thread factor to be used for STRs using Lucene search.

- StuckBrandingManagerTimeout

Section Relativity.Production

Value 900

Description The amount of time, in seconds, that must elapse from the last message sent by a branding manager until it times out. Set to 0 to disable.

- SupportedVersions

Section kCura.EDDS.TemplateManager

Value X.X

Description Specifies the Relativity versions that the template manager supports.

- SupportXForwardedFor

Section Relativity.Core

Value False

Description Supports the X-Forwarded-For HTTP header field when checking for trusted client IP addresses on Relativity user accounts. If set to True, X-Forwarded-For is supported. If set to False, X-Forwarded-For is not supported.

- SyncExcludes

Section Relativity.Core

Value kCura.Sync.dll;

kCura.Sync.Utility.dll;

NullableTypes.dll;

itextsharp.dll

Description A semicolon-delimited list of system DLLs that exist in the sync directory that should not be recognized as syncs.

- SystemArtifactCacheExpiration

Section Relativity.Core

Value 240

Description The amount of time, in minutes, before the system artifact cache for any given workspace expires and refreshes the next time it's accessed.

If you're restoring archived databases into newly created workspaces, we recommend that you reduce this value to 15 or 30 minutes.

## T

- TallyBatchAmount

Section kCura.EDDS.Web

Value 1000

Description Determines the number of documents per batch for the tally process.

- TapiForceBcpHttpClient

Section Relativity.DataTransfer

Value "" (blank)

Description When this value is set to true, the HTTP transfer client is forced only for BCP operations. When it's false, the best fit transfer client is chosen at runtime. This functionality is also available as the TapiForceBcpHttpClient configuration setting for the RDC. For more information, see Configuring the RDC .

- TargetTransferRateMbps

Section kCura.Fta

Value 100

Description The default target transfer rate, in Mbps, for the file transfer job configuration.

- TenancyFeatureAvailable

Section Relativity.Core

Value False

Description

This instance setting was deprecated in Relativity 9.5.162.111 .

Determines the visibility of the values that allow a client to become a tenant. If set to True, features related to multi-tenancy are visible and available inside the environment. If set to False, users do not see anything related to multi-tenancy.

- TextExtractionTemporaryDirectory

Section Relativity.Core

Value blank

Description Identifies the temporary directory that the Text Extraction Manager uses. If left blank, the Text Extraction Manager uses the default document directory for the case.

- TextViewerMaxPageSize

Section Relativity.DocumentViewer

Value 512000

Description The maximum size, in bytes, of text streamed to the text viewer at once.

- TextViewerPageBufferSize

Section Relativity.DocumentViewer

Value 102400

Description The buffer size, in bytes, for text allowed to stream to the text viewer.

- ThresholdForIdClauseInMemoryForDeleteExtensions

Section Relativity.DocumentViewer

Value 100

Description Determines whether the query engine in Relativity uses a .csv file or a subquery in the IN clause of a report row when deleting reports and extensions.

- TitleText

Section kCura.EDDS.Web

Value Relativity

Description Defines the text of the header title within Relativity.

- TraceSampleRatePercentage

Section Relativity.OpenTelemetry

Value 25

Description The percentage between 0 and 100 that Open Telemetry samples distributed traces. As the probability increases, more resources such as CPU, memory, and disk are required to accommodate the higher sampling rates.

- TransmissionMetricCount

Section Relativity.Telemetry

Value 15000

Description

Determines the size of the batch used for sending metric data to the transmission agent. A batch is a group of metrics, and the number of metrics in a group is determined by the batch size.

This instance setting is available only when you install telemetry in your environment.

- TransmissionUpdateMetricCount

Section Relativity.Telemetry

Value 5000

Description

Determines the size of the batch used for transmitting data back to Relativity ODA LLC. A batch is a group of metrics, and the number of metrics in a group is determined by the batch size.

This instance setting is available only when you install telemetry in your environment.

- TreatArmRestoreJobFailureAsWarning

Section Relativity.StructuredAnalytics

Value True

Description

If set to True, ARM restore jobs will skip analytics indexes and structured analytics sets that have failed. To allow ARM jobs to error when an index or set fails, set this instance setting to False.

This instance setting is hidden and needs to be manually created to adjust the value. To learn more about creating an instance setting, see Instance settings .

- TreatHtmlAndXmlAsText

Section kCura.EDDS.Web.Distributed

Value True

Description

Controls the content-type header returned by files with HTM or HTML extensions from Relativity.Distributed.

If set to True, the content-type is text/plain. If set to False, the content-type is set to text/html. The default value is True. The net effect of setting this to True is that the Native Viewer displays the raw markup of HTML files instead of rendering the content.

Recommended security value

True - this helps prevent malicious code from executing when a Native document is viewed in the Viewer because it’s not automatically rendered. The content of the content-type header for the native files is unknown and, therefore, untrusted.

- TreeViewNodeWaitTimeMilliseconds

Section kCura.Fta

Value 500

Description The default wait time, in milliseconds, for the tree view node when users expand the node. When the wait time is over, a spinner displays in that node to notify users that data is loading.

- TrustedIPsForTokenLogin

Section kCura.EDDS.Web

Value empty

Description

A comma-delimited list of trusted IP addresses for logging in to Relativity with an authentication token. Enter any to trust all IPs.

This instance setting is deprecated and will be removed in a future version.

## U

- UIQueryTimeout

Section Relativity.Production

Value 120

Description The amount of time, in seconds, for a production view query to execute until it times out.

- UnpackAgentUpdateRateMilliseconds

Section kCura.Fta

Value 250

Description The default rate, in milliseconds, for the transfer agent to update the client job RDO during the auto-unpack process.

- UnpackFrontEndUpdateRateMilliseconds

Section kCura.Fta

Value 1000

Description The default rate, in milliseconds, to retrieve the auto-unpack progress from the RDO and update the front-end.

- UpdateIncludeInTextIndexOnRapImport

Section Relativity.Core

Value False

Description

Determines whether application fields with the Include In Text Index property set to True are included in the text index after import.

The default value is False. If set to True, the fields are included in the text index which requires the index to be rebuilt and can impact performance.

- UseAgentBasedConversion

Section Relativity.Core

Value False

Description

Change the value to true to use conversion agents on cloud instance.

- UseExtractedTextPathOnlyforPublish

Section Relativity.Core

Value True

Description

Controls whether during publish, extracted text is included as a path, value set to True, or as plain text, value set to False.

- UsePermissionsCachingMode

Section Relativity.Data

Value Standard

Description

Indicates the mechanism used to check Relativity user permissions. This instance setting can be set to the following:

- Cache —use a permissions caching mechanism to improve performance by minimizing calls to the SQL database.

- Standard (Default)—request the full permission matrix and then filter for required permissions. The most reliable, but may slow performance.

- Lazy —only pull permission rows with given artifactTypeId. No caching, but better performance than Standard.

- UsePermissionsCachingSeconds

Section Relativity.Data

Value 30 seconds

Description Indicates the number of seconds between the previous and next cache refresh. If a change occurred during this interval, the refresh updates the access rights that a user has to a Relativity object.

- UseTimeBasedConvertedCacheManagement

Section Relativity.Core

Value False

Description

Controls the toggle between cache size-based and last access-based cache management.

If set to True, your instance will use time-based cache management, which will reference the HoursToRetainConvertedDocuments instance setting value to determine how long to retain cache files. If set to false, your instance will use cache size-based cache management which will reference the CacheLocationUpperThreshold and CacheLocationLowerThreshold instance setting values to determine rules for retaining cache files.

- UserCanChangeDocumentViewerDefault

Section kCura.EDSS.Web

Value False

Description

Controls the default value on user creation for the User Can Change Document Viewer option.

If set to True, the user can change the document viewer. If set to False, the user cannot change the document viewer.

- UserCanChangePasswordDefault

Section Relativity.Authentication

Value True

Description

Sets default value for the UserCanChangePassword setting in the Authentication Provider Settings section of the Authentication Provider tab.

The default value for the UserCanChangePassword. True lets the user change their own password.

- UserCanChangeSettingsDefault

Section kCura.EDDS.Web

Value True

Description

Controls the default value on user creation for the User Can Change Settings option. If set to True, the user can change settings. If set to False, the user cannot change settings.

- UsersMustAgreeToTermsOfUse

Section kCura.EDDS.Web

Value False

Description

Controls whether Relativity displays the terms of use agreement and requires the user to accept it.

If set to True, the users must accept the terms of use when they log in to Relativity for the first time. If set to False, Relativity does not display the terms of use when users log in.

- UserStatusCacheExpiration

Section Relativity.Core

Value 30

Description The amount of time, in seconds, that the UserStatus cache is used from memory before refreshing with data from the UserStatus table.

- UseWindowsAuthentication

Section Relativity.Authentication

Value False

Description

Determines whether Relativity uses Windows Authentication.

Setting this value to False disables Windows Authentication. Setting this value to True enables Windows Authentication and requires the user to log in to Relativity from the current machine. You can then use the Authentication Data field on the User layout to map user credentials to a Windows account. Users can then enter their Windows passwords when logging in to Relativity.

## V

- ValidateAssemblyVersion

Section kCura.EDDS.WebAPI

Value x.x.*.*

Description

This instance setting is not used to determine the compatibility of the RDC or Import API with a specific version of Relativity. For more information, see RDC compatibility matrix .

Determines which parts of the Relativity version number are validated between the desktop client and the Relativity WebAPI version. For example, given the WebAPI version is 4.20.1.1 and the desktop client is 4.20.1.2:

- *.*.*.* match

- x.x.*.* match

- x.x.x.x do not match (the last node between the two is different)

- x.x.x.* match

- *.*.*.x do not match

- ViewableDocumentsIncrementCount

Section Relativity.Core

Value 5000

Description Determines the number of items that can be added to the viewable set on various list pages. It is the value in the Add next xxx drop-down menu on the bottom of various list pages.

- ViewerShowsHelpfulTroubleshootingErrorMessage

Section Relativity.DocumentViewer

Value True

Description

If set to True, the Viewer will display full-length and descriptive, custom error messages for each error that you experience. If set to False, the Viewer will display the following error message for every error you experience:

An Error Has Occurred

An error has occurred while trying to view this document.

- ViewersToHide

Section Relativity.DocumentViewer

Value True

Description

A comma-delimited list of Viewers to hide in the Review Interface. The specified Viewers will be hidden for all users across all workspaces. Valid options: Native, Image, Text, Production, Renderedpdf.

Currently, the Renderedpdf value does not hide the PDF Viewer in workspaces where a PDF application is installed.

- ViewQueryOptimization

Section Relativity.Core

Value 5

Description Do not modify without advice from Relativity Customer Support. This defines the number of entries cached for use with holding page view states. Requires an IISReset after you change the value.

- ViewStateNumPages

Section kCura.EDDS.Web

Value 3000

Description Determines the number of times the view state is saved before it is recycled. If the value is less than 1, it will default to 5.

- ViewerVisibilityWithoutContentForPreview

Section Relativity.DocumentViewer

Value Full

Description

This instance setting determines the user preference for Viewer visibility when using the Document Preview panel. The default value for this instance setting is Full with the option to set it to Limited, if desired.

If set to Limited, the user only sees the Viewers for which the document has content and, when navigating across documents, the active Viewer is automatically switched to a Viewer for which the document has content.

If set to Full, the user sees all of the Viewers regardless of whether there is content for them or not. When the user is navigating across documents, the active Viewer is never automatically switched.

## W

- WebAPIPath

Section kCura.EDDS.Web

Value During Relativity installation

Description

Identifies the WebAPI path for Relativity.

If you enter a full URL for this value, the protocol must match what is used in the browser. If Relativity is set up to use either HTTP or HTTPS, but not both, you can enter a full URL. Do not specific the protocol in this value if Relativity is set up to use both HTTP and HTTPS.

- WebClientBatchSize

Section Relativity.Core

Value 1000

Description Determines the number of pages within the document per batch for mass creating and mass deleting redactions within the web client.

- WebClientKeepAliveInterval

Section kCura.EDDS.Web

Value 5

Description The time interval, in minutes, that the Web Client sends ping-type requests to keep sessions open with servers that it uses, such as RelativityWebAPI and Relativity.Distributed.

- WebClientLongTimeout

Section kCura.EDDS.Web

Value 3000

Description The amount of time, in milliseconds, that the Web Client components waits for a response when making a potentially long-running WebAPI call before assuming the request has timed out.

- WebClientMaximumRetries

Section kCura.EDDS.Web

Value 2

Description Determines the maximum number of times the Web Client attempts to make a WebAPI call before throwing an error.

- WebClientNativeViewerCacheAheadMaxSizeInBytes

Section kCura.EDDS.Web

Value 52428800

Description The maximum size, in bytes, of a file the Relativity Web Client Native Viewer Cache Ahead technology caches.

- WebClientPerformanceLatencyTests

Section kCura.EDDS.Web

Value 5

Description Determines the number of latency tests that the Relativity Web Client performs when logging performance.

- WebClientPerformanceLoggingInterval

Section kCura.EDDS.Web

Value 300000

Description The amount of time, in milliseconds, between performance logging audits from the Relativity Web Client when logging performance.

- WebClientPopupDelay

Section kCura.EDDS.Web

Value 3000

Description The amount of time, in milliseconds, before pop-ups appear when performing a long running operation.

- WebClientRedactionWarning

Section kCura.EDDS.Web

Value False

Description

Controls whether a warning appears if there is a 25x25 redaction on the page.

If set to True, the warning appears if there is a 25x25 redaction on the page. If set to False, the warning does not appear.

- WebClientRequiredCookies

Section kCura.EDDS.Web

Value blank

Description A semicolon-delimited list of required cookies to pass from the web browser to the web client. Cookies are selected by verifying that the cookie name contains the listed string.

- WebClientTimeout

Section kCura.EDDS.Web

Value 3000

Description The amount of time, in milliseconds, that the web client components wait for a response when making a potentially long running WebAPI call before assuming the request has timed out.

- WebClientValidateAssemblyVersion

Section kCura.EDDS.Web

Value x.x.x.x

Description

Affects how the web client manager determines whether it needs to download and install a new version of the web client. For example, given that Relativity is version 4.20.1.1 and the web client is 4.20.1.2:

- *.*.*.* will not cause a download/install

- x.x.*.* will not cause a download/install

- x.x.x.x will cause a download/install (the last node between the two is different)

- x.x.x.* will not cause a download/install

- *.*.*.x will cause a download/install

- WindowsAuthIpRange

Section Relativity.Authentication

Value *.*.*.*

Description Specifies a list of IP addresses that Relativity uses to validate the IP address of a user during login. The default "*.*.*.*" permits all IP address. When specifying multiple IP addresses, enter each on a separate line. If you do not enter any value for this instance setting, then the default value (*.*.*.*) lets users log in from any IP address. When specifying multiple IP addresses, enter each on a separate line.

- WordIndexMaxWordSize

Section kCura.EDDS.Agents

Value 200

Description Determines the longest character length of a word when creating a word index. Words larger than this value are truncated.

- WorkerStatusCacheExpiration

Section Relativity.Core

Value 30

Description The amount of time, in seconds, that Invariant is cached in the Worker Status Kepler service before refreshing.

- WorkerStatusServiceTimeout

Section Relativity.Core

Value 5

Description The amount of time, in seconds, before calls to Invariant from the Worker Status Kepler server time out.

- WorkspaceUpgradeAutoRetryLimit

Section Relativity.Core

Value 1

Description The number of times that the Workspace Upgrade Manager agent automatically retries a failed workspace upgrade before it is marked as completed or failed. The maximum effective value is 5, and larger values are reset to 5. A value of 0 disables the auto-retry logic, and requires you to manually retry a failed workspace.

- WorkspaceUpgradeCountForGCFullCollect

Section Relativity.Core

Value 0

Description Controls the number of workspaces a group of Application Installer Manager agents on an agent server upgrade before performing a full garbage collection, including compacting the large object heap. For example, if you set this value to 500, and you have two Application Installer Manager agents on an agent server, the garbage collection occurs when both agents have installed applications in a total of 500 workspaces. This setting reduces the amount of memory used during workspace upgrades in large environments. A value of 0 disables the garbage collection and causes memory usage to grow faster during workspace upgrades within large environments. The overall speed of your upgrade may decrease over time. Additionally, the upgrade has the potential to consume all the server's memory.

- WorkspaceUpgradeCountForGCFullCollect

Section Relativity.Core

Value 0

Description Controls the number of workspaces a group of Application Installer Manager agents on an agent server upgrade before performing a full garbage collection, including compacting the large object heap. For example, if you set this value to 500, and you have two Application Installer Manager agents on an agent server, the garbage collection occurs when both agents have installed applications in a total of 500 workspaces. This setting reduces the amount of memory used during workspace upgrades in large environments. A value of 0 disables the garbage collection and causes memory usage to grow faster during workspace upgrades within large environments. The overall speed of your upgrade may decrease over time. Additionally, the upgrade has the potential to consume all the server's memory.

- WrapBrandingTextDefault

Section Relativity.Core

Value false

Description Determines the default value for the Wrap Branding Text field. The field determines whether a Production's branding text will wrap if the content of two adjacent footers or headers are likely to overlap.

## X

- XForwardedForTrustedProxies

Section kCura.EDDS.Web

Value blank

Description Specifies a list of comma-separated IP addresses or ranges, such as wildcards and classless inter-domain routing (CIDR) blocks. These addresses are excluded when the X-Forwarded-For header is checked to determine whether a user's IP is trusted.

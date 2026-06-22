---
title: "Database schema updates"
url: https://platform.relativity.com/Server2025/Content/What_s_new/Database_schema_updates.htm
collection: developer
fetched_at: 2026-06-22T06:29:15+00:00
sha256: d945fb0abe1b4f02e567ee07e6314477afbb7a3b852b98cb6ddd880abf7490c3
---

Database schema updates

# Database schema updates

The table below lists the updates made in recent releases to both the EDDS and Workspaces database schema.

Changes marked as Continuous improvement in the Version column below were deployed outside of a planned release.

## Database schema updates table

Database Table affected Change type Change details Version

EDDS UserPasswordResetToken Modification Added new column ResetPasswordCounter to track the email count for Forgot Password functionality (without Reset Link). Server 2025

EDDS, Workspace GroupUser Modification Added the LastModifiedOn column to the GroupUser table to track the timestamp of when a user is added to a group. This change addresses the UGS app defect where users were being synced only after an edit. With this update, the system now correctly identifies users as modified when they are added to groups, ensuring proper synchronization. Server 2025

Workspace AnalyticsIndexMetadataRepository Modification The IngestionJobID column is new and it stores the ID of the Analytics index job. Server 2024

Workspace

ImageQueueDataAccess Addition The ImageQueueDataAccess table is new and is created in the middle of an image-to-PDF job in your workspace. The table name structure is this: PDF_ID_JOBGUID (e.g. PDF_96_IMAGE_71d9aa6bd7a34504aa7e5b8a2a48d399) Server 2024

EDDS

WorkspaceCreateRequestGuid Addition The WorkspaceCreateRequestGuid table is new, and it tracks workspace duplication requests using a unique request GUID, aiding in identifying and managing duplicates during workspace creation. It records request GUIDs, details, responses, and timestamps. Server 2024

EDDS

UpdateLogs Addition The UpdateLogs table is new and stores a detailed list of updates performed on the Relativity instance. Server 2024

EDDS,

Workspace

ScriptRun Modification The ScriptLastModified and AgentCheckInDatetime columns have been changed from type datetime2 to type datetime. Server 2024

EDDS CustomPage Modification The IsStaticBasedContent column is new on the CustomPage table and was added to monitor the type of the CustomPages Server 2024

EDDS ApplicationToggle Addition The ApplicationToggle table is new and stores a list of toggles used by an ADS application. Prairie Smoke/12.2

EDDS

- AnalyticsCoreWorkspaceMigrationManagerQueue

- AnalyticsCoreManagerMigrationManagerQueue

Modification The AgentName column has been removed. The JobLockExpire column is new and stores an indicator that the Analytics Core ARM agents are working on a job. When the job is isn't being worked on, this value is null. Prairie Smoke/12.2

Workspace AnalyticsIndexMetadata Modification The ActivationInProgress column is new and it stores an indicator of whether index activation is in progress. A value of 1 indicates activation is in progress. A value of 0 indicates activation is not in progress. Prairie Smoke/12.2

EDDS ProductionSetQueue Modification The following columns are new and are used to resume the staging process when a production staging is paused for RAP deploy in RelativityOne:

- LastProductionInfoRecord stores the last production information record that was created in the staging process

- StagingBatchSize stores the batch size for creating production information objects.

Prairie Smoke/12.2

EDDS ApplicationComponent Addition The ApplicationComponent table is new and it maintains a record of all guids associated with Library Applications within the instance. Prairie Smoke/12.2

Workspace ActiveLearningReview Modification The following columns are new:

- IncludeRecall

- ElusionRate

- EludedDocuments

- Precision

- PrecisionMarginofError

- Recall

- RecallLower

- RecallUpper

- Richness

- RichnessMarginofError

ElusionRate and EludedDocuments are used to store Elusion Test statistics for an accepted or rejected Elusion Test so they do not need to be recalculated.

All other columns are used to store new statistics for an Elusion Test that were not previously displayed at all (users will need to opt in at the time of starting an Elusion Test, because this involves changes to how we sample documents)

Osier/12.1

Workspace Document Modification Any missing relational indexes are recreated during the database upgrade phase. Osier/12.1

EDDS ToggleDefault Addition The ToggleDefault table is new and it stores toggle default values. Osier/12.1

EDDS Toggle Modification The Default column has been removed, and the IsEnabled column no longer allows null values. Osier/12.1

EDDS

- OCRSetQueue

- OCRWorkerQueue

Removal As part of Relativity's OCR decoupling, we have removed the following two tables from EDDS database:

- OCRHistory

- OCRSetQueue

- OCRWorkerQueue

- SystemArtifact

Osier/12.1

EDDS PdfMaintenance Addition This new table is a component of the new PDF application. Ninebark/12.0

EDDS AnalyticsIndexMetadata Modification The new field LastJobStageFinished in AnalyticsIndexMetadata keeps track of the last time a conceptual analytics index finished a build-related (population, build, activation, errored) process. This is similar to the existing field LastUsedOn which timestamps the same times as LastJobStageFinished but also includes times that the index was used for queries. Ninebark/12.0

EDDS/Workspace ScriptRun Modification The ScriptLastModified and AgentCheckInDatetime columns have been changed from type datetime2 to type datetime. Osier/12.1

EDDS Toggles Modification The IsEnabled column now allows nulls. Osier/12.1

Workspace DgImportFileInfoType Addition It's required for table valued parameters to move large number of rows in one call and to avoid a huge IN clause. Osier/12.1

Workspace AnalyticsCategorizationSetMetadata Modification The Analytics Core application post install event handler adds the KeepRemovedResults BIT NOT NULL column to the AnalyticsCategorizationSetMetadata table. This column acts as a per categorization set level switch to enable or disable functionality used by the Trace application. Ninebark/12.0

Workspace ImageQueueDataAccess Addition The ImageQueueDataAccess table is new and is created in the middle of an image-to-PDF job in your workspace. The table name structure is this: PDF_ID_JOBGUID (e.g. PDF_96_IMAGE_71d9aa6bd7a34504aa7e5b8a2a48d399) Ninebark/12.0

EDDS N/A Modification A new job type has been introduced for processing. Job type name is FinalizeJobPublishWithExpression jobtype. This job type is entered as a system artifact. Osier/12.1

EDDS AgentType Modification Removed the OCR Set Manager and OCR Worker agent types from Relativity. They were replaced with new OCR Agents. Osier/12.1

EDDS AccessControlListPermission Modification With this change, custom page permissions have been removed from the Everyone group. Ninebark/12.0

EDDS AnalyticsIndexC4PopulationJob Modification There is a new column called JobID, and it stores population job IDs for reporting purposes. Ninebark/12.0

Workspace PDFjob Modification There is a new column called Rotation for saving image rotation settings while generating PDFs from images. The PDFjob table is dynamically generated to hold the references to images for PDF jobs. Mayapple/11.3

EDDS AgentType Modification There is a new column on the AgentType table called SharedCompute. Ninebark/12.0

EDDS PDFjob Modification The AuditArtifactID column lists the actual user getting audited instead of the preview user. This is the result of a defect fix. Lanceleaf/11.2

Workspace AutomatedWorkflowEvents Addition The new table AutomatedWorkflowEvents is created at the workspace level where the Relativity Automated Workflows application in installed, to account for changes in the workflow and action-level status. For this reason, few events will be created, and fired when status updates are received for the workflow and/or action within a workflow. This way, the front end can display status projections to Automated Workflow users. Lanceleaf/11.2 (Update 1)

Workspace ContainerArtifactAncestry Removal We've removed legacy ContainerArtifactAncestry table and replaced it with references to ContainerArtifact in ExtendedFolder. We've also removed the following unused triggers:

- FolderDelete

- FolderInsert

- SearchContainerDelete SearchContainerInsert

Osier EA

EDDS ApplicationInstall Modification There are two new columns on the ApplicationInstall table to track cases in which an application install fails.

- ExceptionCategory - the root cause of a particular failure.

- FailedTask - the step where the failure occurred.

Ninebark/12.0

EDDS LoginMethod Modification There are two new columns on LoginMethod table:

- AuthenticatorSecretID - refers to the user's TFA authenticator seed key in secre store

- AuthenticatorSecretValidated - tracks if the user has used the authenticator login at least once

Ninebark/12.0

EDDS AuthenticatorCodeHistory Addition The new table AuthenticatorCodeHistory keeps a subset history of previous one-time-use passcodes used at login. This is to prevent a user from using a single code multiple times in a short period of time. Ninebark/12.0

Workspace

- RelativityAutomatedWorkflowsTriggers

- RelativityAutomatedWorkflowsActions

Addition There is a new Version column on each of the following tables:

- RelativityAutomatedWorkflowsTriggers

- RelativityAutomatedWorkflowsActions

Lanceleaf/11.2 (Update 1)

EDDS PdfJob Addition We've added an index to the PDF application's job table. Juniper/11.1 (Update 2)

Workspace ProductionDataSource Modification The following columns are new:

- NativeRedactTextField (a single object type)

- BurnNativeRedactions (a boolean type field)

White Sedge 2/13.1

EDDS ProductionSetQueue Modification The following columns are new and are in place to track the progress of a production set:

- NativeBrandingQueueRecordsCount

- NativesWithErrors

- NativesRemaining

- TotalNatives

Yarrow 0/13.2

EDDS AnalyticsIndexC4PopulationJob Modification The JobLockExpire column is new, and it stores a datetime value to move away from agent processor locks to time out locks. This change was made to support the transition of RelativityOne Analytics Index Population Manager agents to k8s. Tiger Lily 0/13.0

Workspace AnalyticsIndexMetadataRepository Modification The IngestionJobID column is new and it stores the ID of the Analytics index job. Sundrop/12.3

EDDS CustomPage Modification The IsStaticBasedContent column is new on the CustomPage table and was added to monitor the type of the CustomPages Sundrop/12.3

EDDS ApplicationToggle Addition The ApplicationToggle table is new and stores a list of toggles used by an ADS application. Prairie Smoke/12.2

EDDS

- AnalyticsCoreWorkspaceMigrationManagerQueue

- AnalyticsCoreManagerMigrationManagerQueue

Modification The AgentName column has been removed. The JobLockExpire column is new and stores an indicator that the Analytics Core ARM agents are working on a job. When the job is isn't being worked on, this value is null. Prairie Smoke/12.2

Workspace AnalyticsIndexMetadata Modification The ActivationInProgress column is new and it stores an indicator of whether index activation is in progress. A value of 1 indicates activation is in progress. A value of 0 indicates activation is not in progress. Prairie Smoke/12.2

EDDS ProductionSetQueue Modification The following columns are new and are used to resume the staging process when a production staging is paused for RAP deploy in RelativityOne:

- LastProductionInfoRecord stores the last production information record that was created in the staging process

- StagingBatchSize stores the batch size for creating production information objects.

Prairie Smoke/12.2

EDDS ApplicationComponent Addition The ApplicationComponent table is new and it maintains a record of all guids associated with Library Applications within the instance. Prairie Smoke/12.2

Workspace ActiveLearningReview Modification The following columns are new:

- IncludeRecall

- ElusionRate

- EludedDocuments

- Precision

- PrecisionMarginofError

- Recall

- RecallLower

- RecallUpper

- Richness

- RichnessMarginofError

ElusionRate and EludedDocuments are used to store Elusion Test statistics for an accepted or rejected Elusion Test so they do not need to be recalculated.

All other columns are used to store new statistics for an Elusion Test that were not previously displayed at all (users will need to opt in at the time of starting an Elusion Test, because this involves changes to how we sample documents)

Osier/12.1

Workspace Document Modification Any missing relational indexes are recreated during the database upgrade phase. Osier/12.1

EDDS ToggleDefault Addition The ToggleDefault table is new and it stores toggle default values. Osier/12.1

EDDS Toggle Modification The Default column has been removed, and the IsEnabled column no longer allows null values. Osier/12.1

EDDS

- OCRSetQueue

- OCRWorkerQueue

Removal As part of Relativity's OCR decoupling, we have removed the following two tables from EDDS database:

- OCRHistory

- OCRSetQueue

- OCRWorkerQueue

- SystemArtifact

Osier/12.1

EDDS PdfMaintenance Addition This new table is a component of the new PDF application. Ninebark/12.0

EDDS AnalyticsIndexMetadata Modification The new field LastJobStageFinished in AnalyticsIndexMetadata keeps track of the last time a conceptual analytics index finished a build-related (population, build, activation, errored) process. This is similar to the existing field LastUsedOn which timestamps the same times as LastJobStageFinished but also includes times that the index was used for queries. Ninebark/12.0

EDDS/Workspace ScriptRun Modification The ScriptLastModified and AgentCheckInDatetime columns have been changed from type datetime2 to type datetime. Osier/12.1

EDDS Toggles Modification The IsEnabled column now allows nulls. Osier/12.1

Workspace DgImportFileInfoType Addition It's required for table valued parameters to move large number of rows in one call and to avoid a huge IN clause. Osier/12.1

Workspace AnalyticsCategorizationSetMetadata Modification The Analytics Core application post install event handler adds the KeepRemovedResults BIT NOT NULL column to the AnalyticsCategorizationSetMetadata table. This column acts as a per categorization set level switch to enable or disable functionality used by the Trace application. Ninebark/12.0

Workspace ImageQueueDataAccess Addition The ImageQueueDataAccess table is new and is created in the middle of an image-to-PDF job in your workspace. The table name structure is this: PDF_ID_JOBGUID (e.g. PDF_96_IMAGE_71d9aa6bd7a34504aa7e5b8a2a48d399) Ninebark/12.0

EDDS N/A Modification A new job type has been introduced for processing. Job type name is FinalizeJobPublishWithExpression jobtype. This job type is entered as a system artifact. Osier/12.1

EDDS AgentType Modification Removed the OCR Set Manager and OCR Worker agent types from Relativity. They were replaced with new OCR Agents. Osier/12.1

EDDS AccessControlListPermission Modification With this change, custom page permissions have been removed from the Everyone group. Ninebark/12.0

EDDS AnalyticsIndexC4PopulationJob Modification There is a new column called JobID, and it stores population job IDs for reporting purposes. Ninebark/12.0

Workspace PDFjob Modification There is a new column called Rotation for saving image rotation settings while generating PDFs from images. The PDFjob table is dynamically generated to hold the references to images for PDF jobs. Mayapple/11.3

EDDS AgentType Modification There is a new column on the AgentType table called SharedCompute. Ninebark/12.0

EDDS PDFjob Modification The AuditArtifactID column lists the actual user getting audited instead of the preview user. This is the result of a defect fix. Lanceleaf/11.2

Workspace AutomatedWorkflowEvents Addition The new table AutomatedWorkflowEvents is created at the workspace level where the Relativity Automated Workflows application in installed, to account for changes in the workflow and action-level status. For this reason, few events will be created, and fired when status updates are received for the workflow and/or action within a workflow. This way, the front end can display status projections to Automated Workflow users. Lanceleaf/11.2 (Update 1)

Workspace ContainerArtifactAncestry Removal We've removed legacy ContainerArtifactAncestry table and replaced it with references to ContainerArtifact in ExtendedFolder. We've also removed the following unused triggers:

- FolderDelete

- FolderInsert

- SearchContainerDelete SearchContainerInsert

Osier EA

EDDS ApplicationInstall Modification There are two new columns on the ApplicationInstall table to track cases in which an application install fails.

- ExceptionCategory - the root cause of a particular failure. FailedTask - the step where the failure occurred.

Ninebark/12.0

EDDS LoginMethod Modification There are two new columns on LoginMethod table:

- AuthenticatorSecretID - refers to the user's TFA authenticator seed key in secre store

- AuthenticatorSecretValidated - tracks if the user has used the authenticator login at least once

Ninebark/12.0

EDDS AuthenticatorCodeHistory Addition The new table AuthenticatorCodeHistory keeps a subset history of previous one-time-use passcodes used at login. This is to prevent a user from using a single code multiple times in a short period of time. Ninebark/12.0

Workspace

- RelativityAutomatedWorkflowsTriggers

- RelativityAutomatedWorkflowsActions

Addition There is a new Version column on each of the following tables:

- RelativityAutomatedWorkflowsTriggers

- RelativityAutomatedWorkflowsActions

Lanceleaf/11.2 (Update 1)

EDDS PdfJob Addition We've added an index to the PDF application's job table. Juniper/11.1 (Update 2)

Technical notes

- SQL Access Is Not Recommended. Due to risks, Relativity strongly recommends that customers use the APIs and other Relativity Admin-Dev Tools rather than seeking direct access to the SQL server backend and data store for Client’s RelativityOne Instance.

- User Training and Risks. SQL Access requires advanced technical knowledge, and using SQL Access substantially increases the risks of data destruction, loss or corruption, and RelativityOne system degradation, interruption or failures. Improperly using SQL Access carries substantial risk of destruction of data and degradation or possible interruption of RelativityOne; and Relativity shall not be liable for any mistakes, errors, or other unintended consequences of using SQL Access. If Relativity provides any certificates, passwords, and other credentials (“Client Access Credentials”) in connection with SQL Access, Client is solely responsible for managing the security of Client Access Credentials, and Relativity will not be liable for any unauthorized access or improper use of such Client Access Credentials.

- Compatibility and Other Risks. Relativity periodically updates and modifies RelativityOne, including SQL, in Relativity’s discretion. Relativity: (a) makes no guarantee that the SQL BD Schema update provided herein is free of errors or that there will be compatibility of updates to RelativityOne with any developments, integrations or other actions that Client or its vendors take based on their SQL Access; and (b) will not be liable the SQL BD Schema update provided herein contains errors or if Relativity’s updates and modifications to RelativityOne are incompatible with existing and under-development applications, integrations or other actions that Client or its vendors have taken in using SQL Access.

- Sandbox Testing. Client or its vendors shall thoroughly test for continuing compatibility and shall resolve any resulting compatibility issues (preferably including a high quality automated program). If Client or its vendor discovers any errors or issues with RelativityOne or the SQL BD Schema update provided herein, Client should promptly send an email with relevant details to Relativity Support . Relativity provides a Sandbox Test Environment for integration and functional testing and validation of code, Relativity Custom Applications, extensions, and integrations created by Client or its vendors (“Sandbox Test Purpose”). The Sandbox Test Purpose does not include performance testing or any development work beyond testing. Note that: (a) the Sandbox is a scaled-down, limited version of Client’s RelativityOne Instance; (b) for avoidance of doubt, RelativityOne Availability SLA provisions are not applicable for the Sandbox, which may need to be “turned on” and will be available only while in use by Client.

- Other Client-Related Problems. Relativity is not responsible for RelativityOne issues, errors, loss or corruption of Client Data, or events or problems degrading or interrupting RelativityOne Availability, caused by Client’s personnel, its other enabled users, its third party vendors or their products or services in improperly using SQL Access (“Client-Related Problems”). Any lack of Availability arising from any Client-Related Problems shall be Excused Downtime and shall not count for purposes of determining service credits. However, in such event, Relativity will assist Client by providing a “Data Restore” procedure. In addition, upon Client’s request, Relativity will use reasonable efforts to provide Client and Client’s third party vendors with temporary limited direct access (“Limited Direct Access”) to applicable resources in the RelativityOne infrastructure to the extent necessary to troubleshoot issues with any of their Relativity Custom Applications which are publicly listed on Relativity’s website, provided: (a) Client and/or Client’s third party vendors have already made reasonable efforts to resolve the issue; (b) RelativityOne infrastructure Limited Direct Access will be supervised by Relativity Support and will not involve any access to PaaS resources; and (c) RelativityOne infrastructure Limited Direct Access otherwise complies with the terms of a standard operating and security procedure which Relativity may develop from time to time for handling such requests. Any support that Relativity provides in seeking to help resolve a Client-Related Problem shall not be covered by Relativity support obligations and Client may be required to pay Relativity’s then applicable standard hourly rates.

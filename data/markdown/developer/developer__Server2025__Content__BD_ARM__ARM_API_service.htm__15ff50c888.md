---
title: "ARM API (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_ARM/ARM_API_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:44+00:00
sha256: 0f247092bda79169b6a780ada419fe0793bb622bba9ddbc051bc960d9eda3587
---

ARM API (REST)

# ARM API (REST)

The ARM API provides a REST service that supports multiple operations required to archive, restore, and move Relativity workspace data. You can also use to view information on currently running ARM jobs or to list available workspaces or ARM archives. For example, you could use this service to populate a custom dialog in your application with scheduled ARM archive jobs.

For more information on the ARM application, see Arm Overview on the Relativity documentation site.

## Fundamentals for the ARM API

Review the following guidelines for working with the ARM API.

### Sample use cases

A typical use case would be building a custom ARM client or automating the creation or execution of ARM jobs.

A typical workflow requires these steps:

- Create ARM job (Archive, Restore, Database Restore, or Move)

- Run the job

- Read job status to get information about the job execution and whether it has completed.

## Archive Create

Use this endpoint to create Archive jobs.

To create Archive jobs, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/archive-jobs
```

Copy

Sample JSON request

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
{

    "request":  {

      "WorkspaceID": 1234567,

      "ArchiveDirectory": "\\\\server\\armarchive",

      "JobPriority": "High",

      "ScheduledStartTime": "2020-04-08T14:00:00",

      "MigratorOptions": {

          "IncludeDatabaseBackup": true,

          "IncludeDtSearch": true,

          "IncludeConceptualAnalytics": true,

          "IncludeStructuredAnalytics": true,

          "IncludeDataGrid": true

      },

      "FileOptions": {

          "IncludeRepositoryFiles": true,

          "IncludeLinkedFiles": true,

          "MissingFileBehavior": "SkipFile"

      },

      "ProcessingOptions": {

          "IncludeProcessing": true,

          "IncludeProcessingFiles": true,

          "ProcessingMissingFileBehavior": "SkipFile"

      },

      "ExtendedWorkspaceDataOptions": {

          "IncludeExtendedWorkspaceData": true,

          "ApplicationErrorExportBehavior": "SkipApplication"

      },

      "NotificationOptions": {

          "NotifyJobCreator": true,

          "NotifyJobExecutor": true

      },

    "UiJobActionsLocked": false,

    "UseDefaultArchiveDirectory": false

    }

}
```

Request body parameters:

- WorkspaceID - the artifact ID of the workspace to archive for the archive job. This Workspace must not be in the process of upgrading or currently in use by another ARM job.

- JobPriority - priority of execution for the job. Possible options include "Low", "Medium", and "High".

- ArchiveDirectory - file path of the configured archive directory to save the archive to. When this is set UseDefaultArchiveDirectory has to be false.

- ScheduledStartTime - scheduled time when the job will be run.

- MigratorOptions

- IncludeDatabaseBackup - indicates if the workspace database backup is included in the archive.

- IncludeDtSearch - indicates whether dtSearch indices will be included in the archive directory.

- IncludeConceptualAnalytics - indicates whether Conceptual Analytics indices will be included in the archive directory.

- IncludeStructuredAnalytics - indicates whether Structured Analytics sets will be included in the archive directory.

- IncludeDataGrid - indicates whether Data Grid application data will be present in the archive directory.

- FileOptions

- IncludeRepositoryFiles - indicates whether all files included in the workspace repository, including files from file fields, will be archived in the archive directory.

- IncludeLinkedFiles - indicates whether all linked files that do not exist in the workspace file repository will be archived in the archive directory.

- MissingFileBehavior - indicates whether to skip ("SkipFile") or stop ("StopJob") when missing files are detected during the archiving process. If there is potential for any files to not be found while the job is running, skipping them will result in compiling a downloadable list of the files that were missing and allow the job to complete without error. Setting this to stop will immediately stop on the first missing file and cannot resume until the file is placed in the expected location.

- ProcessingOptions

- IncludeProcessing - indicates whether Processing application data will be present in the archive directory.

- IncludeProcessingFiles - indicates whether all the files and containers that have been discovered by Processing will be archived and placed in the Invariant directory.

- ProcessingMissingFileBehavior - indicates whether to skip ("SkipFile") or stop ("StopJob") when missing Processing files are detected during the archiving process. If there is potential for any files to not be found while the job is running, skipping them will result in compiling a downloadable list of the files that were missing and allow the job to complete without error. Setting this to stop will immediately stop on the first missing file and cannot resume until the file is placed in the expected location.

- ExtendedWorkspaceDataOptions

- IncludeExtendedWorkspaceData - indicates whether extended workspace information is included in the archive. This includes installed applications, linked relativity scripts, and non-application event handlers.

- ApplicationErrorExportBehavior - indicates whether to skip applications that errored during export ("SkipApplication") or to stop ("StopJob").

- NotificationOptions

- NotifyJobCreator - indicates if email notifications will be sent to the job creator.

- NotifyJobExecutor - indicates if email notifications will be sent to the job executor.

- UiJobActionsLocked - indicates if job actions normally available on UI should be visible for the user. This behavior can be override by adding boolean instance setting OverrideUiJobActionsLock.

- UseDefaultArchiveDirectory - when this option is set to true leave ArchiveDirectory empty. ARM will select the fist valid one from configuration.

If job creation is successful, response will be the artifact ID of the newly created job. If the job creation could not be completed, the response will contain validation errors with more detailed information.

## Archive Read

Use this endpoint to read Archive jobs.

To read Archive jobs, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/archive-jobs/<jobID>
```

Request body is empty, the job ID is passed in via the URL.

Copy

Sample JSON response

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
{

    "JobID": 3026,

    "JobName": "Archive New Case Template (1014823) Workspace",

    "JobExecutionID": 3026,

    "JobExecutionGuid": "895ef98e-6c8b-4573-867a-d11f0b39bd54",

    "ArchivePath": "\\\\server\\armarchive\\1014823_New_Case_Template_20200320103044",

    "WorkspaceID": 1014823,

    "ScheduledStartTime": "2020-04-08T14:00:00",

    "JobDetails": {

        "CreatedOn": "2020-03-20T10:30:44.137",

        "ModifiedTime": "2020-03-20T10:30:44.2",

        "SubmittedBy": "Admin, Relativity",

        "State": "Complete",

        "Priority": "Low",

        "ActionsHistory": [

            {

                "Date": "2020-03-20T10:30:44.17",

                "Type": "Created",

                "UserName": "Admin, Relativity"

            },

            {

                "Date": "2020-03-20T10:30:47.607",

                "Type": "Started",

                "UserName": "Admin, Relativity"

            },

            {

                "Date": "2020-03-20T10:31:06.007",

                "Type": "Completed",

                "UserName": "Agent"

            }

        ]

    },

    "MigratorOptions": {

        "IncludeDatabaseBackup": true,

        "IncludeDtSearch": false,

        "IncludeConceptualAnalytics": false,

        "IncludeStructuredAnalytics": false,

        "IncludeDataGrid": false

    },

    "FileOptions": {

        "IncludeRepositoryFiles": true,

        "IncludeLinkedFiles": true,

        "MissingFileBehavior": "SkipFile"

    },

    "ProcessingOptions": {

        "IncludeProcessing": false,

        "IncludeProcessingFiles": false,

        "ProcessingMissingFileBehavior": "SkipFile"

    },

    "ExtendedWorkspaceDataOptions": {

        "IncludeExtendedWorkspaceData": false,

        "ApplicationErrorExportBehavior": "SkipApplication"

    },

    "NotificationOptions": {

        "NotifyJobCreator": false,

        "NotifyJobExecutor": false

    }

    "UiJobActionsLocked": false

}
```

Response body parameters:

- JobID - ID of the created Archive job. This is a generated field.

- JobName - name of the Archive job created. This is a generated field.

- JobExecutionID - ID of the execution of the created Archive Job. This is a generated field.

- JobExecutionGuid - execution GUID of the created Archive Job. This is a generated field.

- ArchivePath - path to the ARM archive. It is created using the ArchiveDirectory field from a Create/Update request and the archive folder name, which is generated.

- WorkspaceID - artifact ID of the workspace archived by the job. This is a generated field.

- ScheduledStartTime - scheduled time when the job will be run.

- JobDetails

- CreatedOn - date and time of job creation. This is a generated field.

- ModifiedTime - date and time of most recent job modification. This is a generated field.

- SubmittedBy - the user responsible for the submission of the job. This is a generated field.

- State - current job state. This is a read-only field.

- Priority - priority of execution for the job.

- ActionsHistory - list of job actions with the following details: date, type and user name. This is a read-only field.

- MigratorOptions

- IncludeDatabaseBackup - indicates if the workspace database backup will be included in the archive.

- IncludeDtSearch - indicates whether dtSearch indices will be included in the archive directory.

- IncludeConceptualAnalytics - indicates whether Conceptual Analytics indices will be included in the archive directory.

- IncludeStructuredAnalytics - indicates whether Structured Analytics sets will be included in the archive directory.

- IncludeDataGrid - indicates whether Data Grid application data will be present in the archive directory.

- FileOptions

- IncludeRepositoryFiles - indicates whether all files included in the workspace repository, including files from file fields, will be archived in the archive directory.

- IncludeLinkedFiles - indicates whether all linked files that do not exist in the workspace file repository will be archived in the archive directory.

- MissingFileBehavior - indicates whether to skip ("SkipFile") or stop ("StopJob") when missing files are detected during the archiving process. If there is potential for any files to not be found while the job is running, skipping them will result in compiling a downloadable list of the files that were missing and allow the job to complete without error. Setting this to stop will immediately stop on the first missing file and cannot resume until the file is placed in the expected location.

- ProcessingOptions

- IncludeProcessing - indicates whether Processing application data will be present in the archive directory.

- IncludeProcessingFiles - indicates whether all the files and containers that have been discovered by Processing will be archived and placed in the Invariant directory.

- ProcessingMissingFileBehavior - indicates whether to skip ("SkipFile") or stop ("StopJob") when missing Processing files are detected during the archiving process. If there is potential for any files to not be found while the job is running, skipping them will result in compiling a downloadable list of the files that were missing and allow the job to complete without error. Setting this to stop will immediately stop on the first missing file and cannot resume until the file is placed in the expected location.

- NotificationOptions

- NotifyJobCreator - indicates if email notifications will be sent to the job creator.

- NotifyJobExecutor - indicates if email notifications will be sent to the job executor.

- UiJobActionsLocked - indicates if job actions normally available on UI should be visible for the user. This behavior can be override by adding boolean instance setting OverrideUiJobActionsLock.

## Archive Update

Use this endpoint to update Archive jobs.

To update Archive jobs, send a PUT request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/archive-jobs/<jobID>
```

The request body is the same as Archive Create , and the job ID is passed in via the URL.

The response returns a status code of 200 when the service successfully updates an Archive job. There is no response body.

## Archive Delete

Use this endpoint to delete Archive jobs.

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/archive-jobs/<jobID>
```

Request body is empty, the job ID is passed in via the URL.

The response returns a status code of 200 when the service successfully deletes an archive job. There is no response body.

## Restore Create

Use this endpoint to create Restore jobs.

To create Restore jobs, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/restore-jobs/
```

Copy

Sample JSON request

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
{

    "request":  {

      "ArchivePath": "\\\\server\\fileshare\\armarchive\\1027887_WorkspaceName_20200113133434",

      "JobPriority": "Medium",

      "ScheduledStartTime": "2020-04-08T14:00:00",

      "ExistingTargetDatabase": null,

      "DestinationOptions": {

        "DatabaseServerID": 1015096,

        "ResourcePoolID": 1015040,

        "MatterID": 1000002,

        "CacheLocationID": 1015534,

        "FileRepositoryID": 1014887

      },

      "MigratorsDestinationOptions": {

        "StructuredAnalyticsServerID": null,

        "ConceptualAnalyticsServerID": null,

        "DtSearchLocationID": null

      },

      "AdvancedFileOptions": {

        "ReferenceFilesAsArchiveLinks": false,

        "UpdateRepositoryFilePaths": true,

        "UpdateLinkedFilePaths": true

      },

      "UserMapping": {

        "AutoMapUsers": true,

        "UserMappings": [

            {

              "ArchiveUserID": 1014868,

              "InstanceUserID": 2156304

            }

         ]

      },

      "GroupMapping": {

        "AutoMapGroups": false,

        "GroupMappings": [

            {

              "ArchiveGroupID": 1038349,

              "InstanceGroupID": 1015025

            }

        ]

      },

      "Applications": [

        {

          "Guid": "6b61baf1-577b-4fbb-b5b3-a9eaa59418f6",

          "ShouldRestore": true

        }

      ],

      "NotificationOptions": {

        "NotifyJobCreator": true,

        "NotifyJobExecutor": true

      },

    "UiJobActionsLocked": false

    }

}
```

Request body parameters:

- ArchivePath - path of the ARM archive to be restored. This archive path must not be in use by another ARM job.

- JobPriority - priority of execution for the job. Possible options include "Low", "Medium", and "High".

- ScheduledStartTime - scheduled time when the job will be run.

- ExistingTargetDatabase - target database in case the archive does not a have database backup bak file (also known as bakless archive).

- DestinationOptions

- DatabaseServerID - artifact ID of the target database server to restore the workspace to.

- ResourcePoolID - artifact ID of the target resource pool to restore the workspace to.

- MatterID - artifact ID of the target matter to restore the workspace to.

- CacheLocationID - artifact ID of the target cache location to restore the workspace to.

- FileRepositoryID - artifact ID of the target file repository to restore the workspace to.

- MigratorsDestinationOptions

- StructuredAnalyticsServerID - artifact ID of the structured analytics server (in case archive contains structured analytics data) to restore the workspace to.

- ConceptualAnalyticsServerID - artifact ID of the conceptual analytics server (in case archive contains conceptual analytics data) to restore the workspace to.

- DtSearchLocationID - artifact ID of the dtSearch location (in case archive contains dtSearch indexes) to restore the workspace to.

- AdvancedFileOptions

- ReferenceFilesAsArchiveLinks - indicates whether files should remain in the archive directory and should be referenced from the workspace database (File table) as opposed to copying to workspace repository (default=false).

- UpdateRepositoryFilePaths - indicates whether repository files' locations should be updated to reflect their new location (default=true).

- UpdateLinkedFilePaths - indicates whether non-repository (linked) files' locations should be updated to reflect their new location (default=true).

- UserMapping

- AutoMapUsers - indicates if archive users should be auto mapped by email address.

- UserMappings - array of explicit user mappings from the archive to Relativity instance.

- GroupMapping

- AutoMapGroups - indicates if archive groups should be auto mapped by name.

- GroupMappings - array of explicit group mappings from the archive to Relativity instance.

- Applications - array of non-required/3rd party applications that should be installed to workspace. Required Relativity applications are automatically upgraded during Workspace upgrade stage and are not needed here.

- NotificationOptions

- NotifyJobCreator - indicates if email notifications will be sent to the job creator.

- NotifyJobExecutor - indicates if email notifications will be sent to the job executor.

- UiJobActionsLocked - indicates if job actions normally available on UI should be visible for the user. This behavior can be override by adding boolean instance setting OverrideUiJobActionsLock.

If job creation is successful, response will be the artifact ID of the newly created job. If the job creation could not be completed, the response will contain validation errors with more detailed information.

## Restore Read

Use this endpoint to read Restore jobs.

To read Restore jobs, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/restore-jobs/<jobID>
```

Request body is empty, the job ID is passed in via the URL.

Copy

Sample JSON response

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
{

    "JobID": 23110,

    "JobName": "Restore 1018486_WorkspaceName_1018486__20190927094548",

    "JobExecutionID": 23283,

    "JobExecutionGuid": "bc9b60c8-d1b2-4bf1-b62a-5bdc9969b5c3",

    "ArchivePath": "\\\\server\\fileshare\\armarchive\\1018486_WorkspaceName_1018486__20190927094548",

    "ScheduledStartTime": "2020-04-08T14:00:00",

    "SourceWorkspace": "WorkspaceName",

    "DestinationWorkspaceID": 1014823,

    "ExistingTargetDatabase": null,

    "JobDetails": {

        "CreatedOn": "2020-05-11T18:31:51.02",

        "ModifiedTime": "2020-05-11T18:31:51.113",

        "SubmittedBy": "Admin, Relativity",

        "State": "NotStarted",

        "Priority": "Low",

        "ActionsHistory": [

            {

                "Date": "2020-05-11T18:31:51.033",

                "Type": "Created",

                "UserName": "Admin, Relativity"

            }

        ]

    },

    "DestinationOptions": {

        "ResourcePoolID": 1015040,

        "DatabaseServerID": 1015096,

        "MatterID": 1000002,

        "CacheLocationID": 1015534,

        "FileRepositoryID": 1014887

    },

    "MigratorsDestinationOptions": {

        "StructuredAnalyticsServerID": 2074938,

        "ConceptualAnalyticsServerID": 2074938,

        "DtSearchLocationID": null

    },

    "AdvancedFileOptions": {

        "ReferenceFilesAsArchiveLinks": false,

        "UpdateRepositoryFilePaths": true,

        "UpdateLinkedFilePaths": true

    },

    "UserMappings": [],

    "GroupMappings": [

        {

            "ArchiveGroupID": 1036399,

            "InstanceGroupID": -1

        }

    ],

    "Applications": [

        {

            "Name": "Single File Upload",

            "Guid": "1738ceb6-9546-44a7-8b9b-e64c88e47320",

            "ShouldRestore": true

        }

    ],

    "NotificationOptions": {

        "NotifyJobCreator": false,

        "NotifyJobExecutor": false

    },

    "UiJobActionsLocked": false

}
```

Response body parameters:

- JobID - ID of the created Restore job. This is a generated field.

- JobName - name of the Restore job created. This is a generated field.

- JobExecutionID - ID of the execution of the created Restore Job. This is a generated field.

- JobExecutionGuid - execution GUID of the created Restore Job. This is a generated field.

- ArchivePath - path to the ARM archive that will be restored.

- ScheduledStartTime - scheduled time when the job will be run.

- SourceWorkspace - name of the source workspace.

- DestinationWorkspaceID - artifact ID of the restored workspace. This is a generated field and will be null if the job has not started and created the new workspace.

- ExistingTargetDatabase - target database in case the archive does not a have database backup bak file (also known as bakless archive).

- JobDetails

- CreatedOn - date and time of job creation. This is a generated field.

- ModifiedTime - date and time of most recent job modification. This is a generated field.

- SubmittedBy - the user responsible for the submission of the job. This is a generated field.

- State - current job state. This is a read-only field.

- Priority - priority of execution for the job.

- ActionsHistory - list of job actions with the following details: date, type and user name. This is a read-only field.

- DestinationOptions

- DatabaseServerID - artifact ID of the target database server to restore the workspace to.

- ResourcePoolID - artifact ID of the target resource pool to restore the workspace to.

- MatterID - artifact ID of the target matter to restore the workspace to.

- CacheLocationID - artifact ID of the target cache location to restore the workspace to.

- FileRepositoryID - artifact ID of the target file repository to restore the workspace to.

- MigratorsDestinationOptions

- StructuredAnalyticsServerID - artifact ID of the structured analytics server (in case archive contains structured analytics data) to restore the workspace to.

- ConceptualAnalyticsServerID - artifact ID of the conceptual analytics server (in case archive contains conceptual analytics data) to restore the workspace to.

- DtSearchLocationID - artifact ID of the dtSearch location (in case archive contains dtSearch indexes) to restore the workspace to.

- AdvancedFileOptions

- ReferenceFilesAsArchiveLinks - indicates whether files should remain in the archive directory and should be referenced from the workspace database (File table) as opposed to copying to workspace repository (default=false).

- UpdateRepositoryFilePaths - indicates whether repository files' locations should be updated to reflect their new location (default=true).

- UpdateLinkedFilePaths - indicates whether non-repository (linked) files' locations should be updated to reflect their new location (default=true).

- UserMapping

- AutoMapUsers - indicates if archive users should be auto mapped by email address.

- UserMappings - array of explicit user mappings from the archive to Relativity instance.

- GroupMapping

- AutoMapGroups - indicates if archive groups should be auto mapped by name.

- GroupMappings - array of explicit group mappings from the archive to Relativity instance.

- Applications - array of non-required/3rd party applications that should be installed to workspace.

- NotificationOptions

- NotifyJobCreator - indicates if email notifications will be sent to the job creator.

- NotifyJobExecutor - indicates if email notifications will be sent to the job executor.

- UiJobActionsLocked - indicates if job actions normally available on UI should be visible for the user. This behavior can be override by adding boolean instance setting OverrideUiJobActionsLock.

## Restore Update

Use this endpoint to update Restore jobs.

To update Restore jobs, send a PUT request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/restore-jobs/<jobID>
```

The request body is the same as Restore Create , and the job ID is passed in via the URL.

The response returns a status code of 200 when the service successfully updates a restore job. There is no response body.

## Restore Delete

Use this endpoint to delete Restore jobs.

To delete Restore jobs, send a DELETE request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/restore-jobs/<jobID>
```

Request body is empty, the job ID is passed in via the URL.

The response returns a status code of 200 when the service successfully deletes a restore job. There is no response body.

## Database Restore Create

Use this endpoint to create Database Restore jobs.

To create Database Restore jobs, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/V1/database-restore-jobs/
```

Copy

Sample JSON request

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
{

    "request":  {

      "SourceDatabase": "EDDS1014823",

      "JobPriority": "Medium",

      "ScheduledStartTime": null,

      "DestinationOptions": {

        "DatabaseServerID": "1015096",

        "ResourcePoolID": "1015040",

        "MatterID": "1000002",

        "CacheLocationID": "1015534",

        "FileRepositoryID": "1014887"

      },

      "UserMapping": {

        "AutoMapUsers": "true",

        "UserMappings": [

          {

            "ArchiveUserID": "1014868",

            "InstanceUserID": "2156304"

          }

        ]

      },

      "GroupMapping": {

        "AutoMapGroups": "false",

        "GroupMappings": [

          {

            "ArchiveGroupID": "1038349",

            "InstanceGroupID": "1015025"

          }

        ]

      },

      "NotificationOptions": {

        "NotifyJobCreator": "true",

        "NotifyJobExecutor": "true"

      },

    "UiJobActionsLocked": false

    }

}
```

Request body parameters:

- SourceDatabase - name of the database which will be restored. This source database must be available and must not be in use by another ARM job.

- JobPriority - priority of execution for the job. Possible options include "Low", "Medium", and "High".

- ScheduledStartTime - scheduled time when the job will be run.

- DestinationOptions

- DatabaseServerID - artifact ID of the target database server to restore the workspace to.

- ResourcePoolID - artifact ID of the target resource pool to restore the workspace to.

- MatterID - artifact ID of the target matter to restore the workspace to.

- CacheLocationID - artifact ID of the target cache location to restore the workspace to.

- FileRepositoryID - artifact ID of the target file repository to restore the workspace to.

- UserMapping

- AutoMapUsers - indicates if archive users should be auto mapped by email address.

- UserMappings - array of explicit user mappings from the archive to Relativity instance.

- GroupMapping

- AutoMapGroups - indicates if archive groups should be auto mapped by name.

- GroupMappings - array of explicit group mappings from the archive to Relativity instance.

- NotificationOptions

- NotifyJobCreator - indicates if email notifications will be sent to the job creator.

- NotifyJobExecutor - indicates if email notifications will be sent to the job executor.

- UiJobActionsLocked - indicates if job actions normally available on UI should be visible for the user. This behavior can be override by adding boolean instance setting OverrideUiJobActionsLock.

If job creation is successful, response will be the artifact ID of the newly created job. If the job creation could not be completed, the response will contain validation errors with more detailed information.

## Database Restore Read

Use this endpoint to read Database Restore jobs.

To read Database Restore jobs, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/database-restore-jobs/<jobID>
```

Request body is empty, the job ID is passed in via the URL.

Copy

Sample JSON response

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
{

    "JobID": 23110,

    "JobName": "Restore EDDS1049998",

    "JobExecutionID": 23283,

    "JobExecutionGuid": "bc9b60c8-d1b2-4bf1-b62a-5bdc9969b5c3",

    "ScheduledStartTime": "2099-03-24T15:03:23.673",

    "DestinationWorkspaceID": 1014823,

    "JobDetails": {

        "CreatedOn": "2020-05-11T18:31:51.02",

        "ModifiedTime": "2020-05-11T18:31:51.113",

        "SubmittedBy": "Admin, Relativity",

        "State": "NotStarted",

        "Priority": "Low",

        "ActionsHistory": [

            {

                "Date": "2020-05-11T18:31:51.033",

                "Type": "Created",

                "UserName": "Admin, Relativity"

            }

        ]

    },

    "DestinationOptions": {

        "ResourcePoolID": 1015040,

        "DatabaseServerID": 1015096,

        "MatterID": 1000002,

        "CacheLocationID": 1015534,

        "FileRepositoryID": 1014887

    },

    "UserMappings": [

        {

              "ArchiveUserID": 1016933,

              "InstanceUserID": 1019365

        }

    ],

    "GroupMappings": [

        {

            "ArchiveGroupID": 1036399,

            "InstanceGroupID": -1

        }

    ],

    "NotificationOptions": {

        "NotifyJobCreator": false,

        "NotifyJobExecutor": false

    },

    "UiJobActionsLocked": false

}
```

Response body parameters:

- JobID - ID of the created Database Restore job. This is a generated field.

- JobName - name of the Database Restore job created. This is a generated field.

- JobExecutionID - ID of the execution of the created Database Restore Job. This is a generated field.

- JobExecutionGuid - execution GUID of the created Database Restore Job. This is a generated field.

- ScheduledStartTime - scheduled time when this job will be run.

- DestinationWorkspaceID - artifact ID of the restored workspace. This is a generated field and will be null if the job has not started and created the new workspace.

- JobDetails

- CreatedOn - date and time of job creation. This is a generated field.

- ModifiedTime - date and time of most recent job modification. This is a generated field.

- SubmittedBy - the user responsible for the submission of the job. This is a generated field.

- State - current job state. This is a read-only field.

- Priority - priority of execution for the job.

- ActionsHistory - list of job actions with the following details: date, type and user name. This is a read-only field.

- DestinationOptions

- DatabaseServerID - artifact ID of the target database server to restore the workspace to.

- ResourcePoolID - artifact ID of the target resource pool to restore the workspace to.

- MatterID - artifact ID of the target matter to restore the workspace to.

- CacheLocationID - artifact ID of the target cache location to restore the workspace to.

- FileRepositoryID - artifact ID of the target file repository to restore the workspace to.

- UserMapping

- AutoMapUsers - indicates if archive users should be auto mapped by email address.

- UserMappings - array of explicit user mappings from the archive to Relativity instance.

-

GroupMapping

- AutoMapGroups - indicates if archive groups should be auto mapped by name.

- GroupMappings - array of explicit group mappings from the archive to Relativity instance.

- NotificationOptions

- NotifyJobCreator - indicates if email notifications will be sent to the job creator.

- NotifyJobExecutor - indicates if email notifications will be sent to the job executor.

- UiJobActionsLocked - indicates if job actions normally available on UI should be visible for the user. This behavior can be override by adding boolean instance setting OverrideUiJobActionsLock.

## Database Restore Update

Use this endpoint to update Database Restore jobs.

To update Database Restore jobs, send a PUT request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/database-restore-jobs/<jobID>
```

The request body is the same as Database Restore Create , and the job ID is passed in via the URL.

The response returns a status code of 200 when the service successfully updates a database restore job. There is no response body.

## Database Restore Delete

Use this endpoint to delete Database Restore jobs.

To create Database Restore jobs, send a DELETE request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/database-restore-jobs/<jobID>
```

Request body is empty, the job ID is passed in via the URL.

The response returns a status code of 200 when the service successfully deletes a database restore job. There is no response body.

## Move Create

Use this endpoint to create Move jobs.

To create Move jobs, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/move-jobs
```

Copy

Sample JSON request

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
{

    "request": {

      "SourceWorkspaceID": 1014823,

      "JobPriority": "High",

      "ScheduledStartTime": "2020-04-08T14:00:00",

      "FileOptions": {

          "LinkToExistingDocuments": true,

          "MissingFileBehavior": "SkipFile",

          "LinkedFileBehavior": "LeaveInPlace"

      },

      "DatabaseOptions" {

          "IncludeDatabaseBackup": false,

          "CustomDatabasePath": "EDDS1014444"

      },

      "DestinationOptions" {

          "ResourcePoolID": 1015040,

          "DatabaseServerID": 1015096,

        "CacheLocationID": 1015534,

        "FileRepositoryID": 1014887

      },

      "NotificationOptions": {

          "NotifyJobCreator": true,

          "NotifyJobExecutor": true

      }

    "UiJobActionsLocked": false

    }

}
```

Request body parameters:

- SourceWorkspaceID - the artifact ID of the workspace to move for the move job. This Workspace must not be in the process of upgrading or currently in use by another ARM job.

- JobPriority - priority of execution for the job. Possible options include "Low", "Medium", and "High".

- ScheduledStartTime - scheduled time when the job will be run.

- FileOptions

- LinkToExistingDocuments - indicates whether repository files should be moved to new location or stay in their current one.

- MissingFileBehavior - indicates whether to skip ("SkipFile") or stop ("StopJob") when missing files are detected during the archiving process. If there is potential for any files to not be found while the job is running, skipping them will result in compiling a downloadable list of the files that were missing and allow the job to complete without error. Setting this to stop will immediately stop on the first missing file and cannot resume until the file is placed in the expected location.

- LinkedFileBehavior - indicates whether linked files should be moved/copied to new location or stay in their current one.

- DatabaseOptions

- IncludeDatabaseBackup - indicates whether the workspace database is backed up and used for the new workspace. Defaults to true.

- CustomDatabasePath - the path to a custom database to apply to the new workspace. Required if IncludeDatabaseBackup is false.

- DestinationOptions

- DatabaseServerID - artifact ID of the target database server to move the workspace to.

- ResourcePoolID - artifact ID of the target resource pool to move the workspace to.

- CacheLocationID - artifact ID of the target cache location to move the workspace to.

- FileRepositoryID - artifact ID of the target file repository to move the workspace to.

- NotificationOptions

- NotifyJobCreator - indicates if email notifications will be sent to the job creator.

- NotifyJobExecutor - indicates if email notifications will be sent to the job executor.

- UiJobActionsLocked - indicates if job actions normally available on UI should be visible for the user. This behavior can be override by adding boolean instance setting OverrideUiJobActionsLock.

If job creation is successful, response will be the artifact ID of the newly created job. If the job creation could not be completed, the response will contain validation errors with more detailed information.

## Move Read

Use this endpoint to read Move jobs.

To read Move jobs, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/move-jobs/<jobID>
```

Request body is empty, the job ID is passed in via the URL.

Copy

Sample JSON response

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
{

    "JobID": 3026,

    "JobName": "Archive New Case Template (1014823) Workspace",

    "JobExecutionID": 3026,

    "JobExecutionGuid": "895ef98e-6c8b-4573-867a-d11f0b39bd54",

    "ScheduledStartTime": "2020-04-08T14:00:00",

    "JobDetails": {

        "CreatedOn": "2020-03-20T10:30:44.137",

        "ModifiedTime": "2020-03-20T10:30:44.2",

        "SubmittedBy": "Admin, Relativity",

        "State": "Complete",

        "Priority": "Low",

        "ActionsHistory": [

            {

                "Date": "2020-03-20T10:30:44.17",

                "Type": "Created",

                "UserName": "Admin, Relativity"

            },

            {

                "Date": "2020-03-20T10:30:47.607",

                "Type": "Started",

                "UserName": "Admin, Relativity"

            },

            {

                "Date": "2020-03-20T10:31:06.007",

                "Type": "Completed",

                "UserName": "Agent"

            }

        ]

    },

    "SourceOptions" {

        "WorkspaceID": 1014823,

          "ResourcePoolID": 1015040,

          "DatabaseServerID": 1015096,

        "CacheLocationID": 1015534,

        "FileRepositoryID": 1014887

    },

    "DestinationOptions" {

          "ResourcePoolID": 1015040,

          "DatabaseServerID": 1015096,

        "CacheLocationID": 1015534,

        "FileRepositoryID": 1014887

    },

    "FileOptions": {

          "LinkToExistingDocuments": true,

          "MissingFileBehavior": "SkipFile",

          "LinkedFileBehavior": "LeaveInPlace"

    },

    "DatabaseOptions" {

          "IncludeDatabaseBackup": false,

          "CustomDatabasePath": "EDDS1014444"

    },

    "NotificationOptions": {

        "NotifyJobCreator": false,

        "NotifyJobExecutor": false

    },

    "UiJobActionsLocked": false

}
```

Response body parameters:

- JobID - ID of the created Move job. This is a generated field.

- JobName - name of the Move job created. This is a generated field.

- JobExecutionID - ID of the execution of the created Move Job. This is a generated field.

- JobExecutionGuid - execution GUID of the created Move Job. This is a generated field.

- ScheduledStartTime - scheduled time when the job will be run.

- JobDetails

- CreatedOn - date and time of job creation. This is a generated field.

- ModifiedTime - date and time of most recent job modification. This is a generated field.

- SubmittedBy - the user responsible for the submission of the job. This is a generated field.

- State - current job state. This is a read-only field.

- Priority - priority of execution for the job.

- ActionsHistory - list of job actions with the following details: date, type and user name. This is a read-only field.

- SourceOptions

- WorkspaceID - artifact ID of the workspace that will be moved.

- DatabaseServerID - artifact ID of the database server for the moved workspace.

- ResourcePoolID - artifact ID of the resource pool for the moved workspace.

- CacheLocationID - artifact ID of the cache location for the moved workspace.

- FileRepositoryID - artifact ID of the file repository for the moved workspace.

- DestinationOptions

- DatabaseServerID - artifact ID of the target database server to move the workspace to.

- ResourcePoolID - artifact ID of the target resource pool to move the workspace to.

- CacheLocationID - artifact ID of the target cache location to move the workspace to.

- FileRepositoryID - artifact ID of the target file repository to move the workspace to.

- FileOptions

- LinkToExistingDocuments - indicates whether repository files should be moved to new location or stay in their current one.

- MissingFileBehavior - indicates whether to skip ("SkipFile") or stop ("StopJob") when missing files are detected during the archiving process. If there is potential for any files to not be found while the job is running, skipping them will result in compiling a downloadable list of the files that were missing and allow the job to complete without error. Setting this to stop will immediately stop on the first missing file and cannot resume until the file is placed in the expected location.

- LinkedFileBehavior - indicates whether linked files should be moved/copied to new location or stay in their current one.

- DatabaseOptions

- IncludeDatabaseBackup - indicates whether the workspace database is backed up and used for the new workspace. Defaults to true.

- CustomDatabasePath - the path to a custom database to apply to the new workspace. Required if IncludeDatabaseBackup is false.

- NotificationOptions

- NotifyJobCreator - indicates if email notifications will be sent to the job creator.

- NotifyJobExecutor - indicates if email notifications will be sent to the job executor.

- UiJobActionsLocked - indicates if job actions normally available on UI should be visible for the user. This behavior can be override by adding boolean instance setting OverrideUiJobActionsLock.

## Move Update

Use this endpoint to update Move jobs.

To update Move jobs, send a PUT request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/move-jobs/<jobID>
```

The request body is the same as Move Create , and the job ID is passed in via the URL.

The response returns a status code of 200 when the service successfully updates a move job. There is no response body.

## Move Delete

Use this endpoint to delete Move jobs.

To delete Move jobs, send a DELETE request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/move-jobs/<jobID>
```

Request body is empty, the job ID is passed in via the URL.

The response returns a status code of 200 when the service successfully deletes a move job. There is no response body.

## Job Run

Use this endpoint to run ARM jobs.

To run ARM jobs, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/jobs/<jobID>/run
```

Request body is empty, the job ID is passed in via the URL.

The response returns a status code of 200 when the service successfully executes an ARM job. There is no response body.

## Job Cancel

Use this endpoint to cancel ARM jobs.

To cancel ARM jobs, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/jobs/<jobID>/cancel
```

Request body is empty, the job ID is passed in via the URL.

The response returns a status code of 200 when the service successfully cancels an ARM job. There is no response body.

## Job Pause

Use this endpoint to pause ARM jobs.

To pause ARM jobs, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/jobs/<jobID>/pause
```

Request body is empty, the job ID is passed in via the URL.

The response returns a status code of 200 when the service successfully pauses an ARM job. There is no response body.

## Terminate Job

Use this endpoint to terminate an ARM job.

To terminate ARM jobs, send a DELETE request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/jobs/<jobID>/terminate
```

Request body is empty, the job ID is passed in via the URL.

The response returns a status code of 200 when the service successfully terminates an ARM job. There is no response body.

## Job Status

Use this endpoint to read the execution status of an ARM job.

To read the execution status of an ARM job, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/jobs/<jobID>/status
```

Request body is empty, the job ID is passed in via the URL.

Copy

Sample JSON response

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
{

    "JobType": "Archive",

    "JobState": "Errored",

    "CurrentJobStage": {

        "Name": "Prepare Archive",

        "Order": 1,

        "NumberOfSucceededTasks": 2,

        "NumberOfFailedTasks": 4,

        "TotalNumberOfTasks": 7,

        "TimeStarted": "2020-03-27T13:18:14.96",

        "TimeElapsed": "01:05:00.5784770",

        "PercentComplete": 80

    },

    "TotalNumberOfStages": 9,

    "TimeStarted": "2020-03-19T13:25:48.147",

    "TimeCompleted": "2020-03-19T14:26:08.010",

    "TimeElapsed": "01:10:29.8630000"

}
```

Response body parameters:

- JobType - type of the job. Possible options include "Archive", "Restore", "DatabaseRestore", and "Move".

- JobState - state of the job. Possible options include: "ExecutionRequested", "Pending", "Processing", "ProcessingWithErrors", "Errored", "Complete", "CancellationRequested", "CancellationPending", "CancellationProcessing", "CancellationProcessingWithErrors", "CancellationErrored", "CancellationComplete", "Paused", "NotStarted", "PauseRequested", "RecoveryRequested", "CancellationRecoveryRequested", "Scheduled", and "CleaningUp".

- CurrentJobStage - detailed information of current job's stage.

- Name - stage name.

- Order - order of the stage. The numbering starts with 0.

- NumberOfSucceededTasks - number of succeeded tasks .

- NumberOfFailedTasks - number of failed tasks.

- TotalNumberOfTasks - number of tasks.

- TimeStarted - stage start time.

- TimeElapsed - stage elapsed time.

- PercentComplete - percentage of successfully completed or failed tasks.

- TotalNumberOfStages - number of stages in the job.

- TimeStarted - job start time.

- TimeCompleted - job completion time.

- TimeElapsed - job elapsed time.

## Job Logs

Use this endpoint to retrieve ARM job logs.

To retrieve ARM job logs, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/jobs/<jobID>/logs
```

Request body is empty, the job ID is passed in via the URL.

Copy

Kepler stream

```text
1
2
3
UtcTime, Severity, LogRowCorrelationId, JobExecutionId, Status, Step, AgentMachineName, HangfireTaskId, Method, Exception

6/3/2020 11:59:21 AM, Information, d90eca4a-d000-435a-9d00-5910f5f84342, 14, CreateAsync, 1, A00SDPDARMAP001, -1, CreateAsync,

6/3/2020 11:59:38 AM, Information, 1a209f79-c507-42b2-96c5-b3942b92463a, 14, Processing stage progression for ARM job 14, 1, A00SDPDARMAP001, 28546, IStageProgressionService.ProcessStageProgression,
```

## Task Retry

Use this endpoint to retry a failed task (e.g. Processing Migrator).

To retry a failed task, send a POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/tasks/<taskId>/retry
```

Request body is empty, the task ID is passed in via the URL.

The response returns a status code of 200 when the service successfully retries a task. There is no response body.

## Job Statistic

Use this endpoint to read statistic of an ARM job.

To read statistic of an ARM job, send a GET request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-arm/v1/jobs/<jobExecutionId>/statistics
```

Request body is empty, the job ID is passed in via the URL.

For the restore job Non Document Repository Files won't be shown in the response.

If the restore job was created with option Reference files as archive links , Document Repository Files and Document Linked Files won't be present in the response because the job didn't copy them. Response for the restore job only contains statistics for items that were present in the source. For example, archives created without Processing Files , statistics for restore job won't have Processing Files in the response.

Response body parameters:

- SourceName - name of the source of items.

- DestinationName - name of the destination for items.

- JobTypeName - name of the job type.

- ArchiveItemsStatistics - statistics of each item type in this job.

- ItemTypeName - the name of item type.

- SourceItemCount - number of source items. This value can be null.

- DestinationItemCount - number of destination items.

- MissingItemsCount - number of missing items. When SoureItemCount is null this value also be null.

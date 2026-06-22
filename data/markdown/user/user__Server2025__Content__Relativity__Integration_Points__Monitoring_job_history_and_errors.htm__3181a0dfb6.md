---
title: "Monitoring job history and errors"
url: https://help.relativity.com/Server2025/Content/Relativity/Integration_Points/Monitoring_job_history_and_errors.htm
collection: user
fetched_at: 2026-06-22T06:09:30+00:00
sha256: b13b62af6c35d2e1c2dfca876a0dd4205abd6baed23a91233122e44428c7e534
---

Monitoring job history and errors

# Monitoring job history and errors

After you create an integration point and initiate the import process, you can monitor the job status on the Job History tab and resolve errors on the Job History Errors tab.

## Job History

This tab lists an entry for each integration point job, and also provides you with the ability to view additional details for a specific job.

The Job History tab lists the following information that you can use to monitor the status of an integration point job:

- Start Time (UTC) - the date and time that a job started running in Coordinated Universal Time (UTC).

- Artifact ID - the artifact ID of the workspace.

- Name - the name for a specific job run by the integration point.

- Integration Point - the name of the integration point used to run the job.

- Job Status - the current status of an integration point job. The following job statuses are available:

- [blank] - the job hasn't started or wasn't run.

- Pending - the job has been submitted but an agent hasn't picked it up, so the import process hasn't started.

- Suspending - the system is performing the application update. The job prepares for being suspended, completing the current task.

- Suspended - the system is performing the application update. The job has been suspended, and waits for the Integration Points agent to pick it up.

- Processing - the job is currently running.

- Error - Job Failed - a job-level error occurred and the import wasn't completed. The integration point may have been able to import some of the records before the error occurred.

- Completed with Errors - the import job completed but at least one item-level error occurred. If you set the Log Errors field to Yes for the integration point, you can view the item-level errors in the section called Job History Errors on the Job Details layout. See Viewing job history details .

When transferring custodians and associating them to managers, errors can occur. If transferring custodians and the manager isn't associated with a manager, the custodian transfer is completed successfully. It will show up as Completed with Errors even though the Items Transferred field and Total Items field will match, while the Items with Errors field states zero errors. This is because the custodian has been imported correctly, but the manager wasn't associated correctly.

- Completed - the import job completed without any item-level errors.

- Destination Workspace - the workspace specified as the destination for the transferred files.

- Items Transferred - the number of records successfully transferred when the job ran.

- Total Items - the total number of items originally designated to be transferred, including those that ended up having errors.

- Items with Errors - the number of records that the integration point failed to import due to item-level errors.

### Viewing job history details

To view additional history information, click the name of a specific job listed on the Job History tab. The Job Details layout displays basic job information, import statistics, and a detailed list of errors.

The Job History Error section always logs job-level errors. If you set the Log Errors field to Yes, then it also logs item-level errors. For more information on setting the Log Errors field, see Importing data through Integration Points .

The Job Details layout includes many of the same fields displayed on the Job History tab. The following list includes the additional fields displayed in this layout:

- End Time (UTC) - the date and time that a job completed in UTC.

- Source Unique ID - the unique identifier for the record in the source that caused an error.

- Error - a brief description of the error that occurred.

- Timestamp - the date and time that a job error occurred in UTC.

- Error Type - indicates whether the error occurred at the job or item level.

## Job History Errors

In the Job History Errors tab, you can use the condition lists at the top of the view to find errors based on any error-related metadata fields, such as Artifact ID, Error, Error Status, Error Type, JobHistory, Name, Source Unique ID, Stack Trace, System Created By, System Created On, System Last Modified On, and Timestamp (UTC).

Once you specify your conditions, you can search for the targeted errors by clicking Search on the right side of the condition lists.

You can then open any of the individuals errors returned in the list by clicking the Name value.

The Job History Error Layout provides the following fields:

- Name - the system-generated name of the error.

- Source Unique ID - the identifier of the item in which the error occurred.

- Job History - the name of the integration point containing the file in which the error occurred.

- Error - the error message.

- Error Status - the current state of the error. You'll see any of the following values for the status field:

- New - the error is new and no action has been taken on it yet.

- Expired - the state assigned to an item level error in either of the following scenarios:

- You received an item-level error on a job, you didn't retry the error, and the job ran on a schedule, meaning the Enable Scheduler field is set to Yes on the integration point.

- You received an item-level or a job-level error, you didn't retry the error, and you click Run Now on the integration point, or it is a scheduled job.

- In Progress - the error is currently in the process of being retried.

- Retried - the item level error in a job has been retried, meaning you clicked Retry Errors on the integration point and the retry job is complete.

- Error Type - an indicator of whether the error is item or job-level.

- Full Error - the error message with details, including a stack trace of the error, when available.

- System Created On - the date and time at which the error was created by the agent during the integration point job.

- System Created By - the agent that created the error during the integration point job.

- System Last Modified By - the agent that last updated the status value of the error.

With the information provided in the Job History Errors Layout, you can identify those files on which errors occurred. You can then access those files to manually address the causes of those errors. From there, you can return to the integration points console and retry the errors.

### Item-level versus job-level errors

Note the following differences in the way Relativity handles item-level and job-level errors.

Relativity handles a mix of item-level and job-level errors in the following way:

- When you click Run Now on an integration point that contains item and job-level errors, the entire job is re-run and all errors are marked as Expired.

- When you click Retry Errors on an integration point that contains item and job-level errors, the entire job is rerun and Relativity assigns a value of Expired to the item-level errors while job-level errors are marked as In Progress and then Retried.

Relativity handles item-level errors in the following way:

- When you click Run Now, the entire job is re-run, and Relativity assigns a value of Expired to the item-level errors.

- When you click Retry Errors, Relativity assigns a value of Retried to the item-level errors and starts a retry job containing only those error documents.

Relativity handles job-level errors in the following way:

- It registers only one job-level error for the integration point.

- When you click Run Now, the entire job is re-run and Relativity assigns a value of Expired to the job-level error.

- The Retry Errors and Run Now buttons are both available.

- The Retry Error button re-runs the whole job, but the job-level error is marked as In progress and then retried.

- The Run Now button re-runs the whole job, but the job-level error is marked as Expired.

Scheduled job is not inserted and an error is thrown that shows up in the errors tab in Admin mode that a scheduled job did not run for this integration because the job was already running.

When you click Retry Errors, the retry job is automatically set to Append/Overlay mode.

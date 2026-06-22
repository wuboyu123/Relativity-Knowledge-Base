---
title: "PDF Queue"
url: https://help.relativity.com/Server2025/Content/Relativity/Mass_operations/PDF_Queue.htm
collection: user
fetched_at: 2026-06-22T06:16:01+00:00
sha256: cb39d4d039d6e054b84f84d8839467f512a1ca4e90e12a85637d99671b6db1a3
---

PDF Queue

# PDF Queue

PDF Queue is a sub-tab of Queue Management. From this screen, you can monitor all PDF jobs across an instance of Relativity that are not yet complete.

## PDF Queue columns

- Workspace ID —the ID of the workspace that contains the products set used for the job.

- Job ID —the unique ID assigned the job.

- Job Type —the type of job submitted. For example, Single, Mass, or Delete.

- Input File Type —the type of file submitted. For example, Native, Image, or Production.

- Status —the current stage of the production job.

- Created - the system has created the PDF job but it has not yet been picked up by an agent.

- PickedUpByAgent - an agent has picked up the PDF job.

- QueueCreated - the backing queue in the system has captured all the documents within the PDF job that need to be worked on.

- InProgress - an agent is currently working on the PDF job, specifically by converting documents to PDFs.

- JobError - the job has stopped due to an error.

- FinalizingInitiated - an agent has converted all the documents within the PDF job; the final step of zipping all the PDFs has been queued up.

- FinalizingInProgress - finalization of the PDF job is in progress, in that an agent is now zipping all the PDFs.

- Cancelled - a user has cancelled the PDF job.

- Staged Documents —the number of staged documents.

- Submitted Documents —the number of documents that were originally submitted.

- In Progress Documents —the number of documents in progress.

- Errored Documents —the number of documents that errored during the process.

- Completed Documents —the number of completed documents during the process.

- Total Documents —the total number of documents processed.

- Skipped Documents —the number of documents skipped.

- User Artifact ID —the unique ID of the user starting the job.

- Submitted Date —the date and time when a PDF job was run.

## Cancel a PDF job

To cancel a PDF job:

- Select the job(s).

- Click the Cancel PDF Job button.

- Click Yes, Cancel PDF Job on the confirmation modal.

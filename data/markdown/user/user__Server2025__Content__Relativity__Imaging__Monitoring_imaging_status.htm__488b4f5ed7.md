---
title: "Monitoring imaging status"
url: https://help.relativity.com/Server2025/Content/Relativity/Imaging/Monitoring_imaging_status.htm
collection: user
fetched_at: 2026-06-22T06:14:12+00:00
sha256: 1b3f10a4fe04dc88a6577f28460e7a38d58d5422e90478df4128d50a94cc8ad0
---

Monitoring imaging status

# Monitoring imaging status

In the imaging status section, you can monitor the progress of the imaging job by referring to the Status field after clicking the Refresh Page link on the console. The Imaging Set status information is also available in the default Imaging Set view.

The Imaging Status section provides the following fields:

- Start time - displays the start time and date of the imaging set. Only available when the imaging set is in Submitting or Imaging states.

- Status - provides any of the following values, depending on the imaging job in the imaging status section and in the default Imaging Set view:

Status Value What Happened What It Means

Staging User clicked Image Documents. Job is in queue table and the Imaging Set is awaiting execution.

Submitting The Imaging Request Agent is submitting documents to the worker manager queue. The Imaging Request is creating the imaging job and doing necessary work to submit documents.

Imaging All documents have been submitted to worker manager queue. Invariant workers are creating images of the documents.

Completed Job has completed. All documents imaged successfully.

Completed with errors Job has completed with imaging errors. One or more documents encountered an error during imaging job.

Error - Job Failed Job manager encountered an exception. Manager terminated imaging job due to exception.

Stopping User clicked Stop. Worker manager queue is stopping worker jobs, and Documents are being updated to Has Images = No

Stopped by user Job has stopped. All worker agents have stopped imaging documents; job manager has stopped the job.

- Image completion - displays the number of remaining documents, successfully imaged documents, documents with errors, and skipped documents.

- Completion Rate - displays the rate at which documents are submitted. For example, X documents submitted per hour or X documents imaged per hour.

- Last Run Error - displays the most recently run job that completed with errors.

Note the following:

- During the conversion process, Relativity skips documents that already have images, documents with restricted native types, and documents with images in a pending state (that's with the Has Images field set to Yes). It includes these items in the skipped documents count.

- If you need to delete an Imaging Set, you should only delete those with the following statuses:

- Stopped by User

- Error - Job Failed

- Completed with Errors

- Completed

-

- In Relativity 9.7.229.5 , the Status field was added to the default Imaging Set view.

---
title: "Managing processing jobs in the queue"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Managing_processing_jobs_in_the_queue.htm
collection: user
fetched_at: 2026-06-22T06:05:59+00:00
sha256: 8fdaf4ad376f9d09154d4e1c2ec2569a12146971f71e78c7e92b19b4da46ef96
---

Managing processing jobs in the queue

# Managing processing jobs in the queue

When you start a processing job, that job eventually goes to the Worker Manager Queue, which you can access through the Queue Management tab to view the status of your processing jobs and change the priorities of jobs that you know need to be completed before others in your environment.

Read if you're studying for the Processing Specialist exam The content on this site is based on the most recent monthly version of Relativity, which contains functionality that has been added since the release of the version on which Relativity's exams are based. As a result, some of the content on this site may differ significantly from questions you encounter in a practice quiz and on the exam itself. If you encounter any content on this site that contradicts your study materials, please refer to the What's New and/or the Release Notes for details on all new functionality.

Processing jobs get the same priority in the queue as native imaging jobs. TIFF-on-the-fly jobs, however, take precedence over both processing and native imaging.

The following columns appear on the Worker Manager Queue sub-tab:

- Workspace – the workspace in which the job was created. Click the name of a workspace to navigate to the main tab in that workspace.

- Set Name – the name of the processing set. Click a set name to navigate to the Processing Set Layout on the Processing Sets tab. From here you can cancel publishing or edit the processing set.

- Data Source - the data source containing the files you're processing. This appears as either the name you gave the source when you created it or as <Custodian Last Name>, <Custodian First Name> - < Artifact ID> if you left this field blank when creating the data source.

- Job Type – the type of job running. The worker manager server handles processing and imaging jobs.

When you click Filter Files on the processing set console, you're performing an intermediate step that is not considered an actual job type by Relativity. For that reason, filtering files is not displayed in the Worker Manager Queue.

- Status – the status of the set. If you're unable to view the status of any processing jobs in your environment, check to make sure the Server Manager agent is running.

- Documents Remaining – the number of documents that have yet to be inventoried, discovered, or published. The value in this field goes down incrementally as data extraction progresses on the processing set.

This column displays a value of -1 if you've clicked Inventory Files , Discover Files , or Publish Files but the job hasn't been picked up by a worker yet.

- Priority – the order in which jobs in the queue are processed. Lower priority numbers result in higher priority. This is determined by the value of the Order field on the data source. You can change the priority of a data source with the Change Priority button at the bottom of the view.

- Processing sets are processed in the queue on a first-come, first-served basis.

- Discovery, publishing, and imaging jobs are multi-threaded and can run in parallel, depending on the number of agents available.

- Where processing jobs have the same queue priority as imaging sets, the TIFF-on-the-fly job takes precedence over both processing and native imaging.

- Publishing jobs take priority over discovery jobs by default.

- Job Paused - the true/false value indicates whether the job was paused.

- Paused Time - the time at which the job was paused, based on local time.

- Failed Attempts - Failed Attempts - the number of times Relativity retries a processing job before flagging the job as paused. The ProcessingRetryCount field sets this number in Instance Settings. See ProcessingRetryCount .

- Submitted Date – the date and time the job was submitted, based on local time.

- Submitted By – the name of the user who submitted the job.

- Server Name – the name of the server performing the job. Click a server name to navigate to the Servers tab, where you can view and edit server information.

At the bottom of the screen, the following buttons in the drop-down appear:

- Cancel Imaging Job - cancel an imaging job. Only imaging jobs can be canceled from the Processing Queue sub-tab. If you have processing jobs selected and you click Cancel Imaging Job , the processing jobs are skipped.

- Resume Processing Job - resumes any paused processing jobs that have exceeded the failed retry attempt count. To resume a paused processing job, check the box next to the data source(s) that you need to resume and click Resume Processing Job . You can resume multiple jobs at the same time.

- Change Priority - change the priority of processing jobs in the queue.

- If you change the priority of a publish or republish job, you update the priorities of other publish and republish jobs from the same processing set. This ensures that deduplication is performed in the order designated on the set.

- When you change the priority of an inventory job, you update the priorities of other inventory jobs from the same processing set. This ensures that filtering files is available as expected for the processing set.

- While there is no option to pause discovery, changing the priority of a discovery job is a viable alternative.

If you click Discover or Publish on the Processing Set Layout, but then cancel the job before the agent picks it up, you can return to the set and re-execute the discovery or publish job.

---
title: "Imaging jobs in the Worker Manager queue"
url: https://help.relativity.com/Server2025/Content/Relativity/Imaging/Imaging_jobs_in_the_Worker_Manager_queue.htm
collection: user
fetched_at: 2026-06-22T06:14:18+00:00
sha256: aea3c148079f4fac20a6831fd8594ca27b0009149a525133f72f564d8e5b89d1
---

Imaging jobs in the Worker Manager queue Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Imaging jobs in the Worker Manager Queue

The Imaging Queue displays all current imaging jobs running in your environment. You can view the queue if you have system admin rights to see the tab. Select the Queue Management tab, and click Worker Manager Queue .

If you have processing installed, the Queue Management tab displays Worker Manager Queue instead of Imaging Queue as a subtab. You can use the Worker Manager Queue subtab to manage both imaging and processing jobs. For more information, see Managing the Processing Queue .

The Imaging Queue view displays the following fields:

- Workspace - indicates the workspace associated with the imaging set, Mass Image, or Image-on-the-fly job.

- Imaging Set Name - indicates the imaging set, Mass Image, or Image-on-the-fly operation used for the job. Mass Image and Image-on-the-fly jobs are named and auto-incremented when they are added to the queue.

- Set Name - indicates the imaging set, Mass Image, or Image-on-the-fly operation used for the job. Mass Image and Image-on-the-fly jobs are named and auto-incremented when they are added to the queue.

- Data Source - only populated for processing jobs.

- Job Type - indicates the job being run, will say "Imaging" for all types of Imaging jobs.

- Imaging Set Artifact ID - is unique identifier for the imaging set. The artifact ID will be set to blank for Image-on-the-fly or Mass Image jobs because these operations do not have imaging sets.

- Imaging Profile - lists the name of profile used to create the document images.

- Documents Remaining - lists the number of documents waiting to be imaged. the "Submitting" status indicates the number of Documents remaining for submission to the Worker Manager Server. The status "Imaging" indicates the number of Documents remaining for the Worker Manager Server to image.

- Status - displays the current stage of the imaging job. Image-on-the-fly or Mass Image operations have only Waiting and Processing statuses. When it is "Submitting," the Imaging Request Agent is submitting Documents to the Worker Manager Server. When it is "Imaging," all Documents have been received by the Worker Manager Server and are waiting to be imaged.

- Priority - indicates the order in which the imaging job will be run. Jobs initiated through image sets or Mass Image operations have default values of 100, while jobs initiated by Image-on-the-fly have default values of 1 (which means they will be worked on before mass image operations).

- Submitted Date - indicates the date and time when an imaging job was submitted, or an attempt was made to resolve errors in a job through the Imaging Set Console.

- Submitted By - lists the name of the user who initiated the imaging job.

Relativity sends jobs to the imaging engine by priority, and then orders them by submitted date. To change the priority of a job, click Change Priority at the bottom of the view. Enter a new integer value in the Priority field, and then click Update . Jobs assigned a lower value have a higher priority.

To cancel imaging jobs, select one or more jobs, and click Cancel Imaging Job . You can only cancel jobs that are in a Status of 'Imaging.' Requests to cancel during 'Submitting' will be ignored.

If you cancel an imaging job or delete an imaging set during an imaging job, all images from imaged documents within that set remain in the database.

On this page

- Imaging jobs in the Worker Manager Queue


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


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use

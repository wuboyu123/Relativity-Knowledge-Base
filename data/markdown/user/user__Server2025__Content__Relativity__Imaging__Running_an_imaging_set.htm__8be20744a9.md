---
title: "Running an imaging set"
url: https://help.relativity.com/Server2025/Content/Relativity/Imaging/Running_an_imaging_set.htm
collection: user
fetched_at: 2026-06-22T06:14:11+00:00
sha256: c34cadfca97fea7a31c965cd6923c8245a0120e009d9f4424bd71dffa93770c5
---

Running an imaging set Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Running an imaging set

To run an imaging set, click Image Documents on the imaging set console. This kicks off the conversion of documents to images. While the job is running, this button toggles to Stop Imaging . Use the Stop Imaging button to stop the imaging job. With the Image Documents Options prompt you can Hide Images for QC Review. See QC Review for more information.

## Special considerations

Keep in mind the following special considerations:

- Never upgrade your Relativity version while there are jobs of any type currently in progress in your environment. Doing this leads to inaccurate results when you attempt to finish those jobs after your upgrade is complete. This is especially important for imaging and processing jobs.

- Imaging is not available if the resource pool has no workers designated for imaging.

- The default priority for all image jobs is determined by the current value of the ImagingJobPriorityDefault entry in the Instance setting table.

- You can't delete an imaging set while it is running.

- Imaging Sets will not re-image documents that already have an image.

## Imaging Set console

Depending on the progress of the job, the following options are available on the console:

- Image Documents - begins the imaging job.

- Release Images - allows users to see the images after the QC review process is complete.

- Hide Images - prevents users from viewing the images until the QC review process is complete.

- Retry Errors - reruns documents with imaging errors. This is only enabled if errors have occurred during the imaging job.

Retry Errors will use the same imaging profile the documents with imaging errors were created with, even if the imaging profile is changed.

- View Document Errors - redirects you to the Imaging Document Error tab, where the results are filtered by all imaging errors associated with the documents in the imaging set. You can expand the results by modifying the filters. See Imaging errors .

- View Document Warnings - redirects you to the Imaging Warnings tab, where the results are filtered by all Imaging Warnings associated with the documents in the imaging set. You can expand the results by modifying the filters. See Imaging Warnings .

- Show Errors - provides the option to view document-level errors for an imaging set run prior to Relativity 9.7.229.5 . When you click this button, a pop-up displays a filterable list of documents and fields. The fields include:

- Control Number - the control number of the item in error.

- Artifact ID - the artifact ID of the item in error.

- File Type Identification (Native) - the file type of the item in error as identified by the native imaging engine. This is only populated if the native imaging engine runs the imaging set.

- File Type Identification (Basic) - the file type of the item in error as identified by the basic imaging engine. This value is populated when the basic engine identified the document when you import the document into Relativity.

- Imaging Method - the method selected in the Native Types table for the identified file type in error – Basic or Native.

- Actual Imaging Method - the method that was used to image the item in error – Basic or Native.

- Message - the description of the cause of the error.

- Full Text - the complete error text string the system provides, including stack trace.

- Refresh Page - refreshes the page and see the current state of the imaging job.

When you mass image, image on the fly, run an imaging set, and retry an imaging set, the list of passwords specified in the password bank accompanies the imaging job so that password-protected files are imaged in that job. For more information, see Password bank .

## Imaging profile caching

Relativity caches all imaging profile settings until the imaging job you kick off through the imaging set console completes. The only exceptions to this are the following scenarios:

- In the case of fatal errors, the imaging profile information remains cached until you delete the set or you delete the job record associated with that set from the ProcessingQueue table.

- In the case of non-fatal errors, Relativity no longer caches all profile information except for the Time Zone and Last Modified Date information.

## Password Bank

The Password Bank stores passwords used to protect certain files. When you process or image files protected by the passwords in this bank, Relativity sends the passwords to the respective engine, which then uses them to unlock the corresponding file.

- The Password Bank tab appears under both the Imaging and the Processing applications and is updated in each to reflect the most current entries are added, deleted, or edited.

- Save as PDF does not integrate with the Password bank. If you select Save as PDF when imaging a native document that is password protected, an error occurs.

For more information, see Password bank .

On this page

- Running an imaging set

- Special considerations

- Imaging Set console

- Imaging profile caching

- Password Bank


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

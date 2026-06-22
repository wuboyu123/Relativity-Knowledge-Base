---
title: "Stage and run a production"
url: https://help.relativity.com/Server2025/Content/Relativity/Production/Production_console/Stage_and_run_a_production.htm
collection: user
fetched_at: 2026-06-22T06:08:43+00:00
sha256: b268d608e348bc10bf1f0987576afa6241b64159e900c8937746563fe4fec802
---

Stage and run a production Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Stage and run a production

To stage and run a production in a single step, click Stage and Run Production on the Production console.

## Staging and running a production

A stage and run production job goes through 4 steps:

- Staging

- Validation

- Production

- Branding

See a Stage and Run Production workflow

### Staging

During the staging step, Relativity takes a snapshot of the data sources. After staging finishes, Relativity automatically begins the validation step.

Staging errors occur when

- The same document is found in multiple data sources.

When the same document is found in multiple data sources, you will receive an error message. The error message identifies the data sources that pulled back the same document and which document they pulled back. To resolve the error, modify the saved searches that you selected as your data sources to ensure that they do not pull back any of the same documents.

- There are no documents in the data sources.

When no documents are found in the data sources, you will receive an error message. To resolve the error, make sure that the saved searches that you selected as your data sources are pulling back documents.

If a staging error occurs, address the error and then click Stage and Run Production .

### Validation

During validation, Relativity performs a conflict check and data source validation. After validation finishes, production begins.

When a validation error occurs, click View Production Errors and Warnings on the Production console to open the Error Starting Production pop-up. The Error Staging Production pop-up lists the errors that occurred.

There are two types of validation errors.

- Data source - occurs when documents in the data source do not have images or natives. To resolve the error, modify the data sources and then click Stage and Run Production .

- Conflict - occurs when the data sources have documents that are also in the saved search selected in the Production Restriction field.

Conflict resolution option Fix

Remove the conflict

Remove documents from the production set that are also in the saved search selected in the Production Restriction field.

To remove the conflict:

- Click Check for Conflicts on the Production console. The Production Restrictions pop-up will open.

- Click Remove Conflict on the Production Restrictions pop-up.

- Click Run Production on the Production console.

Override the conflict

Keep the documents in the production set that are also in the saved search selected in the Production Restriction field.

To override the conflict:

- Click Run Production on the Production console. The Production Warnings pop-up will open.

- Click Override and Continue on the Production Warnings pop-up. The production job will continue without removing the conflict documents.

Modify the production restriction

Modify the Production Restriction field so none of the documents in the production restriction saved search are also in the production set. For information on modifying a production restriction, see Adding and editing production restrictions .

After modifying the production restriction, click Stage and Run Production on the Production console.

### Production

During production, Relativity produces the staged documents. After production finishes, branding begins.

If a production error occurs, click View Production Errors and Warnings on the Production console to see why the error occurred. After addressing the error, click Run Production on the Production console.

### Branding

During branding, Relativity applies redactions and the specified header and footer to the images. Once this step finishes, your production job is complete.

To resolve branding errors:

- Click View Branding Errors on the Production console to open the Branding Errors pop-up.

- Read the Branding Error Message to determine the cause of the error and resolve it. Possible errors include:

Branding Error Message Fix

All branding managers are disabled or no branding manager exists. Enable or create the Branding Manager and Production Manager agents. For more information on agents, see Agents .

Could not find file <file path>. Since the system can not find the file path to the image, make sure the image exists at the file path mentioned in the Branding Error Message. You may need to image or import the document again.

The file at <file path> could not be opened or is not a valid image file.

- If the document is encrypted, add the document's password to the Password Bank. For more information, see Password Bank .

- Make sure Relativity supports the file type of the image. You may need to image or import the document again.

The process cannot access the file <file path> because it is being used by another process. This is usually the result of antivirus software. To resolve the error, click Rerun Errored Documents on the Production console. If you receive the same error after rerunning the errored documents, unlock the file or folder mentioned in the Branding Error Message and then click Rerun Errored Documents .

The number of images for document has changed after this production was initially run.

- Click Rerun Errored Documents to finish the production job.

To cancel the job, click Cancel on the Production console.

### Post Production

This step is only available on the Production Set Console if Post Production was enabled during Production Set creation. During this step Relativity automates frequent production tasks.

## Checking production status

During each part of the production, a report is available in the Status section. The Stage, Produce, and Brand steps of the production has its own report. Use these reports to quickly identify the number of documents, images, redacted documents, etc.

### Staging Summary fields

Staging Summary fields include:

- Total Documents Count - lists the number of documents found during staging.

- Total Images Count - lists the number of images found during staging.

- Documents with Images - lists the number of documents that include images found during staging

- Documents with Natives - lists the number of documents that include native files found during staging.

- Documents with Placeholders - lists the number of documents that include production placeholders found during staging.

- Redacted Documents - lists the number of documents that include redactions found during staging.

### Production Summary fields

Production Summary fields include:

- Begin Bates - lists the Bates number of the first document in the production set.

- End Bates - lists the Bates number of the last document in the production set.

- Total Docs - lists the number of documents included in the production set.

- Total Images - lists the number of images included in the production set.

- Docs with Images - lists the number of documents that include images included in the production set.

- Docs with Placeholders - lists the number of documents that include placeholders included in the production set.

- Docs with Redactions - lists the number of documents that include redactions included in the production set.

Production does not include any redactions applied to native documents when using Relativity Redact, only redactions applied using the image viewer and markup set contained on images will be included.

- Total Image size in GB - lists the size of images in GB.

- Run Date - lists the date of when the production was run.

### Branding Summary fields

Branding Summary fields include:

- Start Time - lists the start time of branding.

- Branding Completion - lists the time of completion for branding.

- Completion Rate - lists the progress of branding.

- Estimated Time Remaining - lists the amount of time left in branding.

### Post Production Summary fields

Post Production fields include:

- Copy Bates to Document Fields - lists the progress of step

On this page

- Stage and run a production

- Staging and running a production

- Staging

- Validation

- Production

- Branding

- Post Production

- Checking production status

- Staging Summary fields

- Production Summary fields

- Branding Summary fields

- Post Production Summary fields


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

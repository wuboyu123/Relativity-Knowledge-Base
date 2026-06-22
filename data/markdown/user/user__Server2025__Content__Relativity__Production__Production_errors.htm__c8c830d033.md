---
title: "Production errors"
url: https://help.relativity.com/Server2025/Content/Relativity/Production/Production_errors.htm
collection: user
fetched_at: 2026-06-22T06:08:33+00:00
sha256: 68e5699172755eaf79445121b3c8bb3016814de6ddd5ec3b8facd315160d37ce
---

Production errors Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Production errors

When staging and running a production job, staging, validation, and branding errors can occur.

## Staging errors

Staging errors occur when

- The same document is found in multiple data sources.

When the same document is found in multiple data sources, you will receive an error message. The error message identifies the data sources that pulled back the same document and which document they pulled back. To resolve the error, modify the saved searches that you selected as your data sources to ensure that they do not pull back any of the same documents.

- There are no documents in the data sources.

When no documents are found in the data sources, you will receive an error message. To resolve the error, make sure that the saved searches that you selected as your data sources are pulling back documents.

## Validation errors

There are two types of validations errors:

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

## Branding errors

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

## Post Production errors

These errors are usually related to transient issues. To resolve Post Production errors:

- Click Rerun Post Production errors on the Production console.

On this page

- Production errors

- Staging errors

- Validation errors

- Branding errors

- Post Production errors


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

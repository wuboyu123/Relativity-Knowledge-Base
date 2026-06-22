---
title: "Reproduce a redaction to a document universe"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Reproduce_redaction_to_document_universe.htm
collection: user
fetched_at: 2026-06-22T06:10:00+00:00
sha256: b79a81dfac858767fd963086e8cc10b393c1ffd37a85dea185a2fee28a496e2c
---

Reproduce a redaction to a document universe Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Reproduce a redaction to a document universe

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

This solution reproduces the redactions made on all pages of all documents in a selected saved search from a source markup set to a destination markup set. This solution does not apply redactions to native files.

## Before you begin

This solution reproduces the redactions made on all pages of all documents in a selected saved search from a source markup set to a destination markup set.

### Supported versions

This solution is supported in Relativity Server 2023, Server 2024, and RelativityOne.

Click on any of these links to download the appropriate version from the Relativity Community:

Solution version Supported Relativity version

2.3 Server 2023-Server 2024, RelativityOne

### Components

This custom solution consists of a Relativity script that runs at the workspace level.

### Considerations

- This script should only be run by a system admin. If you are not a system admin, we recommend you do not run this script.

- The results of the script cannot be undone. We recommend that you create a back-up copy of all redactions before you run the solution.

- All documents in the saved search should be in the same orientation to prevent out-of-bound redactions.

- This script updates the Markup Set field with "Has Redactions" and "Has Highlights".

- This script does not create audit records for the redactions that are copied.

## Deploying and configuring the solution

To deploy the solution, you first add it to the Application Library as a Relativity application. You can then install it from the Application Library to one or more workspaces.

This script runs from the Admin level, you must install this application into a workspace for it to appear in the Script Library (at the instance level).

To add the solution to the Application Library:

- Log in to Relativity.

- Navigate to the Application Library tab.

- Click New Library Application .

- Either click Select File, or drag and drop the file into the Application.

- Navigate to and select the application file included in the solution, and then click Open .

- Click Save to upload the file to the Application Library.

To add the solution to a workspace:

- In the Workspaces Installed section, click Select to install the application to one or more workspaces.

- Select the workspace(s) where you want to install the application, and then click the Move selected left to right icon.

- Click Apply .

The application is installed to the selected workspace(s). A list of workspace(s) where the application has been installed displays in the Workspaces Installed section.

## Running the solution

After installing the application, you can configure and run the solution by doing the following:

- In the workspace, click the Administration tab, and the click the Scripts tab.

- Click the name of the Reproduce Redaction to Document Universe script. The Reproduce Redaction to Document Universe script page appears.

- Complete the following fields:

- Documents to Redact - Select the saved search which contains the documents to reproduce redactions to.

- Source Markup Set - Select the markup set which contains the redaction you would like to reproduce to the destination markup set.

- Destination Markup Set - Select the markup set which you would like to reproduce the redaction to.

## Viewing the results

When the script is executed, it will copy all redactions on the selected source markup set to the destination markup set on all pages of all documents in the selected saved search. After the script runs, the report displays a message indicating that redactions were successfully copied.

On this page

- Reproduce a redaction to a document universe

- Before you begin

- Supported versions

- Components

- Considerations

- Deploying and configuring the solution

- Running the solution

- Viewing the results


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

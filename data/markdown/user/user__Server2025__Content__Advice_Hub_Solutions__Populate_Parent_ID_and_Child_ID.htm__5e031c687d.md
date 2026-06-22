---
title: "Populate Parent ID and Child ID"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Populate_Parent_ID_and_Child_ID.htm
collection: user
fetched_at: 2026-06-22T06:17:12+00:00
sha256: bba37f075853ec52999921288b408240d9ba712cb137d7c3751a0c91c14745d3
---

Populate Parent ID and Child ID Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Populate Parent ID and Child ID

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

The Populate Parent ID and Child ID solution is a workspace-level script that populates a production Parent ID and Child ID on a document for a production set.

Populate Parent ID and Child ID is a separate solution from Populate parent ID to child, which is a workspace-level script that propagates the Document ID of the parent document to any children of that document. See Populate parent ID to child for more details about that solution.

This script will not honor document-level permissions. Workspace admin who have permissions to all documents will run this script.

### Supported versions

This solution is supported in all Server versions and Relativity One.

You can download version 10 of Populate Parent ID and Child ID on the Community. You must be logged in to the Community to access this download.

## Special considerations

Review the following considerations for this solution:

- This script should only be run by a system admin. If you are not a system admin, we recommend you do not run this script.

- Due to changes in the way productions are stored in Relativity, this script is not able to be installed at the Admin (Home) level. Instead it must be installed at the workspace level.

- The script overwrites the values in the Parent and Child ID fields.

- Changes made by the script can't be undone.

- This solution doesn't support the client domains (multi-tenancy) and Data Grid features of Relativity.

- The script takes longer to complete when the workspace contains a large number of groups.

- Since the script framework has a default timeout of 20 minutes, we recommend limiting the number of documents to approximately 20,000 - 30,000.

- As the script determines families based on the sort order the production was produced in, sort by families when producing productions if you plan on using this script.

## Performance

Groups Documents Time

17K 20K 7:25

45K 50K 31:12

73K 100K 1:12:44

The results of the script depend on the size of documents in the workspace. If you have issues with performance, we recommend splitting the documents into multiple production sets or contacting Relativity support.

## Preparing the workspace

Before you can run the script, you must install the script at the workspace level and create two fields on the Document object to store the Parent ID and Child ID.

### Installing the script

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

### Creating the fields

Before running the solution, you need to create a fixed-length text field to store the Parent ID and a long-text field to store the Child ID.

Complete the following steps to create fields for storing the data:

- Navigate to the Fields tabs.

- Click New Field .

- Select Document in the Object Type drop-down list.

- Enter a name for the Parent ID field in the Name field.

- Select Fixed-Length in the Field Type drop-down list.

If you have Store in Data Grid, set it to Disabled in Advanced Settings. Having Store in Data Grid enabled will cause the script to fail.

- Select any other options that you want for the field. Click Save and Back .

- Repeat steps 2-6 for the Child ID field. Select Long-Text in the Field Type drop-down list.

## Running the solution

After configuring the workspace, you can configure and run the solution by completing the following:

- In the workspace, navigate to the Scripts tabs.

- Click the name of the Populate Parent ID and Child ID script.

- In the Actions console, click Run script .

- Complete the following required fields:

- Production - a required list of productions in the workspace.

- Relational Field - a required, single-choice drop-down list that contains an alphabetical list of all Fixed-Length Text fields with relational set to “Yes” in the workspace.

- Parent ID Field - a required, single-choice drop-down list that contains an alphabetical list of all Fixed-Length Text fields in the workspace. The script overwrites the values when it executes.

- Child ID Field - a required, single-choice drop-down list that contains an alphabetical list of all Long-Text fields in the workspace. The script overwrites the values when it executes.

- Click Run .

## Viewing the results

When the script executes, it updates the selected Parent ID and Child ID fields for all documents included in the production set data source. The OutputMessage section lists whether the script ran successfully, how many documents were updated, how long it took to run the script, and error messages.

If any of the following scenarios occur, the documents aren't updated and an error message displays in the OutputMessage section.

- The production set includes one or more documents with the same Begin Bates number.

- The Begin Bates or the End Bates number is null.

- The Inclusion of Related Documents field is set to Yes and documents in a relational group exist outside the production set.

To view the results of the script, create a view on the Documents tab that contains the fields you selected for Relational, Parent ID, and Child ID.

On this page

- Populate Parent ID and Child ID

-

- Supported versions

- Special considerations

- Performance

- Preparing the workspace

- Installing the script

- Creating the fields

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

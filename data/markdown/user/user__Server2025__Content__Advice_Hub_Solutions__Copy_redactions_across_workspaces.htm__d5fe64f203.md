---
title: "Copy redactions across workspaces"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Copy_redactions_across_workspaces.htm
collection: user
fetched_at: 2026-06-22T06:09:57+00:00
sha256: f722998be175b82a0290792604157a7071f7aed81e59c7315df98eb1e754097c
---

Copy redactions across workspaces

# Copy redactions across workspaces

The Copy Redactions Across Workspaces solution copies redactions placed on images from a source markup set to a destination markup set in a separate workspace. This solution does not copy redactions to native files.

To download the solution files, visit the Relativity Community .

## Before you begin

The Copy Redactions Across Workspaces solution copies redactions from a source markup set to a destination markup set in a separate workspace. The solution does not remove original redactions. It only appends new ones to the selected destination set.

### Supported versions

This script is supported in Relativity 8.0 – Server 2024 and RelativityOne.

Solution version Supported Relativity version

4.4.0.1 9.4.254.2 - Server 2024, RelativityOne

### Components

This solution consists of the following components:

- Relativity scripts that run at the workspace level.

- Relativity script that runs at the admin level.

### Considerations

- These scripts should only be run by a system admin. If you are not a system admin, we recommend you do not run these scripts.

- The results of the script cannot be undone. We recommend that you create a back-up copy of all redactions before you run the solution.

- If there are no redactions in the selected markup set for the Source Markup Set input, no documents are affected.

- The saved search used as inputs to the Read Source Markup Set script and Write Destination Markup Set script needs to have images. Otherwise no documents are affected.

- This solution doesn't support the client domains (multi-tenancy).

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

### Installing the Read Source Markup Set script

Install the Read Source Markup Set script to the workspace you want to copy redactions from.

- Navigate to the workspace which you are copying redactions from.

- Navigate to the Scripts tab.

- Click New Relativity Script .

- Next to Script Type , click Select from Script Library .

- Next to Scripts , click Select .

- Select the Copy Redactions Across Workspaces - Read Source Markup Set script from the list.

- Click Set .

- Click Save .

### Installing the Write Destination Markup Set script

Install the Write Destination Markup Set script to the workspace you want to copy redactions to.

- Navigate to the workspace which you are copying redactions to.

- Navigate to the Scripts tab.

- Click New Relativity Script .

- For the Script Type field, click Select from Script Library .

- For the Relativity Script field, click Select .

- Select the Copy Redactions Across Workspaces - Write Destination Markup Set script from the list.

- Click Set .

- Click Save .

## Running the solution

After you prepare the workspaces, you can configure and run each solution in its respective workspace.

There should only be one instance of the solution running at a time. If you run multiple instances of the solution at the same time, the results may be unreliable.

### Running the Setup script

The Copy Redactions Across Workspaces - Setup script only needs to be run once in the admin workspace to begin using this application.

- At the instance level, navigate to the Relativity Script Library tab.

- Find and select Copy Redactions Across Workspaces - Setup from the list.

- Click Run Script .

### Running the Read Source Markup Set script

Run the Read Source Markup Set script in the workspace which you are copying redactions from.

- In the workspace which you are copying redactions from, navigate to the Scripts tab.

- Click on the name of the Copy Redactions Across Workspaces - Read Source Markup Set script.

- Complete the following fields:

- Source Document Set – select the saved search that contains a list of documents you wish to execute upon.

- Doc Identifier – select the fixed-length text field that contains the Document Identifier field.

- Source Markup Set – select the markup set field that you would like to copy the redactions from.

- Click Run .

### Running the Write Destination Markup Set script

Run the Write Destination Markup Set script in the workspace which you are copying redactions to.

- In the workspace which you are copying redactions to, navigate to the Scripts tab.

- Click the name of the Copy Redactions Across Workspaces - Write Destination Markup Set script.

- Complete the following fields:

- Dest. Document Set – select the saved search that contains a list of documents you wish to execute upon.

- Doc Identifier – select the fixed-length field that contains the Document Identifier field.

- Dest. Markup Set – select the markup set field that you would like to copy the redactions to.

- Click Run .

Doc Identifier fields for both the source and destination workspaces need to contain identical values in order to copy all redactions.

## Viewing the results

After you run the solution by running the Read Source Markup Set script, the results appear as a report on the script page. The report includes a list that indicates how many markup sets have successfully been copied.

After you run the solution by running the Write Destination Markup Set script, the results appear as a report on the script page. The report includes a list that indicates how many markup sets have successfully been copied.

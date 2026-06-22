---
title: "Collect folder path data"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Collect_folder_path_data.htm
collection: user
fetched_at: 2026-06-22T06:10:02+00:00
sha256: 80b25e3e73bef6689dbf978cbcdceaf8398568570132268f8a6ac2bbe7de512f
---

Collect folder path data

# Collect folder path data

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

The Collect Folder Path Data solution reports the total number and size of document files, including native, image, and production files, that are in each workspace and folder in a Relativity instance.

## Before you begin

The Collect Folder Path Data solution is an environment-level solution that collects and reports the total number and size, in gigabytes (GB), of document files in a Relativity instance. The report organizes data by workspace and folder, and, for each folder, provides details such as the total number of native, image, and production files within the folder as well as the total size of those files.

### Components

This solution consists of the following components:

- Relativity application

- Custom agents

- Event handlers

- Relativity script that runs at the environment level

### Considerations

Before you deploy and run the solution, it's important to keep the following in mind:

If your environment has a version of Collect Folder Path before version 6.0, please uninstall the older version from each workspace and environment prior to installing version 6.0.

- This script should only be run by a system admin. If you are not a system admin, we recommend you do not run this script.

- We recommend setting the manager agent interval to 86400. Please note that setting the agent to anything less than 3 hours (10800) might affect the final results. This is also directly related to the number of worker agents installed and enabled, as well as available system resources.

- You can only install one manager agent, but you can have more than one worker agent installed. In large environments, we recommend adding multiple worker agents.

- The results of running from the administration mode for a Relativity instance or a specific workspace where you install the solution are the same. The script reports the total number and size of document files for all the workspaces in a Relativity instance. To limit report data to a specific workspace or folder, you can use the filter controls in the report.

- This solution doesn't support the client domains (multi-tenancy) and Data Grid features of Relativity.

## Deploying and configuring the solution

To deploy and configure the solution, perform the following:

- Add the solution application to the Application Library and install it in a workspace.

- Create and enable custom agents that monitor and perform data collection tasks.

- Check the Worker Queue status.

### Excluding specific workspaces

In Solution Version 7.0 or above, specific workspaces can be skipped by the application by adding them to a blacklist. To accomplish this, you will need to update data on the SQL server of the environment. To skip certain workspaces, do the following:

- Collect the Artifact IDs of the desired workspaces to exclude:

- Insert the Artifact IDs into the EDDS.eddsdbo.KCD_1037595_Excludes table.

- Sample query:

```text
INSERT INTO [EDDS].[eddsdbo].[KCD_1037595_WorkspacesToExcludes] (WorkspaceArtifactID)
			VALUES(/* comma separated workspace Artifact IDs */)
```

### Adding the solution to the Application Library and a workspace

To begin using this solution, download and add it to the Application Library as a Relativity application.

To download the application:

-

Log in to the Relativity Community , and click on the Relativity Applications folder.

-

Locate the newest Collect Folder Path Data .rap file that is compatible with your version of Relativity and select it.

The solutions in the Relativity Applications folder are sorted from most recently modified to oldest. As a result, solutions at the top of the page are normally the newest versions of the respective solutions. If you see more than one version of the solution, select the .rap file with the higher version number to ensure you're deploying the most up-to-date solution.

-

Click Download .

To add the solution to the Application Library:

- Navigate to the Application Library tab.

- Click Upload Application .

- Click Select File .

- Navigate to and select the application file included in the solution, and then click Open .

- Click Save to upload the file to the Application Library.

### Creating and enabling custom agents

After you add the solution to the Application Library and install it in a workspace, you're ready to create and enable a Folder Path Manager agent, which monitors data collection tasks for the solution, and one or more Folder Path Worker agents, which collect data about folders and files. Note that only one Folder Path Manager agent can be installed at a time. To optimize solution performance however, you can create and enable multiple Folder Path Worker agents.

To create and enable the Folder Path Manager agent:

- Navigate to the Agents tab.

- Click New Agent .

- Complete the following fields:

- Agent Type - click Select , choose KCD_1037595_FolderPath - Manager , and then click Set .

- Number of Agents - enter 1 .

- Agent Server - click Select , choose the server that you want the agent to run on, and then click Set .

- Run interval - enter 86400 .

We recommend you adjust the agent run interval to execute once a day, or every 86400 seconds.

- Logging level of event details - select the type of information that you want to log for the agent.

- Initial Status - ensure the toggle is enabled.

- Click Save and Back .

The "KCD_1037595_FolderPath - Manager" agent now appears in the list of agents.

To create and enable a Folder Path Worker agent:

- On the Agents tab, click New Agent .

- Complete the following fields:

- Agent Type - click Select , choose KCD_1037595_FolderPath - Worker , and then click Set .

- Number of Agents - enter the number of worker agents that you want to add.

- Agent Server - click Select , choose the server that you want the agent to run on, and then click Set .

- Run interval - type 30 .

- Logging level of event details - select the type of information that you want to log for the agent.

- Initial Status - ensure the toggle is enabled.

- Click Save and Back .

The "KCD_1037595_FolderPath - Worker" agent now appears in the list of agents.

## Running the solution

You can run the Collect Folder Path Data script from administration mode for the Relativity instance the workspace where you installed the solution application.

A job for the Folder Path Worker agent should run at least one time before you run the script.

To check the job status of the Folder Path Worker agent, complete the following:

- Navigate to the workspace where you installed the solution application.

- Navigate to the Worker Queue tab.

The Worker Queue page displays the current job status for each workspace that the Folder Path Worker agent is processing.

After the job status is "Completed" for each workspace, you can run the Collect Folder Path Data script by performing the following steps.

- Navigate to the Relativity Script Library tab. Running the script from the Admin level returns data for all workspaces.

- Click the name of the Collect Folder Path Data script.

- In the console, click Run Script , select the desired Workspace option, and then click Run in the modal.

## Viewing the results

After you run the solution, the results appear as a report on the modal.

The report provides detailed information about the number and size of document files that are in each workspace and folder in the Relativity instance, minus any excluded workspaces. It includes the following columns:

- Workspace Artifact ID

- Workspace Name

- Folder Path

- Document Count

- Native File Count

- Native File Size (GB)

- Image File Count

- Image File Size (GB)

- Produced Image File Count

- Produced Image File Size (GB)

- Total Image File Count

- Total Image File Size (GB)

- Total File Count

- Total File Size (GB)

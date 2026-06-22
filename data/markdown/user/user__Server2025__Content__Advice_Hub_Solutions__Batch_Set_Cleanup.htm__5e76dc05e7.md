---
title: "Batch Set Cleanup"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Batch_Set_Cleanup.htm
collection: user
fetched_at: 2026-06-22T06:04:12+00:00
sha256: bcfeb6d6e4c902ee2229c948bb2a54a9c7d3f2f93f628121d48a5ef90c7906ae
---

Batch Set Cleanup Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Batch Set Cleanup

Batch Set Cleanup replaces the Remove documents from batch sets application, which is no longer supported in Server 2025.

Batch Set Cleanup removes all documents within a saved search of each batch set you specify.

## Migrating from Remove documents from batch sets

Any pre-existing jobs in the Remove documents from batch sets application should be replicated and completed in Batch Set Cleanup before removing the old application. You can do this by following the Running Batch Set Cleanup instructions below, but choosing the same name, saved search, and batch set as the Remove documents from batch sets job you'd like to complete. For more information, visit Running Batch Set Cleanup .

## Before you begin

Batch Set Cleanup removes all documents within a saved search of any batch set you identify while running the application. Review the following information before proceeding:

### Components

This solution consists of the following components:

- Console event handler

- Manager agent

- Worker agent

- Custom job RDO

- Custom page

- Relativity application

### Considerations

- When using a batch set with auto-batch enabled, ensure batching completes before using the batch set with this solution.

- Purging a batch set or the records from a job, while it’s in progress, results in an error.

- Selecting a saved search that contains no documents results in a job with an error status.

## Deploying and configuring the solution

To deploy and configure Batch Set Cleanup in your workspace, you must perform the following step:

- Install the Review application to your workspace.

- Install manager and worker agents.

### Install the Review application to your workspace

To install the application to your workspace, perform the following steps:

- Navigate to the Application Library tab.

- Click on the Review application.

- In the Workspaces Installed section, click Select to install the application to one or more workspaces.

- Select the workspace(s) where you want to install the application, and then click the Move selected left to right icon.

- Click Apply .

The application is installed to the selected workspace(s). A list of workspace(s) where the application has been installed displays in the Workspaces Installed section.

### Install manager and worker agents

To install the required manager and worker agents, perform the following steps:

- Navigate to the Agents tab and then click New Agent .

- Click Select next to Agent Type.

- Locate the Batch Set Cleanup Manager agent, select it, and then click Set .

- Click Select next to Agent Server.

- Select the agent server on which you want the agent to run, and then click Set .

- Set the Run Interval to 5 .

- Select the desired Logging level option.

- Ensure that Initial Status is toggled on.

- Click Save .

The agent appears in the Agents list with the name Batch Set Cleanup Manager.

- Repeat the same process to add the Batch Set Cleanup Worker agent.

Batch Set Cleanup supports a maximum of 10 manager agents and 10 worker agents.

## Running Batch Set Cleanup

To run the application in your workspace, perform the following steps:

### Create a new job

- Navigate to the Batch Set Cleanup tab in your workspace.

- Click New Batch Set Cleanup .

- Enter a Name and optionally, enter a Priority .

- Click Save .

### Configure the job

- Select the job you just created from the list.

- Click Configure Job on the Manage Job console.

- Click on the Saved Search drop-down menu and select the search that contains the documents you want to remove.

- Click on the Batch Sets drop-down menu and select the batch sets you want those documents removed from.

- Click Save .

- Click Submit Job in the Manage Job console.

### 3.1.1 Canceling a job

The Cancel Job button enables on the Manage Job console whenever the current job is in progress. When you click Cancel Job , the agent finishes its current batch of up to 25,000 documents before fully canceling the job.

### 3.1.2 Purging a job

The Purge Job button enables on the Manage Job console whenever a job’s status is Ready, Completed, or Error. When you purge a job, the records from the tables associated with the job delete.

## Viewing the results

The job is finished when the Status field displays Complete.

The results display in the Message field of the job custom object you created. Specifically, the Message fields provides the following counts:

- Total Documents in Saved Search

- Documents Removed from Selected Batchsets

- Documents Not Included in Selected Batchsets

Results don't display until the job status is marked Ready. Click into a specific job and Refresh the page to update the results.

On this page

- Batch Set Cleanup

- Migrating from Remove documents from batch sets

- Before you begin

- Components

- Considerations

- Deploying and configuring the solution

- Install the Review application to your workspace

- Install manager and worker agents

- Running Batch Set Cleanup

- Create a new job

- Configure the job

- 3.1.1 Canceling a job

- 3.1.2 Purging a job

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

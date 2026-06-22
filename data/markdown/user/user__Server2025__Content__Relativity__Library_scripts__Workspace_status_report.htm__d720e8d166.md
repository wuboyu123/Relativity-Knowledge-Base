---
title: "Workspace status report"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Workspace_status_report.htm
collection: user
fetched_at: 2026-06-22T06:15:41+00:00
sha256: f2930c22c5247f5a7422257cf65eaae0ad6fbe8f8a1a7e3430c49af188445e13
---

Workspace status report

# Workspace status report

The Workspace Status Report script reports on the last action performed by a non-system admin in each workspace in the Relativity instance.

## Special considerations

Consider the following when working with the Workspace Status Report script.

- The script runs from Home.

- The script's results exclude users in the System Administrators group.

- If non-system admins complete no actions in a given workspace, then that workspace still appears in the results with its Last Action and Username fields blank.

- Only workspaces with an "Active" status appear in the report.

- The report excludes any audit actions performed by users in the System Administrators group.

### Performance

The script's performance depends on the number of workspaces in the environment. In an environment with 79 workspaces, the script executed in 20 seconds.

Custom components may not exhibit the same performance and behavior as native Relativity features.

## Running the script

To run the script:

- Click your name in the upper right corner of Relativity, and click Home .

- Click the Relativity Script Library tab.

- Click the Workspace Status Report link.

- On the script details page, click the Run Script button.

- (Optional) To exclude actions performed by certain users from the results, enter each user's artifact ID in a comma-delimited list. Don't end the list in a comma.

To find a user's Artifact ID, click on the user from Home, and locate the artifact ID in the URL. For example, a user with the URL <http://localhost/Relativity/Admin/User/View.aspx?AppID=-1&ArtifactID=1020915> has an artifact ID of 1020915.

- In the Run Script window, click Run again.

For additional assistance, contact Relativity Support .

## Outputs

After the script executes, the Results section contains the following information:

Column Description

Workspace Name The name of the workspace.

Workspace Artifact ID The artifact ID of the workspace.

Date of Last Audit Report

The timestamp of the last audit record in the workspace in mm/dd/yyyy format.

The report excludes any actions performed by users in the System Administrators group or in the Users to Exclude list.

Latest Action in Workspace The action of the last audit record in the workspace.

Username The user who performed the action of the last audit record in the workspace in <Last Name>, <First Name> format.

---
title: "Create cluster upgrade jobs"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Create_Cluster_Upgrade_Jobs.htm
collection: user
fetched_at: 2026-06-22T06:15:17+00:00
sha256: 6c213719c027dcb7e6377ac28cf9f6fb12171ebe6c38055b0c6d0eac15e7ec35
---

Create cluster upgrade jobs

# Create Cluster Upgrade Jobs

This Relativity script creates job entries in the EDDS.eddsdbo.ClusterUpgradeJobs database table. The job entries are used to upgrade Analytics clusters for performance improvements introduced in CAAT 3.17.2 and above. The cluster upgrade jobs are managed by the Cluster Upgrade Worker agent. See Agents for more information regarding the Cluster Upgrade Worker agent.

CAAT 3.17.2 was introduced in Relativity 9.2.271.9.

You can run this script to create cluster upgrade jobs for a specific workspace or all workspaces in your environment. The script identifies all the clusters in a selected workspace or all workspaces that have a Version column value equal to 0 in the ContentAnalystCluster table and do not have an entry in the EDDS.eddsdbo.ClusterUpgradeJobs table. The script creates the ClusterUpgradeJobs table if it doesn't already exist. The table contains the following columns and data:

- JobID - identifier column for cluster upgrade jobs

- WorkspaceArtifactID - identifier of the workspace that contains a cluster being upgraded

- IndexID - identifier of the CAAT index where the cluster exists. This identifier matches the ID column on ContentAnalystIndex table.

- ClusterID - identifier of the cluster. This identifier matches the ID column on ContentAnalystCluster table.

- ResourceServerID - identifier of the Analytics Server. This identifier matches the ID column on the ResourceServer table.

- Status - status of an upgrade job represented by one of the following values:

- 0 - Waiting

- 1 - In progress

- 3 - Error

- 2 - Complete

- Retries - number of times the Cluster Upgrade Worker agent retried an errored upgrade job

## Special considerations

Consider the following when running this script:

- This script creates the cluster upgrade jobs, but it doesn't monitor the progress of the upgrade jobs. To check the progress of your queued cluster upgrade jobs, run the Monitor Cluster Upgrade Jobs script.

- The script may run for some time without reporting any progress.

## Inputs

After clicking Run Script on the Script Console, select one of the following options from the Workspace Name drop-down menu:

- <All Workspaces> - select this option to create upgrade jobs for all clusters found in all workspaces in your environment.

- Specific workspace name - select the name of a specific workspace to create upgrade jobs for all clusters found only in the selected workspace.

## Results

After you run the script, the Create Cluster Upgrade Jobs dialog lists all workspaces or your selected workspace based on your input selection and the count of clusters per workspace.

The following columns are included:

Column Definition

ArtifactID Database ID of the workspace

Workspace Name Name of the workspace

Cluster Set Count Number of clusters identified in the workspace

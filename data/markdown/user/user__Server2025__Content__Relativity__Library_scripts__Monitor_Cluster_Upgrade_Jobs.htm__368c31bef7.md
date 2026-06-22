---
title: "Monitor cluster upgrade jobs"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Monitor_Cluster_Upgrade_Jobs.htm
collection: user
fetched_at: 2026-06-22T06:15:24+00:00
sha256: 6cadb5d5db0df867303b8a87a503115f008edc4ad4d70765e4eae97392416b10
---

Monitor cluster upgrade jobs

# Monitor Cluster Upgrade Jobs

This Relativity script checks and reports the status of all Analytics cluster upgrade jobs recorded in the EDDS.eddsdbo.ClusterUpgradeJobs database table. The cluster upgrade jobs are created using the Create Cluster Upgrade Jobs script, and are used to upgrade Analytics clusters for performance improvements introduced in CAAT 3.17.2 and above. The cluster upgrade jobs are managed by the Cluster Upgrade Worker agent. See Agents for more information regarding the Cluster Upgrade Worker agent.

CAAT 3.17.2 was introduced in 9.2.271.9.

## Special considerations

Consider the following when running this script:

- This script monitors the progress of the upgrade jobs. To create cluster upgrade jobs for clusters in one or all of your workspaces, run the Create Cluster Upgrade Jobs script.

- The script may run for some time without reporting any progress.

## Inputs

This script requires no inputs.

## Results

After you run the script, the Monitor Cluster Upgrade Jobs dialog lists a count of the jobs in progress and the status of the jobs. If there aren't any jobs currently in progress, the dialog lists all workspaces in your environment and the count of clusters that were upgraded and not upgraded per workspace.

The following columns are included when existing cluster upgrade jobs are still running:

Column Definition

Count Number of cluster upgrade jobs currently in the queue

Status Status

The following columns are included when there are no cluster upgrade jobs running:

Column Definition

ArtifactID Database ID of the workspace

Workspace Name Name of the workspace

Upgraded Cluster Count Number of clusters upgraded by the Cluster Upgrade Worker agent

Not upgraded Cluster Count Number of clusters not upgraded

If you find workspaces with clusters not upgraded, check the Errors tab for reported cluster upgrade failures:

- Navigate to the Errors tab from Home .

- Click the Show Filters button.

- Type Cluster Upgrade Worker in the URL field and press Enter .

- Review the Message column entries to identify Failed to upgrade cluster messages. The Failed to upgrade cluster error messages include the Workspace ArtifactID, IndexID and ClusterID values.

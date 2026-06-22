---
title: "One or more Agent servers are not assigned to any active Resource Pools"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/51016cf0-7d32-41c9-81f7-06e5db922909.htm
collection: user
fetched_at: 2026-06-22T06:18:20+00:00
sha256: 2c3a2b45ac4737c2449eb46985e0c3300a20e7e902ff34e557cf0f881cd19996
---

One or more Agent servers are not assigned to any active Resource Pools

51016cf0-7d32-41c9-81f7-06e5db922909

# One or more Agent servers are not assigned to any active Resource Pools

## Description

This alert is triggered when one or more Agent servers are not assigned to any active resource pools in Relativity. As a result, agents hosted on these servers will not process jobs, even if they appear enabled.

## Resolution Guidance

### Impact When Active

- When an Agent server is not assigned to a resource pool, it cannot perform any task within Relativity. Agents hosted on unassigned servers will not take on work, even if they appear enabled.

### How To Resolve

-

Log into Relativity and navigate to the Resource Pools tab.

-

Click into the resource pool you intend to use.

-

Click on 'Agent and Worker Servers' within the same resource pool.

-

Click the Add button to open the assignment modal.

-

In the modal:

- Select the unassigned agent server(s) from the left pane.

- Move them to the right pane using the arrow button.

-

Click Apply to confirm.

-

Navigate to the Severs tab and confirm that the agent server status is Active.

-

Go to the Agents tab and verify that agents hosted on the newly assigned servers are enabled.

##### You can also try..

If the alert still persists. You can try following:

- Restart the Relativity Service Host on the affected agent servers.

- Confirm that the agent server is in 'active' state in the Servers tab.

- Review Event Viewer logs or Relativity logs on the agent server if agents still fail to run

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View metrics-*

Filter Query relsvr.instance.resource_server.agent : 0 Zero agent servers assigned to active resource pool

Threshold = 0 Count Equal to 0, alert triggers

Time Window 1 min Verified data for last 1 min

Frequency 1 min Checks for every 1 min

### Alert Metric Details

Metric Name: relsvr.instance.resource_server.agent : 0

Metric Description: Alert triggers on when One or more Agent servers are not assigned to any active Resource Pools.

Metric Attributes:

Attribute Name Description

relsvr.instance.resource_server.agent Number of agent servers assigned to active resource pool

labels.resourcepool_active_or_not Resource Pool active or not

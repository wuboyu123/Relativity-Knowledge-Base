---
title: "Retry Production Job"
url: https://help.relativity.com/Server2025/Content/Relativity/Mass_operations/Retry_Production_Job.htm
collection: user
fetched_at: 2026-06-22T06:16:03+00:00
sha256: f424a246471ec8af609fc64c419d55ea8708c5f043097aa040c6ca8114cef453
---

Retry Production Job

# Retry Production Job

To retry multiple production jobs from the Production Queue tab, use the Retry Production Job mass operation.

See these related pages:

- Production

- Production queue

## Security configuration

You must configure certain instance level permissions to use Retry Production Job.

To configure the security permissions:

- Navigate to the Instance Details tab.

- Click Manage Permissions .

- Click Edit Permissions for a group on the Group Management tab.

- Enable the following security permissions:

Object Security Tab Visibility Admin Operations

- N/A

- Queue Management (parent)

- Production Queue (child)

- Change Queue Priority

- View Admin Repository

As long as you have the listed security permissions, you do not need view permissions to the workspaces or the production jobs to use Retry Production Job.

## Retrying production jobs

To retry production jobs from the Production Queue tab:

- Navigate to the Production Queue tab.

- Select the productions jobs that you want to cancel.

- Click Retry Production Job from the mass operations bar. The Retry production job window opens.

- Click Ok .

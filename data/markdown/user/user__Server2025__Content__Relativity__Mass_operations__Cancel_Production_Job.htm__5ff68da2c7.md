---
title: "Cancel Production Job"
url: https://help.relativity.com/Server2025/Content/Relativity/Mass_operations/Cancel_Production_Job.htm
collection: user
fetched_at: 2026-06-22T06:15:43+00:00
sha256: db2271ad739cf856e5c734f32fed00cb69f3d80c27ea59868041c84bd97fd3e8
---

Cancel Production Job

# Cancel Production Job

To cancel multiple production jobs from the Production Queue tab, use the Cancel Production Job mass operation.

## Security configuration

You must configure certain instance level permissions to use Cancel Production Job.

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

As long as users have the listed security permissions, they do not need view permissions to the workspaces or the production jobs to use Cancel Production Job.

## Using Cancel Production Job

To cancel multiple production jobs from the Production Queue tab:

- Navigate to the Production Queue tab.

- Select the productions jobs that you want to cancel.

- Click Cancel Production Job from the mass operations bar. The Cancel production job window opens.

- Click Ok .

For more information about the Production queue, see Production queue .

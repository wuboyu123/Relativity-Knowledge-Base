---
title: "ARM"
url: https://help.relativity.com/Server2025/Content/ARM/ARM_Overview.htm
collection: user
fetched_at: 2026-06-22T06:03:03+00:00
sha256: 3f226d9144f4f1793b331770fe874d48f8d0df9de7fbf2a31d5fd7482b99dbdf
---

ARM

# ARM

Use the ARM application to archive, restore, and move Relativity workspaces between Relativity installations or SQL Servers.

## Job types

- Archive —the archive function assesses a workspace’s primary and critical components and packages those components into an archive. This archive can serve multiple purposes that vary for each organization. For example, you can use this archive to migrate a workspace from one SQL Server to another.

- Move —the move function acts as a 2-in-1 archive and restore. This function can be used to move a workspace or its components between resources on the current installations of Relativity. It is useful when moving a workspace from one SQL Server to another.

- Restore —the restore function restores a fresh workspace in the target installation of Relativity using an archive created with ARM or a restored SQL database. This function is dependent upon the archive function. You can use this function to restore an existing workspace on a different server.

ARM jobs are executed asynchronously by one or many agents. Multiple agents can work simultaneously to complete tasks for different jobs or can work on separate tasks for the same job.

The ARM application uses a staging system that breaks up a job’s work into individual tasks. This staging system shows a job’s progress and gives you actionable information in the case of a job failure. You can see what went wrong, make adjustments, and then resume the job from where it left off.

Stages are executed sequentially; however, the tasks in each stage can be completed simultaneously. If a task fails, the job halts progress in that stage, stores the progress, and then retries the tasks that did not complete.

## Security permissions

By default, only system administrators can access ARM. However, you can grant users in other Relativity groups access to ARM using instance security permissions.

See Instance security for more information.

The following minimum security permissions are required to use ARM.

Object security Tab visibility Admin operations

N/A

ARM parent tab and all child tabs

View Admin Repository

## Unsupported Relativity data

ARM currently does not support the following:

- The Move operation for Processing data like Invariant stores, job metadata, and unpublished files.

- Collections data.

- Cached files. This table is truncated.

You should always be on the latest version of ARM for your Relativity version to take advantage of the current ARM functionality. Refer to the following table to see details on ARM / Relativity compatibility for various types of Relativity data that are partially or completely unsupported.

Relativity Version ARM Version Data Grid Analytics Processing Collections data Cached Files

Server 2024 24000.0.4.13 Archive, Restore, Move Archive, Restore Archive, Restore N/A N/A

## Considerations before using ARM

### General considerations

Review the following before working with ARM:

- You should ensure that the case workspace is not in the process of updating at the time of archiving to prevent inconsistencies in the interim between the archive and the restore.

- You cannot restore a workspace to any previous versions of Relativity, but you can restore to the same version or newer versions. For example, you can restore an archived Relativity Server 2023 workspace to Relativity Server 2024, but you cannot restore an archived Relativity Server 2024 workspace to Relativity Server 2023.

- For Relativity Server you can only restore a workspace to the same version of SQL Server or a higher version. This rule applies to both major and minor SQL version differences. SQL versioning is not an issue in RelativityOne. Customers can restore any workspace from Server to RelativityOne.

- Be sure that the following ports are open on your agent server running the ARM agents to successfully transfer data: Outbound TCP 33001 and Outbound UDP 33001. For more information, contact Relativity Support .

- For ARM archive, if SQL server has a security certificate installed, we recommend decrypting the database before archiving the workspace. An archive created when security certificate was installed on SQL server can be restored only to an SQL Server with the same security certificate. If you have not decrypted the database, you will not be able to restore it in different SQL server.

- Workspaces using Blackout 5.3 or above that migrate from Server to RelativityOne are not supported by Redact.

### Active learning considerations

Review the following before working with active learning projects in ARM:

- When you archive an active learning project, the associated classification index is also archived.

- When restoring a workspace with an active learning project, map your users and permission groups. The users will still exist in the project, but you will need to manually add them back to the queue.

- If you do not map your permission group, Relativity creates a permission group so the active learning project is still usable, but you must add reviewers to the group.

### Analytics considerations

When working with Analytics indexes in ARM:

- If your archived workspace contains Analytics archives, then an Analytics server must exist in the target workspace resource pool.

-

Only active indexes are archived.

### dtSearch considerations

If your archived workspace contains dtSearch archives, the target workspace must have a dtSearch index.

### Processing data considerations

When migrating Processing sets using ARM, please consider these items:

- You must have the Processing Migration Manager installed and enabled to restore processing data. If that agent is disabled, you will receive an error when you try to run the restore job.

- To restore processing data, the Temporary directory field on the Worker Manager Server object in Relativity associated with the workspace in which you're processing data must display the BCP path and a server name, not just local host.

- You should not have any processing jobs, like inventory, discovery, or publish, running in the workspace you are archiving while performing the processing restore job.

- If you receive an authentication error during the restore job, verify that the IdentityServerURL entry in the Invariant AppSettings table contains a valid address with a fully qualified domain name.

- Make sure that the data source location, the Source Path field, is valid in the restored environment for any processing sets that you have restored but have not yet discovered, for any newly created sets, or for sets that were inventoried only. If it is not valid, make sure to update that value for all your data sources.

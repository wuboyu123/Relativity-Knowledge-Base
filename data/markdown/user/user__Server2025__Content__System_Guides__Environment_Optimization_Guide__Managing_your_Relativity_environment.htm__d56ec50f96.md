---
title: "Managing your Relativity environment"
url: https://help.relativity.com/Server2025/Content/System_Guides/Environment_Optimization_Guide/Managing_your_Relativity_environment.htm
collection: user
fetched_at: 2026-06-22T06:17:59+00:00
sha256: 009734d14a46b30744c8e211d88b66a19364ec3c0e486f3bcd2cb1547a278f9f
---

Managing your Relativity environment Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Managing your Relativity environment

To effectively manage Relativity, follow these recommendations for backing up and maintaining your environment.

## Workspace management and maintenance

Large workspaces with more than 500,000 records often require that system or database admins place additional indexes on any necessary fields in the SQL database. This ensures optimal workspace performance for the review team. For more information on SQL indexes, see SQL table index management .

For example, if a document list view includes a sort condition on an un-indexed fixed-length text field in a multimillion record workspace, each time a user selects that view, the executed query sorts on millions of rows. This can take extended time to complete. Each time a user selects this view it consumes significant server resources. Placing an index on this database's eddsdbo.Document table column can help reduce the query time.

You can use the provided generic SQL script to create indexes. Execute the following command to place a non-clustered index on a field:

CREATE NONCLUSTERED INDEX [IX_FieldName] ON [EDDSDBO].[Document] ([FieldName] ASC)

- Execute within the context of the database where you want to add the index.

- Replace the two instances of FieldName with the name of the field you would you want to place an index on (IX_ is just a naming convention). Consider including your initials here for identification purposes.

- Remove any spaces or special characters in the name in the script.

- Execute this script after-hours. This script locks the table for writes during the index build.

In addition to Fixed-Length Text fields, you can apply indexes to Yes/No (Boolean), Decimal, Whole Number, or Date fields on the document table of a workspace database. System admins should identify which fields are regularly queried, sorted, and filtered on in large databases for index creation.

Any manually created indexes carry over during workspace creation. Relativity performs a full backup restore operation and doesn't contain any logic to delete indexes.

Understanding when and where to create additional non-clustered indexes improves with experience. Avoid indexing everything, because a large number of additional indexes can slow down insert and update operations. This can also increase the size of the database which increases maintenance, backup, and replication times.

Read indexes from the SQL Server more than you write indexes. SQL Dynamic Management Views collect and store index usage information. There are scripts available to query this data for reporting purposes. Restarting SQL Server purges data stored in the DMVs, so only analyze this information when the SQL instance has been online for at least a few days or weeks.

### Analysis of long running queries

Long running queries take more than a few seconds to complete. This can include document list views, advanced searches, and other areas of the platform.

- Use the History tab in any workspace to identify long running queries. Include the Execution Time field in a History tab view. This helps to identify queries that take an extended amount of time to process.

- Use the History tab to view the actual SQL executed for every query. Relativity stores the information in the History tab in the eddsdbo.AuditRecord table for each workspace.

- Determine if you can optimize these queries to run more efficiently. For example, avoid nested or combined searches when possible. Avoid "Is Like" statements and simplify the criteria wherever possible.

- Use the estimated execution plan in SQL Server Management Studio to look for suggested indexes. You can also use the SQL Server Database Tuning Advisor for this purpose. If you use this tool, be mindful of the overhead involved as it analyzes the workload in order to make recommendations. If you can't make troublesome queries more efficient through Relativity, you can analyze them using the estimated execution plan or the SQL Server Database Tuning Advisor for suggestions. Apply any suggested indexes and statistics after hours, if necessary.

There are other SQL tools available to help identify long running queries, resource usage and overuse, and database locking issues. These tools are affordable and can assist in SQL Server performance troubleshooting. You can also use SQL Server Activity Monitor, Profiler, and Extended Events for monitoring purposes. Use caution and follow Microsoft best practices when using these tools, as they can be resource-intensive.

### Full-text index management

In Relativity, the keyword search function queries the full-text index of a workspace’s database.

You can query the health of a full text index in SQL Server. The following query returns the number of fragments in a full-text index. Execute it on the database in question.

SELECT OBJECT_NAME(table_id) AS [Table Name], fragment_id, fragment_object_id, [status], data_size, row_count

FROM sys.fulltext_index_fragments WITH (NOLOCK)

For more information on full-text index fragments, see http://msdn.microsoft.com/en-us/library/cc280700.aspx .

If you experience slow keyword search performance, you may need to rebuild the full-text index for that database. You can determine this in SQL Server by querying the amount of FT fragments. Microsoft states that performance suffers significantly if an index has more than 100 fragments. We suggest rebuilding or merging indexes with more than 10 fragments.

To rebuild the FT Catalog for a workspace:

- Navigate to that database in SQL MGMT Studio.

- Expand the Storage > Full Text Catalogs folders, and then right-click FT Catalog .

- Select the option to Rebuild .

During a full-text index rebuild, the workspace is still accessible. However, any keyword or "Contains" searches return incomplete results as the index populates. You should perform this task after hours. Select Properties for the index to view build status and progress.

You could optionally take a full backup of a database, restore it to the same server, and rebuild the full-text index for this restored database. Next, run an identical "Contains" query across each to measure any performance gain from a rebuild. You can also use this to gauge how long it takes to rebuild in the production database and schedule any necessary outage.

You can also use a smart script for managing full-text indexes during a scheduled maintenance window. Contact Relativity Support to obtain this script and get more information.

For more information on full-text search internals and enhancements, see http://msdn.microsoft.com/en-us/library/cc721269.aspx .

### Audit record table

Relativity stores all history for a workspace in the AuditRecord table for that database. The data in this table appears in the History tab for that workspace. Relativity audits all activity. An active workspace with 100 users can generate over ten million audits per month. This table could grow in size by hundreds of millions of rows in some scenarios.

If this table is very large, reducing its size can result in faster backup and index rebuild times.

Unfortunately, organizations often require all audit history be readily available to the review team. In some cases, it may be possible to delete some of the existing audit entries to reduce size and reclaim space.

Consider the following options to reduce the table size:

- Backup the database, backup the AuditRecord table, and then truncate the table (delete all existing audit history).

- Backup the database, backup the AuditRecord table to a certain date, and then delete everything from the table with a time stamp before that date.

If it's not possible to delete any audit entries, there are other options available to help assist with the management of this large table. See the Database Partitioning for Archiving Audit Records in the Relativity Community.

Please contact Relativity Support for assistance with this operation.

## SQL backups

You can set up all tasks mentioned in this document via the Maintenance Plan Wizard in Microsoft SQL Server Management Studio. Other third-party backup tools are available that are easier to manage, have a high compression ratio, and may take less time to complete.

Backup the following to ensure a full recovery of the system, if that becomes necessary:

- Relativity Workspace Databases (.mdf, .ndf) - all relevant databases are of the format EDDS#######

- Relativity Workspace Database Logs (.ldf) - all relevant database logs are of the format EDDS#######

- Relativity System Databases (.mdf, .ndf) - EDDS

- Relativity System Database Logs (.ldf) - EDDS

- Relativity Processing and Native Imaging Databases – INV#######, Invariant

- Relativity Processing and Native Imaging Logs - INV#######, Invariant

- System Databases and Logs - primary, model, msdb (there is no need to back up tempdb)

The Full-Text Engine in SQL Server is fully integrated into the database, and full-text indexes are stored within database files (.ndf), rather than externally in the file system. Back up these files as well if they're in a separate file group.

### Full backups

A Full Backup backs up the entire database. This includes the transaction log so you can recover the full backup.

Creating a full backup is a single operation, usually scheduled to occur at regular intervals. We recommend running a full backup nightly or weekly. Writing to fast storage, maintaining log file sizes, and including backup file compression can help reduce full backup execution time.

Although not required, verifying a backup is a useful practice. Verifying a backup checks that the backup is physically intact, ensures that all the files in the backup are readable and can be restored, and confirms that you can restore your backup in the event you need to use it.

### Differential backups

A differential backup contains all data that has changed since the last full backup. This is known as the base. Differential backups are quicker and smaller than full backups because they contain only what has changed since the previous backup.

You can only restore a differential backup after restoring a full backup. Differential backups provide no point-in-time restore capabilities.

### Transaction log backups

Transaction log backups provide point-in-time restores or point-of-failure restores of databases.

Another advantage of transaction log backups is that SQL Server automatically truncates the inactive portion of the transaction log after it finishes backing up the transaction log. This inactive portion isn't used during the recovery process and contains completed transactions. The active portion of the transaction log contains transactions that are still running and have not yet completed. SQL Server reuses this truncated, inactive space in the transaction log. This prevents the transaction from growing and using more space.

In your hosted instance, you might make full backups nightly and transaction log backups hourly during the day. Other partners may only take full backups on the weekends and differentials nightly, along with transaction log backups during the day. You may have to adjust your backup schedules to accommodate different review schedules.

## SQL recovery models

Recovery models control transaction log maintenance. There are three different types of recovery models you can set at the database level.

The default databases are set to use the Full recovery model. This setting is carried over to any new databases because Relativity performs a full backup and restore operation during workspace creation.

Relativity supports the Simple recovery model for all workspaces. This decision would be entirely dependent on the disaster recovery requirements of your team. The considerations with making this change are detailed in the following MSDN article: http://msdn.microsoft.com/en-us/library/ms189275.aspx .

## Relativity data backups

In addition to the SQL data, we recommend backing up the following items on a regular basis:

- dtSearch and Analytics Index Shares - these can be rebuilt, but the process may take days depending on the amount of data.

- Relativity Web Server Install Directories - back up the the IIS Relativity virtual directories to ensure you can recover any event handlers, custom images, etc.

- Native and Image File Shares - larger Relativity installations can potentially have millions of these files. The storage unit housing these files most likely includes several layers of redundancy. You must decide what backup solution works best for your team.

## Check Database Integrity task

The Check Database Integrity task checks the allocation and structural integrity of all the objects in the specified database. This task executes the DBCC CHECKDB Transact-SQL statement. This ensures that any integrity problems within the database are reported to a system admin to address. For details, see http://msdn.microsoft.com/en-us/library/ms176064.aspx .

We recommend scheduling this task to run weekly. Ideally, you should run this task nightly. The earlier you find any database corruption, the quicker you can address it and reduce the risk of data loss. Unfortunately, this task can be very time consuming and resource intensive on larger databases.

Database corruption is usually caused by the underlying storage. It's important to schedule and monitor this task. If the task completes successfully, then there's no corruption in the analyzed databases.

## SQL table index management

It's important to eliminate table index fragmentation in all Relativity databases. For more information, see SQL Server table index fragmentation .

We developed the IndexOptimize smart script to eliminate index fragmentation and update statistics in all Relativity workspace databases. You can download IndexOptimize in the Relativity Community. Details are included in the comments section of the script. We recommend scheduling this task to run nightly.

See the Index Optimize Maintenance Plan Setup Instructions guide for assistance with setting up and scheduling Index Optimize along with other SQL maintenance plans. This guide is included in the .zip file when you download the IndexOptimize tool from the Relativity Community. If you need a Relativity Community account or assistance with setting up your maintenance plan, contact Relativity Support .

### Updating statistics

The SQL Query Analyzer uses statistics to choose the best path for obtaining data in order to boost query performance.

This task updates query optimization statistics on a table or indexed view. The query optimizer already updates statistics as necessary to improve query plans by default. The Index Optimize maintenance plan includes statistics maintenance as well. The default settings are ideal for most instances, but can be adjusted if necessary. You can also improve query performance by using UPDATE STATISTICS or the stored procedure sp_updatestats to update statistics more frequently than the default updates. For details, see http://msdn.microsoft.com/en-us/library/ms187348.aspx .

Consider updating statistics after performing maintenance procedures that change the distribution of data, such as truncating tables or performing bulk inserts of a large percentage of rows, such as data imports. This can avoid future delays in query processing while queries wait for automatic statistics updates.

For more information on updating statistics to improve query performance, see http://msdn.microsoft.com/en-us/library/ms190397.aspx .

## Database log management

The database transaction log file (.ldf) stores details of all modifications performed on the SQL Server database and the details of the transactions that performed each modification.

### Size management

SQL Server automatically marks the inactive portion of the transaction log for reuse after it finishes backing up the transaction log. This inactive portion contains completed transactions and isn't used during the recovery process. The active portion of the transaction log contains transactions that are still running and have not yet completed. SQL Server reuses this truncated, inactive space in the transaction log. This prevents the transaction from growing and using more space.

We recommend scheduling transaction log backups to occur every hour or less during the day to keep these file sizes in check.

Although you can manually truncate the transaction log, we strongly advise against doing this because it breaks the log backup chain. The database isn't protected from media failure until you create a full database backup. Use manual log truncation only in very special circumstances. You should create a full database backup as soon as it's practical for you. You can truncate and shrink the transaction log file for a database with the following SQL script.

USE EDDS#######

GO

-- Truncate the log by changing the database recovery model to SIMPLE.

ALTER DATABASE EDDS#######

SET RECOVERY SIMPLE;

GO

-- Shrink the truncated log file to 1 GB.

--Specify the correct name of the file

DBCC SHRINKFILE (EDDS#######_Log, 1024)

-- Reset the database recovery model.

ALTER DATABASE EDDS#######

SET RECOVERY FULL;

GO

Transaction logs can present problems because they are often forgotten about until an issue occurs. The log continues to grow as users perform operations within the database. As the log grows, available disk space decreases. Unless routine action is taken to prevent this, the transaction log eventually consumes all available space. If the log is configured to grow indefinitely (which is the default), it consumes all available physical disk space where it's stored. Either scenario causes the database to stop functioning.

Regular backups of the transaction log help prevent it from consuming all of the disk space.

For additional best practices on maintaining SQL Database Log (ldf) Files, see the Managing Relativity SQL Log Files document in the Relativity Community.

### Virtual log file (VLF) management

If you don't pre-allocate database transaction log files, they can become internally fragmented. These files can also become internally fragmented if there are many auto-growth operations.

SQL Server automatically checks for the amount of VLFs in database log files. It then writes a warning event for database logs with an excessive amount.

## Shrink Database task

The Shrink Database task reduces the size of SQL Server database and log files but this does come with a cost to performance. For more information, review the following article Why you should not shrink your data files . Relativity doesn't recommend the shrinking of Relativity workspace databases due to the performance problems associated with doing so.

### Best practices

However, if you still want to shrink a database please consider the following information before running the operation:

- A shrink operation is most effective after an operation that creates lots of unused space, such as an operation to truncate or drop a table. An example would be after a large deletion of documents in a Relativity Case that you don't expect additional loads to happen in the near future. However, be sure to turn off snapshot auditing during the deletion otherwise the audit table will contain a lot of the data.

- Most databases require some free space to be available for regular day-to-day operations. If you shrink a database repeatedly and notice that the database size grows again, this indicates that the space that was shrunk is required for regular operations. In these workspaces, repeatedly shrinking the database is not useful.

- A shrink operation doesn't preserve the fragmentation state of indexes in the database and generally increases fragmentation to a degree. This is another reason not to repeatedly shrink the database.

For more information on shrinking the database, see http://msdn.microsoft.com/en-us/library/ms190488.aspx .

## Job email notification alerts

Job email notification alerts are designed to notify system admins when a SQL job has completed and whether it was successful. It's important to configure these email alerts.

Set up SQL Database Mail on all Relativity SQL Servers and add these notification alerts to all scheduled Relativity maintenance tasks. Configure the alerts to email system admins when jobs succeed or fail. Whenever possible, set the operator’s email address to a distribution list rather than an individual email.

## Relativity applications

You can extend the functionality and features available in Relativity by installing custom applications to workspaces. You can also add them to the application library. You also have the option to uninstall these applications when you no longer need them in your environment. To ensure optimum performance of Relativity, uninstall applications only during off-hours when users aren't actively reviewing documents in any workspaces.

For more information, see Application Deployment System on the Server 2025 Developers site.

On this page

- Managing your Relativity environment

- Workspace management and maintenance

- Analysis of long running queries

- Full-text index management

- Audit record table

- SQL backups

- Full backups

- Differential backups

- Transaction log backups

- SQL recovery models

- Relativity data backups

- Check Database Integrity task

- SQL table index management

- Updating statistics

- Database log management

- Size management

- Virtual log file (VLF) management

- Shrink Database task

- Best practices

- Job email notification alerts

- Relativity applications


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

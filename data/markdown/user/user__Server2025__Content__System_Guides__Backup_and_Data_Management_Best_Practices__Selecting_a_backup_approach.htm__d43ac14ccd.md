---
title: "Selecting a backup approach"
url: https://help.relativity.com/Server2025/Content/System_Guides/Backup_and_Data_Management_Best_Practices/Selecting_a_backup_approach.htm
collection: user
fetched_at: 2026-06-22T06:17:49+00:00
sha256: 196dcfa4e5327284b03d66e42f489691cb2e684011dbc948d8249c51f0cf31bd
---

Selecting a backup approach Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Selecting a backup approach

You can implement one of the following approaches to backing up your data online:

- Active databases

- Inactive databases

## Active databases

Relativity databases may experience a very high number of inserts and updates and can become corrupt at any time. An "active database" experiences moderate to heavy use. For this type of database, data loss would be catastrophic to business.

For your active databases, we recommend using one of the following backup strategies.

- Performing nightly full database backup

- Performing weekly full database backup

- Performing weekly full database backups with no log backups

### Performing nightly full database backup

Follow these steps to perform nightly full database backups with log backups for point-in-time recovery.

Data file:

- Perform a full backup of the database nightly.

- Mirror to remote disaster recovery site. (Mirror can mean log shipping, SAN snapshots, or replication. Follow the established strategies of your business.)

- Restore nightly backup to inexpensive equipment each day.

- Run DBCC CheckDB each day or as often as possible, and meet the business requirements for data loss prevention.

- Complete the DBCC before the next backup occurs.

Log file: Follow best practices for managing log files as outlined in Managing Relativity Log Files . Understand the best approach for timely restoration to meet your recovery time objectives (RTO) and recovery point objectives (RPO).

A Relativity database log file may occasionally experience a high amount of growth. If the log files fill the log drive, those workspaces become inaccessible. If this happens on the SQL Server that contains the EDDS database, the entire environment becomes inaccessible.

### Performing weekly full database backup

Follow these steps to perform weekly full database backups with nightly differentials and log backups.

Data file:

- Perform a full backup the database weekly.

- Perform a differential backup of the database nightly.

- Mirror to remote disaster recovery site.

- Restore nightly backup to inexpensive equipment each day.

- Run DBCC CheckDB each day.

- Complete the DBCC before the next backup occurs.

Log file:

- Follow best practices for managing log files as outlined in Managing Relativity Log Files.

- You should also back up log files as dictated by business needs for point-in-time recovery. This backup should overcome any possibility of filling the log drives.

Relativity may write a lot of data to the log files at times. If the business only requires a four-hour increment for point-in-time recovery, but the system could write enough data to the log files in four hours to fill the drives, then you must either run log backups more frequently, or increase the size of the drives. Be sure that you understand how to restore log files; document the procedure for restoring log files and practice doing it.

The following formula determines the higher bound constraint of frequency of log backups:

- If there is x GB of free space on the log drive, and the system can write data to the system at rate of y GB/hr, and t is time, then the frequency of log backups F is F(t) = b (x/y) . b is given by some integer less than one which is determined by the capability of the system to move data. If this number cannot be maintained at some value b < 1 , then additional bandwidth from production disk storage to backup storage is required. This variable is then the ratio of synchronous read/write where it is some value less than one and represents actual demand on the system, not merely the capability of the system. In other words, the assumption is that the value of b will exist in some domain such that, during normal production activity, the ability of the system to read data from the log disks is not impeded by its write activity.

For example, if during a normal hour of production 100 GB are written to the system and 100GB are read from the disk by production systems, and the remaining capacity is only an additional 50GB of sequential read data, then b= 2 and this is not a value of b< 2 . Log backups may not complete before the next round is scheduled, or the production system performance suffers because you're operating your system at the upper limit of what your system can handle.

Whereas the lower limit of the frequency of log backups is controlled by the need of the business for point-in-time recovery , performing more log may be required by the need to prevent a drive from becoming full.

### Performing weekly full database backups with no log backups

Follow these steps to perform weekly full database backups with nightly differentials and no log backups.

- Perform a full backup of the database weekly.

- Perform a differential backup of the database nightly.

- Mirror to remote disaster recovery site.

- Restore nightly backup to inexpensive equipment each day.

- Run DBCC CheckDB each day.

- Complete the DBCC before the next backup occurs.

- Set recovery model to SIMPLE .

Log file:

In this configuration, set the recovery model of the database to SIMPLE and size the log files appropriately, as outlined in Managing Relativity Log Files . At a minimum, you should set the log files to the approximate size of the Document table. With this approach, you can only restore to the point in time of your full or differential backups, as no log backups are taken throughout the day.

If you suspect excessive logging at any time, please report it to Relativity Support to identify or determine a root cause.

## Inactive databases

Inactive databases also require attention. You may not routinely back up inactive databases, but a stored backup may become corrupted over time for various reasons—such as head crashes, aging, wear in the mechanical storage devices, etc..

Data can become corrupted just sitting on a disk. This is called silent data corruption. No backup can prevent silent data corruption—you can only mitigate risk.

### Preventing silent data corruption

The consequences of a silent data corruption may lay dormant for a long time. Many technologies have been implemented over the years to ensure data integrity during data transfer. Server memory uses Error Correcting Code (ECC), and Cyclic Redundancy Checks (CRCs) protect file transfers to an extent.

It's important to maintain the integrity of data at rest on disk systems that aren't accessed over a long period of time. Without a high degree of protection, data corruption can go unnoticed until it's too late.

For instance, a user attempting to access the database may receive the following error when running certain queries:

Error 605

Severity Level 21

Message Text

Attempt to fetch logical page %S_PGID in database '%.*ls' belongs to object '%.*ls', not to object '%.*ls'.

Then, while running DBCC to try to repair it, the database administrator receives this error: "System table pre-checks: Object ID 7. Could not read and latch page (1:3523) with latch type SH. Check statement terminated due to unrepairable (sic) error."

After this occurs, the database administrator checks for backups, and hopefully recovery happens quickly and inexpensively.

Sometimes, the backup is also corrupt. Often times when this happens, there is no way to recover missing data (e.g., the database can’t be repaired if complete tables have been destroyed.

When DBCC checks are not run regularly against backup files, a corruption such as the previous example may go unnoticed for weeks.

To prevent this data corruption for business-critical databases, the following steps should occur after completing every backup:

- Restore the backup to inexpensive hardware running MS SQL Server.

- Run DBCC CheckDB .

- Create a hash of the database BAK file.

### Example strategy

Follow these guidelines to prevent data corruption of inactive databases:

- Perform DBCC CheckDB against business-critical databases.

- Keep one week’s work of backups.

- Run a file hash each night.

- Ensure that no file hash has changed. (A file that becomes corrupt will have a different hash.)

Freeware tools, such as ExactFile , include features that make it easy to test hash values by creating a digest of a directory of files. This digest can be tested and rebuilt daily or on a sensible schedule that meets business obligations.

On this page

- Selecting a backup approach

- Active databases

- Performing nightly full database backup

- Performing weekly full database backup

- Performing weekly full database backups with no log backups

- Inactive databases

- Preventing silent data corruption

- Example strategy


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

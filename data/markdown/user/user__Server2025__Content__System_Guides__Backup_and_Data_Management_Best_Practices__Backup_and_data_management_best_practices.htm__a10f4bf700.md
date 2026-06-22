---
title: "Backup and data management best practices"
url: https://help.relativity.com/Server2025/Content/System_Guides/Backup_and_Data_Management_Best_Practices/Backup_and_data_management_best_practices.htm
collection: user
fetched_at: 2026-06-22T06:04:46+00:00
sha256: 8c1a59ffd5e1b6f266bdc7f2707d385c34cc5037b1b409ebd877d373b3df7c4c
---

Backup and data management best practices

# Backup and data management best practices

This guide provides an overview of considerations for data recovery and developing a Relativity backup strategy. Often, backup strategies are inconsistent, poorly documented, and misunderstood. This misunderstanding stems from widespread expectations that backups must exist, must be readily available at a moment’s notice, and must be restored immediately, regardless of size. When backup and Disaster Recovery (DR) practices are not documented, management believes that not only do they exist, but that they are good, consistent, and that they are current (possibly up to the minute). It is therefore critical to document your organizations SQL backup strategy and practices.

This guide assumes an understanding of the following technologies: Redundant arrays of independent/inexpensive disks (RAID), tape backup, error checking, hash algorithms, and general security strategies.

To deliver in-depth support for litigated matters, Relativity uses a very compartmentalized approach to database storage. Each individual workspace is set up with a dedicated database.

Relativity also provides processing functionality, which ingests native files into databases. With Relativity Processing installed, each workspace that uses processing has a “sister” store database. These sister store databases begin with the letters “INV” and exist on a separate database server.

Document long text fields and workspace audit history can optionally be stored in Relativity Data Grid rather than in SQL. For more information on backing up this data, please reference Backing up Relativity Data Grid .

## Protecting backed up data

After backing up data, some system admins won't worry about data maintenance. They make the assumption that, once “backed up,” data remains consistent and complete. However, experienced system admins know that databases, and data stored on disk in general, can become corrupted just from sitting on a disk. Further risk is introduced when third-party data synchronization components and snapshotting technologies are used.

For this reason, you must adopt in-depth backup strategies for all business-critical data. All Relativity backups—especially those taken offline—should have multiple BAK copies in different locations, and they should be periodically checked for consistency. For SQL backup strategies, see Selecting a backup approach .

Ultimately, you should protect the data according to business demands. However, consistency checking puts additional strain on both infrastructure and personnel. You must scale these resources according to the acceptable level of data loss based on business requirements.

First, you must determine the mean time to failure (MTTF) of a system. Next, based on the business requirements, you need to determine the acceptable data loss tolerances. Once you fully understand these factors, you can implement the appropriate number of redundant disks to provide a first layer of defense against data loss.

### First line defense

More disks mean greater redundancy. The ability to have data striped across disks improves redundancy. In RAID 1+0, every disk you add increases redundancy. With bit-level striping, bytes are striped across multiple disks. Storage redundancy in RAID is your first line of defense. When a hard drive starts to become corrupt, the storage controller can take it offline. Once it is replaced, rebuild its contents using the non-corrupt contents of other drives. This occurs automatically online.

A successful Data Loss Prevention (DLP) strategy leverages knowledge of MTTF against mean time to repair (MTTR). It has an understanding of disk striping in order to maximize reliability at the online storage layer. For more information on establishing backup maintenance procedures, see Selecting a backup approach .

Backups, or offline data, are another way to mitigate risk. An additional strength of the strategy comes from having multiple copies of a file and the ability to detect a failure of the data before it’s lost. Other countermeasures, such as non-volatile RAM (NVRAM) cache, also help prevent data loss. Such solutions haven't become mainstream yet.

Microsoft SQL Server always keeps the most recent data in RAM and writes the data to disk as load permits. If SQL Server crashes and fails over to a clustered server, the data in RAM on the downed server can’t be recovered. If necessary, assess and adopt NVRAM technology.

This guide outlines several approaches to backing up data and provides information on redundancy maintenance practices. Ultimately, data retention is a business decision. The cost of doing business, profit requirements, and the potential damage of data loss are all business concerns. This guide doesn’t cover disaster recovery options.

For disaster recovery (DR) options, see the Disaster Recovery guide on the Relativity Community. There are many options for replication/mirroring of a site for failover in a Disaster Recovery situation. This document outlines the necessary steps to take after a failover in order to return Relativity to an operating state.

### Second line defense

The second line of defense is nearline data storage. Data is nearline if it can be brought online quickly. For example, your most recent backup file saved on a SAN is "nearline" and immediately accessible . It should be free of corruption.

### Third line defense

The third line of defense is offline data. Offline data can be removed from nearline data in both time and space. For large data, you can manually ship an offline data backup or move it over the Internet over a period of several days. The time differential depends on the following factors:

- Cost of storage

- The value to the business of maintaining large amounts of recent data, offline and far away

- Logistics

For highly mission-critical data, you must synchronize the data on a daily, if not hourly, basis. For example, a disaster recovery data center may be third-line data. To establish a Disaster Recovery (DR) site, you can use technologies such as log-shipping over high-speed Internet or mirroring. There also exist mechanisms with SAN and virtual technologies to keep data that's far away almost up to the minute. This is very expensive and requires tremendous expertise to setup and maintain. It will almost inevitably impact production environment performance.

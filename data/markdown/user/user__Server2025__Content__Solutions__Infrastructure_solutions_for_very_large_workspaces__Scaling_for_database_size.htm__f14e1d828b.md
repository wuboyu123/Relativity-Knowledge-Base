---
title: "Scaling for database size"
url: https://help.relativity.com/Server2025/Content/Solutions/Infrastructure_solutions_for_very_large_workspaces/Scaling_for_database_size.htm
collection: user
fetched_at: 2026-06-22T06:17:34+00:00
sha256: 32957009ec43ef31b70300af941e554bdab15d395f0927b4241dd9d72e034788
---

Scaling for database size

# Scaling for database size

Massive cases require very large databases that can be accessed from a single SQL Server. This page reviews the best practices relating to the SQL Server when workspaces grow to several terabytes.

## Web servers

In some workspaces documents can be larger than average. Large documents may require many coding fields, which increases the size of layouts. When a coding layout becomes excessively large, it places excessive load on the web server. You may need to create more coding layouts and adjust your workflow accordingly.

The size of the document folder tree may also affect performance. Web servers experiencing such a load show large RAM reservations in the Relativity application pool. To alleviate this you can add more RAM, trim the number of folders, or add more web servers.

Large folder counts also increase the time it takes for a workspace to load in the Relativity Desktop Client and in the web browser. To reduce load time, increase the bandwidth available between the load server and the web server as well as to users.

## Audit record management

Depending on the type of review, the following activities may result in the auditRecord table rapidly increasing in size:

- Many overlays of data

- This causes the auditRecord table to increase in sizes equivalent to the size of the data being overlaid, plus any XML overhead.

- Propagation

- When propagation is active in databases with large families, it causes tremendous increases in audit size.

- Deleting

- Deleting is incredibly audit intensive, because Relativity audits all deleted data. Disable snapshot auditing if possible.

When adjusting any level of auditing, it's important to thoroughly communicate the changes and completely understand the repercussions of adjusting audit levels.

## Conversion recommendations

Large documents take longer to convert and use up more bandwidth as they move between the conversion agent, viewer cache location, and web server. Each conversion agent can accommodate up to 100 concurrent users per agent.

There should be no more than two Conversion Complete agents per environment. While only one Conversion Complete agent is necessary, a second may be added to a separate agent server for redundancy.

## Data Grid/Audit

Both Audit and Data Grid provide the following benefits:

- Scalability and more efficient review workflows on case sizes with 100 million or more documents and billions of audits.

- More performant database maintenance, backup, and upgrades.

- A reduction in SQL server database sizes, leading to better performing SQL databases.

Note the following about using the Data Grid File System:

- In very large environments we recommend to use SSDs for Data Grid storage.

- The amount of extracted text in the environment drives the document table size.

- Use Relativity Data Grid to store and analyze extracted text and audit data at massive scale.

- As more data moves into Data Grid, the network bandwidth becomes a bottleneck.

Note the following about using Audit:

- In very large environments the driving factor for large databases are the document audit record tables.

- Audit provides increased visibility into reviewer productivity and system performance.

Use one of the following GB Ethernet configurations for Audit:

- 10GB Ethernet (10GbE)

- Good for environments with moderate to high data traffic and performance.

- 25GB Ethernet (25GbE)

- Ideal for data-intensive applications that require high data transfer rates and lower latency.

- 40GB Ethernet (40GbE)

- Excellent for large-scale Data Grid implementations with very high data transfer requirements.

- 100GB Ethernet (100GbE)

- Cutting-edge, high performance Data Grid environments where maximum throughput is critical to business needs.

## SQL recommendations

In large documents, large extracted text fields can slow the responsiveness of SQL. Large extracted text fields also affect the amount of time it takes to build dtSearch indexes. This can also affect the amount of time it takes to load and update data through the Relativity Desktop Client.

When the amount of data in a table exceeds the available RAM, consider the following:

- Latency is related to disk I/O speeds. A slow database means slower query performance as data loads from disk.

- You can achieve faster queries with more RAM. Consider installing the maximum amount of RAM.

- You can achieve faster queries with more disk I/O.

- Better disks, such as SSD, also improve or eliminate latency problems.

- Lower latency on tempDBs and log files means better overall performance.

- Well-tuned indexes and statistics allow for faster CRUD.

### Common mistakes

SQL Server CPU is precious.Other programs running on your SQL server may be consuming CPU cycles at all times. Be aware of the performance costs of any running applications other than the OS and the SQL engine. These components steal cycles. In addition, you must tightly control user access to SQL. Submit custom queries for DBA review and then schedule.

In addition, avoid these common mistakes when managing a very large workspace:

- Don’t alter instance settings in SQL without knowing exactly what they do.

- Don’t neglect to take database backups and perform DBCC checks. When a workspace is very large, backups may fail for various reasons.

- Remember to manage log files in Relativity.

- Don't keep logs, tempDBs, the full-text catalog, and data files (or any combination of them) together on the same drive.

Large amounts of data in a single table can also slow maintenance. This is because you may need to index many SQL indexes to improve search and sorting performance. Inserts, deletes, and updates all become slower when there are many indexes. You must balance the number indexes against database maintenance performance, and apply indexes judiciously. In large environments, employ a DBA is who understands query optimization and stays ahead of need by understanding the project and its drivers.

Finally, we do not recommend or support use of Microsoft's Database Engine Tuning Advisor’s (DTA) recommendations . All tuning recommendations for very large databases should be reviewed by someone who understands the I/O subsystem, how to use different columns in the database, and whether or not the index actually helps. DTA recommendations are often completely oblivious to the size of the columns it recommends indexing, and can lead to catastrophic results.

Hire a qualified DBA who understands how to manage a rapidly changing database. The DBA should understand the need for proper index management, performance tuning, backups, and DBCC checks.

### Managing indexes

In very large Relativity workspaces, place additional indexes on any fields that require them in the SQL database. This helps to optimize workspace performance for the review team. However, having too many indexes can slow down insert, update, and delete statements. Your team should understand how to analyze the SQL Dynamic Management Views (DMVs) to identify index candidates and those that should be dropped. Note that auto-collected DMV data is flushed with each SQL instance reboot.

To manage your SQL indexes over time:

- Assign responsibility for regular index analysis and maintenance to an internal staff member.

- Set aside some time (weekly or biweekly) to analyze and maintain custom indexes.

### Disks

SQL houses the majority of data reviewers search and tag in a large-scale review. The total size of frequently requested data shouldn't be larger than the total RAM available to deliver that data in a reasonable amount of time.

SQL data should live on the fastest available storage, with the tempDB data and Log files on SSDs and at least 400 MB/s concurrent throughput each on the Data, Log, and FT catalog volumes. This means the server should sustain a cumulative of 1600 MB/sec write. High-performance sequential write speed (cache optimized) may be desirable for backups, but it generally doesn't impact Relativity performance.

For workspaces where the document table and its indexes exceed the size of available SQL Server physical RAM by an unacceptable amount, add additional fiber or iSCI connections to maintain performance levels.

In an environment intended to store many TB of data, data throughput on the I/O subsystem must meet the demands of the application’s capacity to serve the data. If it doesn't meet the demands, users experience a slowdown during review. In cases where disk latency has increased beyond acceptable levels, increase the I/O throughput to the SQL Server to match demand. It’s also important to properly manage SAN cache optimization and manage user expectations when necessary.

Relativity SQL Servers with 512 GB to 2 TB RAM are more common as the amount of data being hosted grows. When workspaces get this large, you must either cache most of the workspace in RAM, or build out an array of very fast disks with high quality I/O throughput. Both approaches are expensive.

### SQL Latency

SQL Server disk write latency should be 20 ms or less. Reads may be a problem if they exceed 50 ms, with 100 ms being a "panic" number. You should always evaluate latency in tandem with SQL wait stats. Some Relativity clients set their system specifications with the goal of less than 15 ms latency on the data drives, (which should be blocked at 64k) and less than 5 ms on the tempDB and log files. Typical latency on the tempDBs, in a well-tuned environment, average less than 1 ms. SQL Server disk read/write latency for translation Log SAN volumes should be 10 ms or less, according to Microsoft best practices. Sequential writers to the translation log can be as fast as 1 ms.

We recommend following the best practices outlined in the Environment optimization guide . You may also choose to work with your storage vendor to configure the device and to ensure that the device is configured for optimal performance. Work with your storage vendor or follow Microsoft best practices to determine where different SQL data should live and how to optimize the cache. Random seeks are best for database data files, while sequential is best for logs. Make these determinations with your vender because different SANs behave differently, and different workspaces and activities may place different demands on the disk subsystem.

Work continuously to ensure that the link between SQL and the storage is configured for optimal performance. Work with your storage vendor to ensure that the multipath I/O (MPIO) is set up correctly and provides optimal performance. This setup becomes much more complicated and less efficient when virtualizing SQL.

Only a Relativity-dedicated team should attempt virtualization of SQL for extremely large workspace(s). The team should include both SAN and virtualization experts. Carefully assess the use of blade servers, because many of them have configuration limitations that adversely impact SQL.

Before going live with SQL in any Relativity environment, test the throughput using CrystalDiskMark or SQL Disk IO (free utilities), lometer, or something similar. If your I/O profile doesn't meet your expectations, performance isn't going to meet end user requirements. For other general best practices, see the Environment optimization guide .

### dtSearch

In a distributed environment, where workers are going to be building an index on multiple machines, verify the throughput of your network. Network problems are the biggest bottleneck for dtSearch builds. When scaling your building, more dtSearch agents equal better performance until your environment reaches an I/O bottleneck.

### Scaling dtSearch workers and search agents

Each dtSearch index worker that lives on an agent machine uses 1 core and up to 1 GB of RAM. For this reason, you must carefully size the dtSearch index worker box. The total size of the index that dtSearch builds for any given batch (dtSearchindexBatchSize) doesn't vary, and is set by default to 250,000 documents. The total RAM required may vary as the size of the documents vary and if the size of the batch is adjusted upward. Start with at least 1 GB of RAM per core, monitor for excessive paging, and then scale accordingly. There can be many unknowns in a very large workspace, which is why this RAM recommendation may need higher than the standard 1 GB/core.

If you experience faster speeds when you increase something, or vice-versa, don't assume that it's good. Changes you make to the size of the sub-indexes to improve performance in one area may adversely impact another. There is also a point of diminishing returns. It’s a balancing act, and the only way to gain mastery of it is to practice, watch, keep records, and know the throughput and latency figures for your environment.

It’s very important that the data set used in a dtSearch build is real data. The presence of many long strings of random characters hurt search performance, as well as the performance of the build and merge process. For more information on dtSearch index building, see Workflow solutions for very large workspaces .

Searches are multi-threaded, and spawn as many threads as there are sub-indexes or cores—whichever number is lowest is the constraint. For example, if you have four cores and eight sub-indexes, you see four cores performing the search. If you have eight cores and four sub-indexes. you see four active cores. If you have two searches running simultaneously against the same index that has four sub-indexes, and you have eight cores, you see eight active cores.

An instance setting controls the default size of the sub-index. You can adjust this per each index creation through a setting on the index creation configuration screen. The default value is 250,000 documents.

The dtSearch agent is not throttled. If you put one search agent on a server with eight cores, it uses all of them as load demands. Set up a dedicated dtSearch Search Agent Server if you know you have cases that have multiple (more than one or two) sub-indexes that have multiple searches executed against them. You aren't limited to just one search server, either. If you have five, four-core search servers in the resource pool, that’s 20 cores total.

The amount of hardware needed to support the dtSearch architecture is highly subjective. For example, if you set your sub-index size to be 250,000, and none of your indexes have more than 250,000 total records, then you never have a dtSearch that multi-threads. In other words, multiple processes never search a single sub-index. Additionally, cores aren't process bound—for example, while waiting for an I/O response, a single core may go off and do other things. dtSearch is highly I/O bound and the first bottleneck encountered is I/O, and not CPU.

So how do you know when to scale? For the moment, our recommendation is that you understand your existing tier, and then deploy per these recommendations (you can determine your level by referencing the System Requirements .

Data centers that host larger workspaces will likely have a very robust infrastructure. With enterprise grade I/O, faster CPU, and industrial strength bare metal, single agents to tackling larger batches of documents may be preferable. For workspaces with 15m + documents, a batch size of 500k may be preferable. There is no substitute for experience, so be sure to test with different batch sizes in a quiet environment, and discover where the sweet spot is.

With the dtSearch grid, you can have additional search agent machines, so it may make sense to spread shares, indexing agents, and searching agents out across a wider footprint to improve network latency, as sub-indexes can only live on network shares. Using local drive letters isn't supported.

### Other

Files (natives and images) and dtSearch/Analytics indexes can live on slower, tier-3 (SATA) storage. A NAS is often used to serve up the files. Alternatively, you can set up a VM as a file server and connect it to a SAN.

### Database maintenance

For even the largest, most active workspaces, it’s important to set aside some time each day for maintenance. Key maintenance tasks include the following:

- Eliminate index fragmentation each night.

- Update statistics each night.

- Set Auto Update Statistics for the database to On.

- Back up the transaction log for the database at least once an hour. This way the database can reuse the file and limit auto-growth.

- Either conduct full backups nightly or conduct full backups weekly with nightly differentials.

- Schedule database integrity checks to run weekly.

- Set all maintenance jobs to send email alerts on completion or failure of each task to more than one person.

## Workflow and searching

There are three main methods of searching in Relativity. Each method encounters challenges in environments with very large search sets and document counts.

### Keyword search (full-text index)

The Search Conditions search textbox searches all fixed-length and long text fields that have Include in Text Index set to Yes. Marking a field with this property adds the field to the full-text catalog indexes in SQL. Relativity can then use the contains operator to search that field.

Keyword searching is different from other Relativity search methods. This is because the SQL Server, by default, begins to populate the full-text index as soon as it detects new data. In certain circumstances, this consumes an unacceptable level of resources. For example, if you add 30 fields to the index simultaneously, the environment could suffer severe performance degradation. Or, if millions of documents are loaded into an environment that has many fields in the catalog, the resulting build may strain the available resources.

When users import data into one of the indexed fields or add or remove a field from the full-text catalog in a very large workspace, it triggers an automatic operation to update the catalog. If there is a large number of indexed fields in the catalog and many new records (perhaps as many as 1 mm per hour), the integrated full-text service (iFTS) experiences load.

Updating data in indexed fields also triggers an update of the index. In very large workspaces, this can be slow and taxing. To avoid potential document table locking and other performance issues, consider the following:

- Limit the number of fields added to this index to 20 or fewer, if possible.

- Schedule a nightly job to update the full-text catalog.

- Use dtSearch when possible.

- Move the catalog to separate drives.

- Delay the full population until an off-peak time when you create a full-text index. This is especially important if the base table of a full-text index is large.

- Disable automatic track changes of the full text catalog. Instead, schedule a job to re-enable automatic mode after the load completes. As a result of this, changes made to any fields in the catalog don't appear in search results until the following day, unless you manually trigger an update.

For instructions on how to stop automatic population, see the following Microsoft article: http://msdn.microsoft.com/en-us/library/ms142575.aspx

### SQL Searching

Relativity offers users the ability to create and execute ad hoc SQL searches. These searches may hit against date columns, email fields, custodian data, and various single and multi-choice fields. Often, these queries can be very complex, poorly indexed, and poorly performing. A combination of sizing the environment properly and ensuring a good SQL indexing strategy provides a certain level of comfort.

This is because indexed searches always perform vastly better than non-indexed ones. Additionally, for better performance, using multiple files for heavy use objects alleviates disk I/O pressure.

### Analytics

Contact Customer Support to work with our Analytics experts to implement best practices for a large workspace index.

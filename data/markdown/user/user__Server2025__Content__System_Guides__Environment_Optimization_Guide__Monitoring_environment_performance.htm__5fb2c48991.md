---
title: "Monitoring environment performance"
url: https://help.relativity.com/Server2025/Content/System_Guides/Environment_Optimization_Guide/Monitoring_environment_performance.htm
collection: user
fetched_at: 2026-06-22T06:17:58+00:00
sha256: 1f17f4558d1a23abfa36ab1d47d29deaa201c754af03c9792a1884a7aefb6126
---

Monitoring environment performance Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Monitoring environment performance

The hardware and software hosting the instance must be healthy to provide an exceptional Relativity experience. To ensure that your environment is healthy, review the following performance considerations.

## Windows and SQL Server log analysis

Regularly monitor Windows and SQL event logs. These tools can automatically email your IT team when warnings or errors occur. This type of monitoring is often overlooked by IT administrators. It's important to actively monitor these logs on a regular basis in the environment.

There are many tools available to monitor and notify system admins of any issues that arise. It's crucial that all Relativity servers are monitored for the following:

- Available disk space - Alert system admins of low disk space on any Relativity server.

- Server availability - Alert system admins if any server becomes unresponsive. This is accomplished with simple internal ping tests.

- Website availability - Alert system admins if the website becomes unavailable.

- Resource utilization - See Resource utilization .

## Resource utilization

Monitoring resource utilization is a more involved process. Using this process, you can identify bottlenecks and anticipate when it might be time to scale or adjust the environment. The license agreement doesn't limit the amount of hardware or Relativity roles you can add to an instance; you can make adjustments as needed.

Monitor processor and memory utilization across all servers. Note that SQL always shows high memory utilization because it stores as much as it can in memory. It's important to identify any SQL Server storage bottlenecks, which includes the disks or the connection to the disks.

Best practices for monitoring resource utilization include gathering benchmarks at different times of the day. This determines what the acceptable ranges are for the performance counters you intend to monitor. Create this baseline so you can compare it to results as the environment continues to grow. Third party monitoring tools often simplify the gathering and summarizing of performance related metrics. Summarizing this material assists your team to more easily identifying when it might be time to scale one or more areas of the system.

It's difficult to provide specific thresholds or recommendations for performance counters as every environment is different.

### Monitoring disk usage

Disk latency is the fundamental measure of disk performance.

- The Avg. Disk/sec Read and Avg. Disk/sec Write counters of the Windows Performance Monitor “Logical or Physical Disk” Objects. You can use these to measure disk latency.

- SQL Server Avg. Disk/sec Read latency should generally be 20ms or less per Microsoft best practices for database volumes. However, 100ms or less is more realistic in environments with traditional storage media. Our clients can take advantage of more recent developments in flash and solid storage.

- SQL Server Avg. Disk/sec Write latency should generally be 3-5ms or less per Microsoft best practices for transaction log volumes. However, 20ms or less is more realistic in environments with traditional storage media. Keep the I/O response times on SQL database log files as low as possible.

Monitor the SQL Server tempdb system database in Relativity environments. This often becomes a bottleneck for many of our larger clients. It's more common for clients to store the tempdb database for each SQL instance on flash or solid state storage instead of traditional, spinning media.

The following table provides additional suggestions for optimal SQL Server disk latency.

Object Counter You Want Description

Physical disk Avg. Disk Sec/Read < 8 ms A key measure of disk latency representing average time, in milliseconds, of each read to disk where >20 is poor, <20 is good/fair, <12 is better, <8 is best

Physical disk Avg. Disk Sec/Write

< 8 ms (non-cached)

< 1 ms (cached)

A key measure of disk latency representing the average time, in milliseconds, of each write to disk where non-cached writes (>20 poor, <20 fair, <12 better, <8 best) differ significantly from cached writes (>4 poor, <4 fair, <2 better, <1 best).

For OLTP databases, the lower this number the better, especially for disks holding the transaction log.

For additional information on monitoring for Disk I/O bottlenecks in a system, see http://msdn.microsoft.com/en-us/library/ms175903.aspx .

The disk queue counters aren't usually helpful since they require that you know how many spindles are included in an array as well as any available caching or auto-tier mechanisms.

It's also very important to ensure that the link between SQL and the storage is configured for optimal performance. Work with your storage unit provider to ensure that the pathing is set up correctly and provides optimal performance. This setup becomes more complicated when virtualizing SQL. Other performance objects typically monitored for SQL include several memory counters.

Page life expectancy can indicate if SQL has enough memory available to perform optimally. Lower values during regular operations suggest a need to install more memory. A popular suggested threshold for this counter is 300 seconds, which is often far too low. A more realistic value can be determined by performing this equation (DataCacheSizeInGB/4GB *300).

For more information, see https://www.sqlskills.com/blogs/jonathan/finding-what-queries-in-the-plan-cache-use-a-specific-index/ .

In addition to other available tools, you can log these performance counters using the Windows Performance Monitor in Windows Server.

## Analytics performance considerations

Use the following guidelines to ensure that the analytics operations perform quickly and efficiently in your Relativity instance.

### Server requirements for index builds

Server memory is the most important factor in building an analytics index. The more memory the server has, the larger the datasets can be indexed without significant memory paging. Use the following equation to estimate how much free RAM on the analytics server is needed to complete an Analytics index build:

(Number of training documents) * 6000 = RAM required (bytes)

This equation is based upon the average document set in Relativity. If the dataset has more unique terms than an average dataset, more RAM is required to build the index.

The analytics index creation process also depends on CPU and I/O resources at various stages. Ensuring that the analytics server has multiple processors and fast I/O increases efficiency during the build process.

### Memory requirements for querying

When an analytics index has queries enabled, the index is loaded into RAM in an lsiapp.exe process. For indexes with millions of documents, this RAM requirement can be thousands of MB. The RAM requirement is dependent upon the number of unique terms in the dataset. Therefore, the range of RAM needed for an index to be enabled is as follows:

- (Number of searchable documents) * 5000 = High end of RAM required (bytes)

- (Number of searchable documents) * 400 = Low end of RAM required (bytes)

It's a best practice to Disable Queries on any analytics index that isn't used. This frees up RAM on the analytics server, and you can re-enable them instantly.

### Server requirements for structured analytics

Structured analytics operations execute using the Java process on the analytics server. Ensuring that Java has enough RAM prevents restarts of the service or out of memory exceptions. You should also optimize the agent server to ensure that the export and import processes are as fast as possible. Ensure there are multiple Structured Analytics Worker agents. It is recommended to have, at minimum, 4 worker agents. Make sure that each worker agent has at least 1 GB RAM and 1 processor core available.

The structured analytics process also depends on CPU and I/O resources at various stages. Ensuring that the analytics server has multiple processors and fast I/O increases efficiency during structured analytics tasks.

### Relativity Processing

When scaling Relativity Processing Worker machines horizontally, it's equally important to scale the storage if you want to continue to see linear improvements in performance. It doesn't help to put 20+ worker machines online if your storage system doesn’t have the available IOPS and throughput to support them.

Relativity Processing is an application you use to ingest raw data directly into your workspace for eventual search and review without the need for an external tool. A processing job consists of two parts, file discovery, and file publishing.

#### Discovery phase

During the discovering phase, the Relativity processing engine begins to ingest the files you specify in a processing set, and then OCR and/or text extraction are performed on those files.

Observations / Recommendations:

- During this phase, the only real shared resource is the file share.

- Depending on the storage subsystem, the source directory for the processing engine probably shouldn't be the same as the file share hosting Review.

- Excessive read I/O from the file share hosting Relativity natives and images required for review may increase Relativity viewer response times.

- The same is true of the destination directory.

- Excessive write I/O to the file share hosting Relativity natives and images required for review may increase Relativity viewer response times.

- For workspaces where you will use processing, ensure the default file share is on separate storage from the rest of the files. If this is not possible, thoroughly test the I/O capabilities of the storage subsystem. This ensures that these operations don't negatively impact Review.

#### Publishing phase

At any point after the completion of file discovery, you can publish the files that have been discovered in the processing set. During the publishing phase, the processed documents are made available for review via the workspaces document tab.

Observations / Recommendations:

- There is almost no contention on the file share as expected during this phase.

- There is some SQL contention as data is inserted into the workspace database.

- SQL processor utilization increases during the publishing phase.

- The SQL TempDB experiences increased usage, but no worse than a standard Relativity data import via the Relativity Desktop Client.

## Marvel

All Relativity users who implement Data Grid can receive Elasticsearch Marvel licenses. Use Marvel to view your cluster status in a simple, single pane overview; investigate highly detailed system metrics; visualize cluster events and metrics together to analyze how changes affect performance; and access the REST API.

See Marvel for more information.

## Head

Head is a plugin for Data Grid that displays the overall cluster health, the different indexes residing in that cluster and the shards of the indexes. Using this plugin, you can quickly check on the health of the cluster.

See Head for more information.

## SQL Server table index fragmentation

This section outlines the fragmentation of the SQL table column index, and describes how to eliminate it to ensure optimal system performance.

### SQL table indexes overview

SQL table column indexes help improve system performance by reducing the amount of I/O (disk read and write) operations necessary to retrieve data.

These indexes speed up queries by providing quick access to data without the need for full table scans. A full table scan occurs when SQL has to read every row in a table to obtain the information it's querying. Each Relativity database contains many indexes to help ensure optimal performance. It's important to maintain these indexes throughout the life of a workspace.

### Index fragmentation

Fragmentation occurs through the process of data modifications (INSERT, UPDATE, and DELETE statements) made against the table and to the indexes defined on the table. Because these modifications aren't ordinarily distributed equally among the rows of the table and indexes, the fullness of each page can vary over time. For queries that scan part or all of the indexes of a table, this kind of fragmentation can cause additional page reads and slow performance.

This information was provided by the following Microsoft article: http://msdn.microsoft.com/en-us/library/ms188917.aspx .

### Effects of fragmentation

If heavy fragmentation exists, performance is degraded and Relativity responds slowly, resulting in timeouts across various parts of the application. This includes searches, views, updates, deletes, data imports/exports, etc. Often a highly fragmented index can be worse than having no index at all.

### Removing fragmentation

We designed a smart script named IndexOptimize that eliminates index fragmentation in all Relativity workspace databases. IndexOptimize is available for download in the Relativity Community. Details are included in the comments section of the script.

For instructions on setting up this SQL job, see SQL table index management .

Alternatively, you may wish to create a custom job that meets your specific needs.

We recommend scheduling IndexOptimize to run nightly.

On this page

- Monitoring environment performance

- Windows and SQL Server log analysis

- Resource utilization

- Monitoring disk usage

- Analytics performance considerations

- Server requirements for index builds

- Memory requirements for querying

- Server requirements for structured analytics

- Relativity Processing

- Marvel

- Head

- SQL Server table index fragmentation

- SQL table indexes overview

- Index fragmentation

- Effects of fragmentation

- Removing fragmentation


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

---
title: "Scaling for document count"
url: https://help.relativity.com/Server2025/Content/Solutions/Infrastructure_solutions_for_very_large_workspaces/Scaling_for_document_count.htm
collection: user
fetched_at: 2026-06-22T06:21:03+00:00
sha256: 436ef6d7dabf018a2c39d71d0607c6fa24007de5b1d9d935503ffd5e24173053
---

Scaling for document count Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Scaling for document count

Multi-million record cases present some unique management challenges. This page reviews the primary areas that need special attention when dealing with workspaces that contain many documents.

## Web servers

Consider the following best practices when scaling your web servers for cases with very large document counts.

Thoroughly test any custom scripts or assemblies to verify that they can handle a workspace of this size.

### Web API

When loading documents into a workspace:

- Ensure that you’re running in Direct Mode and that the loading server is close to the Relativity farm.

- Use the 64-bit version of the Relativity Desktop Client (RDC).

- Design the workflow so that you can load with pointers.

- Understand that a heavy data load causes heavy SQL load. This can impact the review.

- Consider using workflows that can separate non-indexed data, and run the full-text service in an automated fashion.

- Use one or more dedicated loading servers.

- Verify the connection speed between all servers involved in loading data.

- Ensure that the URL of the webAPI doesn't route through any other devices, such as a firewall.

- Do NOT load ExtractText first.

SQL stores up to the first 8000 characters of all Long text (nvarchar(max)) fields on-row. This means if you load ExtractedText first, any document that contains less than 8000 characters Relativity stores on-row. Any subsequent long text fields you load, may roll off-row and the ExtractedText column, reside in two different locations on disk.

Entries that are less than 8k are on-row, and ones that are greater are off-row. This means that any operations that attempt to sequentially read large amounts of ExtractedText, for things like index builds, become random seeks. Random seeks perform far more poorly than sequential reads. Having a DBA on staff that understands these types of data mechanics is essential to ensuring the smooth operation. This also ensures you achieve efficiency of large sequential reads and writes.

To increase the speed of loading, add additional RDC instances. However, too many RDC instances cause degradation of the load and can ultimately lead to failure.

We recommend limiting this to four concurrent imports at a time into one workspace.

Due to auditing, it’s always faster to append (insert) data than to overlay (update) existing data. Appending doesn't audit the entire record, but overlays create an audit of the data as it existed both before and after the change. If you perform an overlay, ensure that you first index the overlay identifier in SQL. Typically, someone who has been tasked with managing SQL, such as a DBA, performs this task.

After a large data set is added to a table in the SQL database, the ongoing performance of inserts and updates to the table depends on the health of its indexes and the concurrence of its statistics. At certain points, you may need to run maintenance with online index builds while loading data.

### Relativity.distributed

An environment with many millions of documents typically has hundreds of reviewers. See Scaling for number of users for information on scaling for large numbers of users.

One way to deal with both a large number of users and large documents is to set the case up with its own download handlers. To establish a dedicated domain of web servers for a case, set the download handler to a network load balancer, or other type of single-point access hardware or software load balancer that allows for sticky sessions.

In cases with extremely large documents, requests to the Relativity.distributed service queue, and you can download multiple docs simultaneously. However, when you queue many large documents, they all consume bandwidth, which eventually becomes saturated. For this reason, configuring a single download handler may not be sufficient.

Monitor bandwidth carefully. High latency on an otherwise close web server is a strong indicator that the server is under-powered or that its connection is saturated. You may need more servers.

User behavior can be as important as the number of users. A single user can perform actions that increase the load on the web server more than expected. Scale according to load as well as user count. The following common user actions can substantially increase the load on the web server:

- Many simultaneous windows or unnecessary opening and closing of windows

- Frequent and large printing jobs

- Frequent mass operations

- Frequent deleting

While some of these operations are sometimes necessary, all users should consider how their actions may impact the current load in an environment when they kick off large operations.

### Folders

A large numbers of folders may cause memory pressure on the web server. To alleviate this, either increase the RAM or decrease the number of folders. Extremely deep folder structures can also cause very long scan times. Excessively large strings (more than 2,097,152 bytes) cause serialization errors.

### Layouts

Very complex layouts with many choices and fields don't perform as well as simpler layouts that target more-specific coding. Complex layouts place a rendering load on the web server and a heavy query load on the SQL Server. Use popup pickers for fields with a large number of choices.

## Conversion recommendations

The Conversion Agent handles most of the actual work for a conversion request. More documents in the environment means more conversion requests made to the conversion agents. Conversion agents scale around 100 users per conversion agent, similar to conversion workers.

There should be no more than two Conversion Complete agents per environment. While only one Conversion Complete agent is necessary, a second may be added to a separate agent server for redundancy.

When documents are converted Relativity saves a copy of the document in the Viewer Cache location. You can warm the cache location by performing a Mass Convert mass operation. This pre-converts a large set of documents into HTML5 format before review. By using mass convert you can eliminate document load time in the viewer.

You can create as many cache locations as you need. For workspaces with a large amount of documents we recommend creating a new location for each workspace.

## SQL recommendations

### SQL Enterprise Edition

The Enterprise Edition of SQL offers many features that assist with the operation and performance of an environment that meets or exceeds very large workspace conditions.

### Maintenance plans

Maintenance is a critical operation in a busy SQL environment. Failing to run maintenance results in extreme performance declines followed by catastrophic failures of many core activities in Relativity. For more information on configuring SQL maintenance plans, see How to Setup Index Optimize - SQL Server Maintenance Plan .

### Index strategy

It’s not uncommon for a single document table in a very large workspace to have several hundred fields. In such cases, you can often improve query performance by adding indexes. However, be careful that the number of indexes doesn’t become excessive. Extreme slowness may occur in any workspace that has dozens of indexes. You must update all indexes whenever data changes, including both updates and inserts.

You should plan indexes and put a strategy in place to manage them. This strategy should ensure that you evaluate the usefulness of the indexes and remove unused indexes.

We recommend a robust test environment. SQL Server Management Studio provides a Database Tuning Advisor (DTA) tool that can be very helpful. Environments that are hosting very large workspaces should never run the DTA in production. Run the tool against a copy of the database in a development or test environment.

Finally, don’t simply accept the Microsoft Database Engine Tuning Advisor’s (DTA) recommendations. You should fully understand the results of the DTA before you apply them. Some recommendations that the DTA makes might not improve performance and may cause a large resource drain as you apply recommendations. Avoid duplicate indexes, and remove old, stale indexes you're no longer using.

Someone who understand the I/O subsystem should review all tuning recommendations for very large databases. They should also understand how different columns in the database are used, and whether or not the index will actually help.

Hire a qualified DBA who understands how to manage a rapidly changing database. The DBA should understand the need for proper index management, performance tuning, backups, and DBCC checks.

### Monitoring utilities

There are number of third party software packages that provide SQL monitoring. These applications can provide valuable insight by collecting information on an ongoing basis. They gather information pertaining to page life expectancy, long running queries, CPU load, RAM use, blocking, and deadlocks. These applications gather and present this information in user-friendly charts and graphs.

Take care to use a reputable tool because such utilities can have a significant impact on the environment. Microsoft SQL Server comes with a very feature-rich set of Database Management Views (DMVs). These are views that are already managed and maintained inside of SQL. In fact, software designed to monitor SQL runs scripts that query these views. A DMV gathers the following useful metrics:

- Latency by data file

- IO by file

- Longest running queries

- Queries by CPU

- Objects in RAM

The Relativity performance testing team uses a tool called Load Runner to benchmark Relativity, but hosts who seek to truly push hardware performance threshold should seek to perform their own tests. Relativity provides no load/stress testing tool that integrates with the application.

On this page

- Scaling for document count

- Web servers

- Web API

- Relativity.distributed

- Folders

- Layouts

- Conversion recommendations

- SQL recommendations

- SQL Enterprise Edition

- Maintenance plans

- Index strategy

- Monitoring utilities


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

---
title: "Infrastructure solutions for very large workspaces"
url: https://help.relativity.com/Server2025/Content/Solutions/Infrastructure_solutions_for_very_large_workspaces/Infrastructure_solutions_for_very_large_workspaces.htm
collection: user
fetched_at: 2026-06-22T06:04:53+00:00
sha256: 6bb86c83a86f8ea9da7c76c3b464845286ea6962a53adc70f027e8d2acee9d21
---

Infrastructure solutions for very large workspaces Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Infrastructure solutions for very large workspaces (VLRW)

This guide explains the best approach for identifying and fixing problematic Relativity workspaces. Typically, these workspaces are very large and likely exhibit symptoms due to one or more of the following conditions:

- Number of users – the number of users relates to the total concurrent connections to the database. Experience has shown that scalability issues begin when a client scales up to 200 users. This often occurs very suddenly.

- Document count – a database is considered “large” if it has more than 1 million records and a server that hasn't scaled to accommodate it. Very large workspaces may contain more than 15 million records.

- Database size – the total size of all of the databases (tables and indexes) on a single server that may be accessed simultaneously. This may cause excessive calls to disk and result in poor performance. Typically, this begins when this size exceeds 150 GB over the total amount of RAM available to SQL, and the disk subsystem can't keep up.

This guide provides scalability best practices for each of these three conditions. These guidelines can help infrastructure managers understand how to scale environments for very large Relativity workspaces (VLRWs).

"Successful" environments have average long running simple queries of less than two seconds.

For the purposes of this guide, a database can be considered a VLRW when it begins to warrant the support staff’s attention and when it puts pressure on the system it’s occupying. Measures must be taken to alleviate the pressure.

The scaling approach should balance the activity in a database against its size, number of users, and underlying environment. To help make the recommendations useful, we evaluate VLRWs by size and by the symptoms its host exhibits. Symptoms are caused by data size, the number of records, and the number of users.

In general, you should be most concerned with performance when you observe the following:

- The amount of data that SQL tries to read into memory approaches an amount that results in long running queries and complaints from users.

- Due to heavy requests, file and disk latency exceeds standards.

- User complaints increase.

- Query durations increase.

There are several factors that you must consider when determining the minimum system requirements needed to support an environment that may reach many terabytes in size. For more information about the systematic causes of infrastructure pressures, see Identifying the need to scale .

This page contains the following sections:

- Identifying the need to scale

- Scaling Relativity

See these related pages:

- Scaling for number of users

- Scaling for document count

- Scaling for database size

- Infrastructure checklist for very large workspaces

## Identifying the need to scale

Note that these criteria only apply after all best practices have been verified as executed, and any other potential source of trouble has been eliminated.

### Preliminary considerations

Any database can be overwhelmed by excessive queries, index builds, overly complex searches, and too many users. The following issues may bloat a database unnecessarily or cause poor responsiveness:

- Audit record growth

- Schema changes, such as adding and removing fields

- Slowness caused by too many fields added to the full-text catalog

- Index builds causing considerable drag

- Excessively complex searches

- Large number of folders

- Unauthorized actions or poorly controlled actions on a database server

You should resolve these issues prior to purchasing additional equipment. Ultimately, user demand-driven scaling only temporarily appeases users’ needs, which scale in tandem to your efforts.

#### Are you at capacity?

Many SANs and servers may possess untapped CPU sockets, RAM buses, and internal disk configurations. Prior to purchasing new equipment, determine whether or not the existing equipment meets requirements.

For example, SQL Server connected to a SAN via only four iSCSI ports when there are 16 available is perhaps only operating at 25 percent of its potential. However, keep in mind that as systems become busier, their ability to ingest additional load decreases at an inverse rate.

This guide provides performance solutions for each of the relevant hardware arenas, including network, storage, RAM, and CPU. Solutions are addressed in terms of users, record counts, and database size. For example, assume you're operating at capacity, there's no more room for additional hardware, and network traffic (inter-server communications) attributed to Relativity is necessary.

No one condition creates a VLRW. Rather, several factors converge to create a critical mass event in your infrastructure. You might not even realize that you have a VLRW until you begin to experience problems. In fact, a single document table that contains 1,000 records may require the same level of attention as a database that houses 10 million or 100 million rows.

## Scaling Relativity

In a small workspace, data exists in discrete, known quantities. Basically, the data "fits" in the environment in terms of disk I/O and memory use. It is then balanced against raw processing power and network transfer speeds to create the perception of a "fast database."

In such an environment, storage, RAM, and processing power come together well and are appropriate to the case. At the center of this "fast" environment are two main points of concern:

- The largest Document table

- The largest auditRecord table

Much of this guide has focused on how to handle the various types of load placed on these objects. While other objects may require equal consideration, these two objects will nearly always exceed any other object in size and use. These two tables are the two objects to which the entire environment must be tailored.

To scale Relativity efficiently, we must account for the purpose behind each of these large objects. The Document table serves as the repository for all document metadata for one workspace, as well as some types of coding fields. Other coding data and object data exist in other tables, such as the zCodeArtifact_###### and File tables. The auditRecord_primaryPartition table serves as a case-level repository for all activity and changes that occur to the workspace.

If either reaches a certain tipping point, then you must adjust the infrastructure and not the product. The primary bottleneck on a single machine is almost always throughput from SQL to the disk or SAN. Whatever SQL can't store in memory, it needs to grab from storage. A workspace that contains a document table and/or an audit record of a size where many queries begin to exceed the tipping point will require significant scaling of its I/O and RAM.

### Tipping point

MS-SQL tries to keep as much of the database in RAM as possible. Information in RAM always represents the most recent change data. People are usually surprised by how much RAM SQL consumes and the massive I/O churn they may experience. The briefest explanation is that the operating system reads data from disk in certain sized chunks, and, at a certain percentage of estimated rows to be returned, SQL decides it's more efficient to read everything from disk in a large "scan" operation, and then perform searching operations against all of the data, at once, in memory. It does this because it decides that it's more efficient to perform one large read, as opposed to doing many short reads.

The question becomes, then, how long will it take to pull x amount of data (GB or TB) from the storage subsystem? Longer than 2 seconds? How many search queries are selective enough to leverage an index rather than performing a scan? Microsoft Fast Track requirements detail these types of scenarios in detail for participating hardware vendors, including Dell and HP. The expense required to deploy the Fast Track recommendations may be prohibitive, but they do provide a list the equipment required to support these types of huge data sets.

We consider any document query that runs longer than 2 seconds to be a long-running query.

To support large SQL operations, offload as much of the I/O to local PCI-E flash or SSD wherever possible. For instance, Fusion-io cards could be used to house the tempDB data files and/or database log files.

#### SQL tipping point

The SQL tipping point is much lower than most people think, which is why SQL needs so much RAM. Operating systems read data from disk in certain sized chunks, and if SQL decides it needs to read in every sector, it scraps the index and reads it all into RAM. When queries are not "selective" enough to satisfy this requirement, this is when SQL will convert an efficient index seek to a scan. An index scan is bad because it reads in the entire index.

Scans can happen for any number of reasons, non-selectivity being just one of them, and certainly if a non-selective query is written with the intent of exploring data, as often is the case in searching work, then such scans cannot be helped. The easiest way to determine if an index scan is occurring due to selectivity is by forcing the query to be more selective, and observe the query plan.

An index scan that occurs when a large date range is selected should convert to an index seek when a single date is selected. If it does not, then there is something else wrong with the index or the query is beyond the scope of this document.

SQL stores the data in a table in a physical way on disk. This data is ordered by and on a clustered index. A clustered index scan should be avoided at all costs. By prohibiting activities that trigger clustered index scans, or by planning for them, large amounts of data can be stored. Many non-clustered indexes can be stored in RAM far more easily than a single Document table numbering in the Terabytes, so care should be taken to either purchase enough RAM for large clustered index scans, or to prohibit and engage in a campaign of testing and planning searches and indexing.

On this page

- Infrastructure solutions for very large workspaces (VLRW)

- Identifying the need to scale

- Preliminary considerations

- Scaling Relativity

- Tipping point


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

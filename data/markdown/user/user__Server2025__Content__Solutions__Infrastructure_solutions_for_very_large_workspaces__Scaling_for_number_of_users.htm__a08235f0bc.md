---
title: "Scaling for number of users"
url: https://help.relativity.com/Server2025/Content/Solutions/Infrastructure_solutions_for_very_large_workspaces/Scaling_for_number_of_users.htm
collection: user
fetched_at: 2026-06-22T06:21:05+00:00
sha256: 18e8848d11975244cef503f110e3151d7accac8c0f51f75cc42e583f61aa509f
---

Scaling for number of users

# Scaling for number of users

When a workspace has a large number of users, you must scale the environment to the large number of concurrent connections to the database. This page reviews important considerations and best practices for scaling workspaces with many users.

## Web servers

While a SQL Server is very sensitive to the size of the data tables it hosts, web servers are very sensitive to the number of users. The primary method of scaling Relativity web servers is to add more web servers.

The web server is the first line of defense against system saturation. A surge in review often causes a need for additional web resources before any other server begins to feel pressure. While web servers are usually the first to show signs of stress due to a large number of users, a large user load could also strain SQL.

### Application pools

Relativity enhances scalability through the use of application pools. By creating purpose-driven pools, you can move services that become resource intensive and redistribute them. The three main application pools are listed below, along with the user activities that place load on the server:

- Relativity.distributed

- Large documents or frequent document viewing (offload specific, heavy cases to single servers, or offload to a near-proximity web and file server for geocentric user populations).

- Many users in a distant location cause high latency

- RelativityWebAPI

- Importing many load files through the Relativity Desktop Client (RDC) concurrently (offload to a dedicated import/export server)

- Relativity

- Large, complex coding layouts (offload with RULB and NLB to create a server farm)

- Offload to a hardware load balancer that supports sticky sessions.

- Event handlers

- Extracted text in large item list views (list view set to 1,000)

- Large, complex folder views and choice trees

You can move the following functions (by offload) to separate servers. Ultimately, the best approach is to add more web servers and to implement a proper load balancing strategy. Relativity comes with the built-in Relativity User Load Balancer, but you must configure it. If a particular workspace has a latency issue, set up a separate web server to act as a download handler. You can easily configure this at the workspace level.

### Download handlers

Typically, infrastructure managers build Relativity web servers into a single, load balanced farm. To offload the strain incurred by a single workspace with many users, it's common to use a different case download handler for just that workspace. You can then dedicate a web server that you can scale vertically.

When under load, Relativity web servers respond well to scaling either up or out. In other words, either increase the RAM and CPU allocation to the existing web servers, or add more web servers. Load balancing is also a great way to maximize computing resources, but you must take care in certain areas.

### Load balancing

Load balancing applies to the following categories:

#### Physical

Successfully implement physical devices to physically load balance web servers. It’s important that the physical device not interfere with, rewrite, or otherwise alter the actual web calls made by the Relativity.distributed service.

Physical devices must use IP affinity. Users can't migrate to less loaded servers after logging on to the server. Note that Relativity doesn't innately support physical load balancers. While we can provide advice on Relativity and authentication, you should contact the appliance vendor regarding any problems with a physical device.

#### Microsoft NLB

Microsoft Network Load Balancing (NLB) works best when you distribute the user base equally across multiple external networks. Due to Relativity’s persistent session requirement, if too many users access Relativity from one network, the load distribution may become lopsided. This means one web server bears too great a load. For this reason, we recommend using Relativity User Load Balancing (RULB) in tandem with NLB.

#### Relativity User Load Balancing (RULB)

Relativity User Load Balancing (RULB) technology is a Relativity-core technology that ensures number of users on any given web server doesn't exceed the number of users on any other web server. Once a user is on the server, they stay there until they've logged off and re-accessed the system. When you implement RULB with SSL, RULB requires a secure certificate for each server in the farm.

## Bandwidth

The amount of bandwidth consumed depends heavily on both the number of reviewers and the number documents being reviewed. Understand the following conditions when assessing bandwidth:

- The average size of a document being reviewed

- The speed of the review

- The number of reviewers

Reviews are slower when reviewers examine documents for longer periods of time. Slow reviews can create a slower connection because the next document downloads in the background. This is true if you enable the Native Viewer Cache Ahead setting for each user.

Sometimes, due to bandwidth considerations and the potential lack of high-speed internet for the reviewers, you can deploy a Citrix/TS server farm. You can virtualize Citrix and TS, but be sure to avoid over-commitment.

Carefully monitor the number of users on a single Citrix server. Too many users on a single machine may quickly drain resources in certain conditions, including the following:

- Very large images

- Heavy redacting

- Very large spreadsheets

- Users opening multiple tabs in a browser window

- Massive persistent highlight sets

You should scale Citrix outward by deploying more servers. When operating Citrix machines in a virtual environment, adding more cores to a single server is viable only if physical cores are available, and commitment thresholds aren't breached. You must also consider the impact of having a single, large, multi-cored machine on the same virtual host as many, fewer cored machines.

## Conversion recommendations

Environments with a large number of users will most likely review a large number of documents. This equates to more conversion requests being made to the conversion agents.

## SQL recommendations

A good rule to follow in a highly transactional environment is to have 1 GB of RAM per 1,000 queries per second. Another popular approach is to buy as much RAM as you can afford. In an environment with many users, the number of cores may be the first thing that maxes out. Adding more cores may be the answer, but you also need more RAM.

The following considerations may pertain to SQL environments that experience heavy traffic:

- Use SQL Enterprise Edition

- Network bandwidth availability to the SQL Server

- Disk scalability – readily available SAN LUNs - know your IOPS and your workload profile.

- Test and benchmark your disk IO so you know when you exceed capacity.

- Large document table that experience frequent scans need larger amounts of RAM.

## Workspace administration

### Training

Attend our training sessions as necessary to understand Relativity best practices. In addition, conduct frequent internal training sessions to ensure that the case team has a consistent process for adjusting the workspace and workflow.

### Workspaces with many users

In workspaces with many users, ensure that users with access to create views, fields, indexes, and other objects in the workspace are aware of best practices for large workspaces. The following are some of these best practice guidelines:

#### Adding fields

Relativity provides users with the ability to add or delete fields on the document table on-the-fly. This operation momentarily locks the entire table while adding the field.

You can also add and remove fields to the full-text index on demand. This can cause increased loads on the SQL Server, especially if the fields contain a lot of data, or a lot of new records are suddenly added. The following are guidelines for working with custom fields in a large workspace:

- Understand the advantages of using fixed-length text versus long text fields. See Fixed-length text vs. long text field types in the Environment optimization guide.

- Understand your data. Don’t make fixed-length text fields longer than necessary. Don't use long text fields when a fixed-length text field works. You can easily correct these mistakes, but they can have a heavy performance impact if the problem is excessive.

- Keep track of the fields you add to the full-text index. If you use keyword search, only index the necessary fields.

- Limit list filter options for fields. Be aware of the filter options of fields in document list views. List filters on columns with many unique values can tax the web server.

- Understand how to change certain field properties, such as enabling Pivot. You should include fields that are used for pivot group by function in full text index.

#### Searching

- Eliminate "is like" queries whenever possible.

- Ensure users understand that conditions are SQL-based queries. You can only search a dtSearch index through the search textbox in the Search Conditions section. See Search conditions .

- Avoid excessively nested searches (generally three or more).

- Code existing searches to avoid re-running the same search multiple times.

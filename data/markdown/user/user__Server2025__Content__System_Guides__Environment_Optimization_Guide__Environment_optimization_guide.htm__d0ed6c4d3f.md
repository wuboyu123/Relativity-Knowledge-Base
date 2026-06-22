---
title: "Environment optimization"
url: https://help.relativity.com/Server2025/Content/System_Guides/Environment_Optimization_Guide/Environment_optimization_guide.htm
collection: user
fetched_at: 2026-06-22T06:03:19+00:00
sha256: 3ad597f5bc8312664a5b33f017fc22e99574971b879e41ecd9d2f04f9ee81226
---

Environment optimization Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Environment optimization

This guide outlines the best practices for maintaining and optimizing a Relativity environment. Follow these recommendations to ensure stability and optimal performance of all workspaces.

## Release updates

Note the changes and additions to this guide for each service release:

- We typically release a new major version of Relativity once a year.

- Product updates are released once a month. You can view Relativity release notes on this site.

## Training and support

This guide is often provided to system admins who may not have any exposure to the Relativity interface. For more information, you can access the following resources:

- Documentation - we constantly strive to ensure that all users of Relativity are educated on the full functionality of the platform. To help you and your team stay well informed, we post all documentation on this website. To access documentation from previous versions of Relativity, see the Documentation archives .

- Relativity Community - you can access the Relativity Community from the Relativity .com Support page. If you need a Relativity Community account, contact Relativity Support .

## Environment optimization checklist

Use the following checklist to help manage and plan for your Relativity environment.

Reference Task Done

Release updates Review patch releases twice a year.

Training and support

Review the Infrastructure Study Resources .

Review Relativity documentation .

Explore the Relativity Community .

Configuring Windows server

Review the guidelines for Configuring Windows server for optimal performance.

Review the Microsoft Windows server service packs and verify the latest pack is installed.

Review the guidelines for Configuring Windows server and configure them for high performance.

Configure Windows visual effects for high performance.

Configure Windows processor scheduling .

Set up automatic disk defragmentation based on the guidelines for Windows NTFS fragmentation

Manually set the size of the paging file to 4095 MB or higher based on the guidelines for Configuring virtual memory .

Exclude the SQL Server, agent server, web server, Analytics indices, dtSearch indices, and the file repository from the antivirus software based on guidelines for the Antivirus directory exclusion list .

Create a management server with SSMS and the RDC based on the guidelines for the Management server .

Configuring SQL Server Review the details for Configuring SQL Server for optimal performance.

Set the Optimize for ad hoc workloads option .

Set the Max degree of parallelism option .

Optimize the TempDB database .

Set SQL maximum server memory .

Enable Instant file initialization .

Set the File allocation unit size .

Review the Microsoft SQL Server service packs requirements and verify that the latest pack is installed.

Set Autogrowth settings settings for SQL Server files.

Review RAID levels and SQL Server storage options:

- Verify that the tempdb data files reside on the fastest disks.

- Verify that data, log, full-text, and tempdb files reside on separate disk volumes.

Configuring the Analytics server Never set the Java maximum (-Xmx) to be less than the Java minimum (-Xms). To learn more, see Configuring the analytics server .

Review the details for Configuring the Analytics server to configure an Analytics temporary directory.

Review Index directory requirements requirements and store the Analytics index locally, if possible.

Setting up your workspace Ensure you are following best practices while Setting up your workspace .

Review Fixed-length vs. long text field types and ensure to use fixed-length fields when possible.

Review Fixed-length text field considerations and set your fixed-length text fields to the appropriate size.

Review Unicode support and define the Unicode Enabled field property prior to import.

Review details on Data imports and ensure you are not running the Relativity Desktop Client on a Relativity production server.

Follow best practices for Views and searching .

Review details on using the Tally/Sum/Average mass operation and create indexes on groups that you Tally on.

Create a non-clustered index on fields that are being used for Group by for Pivot .

Learn how to use various User notifications methods.

Monitoring environment performance

Review guidelines for Monitoring environment performance .

Review Monitoring environment performance and ensure you have the right amount of memory when creating indexes.

Perform Windows and SQL Server log analysis and set up these alerts for SQL and Windows server logs:

- Low disk space on the servers

- Server becomes unresponsive

- Website becomes unavailable

Review Analytics performance considerations .

SQL Server table index fragmentation Understand, identify, and remove fragmentation.

Monitoring disk usage Measure disk latency.

Gather benchmarks for Relativity servers' Resource utilization .

Review Monitoring environment performance .

Managing your Relativity environment Review maintenance plan recommendations.

Create SQL backups for:

- Relativity system databases

- Relativity system database logs

- System databases and logs

Verify backup integrity is selected for Full backups .

Set up SQL recovery models .

Create Relativity data backups for:

- dtSearch and Analytics index shares

- Relativity web server install directories

- Native and image file shares

Schedule a weekly Check Database Integrity task .

Perform SQL table index management and schedule the IndexOptimize smart script for index and statistics maintenance.

Review recommendations for Updating statistics to improve query performance.

Review the Database log management recommendations.

Review the Shrink Database task and ensure that AUTO_SHRINK is not enabled.

Set up SQL Database Mail on all Relativity SQL Servers and add Job email notification alerts to all scheduled Relativity maintenance tasks.

Perform Workspace management and maintenance on workspaces with 500,000+ records.

Perform an Analysis of long running queries and try to optimize long-running queries.

Set up Full-text index management .

Manage the Audit record table , if needed.

Expanding your Relativity environment Review ways of Expanding your Relativity environment .

Scale Agents as needed.

Create a dedicated web server for Relativity Desktop Client import or export .

Create a dedicated agent server for the dtSearch Expanding your Relativity environment .

Set up Expanding your Relativity environment to add additional servers for increased throughput and performance as needed.

Increase Physical memory on the SQL Server(s) , if needed.

Create Distributed Relativity SQL Servers , if needed.

Set up Web load balancing , if needed.

Create Terminal services servers, if needed.

Test the capacity of a network connection with the Expanding your Relativity environment .

On this page

- Environment optimization

- Release updates

- Training and support

- Environment optimization checklist


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

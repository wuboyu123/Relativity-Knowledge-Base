---
title: "Viewer performance troubleshooting"
url: https://help.relativity.com/Server2025/Content/System_Guides/Viewer_performance_troubleshooting.htm
collection: user
fetched_at: 2026-06-22T06:16:49+00:00
sha256: 1e8a05372cfd8b38f431c60d2c3c2a7cd6b5c29b8b1205e67fcdf7c431157300
---

Viewer performance troubleshooting

# Viewer performance troubleshooting

This guide serves as a troubleshooting guide for performance issues in the HTML viewer. This guide assumes you have a basic familiarity with the conversion process, agents, and RabbitMQ. Before using this guide, complete basic troubleshooting like ensuring conversion agents are in the correct resource pool and that agent server services are running.

## Before You Begin

Before you begin the troubleshooting process, ensure the suggested infrastructure specifications located in the System Requirements guide are met.

## Infrastructure Overview

Consider the following components that impact performance in the new HTML Viewer.

- Browser - Whether you’re using Internet Explorer, Chrome, Firefox, or Safari, your browser plays two major roles in the HTML viewer. The browser is responsible for requesting and downloading files and metadata associated with the viewer and for rendering the document with all redactions and annotations. The browser is not responsible for conversion.

- Web server - The web server handles all authentication and security. It’s also responsible for handling communication between you, the Document Viewer Service, conversion agents, conversion complete agents, and sending files to your browser. Relativity, conversion agents, and sending files to your browser.

- Relativity SQL - Relativity SQL is responsible for storing all document data and metadata and cache locations for converted files.

- Relativity File Share - The Relativity File Share stores pre-conversion and post-conversion files. The file shares are responsible for servicing requests by the web server and conversion agents.

- Conversion Complete Agents - The conversion complete agent finishes the conversion response from the conversion agents and inserts data into the converted cache table. If the conversion is an on the fly request, the agent then responds to the browser with those details.

## Terminology

Before you begin the troubleshooting process, familiarize yourself with the following terminology.

- Cache - The location where converted files are stored in case they are viewed again. This prevents unnecessary conversion.

- Preconvert - When viewing document X in a document list, Relativity submits the next three documents for conversion in the background, converting them before you view them. The number of documents converted is a configurable value.

- ConvertedCacheFile - This table stores references to converted documents along with certain metrics.

## Special considerations

The asynchronous nature of document conversion and viewing means there are several components to check in order to identify performance issues. As a rule, determine a method to test suspected performance problems, eliminating as much uncertainty as possible, before you make any modifications.

## Identifying the problem

The following section assists you in investigating large parts of the infrastructure. You don’t need to follow this section linearly.

### Eliminate conversion

First, determine whether the conversion process itself is causing problems or whether the problem lies in the client, document viewer services, agents, web, or SQL Servers. By identifying the cause of the problem, you can narrow down the performance issue to the fewest components.

If documents take many seconds to convert and download, use the following steps to pinpoint the source of the issue:

- Note the artifactID of the document which takes many seconds to convert and download. Note the time required for this process.

- Refresh the current page once the render finishes.

If the page refresh is faster than the original page load, there is a problem with the conversion process. See Conversion is a problem .

If the page refresh took the same amount of time as the original page load, conversion is not the source of performance issues. See Conversion is not the problem .

## Conversion is a problem

If you determined conversion is a problem, ensure you narrow down the conversion problem to one of the following performance components:

- Document Viewer Service takes a long time to submit request to the conversion agent.

- The conversion agent process takes a long time.

- The Relativity web server’s Conversion API.

- The conversion complete agent process takes a long time.

- The environment doesn’t have enough conversion agents to handle the load.

- The environment doesn't have enough conversion complete agents to handle the load.

### Conversion agent

If you determined the conversion agent process takes a long time, you can run the Conversion time metrics gathering.sql script available in the Relativity Community . The script identifies problems in the last 5 million (configurable value) document conversion operations. The script produces two sets of output. The first set of output contains the following information:

- Last Access Hour - The script buckets conversions by the hour.

- When comparing to peak times or user reported issues, the times are UTC.

- Type - Types are “Native,” “Image,” and “Production.”

- There may be “duplicate” rows for production. Duplicate rows for production mean two different production sets were reviewed in the same hour.

- Document Count - The number of documents converted during that hour for the given type.

- Average/Max Conversion Time (ms) – The average and maximum conversion times within the hour.

- Average/Max Output File Size (bytes) - The average and max output file sizes within the hour. This value is only present on image or production type records.

The second set of output separates conversion times by percentiles. In the following example 95% of all image conversions took 4.473 seconds or less to complete; 90% of all native conversions took 0.706 seconds or less to complete:

You can determine whether the conversion agent is the source of performance issues in your environment by reviewing the two outputs from running the “Conversion time metrics gathering.sql” script. While conversion times are dependent on your hardware and document set, the following are general guidelines for the average conversion process:

- Native - 750ms or less on average.

- Image - 500ms or less on average.

- Production - 500ms or less on average.

The conversion agent is not the source of the performance issues if conversion times are significantly lower than the time required to initially load a document. If conversion times are comparable to the time required to initially load a document, the conversion agent is the primary source of performance issues.

#### Possible solutions

If you determine the conversion agent is the source of your performance issues, consider the following performance solutions:

- Check the agent's hardware and verify compatibility with the System Requirements on the Relativity documentation site.

- Check virtual machine allocations for memory or CPU overcommitment.

- Investigate whether issues are limited to a particular document or document type.

- Increase the instance setting kCura.EDDS.Web, PreConvertCacheSize.

- Use the conversion mass operation to convert batches before reviewers log in each day.

The last two options assist with perceived performance rather than improving actual performance. For either of the last two options, test to ensure the environment can handle the load and that more conversion agents aren't needed.

### Web server

If the web server is the source of performance issues, Relativity runs slowly and the web server likely sits at 100% CPU and/or RAM utilization. This means the web server doesn’t have adequate hardware to support the environment.

### Document Viewer Service

If the document viewer service is the source of performance issues, Relativity API runs slowly. This means the web server doesn’t have adequate hardware to support the environment.

Possible solutions:

- Restart Service Host on the web servers

### Conversion Complete Agent

If the conversion complete agent is the source of performance issues:

- Restart Service Host on the web servers

### None of the above

If conversion is a problem, but the document viewer service, conversion agents, and conversion complete agents and web servers all perform as expected, then consider environmental scaling as the source of performance issues. To confirm that environmental scaling is the root cause, examine the "conversions_rp<Resource Pool ID>" topic's subscriptions. If large numbers of messages are piling up on these subscriptions, then add more conversion agents to the resource pool. Examine "conversions_responses" if any of those subscriptions have large number of messages piling up on these, then add more conversion complete agents.

As a base recommendation dedicate one conversion agent solely to conversion for every 100 concurrent reviewers and 1 conversion complete agent per web server on the core agents server. However, this ratio is only a suggestion, as different workflows may require a different number of conversion agents. For example, if your workflow has many documents taking minutes to convert, additional conversion agents may be recommended.

## Conversion is not the problem

If conversion is not the source of the performance issues, the environment is the likely source.

### Relativity SQL

Before sending a document to the client machine, the web server needs to know where the document resides on the disk.

If the entire environment is experiencing poor performance, Relativity SQL is not the source. If Relativity SQL is the source, performance issues occur only in a single workspace or workspaces using the same template.

This script is useful for identifying SQL problems. There is a low chance that there is locking on the ConvertedCacheFile table, which suspends queries accessing the cache location. If you see many suspended queries accessing the ConvertedCacheFile table with long lock waits when you check the output of this script, then the table has a locking problem.

#### Possible solutions

If you determine Relativity SQL is the source of your performance issues, consider the following performance solutions:

- Follow the blocking chain to the root query. Often it is a rogue query (e.g., attempting to remove dirty rows from ConvertedCacheFile with a table lock).

- Check the indexes on ConvertedCacheFile. Relativity ships with indexes that support fast, low locking queries, but if these are missing, access to the table takes significantly longer and holds locks.

- Check the ConvertedCacheFIle which may be large and unwieldy. This is in part because Relativity does not delete from this table, instead old converted files are marked "dirty" and ignored. If the table is too large, clean up the table during downtime with the following query: DELETE FROM [EDDSDBO].[ConvertedCacheFile] WITH ( TABLOCKX ) WHERE [ Dirty ] = 1,

- Check SQL memory usage. Lock escalations may be causing normal operation to grab table locks if a lot of locks and memory pressure exist. This is extremely rare and indicates a larger problem. Should you encounter this problem, contact Customer Support.

### Web servers, cache servers, and network

If Relativity SQL isn’t the source of your performance issues, it is likely the web and cache servers are the source.

To check your web and cache servers’ performance, use the following procedure:

- In any browser, press F12 to open the developer tools.

- Run a network capture for the second time a document is viewed. Internet Explorer 10 displays the following window:

-

Zoom in on the segment containing /Relativity/CustomPages/C9E4322E… and /Relativity/CustomPages/5725cab5… (Columns are rearranged in the screen shot.) These calls receive the CacheID for the document (C9E) and download the converted file (5725).

The web and cache servers respond quickly if “taken” times are small. However, if “taken” times are in seconds or hundreds of milliseconds, sending data from the servers to the client is the source of your performance problem.

#### Possible solutions

If you determine the web or cache server is the source of your performance issues, consider the following performance solutions:

- Use 4 CPU cores and 4GB of RAM for every 25 active users on a web server in Relativity 9.2. Ensure your environment meets these specifications.

- Check the network connection between all components, including the client machine.

- Check the disk utilization on the cache server, and, if necessary, separate your cache storage from file storage.

### Client machine

If you determine the Client machine is the source of your performance issues check to see if the performance problem is present on a different machine running the same browser.

### Web browser

If you determine the web browser is the source of your performance issues, check to see if the performance problem is present in Chrome, Firefox, and Internet Explorer 10/11.

Testing shows some performance problems exist only in Internet Explorer 10. If Internet Explorer is preferred, Internet Explorer 11 could provide better performance.

### Metadata

If you determine metadata is the source of your performance issues, check to see if the performance problems are present when there are no persistent highlight sets or markup sets.

### Data

If you determine data is the source of your performance issues, check to see if the performance problem is present on different documents and document types. Large (50+ pages) image files/productions, spreadsheets, and some other file types exhibit some performance issues in the HTML viewer.

## Knowledgebase articles

You can also use knowledgebase articles to diagnose and solve viewer performance issues not explained in this guide. The knowledgebase articles are provided by Customer Support and are available via the Relativity Community .

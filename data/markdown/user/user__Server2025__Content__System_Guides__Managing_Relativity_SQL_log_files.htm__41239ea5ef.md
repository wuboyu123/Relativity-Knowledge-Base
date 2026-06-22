---
title: "Managing Relativity SQL log files"
url: https://help.relativity.com/Server2025/Content/System_Guides/Managing_Relativity_SQL_log_files.htm
collection: user
fetched_at: 2026-06-22T06:04:48+00:00
sha256: 7a1c27457198b5d19d72eea71364aedbcb1d333ee73b79a3aa16ebce840d33f2
---

Managing Relativity SQL log files

# Managing Relativity SQL log files

This page provides tips for keeping log files healthy and a procedure for properly sizing log files. Keep in mind that you should consistently monitor the log files because, if the log drive fills up, and SQL stops, Relativity will also stop working.

## Overview

Relativity databases typically exist in fast-growing environments with high activity.Therefore, it’s important for the transaction logs to be healthy because they keep a history of all executed actions. Unhealthy log files can result in bottlenecks even if they are small in size. Tiny log files that experience large transactions can slow down an environment because, even with instant file initialization turned on, they still need to write zeroes in order to grow.

## Log maintenance tips

Consider the following tips when maintaining log files:

- Ensure that log file backups are set to run at least once every hour. Consider running them more often in the following scenarios:

- You want to recover with less than one hour of data loss.

- Your system writes more data to the log file in one hour than is ideal.

- The amount of data written to the log file in one hour causes the log file to fill the drive. SQL marks space in the log file as reusable once it is backed up, so it shouldn’t grow too large.

Some single transactions in Relativity are quite large and may result in log file growth through multiple transaction log backups. This can prevent successful log backups. Contact Customer Support if this happens, and let them know what action caused it.

- Ensure the autogrowth of the log files is set to at least 512 MB, but no more than 1 GB. When log file growth occurs, zeroes must be written to disk before anything else is written to the log file. Setting autogrowth too high can cause other transactional activity to be suspended while autogrowth is in progress.

- In certain situations, when Relativity begins an operation, such as a large data load, many gigabytes of data can pour into the log file before the next scheduled log backup marks space as available. Taking more frequent log backups can mitigate this kind of issue. Unanticipated growth can also occur when extremely large transactions run. Should this occur, contact Customer Support .

If you find that, even with proper transaction log backups, your log files are growing too large, contact Customer Support . If you know that you are creating hundreds of gigabytes of new data in your database, we strongly recommend that you grow the log file during a maintenance window beforehand. This reduces environmental impact when loading during the day.

## Setting the size of a SQL log file

Use the following flow chart to decide how many VLFs to make:

- Is the growth less than 1/8 of current physical log size? If yes, then make 1 VLF.

- If not, is the growth less than 64 MB? If yes, is the Is version SQL 22 or above? If yes to both of these questions, then make 1 VLF.

- If the answer is no to both questions 1 and 2, then make 4 VLF. If the answer is no to question 2 only, is growth less than 1 GB? If so, then make 8 VLF.

- If the answer to question 3 is no, then make 16 VLF for any growth greater than 1 GB.

Before you begin this procedure, perform a full backup, and make sure there are no transactions running.

This work may have heavy environmental impact. You should only perform this process in a maintenance window.

Perform the following steps to set the size of a SQL log file:

You should test this process on a test database, and time it as a baseline.

- Right-click the database, and then select Properties .

- Click Files .

- Click Initial Size , and then set it to 1 . This decreases your start size to 3 VLFs. If the log file does not shrink, we recommend contacting your database administrator for assistance. If it does shrink, run a script to truncate the log.

- Click Initial Size , and then set it to 1/3 the size you want. This can take a few seconds or several minutes as the log file grows.

For a target file size greater than or equal to 25 GB, grow the file in 8 GB chunks rather than thirds of the target size.

- Set the Initial Size value to 2/3 the final size.

For a target file size greater than or equal to 25 GB, grow the file in 8 GB chunks repeatedly until you're within 8 GB of the target size.

- Set the Initial Size value to the target size.

This method should produce around 50 VLFs or a value twice that of your target file size in GB for larger databases.

New workspaces copy the LDF file from the database of the template case, but the LDF for the new workspace shrinks when the systems creates the workspace. This means that new workspaces always have approximately the same LDF file size and VLF count when they're created and should have this maintenance procedure performed prior to any large data imports.

### Log file sizing considerations

If you know you’re going to perform maintenance on your database that requires a complete copy of a large table, consider making the log file as big as that table and its indexes. You should continuously monitor your log files and adjust accordingly.

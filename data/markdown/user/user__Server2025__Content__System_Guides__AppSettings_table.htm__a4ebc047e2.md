---
title: "AppSettings table"
url: https://help.relativity.com/Server2025/Content/System_Guides/AppSettings_table.htm
collection: user
fetched_at: 2026-06-22T06:04:44+00:00
sha256: 421275b9a6f5fa5ca4be14e5127f0119039cca87d8ae5b25ddb7c1a246381316
---

AppSettings table Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# AppSettings table

This guide provides a description of configurable entries in the AppSettings table in the processing SQL Server. The AppSettings table contains configurable values applicable to processing data with web Processing or the Relativity Processing Console .

## AppSettings table values

Click the blue column headings to sort the table alphabetically by Row Category .

The following list contains the only values that you should modify.

Row Category SubCategory Description Value1 Value2

CompressMetadata* The value to store document metadata in a binary serialized format within the Store. The value can be 0 - 1 (0 = false, 1 = true). This value is only applied when creating a new Store and overrides the value in the Flags column on the Stores table. 1 (true)

DataFiles This is the default UNC path where you store natives, text and OCR when using the Relativity Processing Console. We recommend that you start with 250 GB and increase the value according to how heavily you plan to use the RPC. \\exampleUNCpath\examplefolder

DefaultDatabasePath This is the default path where Invariant database files are stored C:\thisisanexamplepath

DoNotCopySourceContainers

This determines whether or not Relativity Processing makes a copy of the folder specified in your processing data sources and places that copy in the file repository.

- A value of 0 (false) means that it does make a copy.

- A value of 1 (true) means that processing does not make a copy.

- This setting does not appear by default. You must manually add it to your appsettings table.

- This setting is not respected when the path/filename of the source container exceeds 256 characters.

- This setting is not respected when the path is fewer than 256 characters while the file name is greater than 200.

- This setting was introduced in Relativity 9.4.

1 (true)

dtSearchPath dtSearch index path This is the location that stores dtSearch data.

E01/BatchSize Processing Indicates the number of files that E01 will process as part of a batched job. 10,000

Email/UseSMTPAddresses Processing The default value to use the SMTP formatted address when processing an email file. The value can be 0 - 1 (0 = false, 1 = true). This value is only applied when processing documents via the API. 1 (true)

Excel/Timeout The time in milliseconds for Relativity to determine that an Excel process is stuck and needs to be ended. This is reset each time Excel sends data to Relativity, and if it doesn't send new information within 300,000 milliseconds (5 minutes), Relativity ends the process. This is relevant to clients who are processing large Excel files and who may want to edit this value to allow more time for those files. 300,000 (milliseconds)

HttpWebRequestTimeout The time in seconds to wait for an HttpWebRequest to return a response. For a value of 0, the default timeout is used. 0 NULL

IdentityServerURL URL of the Identity Server for RPC Authentication. Do not include /connect/authorize, as this is appended in code. https://example/Relativity/Identity NULL

JobDefaultSetting Images/CADTimeout The timeout value in seconds used when processing/imaging CAD files. The default value is 600 seconds.

JobDefaultWorkerGroup Imaging This is the default workgroup used for all imaging jobs. 0. (0-10 are the only numbers available.)

JobDefaultWorkerGroup Processing This is the default workgroup used for all processing jobs. 0. (0-10 are the only numbers available.)

LongRunningJobTimeout Job The amount of time (in milliseconds) to run a job before the Worker terminates the worker process. Value1 is the representation of 30 minutes in milliseconds. You may want to adjust this value if you have large documents that need additional time for processing. If you need to adjust this value, you can manually go into the App Settings table and increase the value accordingly. 1,800,000 (milliseconds)

LongRunningRetryJobTimeout Job The amount of time (in milliseconds) to run a non-publish retry job before the worker terminates the worker process. If blank, the value used will be equal to LongRunningJobTimeout setting. 540,000 (milliseconds)

MapVolume This is the UNC path for the source location displayed in the processing console when importing data into a data store. You can add multiple MapVolumes in separate rows. NULL \\exampleUNCpath\examplefolder

MigrationBatchSize Determines the number of database records that can be modified per batch during migration. This value is meant for use with ARM for Invariant/Processing. 10,000

MigrationBatchTimeoutDelay Determines the delay time in milliseconds between each batch modification of database records during migration. This value is meant for use with ARM for Invariant/Processing. 500 (milliseconds)

RepeatLoggingIntervalInMinutes The timespan, in minutes, that errors will be re-logged when Invariant is in a retry loop. 5

RPCDefaultJobPriority Priority This value sets the default priority for all jobs initiated from the processing console. The default value is 100.

WorkerNetworkPath This is the default UNC path where upgrade files are temporarily stored when upgrading the processing engine. \\exampleUNCpath\examplefolder

WorkerFileCheckTimespanInMinutes Timespan in minutes that the network share is checked for file updates. This setting is used by the Queue Manager to check the file share for changes; if it detects a change, such as a dll drop or file handler upgrade, the smart launcher then updates the workers. 2

* The CompressMetadata flag, which is an Invariant setting that controls how metadata is saved to the database, is enabled by default. Making this flag enabled provides ingestion performance improvements and reduces the size of your store databases. To assist with troubleshooting and to give you control over this setting, there is a new entry in the AppSettings table called CompressMetadata, which by default, has CompressMetadata enabled for when you create a new store either through Relativity or the RPC . To disable CompressMetadata, set this value to 0 (false/disabled).

Note that the CompressMetadata flag is also set on all of your Invariant stores. If you need to disable metadata compression on any of your stores, you must manually change the value from 4 (true/enabled) to 0 (false/disabled).

Contact Support if you need assistance determining when to disable metadata compression on your stores.

On this page

- AppSettings table

- AppSettings table values


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

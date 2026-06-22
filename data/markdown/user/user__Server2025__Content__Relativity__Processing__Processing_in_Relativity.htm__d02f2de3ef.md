---
title: "Processing"
url: https://help.relativity.com/Server2025/Content/Relativity/Processing/Processing_in_Relativity.htm
collection: user
fetched_at: 2026-06-22T06:02:09+00:00
sha256: a896797cc9fcb421978d55d4bba44c7dcecd860b4ad3e8a33619868ffd2db4b6
---

Processing Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Processing

Use Relativity’s processing feature to ingest raw data directly into your workspace for eventual search, review, and production without the need for an external tool. You can use the various processing objects to create custom processing jobs that handle a wide array of information.

Read if you are studying for the Processing Specialist exam The content on this site is based on the most recent monthly version of Relativity, which contains functionality that has been added since the release of the version on which Relativity's exams are based. As a result, some of the content on this site may differ significantly from questions you encounter in a practice quiz and on the exam itself. If you encounter any content on this site that contradicts your study materials, please refer to the What's New and/or the Release Notes for details on all new functionality.

Some of the primary goals of processing are to:

- Discern, at an item level, exactly what data is found in a certain source.

- Record all item-level metadata as it existed prior to processing.

- Enable defensible reduction of data by selecting only items that are appropriate to move forward to review.

Processing does not perform language identification. For information on how to perform language identification using Analytics, see Language identification .

To gain control over more complex processing jobs on a granular level, you can use the Processing Console desktop application. For more information, see the Processing Console .

There are no specific security requirements, but if a user needs to be restricted from running processing, then permissions need to be revoked to all processing objects.

See these related sections:

- Installing and configuring processing

- Supported file types

- Entities

- Password bank

- Processing profiles

- Processing sets

- Inventory

- Discovering files

- Publishing files

- Processing error workflow

- Reports

- Managing the processing queue

- Deduplication considerations

- Processing duplication workflow

- Processing Console

## Application version considerations

All the content in this section and its related pages correspond to the latest version of the Processing application, which is updated on a monthly basis with the release of each patch of Server 2025 .

If the processing components in your environment do not match the descriptions in this content exactly, it may be because you are using an older version of the Processing application. To get the newest version of the Processing application, upgrade to the latest product update of Server 2025 .

For a list of changes made to processing per monthly product update, see the Release Notes .

## Basic processing workflow

The following steps depict a typical processing workflow that uses all available processing objects and phases. Note that each user's workflow may vary. You may not be required to follow all of these steps for every processing job you run.

- Processing sets

-

Entities can be created on the fly, in advance, or automatically through imports or connections to HR systems.

-

Processing Profiles carry over from template workspaces.

-

If necessary, create new Password Bank Entries with passwords for any password-protected files to be processed.

- (Optional) Inventory

-

Inventoried files can be filtered down based on several metadata attributes prior to publish.

-

Reports can be run to understand and communicate the files culled from publish.

-

Discovering files and Publishing files

-

Post publish—view, ignore, or retry any errors that occurred during any phase of the processing job. If needed, republish the files.

## Logging for processing

The logging framework enables you to efficiently gather runtime diagnostic information. You can use logging for troubleshooting application problems when you need a very granular level of detail, for example, when working with a Relativity Support representative.

Relativity system components that can log messages are identified based on the system-subsystem-application designation. When troubleshooting, use the system-subsystem-application matrix to configure logging to target a specific Relativity component, such as the Processing application.

It is recommended that you not set your logging to verbose when publishing documents to a workspace, as doing so can cause your worker to run out of resources, such as CPU, RAM, disk usage, or others, which then causes your publish job to cease entirely. If you need to use verbose logging in order to collect detailed logs, do so for short periods of time only, under 5 minutes, and have a developer on hand to troubleshoot if any issues occur.

For more information, see Logging and Logging system-subsystem-application matrix .

On this page

- Processing

- Application version considerations

- Basic processing workflow

- Logging for processing


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

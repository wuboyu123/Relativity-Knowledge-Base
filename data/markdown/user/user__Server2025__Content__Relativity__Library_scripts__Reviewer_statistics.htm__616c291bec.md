---
title: "Reviewer statistics"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Reviewer_statistics.htm
collection: user
fetched_at: 2026-06-22T06:02:48+00:00
sha256: 73f4b5bebbbf0daa221ebc2842ba7e5689ee926d2ff5912b9391cdc330391a6c
---

Reviewer statistics Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Reviewer statistics

If the workspace has a large amount of audit data, we recommend breaking up the date ranges to smaller data sets to be able to retrieve the data efficiently. If a data set becomes too large, the report performance begins to degrade and may result in an error.

The Relativity Reviewer Statistics scripts report on the efficiency of reviewers over the specified date range. The returned statistics provide a count on how many documents were reviewed over a certain period of time. Time zone of the reviewers must be specified in order for the report to accurately account for reviewers in different time zones.

The returned statistics provide a count of how many documents were reviewed over a certain period of time. For simple coding fields like textbox, radio button, drop down, etc., edit tracking occurs when a user clicks Save, or Save and Next. For example, when a user commits coding changes.

You can use the following scripts to generate this information:

- Reviewer Statistics - use this script to generate a report that lists the system admins.

- Reviewer Statistics - No System Administrators - use this script to generate a report that does not include system admins.

Ensure that users running this script have both the Relativity Script Object Security > View permission enabled and View All Audits checked in the Admin Operations section of Other Settings.

## Inputs

Enter the following field information:

- Reviewer Time Zone - The reviewer time zone for which you wish to report on.

- Start Date - the start date for which you wish to report on.

- End Date - the end date for which you wish the report on.

- Include Additional Action - set this field to add statistics for Mass Edits and Propagation.

- Downtime threshold (minutes) - this field helps to calculate the Total Usage Time metric and determines whether two audits belong to the same group of action. The default value for this field is 60 minutes. If the time difference between the two actions is less than the Downtime threshold, that time will be included to add up to the Total Usage metric; if it's greater than the Downtime threshold, only two minutes will count for these two actions (one minute for each action).

If the Audit application is installed in your workspace, the script pulls audit data from Elasticsearch.

## Results

Once you run this script, the Reviewer Statistics report displays.

The report includes the following columns:

By default, the following columns are not included in the output. To include these columns, in the Include Additional Action drop-down list, select Mass Edits and Propagation .

Propagations

Distinct Propagations

Propagations Per Hour

Propagations Per Day

Distinct Propagations Per Hour

Distinct Propagations Per Day

Column Definition

Full Name The reviewer’s full name.

Total Usage Time The total usage time is calculated as the difference between the time the user first views or edits any document in the workspace and the time the user last views or edits any document in the workspace per session. A session is anytime the user has logged in to Relativity. All sessions for the selected date range are then totaled per user.

When audits are stored in Elasticsearch, the session ID is used to calculate the total usage time for the session.

Views The total number of documents a reviewer looked at over the reported period.

Distinct Views The number of unique documents a reviewer looked at over the reported period.

Edits The total number of editing/coding decisions made over the reported time period.

Distinct Edits The total number of documents edited, excluding repeated edits of the same document. The "distinct" classification is meant to account for duplicate actions performed against unique documents.

Edits Per Hour The number of edits per hour based on the reviewer’s total usage time.

Edits Per Day The number of edits performed per day over the period reported on.

Distinct Edits Per Hour The number of distinct edits per hour based on the reviewer’s total usage time.

Distinct Edits Per Day The number of unique edits performed per day over the period reported on.

Mass Edits The total number of document edits using the Mass Edit action.

Distinct Mass Edits The total number of unique document edits using the Mass Edit action.

Mass Edits Per Hour The number of Mass Edits per hour based on the reviewer's total usage time.

Mass Edits Per Day The number of Mass Edits per day over the period reported on.

Distinct Mass Edits Per Hour The number of distinct Mass Edits per hour based on the reviewer's total usage time.

Distinct Mass Edits Per Day The number of distinct Mass Edits per day over the period reported on.

Propagations The total number of documents that were updated via propagation.

Distinct Propagations The total number of unique documents that were updated via propagation.

Propagations Per Hour The number of propagations applied per hour based on the reviewer's total usage time.

Propagations Per Day The number of propagations applied per day based on the period reported on.

Distinct Propagations Per Hour The number of unique documents that had propagations applied per hour based on the reviewer's total usage time.

Distinct Propagations Per Day The number of unique documents that had propagations applied per day based on the period reported on.

On this page

- Reviewer statistics

- Inputs

- Results


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

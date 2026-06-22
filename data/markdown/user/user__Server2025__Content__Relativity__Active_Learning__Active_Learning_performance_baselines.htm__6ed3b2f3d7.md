---
title: "Active Learning performance baselines"
url: https://help.relativity.com/Server2025/Content/Relativity/Active_Learning/Active_Learning_performance_baselines.htm
collection: user
fetched_at: 2026-06-22T06:08:08+00:00
sha256: 02fa7c030847d94fd174e675a3b21f9abc5d6ce7789b132861739888e9375c3e
---

Active Learning performance baselines Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Active Learning performance baselines

This page is meant to be used as a reference to track the overall performance of Active Learning in RelativityOne. It should not be used as a benchmark of what you expect to see in a production client environment or Relativity Server environment due to differences in data, infrastructure, and configuration. The results may not scale linearly. Exceeding these limits may result in failure or degraded experience using Active Learning. If you have a larger data set, see Scaling Active Learning for options.

## Active Learning project size recommendations

These recommendations are the result of extensive testing in RelativityOne. For the best user experience, we advise adding a maximum of 9 million total documents and a maximum of 1 million coded documents to an Active Learning project .

We recommend no more than 150 concurrent reviewers per project. Concurrent reviewers are defined as reviewers making coding decisions in an Active Learning queue at the same time. There is no limit to how many reviewers you can add to a queue as long as the number of concurrent reviewers remains at 150 or fewer.

Max documents in classification index Max coded documents Max concurrent reviewers

9 million 1 million 150

## Data set details

These tests were run on a subset of the following data set in a RelativityOne environment. Results may vary.

Data set name File count Average extracted text size (KB) Total Extracted Text size (GB)

Real World 9,154,516 30.18 276.25

## Classification index population + build results

A classification index is required for an Active Learning project. This performance run includes population of all documents and building. Start time was measured as the time the first document was sent to the Analytics server, and end time was measured as when the last document became available in Active Learning.

Index size (Documents) Pre-coded documents Population rate (GB/hr) Population time

(h:mm:ss) Index build

(h:mm:ss) Total operation time (h:mm:ss) Documents/hr

1,000,000

10

13 3:03:29 0:13:30 3:16:59 304,878

## Active Learning index build results

Once the Active Learning model completes its initial build, the model builds at maximum every 20 minutes to include new coded documents. The documents were randomly coded 50% responsive and 50% non-responsive using Relativity's sampling feature.

The test scenarios in the following table use an index that contained 1,000,000 documents.

The results listed below were measured after the initial model build completed and do not include the population stage as the documents have already been added to the index.

Coded documents Index build time (h:mm:ss)

Build 1 10 0:13:30

Build 2 100,000 0:27:17

Build 3 200,000 0:31:02

Build 4 300,000 0:38:29

Build 5 400,000 0:50:52

Build 6 500,000 0:56:21

Build 7 600,000 1:06:27

Build 8 700,000 1:09:29

Build 9 800,000 1:09:33

Build 10 900,000 2:45:09

Build 11 1,000,000 3:24:16

The test scenarios in the following table use an index that contained 9,154,516 documents.

Coded documents Index build time (h:mm:ss)

Build 1 10 1:38:30

Build 2 100,000 2:59:32

Build 3 700,000 5:14:47

Build 4 800,000 7:39:47

Build 5 900,000 6:50:19

Build 6 1,000,000 6:25:35

## Update ranks results

In an Active Learning project, you can manually update the document ranks and ensure the rank categorization field is up to date. Once you click Update Ranks, you can monitor the update progress via a fly-out modal. You can update ranks again only after the current modification is complete. Update ranks performs faster on subsequent updates than on the initial update.

Project size (documents) Initial update ranks Subsequent update ranks

Operation time (h:mm:ss) Operation time (h:mm:ss)

200,000 0:02:48 0:01:59

400,000 0:06:12 0:04:42

600,000 0:09:42 0:07:02

800,000 0:13:48 0:11:39

1,000,000 0:22:24 0:15:14

9,154,516 5:47:36 3:39:54

On this page

- Active Learning performance baselines

- Active Learning project size recommendations

- Data set details

- Classification index population + build results

- Active Learning index build results

- Update ranks results


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

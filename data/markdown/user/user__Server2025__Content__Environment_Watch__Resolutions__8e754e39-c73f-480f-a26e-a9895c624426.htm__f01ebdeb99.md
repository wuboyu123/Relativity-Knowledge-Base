---
title: "One or more Fileshares are not accessible"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/8e754e39-c73f-480f-a26e-a9895c624426.htm
collection: user
fetched_at: 2026-06-22T06:18:58+00:00
sha256: 3e4d81b3a89a3a297467505f1874ec31de7f3a855c825061c3415f4859b577dc
---

One or more Fileshares are not accessible Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

8e754e39-c73f-480f-a26e-a9895c624426

# One or more Fileshares are not accessible

## Description

This alert is triggered when one or more network file shares on resource servers are inaccessible.

## Resolution Guidance

### Impact When Active

When a network file share on a resource server is inaccessible, dependent applications and processes may be unable to perform read or write operations. This can lead to job failures, processing delays, or interruptions to users until access is restored.

### How To Resolve

- Login to Kibana.

- Navigate to Fileshare dashboard.

- Identify the specific host(s) where the fileshare is inaccessible and note the fileshare path.

- Verify whether the issue is isolated to specific host(s) or affects all hosts attempting to access the fileshare.

- From each impacted host, verify the fileshare path and permissions:

- Verify access to the fileshare path (e.g., \\server\share ).

- Verify read permissions by opening or reading an existing file on the fileshare.

- Verify write permissions by creating or modifying a test file on the fileshare.

- Ensure the service account has the necessary read/write permissions on the fileshare.

- Verify network connectivity and access rules between the impacted host(s) and the fileshare server.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elasticsearch Query

Data View metrics-*

Filter Query relsvr.resourceserver_networkshare.accessible: 0

Group Count

Threshold > 0

Time Window 90 sec

Frequency 30 sec

### Alert Metric Details

Metric Name: relsvr.resourceserver_networkshare.accessible

Metric Description: Alert is true if one or more resource server network shares are inaccessible for at least 90 seconds.

Metric Attributes:

Attribute Name Description

labels.mount_point File share location

labels.state accessible/inaccessible

labels.system_filesystem_display_name File share resource server display name

On this page

- One or more Fileshares are not accessible

- Description

- Resolution Guidance

- Impact When Active

- How To Resolve

- Alert Details

- Alert Condition Details

- Alert Metric Details


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

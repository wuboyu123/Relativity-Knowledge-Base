---
title: "Disk I/O has been exceeding threshold on at least one host"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/50ccd14c-8ec9-43d5-971d-14fc8b5dd700.htm
collection: user
fetched_at: 2026-06-22T06:19:04+00:00
sha256: 7a0bebd0c5b46d2b97b6e9b992890a28262121495cd8d11e761ea4ebdfdd3bbb
---

Disk I/O has been exceeding threshold on at least one host Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

50ccd14c-8ec9-43d5-971d-14fc8b5dd700

# Disk I/O has been exceeding threshold on at least one host

## Description

This alert is triggered when Disk I/O has exceeded the defined threshold for at least 15 minutes on at least one host.

## Resolution Guidance

### Impact When Active

When disk I/O utilization exceeds the threshold for an extended period on a host, the server's performance may be significantly impacted. This can result in slower read/write operations, application timeouts, delayed data processing, and potential service degradation for applications relying on disk operations.

### To resolve this alert, you can try below steps:

- Login to Kibana.

- Click on the alert link in Relativity to navigate to Kibana dashboard.

- Identify the affected host and disk from the navigated dashboard.

- Verify for disk-intensive operations such as backups, data migrations, or large file transfers.

- Investigate the processes or applications causing high disk I/O on the affected host.

- Review recent changes or workload increases that may have caused the disk I/O spike.

- If high disk I/O persists, consider optimizing disk performance, adding storage capacity, or redistributing workload.

- Monitor the host to ensure disk I/O utilization returns to acceptable levels.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Metric threshold

Group Average

Threshold > 0.9

Time Window 15 min

Frequency 1 min

Group alerts by host.name

### Alert Metric Details

Metric Name: system.filesystem.utilization

Metric Description: Alert triggers on Disk I/O has exceeded 90% for at least 15 minutes on at least one host.

Metric Attributes:

Attribute Name Description

labels.device The filesystem device name. For Windows based OS's, this is normally the primary OS drive letter.

labels.mode Mountpoint mode such "ro", "rw", etc.

labels.mountpoint Mountpoint path.

labels.type Filesystem type, such as, "NTFS", "CDFS", etc.

On this page

- Disk I/O has been exceeding threshold on at least one host

- Description

- Resolution Guidance

- Impact When Active

- To resolve this alert, you can try below steps:

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

---
title: "Disk space utilization is above threshold on at least one host"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/3adc059d-d2a0-4706-8ceb-eeeac29f6337.htm
collection: user
fetched_at: 2026-06-22T06:19:03+00:00
sha256: ca11505502dd07e067fe126a5e1e4f4018e5426818f14e169345af29d15c58e8
---

Disk space utilization is above threshold on at least one host Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

3adc059d-d2a0-4706-8ceb-eeeac29f6337

# Disk space utilization is above threshold on at least one host

## Description

This alert is triggered when the disk space utilization exceeds the defined threshold on at least one host for at least 5 minutes.

## Resolution Guidance

### Impact When Active

When disk space utilization exceeds the threshold on a host, the server may be at risk of running out of available storage. This can lead to failed write operations, inability to create temporary files, application instability, or service interruptions. Critical system functions may be impaired if the disk becomes fully utilized.

### To resolve this alert, you can try below steps:

- Login to Kibana.

- Click on the alert link in Relativity to navigate to Kibana Dashboard.

- Identify the affected host from the navigated alert dashboard.

- Investigate which files, directories, or applications are consuming the most disk space.

- Remove unnecessary files or expand disk capacity.

- Monitor the host to ensure disk space utilization returns to acceptable levels.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Metric threshold

Group Average

Threshold > 0.95

Time Window 5 min

Frequency 1 min

Group alerts by host.name

### Alert Metric Details

Metric Name: system.filesystem.utilization

Metric Description: Alert triggers on Disk space utilization exceeds 95% on at least one host for at least 5 minutes.

Metric Attributes:

Attribute Name Description

labels.device The filesystem device name. For Windows based OS's, this is normally the primary OS drive letter.

labels.mode Mountpoint mode such "ro", "rw", etc.

labels.mountpoint Mountpoint path.

labels.type Filesystem type, such as, "NTFS", "CDFS", etc.

On this page

- Disk space utilization is above threshold on at least one host

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

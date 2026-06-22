---
title: "Custom pages failed to install for at least one application"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/e0122758-1312-412f-8ae4-23c134ecb585.htm
collection: user
fetched_at: 2026-06-22T06:18:11+00:00
sha256: 9a55e6ce66d93d42820958d52c623eacdf4e6dabe275fc99699774f75b617925
---

Custom pages failed to install for at least one application Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

e0122758-1312-412f-8ae4-23c134ecb585

# Custom pages failed to install for at least one application

## Description

This alert is triggered when Custom pages failed to install for at least one application.

## Resolution Guidance

### Impact When Active

When custom pages fail to install for an application, users will be unable to access or use the custom page functionality within that application. This can prevent users from accessing critical features, workflows, or custom interfaces that are essential for their work. The application may be partially functional, but custom page-dependent operations will fail.

### How To Resolve

- Verify the Custom Page Deployment Manager agent is enabled in Relativity.

- This agent runs on the web servers under the kCura EDDS Web Processing Manager service rather than on standard agent servers.

- Verify that the kCura EDDS Web Processing Manager service is running on all web servers. If the service is stopped, restart it and confirm that it starts successfully.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elasticsearch Query

Data View metrics-*

Filter Query relsvr.ads.custom_page.deployment.failed : 1

Group Count

Threshold > 0

Time Window 1 min

Frequency 30 sec

### Alert Metric Details

Metric Name: relsvr.ads.custom_page.deployment.failed

Metric Description: Alert triggers when custom page of any application fails to install for at least 1 minute.

Metric Attributes:

Attribute Name Description

labels.application_name Name of the application

labels.name Failed Custom Page Deployment

labels.relsvr_system Agents

labels.relsvr_subsystem Custom Page Deployment Manager

labels.relsvr_server_name [server-name]

labels.installation_date_time Installation date of the application

On this page

- Custom pages failed to install for at least one application

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

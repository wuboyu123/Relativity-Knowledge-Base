---
title: "BCP Directory Is Not Accessible"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/29045df8-efe8-47e7-96f0-87cd04bfa971.htm
collection: user
fetched_at: 2026-06-22T06:18:58+00:00
sha256: 4f4374e60899285a47979f1d97bc5b3e45a7e1a59832b93f098acc8290b4bd3d
---

BCP Directory Is Not Accessible Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

29045df8-efe8-47e7-96f0-87cd04bfa971

# BCP Directory Is Not Accessible

## Description

Triggered when the BCP directory is inaccessible due to permission restrictions or when the BCPPath directory is missing.

## Resolution Guidance

### Impact When Active

- File import/export operations will fail.

- If the BCP share becomes inaccessible, it will impact Processing, ARM, and Environment Watch, causing these components to malfunction or stop functioning properly.

- Users will be unable to proceed with jobs that depend on access to the BCP directory.

### How To Resolve

- Create a directory on the SQL Server in a location where the Relativity Service Account can read and write. Also ensure that SQL services have permissions to read from and write to this directory.

- Update permissions on the BCPPath file share.

- For more details, refer to Relativity Public Documentation to ensure the BCP share is correctly configured.

## Alert Details

### Alert Condition Details

Name Value Description

Rule Type Elastic Query

Data View metrics-*

Filter Query relsvr.sqlbcp_networkshare.accessible : * and labels.state : "inaccessible" BCP directory cannot be accessed

Group Count Above 0 documents

Threshold > 0 Count greater than 0 triggers the alert

Time Window 3 min Evaluates data from the last 3 minutes

Frequency 2 min Checks every 2 minutes

### Alert Metric Details

Metric Name:

relsvr.sqlbcp_networkshare.accessible

Metric Description:

Verifies whether the BCP share defined within the SQL Primary server is accessible from that server.

Metric Attributes:

Attribute Name Description Value

labels.mount_point Location of metrics \\emttest\\BCPPath

labels.relsvr_host_installed_products Products installed Invariant Queue Manager, Invariant Worker, Agent, Secret Store, Service Bus, Service Host, SQL Primary, Web

labels.relsvr_server_type Servers to be verified Agent, Invariant Queue Manager, Invariant Worker, SQL Primary, Secret Store, Service Bus, Service Host, Web

labels.state State of metrics accessible, inaccessible

service.language.name Language dotnet

service.name Service Name relsvr_infrawatch_agent

service.version Version V1

On this page

- BCP Directory Is Not Accessible

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

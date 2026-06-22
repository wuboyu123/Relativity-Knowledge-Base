---
title: "Integration Points Job Failure"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/a071a154-eb05-4f57-ae06-2ab7c5b82b49.htm
collection: user
fetched_at: 2026-06-22T06:18:48+00:00
sha256: f975ffb6b9b05cd741ef392005406a858e2470184854e10d32e89644ba9ff456
---

Integration Points Job Failure Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

a071a154-eb05-4f57-ae06-2ab7c5b82b49

# Integration Points Job Failure

## Description

This alert is triggered when a valid instance value is missing in the instance settings for Integration Points, or when the source and destination fields lack assigned control numbers.

## Resolution Guidance

### Impact When Active

- Import/Export job failures while running the job

### How To Resolve

-

Verify Instance Settings for Integration:

- Navigate to the Instance Settings tab.

- Search for:

- Name: RelativityInstanceURL

- Section: Relativity.Core

- Cross-reference this value with the current instance URL configuration.

- Search for:

- Name: WEBAPI

- Section: Integration

- Check if the URL follows the standard format (e.g., starts with http:// or https:// ).

-

Validate Field Mapping:

- Navigate to the Integration Points section.

- Initiate the creation of a new Integration Job.

- Complete Connect to Source sections and proceed to the Field Mapping stage.

- In the Field Mapping section, ensure that each Source Field is accurately mapped to the corresponding Destination Field, aligning both the field names and object types.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View metrics-*

Filter Query (relsvr.rip.job.relativity_sync : * and (labels.relsvr_rip_job_end_status_saved_search_natives_and_metadata: "Failed" or labels.job_end_status_saved_search_images: "Failed")) or (relsvr.rip.job.counter : * and (labels.name : "relsvr.rip.job.failed.count.ImportLoadFile" or labels.name : "relsvr.rip.job.validation_failed.count.ImportLoadFile"))

Group Count Above 0 documents

Threshold > 0 Count greater than 0 triggers the alert

Time Window 30 min Evaluates data from the last 30 minutes

Frequency 10 min Checks every 10 minutes

### Alert Metric Details

Metric Name:

relsvr.rip.job.relativity_sync, relsvr.rip.job.counter

Metric Description:

Tracks the number of Integration Points jobs that have failed, helping to monitor data transfer reliability and identify misconfigurations or missing mappings.

Metric Attributes:

Attribute Name Description

labels.relsvr.rip.job.end_status_saved_search_natives_and_metadata Integration Points export-to-workspace job end status

labels.name Integration Points import job end status

labels.executing_application Application Name

labels.relsvr_rip_job_execution_status RIP Job Status

On this page

- Integration Points Job Failure

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

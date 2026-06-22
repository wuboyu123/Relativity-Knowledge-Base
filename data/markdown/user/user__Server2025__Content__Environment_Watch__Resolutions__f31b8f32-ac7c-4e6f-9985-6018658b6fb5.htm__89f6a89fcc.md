---
title: "Workspace upgrade failed"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/f31b8f32-ac7c-4e6f-9985-6018658b6fb5.htm
collection: user
fetched_at: 2026-06-22T06:18:13+00:00
sha256: 42c901da53b61e6aa108d56e418b1618c3a62c9d593c09f695c6e0e9636d08f1
---

Workspace upgrade failed Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

f31b8f32-ac7c-4e6f-9985-6018658b6fb5

# Workspace upgrade failed

## Description

This alert is triggered when an error occurs upgrading workspace data or an application.

## Resolution Guidance

### Impact When Active

- System/User Experience Impact While Alert Is Active:

- Definite Impact: Users are unable to perform any workspace-related tasks within the application.

- Possible/Likely Impact: Certain application features or integrations may not function correctly.

### How To Resolve

- Go to the backend of the Relativity instance.

- Verify the 'kCura Service Host Manager' Windows service is running.

- If any one application is not working, restart the 'kCura Service Host Manager' Windows service.

- Wait for 6 min so that all applications/services are deleted and re-created.

- Refresh Kibana browser and the alert will be recovered.

## Alert Details

The alert is active when an error occurs upgrading workspace data or an application.

### Alert Condition Details

Name Value

Rule Type Log threshold

Data View Logs-*

Filter Query When the count OF LOG ENTRIES with a message that matches Relativity.Data.WorkspaceUpgradeException

Threshold > 0

Time Window 1 hour

Frequency 1 min

On this page

- Workspace upgrade failed

- Description

- Resolution Guidance

- Impact When Active

- How To Resolve

- Alert Details

- Alert Condition Details


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

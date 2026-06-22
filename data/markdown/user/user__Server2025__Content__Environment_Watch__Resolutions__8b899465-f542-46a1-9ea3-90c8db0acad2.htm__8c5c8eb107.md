---
title: "Kepler service failed to start after three attempts"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/8b899465-f542-46a1-9ea3-90c8db0acad2.htm
collection: user
fetched_at: 2026-06-22T06:19:27+00:00
sha256: 1d9855b4b32a12dc0357ee38d162646245a15a7e6fc69b026ac59526000cc671
---

Kepler service failed to start after three attempts Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

8b899465-f542-46a1-9ea3-90c8db0acad2

# Kepler service failed to start after three attempts

## Description

This alert is triggered when a Kepler Service has failed to start after three attempts.

### Impact When Active

-

When the Service Host starts up, it creates a Kepler Service for each associated application. Each Kepler Service process includes an automatic retry mechanism that attempts to restart the service if it fails during initialization. The Service Host will attempt up to three restarts. If all three attempts fail, it will stop retrying, and no further automatic restart will occur.

-

Any functionality associated with the affected application will be unavailable.

-

API calls targeting the failed Kepler Service will not be processed.

-

In other words, there will be issues with running any Relativity application functionality or making any API calls to the Kepler Service that is not running.

### How To Resolve

- Go to the Backend of the Relativity instance.

- Verify the 'kCura Service Host Manager' Windows service is running.

- If any one application not working, restart the 'kCura Service Host Manager' Windows service.

- Wait for 6 min so that all applications/services are deleted and recreated.

- Refresh Kibana browser and the alert will be recovered.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View Logs-*

Filter Query labels.event_type :"health_check" AND labels.status_state: "unhealthy" AND labels.event_source :"relsvr.servicehost" AND labels.name:"relsvr.servicehost.startup_service.failure"

Threshold > 0

Time Window 5 min

Frequency 1 min

On this page

- Kepler service failed to start after three attempts

- Description

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

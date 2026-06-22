---
title: "Application Installation Manager is unhealthy"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/d212d142-8150-4f59-87c6-fc8f06fe41c8.htm
collection: user
fetched_at: 2026-06-22T06:18:10+00:00
sha256: 9d5312a72480abef88f53a01dc3e1c977c1f5d411b56c6ce62ccd37c3ae6579a
---

Application Installation Manager is unhealthy Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

d212d142-8150-4f59-87c6-fc8f06fe41c8

# Application Installation Manager is unhealthy

## Description

This alert is triggered when a Relativity application fails to install or deploy successfully within an environment. This may occur due to missing dependencies, configuration issues, or permission errors. A failed installation can prevent the application from functioning as intended.

## Resolution Guidance

### Impact When Active

- Relativity applications and custom solutions cannot be installed, upgraded, or uninstalled.

- Deployment of event handlers, custom pages, or agents may fail, especially during workspace or application setup.

### How To Resolve

- Click on the Alert link in Relativity to go to the Kibana search named [Relativity] Application Installation Manager is unhealthy to view relevant logs and metrics.

- Review the logs for errors or exceptions related to application installation failures.

- Take appropriate action based on the identified error — this may include correcting configuration, resolving permission issues, etc.

- Ensure the Application Installation Manager agent is enabled and actively checking in.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Log threshold

Data View logs-*

Filter Query labels.event_type : "health_check" AND labels.event_source : "relsvr.ads.application.install" AND labels.name : "relsvr.ads.application.install.failed"

Group Count

Threshold > 0

Time Window 1 hour

Frequency 1 min

### Alert Metric Details

Metric Name:

Metric Description: Alert triggers on Application installation failure.

Metric Attributes:

Attribute Name Description

labels.event_source Event Source Name

labels.event_type Event Type

labels.name Health Check Name

labels.status_state unhealthy/healthy

On this page

- Application Installation Manager is unhealthy

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

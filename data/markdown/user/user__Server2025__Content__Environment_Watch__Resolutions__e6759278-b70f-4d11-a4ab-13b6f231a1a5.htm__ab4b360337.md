---
title: "HTTP API - at least one endpoint is not responding"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/e6759278-b70f-4d11-a4ab-13b6f231a1a5.htm
collection: user
fetched_at: 2026-06-22T06:19:23+00:00
sha256: c1f96c437527ba9432420f25e98449260ba64a0d924b5ff9fe9a4ef44e31c51f
---

HTTP API - at least one endpoint is not responding Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

e6759278-b70f-4d11-a4ab-13b6f231a1a5

# HTTP API - at least one endpoint is not responding

## Description

This alert is triggered when an HTTP request to an application or service returns a non-successful status code.

## Resolution Guidance

### Impact When Active

When an HTTP API endpoint is not responding or returning non-successful status codes, the affected application or service will be unable to process requests. This can result in failed operations, user-facing errors, inability to access specific features, and potential disruption to workflows that depend on the affected endpoint.

### How To Resolve

- Identify which host(s) are experiencing the HTTP API endpoint failure from the alert details in Kibana.

- Log into the affected host (Agent or Web server).

- Locate the 'kCura Service Host Manager' Windows service and verify its status.

- If the service is stopped, restart the 'kCura Service Host Manager' Windows service on the affected host.

- Verify the alert has recovered in Kibana.

## Alert Details

### Alert Condition Details

Name Value

Rule Type Elasticsearch Query

Data View metrics-*

Filter Query NOT numeric_labels.http_status_code : 200 and httpcheck.status: *

Threshold > 0

Time Window 5 min

Frequency 1 min

### Alert Metric Details

Metric Name: NOT numeric_labels.http_status_code : 200 and httpcheck.status: *

Metric Description: Alert triggers when HTTP request to application/service returns a non-successful status code (any code other than 200, which indicates a successful request).

Metric Attributes:

Attribute Name Description

labels.http_url HTTP request endpoint (Example: http://emttest/relativity.rest/api/massoperation/v1/mass%20operation%20manager/getkeplerstatusasync)

httpcheck.status HTTP request status (0/1)

numeric_labels.http_status_code Status code of HTTP request (200/404/500)

labels.http_status_class HTTP request stages (1XX/2XX/3XX/4XX/5XX)

On this page

- HTTP API - at least one endpoint is not responding

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

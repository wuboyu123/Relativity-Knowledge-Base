---
title: "HTTP API - at least one endpoint is not responding"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/e6759278-b70f-4d11-a4ab-13b6f231a1a5.htm
collection: user
fetched_at: 2026-06-22T06:19:23+00:00
sha256: c1f96c437527ba9432420f25e98449260ba64a0d924b5ff9fe9a4ef44e31c51f
---

HTTP API - at least one endpoint is not responding

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

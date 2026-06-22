---
title: "HTTP Health Check - at least one application endpoint failed"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/bfec0546-118b-453e-a058-e64038639084.htm
collection: user
fetched_at: 2026-06-22T06:19:24+00:00
sha256: 7dfa856880eebaaa83d4103bf15b01db6304ba10125459f26b5d6e4dede90d30
---

HTTP Health Check - at least one application endpoint failed

bfec0546-118b-453e-a058-e64038639084

# HTTP Health Check - at least one application endpoint failed

## Description

This alert is triggered when a health check, which is a special HTTP request that is designed to assess application health, returns a status code other than 200.

## Resolution Guidance

### Impact When Active

When this alert is triggered, actions involving the application that has failing the HTTP health check request may error out depending on the nature of the HTTP endpoint failure with regard to its health check. This may cause issues and failures to the end user and any Relativity Application that they are using.

### How To Resolve

- Review logs by host name and application to identify the endpoint that is failing.

- Restart the service that the HTTP endpoint is failing in.

- If you are going to restart services, make sure there are no active jobs running for that service.

- If you restart the services on a web server, then you are going to disrupt your users. Make sure you warn them or notify them that there will be a disruption to the application.

- You can try:

- There is a possibility that the service is running but the HTTP health check is returning an error. If that is the case, you can restart the one specific service that the health check alert is coming from. You can only do this if the service process is running.

- Follow the instructions found on this page to read more on how to do this: Server - How to view Kepler micro-services on an Agent or Web Server

- You may just want to restart the service.

## Alert Details

The alert is active for the following conditions in Relativity:

- When an HTTP Health Check Request has failed and returns status code other than 200.

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View metrics-*

Filter Query NOT numeric_labels.http_status_code : 200 AND labels.http_url : imaging%20health%20check%20service AND httpcheck.status: *

Threshold > 0

Time Window 5 min

Frequency 1 min

### Alert Metric Details

Metric Name:

- NOT numeric_labels.http_status_code : 200 AND labels.http_url : imaging%20health%20check%20service AND httpcheck.status:

Metric Description:

- This metric monitors HTTP response status codes for an application endpoint. The alert triggers when the status code is anything other than 200 , indicating a potential service failure or unavailability.

Metric Attributes:

Attribute Name Description

labels.http_url HTTP request endpoint

httpcheck.status HTTP request status

numeric_labels.http_status_code Status code of HTTP request

labels.http_status_class HTTP request stages

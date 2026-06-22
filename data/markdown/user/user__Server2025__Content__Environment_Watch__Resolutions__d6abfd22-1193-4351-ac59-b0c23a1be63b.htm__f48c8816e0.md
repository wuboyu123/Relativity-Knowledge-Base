---
title: "One or more expected Kepler application services are not available"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/d6abfd22-1193-4351-ac59-b0c23a1be63b.htm
collection: user
fetched_at: 2026-06-22T06:19:26+00:00
sha256: a784d60ccbe0184f2b07ebe014a72abedb228d04f197a32b4c21d9ff2ce1c3de
---

One or more expected Kepler application services are not available

d6abfd22-1193-4351-ac59-b0c23a1be63b

# One or more expected Kepler application services are not available

## Description

This alert is triggered when one or more expected Kepler application services are not available

## Resolution Guidance

### Impact When Active

- API calls to the affected Kepler service will fail.

- Any associated Relativity application functionality dependent on that service will also fail.

- If not resolved, this may result in application-level outages or degraded user experiences.

### How To Resolve

- Go to the host where the alert was triggered.

- Open the Services control panel on the host.

- Locate the kCura Service Host Manager Windows service.

- If any Kepler application/service is not running, restart the kCura Service Host Manager service.

- Wait approximately 5 minutes to allow all services to be deleted and recreated.

- Refresh Kibana or your monitoring dashboard to verify the alert clears. Note: Ensure there are no active processing jobs are running when restarting the Service Host Manager as this will disrupt ongoing processing. Imaging Jobs: OCR Jobs PDF Generation Jobs Processing Jobs Export Jobs Relativity Analytics Jobs Database Cleanup or Housekeeping Jobs Custom Agent Jobs

- Navigate to the Agents tab in Relativity.

- Filter by the affected Agent Server.

- Investigate the Last Message field for each agent:

- Working agents should display: working on job in workspace

- Idle agents will display: Completed

## Alert Details

This alert is triggered for the following condition in Relativity:

- When one or more expected Kepler application services are not available.

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View logs-*

Filter Query labels.event_type :"health_check" AND labels.status_state: "unhealthy" AND labels.event_source :"relsvr.servicehost" AND labels.name:"relsvr.servicehost.retry"

Group Count

Threshold > 0

Time Window 5 min

Frequency 1 min

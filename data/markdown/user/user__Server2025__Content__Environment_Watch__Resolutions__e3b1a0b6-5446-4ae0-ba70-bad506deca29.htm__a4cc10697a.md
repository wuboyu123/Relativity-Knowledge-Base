---
title: "Bootstrap Failure"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/e3b1a0b6-5446-4ae0-ba70-bad506deca29.htm
collection: user
fetched_at: 2026-06-22T06:18:51+00:00
sha256: dacf5e9188f7b6bd1bd1e05f523de9cbe390e74be79caa56da9af9ec6340dbc4
---

Bootstrap Failure

e3b1a0b6-5446-4ae0-ba70-bad506deca29

# Bootstrap Failure

## Description

This alert is triggered when a Relativity service is starting up, and fails to initialize an essential component. Here are a few of the essential components:

- The SQL connection used by the Relativity service

- The component used to read instance settings

## Resolution Guidance

### Impact When Active

- A BootstrapException logged in the Windows event logs indicates a fatal error initializing essential components during startup of a Relativity Service.

- This error suggests a critical issue that requires immediate attention.

- Due to this error, workspaces may not appear after logging in.

- Consequently, there will be issues with running any application functionality.

### How To Resolve

- Go to the backend of the Relativity instance.

- Locate 'kCura Service Host Manager' Windows service is up and running

- If any one application/service is not working, restart the 'kCura Service Host Manager' Windows service.

- Wait for 5 minutes so that all applications/services are deleted and recreated.

- If the error still persists, please contact customer support, since it is a bootstrapping error.

## Alert Details

The alert is active for the following condition in Relativity:

- When a BootstrapException is logged in the Windows event logs. This indicates a fatal error during the bootstrapping process, suggesting a critical issue that requires immediate attention.

### Alert Condition Details

Name Value

Rule Type Elastic Query

Data View logs-*

Filter Query message: BootstrapException and message: The bootstrap operation failed

Group Count

Threshold > 0 Count greater than 0, alert triggers

Time Window 1 hour Verified data for last 1 hour

Frequency 1 min Checks for every 1 minute

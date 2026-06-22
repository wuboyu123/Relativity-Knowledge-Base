---
title: "Billing Data Transmission"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Guides/Billing_Data_Transmission.htm
collection: user
fetched_at: 2026-06-22T06:19:46+00:00
sha256: 9ec9708dfc44a554b94e85cc757d18682130ab76737fe71f3001da8e4c5c9888
---

Billing Data Transmission

# Billing Data Transmission

This dashboard monitors the health and activity of Relativity's Billing Agent and Telemetry Metrics Transmission Agent. These components are critical for transmitting billing and telemetry data to ensure accurate licensing and system reporting. By surfacing agent status and recent transmission activity, this dashboard helps administrators quickly identify issues that could impact billing or restrict access to the Relativity instance.

## Agent Status and Transmission Overview

This overview offers visibility into key operational indicators for the environment, including agent activity, recent data transmission status, and whether online billing is currently enabled. Users can use these indicators to validate that billing and telemetry processes are running as expected and to quickly detect failures that require intervention.

### Use Cases

Use Case Description

Troubleshooting Transmission Failures Identify when billing or telemetry data has not been successfully transmitted and take corrective action before it impacts licensing or access.

Monitoring Agent Health Confirm that both Billing and Telemetry Transmission agents are active and functioning, reducing the risk of unexpected downtime.

Post-Installation Validation Verify that billing and telemetry components are correctly configured and operational after a new installation or upgrade.

Compliance and Audit Readiness Ensure accurate billing data transmission for licensing compliance and maintain records for audit purposes.

### Associated Alerts

- Billing Agent has failed in at least one workspace

- Telemetry metrics have not been transmitted in more than 24 hours. You have less than 7 days to correct the issue before Relativity access is disabled

---
title: "Billing Agent has failed in at least one workspace"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/10795d9f-f9c7-472f-80e6-f3e7c8f80e16.htm
collection: user
fetched_at: 2026-06-22T06:18:30+00:00
sha256: 586bbc85dd47e2652f95e4d5371672c485a4e81bc9bcaec58171cf20880ea4bd
---

Billing Agent has failed in at least one workspace

10795d9f-f9c7-472f-80e6-f3e7c8f80e16

# Billing Agent has failed in at least one workspace

## Description

This alert is triggered when the Billing Agent fails to collect system usage and billing data from at least one workspace.

## Resolution Guidance

### Impact When Active

The Billing Agent collects system usage and billing information for Relativity. This agent must be enabled to keep your Relativity access enabled. If the Billing Agent data is not collected for seven days, Relativity access becomes restricted. This will happen whether you are using the online billing method (using the Telemetry Metrics Transmission Agent) or offline billing method (emailing the Billing Statistics scripts outputs to Relativity). Once access has been restricted, only system admins are able to access the system. Other users are locked out. This limited access allows administrators to log in to Relativity and address the problem, for example, by re-enabling the agent.

Billing Agent failure scenarios include:

- The Billing Agent fails to start.

- The Billing Agent starts, but fails to record data for one or more workspaces. This is most commonly due to timeouts, but could be due to workspace databases becoming unavailable or issues with the data in the workspace.

### How To Resolve

Auto-retry : If the Billing Agent fails on a workspace, it moves on to the next workspace. If the agent is still running in off-hours, it retries the workspace(s) that failed.

If auto-retires continue to fail you can try...

- Verify that all workspace-connected databases are online.

- Review log entries on the Billing and Telemetry Metrics Transmission Agent dashboard to identify other potential problems impacting the Billing Agent. The dashboard will show you what workspaces experienced failures and additional details about the workspace-level failures.

- If the billing report queries consistently fail and there are SQL timeout errors in the log, you can use the LongRunningCaseStatisticsQueryTimeout instance setting to increase the timeout value.

- Force a retry. You should only try this measure during normal business hours if you are completely locked out of Relativity. Otherwise, perform the following procedure during low activity hours, because it slows down ongoing processes in your environment and requires a restart of the kCura EDDS Agent Manager service. Use this procedure to run the Billing Agent:

- Log in to Relativity.

- Select the Agents tab.

- Disable the Billing Agent if it is enabled.

- Update the 'AgentOffHourEndTime' Instance Setting value to 23:00:00.

- On the Agents tab in Relativity, enable the Billing Agent.

- On the agent server where the Billing Agent resides, restart the kCura EDDS Agent Manager Windows Service.

- Verify the Billing Agent has run by checking the Event Viewer on the agent server or that the alert is no longer active. If neither has happened, check back in an hour before moving on. You may need to log out and then log back into Relativity to clear the alert.

- Set the AgentOffHourEndTime to the original time before modification. By default, this is set to 05:00:00

## Alert Details

### Alert Condition Details

Name Value

Rule Type Metric threshold

Group max Failed workspaces

Threshold > 0 more than 0, alert triggers

Time Window 30 min Verified data for last 30 minutes

Frequency 1 min Checks for each 1 minute

### Alert Metric Details

Metric Name: relsvr.billing.agent.failed_workspaces

Metric Description: Alert triggers on when the Billing agent is unable to communicate with the failed workspaces.

Metric Attributes:

Attribute Name Description

labels.name Setting Name

labels.relsvr.billing.agent.failed_workspaces_details Failed workspaces details

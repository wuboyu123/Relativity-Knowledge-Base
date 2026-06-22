---
title: "Billing Agent"
url: https://help.relativity.com/Server2025/Content/Relativity/Metrics/Billing_Agent.htm
collection: user
fetched_at: 2026-06-22T06:04:27+00:00
sha256: 26551b882e22525d7d966fe9b5887ea1e460d9c8dc1fc4aae9241e110ff0fa3d
---

Billing Agent

# Billing Agent

The Billing Agent, formerly known as Case Statistics Manager agent, collects system usage and billing information for Relativity . This agent must be enabled to keep your Relativity access enabled.

This page contains the following information:

- Billing data settings

- Troubleshooting Billing Agent

- Restricted Relativity access

See these related pages:

- Telemetry

- Billing reports

## Billing data settings

If your company does not need us to include user, case, matter, or client names on your Relativity invoices for your own billing or record-keeping purposes, you can use Relativity instance settings to obfuscate them. Common reasons for not obfuscating include billing users and/or workspaces to your customers and ease of managing your user base. We recommend that you consult with your finance/billing department and those who manage your Relativity user base before making changes to the default values.

The instance settings are as follows:

- ReplaceCaseNameWithArtifactID - determines whether case names are replaced by case artifact IDs.

- ReplaceUserNameWithHashValue - determines whether the username portions of user email addresses are replaced by hash values. If you have multiple Relativity instances, the value of ReplaceUserNameWithHashValue must be the same across all instances in order for us to properly calculate and bill your users.

- ReplaceClientNameWithHashValue and ReplaceMatterNameWithHashValue - determines whether the client and matter names are replaced by hash values

- LockoutNotificationList - Defines the distribution list for emails warning of a case statistics-based or license-based lockout. For more information, see our Community article on setting up billing contacts to receive alerts.

You can also use the AgentOffHourStartTime and AgentOffHourEndTime to change the off-hours for running the Billing Agent.

If the billing report queries consistently fail and there are SQL timeout errors in the log, you can use the LongRunningCaseStatisticsQueryTimeout instance setting to increase the timeout value.

## Troubleshooting Billing Agent

Billing Agent failure scenarios include:

- The Billing Agent fails to start.

- Individual SQL methods in the agent timeout resulting in the total failure of the agent.

- The Billing Agent attempts a retry on workspaces that initially failed while still in off-hours and workspace(s) fail again.

### Auto-retry

If the Billing Agent fails on a workspace, it moves on to the next workspace. If the agent is still running in off-hours, it retries the workspace(s) that failed. If the workspace(s) still fail, the CSV file is not generated and the billing file is not be produced.

### Billing Agent alerts

If Billing Agent fails to complete a report for any of the workspaces in your environment, an alert appears in the Alerts section. The alert lists the failed workspaces and the date the agent failed.

Billing Agent alerts are visible only to admin users.

If workspace count is less than or equal to five (5):

```text
The Billing Agent failed for workspaces XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX on 10/31/2016.
```

If workspace count is greater than five:

```text
The Billing Agent failed for 17 workspaces on 10/31/2016.
```

The Billing Agent is not disabled upon failure. The alert will be reset once the agent runs again. Detailed information on Billing errors can be found on the Errors tab. For more information, see Errors . You can find even more granular information in the Relativity logs. For more information, see Logging .

## Restricted Relativity access

If the Billing Agent data is not sent for seven days, Relativity access becomes restricted. Once access has been restricted, only system admins are able to access the system. Other users are locked out. This limited access allows administrators to log in to Relativity and address the problem, for example, by re-enabling the agent.

Once the billing data is sent, access returns to normal.

If the Billing Agent fails to generate and send data for all workspaces during the off-hour run, admin users are notified.

To set or update your billing contact, contact Relativity Support .

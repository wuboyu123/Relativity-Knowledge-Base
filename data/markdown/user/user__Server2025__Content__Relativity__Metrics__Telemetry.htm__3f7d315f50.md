---
title: "Telemetry and metrics"
url: https://help.relativity.com/Server2025/Content/Relativity/Metrics/Telemetry.htm
collection: user
fetched_at: 2026-06-22T06:17:15+00:00
sha256: c137049a86f3d3c54dc9493c60a0b6bd8171789cd2a9b224b10990887b8389c3
---

Telemetry and metrics Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Telemetry and metrics

Relativity includes functionality for collectingusage, and billing data. Usage metrics are automatically transmitted to Relativity for analysis and application enhancement purposes. Relativity also collects billing data including the number of active users in your environment.

Telemetry is a required Relativity application that collects metrics:

- System usage metrics – Telemetry collects system usage metrics and securely sends the data to Relativity to improve the quality and performance of Relativity applications.

- Billing data – Telemetry also collects and sends billing data to Relativity .

Telemetry collects billing data and system usage metrics with the Billing Agent. For more information, see Billing Agent .

## Configuring telemetry

All versions of Relativity:

- Billing Agent must be running.

- The server hosting the Telemetry Metrics Transmission agent must be able to send outbound HTTPS requests to update.kcura.com . If necessary, make necessary changes to your firewall settings.

- The Telemetry Metrics Transmission agent must be running. It is automatically added to the Agents tab at the instance level. The agent uses the same setup as your Billing Agent server and resource pool configuration.

You can use the Telemetry Smoke Test Relativity script to verify that telemetry is properly configured in your environment. For more information, see Telemetry Smoke Test .

## Configuring metrics collection

You can configure the metrics that you want to collect by updating specific values for instance settings, and running scripts to enable the collection of metrics for specific applications.

### Enabling metrics categories

Depending on the version of Relativity, you can enable specific metrics categories and exclude the ones you don't need.

The settings in the EDDSMetrics.Whitelist table control whether Relativity collects metrics for a specific application, for example, Processing. This table is added to your Relativity environment when you install Relativity. It contains all enabled metrics categories. For more information about configuring metrics, contact Customer Support .

### Obfuscating metrics

If your company does not need us to include user, case, matter, or client names on your Relativity invoices for your own billing or record-keeping purposes, you can use Relativity instance settings to obfuscate them. Common reasons for not obfuscating include billing users and/or workspaces to your customers and ease of managing your user base. We recommend that you consult with your finance/billing department and those who manage your Relativity user base before making changes to the default values.

The instance settings are as follows:

- ReplaceCaseNameWithArtifactID - determines whether case names are replaced by case artifact IDs.

- ReplaceUserNameWithHashValue - determines whether the username portions of user email addresses are replaced by hash values. If you have multiple Relativity instances, the value of ReplaceUserNameWithHashValue must be the same across all instances in order for us to properly calculate and bill your users.

- ReplaceClientNameWithHashValue and ReplaceMatterNameWithHashValue - determines whether the client and matter names are replaced by hash values

- LockoutNotificationList - Defines the distribution list for emails warning of a case statistics-based or license-based lockout. For more information, see our Community article on setting up billing contacts to receive alerts.

## Telemetry lockout

Telemetry is used to collect and transmit billing data to Relativity . This functionality exists in parallel with Billing Agent. For more information, see Billing Agent .

Failure to transmit telemetry billing data to Relativity causes Relativity access to be disabled after seven (7) days. Telemetry lockout is similar to Billing agent lockout. If your security setup doesn't allow access to public internet, contact Relativity support to configure offline-billing.

A notification of metrics transmission failure is displayed in Alerts:

Metrics transmission failure can be caused by network access problems. It can also be caused by Relativity services failures on the telemetry agent server.

To troubleshoot metrics transmission failure:

- Review Relativity logs. Look for error related to Metrics Transmission Agent. In most cases, the error message and the exception stack trace can point you to the cause of the failure. You can also use the Errors tab in Relativity.

- Verify that your network firewall rules allow outbound HTTPS traffic from the Telemetry Transmission agent server to update.kcura.com.

- Verify that Relativity services are running properly on the Telemetry agent server and that metrics are being logged.

- Verify that your network firewall rules allow outbound internet traffic from the telemetry agent server to the Relativity billing server.

- After you identified and corrected the problem, the telemetry agent will be automatically rerun and Relativity access will be restored. Note that the Metrics Transmission Agent must be set to Active and the Relativity Agent Manager service must be running.

On this page

- Telemetry and metrics

- Configuring telemetry

- Configuring metrics collection

- Enabling metrics categories

- Obfuscating metrics

- Telemetry lockout


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

---
title: "Telemetry metrics have not been transmitted in more than 24 hours. You have less than 7 days to correct the issue before Relativity access is disabled"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/414f4243-7b56-4150-8c6a-3f5884bc34ea.htm
collection: user
fetched_at: 2026-06-22T06:18:29+00:00
sha256: 37cf3fe5857359ab785dddd3b131474f53fcb3da19eb36cc33aa71d0f4e7b6f9
---

Telemetry metrics have not been transmitted in more than 24 hours. You have less than 7 days to correct the issue before Relativity access is disabled Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

414f4243-7b56-4150-8c6a-3f5884bc34ea

# Telemetry metrics have not been transmitted in more than 24 hours. You have less than 7 days to correct the issue before Relativity access is disabled

## Description

This alert is triggered when the "IsOnline" Instance setting is true and the Telemetry Metrics Transmission Agent has not successfully transmitted metrics to Relativity in more than 24 hours.

## Resolution Guidance

### Impact When Active

Telemetry is used to collect and transmit billing data to Relativity. Metrics transmission failure can be caused by network access problems. It can also be caused by Relativity services failures on the telemetry agent server. If telemetry is not sent for 7 consecutive days, Relativity access will be disabled. If not resolved, all non-admin users could be locked out of Relativity.

### How To Resolve

Does the instance have internet access?

-

If Yes:

- Confirm that the IsOnlineInstance instance setting is set to True.

- Ensure the Telemetry Metrics Transmission Agent is deployed in the environment.

- Verify that the agent has access to https://update.kcura.com over port 443 (HTTPS).

-

If No:

- Set the IsOnlineInstance instance setting to False.

- The Telemetry Metrics Transmission Agent can be safely removed from the environment.

- As theinstance does not have internet access, the billing data needs to be sent manually each month. To do this please export the results of the following scripts and submit them to the Relativity Billing team:

- Billing Statistics - Users

- Billing Statistics - Case Rollup

##### You can also try..

- If you're still running into issues, try the the steps from here .

## Alert Details

### Alert Condition Details

Name Value

Rule Type Metric threshold

Filter Query labels.relsvr_online_instance: "Yes"

Group max

Threshold > 24

Time Window 30 min Verified data for last 30 minutes

Frequency 15 min Checks for each 15 minute

### Alert Metric Details

Metric Name: relsvr.telemetry.metrics.last_transmission_hours

Metric Description: Alert triggers on when the 'IsOnlineInstance' instance setting is set to true AND when metrics have not been successfully submitted by the Telemetry Metrics Transmission Agent in more than 24 hours.

Metric Attributes:

Attribute Name Description

labels.name Setting Name

labels.relsvr_online_instance IsOnlineInstance instance setting

labels.telemetry.metrics.last_transmission_timestamp Last transmission timestamp

labels.telemetry.metrics.lockout_timestamp Lockout timestamp

On this page

- Telemetry metrics have not been transmitted in more than 24 hours. You have less than 7 days to correct the issue before Relativity access is disabled

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

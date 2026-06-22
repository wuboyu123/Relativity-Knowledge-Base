---
title: "Telemetry Smoke Test"
url: https://help.relativity.com/Server2025/Content/Relativity/Metrics/Telemetry_Smoke_Test.htm
collection: user
fetched_at: 2026-06-22T06:17:16+00:00
sha256: 31eb01059e035ea987642e0be99bbfe3652514da2d4679f328adbba615bafb52
---

Telemetry Smoke Test Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Telemetry Smoke Test

This test is used to verify that system usage metrics can be transmitted to Relativity . For information on telemetry configuration see Telemetry and metrics .

For Server 9.7 and later, telemetry can be verified by the following procedure:

- Disable the telemetry agent.

- Logout and log back in to Relativity.

- Enable the telemetry agent.

- After 15 seconds, refresh the page and observe the agent message:

- Success Condition - telemetry agent message is immediately updated to "Started." and after several seconds or minutes "Completed."

- Failure Condition - telemetry agent message is immediately updated to "Received error during transmission (retrying 1/10): An error occurred while sending the request." and after several minutes, "Transmission failed after 10 retries"

For Server versions earlier than 9.7, it is necessary to have access to SQL server to verify telemetry:

- Ensure that the telemetry agent is enabled.

- In SQL server, add a record to the metrics table using the following script:

```text
DECLARE @ID nvarchar(50) = convert(nvarchar(50), NEWID())
DECLARE @SmokeBucketName nvarchar(500) = 'SmokeTest.Telemetry'
DECLARE @Date nvarchar(50) = Convert (nvarchar(25), CONVERT (date, GETDATE(), 126)) + 'T00:00:00.0000000-00:00'
DECLARE @SmokeObjectValue nvarchar(MAX) = '{"MetricID":0,"ID":"'+ @ID +'","Timestamp":"'+ @Date +'","Bucket":"'+ @SmokeBucketName +'","WorkspaceGuid":"00000000-0000-0000-0000-000000000000","WorkflowID":"","MetricTarget":1,"MetricType":4,"Value":"Test"}'
INSERT INTO [EDDSMetrics].[eddsdbo].[Metrics] ([Bucket], [Object]) VALUES (@SmokeBucketName, @SmokeObjectValue)
SELECT TOP 1 [Bucket] FROM [EDDSMetrics].[eddsdbo].[Metrics] WHERE [Bucket] = @SmokeBucketName
```

- Wait 30 seconds for the telemetry agent is execute.

- Query the metrics table and verify that there are no records:

```text
SELECT TOP 1 [Bucket] FROM [EDDSMetrics].[eddsdbo].[Metrics] WHERE [Bucket] = 'SmokeTest.Telemetry'
```

- Success Condition - database has no records after being queried the second time.

- Failure Condition - the inserted record is not removed from the metrics table within the expected time.

On this page

- Telemetry Smoke Test


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

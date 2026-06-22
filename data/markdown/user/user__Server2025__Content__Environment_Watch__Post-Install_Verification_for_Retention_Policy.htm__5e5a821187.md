---
title: "Post-Install Verification for Retention Policy"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Post-Install_Verification_for_Retention_Policy.htm
collection: user
fetched_at: 2026-06-22T06:11:56+00:00
sha256: 6d3b855b6b4d4e916b396b12c9b2314679e6f395797edfb7433c2785d95020d8
---

Post-Install Verification for Retention Policy Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Post-Install Verification for Retention Policy

## Verify Retention Policy Configuration

This verification step confirms that the retention period (data lifecycle) is properly configured for your Application Performance Monitoring(APM) data streams.

## Verification Steps

-

Navigate to Kibana Dev Tools Console:

- Open Kibana in your web browser

- Click on Dev Tools in the left navigation menu

-

Run the following queries to verify retention policies for each data stream type:

### Verify Logs Retention Policy

Copy

```text
GET /_data_stream/logs-apm.app*?filter_path=data_streams.name,data_streams.lifecycle

```

### Verify Metrics Retention Policy

Copy

```text
GET /_data_stream/metrics-apm.app*?filter_path=data_streams.name,data_streams.lifecycle

```

### Verify Traces Retention Policy

Copy

```text
GET /_data_stream/traces-apm*?filter_path=data_streams.name,data_streams.lifecycle

```

## Expected Results

Each query should return the data stream names along with their configured lifecycle settings.

Sample Output:

Copy

```text
{

  "data_streams": [

    {

      "name": "logs-apm.app.relsvr_logging-default",

      "lifecycle": {

        "enabled": true,

        "data_retention": "90d",

        "effective_retention": "90d",

        "retention_determined_by": "data_stream_configuration"

      }

    }

  ]

}

```

## What to Check

- enabled : Should be true

- data_retention : Indicates the configured retention period (e.g., "30d" for 30 days, "90d" for 90 days)

If the lifecycle settings don't match your expected configuration, you may need to update your retention period according to elasticsearch_retention_policy_guidelines.md .

On this page

- Post-Install Verification for Retention Policy

- Verify Retention Policy Configuration

- Verification Steps

- Verify Logs Retention Policy

- Verify Metrics Retention Policy

- Verify Traces Retention Policy

- Expected Results

- What to Check


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

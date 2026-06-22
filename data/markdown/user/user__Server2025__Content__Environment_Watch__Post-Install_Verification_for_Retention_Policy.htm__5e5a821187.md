---
title: "Post-Install Verification for Retention Policy"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Post-Install_Verification_for_Retention_Policy.htm
collection: user
fetched_at: 2026-06-22T06:11:56+00:00
sha256: 6d3b855b6b4d4e916b396b12c9b2314679e6f395797edfb7433c2785d95020d8
---

Post-Install Verification for Retention Policy

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

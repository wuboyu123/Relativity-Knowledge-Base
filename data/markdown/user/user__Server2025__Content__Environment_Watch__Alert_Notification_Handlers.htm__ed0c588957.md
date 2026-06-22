---
title: "Alert Notification Handlers"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Alert_Notification_Handlers.htm
collection: user
fetched_at: 2026-06-22T06:11:45+00:00
sha256: b552024d32f797b526fcbcd9e1dd2a324dfb1aadc67de742756bcccfffabbee6
---

Alert Notification Handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Alert Notification Handlers

The "handlers" allow a client to send alert notifications to the specified provider.

### Slack Handler

The Slack handler allows alerts to be sent to a designated Slack channel. Configuration options include:

Property Description

accessToken The Slack API token used for authentication.

acknowledgeAlertEnabled Boolean flag to enable/disable alert acknowledgment in Slack. This is by default false since implementation is not done.

channel The Slack channel ID where alerts will be posted.

enabled Boolean flag to enable/disable Slack notifications.

messageIntervalSeconds Interval (in seconds) between alert messages sent to Slack. It should be greater than or equal to the minimum Slack interval in seconds, i.e., 180.

### Configure Slack in Custom JSON Configuration File

#### Prerequisites

Before configuring Slack notifications:

- Create a Slack App in your Slack workspace.

- Generate a "Bot User OAuth Token" with the required permissions to post messages to channels.

#### Configuration

To configure Slack notification in the custom JSON configuration file, locate the alertNotificationHandlers section and update the configuration as below.

Copy

```text
{

  "environmentWatchConfiguration": {

    "monitoring": {

      "instance": {

        "sources": {

          "certificates": {},

          "windowsServices": {

            "enabled": false,

            "include": []

          }

        },

        "otelCollectorYamlFiles": []

      },

      "installedProducts": [

        {

          "productName": "Agent",

          "sources": {

            "certificates": {

              "enabled": true,

              "include": []

            },

            "windowsServices": {

              "enabled": true,

              "include": []

            }

          },

          "otelCollectorYamlFiles": []

        }

      ],

      "hosts": [

        {

          "hostName": "emttest",

          "sources": {

            "certificates": {

              "enabled": true,

              "include": []

            },

            "sqlServers": {

              "enabled": false,

              "include": []

            },

            "windowsServices": {

              "enabled": false,

              "include": []

            }

          },

          "otelCollectorYamlFiles": []

        }

      ]

    },

    "alertNotificationHandlers": {

            "slack": {

                "accessToken": "Bot User OAuth Token",

                "acknowledgeAlertEnabled": false,

                "channel": "slack-channel-id",

                "enabled": true,

                "messageIntervalSeconds": 60

            }

        }

  }

}

```

### Verification in Kibana

- Navigate to Kibana Dashboard.

- Select Alerts Overview Dashboard, observe for any triggered alerts.

- Verify the Slack notifications are received in the specified Slack channel.

### Slack Notification Example

## Troubleshooting

Refer to the Troubleshooting Guide to resolve any custom JSON slack configuration issues.

On this page

- Alert Notification Handlers

-

- Slack Handler

- Configure Slack in Custom JSON Configuration File

- Verification in Kibana

- Slack Notification Example

- Troubleshooting


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

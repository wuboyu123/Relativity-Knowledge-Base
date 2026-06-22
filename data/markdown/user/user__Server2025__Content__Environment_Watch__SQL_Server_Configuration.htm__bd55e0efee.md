---
title: "SQL Server Configuration"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/SQL_Server_Configuration.htm
collection: user
fetched_at: 2026-06-22T06:11:46+00:00
sha256: 89bdf5b194e17040d2e6d17bebbafc808a3ac375e1343cc3e0f8e5051d73d5c7
---

SQL Server Configuration Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# SQL Server Configuration

Use the steps below only to explicitly configure SQL Server instances or if the environment uses SQL cluster servers for Environment Watch monitoring.

SQL Primary and SQL Distributed instances are auto-configured by default; however, this feature also allows for manual configuration of the instances. Monitoring these instances using the Environment Watch Windows service requires defining specific configurations in a custom JSON configuration file.

## Configure SQL Server Instances

Define SQL server configuration in the custom JSON configuration file within the " hosts " section.

SQL server configuration in the custom JSON configuration file must always be specified within the " hosts " section.

Locate the " hosts " section in the JSON file and add an entry for each SQL server instance to be monitored. Include each hostName with the following details:

Example: For an environment containing a SQL server with two nodes ( SQLNode1 and SQLNode2 ):

Update the "hosts" section for each node by:

- Specify the correct host name

- Set the enabled flag to true

- Specify the appropriate SQL server/cluster name ( clusterVirtualName )

- Provide the corresponding instance name ( instanceName )

- Below configuration sets both SQLNode1 and SQLNode2 nodes to monitor the SQL server instance SQL_INSTANCE with the virtual cluster name SQLCLUSTER .

Copy

```text
{

  "environmentWatchConfiguration": {

    "monitoring": {

      "instance": {

        "sources": {

          "certificates": {},

          "windowsServices": {}

        },

        "otelCollectorYamlFiles": []

      },

      "installedProducts": [

        {

          "productName": "Agent",

          "sources": {

            "certificates": {},

            "windowsServices": {}

          },

          "otelCollectorYamlFiles": []

        }

      ],

      "hosts": [

        {

          "hostName": "SQLNode1",

          "sources": {

            "certificates": {},

            "sqlServers": {

              "enabled": true,

              "include": [

                {

                  "clusterVirtualName": "SQLCLUSTER",

                  "instanceName": "SQL_INSTANCE"

                }

              ]

            },

            "windowsServices": {}

          },

          "otelCollectorYamlFiles": []

        },

        {

          "hostName": "SQLNode2",

          "sources": {

            "certificates": {},

            "sqlServers": {

              "enabled": true,

              "include": [

                {

                  "clusterVirtualName": "SQLCLUSTER",

                  "instanceName": "SQL_INSTANCE"

                }

              ]

            },

            "windowsServices": {}

          },

          "otelCollectorYamlFiles": []

        }

      ]

    },

    "alertNotificationHandlers": {}

  }

}

```

If the environment does not use SQL server instances, then update enabled flag to false for all SQL server instances in the " hosts " section to disable SQL monitoring.

### Restart the Environment Watch Windows Service

After updating the environment-watch-configuration.json file with the SQL server configuration, save the changes, restart the Environment Watch Windows service to apply the changes. This ensures that the service reads the updated configuration and begins monitoring the specified SQL server instances.

Once the Windows service has been restarted, verify the SQL instances are being monitored correctly by checking the Environment Watch discover, dashboards for relevant metrics, alerts.

### Verification in Kibana

- Navigate to the Kibana SQL Dashboards.

- Verify data is being populated for all Kibana Dashboards.

- Navigate to Kibana Overview/Alerts.

- Verify that there are no alerts triggered.

## Troubleshooting

Refer to the Troubleshooting Guide to resolve any custom JSON SQL server configuration issues.

On this page

- SQL Server Configuration

- Configure SQL Server Instances

- Restart the Environment Watch Windows Service

- Verification in Kibana

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

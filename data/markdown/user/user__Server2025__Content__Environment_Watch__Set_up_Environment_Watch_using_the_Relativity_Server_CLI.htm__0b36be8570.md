---
title: "Set up Environment Watch using the Relativity Server CLI"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Set_up_Environment_Watch_using_the_Relativity_Server_CLI.htm
collection: user
fetched_at: 2026-06-22T06:11:26+00:00
sha256: 139d8bca5dd596d463c4370fce711708d0a7b382477f88dae0a6cf4d190b1b12
---

Set up Environment Watch using the Relativity Server CLI Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Set up Environment Watch using the Relativity Server CLI

This step is required for Environment Watch.

It is recommended to run the CLI from the Primary SQL Server.

### Prerequisites

- Elastic Stack Certificates are installed on all Servers

- Verify that the Elastic Stack services (Elasticsearch, Kibana, and APM) are running

- Access to Elastic Stack, Primary SQL Server, and Secret Store (Whitelisted for Secret Store access. Please see here for information on whitelisting.)

- The Server-bundle zip file has been downloaded and extracted to `C:\Server.Bundle.x.y.z'

### Set up instructions

-

Open elevated command prompt/powershell. Run the below command. Select Environment Watch

Copy

```text
 C:\Server.Bundle.x.y.z\relsvr.exe setup

 Relativity Server CLI - 24.0.1196

 Copyright (c) 2025, Relativity ODA LLC

 What would you like to setup?

   DataGrid

 > Environment watch

   Exit

```

-

Confirm the Environment Watch setup.

Copy

```text
 Confirm you would like to perform the 'Environment Watch' setup [y/n] (y): y

```

-

Enter the required Relativity parameters.

Copy

```text
 Existing settings do not exist

 Enter the Relativity admin username (relativity.admin@kcura.com): relativity.admin@kcura.com

 Enter the Relativity admin password: *********

 Enter the Relativity instance url (https://emttest/Relativity): https://emttest/Relativity

 Relativity instance is verified

```

-

Enter the required Elastic Stack parameters.

Copy

```text
 Enter the Elasticsearch admin username (elastic): elastic

 Enter the Elasticsearch admin password: *********

 Enter the Elasticsearch cluster endpoint URL (https://emttest:9200): https://emttest:9200

 Elasticsearch cluster endpoint URL is verified

 Enter the Elasticsearch APM Server endpoint URL (http://emttest:8200): http://emttest:8200

 Enter the Elasticsearch Kibana endpoint URL (http://emttest:5601): http://emttest:5601

```

-

The CLI will now apply the necessary configurations. Please wait for the process to finish.

Copy

```text
 Elasticsearch Kibana URL is verified

 API Key creation and validation completed ------------------------- 100%

 OAuth2 client exists ---------------------------------------------- 100%

 Relativity secret store updated ----------------------------------- 100%

 Relativity logging updated ---------------------------------------- 100%

 Relativity toggles updated ---------------------------------------- 100%

 Relativity AppDomain monitoring enabled --------------------------- 100%

 APM settings updated ---------------------------------------------- 100%

 Elasticsearch indexes updated ------------------------------------- 100%

 Kibana Tag imported ----------------------------------------------- 100%

 Kibana IndexPattern imported -------------------------------------- 100%

 Kibana SavedSearch imported --------------------------------------- 100%

 Kibana Dashboard imported ----------------------------------------- 100%

 Kibana Alert imported --------------------------------------------- 100%

 Kibana Custom Role created. --------------------------------------- 100%

 Relativity installation SQL record updated ------------------------ 100%

 The Environment Watch setup has been completed. The Relativity Environment Watch installer package should now be installed within each server contained within this Relativity instance. As each server is setup for monitoring, restart all Relativity services within the machine including "kCura Edds Agent Manager," "kCura Edds Web Processing Manager," and "kCura Service Host Manager" to begin sending telemetry to Elasticsearch.

```

-

Successful completion indicates that Environment Watch is configured. The setup process will automatically retry three times on parameter entry errors before exiting. If it exits, the process must be restarted..

Refer to the Troubleshooting Guide if you encounter any issues.

## Next Steps

- Click here to continue Environment Watch Setup

On this page

- Set up Environment Watch using the Relativity Server CLI

-

- Prerequisites

- Set up instructions

- Next Steps


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

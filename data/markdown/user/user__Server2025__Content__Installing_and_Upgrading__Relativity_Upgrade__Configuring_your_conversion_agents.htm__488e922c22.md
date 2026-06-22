---
title: "Configuring your conversion agents"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Relativity_Upgrade/Configuring_your_conversion_agents.htm
collection: user
fetched_at: 2026-06-22T06:10:52+00:00
sha256: 94c4d5ff63439bb59ca710c8744988e083ec694807b44d31d00a6016aff39048
---

Configuring your conversion agents Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Configuring your conversion agents

When you convert a document in Relativity, that conversion job is performed by a dedicated conversion agent.

Server 2025 uses a message broker to submit conversion jobs and communicate with your designated conversion agents. You must install the message broker before you run your upgrade to Server 2025 . For more information, see Installing RabbitMQ .

If you have dedicated conversion workers, it's recommended that you re-purpose the dedicated workers as agent servers with a single conversion agent. For more information, see Re-purposing a conversion worker as a conversion agent.

If you have a Tier 1 or similar environment that does not have any Invariant workers dedicated solely to conversion, you can add a conversion agent to an existing agent server. Or you can allocate new hardware dedicated to conversion. For more information, see Adding conversion agents to an environment with no dedicated conversion workers.

## Conversion agent considerations

Consider the following about conversion agents when installing or upgrading to Server 2025 : On a new installation of Server 2025 , Relativity automatically creates one conversion agent and adds it to the default secondary agent server. You should then add the agent server to the appropriate resource pool. For more information, see Resource pools .

## Re-purposing a conversion worker as a conversion agent

If you have existing Invariant workers that Relativity uses solely for conversion, you can re-purpose your hardware to support conversion agents.

Do not follow these steps if your worker server handles more than just conversion jobs. You still need Invariant workers for other jobs such as Processing, Imaging, and Save as PDF.

To re-purpose a conversion worker as a conversion agent, perform the following steps:

These steps are only required if you're upgrading from Relativity 9.3 or lower, since conversion was performed by a worker in those versions, and only if your worker was designated for conversion.

- Ensure the message broker is installed in the environment.

- Uninstall Invariant on the server in the Windows Control Panel Add/Remove Programs. Doing this uninstalls existing Invariant applications.

- If it's still visible in the Server Management tab in Relativity, delete the old worker from that location.

- Set up a new agent server for conversion agents. For more information, see Infrastructure configuration . This process requires a manual copy of a valid SSL certificate to the agent server.

To set up the second agent server, perform the following steps:

- Edit the RelativityResponse.txt file to include only the lines enabled (=1).

INSTALLAGENTS = 1 in the feature section.

- Run the Relativity installer on the machine. For more information see, Agent installation .

## Adding conversion agents to an environment with no dedicated conversion workers

If your environment does not have any Invariant workers dedicated to conversion, you have two options when setting up conversion for Server 2025 .

### Adding a conversion agent to an existing server

You can add a conversion agent to one of your existing servers.

If you use this option, add the conversion agent to one of your lesser-used agent servers. You could also rearrange some of your existing agents between your agent servers, which dedicates more resources to conversion.

For greater control over the resources you allocate to conversion, you can also install a new agent server in a virtual machine and host a single conversion agent on that machine. For more information see, Agent installation .

### Allocate additional hardware to host a new agent server

You also have the option of allocating additional hardware to host a new conversion agent server. To allocate additional hardware, follow these steps:

- Ensure that the message broker is installed in the environment.

- Set up a new, secondary agent server for conversion agents. For more information, see Infrastructure configuration .

To set up a secondary agent server, perform the following steps:

- Ensure that the message broker is installed in the environment.

- Edit the RelativityResponse.txt file to include only the lines enabled (=1).

INSTALLAGENTS = 1 in the feature section.

- Run the Relativity installer on the machine. For more information see, Agent installation .

On this page

- Configuring your conversion agents

- Conversion agent considerations

- Re-purposing a conversion worker as a conversion agent

- Adding conversion agents to an environment with no dedicated conversion workers

- Adding a conversion agent to an existing server

- Allocate additional hardware to host a new agent server


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

---
title: "Installing to agent servers"
url: https://help.relativity.com/Server2025/Content/System_Guides/Agents_Guide/Installing_to_agent_servers.htm
collection: user
fetched_at: 2026-06-22T06:04:21+00:00
sha256: f357b98d23d571bcc7a6a8cfec9cb47b8ba9a4ecb0afa1affc8a5143a40ad06f
---

Installing to agent servers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Installing to agent servers

Every agent server runs the kCura EDDS Agent Manager Windows Service. This service launches the EDDS -> kCura.EDDS.AgentManager.exe Windows process. That single process manages and executes the Relativity agents which are assigned to that specific agent server.

During Relativity installation, you can select whether to install the Agent Service on your server. The server running the Agent Service functions as the primary agent server because it runs all of the single-installation agents. See Primary agent server .

When you edit the RelativityResponse.txt file set the DEFAULTAGENTS setting in the Agent Properties section to 1 to install the full set of default Relativity agents to your server. See Secondary agent server for more information.

The DEFAULTAGENTS setting only works during initial installation. This field is ignored on upgrade.

Using the Relativity user interface, you can add, modify, or delete Relativity agents from the server. See Managing agents in Relativity for more information.

To run a job in a workspace, you must have that particular agent running on the agent server assigned to the resource pool where your workspace resides. For example, if the Transform Set Manager agent is not present on any of the agent servers in the resource pool that houses your workspace, you won't be able to run a Transform Set job.

This applies to all agents except the Case Manager, Billing Agent, Group Membership Manager, Group Membership Worker, and File Deletion Manager. These agents run across the environment regardless of their assigned server and resource pool. For more information, see Agents and Billing Agent .

## Primary agent server

The primary agent server in a Relativity environment is intended to run one full set of agents, including both single-installation and multiple-installation agents. In addition to hosting a full set of agents, you can optionally configure your primary agent server to host secondary instances of the multiple-installation agents.

We recommend installing only one additional instance of each Branding Manager or Production Manager agent on your primary agent server. See List of agents for details.

## Secondary agent server

If you select the Include default agents check box during installation, the Relativity installation package installs the full set of agents on a secondary agent server. You can then manually remove the single-installation agents and add additional multiple-installation agents. You can add the Workspace Upgrade Manager agent to a secondary server, but you should install only a single agent of this type per environment.

You can add several of the following multiple-installation agents to each secondary agent server:

- Application Installation Manager

- AssistedReviewWorkerAgent

- Branding Manager

- dtSearch Index Worker

- OCR Worker

- Production Manager

- Content Analyst Index Manager

- Workspace Upgrade Worker

- Group Membership Manager

- Group Membership Worker

Secondary agent servers are commonly configured to run 2x quad-core processors. This configuration supports any combination of eight agents, such as four Branding Manager agents and four Production Manager agents.

In this example, the combined count of Branding and Production Managers can't exceed the total number of individual processor cores present on the server.

## Installing agent servers in a workgroup

After installing the Relativity agent server on a machine that is a part of a workgroup, start the kCura EDDS Agent Manager service under a Windows account that is a member of the Administrators group.

If your environment contains workspaces with Data Grid enabled fields, agent servers must have access to the endpoint URL on the Elasticsearch client node for dtSearch functionality.

## Adding an agent server to a resource pool

You need to add your agent server to a resource pool after you configure it. This step ensures that the agents on the server are available to run jobs.

- From Home , select the Resource Pools tab.

- Select the resource pool to which you want to add the workgroup server.

- In the Resource Pool information screen, go to the Agent Servers section and click Add .

- Select the NewAgentServerMachineName workgroup server, and then click OK .

-

When adding a new server to your resource pool, ensure that you apply the same hotfix to the new server that you may have applied to any existing Web or Agent Servers.

On this page

- Installing to agent servers

- Primary agent server

- Secondary agent server

- Installing agent servers in a workgroup

- Adding an agent server to a resource pool


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

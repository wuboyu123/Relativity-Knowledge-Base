---
title: "Adding and editing agents"
url: https://help.relativity.com/Server2025/Content/System_Guides/Agents_Guide/Adding_and_editing_agents.htm
collection: user
fetched_at: 2026-06-22T06:04:33+00:00
sha256: ede0ffc76731b85af86d88021587b3d3fa26dba8b920d83a11118d65e73d820c
---

Adding and editing agents

# Adding and editing agents

You can add new agents to accommodate a large number of jobs in the workspace. For instance, if you need to complete multiple large OCR jobs, you may need to add additional OCR worker agents to your environment.

## Adding agents

Before adding agents, be sure to read the agent instances guidelines. See Agent installation requirements .

To add an agent, perform the following steps:

- From Home , select the Agents tab.

- Click New Agent . The Agent Information screen displays.

- Complete all of the fields in the Agent Information section. See Fields for details.

- From the Enabled field, select Yes to enable the agent or No to create the agent without enabling it on the server.

- Click Save . If the agents were successfully added to the environment, you'll see a green check box and message at the top of the page.

Verify that the new agents appear on the Agents tab in Relativity. Each agent appears by agent type in the Name column, and the agent type is followed by the number of the agent type. For example, if you create two Analytics Categorization Manager agents, the first appears as Analytics Categorization Manager (1) and the second appears as Analytics Categorization Manager (2).

## Fields

The agent object fields are as follows:

- Agent Type - displays the Select Agent Type dialog, allowing you to select the appropriate agent type. Once the agent type is saved, it can't be changed.

- Number of Agents - contains the number of instances of this agent type that will be created. If you enter a number that would cause the agent to exceed its maximum agents per server value, you receive an error message and the new agent(s) won't be created.

When you create multiple instances of an agent type, each instance is named with a number following in parentheses. For example, the first instance of an OCR Manager agent is named OCR Manager (1). The second instance is named OCR Manager (2), and so on. Not all types of agents can have multiple instances.

- Agent Server - displays the Select Resource Server dialog, allowing you to select the server on which the agent will reside and click OK to return to the Agent Information screen.

After you select the agent type, only servers with a processing type that is compatible with the agent type appear in the Resource Server dialog. If you select the server first and then select an agent type that is not compatible, you receive an error message.

- Run Interval - The interval, in seconds, at which the agent should check the database for available jobs. It populates with a default value based on the agent type.

- Logging level of event details - specifies the types of events logged for the agent. It populates with a default selection based on the agent type. You can modify this setting by choosing from the following options:

- Log critical errors only - logs messages about critical system failures

- Log warnings and errors - logs messages about critical and non-critical service errors and disruptions in activity

- Log all messages - logs detailed messages about all errors and life cycle events

When the Log all messages option is selected, the Event Log is rapidly filled to capacity with detailed messages, which causes previous messages to be purged from the log. This option could result in error messages being purged before you have a chance to view the errors.

- Enabled - designates the agent instance as disabled or enabled.

## Editing or disabling agents

You can disable agents that aren't being used and later restart them. For example, you can disable agents on a retired server or enable OCR worker agents for new OCR jobs.

Disabled agents still exist on the server. They continue to use use disk and memory resources even though they don't execute jobs.

To edit or disable an existing agent, perform the following steps:

- From the Agents tab at Home , click the name of the agent you want to modify.

- From the Agent Information screen, click Edit . See Managing agents in Relativity for details on how agent actions are handled by the Agent Manager service.

- To edit an agent, change the information under Agent Information as necessary. See Fields for details.

- To disable an agent, go to the Status section and change the Enabled value to No .

- Click Save .

If you edit or disable an agent while another job is being processed, the change won't apply until after the that job completes.

## Restarting disabled agents

If an agent has been disabled for any reason, you can restart it in the Agents tab.

- From Home , select the Agents tab.

- Select the check box for each disabled agent that you want to restart.

- Click the Restart Disabled Agents button at the top of the Agents view.

This re-enables the agent and changes its value in the Enabled field to Yes .

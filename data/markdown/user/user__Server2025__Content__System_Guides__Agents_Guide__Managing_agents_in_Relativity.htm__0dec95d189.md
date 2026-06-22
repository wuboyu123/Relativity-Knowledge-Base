---
title: "Managing agents in Relativity"
url: https://help.relativity.com/Server2025/Content/System_Guides/Agents_Guide/Managing_agents_in_Relativity.htm
collection: user
fetched_at: 2026-06-22T06:04:37+00:00
sha256: eeab8f8f6facfccb2613da03e7017ee6ca1fa0cf0f29b2504feb58d648bc19cb
---

Managing agents in Relativity

# Managing agents in Relativity

You may need to monitor, edit, or disable agents for troubleshooting or to meet your environment's changing needs. Use the following best practices when working with agents:

- Perform agent modifications while agents are idle to minimize any potential issues.

- Only one person should be building, modifying, or interacting with any particular agent at a time.

- Understand how agent actions are handled by the Agent Manager Windows Service. See Agent Manager service .

If you're working with agents in a very large Relativity workspace, contact Relativity Support .

## Agent Manager service

When you add a new agent from the Relativity interface, the agent is immediately created on the server. Agent information is stored in the EDDS database, and the Agent Manager Windows Service manages the agents on your server.

When you modify agents from the Agents tab in the Relativity interface, values are updated in the database. The Agent Manager service reads this information from the database every five seconds. If agents have been created, updated, or deleted during the previous five seconds, the Agent Manager Windows Service retrieves this information from the database and makes the changes to the agents on your server.

The following sections describe how agent actions are handled by the Agent Manager Windows Service.

### Agent edits

Agent edits are as follows:

- Agent Server - if an agent is moved to another server in the database, the agent will finish the job that it's currently working on before the change takes effect.

- For example, if you move the agent from Server A to Server B, the Agent Manager service running on Server A checks to see whether the agent is executing any jobs. If the agent is currently executing a job, then it's not moved from Server A. The Agent Manager service will continue to check the agent at five-second intervals, and if the agent is finished executing its job, then it's removed from Server A and placed on Server B.

- Run interval - when you modify an agent’s interval, the interval is updated immediately on the server. Any time elapsed from the previous interval is applied toward the new interval. For example, if four minutes have elapsed on a five-minute interval, and you increase the interval to 10 minutes, then the agent will run again in six minutes.

- Logging level - when you change an agent’s logging level, it's updated immediately on the server.

- Enabled status - if an agent's Enabled status is changed to No, the agent will finish the job that it's currently working on before it is disabled.

### Agent deletes

When the Agent Manager Windows Service runs, any agents marked for deletion are checked to see if they're executing a job. If an agent marked for deletion is executing a job, then it's not deleted. The Agent Manager service will continue to check the agent at five-second intervals, and when the agent is finished executing its job, it is deleted.

### Pending updates

The Pending Action field on the agent item list indicates whether an agent is pending a change. The available statuses for this column include the following:

- Deleting - the agent will be deleted once the current job completes.

- Disabling - the agent will be disabled once the current job completes.

- Moving - the agent will be moved to the new server once the current job completes.

- Updating - the agent has been modified, but the change won't be made until the Agent Manager Windows Service runs again.

## Mass agent operations

Using the mass operations menu, you can copy, edit, or delete multiple agents at once. See also Adding and editing agents .

### Mass copy

To mass copy agents, complete the following steps:

- From Home , select the Agents tab.

- Select the agents you want to copy and select Copy from the drop-down menu.

- Click Go . The new agent instances display in the Agents list, numbered incrementally.

For example, if you copy the Branding Manager agent, Branding Manager (1) and Branding Manager (2) will display in your agents list.

If completing the mass copy operation would cause one or more agents to exceed their maximum agents per server value, then none of the selected agents will be copied and you'll receive an error message.

### Mass edit

Using the Edit mass operation, you can make the same change(s) to multiple agents at once. The following settings can be edited using this operation:

- Run interval

- Logging level of event details

- Status

To change the agent server, you must edit the agent manually. See Editing or disabling agents for more information.

To edit multiple agents at once using the mass operation menu, complete the following steps.

- From Home , select the Agents tab.

- Select the agents to edit and choose Edit from the drop-down menu.

- Click Go . The Edit Agents dialog displays.

- Select the check box to the left of the component to be edited, and enter or select the corresponding new value. See Fields for details.

- Click Save to apply the change and return to the Agents list.

### Mass delete

To delete one or more agents using the mass operation menu, complete the following steps.

- From Home , select the Agents tab.

- Select the agents you want to delete and select Delete from the drop-down menu.

- Click Go to flag the agents for delete from your environment.

## Uploading an assembly containing agent types

You can upload an assembly that contains agent types to Relativity. See Resource files for steps to upload an assembly to Relativity.

When you upload an assembly that contains agent types, those agent types become available for selection when you create a new agent. When you click from the Agent Type field, any agent types contained in an assembly uploaded to Relativity will be accessible from the Select Agent Type dialog.

Consider the following when working with assemblies that contains agent types:

- The details view for each assembly displays the agent types (if any) associated with that assembly.

- If an agent type is contained in an assembly, and you deploy agents using that agent type in your environment, you must delete all agents of that type before you can delete the assembly.

- If you remove an agent type from an assembly and then re-upload that assembly to Relativity, the agent type will be deleted from your environment.

## Viewing logged agent events

You can view logging information about Relativity agents in the Event Viewer on your primary or secondary agent server.

- To open the Event Viewer in Windows, click the Start > Programs > Administrative Tools > Event Viewer.

- In the Event Viewer, open Windows Logs > Application .

---
title: "Managing and setting Relativity agent quantity limitations"
url: https://help.relativity.com/Server2025/Content/System_Guides/Agents_Guide/Managing_and_setting_Relativity_agent_quantity_limitations.htm
collection: user
fetched_at: 2026-06-22T06:04:39+00:00
sha256: 2e394700284eea23653fbb2c15703711bdef0d1f509cc32bbd5c5ebc09224fc5
---

Managing and setting Relativity agent quantity limitations Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Managing and setting Relativity agent quantity limitations

The purpose of the following information is to enable you to successfully make changes to the Agent table using SQL. This will allow you to enforce restrictions of many types of agents so that you don’t find yourself in a situation where too many agents have been created.

In the EDDS database of Relativity, there is a table called AgentType. In each line listed in SQL, the table has a number of columns and a row for each agent. The following image shows only a few columns.

Each column gives you some additional control over the number of agents that can be deployed in an environment. Columns are described in AgentType table column definitions . For columns that describe a quantity limitation, a value of 0 means that the agent will be untracked/unenforced. Min x columns that are not mentioned in AgentType table column definitions are not mentioned because they are not enforced.

The only time that this check is made is when the agent is first deployed. Anything that happens afterward, such as a server moving to a different resource pool, or a change to these rules, will not affect existing agent counts. Changes are not applied retroactively.

## Analytics considerations

Analytics server agents, while present in this table, follow some slightly different rules for scaling that you should consider when deploying them. The Relativity Analytics Cluster Manager and Content Analyst Index Manager agents are scalable at 1 agent each per Analytics server in the environment. The Relativity Analytics Categorization Manager is scalable at 2 agents per Analytics server in the environment.

## AgentType table column definitions

- ArtifactID - The agent's unique ArtifactID

- Name - The name of the agent, which reflects its type

- Full namespace - The full name of the agent, such as kCura.EDDS.Agents.FileDeletionManager. This should never be changed.

- MaxInstancePerServer - Set a limit on a per server basis. By default, all 0s except for dtSearchSearch.

- MaxInstancePerResourcePool - Set the maximum number of agents per resource pool to prevent users from deploying multiple instances of agents when there should be only one. Be aware, however, that if a server is moved from one resource pool to another, there will be no correction or warning that you have violated the resource pool limit. Only the Server Manager agent has a default limit here.

- MinInstanceEnvironment - Every agent has a default MinInstanceEnvironment requirement of 1 . However, you're not required to have all of the agents, and this value is used only once during initial installation, so it can be changed. Relativity gives warnings when minimum recommendations are not met, but minimums are not enforced.

- DefaultInterval - How often the agent checks in, in seconds. The default interval on agents “checking in” to their queues for more work is 5 seconds. In an environment with many agents, this may be too often and may result in thousands of queries per minute when much longer intervals would suffice. For example, using a 30 second interval, it would take you at least that long to navigate to the Agents tab to see if the agent is running. If you apply this across the board, it would reduce agent queries to the database by a considerable amount.

- Description - The description of the agent

- Guid - The agent's unique identifier

- LoggingLevel - There are three levels of logging: 1 is for Errors only , 5 is for Warnings and errors , and 10 is for Log all messages .

## Editing the AgentType table

Following these guidelines, you can set the default settings for each agent. You can only set the defaults by running SQL queries against the table itself.

For example, the following query changes the maximum number of OCR workers in an environment to 10.

```text
UPDATE [EDDS].[eddsdbo].[AgentType] SET  [MaxInstanceResourcePool]= 10
WHERE [Name] = 'OCR Worker'

```

If you have 12 agents already in any resource pool, this will do nothing to remove them or even warn you. If you move a server to a different resource pool, there will be no check to prevent it from moving if the move causes it to exceed the predefined limit.

## Editing the Agent table

The EDDS.eddsdbo.Agent table needs the column [Updated] set to 1 whenever a change is manually made to it. Otherwise the Agent Managers that are currently running will revert the database record to the values they have cached.

The Agent table inherits several of the columns in the AgentType table when the agent is deployed. The logging level and interval are all written to this table. The Name column gets appended with some number (n). If you want to change the values for existing agents for either of these values, you can change them through the UI. If you have many changes to make, it will be faster to change them in the Agent table.

The following sample SQL statement updates the run interval to 10, and sets the logging level to Log warnings and errors for all dtSearch Index Workers.

```text
UPDATE [EDDS].[eddsdbo].[Agent] SET [Updated] = 1, [Interval] = 10, [LoggingLevel] = 5
WHERE [Name] LIKE 'dtSearch Index Worker%'
```

Executing this SQL in Sql Server Management Studio updates the dtSearch index worker default maximum of agents to 10.

On this page

- Managing and setting Relativity agent quantity limitations

- Analytics considerations

- AgentType table column definitions

- Editing the AgentType table

- Editing the Agent table


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

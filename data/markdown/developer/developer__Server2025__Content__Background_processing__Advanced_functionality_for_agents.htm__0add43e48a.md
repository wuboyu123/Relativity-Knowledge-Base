---
title: "Advanced functionality for agents"
url: https://platform.relativity.com/Server2025/Content/Background_processing/Advanced_functionality_for_agents.htm
collection: developer
fetched_at: 2026-06-22T06:31:02+00:00
sha256: 1a5964ea3dfcb706331e5232e01a2b22b2eebc146cc33991f214b9181ff5daf2
---

Advanced functionality for agents Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Advanced functionality for agents

You can further enhance the custom agents that you develop by incorporating advanced functionality into them.

## Set default values for an agent type

When you develop a custom agent, consider limiting the maximum number that can run simultaneously in your environment. This practice ensures that your environment or application doesn't experience performance degradation.

Use the following steps to set default values on your custom agent:

- Open SQL Server Management Studio on your Relativity database server.

- Navigate to the AgentType table in the EDDS database.

- Edit the following fields on your agent:

- DefaultInterval – default time populated when you created an instance of this agent type. This value is in seconds.

- DefaultLogging – default logging level selected when you created an instance of this agent type.

- MinInstanceEnvironment – the minimum number of agents allowed in a Relativity environment. If the number of agents falls below this minimum value, then a warning message appears on the Alert pop-up.

- MaxInstanceEnvironment – the maximum number of agents allowed in a Relativity environment. If the number of agents exceeds this maximum value, then a warning message appears on the Alert pop-up.

- MinInstanceServer – the minimum number of agents allowed on each Relativity agent server. If the number of agents falls below this minimum value, then a warning message appears on the Alert pop-up.

- MaxInstanceServer – the maximum number of agents allowed on each Relativity agent server. If the number of agents exceeds this maximum value, then a warning message appears on the Alert pop-up.

- MinInstanceResourcePool – the minimum number of agents allowed in a Resource Pool. If the number of agents falls below this minimum value, then a warning message appears on the Alert pop-up.

## Provide default values for schedule intervals

Define agent triggers so that you can run these background processes at optimal time intervals for performing their tasks. Consider the following sample intervals:

- 3600 second intervals - The agent runs once an hour.

- 300 second intervals - The agent runs every once 5 minutes.

- 30 second intervals – The agent runs every once 30 seconds.

For example, you could add the following code as the first step in the Execute() method that you override when you create a custom agent. You can then use UTC time to control the time intervals when the agent runs.

Copy

```text
1
2
3
4
5
System.DateTime offHourStart = <b><ReplaceWithYourTime_X></b>;

System.DateTime offHourEnd = <b><ReplaceWithYourTime_Y></b>;

if (!(System.DateTime.Now.Ticks >= offHourStart.Ticks && System.DateTime.Now.Ticks <= offHourEnd.Ticks)){

     return;

}
```

You can customize your agent to only run between Time_X and Time_Y. Your agent could run once an hour during a specific two hour window, so that it actually only runs twice per day.

On this page

- Advanced functionality for agents

- Set default values for an agent type

- Provide default values for schedule intervals


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use

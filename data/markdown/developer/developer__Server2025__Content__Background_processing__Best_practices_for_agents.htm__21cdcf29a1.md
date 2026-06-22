---
title: "Best practices for agents"
url: https://platform.relativity.com/Server2025/Content/Background_processing/Best_practices_for_agents.htm
collection: developer
fetched_at: 2026-06-22T06:31:01+00:00
sha256: 2688dd2cc90b31670c8498b3e5f2e8e4ace85c7559bb74ba70112d612f9eb2c9
---

Best practices for agents

# Best practices for agents

Use these guidelines to optimize your application development with custom agents.

## Optionally use a job queue

When you implement a new agent, you have the option to use a job queue table stored in the EDDS database. This approach ensures that the application and agent can share information about job statuses and errors. Implement job queue error handling, which might include displaying an error message. Disable the agent when a critical error occurs.

Store custom applications application queues in the EDDS, rather than at the workspace database level.

## Use helper classes

Use the helper classes so that you program to an interface. The helper classes provide functionality for returning a database context and connecting to the Services API. They are available when you reference the Relativity.API.dll in your projects. Codes samples for agents illustrate how to establish this connection with the helper classes. See Basic concepts for agents .

## Handle error scenarios

Make sure that your custom code handles any errors that your agent may encounter. Relativity disables your custom agent if it throws an exception for an error scenario that it can’t resolve, or for one that requires manual intervention to resume execution.

When temporary service interruptions occur, your agent may encounter an error scenario due to an inaccessible external resource, such as a file system, SQL server, or API. In these cases, your agent should make a limited number of attempts to retry the failed operation. Since long-lived failures may be indistinguishable from temporary interruptions, implement your code so that it doesn’t enter an infinite loop.

Additionally, when resource overutilization causes a failure, avoid making retry attempts too often, because they worsen the situation. Instead, implement your code so that it waits between retry attempts.

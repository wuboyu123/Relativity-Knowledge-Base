---
title: "Build agents"
url: https://platform.relativity.com/Server2025/Content/Background_processing/Background_processing.htm
collection: developer
fetched_at: 2026-06-22T06:28:34+00:00
sha256: a5f9548a1c6e6410f133987d0f40727ae80e9d5d5266c84ab6ca7a03b35eeca3
---

Build agents

# Agents

You can perform background processing in Relativity by developing custom agents. Because these agents perform background work, they don't interfere with user activities performed through the Relativity UI. These agents aren't event driven so they have no dependency on user activity.

Additionally, you can implement agents as managers that monitor tasks or workers that perform specific jobs in your environment. You can develop custom agents to perform their background processes at configurable intervals. For example, Relativity uses agents to OCR documents.

Other common use cases include:

- Using agents to make calls to third-party APIs.

- Developing a mass updater, which is an agent triggered when a system admin clicks a console button. In this case, the agent updates a large number of items tied to some custom object. It sets up a job based on the workspace and the objects in the workspace that need to be updated.

- Implementing a job scheduler, which is an agent that is used to execute nightly jobs. For example, you could implement an agent that builds your dtSearch indexes nightly.

- Developing an email agent, which is used to send emails. This agent runs in the background making connections to the SMTP server, and performing other tasks.

See these related pages:

- Basic concepts for agents

- Best practices for agents

- Advanced functionality for agents

- Troubleshoot agents

## Version History

v5000.0.2

##### Release Notes

- Initial version for Server 2024 release

##### Supported Relativity Version Range

Lowest Version Highest Version

Server 2024 Server 2025

v17.4.2

##### Release Notes

- Initial version for Server 2023 release

##### Supported Relativity Version Range

Lowest Version Highest Version

Server 2023 Server 2024

---
title: "Servers"
url: https://help.relativity.com/Server2025/Content/Relativity/Servers/Servers.htm
collection: user
fetched_at: 2026-06-22T06:01:59+00:00
sha256: 02789d0fae0f449fcda60b12b9b810b2a99eaa5d9d1b0385b6fdeb9250aa06f1
---

Servers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Servers

The Servers tab provides a complete list of all servers that exist in your environment that you added either manually or during installation. You also have the option of adding new servers to the environment and editing certain settings of existing servers.

-

Analytics servers register automatically when you upgrade. You can also manually add Analytics and worker manager servers through the Servers tab. The Servers item list displays information like the server name, type, and version.

-

When adding a new server to your resource pool, ensure that you apply the same hotfix to the new server that you may have applied to any existing Web or Agent Servers.

## Servers automatically added during Relativity installation

### Agent server

The agent server facilitates the work of various agents in Relativity. There must be at least one active agent server per environment. For more information, see Installing to agent servers .

### Cache location server

Cache location servers temporarily store natives, images, productions, and other file types the viewer uses. During installation, Relativity automatically creates one cache location server per file repository that is currently in use. It appends a subfolder called cache to the file repository path, such as \\localhost. In addition, you can add cache location servers to resource pools, so that they are available to select when you create a workspace. You must select a default cache location server when you create a workspace. For more information, see Resource pools and Workspaces .

### Services server

The Services server accommodates the Relativity.Services application pool, which is added automatically with the Relativity.Services virtual directory during installation.

### SQL - Distributed server

The distributed server accommodates a distributed instance of a SQL Server, which can house multiple workspace databases at one time, with the primary SQL instance housing the EDDS database. For more information, see Using the Relativity installer .

### SQL - Primary server

The primary server accommodates the primary instance of SQL, which houses the EDDS database. For more information, see Using the Relativity installer .

On an SQL Server profile, you can edit the Workspace Upgrade Limit field, which controls the number of agents accessing the server during an upgrade. The setting entered in this field can’t exceed the setting in the GlobalWorkspaceUpgradeLimit instance setting value. If you enter a number that exceeds this instance setting value, an error occurs that cancels your update. For more information, see Instance settings and Upgrading workspaces .

### Web server

There are multiple types of web servers:

- Web - Distributed: Forms Authentication - facilitates authentication based on specific code for distributed web servers. This is added automatically during Relativity installation.

- Web Background Processing - facilitates web background processing windows service, which is added automatically with the corresponding application pool during Relativity installation.

- WebAPI: AD Authentication - facilitates active directory service for the WebAPI component. This is added automatically during Relativity installation. For more information, see Authentication .

- WebAPI: Forms Authentication - facilitates authentication based on specific code for the WebAPI component. This is added automatically during Relativity installation.

## Servers requiring manual addition after Relativity installation

### Analytics server

The Analytics server facilitates Analytics functions. This server, if active, is available for selection when you're creating or editing an Analytics index, Structured Analytics set, and Assisted Review project. For more information, see Adding an Analytics server .

### Worker manager server

The worker manager server performs processing, imaging, and conversion. This server also facilitates all phases of a processing job, including inventory, discovery, and publish. See Configuring the worker manager server for more information.

## Restarting Windows Services

You can restart Windows Services for agent servers, web background processing servers, worker manager servers or analytics servers by using the Windows Service console.

Use the following steps to restart a Windows service from the Windows Service console:

- Navigate to the Servers tab.

- Click the server with the Windows Service you want to restart.

- Click Restart Windows Service .

### Service Status

The Service Status section of the Windows Service console displays the state of the service. A Windows Service can have any of the following service statuses:

- Running - appears if Relativity detects the Windows Service is running.

- Stopped - appears if Relativity detects the Windows Service is stopped.

- Pending - appears if Relativity detects the Windows Service is in the process of restarting.

- Unknown - appears if Relativity is unable to detect the status of the Windows Service.

### Manage Service

The Manage Service section of the Windows Service console allows you to restart the Windows Service or refresh the page. Click Restart Windows Service to restart the service. Click Refresh Page to revise the Service Status.

You can also restart multiple Windows Services by using the mass operation option at the bottom of the Servers tab.

On this page

- Servers

- Servers automatically added during Relativity installation

- Agent server

- Cache location server

- Services server

- SQL - Distributed server

- SQL - Primary server

- Web server

- Servers requiring manual addition after Relativity installation

- Analytics server

- Worker manager server

- Restarting Windows Services

- Service Status

- Manage Service


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

---
title: "Loading application resources"
url: https://platform.relativity.com/Server2025/Content/Building_Relativity_applications/Loading_application_resources.htm
collection: developer
fetched_at: 2026-06-22T06:30:51+00:00
sha256: c7ea69eeb942ceb5641793a99654a9ee022fb9ab68be1f7bfaee0d576977d7f6
---

Loading application resources

# Loading application resources

Application Deployment System components – agents, custom pages, event handlers – include resource files such as application libraries (DLLs), config files, images, and stylesheets. When developing and troubleshooting Relativity applications, it is important to understand where and in what order the resources are deployed.

See these related pages:

- Basic concepts for the application framework

- Build your first application

- Create an application in Relativity

- Best practices for building applications

- Advanced functionality for the application framework

- Develop application event handlers

- Troubleshoot applications errors

## Application domain directories

Agents, custom pages, and event handlers, and Kepler services run in their own application domains that are spun up dynamically.

### Agents

Agent domains are created by Relativity when a new agent is created. Agent domains are under the temp folder for the user profile that the agent manager runs under:

Copy

```text
1
c:\Users\username\AppData\Local\Temp\Agent\
```

The DLLs in the domain come from these sources:

- C:\Program Files\kCura Corporation\Relativity\Agents\bin\

- Resource files for the agent

### Custom pages

Custom page domains are created by the Custom Page Deployment Manager Agent in

Copy

```text
1
c:\Program Files\kCura Corporation\Relativity\EDDS\CustomPages\
```

The DLLs in the domain come from these sources:

- A combination of C:\Program Files\kCura Corporation\Relativity\EDDS\bin\ and C:\Program Files\kCura Corporation\Relativity\Library\ folders

- Resource files for the custom page

### Event handlers

Event handler domains are created the first time the event handler is called by the application. Event handler domains by default are under the temp folder, typically:

Copy

```text
1
C:\Windows\Temp\RelativityTemporaryDLLs\TempDomains\<####>\
```

The DLLs in the domain come from these sources:

- C:\Program Files\kCura Corporation\Relativity\EDDS\bin\

- Resource files for the event handler

## Loading order and priority

The ADS components resource files are loaded in the following order:

- Agents and event handlers create their application domain and then drop resource files for the app into the domain.

- Custom pages unzip the custom page file into the domain directory then drop in the Relativity DLLs.

It is possible to have duplicate files between the application's resource files and the ones Relativity loads into a domain. For agents, the application resource file overrides the file loaded from the Relativity installation directories. For custom pages and event handlers, the file provided by Relativity would be the last one loaded into the domain and overwrite the application-specific file.

---
title: "Introduction to Relativity extensions"
url: https://platform.relativity.com/Server2025/Content/Extend/Introduction.htm
collection: developer
fetched_at: 2026-06-22T06:22:11+00:00
sha256: 4ec39a2cf492c791613d33083a90dc7235dd7461bf8f21825e4a621833b14a4f
---

Introduction to Relativity extensions

# Extending Relativity

Relativity exposes several Extensibility Points that allow you to extend Relativity and enhance the platform’s capabilities. These Extensibility Points require you to write code in the .NET Framework, and then deploy that program to run within Relativity. To learn more about the extensibility points and how you can build them, you can follow our tutorials .

## Extensibility Points

Platform extension APIs (also known as Extensibility Tools) expose interfaces through the .NET Framework that you can use to implement components used in Relativity applications and hosted on the Relativity platform.

- Agents : build and deploy custom background processes to handle long running tasks or batch operations.

- Custom / Kepler APIs : use the Kepler hosting library to deploy your own REST APIs within Relativity.

- Custom pages : Deploy your custom web application within Relativity to add your own pages, workflows, and UI elements.

- Event handlers : enhance certain common activities with pre- and post-actions.

- Relativity API Helpers - include interfaces that you can program against when developing agents, custom pages, and event handlers. They provide the ability to write common code for sharing across these extensibility points to simplify your development processes.

- Relativity Application Framework - use the Relativity Application Framework to create a RAP file, which is used to package and deploy an application to other workspaces or instances

- Relativity Scripts - use custom scripts to extend Relativity functionality and modify data sets in workspaces. For example, you can develop scripts to generate custom reports, auto-populate fields, or reformat data based on predetermined parameters

## User Interface Customization APIs

UI customization APIs consist of JavaScript APIs that you can use to customize user interactions with various forms or the viewer interface available in the Relativity UI.

- Relativity Forms API - provides a front-end page life cycle used to facilitate the customization of view, edit, and layout pages. This API provides support for customizing loading, updating, and submitting forms, as well as other options.

- Review API - includes a suite of APIs for customizing the viewer interface by implementing and enhancing user workflow with the Review Extensions framework. This framework supports executing custom code, adding custom content to the user interface, the addition of custom toolbar controls, and other features.

- Supported JavaScript APIs - lists JavaScript APIs that you can call from Relativity's main window.

## Extending Relativity vs. Integrating with Relativity

This comparison describes main differences between integrating with Relativity with the available APIs, and extending Relativity with the available Extension Points

Extending Relativity Integrating with Relativity’s APIs

Languages and tooling Must use .NET Framework 4.6.2 and deploy using Relativity’s Application Deployment System. Integrate using any tool or language that supports REST.

Deployment Runs on Relativity’s platform, inside Relativity’s ecosystem and datacenter. Runs on your own private cloud, datacenter, and/or machines

Observability and troubleshooting Access to logs through the Log Extractor tool. Access to any observability tools that you use.

Maintainability Code must be kept updated multiple times each year as Relativity’s implementation continues to evolve Domain driven; stable abstractions allow integrations to remain unchanged for years at a time.

---
title: "Swagger OpenAPI workflow"
url: https://platform.relativity.com/Server2025/Content/Getting_Started/Swagger_workflow.htm
collection: developer
fetched_at: 2026-06-22T06:33:20+00:00
sha256: d35793736a00f1a71c81014afd92606bbcaea8345ad80aad556f80df9fd3b448
---

Swagger OpenAPI workflow

# Swagger OpenAPI workflow

You can leverage the online Swagger editor to view JSON OpenAPI specification files that are provided with select Relativity nuget packages.

Not all nuget packages currently have a JSON OpenAPI specification provided.

## Using Swagger with an OpenAPI specification

We'll use the Relativity.Infrastructure.SDK nuget package in this tutorial as an example, but you can use any nuget package that comes with a JSON file.

- Download the Relativity.Infrastructure.SDK nuget package (see Relativity Server APIs , and then explore the package with 7zip (or other applicable tool).

- Locate the JSON file in the Content directory of the nuget package (e.g., Relativity.Infrastructure.SDK.4.1.0.nupkg\content\openapidoc{versionNumber}.json).

- Right click on the file using your extraction tool, and then extract the file to a convenient local directory. (e.g., select Copy To , and then select a new directory).

- Navigate to https://editor.swagger.io/ .

- Import the JSON file by navigating to File > Import file , and select the file you extracted in step 3.

- Hide any errors by clicking the Hide button.

- Scroll down on the righthand pane until you see API endpoint information.

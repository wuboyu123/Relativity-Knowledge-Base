---
title: "Elastic Stack Installation Overview"
url: https://help.relativity.com/Server2025/Content/Elasticstack/Elastic_Stack_Installation_Overview.htm
collection: user
fetched_at: 2026-06-22T06:03:42+00:00
sha256: d9cebab3390b5f9b40d3f1145a2b35095f713f16fbbb6db321bb6586f79748f8
---

Elastic Stack Installation Overview Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Elastic Stack Installation Overview

This page provides a high-level overview of the Elastic Stack installation process and helps identify the correct installation path for the environment.

A Relativity Elastic Stack deployment includes Elasticsearch, Kibana, and APM Server (when applicable). The required Elastic Stack components depend on environment configuration and system requirements. For details, see the Elastic Stack System Requirements .

For information about supported Elasticsearch versions and deployment approaches for existing Data Grid clusters, see Supported Elastic Stack Versions .

## Cluster Architecture Decision

Before beginning installation, you must decide on your cluster architecture:

Option 1: Single Unified Cluster (single cluster with multiple nodes)

- One Elasticsearch cluster that contains all data (Environment Watch and Data Grid Audit)

- Simpler to manage and maintain

- Shared resources and infrastructure

- Suitable for most deployments

Option 2: Separate Clusters (multi-cluster)

- Two independent Elasticsearch clusters:

- One dedicated cluster for Environment Watch

- One dedicated cluster for Data Grid Audit

- Complete isolation between workloads

- Independent scaling and resource allocation

- Recommended for very large deployments or when strict data separation is required

For most organizations, Option 1 (Single Unified Cluster) is recommended as it simplifies operations while providing adequate performance and isolation through index management.

## Offline Environment Considerations

For Elastic's guidance on air-gapped installations, see Air-gapped install .

If your environment is offline or air-gapped (no direct internet access), you have two options for obtaining Elastic Stack installation files:

Option 1: Proxy Server (Recommended)

Using a proxy server is the simplest approach for air-gapped environments:

-

Configure a proxy server that has internet access and is reachable from your isolated network.

-

Set proxy environment variables on the target servers before downloading:

Copy

```text
$env:HTTP_PROXY = "http://proxy.yourcompany.com:8080"

$env:HTTPS_PROXY = "http://proxy.yourcompany.com:8080"

```

-

Download files normally using the URLs in this guide — traffic will route through the proxy.

Benefits:

- Minimal workflow changes from standard installation

- Automatic dependency resolution for plugins

- Easier to maintain and update over time

Option 2: Manual File Transfer (Air-Gapped)

For fully isolated networks with no proxy access:

-

From an internet-connected machine, download all required files:

- Elasticsearch ZIP (e.g., elasticsearch-8.x.x-windows-x86_64.zip )

- Kibana ZIP (e.g., kibana-8.x.x-windows-x86_64.zip )

- APM Server ZIP (e.g., apm-server-8.x.x-windows-x86_64.zip )

- RWSM NuGet package from https://relativitypackageseastus.jfrog.io/artifactory/api/nuget/server-nuget-virtual/Download/Relativity.Windows.ServiceManager/2.24.0

- Any required plugins from Elastic's plugin repository

-

Transfer files to the air-gapped environment using approved media (USB drive, secure file transfer, etc.).

-

Install plugins offline using local file paths:

Copy

```text
.\elasticsearch-plugin install file:///C:/downloads/mapper-size-8.x.x.zip

```

Considerations:

- Requires more planning and coordination

- All dependencies must be manually tracked and transferred

- Plugin versions must exactly match the Elasticsearch version

## Installation Paths

Once you have reviewed the considerations above, choose the appropriate installation method for your environment:

| Automated and Manual

On this page

- Elastic Stack Installation Overview

- Cluster Architecture Decision

- Offline Environment Considerations

- Installation Paths


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

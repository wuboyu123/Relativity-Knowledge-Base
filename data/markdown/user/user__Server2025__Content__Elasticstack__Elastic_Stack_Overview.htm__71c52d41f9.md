---
title: "Elastic Stack Overview"
url: https://help.relativity.com/Server2025/Content/Elasticstack/Elastic_Stack_Overview.htm
collection: user
fetched_at: 2026-06-22T06:10:58+00:00
sha256: e9a95b2092c1263bfa6d5bb1f8efa013f2f8c78baf92c897ace1cd2179066aa5
---

Elastic Stack Overview Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Elastic Stack Overview

Relativity uses components of the Elastic Stack to support Data Grid Audit and Environment Watch functionality. Depending on whether the Elastic Stack is being installed for the first time or an existing deployment is being upgraded, the required steps may differ.

This page provides a high-level overview of the Elastic Stack installation process and helps identify the correct installation path for the environment.

A Relativity Elastic Stack deployment includes Elasticsearch, Kibana, and APM Server (when applicable). The required Elastic Stack components (such as Kibana or APM Server) depend on environment configuration and system requirements. For details, see the Elastic Stack System Requirements .

If you are currently running Elasticsearch 7.x for Data Grid, upgrading or migrating that cluster is not required to use Environment Watch. Relativity supports the following deployment approaches:

- Approach 1: Upgrade the existing Data Grid Elasticsearch cluster to a supported version (8.x or 9.x) and upgrade the indexes to support both Data Grid and Environment Watch from a single cluster.

- Approach 2: Maintain the existing Data Grid Elasticsearch cluster on version 7.x and deploy a separate Elasticsearch cluster running a supported version (8.x or 9.x) for Environment Watch only.

## Installing Elastic Stack

This scenario applies when deploying Elastic Stack for the first time in a Relativity environment. The installation process includes the following high-level steps:

- Install Elasticsearch, Kibana (if applicable), and APM Server (if applicable) as described in the Elastic Stack installation topics

- Set up Data Grid Audit or Environment Watch using the Relativity CLI.

## Upgrading Elastic Stack

This scenario applies when upgrading or migrating an existing Elastic Stack deployment to a supported version. The upgrade process includes the following high-level steps:

- Upgrade or migrate Elasticsearch to a supported version

- Set up Data Grid Audit or Environment Watch using the Relativity CLI.

- Complete the one-time migration from a Platinum license to a Basic license , if applicable.

## System Requirements and Pre-installation Planning

Before installing or upgrading Elastic Stack components, review the Elastic Stack System Requirements to verify that the environment meets all prerequisites.

## Troubleshooting

Refer to the Troubleshooting Guide if you encounter any issues.

On this page

- Elastic Stack Overview

- Installing Elastic Stack

- Upgrading Elastic Stack

- System Requirements and Pre-installation Planning

- Troubleshooting


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

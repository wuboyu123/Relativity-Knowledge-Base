---
title: "Environment Watch and Data Grid Audit Installation"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Environment_Watch_and_Data_Grid_Audit_Installation.htm
collection: user
fetched_at: 2026-06-22T06:11:25+00:00
sha256: 5cb5c88dcf81b98d106b2fb9661f9e87bea34b6fd100ec9cb578bec68aecf01b
---

Environment Watch and Data Grid Audit Installation

# Environment Watch and Data Grid Audit Installation

## Installation Overview

Environment Watch and Data Grid Audit require installation and configuration of third-party and Relativity software. This installation guide provides a high-level installation overview for Environment Watch and Data Grid Audit. Detailed instructions for installing and configuring the Elastic Stack are documented separately. Additional steps for configuring the Audit application within Relativity are covered here .

The Relativity applications and components that are referenced in this installation guide are packaged together in the Server bundle release. You can find the latest bundle on GitHub here . Environment Watch and Data Grid Audit also require Relativity applications that are available in the Relativity Application Library and not packaged in the bundle or covered in this installation guide (e.g. Pagebase and Telemetry for Environment Watch, Audit for Data Grid Audit, and InfraWatch Services for both). These applications are identified as pre-requisites in relevant sections of this installation guide.

For information about Environment Watch's performance impact on Relativity workloads, see Environment Watch Performance Impact .

The Server bundle is generally released quarterly, with hotfixes provided for critical issues as needed.

## Elastic Stack Setup

Environment Watch and Data Grid Audit depend on a properly installed and configured Elastic Stack, including Elasticsearch and Kibana.

For complete, step-by-step instructions on installing and configuring the Elastic Stack for Relativity, see: Elastic Stack Setup documentation

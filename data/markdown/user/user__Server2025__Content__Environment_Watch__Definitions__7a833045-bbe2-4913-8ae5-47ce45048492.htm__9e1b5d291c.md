---
title: "x509: certificate has expired or is not yet valid"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Definitions/7a833045-bbe2-4913-8ae5-47ce45048492.htm
collection: user
fetched_at: 2026-06-22T06:18:35+00:00
sha256: b404b01bf35e523b6ffa72b01d5c4cc92001c7a891fbe5692095f1d83b65b9f5
---

x509: certificate has expired or is not yet valid Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

7a833045-bbe2-4913-8ae5-47ce45048492

# x509: certificate has expired or is not yet valid

## Description

Alert is active when there are,

- Missing required certificates in the server

- Expired Certificates, that needs to be renewed

## Alert Details

Alert ID: 7a833045-bbe2-4913-8ae5-47ce45048492

Tags:

- Type:Infrastructure

- Group:Server Health

- PageType:Dashboard

- PageID: e6fe25a9-6f23-41e1-b7f4-5815ced0056b

- CreatedBy:Relativity

- ResolutionURL: /environment-watch/alerts/00024-x509-certificate-has-expired-or-is-not-yet-valid-alert-resolution-sop

## Metric/Log/Trace Details

Metric Name: relsvr.x509_certificate

Metric Attributes:

Attribute Name Description Value

labels.issued_by Issued by Relativity - Intermediate

labels.issued_to Issued to Relativity Secret Store

labels.relsvr_host_installed_products Products installed Invariant Queue Manager,Invariant Worker,Agent,Secret Store,Service Bus,Service Host,SQL Primary,Web

labels.relsvr_server_type Servers to be verified Agent, Invariant Queue Manager, Invariant Worker, SQL Primary, Secret Store, Service Bus, Service Host, Web

labels.state State of metrics installed_not_expired, installed_expired, not_installed

labels.store_location Store locataion LocalMachine

labels.subject_name CN=Relativity Secret Store

service.language.name Language dotnet

service.name Service Name relsvr_infrawatch_agent

service.version Version V1

## Rule details

Alert Condition Description:

Alert triggers when there are,

- Missing required certificates in the server

- Expired Certificates, that needs to be renewed, for the last 30 minutes

Name Value Description

Rule Type Elastic Query

Data View - metrics-* for Meters

Filter Query relsvr.x509_certificate : * and (labels.state :"not_installed" or labels.state :"installed_expired") Certifcates must be expired or not installed

Group Count Above 0 docuemnts

Threshold Above 0 docuemnts

Time Window Last 30 min data to be considered

Frequency 15 mins

## Requires User Intervention

- Yes: alert immediately

- Min time before the alert is active : 30 minutes

## Visualization link

Kibana Dashbaord

## Related Alerts

Host Heartbeat alert should not be in active state.

On this page

- x509: certificate has expired or is not yet valid

- Description

- Alert Details

- Metric/Log/Trace Details

- Rule details

- Requires User Intervention

- Visualization link

- Related Alerts


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

---
title: "Certificates"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Guides/Certificates.htm
collection: user
fetched_at: 2026-06-22T06:20:20+00:00
sha256: 9d584fcd3c7f822b385aa4912eb0057352f2094f9eb3da17e2ed0bd982d44604
---

Certificates Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Certificates

This dashboard provides visibility into the status and validity of certificates used across your Relativity environment. Certificate health checks focus on determining whether a detected certificate has expired; the system does not generate alerts if a certificate is expected but not found. Relativity defines three primary certificates: the Secret Store Certificate, Identity Server Certificate, and Cookie Signing Certificate. Currently, the dashboard detects the Secret Store Certificate, with support for the other certificates planned for Server 2026.

## Prerequisites

By default, Environment Watch comes with built-in monitoring for a secret store certificate. Monitoring can be extended to additional certificates across different servers through a Custom JSON configuration , enabling inclusion of certificates that are critical to the Relativity environment. For detailed instructions on configuring custom certificate monitoring, see the Install Other Integrations

## Certificate Health Status and Expiration Details

The dashboard provides a comprehensive overview of the certificates that Relativity creates and supports within your environment. At the top, the Health indicator displays the overall status of these certificates. A Healthy status indicates that the certificates are properly installed and have not yet expired. The accompanying metrics summarize the number of supported certificates expiring within the next 30 days and the total number of certificates currently being monitored.

The table below lists detailed certificate information, including the Host, Subject Alternative Name (SAN), Expiration Date, State, Issued To, Issued By, and Issued On fields. It also includes usage details, the servers where each certificate is installed, and the number of Days Until Expiration. This detailed view helps you easily identify which certificates are close to expiry or need attention, ensuring that all secure connections remain valid and uninterrupted.

### Use Cases

Use Case Description

Monitor certificate health Quickly verify that all certificates are valid and functioning correctly across your Relativity infrastructure.

Track certificate expirations Identify certificates nearing expiration to plan renewals and prevent service disruptions.

Ensure compliance and security Maintain visibility into certificate issuances and ensure proper management and security practices are followed.

Validate operational readiness Validate certificate installation across services and servers to support secure, stable Relativity operations.

### Associated Alerts

- x509: certificate has expired or is not yet valid

On this page

- Certificates

- Prerequisites

- Certificate Health Status and Expiration Details

- Use Cases

- Associated Alerts


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

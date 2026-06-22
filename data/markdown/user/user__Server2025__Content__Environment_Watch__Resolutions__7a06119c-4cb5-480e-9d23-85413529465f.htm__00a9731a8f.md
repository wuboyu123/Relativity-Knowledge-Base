---
title: "TLS certificate validation errors have occurred"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/7a06119c-4cb5-480e-9d23-85413529465f.htm
collection: user
fetched_at: 2026-06-22T06:19:11+00:00
sha256: 473655cd9e74e7c0b8db2869ff18a2505afb9ca6dd3d23658ed832e3a108b8d0
---

TLS certificate validation errors have occurred Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

7a06119c-4cb5-480e-9d23-85413529465f

# TLS certificate validation errors have occurred

## Description

This alert is triggered when TLS/SSL certificate validation errors are detected in system logs, such as failures to establish a trust relationship for secure channels. These errors typically occur when certificates are expired, untrusted, or misconfigured, potentially disrupting secure communications between services and users.

## Resolution Guidance

### Impact When Active

Definite Impact:

- Failure of services or agents that rely on secure communication, such as the Relativity Service Bus, Analytics components, or integrations with external systems.

- Inability to establish secure connections between Relativity services, leading to service disruptions.

Possible/Likely Impact:

- Failures in document processing, analytics operations, or other functionalities that depend on TLS/SSL communication.

- Security warnings or errors when accessing Relativity features.

### How To Resolve

Follow the steps below to diagnose and resolve the issue:

### 1. Validate Certificate Properties

Check the certificate being used for secure communication:

- It is not expired

- The Common Name (CN) or Subject Alternative Name (SAN) matches the machine name or FQDN

- The Enhanced Key Usage (EKU) includes Server Authentication

- The certificate is trusted by all machines involved (Web, SQL, Analytics, Agent, Worker, Queue Manager, etc.)

If any of your certificates do not adhere to the above requirements, use the steps below to replace them:

### 2. Update HTTPS Certificate Binding in IIS (Web Servers)

Location: Public and Internal Web Servers

- Open IIS Manager

- Navigate to Sites > Default Web Site

- Click Bindings

- Select the existing HTTPS binding and click Edit

- Choose the correct/valid certificate from the dropdown

- Apply changes and restart IIS via PowerShell ( iisreset ) or from IIS Manager

### 3. Update Service Bus TLS Settings

- Relativity provides a utility to help update Service Bus TLS.

Access it here: Relativity Service Bus TLS Utility

- For detailed guidance on configuring certificates for RabbitMQ, refer to our official documentation: RabbitMQ TLS Setup - Pre-installation Requirements

If using a self-signed certificate, ensure it is manually trusted and imported on all relevant servers: Web, SQL, Agents, Workers, Queue Manager, and Analytics.

### 4. Configure SQL Server for TLS

Location: SQL Server

- Open SQL Server Configuration Manager

- Navigate to SQL Server Network Configuration > Protocols for [Instance Name]

"MSSQLSERVER" is the default instance name. If a custom name is used during setup, select that option instead.

- Right-click and select Properties

- On the Certificate tab, choose the correct certificate

- Optionally enable Force Encryption on the Flags tab

- Restart SQL Server

- Ensure all Relativity servers trust the SQL certificate

Reference: For more detailed guidance on managing SQL Server TLS Certificates, refer to MS documentation:

### 5. Update Analytics Server (CAAT) Configuration

Secure Analytics (CAAT) with TLS. Ensure the appropriate certificate is selected and trusted by all communicating machines.

- Follow guidance in:

Follow the steps in our official documentation to configure or update TLS on the Analytics server: Upgrading or Installing Relativity Analytics

Self-signed certificates used here must also be trusted by all servers interacting with Analytics.

## You can also try as per the Resolution template

### Check Hostname and Certificate Matching

Ensure that the hostname used in the connection matches the Common Name (CN) or Subject Alternative Name (SAN) specified in the TLS/SSL certificate.

### Validate System Time

Confirm that the system clocks on all servers are synchronized and set correctly, as significant time discrepancies can cause TLS/SSL handshake failures.

### Use Diagnostic Tools

Utilize tools like openssl s_client, curl -v, or browser developer tools to test SSL/TLS connections and identify specific issues in the handshake process.

### Review Firewall and Network Settings

- Ensure firewalls or security groups are not blocking SSL/TLS traffic between Relativity components. 2.If issues persist, contact Relativity Support for further assistance [https://community.relativity.com/s/support]

## Alert Details

This alert monitors log entries for TLS/SSL certificate validation errors like:

"Could not establish trust relationship for the TLS/SSL secure channel."

- The alert runs every minute

- It triggers if any relevant errors are detected in the last minute

### Alert Condition Details

Rule Type Value Description

Data View Logs-*

Filter Query message: " Could not establish trust relationship " Filters for matching error message

Group Count

Threshold > 0 Count greater than 0 triggers the alert

Time Window 1 hour Checks logs from the past hour

Frequency 1 minute Evaluates every minute

### Alert Metric Details

- Metric Name: logging

- Metric Description: Could not establish trust relationship

- Metric Attributes: Message

Attribute Name Description Value

Log level Severity of the log entry generated during certificate errors Error

On this page

- TLS certificate validation errors have occurred

- Description

- Resolution Guidance

- Impact When Active

- How To Resolve

- 1. Validate Certificate Properties

- 2. Update HTTPS Certificate Binding in IIS (Web Servers)

- 3. Update Service Bus TLS Settings

- 4. Configure SQL Server for TLS

- 5. Update Analytics Server (CAAT) Configuration

- You can also try as per the Resolution template

- Check Hostname and Certificate Matching

- Validate System Time

- Use Diagnostic Tools

- Review Firewall and Network Settings

- Alert Details

- Alert Condition Details

- Alert Metric Details


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

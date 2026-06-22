---
title: "x509: certificate has expired or is not yet valid"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Resolutions/7a833045-bbe2-4913-8ae5-47ce45048492.htm
collection: user
fetched_at: 2026-06-22T06:18:37+00:00
sha256: 90c1b631b7a277271840ac585ffc52a7b78a4e6834287e23037a5bcfbc7d705b
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

The Alert is triggered when there are,

- Missing required certificates in the server

- Expired Certificates, that needs to be renewed

## Resolution Guidance

### Impact When Active

- Complete System Outage - Entire Relativity environment becomes inaccessible.

- Authentication Failure - No users can log in (all methods fail)

- Database Connectivity Loss - Encrypted connection strings cannot be decrypted

- All Services Stop - Web, Agents, Queue Manager, APIs all fail

### How To Resolve

### Steps To Resolve Missing or Expired Relativity SecretStore Certificate

- Navigate to the SecretStore Client directory ( C:\Program Files\Relativity Secret Store\Client )

- Run the repair mode to regenerate the certificate

- Execute the following command: .\secretstore configure-service --repair

- The command will prompt for the unseal key and confirmation to proceed. This process will create new root, intermediate, and client certificates.

- After the repair completes, re-register all client machines that connect to the Secret Store.

### Steps To Resolve Missing or Expired Relativity Identity Certificate

#### Option 1

-

Log in to the Primary SQL server using the Relativity Service Account.

-

Navigate to the Procuro directory (e.g. C:\Program Files\kCura Corporation\Relativity\Procuro )

-

Launch kCura.EDDS.Procuro.exe as administrator.

-

Click "< Back" at the bottom right.

-

Generate a new certificate or choose an existing certificate that is already in the certificate store:

-

To generate a new certificate, ensure that the radio button by Generate New Certificate is selected. Then, click "Update Certificate."

-

To choose an existing certificate, click the radio button by Select Certificate and choose the certificate from the list. Then, click "Update Certificate."

-

Click "Next".

-

Close the Procuro Window by clicking on the "X" in the upper right corner.

-

DO NOT hit the Upgrade button, this is unnecessary and if you have applied hotfixes it will revert them!

-

Reboot all Web and Agent servers.

-

Restart service on Queue Manager server.

-

If you have Data Grid in your environment, the Data Grid Control nodes need to be restarted.

- Secret Store does not need to be restarted, nor server rebooted.

Note: Simply restarting the Relativity Services on web and agent servers does not guarantee that connection strings between servers will be severed and reestablished using the new certificate.

#### Option 2

Can be used if Primary SQL is not available to run Procuro on, or if the "Back" button under Option 1, step 4 is not available.

WARNING: Hotfixes and Patches WILL be reverted and need to be applied again if going through with this method.

-

Copy the entire Procuro folder from the Primary SQL server, and copy it onto another server within the environment. For example, a web or agent server.

-

Open EDDS and take note of the current value. This value will be the thumbprint of the current RelativityIdentityCertificate.

-

Rename the edds.CertificateState table and its PK key (can be as simple as adding '_OLD' at the end of both).

-

Open Procuro.exe on the server it was added to from step 1.

-

Hit the upgrade button on the screen.

- WARNING: Hotfixes and Patches WILL be reverted and need to be applied again if going through with this method.

-

After it completes, new edds.CertificateState table should be generated, and the Identity certificate will be created on the server where Procuro is run from.

- Identity Cert needs to be installed into Secret Store, which is completed with either options. Therefore, it does not matter where the physical cert lives.

-

Reboot all Web and Agent servers.

-

Restart service on Queue Manager server.

-

If you have Data Grid in your environment, the Data Grid Control nodes need to be restarted.

- Secret Store does not need to be restarted, nor server rebooted.

Note: Simply restarting the Relativity Services on web and agent servers does not guarantee that connection strings between servers will be severed and reestablished using the new certificate.

### Steps To Resolve Missing or Expired Relativity Cookie Certificate

-

Log in to the Primary SQL server using the Relativity Service Account.

-

Navigate to the Procuro directory (e.g. C:\Program Files\kCura Corporation\Relativity\Procuro )

-

Launch kCura.EDDS.Procuro.exe as an administrator.

-

Click the Upgrade button..

- WARNING: Hotfixes and Patches WILL be reverted and need to be applied again if going through with this method.

-

The upgrade process will start and update the edds.CookieCertificateState table with the new certificate thumbprint. The cookie certificate will be created on the server from which Procuro is run.

-

Reboot all Web and Agent servers.

## Alert Details

### Alert Condition Details

Alert Condition Description:

Alert triggers when there are,

- Missing required certificates in the server

- Expired Certificates, that needs to be renewed, for the last 30 minutes

Name Value Description

Rule Type Elastic Query

Data View - metrics-* for Meters

Filter Query relsvr.x509_certificate : * and (labels.state :"not_installed" or labels.state :"installed_expired") Certifcates must be expired or not installed

Group Count Above 0 documents

Threshold > 0 Count greater than 0 triggers the alert

Time Window 30 min Evaluates data from the last 30 minutes

Frequency 15 min Checks every 15 minutes

### Alert Metric Details

Metric Name: relsvr.x509_certificate

Metric Description:

Tracks x509 certificate status (installed/expired/missing) across Relativity server components, including certificate issuer, subject, and store location information.

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

On this page

- x509: certificate has expired or is not yet valid

- Description

- Resolution Guidance

- Impact When Active

- How To Resolve

- Steps To Resolve Missing or Expired Relativity SecretStore Certificate

- Steps To Resolve Missing or Expired Relativity Identity Certificate

- Steps To Resolve Missing or Expired Relativity Cookie Certificate

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

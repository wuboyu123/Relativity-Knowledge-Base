---
title: "Cookie signing certificate"
url: https://help.relativity.com/Server2025/Content/Relativity/Authentication/Cookie_signing_certificate.htm
collection: user
fetched_at: 2026-06-22T06:17:43+00:00
sha256: 89ac260c78bdea0841f9a95091029f0df7f18fc23d747b3af362161702990505
---

Cookie signing certificate Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Cookie signing certificate

The Cookie Signing Certificate is a specialized certificate designed specifically to mitigate potential security risks associated with cookie management. It can be updated using the Procuro tool on the Primary SQL server by following these steps:

-

Log in to the primary SQL server using the Relativity Service Account.

-

Access the Procuro directory (e.g. C:\Program Files\kCura Corporation\Relativity\Procuro).

-

Launch kCura.EDDS.Procuro.exe as administrator.

-

Click the Upgrade button. Please refer to the scenarios below for troubleshooting issues.

-

Close the Procuro window.

- The certificate is updated in SQL server or servers. Once complete, Relativity will configure a new Cookie signing Certificate for the environment and will invalidate all authentication sessions.

The certificate is valid for two years and cannot be replaced with a custom certificate.

## Updating the Cookie Signing Certificate

Use the following scenarios to understand how the system updates the cookie signing certificate when you click the Procuro Upgrade button .

Scenario 1: Certificate is expired

If the cookie signing certificate is expired, clicking the Procuro Upgrade button deletes the expired certificate and creates a new entry in the eddsdbo.CookieCertificateState table.

Scenario 2: Certificate state is set to 0

If you manually set the state of the existing cookie certificate to 0, clicking the Procuro Upgrade button adds a new certificate entry to the eddsdbo.CookieCertificateState table.

Scenario 3: Certificate rows are deleted

If you delete all rows from the eddsdbo.CookieCertificateState table, clicking the Procuro Upgrade button creates a new certificate entry in the table.

For additional details, see the knowledgebase article How to Renew CookieSigning Certificate on the Community.

On this page

- Cookie signing certificate

- Updating the Cookie Signing Certificate


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

---
title: "Identity server certificate"
url: https://help.relativity.com/Server2025/Content/Relativity/Authentication/Identity_server_certificate.htm
collection: user
fetched_at: 2026-06-22T06:17:45+00:00
sha256: 3b8fb6283572365f1f328a20b89a756d08a0d14b4635f33c9780d830c0f878a5
---

Identity server certificate Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Identity server certificate

The Identity server certificate must be updated using Procuro on the Primary SQL server. To update your Relativity identity server certificate, please follow the instruction below.

-

Log in to the primary SQL server using the Relativity Service Account.

-

Access the Procuro directory (e.g. C:\Program Files\kCura Corporation\Relativity\Procuro).

-

Launch kCura.EDDS.Procuro.exe as administrator.

-

Click the Back button.

-

Click Update Certificate

-

Click Next .

-

Close the Procuro window.

-

Delete the old certificate from the SQL server or servers.

-

Restart IIS and all Relativity services on all Relativity servers.

Once complete, Relativity will configure a new Identity Certificate for the environment and will invalidate all authentication sessions.

On this page

- Identity server certificate


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

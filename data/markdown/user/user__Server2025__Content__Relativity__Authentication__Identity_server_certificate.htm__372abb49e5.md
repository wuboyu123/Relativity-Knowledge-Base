---
title: "Identity server certificate"
url: https://help.relativity.com/Server2025/Content/Relativity/Authentication/Identity_server_certificate.htm
collection: user
fetched_at: 2026-06-22T06:17:45+00:00
sha256: 3b8fb6283572365f1f328a20b89a756d08a0d14b4635f33c9780d830c0f878a5
---

Identity server certificate

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

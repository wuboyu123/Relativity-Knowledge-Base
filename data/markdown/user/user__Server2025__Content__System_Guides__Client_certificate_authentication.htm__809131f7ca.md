---
title: "Client certificate authentication"
url: https://help.relativity.com/Server2025/Content/System_Guides/Client_certificate_authentication.htm
collection: user
fetched_at: 2026-06-22T06:17:39+00:00
sha256: c6958309bd007d2b2f0282f78c8cf775bf8258163db9cec9b8d412d9b6f15cfb
---

Client certificate authentication

# Client certificate authentication

Relativity supports client certificate authentication, which may also be referred to as smart card authentication. This two factor authentication method uses a PIN and a client certificate stored on a personal identity verification (PIV) card. When logging in to Relativity, the user inserts a PIV card into the card reader, and clicks a PIV login button. Next, the user selects the appropriate certificate on the PIV card, and then enters a PIN.

## Configuring a user for client certificate authentication

In Relativity, you configure client certificate authentication at the user level.

Before you begin, obtain the value in the Subject Alternative Name field of the certificate generated for a user. Contact your system or other administrator responsible for generating these certificates in your organization for this information.

Use the following steps to configure a user for client certificate authentication:

- Log in to Relativity with system admin credentials.

- Select Home from the user drop-down menu.

- Click the Users tab.

- Click the Edit link next to an existing username, or create a new user. See Creating and editing a user .

- In the Login Method section, click New to open the Login Method Information form.

- Select a Smart Card Provider .

- In the Certificate Subject field, enter <Subject Alternative Name> . The Subject Alternative Name is associated with the certificate on the smart card used to log in to Relativity.

For example, if the Subject Alternative Name is jsmith@example, then you would enter jsmith@example in the Certificate Subject field.

- Click Save . The user can now use client certificate authentication to log in to Relativity.

## Logging in to Relativity with client certificate authentication

You can log in to Relativity by inserting your PIV card into your smart card reader, selecting a certificate, and entering your PIN.

Use the following steps to log in to Relativity:

- Insert your PIV card into the smart card reader for your computer.

- Browse to your Relativity website with the URL provided by your system admin.

- Enter your email address in the Username box.

- Click the button under the External Login heading.

Your system admin may customize the label on the button for your Relativity application.

- On the Select a certificate dialog, highlight the certificate used for logging in to Relativity.

- Click OK .

- Enter your PIN for your smart card, and click OK .

---
title: "Using an existing public key infrastructure"
url: https://help.relativity.com/Server2025/Content/System_Guides/Secret_Store/Using_an_existing_public_key_infrastructure.htm
collection: user
fetched_at: 2026-06-22T06:21:09+00:00
sha256: c82d834c204ab3728e9d6be7a8e964f97f8f1853abf1d1985149a87479e95756
---

Using an existing public key infrastructure

# Using an existing public key infrastructure

Secret Store provides the option to authenticate to Secret Store using an existing, external public key infrastructure (PKI) instead of a PKI provisioned by Secret Store.

Relativity recommends only using an existing PKI if you have the expertise to manage PKIs. If you need to utilize this feature, contact ﻿ Relativity Support .

## Special considerations

If an external certificate authority is imported into Secret Store and used for authentication, the following considerations need to be made:

- If you do not have certificates signed by this external authority and you cannot obtain certificates signed by this authority, you will not be able to authenticate to your Secret Store.

- The client certificates must be signed directly by the authority and not be part of a chain as Secret Store only respects on level of signing.

- All client certificates signed by the authority will have access to the secrets in Secret Store.

## First time install: specifying an external PKI when configuring the Secret Store service

After you install Secret Store, the Secret Store service can be configured to use an external PKI using the secretstore.exe command line utility and the command configure-service with the serverCertificate and the externalAuthenticatorThumbprint command line options. Both options must be specified to use an external certificate authority. Secret Store uses TLS for mutual authentication, which ensures that access to Secret Store is only granted to machines that you register in your Relativity environment. The serverCertificate parameter is the thumbprint of the TLS certificate to be used by the Secret Store server. The externalAuthenticatorThumbprint is the thumbprint of the certificate authority to be used by the client for Secret Store authentication. See the following example:

```text
.\secretstore.exe configure-service --serverCertificate=0000000000000000000000000000000000000000 --externalAuthenticatorThumbprint=0000000000000000000000000000000000000000

```

This will result in Secret Store importing the specific certificate authority to be used for authentication instead of provisioning a new PKI. Additionally, a clientRegistration.ps1 script will be generated to register your machines to use Secret Store. Copy the script and the Secret Store executable to your client machines and run as normal.

## Migrating from an internal authority to an external authority

Migrating Secret Store from an internal authority to an external authority is done in two parts: migration of the server and migration of the client. To migrate to an external authority with an already installed and configured Secret Store:

- Ensure that:

- The target certificates are installed on the Windows Machine Certificate store on the Secret Store server.

- Secret Store is configured to use a custom TLS certificate. See Configuring the service .

- Secret Store is unsealed. See Unsealing the Secret Store .

- On your Secret Store server, execute the ServerAuthorityMigration.ps1 script. This will

- Import the specified authority.

- Remove the relativity-intermediate authority from the Secret Store server.

- Remove the Relativity Secret Store client certificate, Relativity-Intermediate certificate authority, and Relativity-CA root certificate from the server's windows certificate store.

See the following example:

```text
.\ServerAuthorityMigration.ps1 -AuthenticatorName AuthName -ExternalAuthenticatorThumbprint 0000000000000000000000000000000000000000

```

- On each client, execute the ClientAuthorityMigration.ps1 script. This will

- Configure the client to use the specified authority.

- Remove the Relativity Secret Store client certificate, Relativity-Intermediate certificate authority, and Relativity-CA root certificate from the client's windows certificate store.

See the following example:

```text
.\ClientAuthorityMigration.ps1 -SecretStoreExePath path/to/secretstore.exe/including/exe/name -AuthenticatorName AuthName

```

## Rotating the authority

Use the secretstore.exe authority and the secretstore.exe use-authenticator commands to change the authority.

- Import a new authority using secretstore.exe authority import:

```text
.\secretstore.exe authenticator import NewAuthName --externalAuthenticatorThumbprint=0000000000000000000000000000000000000000

```

- Configure your server and clients to use the newly imported authority by executing secretstore.exe use-authenticator on each Secret Store machine:

```text
.\secretstore.exe use-authenticator NewAuthName

```

- Remove the old authority using secretstore.exe authority remove:

```text
.\secretstore.exe authority remove OldAuthName

```

## Recovering after certificate expiration

In the case that the external certificates to your Secret Store expire and you can no longer access Secret Store, the secretstore.exe configure-service command can be run with the repair flag to regenerate all internal PKI certificates.

```text
.\secretstore.exe configure-service --repair

```

Once the repair runs, you can follow the migrate flow to migrate your Secret Store server and clients to use an external authority.

## Command reference

### Authenticator

Operations to manage authorities in Secret Store.

Parameters:

- Action - Required. Action to take on authority. Possible actions are import and remove .

- AuthenticatorName - Required. Name of authority the action will execute against.

- ExternalAuthorityCertificate - Required on import. Certificate thumbprint of the authority to be added to secret store.

- Url - Optional.

### use-authenticator

Configures the Secret Store client to use the specified authority.

Parameters:

- AuthenticatorName - Required. Name of the authority to be used by the Secret Store client.

- url - Optional.

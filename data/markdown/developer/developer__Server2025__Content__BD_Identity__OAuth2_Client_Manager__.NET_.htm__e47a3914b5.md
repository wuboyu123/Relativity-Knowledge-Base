---
title: "OAuth2 Client Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/OAuth2_Client_Manager__.NET_.htm
collection: developer
fetched_at: 2026-06-22T06:26:57+00:00
sha256: 2210725c359ea8ca2e909745692f560d950f6df49842a6cd32ef971a0fadbe5b
---

OAuth2 Client Manager (.NET)

# OAuth2 Client Manager (.NET)

In Relativity, you can use OAuth2 clients to configure external services and applications to authenticate against Relativity in a secure manner. For more information, see OAuth2 clients in the Relativity Documentation site.

The OAuth2Client Manager API exposes CRUD operations for OAuth2 clients. It also supports generating secrets for OAuth2 clients.

As a sample use case, you can implement a client application that presents the user with the Relativity login page to obtain an access token for calling Relativity APIs. The application can then call the APIs to perform tasks for customized e-discovery workflows and automation.

You can also use the OAuth2 Client Manager API through REST. For more information, see OAuth2 Client Manager (.NET) .

## Fundamentals for the OAuth2 Client Manager API

Review the following information to learn about the methods and classes used by the OAuth2 Client Manager API.

Methods

The OAuth2 Client Manager API includes the following methods available on the IOAuth2ClientManager interface in the Relativity.Identity.<VersionNumber>.Services namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- CreateAsync() method - adds a new OAuth2 client to Relativity. This overloaded method offers two options for adding a client:

- Create an OAuth2 client by specifying the flow and redirectUris.

- Create an OAuth2 client by using OAuth2Client objects. See Create an OAuth2 client .

- DeleteAsync() method - removes an OAuth2 client from Relativity.

- SaveAsync() method - saves changes made to an OAuth2 client. See Update an OAuth2 client .

- RegenerateSecretAsync() method - generates a new secret for an OAuth2 client. All previous secrets are immediately invalidated. See Regenerate a client secret .

Classes and enumerations

The OAuth2 Client Manager API uses the following classes:

- Claim class - represents information about a user or OAuth2 client. It has these properties:

- Type - a string representing the type of claim.

- Value - a string representing the claim value.

-

OAuth2Client class - represents a OAuth2 client used for obtaining access tokens and authenticating web requests.

View property descriptions

- AccessTokenLifetimeInMinutes - the duration in minutes that access tokens issued to the clients are valid. We recommend using a duration based on the specified OAuth2 flow:

- Client credentials and code flow - use a short lifetime. We recommend that this value matches the default value of 1 hour or 60 minutes used by the Identity Server.

- Resource Owner access - use a lifetime of 1 hour because a client secret and a refresh token are available.

- Implicit flow tokens - match the lifetime of Relativity tokens, which is 10 hours or 600 minutes. After this time, the user must log in again.

- Name - a unique name for the OAuth2 client.

- Enabled - a Boolean value indicating whether the client is given access to Relativity. When a client is created, this value is automatically set to true.

- Flow - the mechanism for acquiring an authentication token. It is also called the OAuth2 grant type. This property is set during client creation and cannot be updated. The OAuth2Flow enum defines these values.

- Id - the unique identifier for the client. Relativity autogenerates this value if you do not specify it during client creation.

- IsSystem - a Boolean value indicating whether the OAuth2 client is an internal Relativity application. This property is read-only.

- RedirectUris - the URLs used to redirected the user after a request is authorized. These values must be specified for implicit or code flow types.

- Secret - the unique secret used by the client. Relativity autogenerates this value if you specify the Flow type as client credential, resource owner, or code.

- Scopes - a list of scopes this client is allowed to request. Currently, you cannot set this property, but the following table contains the default scopes:

Scope / Flow Implicit Client Credentials Code Resource Owner

id_token ✓ ✓ ✓

access_token ✓ ✓ ✓ ✓

refresh_token ✓ ✓ ✓

- ContextUser - used when assigning the user to the OAuth2 client for permissions and auditing. This property is required if OAuth2 flow is set to client credentials. It cannot be used for other flows.

- Claims - list of additional claims the OAuth2 client receives in access tokens. Only specific claim types are allowed by the system.

- OAuth2Flow enum - represents the workflow that an OAuth2 client uses for authorization. It defines the following flows:

- Implicit = 0

- Client Credentials = 1

- Code = 2

- Resource Owner = 3

## Guidelines for the OAuth2 Client Manager API

Use these guidelines when working with the OAuth2 Client Manager API:

- The Relativity user accessing the API must have the permissions required for working with OAuth2 client objects.

- Before creating a Relativity OAuth2 client, you must correctly identify the flow or grant type required by the client application. The supported flows are defined by the OAuth2Flow enum. See Classes and enumerations .

- In a typical programming workflow, you first create an OAuth2 client object, and then specify how long the access token granted to the client is valid.

- It may be necessary to regenerate the client secret for security purposes. The reset takes effect immediately or with a specified delay.

- System OAuth2 clients cannot be deleted.

## Create an OAuth2 client

Use the CreateAsync() method to add a new OAuth2 client to Relativity.

- You cannot create a client with an ID that already exists.

- You cannot set the Secret property of the OAuth2Client because it is currently unsupported.

View code sample Copy

```text
1
2
3
4
5
6
7
8
9
10
11
12
Identity.{versionNumber}.OAuth2ClientModels.OAuth2Client client = new Identity.{versionNumber}.OAuth2ClientModels.OAuth2Client

{

    Name = _clientName,

    Flow = Identity.{versionNumber}.OAuth2ClientModels.OAuth2Flow.ClientCredentials,

    RedirectUris = new List<Uri>(),

    AccessTokenLifetimeInMinutes = 180,

    ContextUser = 13941790

}

using (Relativity.Identity.{versionNumber}.Services.IOAuth2ClientManager oAuth2ClientManager = new ServiceFactory(settings).CreateProxy<IOAuth2ClientManager>())

{

    await _clientMgr.CreateAsync(client);

}
```

## Update an OAuth2 client

Use the SaveAsync() to update an OAuth2 client.

- Update the properties on the OAuth2Client object. This code sample sets the access token lifetime to 10 minutes and the client to active. Copy

```text
1
2
client.AccessTokenLifetimeInMinutes = 10;

client.Enabled = true;
```

- Call the SaveAsync() method by passing it the OAuth2Client object with updated property values: Copy

```text
1
await clientManager.SaveAsync(client);
```

## Regenerate a client secret

To regenerate a client secret, call the RegenerateSecretAsync() method by passing the generated ID of the OAuth2 client:

Copy

```text
1
string newSecret = await clientManager.RegenerateSecretAsync(client.Id);
```

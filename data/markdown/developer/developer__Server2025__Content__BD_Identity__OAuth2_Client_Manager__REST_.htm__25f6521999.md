---
title: "OAuth2 Client Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/OAuth2_Client_Manager__REST_.htm
collection: developer
fetched_at: 2026-06-22T06:26:59+00:00
sha256: 843f543064a71c2cc91d35e2a4d292409372fe1fc6ec85ffc1879c6cfa659f86
---

OAuth2 Client Manager (REST)

# OAuth2 Client Manager (REST)

In Relativity, you can use OAuth2 clients to configure external services and applications to authenticate against Relativity in a secure manner. For more information, see OAuth2 clients in the Relativity Documentation site.

The OAuth2Client Manager API exposes CRUD operations for OAuth2 clients. It also supports generating secrets for OAuth2 clients.

As a sample use case, you can implement a client application that presents the user with the Relativity login page to obtain an access token for calling Relativity APIs. The application can then call the APIs to perform tasks for customized e-discovery workflows and automation.

You can also use the OAuth2 Client Manager service through .NET. For more information, see OAuth2 Client Manager (.NET) .

## Guidelines for the OAuth2 Client Manager service

Review the following guidelines for working with the Federated Instance Manager service.

### URLs

The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 or v2

- Set the {clientID} to the Artifact ID of a given entity.

For example, you can use the following URL to delete a client:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/oauth2-clients/{clientID}
```

- {versionNumber} to the version of the service, such as v1 .

- {clientID} to the Artifact ID of the client to deleted.

## Create an OAuth2 client

The OAuth2 Client Manager service supports the following options for creating a client:

- Create a client with flow and redirectUrs

- Create a client with OAuth2Client object

### Create a client with flow and redirectUrs

To create an OAuth2 client by specifying a flow and redirectUrs, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/oauth2-clients
```

View field descriptions for a request

The body of the request contains the following fields:

- AccessTokenLifetimeInMinutes - the duration in minutes that access tokens issued to the clients are valid. For Client credentials and code flow, use a short lifetime. We recommend that this value matches the default value of 1 hour or 60 minutes used by the Identity Server.

- ContextUser - used when assigning the user to the OAuth2 client for permissions and auditing. This property is required if OAuth2 flow is set to client credentials. It cannot be used for other flows.

- Enabled - a Boolean value indicating whether the client is given access to Relativity. When a client is created, this value is automatically set to true.

- Flow - the mechanism for acquiring an authentication token. It is also called the OAuth2 grant type. This property is set during client creation and cannot be updated. The OAuth2Flow enum defines these values:

- Implicit = 0

- Client Credentials = 1

- Code = 2

- Resource Owner = 3

- Name - a unique name for the OAuth2 client.

- RedirectUris - an array of URLs for redirecting the user after a request is authorized. These values must be specified for implicit or code flow types.

View a sample JSON request Copy

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
{

   "AccessTokenLifetimeInMinutes":"180",

   "ContextUser":13941790,

   "Enabled":true,

   "Flow":"ClientCredentials",

   "Name":"Test Client 1",

   "RedirectUris":[

   ]

}
```

View field descriptions for a response

- AccessTokenLifetimeInMinutes - the duration in minutes that access tokens issued to the clients are valid. For Client credentials and code flow, use a short lifetime. We recommend that this value matches the default value of 1 hour or 60 minutes used by the Identity Server.

- Name - a unique name for the OAuth2 client.

- Enabled - a Boolean value indicating whether the client is given access to Relativity. When a client is created, this value is automatically set to true.

- Flow - the mechanism for acquiring an authentication token. It is also called the OAuth2 grant type. This property is set during client creation and cannot be updated. The OAuth2Flow enum defines these values:

- Implicit = 0

- Client Credentials = 1

- Code = 2

- Resource Owner = 3

- ID - the unique identifier for the client. Relativity autogenerates this value if you do not specify it during client creation.

- IsSystem - a Boolean value indicating whether the OAuth2 client is an internal Relativity application. This property is read-only.

- RedirectUris - an array of URLs for redirecting the user after a request is authorized. These values must be specified for implicit or code flow types.

- Secret - the unique secret used by the client. Relativity autogenerates this value if you specify the Flow type as client credential, resource owner, or code.

- Scopes - an array of scopes this client is allowed to request. Currently, you cannot set this property, but the following table contains the default scopes:

Scope / Flow Implicit Client Credentials Code Resource Owner

id_token ✓ ✓ ✓

access_token ✓ ✓ ✓ ✓

refresh_token ✓ ✓ ✓

- ContextUser - used when assigning the user to the OAuth2 client for permissions and auditing. This property is required if OAuth2 flow is set to client credentials. It cannot be used for other flows.

- Claims - an array of additional claims the OAuth2 client receives in access tokens. Only specific claim types are allowed by the system.

View a sample JSON response Copy

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
13
14
15
16
17
18
19
{

   "AccessTokenLifetimeInMinutes":480,

   "Name":"Test Client 1",

   "Enabled":true,

   "Flow":"ClientCredentials",

   "ID":"6ebd0b610e68c88aa5ededf22c",

   "IsSystem":false,

   "RedirectUris":[

   ],

   "Secret":"da7f44dc5dfa685891aa24c842e1f1289796c7f9",

   "Scopes":[

   ],

   "ContextUser":13941790,

   "Claims":[

   ]

}
```

### Create a client with OAuth2Client object

To create an OAuth2 client with OAuth2Client objects, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/oauth2-clients
```

View field descriptions for a request

The body of the response must contain a newClient object with the following fields:

- AccessTokenLifetimeInMinutes - the duration in minutes that access tokens issued to the clients are valid. For Client credentials and code flow, use a short lifetime. We recommend that this value matches the default value of 1 hour or 60 minutes used by the Identity Server.

- ContextUser - used when assigning the user to the OAuth2 client for permissions and auditing. This property is required if OAuth2 flow is set to client credentials. It cannot be used for other flows.

- Enabled - a Boolean value indicating whether the client is given access to Relativity. When a client is created, this value is automatically set to true.

- Flow - the mechanism for acquiring an authentication token. It is also called the OAuth2 grant type. This property is set during client creation and cannot be updated. The OAuth2Flow enum defines these values:

- Implicit = 0

- Client Credentials = 1

- Code = 2

- Resource Owner = 3

- Name - a unique name for the OAuth2 client.

- RedirectUris - an array of URLs for redirecting the user after a request is authorized. These values must be specified for implicit or code flow types.

View a sample JSON request Copy

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
{

   "newClient":{

      "AccessTokenLifetimeInMinutes":"180",

      "ContextUser":13941790,

      "Enabled":true,

      "Flow":"ClientCredentials",

      "Name":"Test Client 2",

      "RedirectUris":[

      ]

   }

}
```

View field descriptions for a response

- AccessTokenLifetimeInMinutes - the duration in minutes that access tokens issued to the clients are valid. For Client credentials and code flow, use a short lifetime. We recommend that this value matches the default value of 1 hour or 60 minutes used by the Identity Server.

- Name - a unique name for the OAuth2 client.

- Enabled - a Boolean value indicating whether the client is given access to Relativity. When a client is created, this value is automatically set to true.

- Flow - the mechanism for acquiring an authentication token. It is also called the OAuth2 grant type. This property is set during client creation and cannot be updated. The OAuth2Flow enum defines these values:

- Implicit = 0

- Client Credentials = 1

- Code = 2

- Resource Owner = 3

- ID - the unique identifier for the client. Relativity autogenerates this value if you do not specify it during client creation.

- IsSystem - a Boolean value indicating whether the OAuth2 client is an internal Relativity application. This property is read-only.

- RedirectUris - an array of URLs for redirecting the user after a request is authorized. These values must be specified for implicit or code flow types.

- Secret - the unique secret used by the client. Relativity autogenerates this value if you specify the Flow type as client credential, resource owner, or code.

- Scopes - an array of scopes this client is allowed to request. Currently, you cannot set this property, but the following table contains the default scopes:

Scope / Flow Implicit Client Credentials Code Resource Owner

id_token ✓ ✓ ✓

access_token ✓ ✓ ✓ ✓

refresh_token ✓ ✓ ✓

- ContextUser - used when assigning the user to the OAuth2 client for permissions and auditing. This property is required if OAuth2 flow is set to client credentials. It cannot be used for other flows.

- Claims - an array of additional claims the OAuth2 client receives in access tokens. Only specific claim types are allowed by the system.

View a sample JSON response Copy

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
13
14
15
16
17
18
19
{

   "AccessTokenLifetimeInMinutes":180,

   "Name":"Test Client 2",

   "Enabled":true,

   "Flow":"ClientCredentials",

   "ID":"c00de24425b3c969b657e663a4",

   "IsSystem":false,

   "RedirectUris":[

   ],

   "Secret":"0d5e9b34193dc18a634141289a9f178477a354da",

   "Scopes":[

   ],

   "ContextUser":13941790,

   "Claims":[

   ]

}
```

## Update an OAuth2 client

To update an OAuth2 client, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/oauth2-clients
```

View field descriptions for a request

The body of the request contains a client object with the following fields:

- AccessTokenLifetimeInMinutes - the duration in minutes that access tokens issued to the clients are valid. For Client credentials and code flow, use a short lifetime. We recommend that this value matches the default value of 1 hour or 60 minutes used by the Identity Server.

- Name - a unique name for the OAuth2 client.

- Enabled - a Boolean value indicating whether the client is given access to Relativity. When a client is created, this value is automatically set to true.

- Flow - the mechanism for acquiring an authentication token. It is also called the OAuth2 grant type. This property is set during client creation and cannot be updated. The OAuth2Flow enum defines these values:

- Implicit = 0

- Client Credentials = 1

- Code = 2

- Resource Owner = 3

- ID - the unique identifier for the client. Relativity autogenerates this value if you do not specify it during client creation.

- IsSystem - a Boolean value indicating whether the OAuth2 client is an internal Relativity application. This property is read-only.

- RedirectUris - an array of URLs for redirecting the user after a request is authorized. These values must be specified for implicit or code flow types.

- Secret - the unique secret used by the client. Relativity autogenerates this value if you specify the Flow type as client credential, resource owner, or code.

- Scopes - an array of scopes this client is allowed to request. Currently, you cannot set this property, but the following table contains the default scopes:

Scope / Flow Implicit Client Credentials Code Resource Owner

id_token ✓ ✓ ✓

access_token ✓ ✓ ✓ ✓

refresh_token ✓ ✓ ✓

- ContextUser - used when assigning the user to the OAuth2 client for permissions and auditing. This property is required if OAuth2 flow is set to client credentials. It cannot be used for other flows.

- Claims - an array of additional claims the OAuth2 client receives in access tokens. Only specific claim types are allowed by the system.

View a sample JSON request Copy

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
13
14
15
16
17
18
19
20
21
{

   "client":{

      "AccessTokenLifetimeInMinutes":460,

      "Name":"Test1",

      "Enabled":true,

      "Flow":"ClientCredentials",

      "ID":"444db2d2b819f6a6d66ac86865",

      "IsSystem":false,

      "RedirectUris":[

      ],

      "Secret":"798f5b9658ea37c7895d37b49abd5a9ffa01f835",

      "Scopes":[

      ],

      "ContextUser":13941790,

      "Claims":[

      ]

   }

}
```

When the OAuth2 client is successfully updated, the response returns the status code of 200. For more information, see HTTP status codes in Relativity REST APIs .

## Delete an OAuth2 client

To delete an OAuth2 client, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/oauth2-clients/{clientID}
```

The request body is empty.

When the OAuth2 client is successfully deleted, the response returns the status code of 200. For more information, see HTTP status codes in Relativity REST APIs .

## Regenerate a client secret

To regenerate an OAuth2 client secret, send a GET request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/Relativity-Identity/{versionNumber}/oauth2-clients/{clientID}/regenerate-secret
```

The request body is empty.

The response contains a string representing the new secret for the client:

Copy

```text
1
ccce232bccd58a467554c718e8638058ade3096b
```

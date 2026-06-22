---
title: "Authentication provider type (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/Authentication_Provider_Type__REST_.htm
collection: developer
fetched_at: 2026-06-22T06:25:37+00:00
sha256: e172fcea5ec4b60c61437e2fc42337c216b1e70bdcbe8b0c39fa8eb0284472c5
---

Authentication provider type (REST)

# Authentication provider type (REST)

An authentication provider type represents an authentication protocol available for use in Relativity. Admins can enable or disable an authentication provider type for users, but they cannot remove them from the system. For more information, see Authentication in the Relativity Documentation site.

The Authentication Provider Type service exposes functionality for programmatically enabling and disabling authentication protocols used by Relativity. It also provides endpoints to read one or more provider types.

You can use the Authentication Provider Type service through .NET. For more information, see Authentication provider type (.NET) .

## Guidelines for the Authentication Provider Type service

Review the following guidelines for working with the Authentication Provider Type service.

### URLS

The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 or v2

- Set {providerTypeName} parameter in the URLs to the string representing the provider's name.

## Retrieve an authentication provider type

To retrieve an authentication provider type, send a GET request with a URL in the following format:

Copy

```text
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/auth-provider-types/{providerTypeName}
```

The request body is empty.

The response contains the following fields:

- Name - a string representing the name of the protocol.

- Type - a ProtocolType enum indicating protocol that the authentication provider type uses as follows:

- External - a protocol type requiring the user to authenticated with an external identity provider.

- Local - a protocol type requiring the user to enter credentials on the login page.

- Description - a string describing the protocol.

- IsEnabled - a Boolean value indicating whether the authentication provider type is enabled. The values for this field are true or false.

The response contains the following sample JSON:

Copy

```text
1
2
3
4
5
6
{

   "Name":"Password",

   "Type":"Local",

   "Description":"Authenticate using an e-mail address and a password.",

   "IsEnabled":true

}
```

## Read all authentication provider types

To read all available authentication provider types, send a GET request with a URL in the following format:

Copy

```text
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/auth-provider-types
```

The request body is empty.

See the field descriptions for the response in Retrieve an authentication provider type .

The response contains the following sample JSON:

Copy

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
[

   {

      "Name":"Password",

      "Type":"Local",

      "Description":"Authenticate using an e-mail address and a password.",

      "IsEnabled":true

   },

   {

      "Name":"Integrated Authentication",

      "Type":"External",

      "Description":"Authenticate using integrated Kerberos / NTLM.",

      "IsEnabled":true

   },

   {

      "Name":"Active Directory",

      "Type":"Local",

      "Description":"Authenticate using an e-mail address and an Active Directory password.",

      "IsEnabled":true

   }

]
```

## Update an authentication provider type

To enable or disable an authentication provider type, send a POST request with a URL in the following format:

Copy

```text
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/auth-provider-types
```

The request must contain the following fields:

- name - a string representing the name of the protocol.

- isEnabled - a Boolean value indicating whether to enable or disable authentication provider type. The values for this field are true or false.

This sample JSON request disables a password authentication type:

Copy

```text
1
2
3
4
{

   "name":"RSA",

   "isEnabled":false

}
```

The response contains a status code of 200 when the update succeeds and 400 when it fails.

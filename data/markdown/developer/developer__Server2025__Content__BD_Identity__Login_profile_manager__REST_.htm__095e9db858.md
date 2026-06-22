---
title: "Login Profile Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/Login_profile_manager__REST_.htm
collection: developer
fetched_at: 2026-06-22T06:26:47+00:00
sha256: 810af21908f4d7ef0894645a04862cd6a09dfdb2dd2557ab67ec6d0beecacbd7
---

Login Profile Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Login Profile Manager (REST)

The login profile defines how an individual user logs into Relativity by setting user-specific options for each provider in the authentication profile. Each entry in the user's login profile corresponds to a matching entry in the environment's authentication profile, such as Provider in the environment for Password, Integrated Authentication, Active Directory, RSA, and Client Certificate.

The Login Profile Manager service is used to configure authentication profiles and user login profiles.

- Authentication profile - The authentication profile is a collection of authentication providers which user login methods are created from. For example, the authentication profile is where you configure Password settings such as min and max password length. It also is where you define external identity providers that use the OpenID Connect and SAML protocols. How you configure your authentication profile determines how the look and behavior of the Relativity login page.

- Login Profile - While the authentication profile applies to the environment, each user has a Login Profile that defines the user-specific options for various providers on the authentication profile. Each entry in the user's Login Profile corresponds to a matching entry in the environment's authentication profile. Each user automatically has a login profile upon creation, and you cannot delete that profile.

You can also use the Login Profile Manager service through .NET. For more information, see Login Profile Manager (.NET) .

## Guidelines for the Login Profile Manager service

Review the following guidelines for working with this service.

### URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

See Login Profile Manager (.NET) for more information.

## Get global authentication profile

To retrieve the global authentication profile, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/auth-profile/global
```

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- ID - an integer representing the ID of the profile.

- IsGlobal - a Boolean value indicating whether this profile is the global authentication profile for Relativity.

- Description - a string describing the profile.

- Password - the Password Provider for this profile. A null value indicates that password authentication is disabled for this profile.

- Name - the name of the provider.

- IsEnabled - a Boolean value indicating whether the provider is enabled.

- MinimumPasswordLength - an integer indicating the minimum password length allowed.

- MaximumPasswordLength - an integer indicating the maximum password length allowed.

- MaximumPasswordAgeInDaysDefaultValue - an integer indicating the default number of days until a user is forced to change the password.

- UsersCanChangePasswordDefaultValue - a Boolean value indicating whether users are allowed to change their passwords.

- AdminsCanSetPassword - a Boolean value indicating whether admins can set user passwords.

- AllowEmailPasswordRecovery - a Boolean value indicating whether email password recovery is available for users.

- PasswordRecoveryRequestLimit - an integer indicating the maximum number of email password recovery requests that can be outstanding at one time for a given user.

- MaximumPasswordHistory - the number of passwords to remember when setting a new password. Users cannot set their password to any previous passwords within the defined window size. Setting this value to zero disables password history checking.

- MaximumInvalidLoginAttempts - an integer indicating the number of attempts users are allowed before locking their password methods.

- AdditionalWorkFactor - a measure of the amount of time required to verify a password when a user logs into Relativity.

The value of this setting is added to the work factor for the Relativity environment. Set this value to zero to use the default work factor for the Relativity environment. In most cases, this value is sufficient.

- IntegratedAuthentication - the Integrated Authentication Provider for this profile. A null value indicates that Windows authentication is disabled for this profile.

- Name - the name of the provider.

- IsEnabled - a Boolean value indicating whether the provider is enabled.

- ActiveDirectory - the Active Directory Provider for this profile. A null value indicates that Active Directory authentication is disabled for this profile.

- Name - the name of the provider.

- IsEnabled - a Boolean value indicating whether the provider is enabled.

- ClientCertificate - the Client Certificate Provider for this profile. A null value indicates that client certificate authentication is disabled for this profile.

- Name - the name of the provider.

- Description - a string describing the provider

- IsEnabled - a Boolean value indicating whether the provider is enabled.

- DisplayOnLoginPage - a Boolean value indicating whether a button for this provider is displayed on the Relativity login page.

- Caption -the text used for the button in the UI.

- RSA - the RSA Provider for this profile. A null value indicates that client certificate authentication is disabled for this profile.

- Name - the name of the provider.

- IsEnabled - a Boolean value indicating whether the provider is enabled.

- OpenIDConnectProviders - an array of OpenID Connect providers for this profile.

- SAML2Providers - an array of SAML2P providers for this profile.

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
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
{

   "ID":1,

   "IsGlobal":true,

   "Description":"Global Authentication Profile",

   "Password":{

      "Name":"Default Password Provider",

      "IsEnabled":true,

      "MinimumPasswordLength":8,

      "MaximumPasswordLength":50,

      "MaximumPasswordAgeInDaysDefaultValue":0,

      "UsersCanChangePasswordDefaultValue":true,

      "AdminsCanSetPassword":true,

      "AllowEmailPasswordRecovery":false,

      "PasswordRecoveryRequestLimit":10,

      "MaximumPasswordHistory":5,

      "MaximumInvalidLoginAttempts":10,

      "AdditionalWorkFactor":0

   },

   "IntegratedAuthentication":{

      "Name":"Default Integrated Authentication Provider",

      "IsEnabled":true

   },

   "ActiveDirectory":{

      "Name":"Default Active Directory Provider",

      "IsEnabled":true

   },

   "ClientCertificate":{

      "Name":"Default Smart Card Provider",

      "Description":"",

      "IsEnabled":true,

      "DisplayOnLoginPage":false,

      "Caption":""

   },

   "RSA":{

      "Name":"Default RSA Provider",

      "IsEnabled":true

   },

   "OpenIDConnectProviders":[



   ],

   "SAML2Providers":[



   ]

}
```

## Update an authentication profile

To update an authentication profile, send a PUT with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/auth-profile
```

The request for an update operation contains the same fields as a response for a create operation. See the descriptions in View field descriptions for a response .

View a sample JSON request

This sample request illustrates how to update each provider type. The response contains a profile object with the following fields:

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
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
{

   "profile":{

      "ID":1,

      "IsGlobal":true,

      "Description":"Global Authentication Profile",

      "Password":{

         "Name":"Default Password Provider",

         "IsEnabled":true,

         "MinimumPasswordLength":8,

         "MaximumPasswordLength":50,

         "MaximumPasswordAgeInDaysDefaultValue":0,

         "UsersCanChangePasswordDefaultValue":true,

         "AdminsCanSetPassword":true,

         "AllowEmailPasswordRecovery":false,

         "PasswordRecoveryRequestLimit":10,

         "MaximumPasswordHistory":5,

         "MaximumInvalidLoginAttempts":10,

         "AdditionalWorkFactor":0

      },

      "IntegratedAuthentication":{

         "Name":"Default Integrated Authentication Provider",

         "IsEnabled":true

      },

      "ActiveDirectory":{

         "Name":"Default Active Directory Provider",

         "IsEnabled":true

      },

      "ClientCertificate":{

         "Name":"Default Smart Card Provider",

         "Description":"",

         "IsEnabled":true,

         "DisplayOnLoginPage":false,

         "Caption":""

      },

      "RSA":{

         "Name":"Default RSA Provider",

         "IsEnabled":true

      },

      "OpenIDConnectProviders":[



      ],

      "SAML2Providers":[



      ]

   }

}
```

When the profile is successfully updated, the response returns the status code of 200. For more information, see HTTP status codes in Relativity REST APIs .

## Get a login profile for a user

To get a login profile for a user, send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/{userID:int}/login-profile
```

The request body is empty.

View field descriptions for a response

The response contains the following fields:

- UserID - an integer representing the ID of the profile.

- Password - a login method that requires the user to enter a password. It contains the following fields:

- Email - a string representing the email address of the user.

- InvalidLoginAttempts - an integer representing the number of login attempts that failed.

- IsEnabled - a Boolean value indicating whether the login method is enabled.

- MustResetPasswordOnNextLogin - a Boolean value indicating whether the user is forced to reset the password after the next successful login.

- UserCanChangePassword - a Boolean value indicating whether the user can change the password.

- PasswordExpirationInDays - an integer indicating the number of days a new password is valid, that is until it expires. Set this property to zero if you do not want the password to expire.

- PasswordExpires - the date and time when the current password expires.

- TwoFactorMode - a string providing information used for two factor authentication ( None , Always , or OutsideRestrictedIPs ).

- TwoFactorInfo - a string containing your email address if TwoFactorMode is set to Always or OutsideRestrictedIPs. If TwoFactorMode is set to None, the string is left empty.

- TwoFactorProtocol - a string set to Authenticator or Email if TwoFactorMode is set to Always or OutsideRestrictedIPs. If TwoFactorMode is set to None, the string is left empty.

- OpenIDConnectProviders - an array of OpenID Connect providers for this profile.

- SAML2Providers - an array of SAML2P providers for this profile.

For examples of additional providers, see View field descriptions for a response .

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

   "UserID":9,

   "Password":{

      "Email":"relativity.admin@kcura.com",

      "InvalidLoginAttempts":0,

      "IsEnabled":true,

      "MustResetPasswordOnNextLogin":false,

      "UserCanChangePassword":true,

      "PasswordExpirationInDays":0,

      "PasswordExpires":"9999-12-31T23:59:59.9999999",

      "TwoFactorMode":"None"

   },

   "OpenIDConnectMethods":[



   ],

   "SAML2Methods":[



   ]

}
```

## Update a login profile for a user

To update a user's profile, send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/{userID:int}/login-profile
```

View field descriptions for a request

The request contains a profile object with the same fields as the following fields:

- UserID - an integer representing the ID of the profile.

- Password - a login method that requires the user to enter a password. It contains the following fields:

- Email - a string representing the email address of the user.

- InvalidLoginAttempts - an integer representing the number of login attempts that failed.

- IsEnabled - a Boolean value indicating whether the login method is enabled.

- MustResetPasswordOnNextLogin - a Boolean value indicating whether the user is forced to reset the password after the next successful login.

- UserCanChangePassword - a Boolean value indicating whether the user can change the password.

- PasswordExpirationInDays - an integer indicating the number of days a new password is valid, that is until it expires. Set this property to zero if you do not want the password to expire.

- PasswordExpires - the date and time when the current password expires.

- TwoFactorMode - a string providing information used for two factor authentication ( None , Always , or OutsideRestrictedIPs ).

- TwoFactorInfo - a string containing your email address if TwoFactorMode is set to Always or OutsideRestrictedIPs. If TwoFactorMode is set to None, the string is left empty.

- TwoFactorProtocol - a string set to Authenticator or Email if TwoFactorMode is set to Always or OutsideRestrictedIPs. If TwoFactorMode is set to None, the string is left empty.

- OpenIDConnectProviders - an array of OpenID Connect providers for this profile.

- SAML2Providers - an array of SAML2P providers for this profile.

For examples of additional providers, see View field descriptions for a response .

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

   "profile":{

      "UserID":9,

      "Password":{

         "Email":"relativity.admin@kcura.com",

         "InvalidLoginAttempts":0,

         "IsEnabled":true,

         "MustResetPasswordOnNextLogin":false,

         "UserCanChangePassword":true,

         "PasswordExpirationInDays":0,

         "PasswordExpires":"9999-12-31T23:59:59.9999999",

         "TwoFactorMode":"None"

      },

      "OpenIDConnectMethods":[



      ],

      "SAML2Methods":[



      ]

   }

}
```

When the profile is successfully updated, the response returns the status code of 200. For more information, see HTTP status codes in Relativity REST APIs .

## Helper endpoints for invitation emails

The Login Profile Manager service has helper endpoints that you can use to send invitations to newly-created users to log in to Relativity and set their passwords.

### Verify that invitation emails can be sent successfully

Before sending invitation emails, you can determine whether the users can be invited. Send a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/bulk-invitation/verify
```

The request must include an array of the Artifact IDs for users .

Copy

```text
1
2
3
4
5
6
{

   "userIDList":[

      "102010",

      "12313123"

   ]

}
```

View a sample JSON response

The response contains any validation errors:

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
{

   "Success":false,

   "Errors":[

      {

         "UserID":102010,

         "Exception":"SMTP server not running, verify smtp settings",

         "StatusCode":422

      },

      {

         "UserID":12313123,

         "Exception":"SMTP server not running, verify smtp settings",

         "StatusCode":422

      }

   ]

}
```

### Send a single invitation email

To send an invitation email, issue a POST request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/{userID:int}/invitation
```

The request body is empty.

When the invitation is successfully sent, the response returns the status code of 200. For more information, see HTTP status codes in Relativity REST APIs .

### Send bulk invitations to users

To send invitations to multiple users, send a POST request with a URL in the following format:

Copy

```text
1
<host>Relativity.REST/api/Relativity-Identity/{versionNumber}/users/bulk-invitation
```

The request must contain an array of the Artifact IDs for the users who should receive the invitations:

Copy

```text
1
2
3
4
5
6
{

   "userIDList":[

      "102010",

      "12313123"

   ]

}
```

View sample JSON responses

If any of the invitations fail to be sent, the response returns the Success flag with the value of false, and the errors for specific users:

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
{

   "Success":false,

   "Errors":[

      {

         "UserID":102010,

         "Exception":"SMTP server not running, verify smtp settings",

         "StatusCode":422

      },

      {

         "UserID":12313123,

         "Exception":"SMTP server not running, verify smtp settings",

         "StatusCode":422

      }

   ]

}
```

If all invitations are successfully sent, the response does not contain any errors:

Copy

```text
1
2
3
4
{

  "Success": true,

  "Errors": []

}
```

### Set a user's password

To set the user's password, send a PUT request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/{userID:int}/login-profile/set/password
```

The request body must include a string value for the password:

Copy

```text
1
2
3
{

   "password":"newpassword"

}
```

When the password is successfully set, the response returns the status code of 200. For more information, see HTTP status codes in Relativity REST APIs .

### Reset authenticator secret (2FA)

To set the authenticator secret, send a DELETE request with a URL in the following format:

Copy

```text
1
<host>/Relativity.REST/api/Relativity-Identity/{versionNumber}/users/{userID:int}/login-method/{loginMethodID:int}/two-factor-application
```

The request must contain a value for the login method ID:

Copy

```text
1
2
3
{

   "loginMethodID":1010121

}
```

When the secret is successfully reset, the response returns the status code of 200. For more information, see HTTP status codes in Relativity REST APIs .

On this page

- Login Profile Manager (REST)

- Guidelines for the Login Profile Manager service

- URLs

- Get global authentication profile

- Update an authentication profile

- Get a login profile for a user

- Update a login profile for a user

- Helper endpoints for invitation emails

- Verify that invitation emails can be sent successfully

- Send a single invitation email

- Send bulk invitations to users

- Set a user's password

- Reset authenticator secret (2FA)


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use

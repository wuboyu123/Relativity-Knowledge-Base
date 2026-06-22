---
title: "Authentication provider type (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/Authentication_Provider_Type__.NET_.htm
collection: developer
fetched_at: 2026-06-22T06:25:33+00:00
sha256: 463cb8f685964c49bb0f75cbf2b457423ec3525270d5e9bf51ccc6e1fc2758fb
---

Authentication provider type (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Authentication provider type (.NET)

An authentication provider type represents an authentication protocol available for use in Relativity. Admins can enable or disable an authentication provider type for users, but they cannot remove them from the system. For more information, see Authentication in the Relativity Documentation site.

The Authentication Provider Type API exposes functionality for programmatically enabling and disabling authentication protocols used by Relativity. It also provides methods to read one or more provider types.

You can use the Authentication Provider Type API through REST. For more information, see Authentication provider type (REST) .

## Fundamentals for the Authentication Provider Type API

Review the following information to learn about the methods and classes used by the Authentication Provider Type API.

### Methods

The Authentication Provider Type API includes the following methods available on the IAuthProviderTypeManager interface in the Relativity.Identity.<VersionNumber>.Services namespace.

The <VersionNumber> variable in the namespace indicates the version number of the API. The version number uses the format uppercase V and an integer version number , such as V1 or V2 in .NET.

- ReadAsync() method - retrieves a single authentication provider type by name. It returns an AuthProviderType object.

- ReadAllAsync() method - retrieves all available authentication provider types.

- UpdateAsync() method - modifies a single provider type by enabling or disabling it.

To enable an authentication provider type, call the UpdateAsync() method by passing the provider's name and true parameter. To disable it, pass provider's name and the false to the method.

### Classes

The Authentication Provider Type API uses the following class and enumeration:

- AuthProviderType class - represents an authentication provide type. It contains the following fields:

- Name - a string representing the name of the protocol.

- IsEnabled - a Boolean value indicating whether the authentication provider type is enabled. The values for this field are true or false.

- Type - a ProtocolType enum indicating protocol that the authentication provider type uses.

- Description - a string describing the protocol.

- ProtocolType enum - indicates the type of authentication provider as follows:

- Local - a protocol type requiring the user to enter credentials on the login page.

- External - a protocol type requiring the user to authenticated with an external identity provider.

## Guidelines for the Authentication Provider Type API

Use these guidelines when working with authentication providers:

- Wrap the IAuthProviderTypeManager interface proxy in a using block.

- Avoid disabling all types or types used primarily to log in to the Relativity instance. Disabling these providers may lock all users out of the instance.

## Code sample

The following code sample ensures that only Password and OpenIDConnect types are enabled.

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
using (Relativity.Identity. {versionNumber}.Services.IAuthProviderTypeManager authProviderTypeManager = new ServiceFactory(settings).CreateProxy<IAuthProviderTypeManager>()) {

  IEnumerable<AuthProviderType> providerTypes = await authProviderTypeManager.ReadAllAsync();

  foreach(AuthProviderType type in providerTypes) {

    if (!(type.Name.Equals("Password") || type.Name.Equals("OpenID Connect")) && type.IsEnabled) {

      authProviderTypeManager.UpdateAsync(type.Name, false);

    }

  }

}
```

On this page

- Authentication provider type (.NET)

- Fundamentals for the Authentication Provider Type API

- Methods

- Classes

- Guidelines for the Authentication Provider Type API

- Code sample


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

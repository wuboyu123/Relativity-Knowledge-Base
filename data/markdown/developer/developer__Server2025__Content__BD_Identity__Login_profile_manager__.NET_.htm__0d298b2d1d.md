---
title: "Login Profile Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/Login_profile_manager__.NET_.htm
collection: developer
fetched_at: 2026-06-22T06:25:08+00:00
sha256: 6cd6eadb91e1a1a925888cf0abf9c8fac2644cdcc0e84cd44e672a8190ffc660
---

Login Profile Manager (.NET) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Login Profile Manager (.NET)

The login profile defines how an individual user logs into Relativity by setting user-specific options for each provider in the authentication profile. Each entry in the user's login profile corresponds to a matching entry in the environment's authentication profile, such as Provider in the environment for Password, Integrated Authentication, Active Directory, RSA, and Client Certificate.

The Login Profile Manager API is uses to configure authentication profiles and user login profiles:

- Authentication profile - The authentication profile is a collection of authentication providers which user login methods are created from. For example, the authentication profile is where you configure Password settings such as min and max password length. It also is where you define external identity providers that use the OpenID Connect and SAML protocols. How you configure your authentication profile determines how the look and behavior of the Relativity login page.

- Login profile - While the authentication profile applies to the environment, each user has a Login Profile that defines the user-specific options for various providers on the authentication profile. Each entry in the user's Login Profile corresponds to a matching entry in the environment's authentication profile. Each user automatically has a login profile upon creation, and you cannot delete that profile.

You can interact with the Login Profile Manager using the ILoginProfileManager interface. The methods on the interface allow you to retrieve and update a user's login profile and Relativity's authentication profile. You can also send out login invitation emails and manually set passwords.

You can also use the Login Profile Manager API through REST. For more information, see Login Profile Manager (REST) .

## Fundamentals for the Login Profile Manager API

Review the following information to learn about the methods and classes used by the Login Profile Manager API.

Methods

- GetGlobalProfileAsync() - reads the authentication profile for the Relativity Instance.

- SaveProfileAsync(AuthProfile profile) - updates the authentication profile to match the submitted profile.

- GetLoginProfileAsync(int userID) - get a Login Method Profile for a given user.

- UpdateLoginProfileAsync(int userID, LoginProfile profile) - save a Login Method profile.

- SetPasswordAsync(int userID, string password) - explicitly set a user's password.

- SendInvitationAsync(int userID) - sends an Invitation Workflow email to each specified user.

- SendBulkInvitationAsync(IEnumerable<int> userIDList) - sends an Invitation Workflow email to each specified user.

- VerifyBulkInvitationAsync(IEnumerable<int> userIDList) - verifies an Invitation Workflow without sending an email.

Classes

- AuthProfile

- ID (Integer) - The ID of the profile.

- SiteUri (Uri) - The public uri of the relativity instance. Used during creation of password invite and redirect urls for SAML and OpenID Connect Providers.

- IsGlobal (Boolean) - Boolean representing if profile is global. Always true.

- Description (String) - Description of the profile

- ActiveDirectory - The Active Directory provider. This provider is not supported in Relativity One.

- ClientCertificate - The Client Certificate provider. This provider is not supported in Relativity One.

- IntegratedAuthentication - The Integrated Authentication provider. This provider is not supported in Relativity One.

- OpendIDConnectProviders - The list of OpenID Connect providers

- PasswordProvider - The Password Provider

- RSA - The RSA provider. This provider is not supported in Relativity One.

- SAML2Providers - The list of SAML2 providers

- ActiveDirectoryProvider

- Name (String) - The name for the provider; must be unique within the profile.

- IsEnabled (Boolean) - Whether the provider is enabled or not.

- ClientCertificateProvider

- Name (String) - The name for the provider; must be unique within the profile.

- Description (String) - A description for the provider.

- IsEnabled (Boolean) - Whether the provider is enabled or not.

- DisplayOnLoginPage (Boolean) - Determines if the login page should display a button for users to click to authenticate with a client certificate.

- Caption (String) - The caption text to display on the login page button. Only used if DisplayOnLoginPage is true.

- IntegratedAuthenticationProvider

- Name (String) - The name for the provider; must be unique within the profile.

- IsEnabled (Boolean) - Whether the provider is enabled or not.

- OpendIDConnectProvider

- RedirectUri (Uri) - Relativity Url the identity provider should POST signed assertions to log users in. This property is read-only and generated by Relativity.

- Flow (OAuth2Flow enum) - Specifies the authorization grant type Relativity will use for interacting with the identity provider.

- Authority (Uri) - The public base url of the OpenID Connect provider. Relativity must be able to resolve the OpenID Connect well-known endpoint from this url (<authority>/.well-known/openid-configuration)

- ClientID (String) - The client identifier of the relativity instance created by the OpenID Connect provider

- ClientSecret (String) - The client secret of the relativity instance created by the OpenID Connect provider

- Caption (String) - The caption text to display on the login page button. Only used if DisplayOnLoginPage is true.

- DisplayOnLoginPage (Boolean) - Determines if the login page should display a button for users to click to authenticate with this OpenID Connect provider.

- IsEnabled (Boolean) - Whether the provider is enabled or not.

- Description (String) - A description for the provider.

- Name (String) - The name for the provider; must be unique within the profile.

- SubjectClaimType (String) - The claim type to use for matching the assertion to a user's login method. Defaults to the "sub" claim.

- Scopes (List<String>) - List of identity scopes Relativity will request from the identity provider

- PasswordProvider

- Name (String) - The name for the provider; must be unique within the profile.

- IsEnabled (Boolean) - Whether the provider is enabled or not.

- MinimumPasswordLength (Integer) - Minimum password length, users with passwords shorter than this will need to reset their password on next login.

- MaximumPasswordLength (Integer) - Minimum password length, users with passwords longer than this will need to reset their password on next login.

- MaximumPasswordAgeInDaysDefaultValue (Integer) - Maximum days that a user's password can be active until the user will need to reset their password on next login

- UsersCanChangePasswordDefaultValue (Boolean) - Default UI setting for whether users can change their password.

- AdminsCanSetPassword (Boolean) - Boolean representing if system administrators can set a user's password.

- AllowEmailPasswordRecovery (Boolean) - Determines whether email password recovery is available for users.

- PasswordRecoveryRequestLimit (Integer) - The maximum number of email password recovery requests that can be outstanding at one time for a given user.

- MaximumPasswordHistory (Integer) - Number of previous passwords Relativity will track to prevent user's from reusing a password. Setting this value to zero will disable previous password checks.

- MaximumInvalidLoginAttempts (Integer) - The number of attempts a user is allowed to use before locking their password method.

- AdditionalWorkFactor (Integer) - A measure of the amount of time required to verify a password when a user logs into Relativity.

- RSAProvider

- Name (String) - The name for the provider; must be unique within the profile.

- IsEnabled (Boolean) - Whether the provider is enabled or not.

- SAML2Provider

- Name (String) - The name for the provider; must be unique within the profile.

- Description (String) - A description for the provider.

- IsEnabled (Boolean) - Whether the provider is enabled or not.

- Issuer (String) - Url of the identity provider issuing the SAML Assertion.

- Audience (String) - Identifier for the application receiving the assertion.

- RedirectUri (System.Uri) - Relativity Url the identity provider should POST signed assertions to log users in. This property is read-only and generated by Relativity.

- Certificate (String) - PEM formatted public keys used to validate incoming assertions.

- SubjectClaimType (String) - The claim type to use for matching the assertion to a user's login method. Defaults to "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier".

- LoginProfile

- UserID (Integer)

- Password

- IntegratedAuthentication

- ActiveDirectory

- ClientCertificate

- RSA

- List<OpenIDConnectMethods>

- List<SAML2Methods>

- PasswordMethod

- Email (string) - The email address of the user

- InvalidLoginAttempts (int) - Number of attempts to log in with the password that have not succeeded.

- IsEnabled (boolean) - Whether the login method is enabled

- MustResetPasswordOnNextLogin (boolean) - Controls whether the user is forced to reset their password after the next successful login

- UserCanChangePassword (boolean) - Whether the user can change their own password

- PasswordExpirationInDays (int) - The number of days a new password is valid for until it expires. A value of zero will set a password to never expire.

- PasswordExpires (System.DateTime) - The date and time that the current password will expire.

- TwoFactorInfo (string) - Information used for two factor authentication

- TwoFactorMode (TwoFactorMode) - Determines when two factor authentication is used.

- TwoFactorProtocol (TwoFactorProtocol) - The selected protocol to use if two factor authentication is enabled

- IntegratedAuthenticationMethod

- Account (string) - The name of the user account in Active Directory. It can be specified as a SAM Account (domain\username) or as a UPN (user@fully-qualified-domain)

- IsEnabled (bool) - Whether the login method is enabled

- ActiveDirectoryMethod

- Account (string) - The name of the user account in Active Directory. It can be specified as a SAM Account (domain\username) or as a UPN (user@fully-qualified-domain)

- IsEnabled (bool) - Whether the login method is enabled

- ClientCertificateMethod

- Name (string) - A name of the matching certificate provider from the corresponding Auth Profile.

- Subject (string) - The value to match against in the Common Name (CN) or Subject Alternate Name (SAN) of the client certificate.

- IsEnabled (bool) - Whether the login method is enabled

- RSAMethod

- Subject (string) - The RSA login name or email address to match against

- IsEnabled (bool) - Whether the login method is enabled

- OpenIDConnectMethod

- ProviderName (string) - The name of the OpenId Connect provider this login method belongs to

- Subject (string) - The lookup value to match an external identity to the user.

- IsEnabled (bool) - Whether the login method is enabled

- SAML2Method

- ProviderName (string) - The name of the SAML2 provider this login method belongs to

- Subject (string) - The lookup value to match an external identity to the user.

- IsEnabled (bool) - Whether the login method is enabled

- TwoFactorMode Enum

- None -Two Factor authentication is turned off.

- Always - User must always use Two Factor authentication when logging in.

- OutsideRestrictedIPs - User must use Two Factor authentication when logging in from an IP address that is outside the trusted IP list.

- TwoFactorProtocol

- Email - Use email to facilitate two factor codes

- Authenticator -Use an authenticator app to facilitate two factor codes

## Guidelines for the Login Profile Manager API

Before programmatically interacting with login profiles, familiarize yourself with the Relativity authentication provider user interface and review the information in the Relativity Documentation site . Note there is a strong correlation between the API operations and object properties and the user interface elements.

Use these guidelines when working with authentication methods:

- The user must have the permissions required for working with Relativity login methods.

- Login methods are interacted with through the user login method profile. The profile is the collection of all the methods for that user.

- There can only be one method instance for each authentication provider.

- A user can only have one of the following provider type methods active at any one time: Password, RSA, Active Directory.

### Read a user login profile and create a login method

The following code sample shows how to read in a User Login Profile and create a login method for an OpenIDConnect provider.

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
13
14
15
16
using (Relativity.Identity.{versionNumber}.Services.ILoginProfileManager loginProfileManager = new ServiceFactory(settings).CreateProxy<ILoginProfileManager>())

{

LoginProfile profile = await loginProfileManager.GetLoginProfileAsync(1012311);



if(profile.OpenIDConnectMethods.SingleOrDefault(x => x.ProviderName.Equals("My OIDC Provider")) == null)

{

OpenIDConnectMethod oidcMethod = new OpenIDConnectMethod() {

IsEnabled = true,

ProviderName = "My OIDC Provider",

Subject = "0e58f970-2113-4a6e-8655-82c10e6d9412"

};

profile.OpenIDConnectMethods.Add(oidcMethod);



loginProfileManager.UpdateLoginProfileAsync(1012311, profile);

}

}
```

On this page

- Login Profile Manager (.NET)

- Fundamentals for the Login Profile Manager API

- Guidelines for the Login Profile Manager API

- Read a user login profile and create a login method


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

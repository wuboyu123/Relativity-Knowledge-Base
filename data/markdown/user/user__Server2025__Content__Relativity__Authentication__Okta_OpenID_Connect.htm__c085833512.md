---
title: "Okta OpenID Connect"
url: https://help.relativity.com/Server2025/Content/Relativity/Authentication/Okta_OpenID_Connect.htm
collection: user
fetched_at: 2026-06-22T06:17:41+00:00
sha256: 21ddb62c61118128d86670c094f7f370f6cf58bb4e025ba488d1240dc9b41f03
---

Okta OpenID Connect Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Okta OpenID Connect

Okta can be set up as an OpenID Connect authentication provider to log users into a different Relativity instance.

This documentation contains references to third-party software, or technologies. While efforts are made to keep third-party references updated, the images, documentation, or guidance in this topic may not accurately represent the current behavior or user interfaces of the third-party software. For more considerations regarding third-party software, such as copyright and ownership, see Terms of Use .

## Pre-requisites

- To configure Okta as an OpenID Connect provider for Relativity, you, or your Okta admin, will need to set up the Relativity app in Okta. To complete this part of the configuration, follow the steps in the Okta documentation . During the process, select Web as the platform and OpenID Connect as the sign-on method. After completing the steps provided by Okta and customizing the steps for Relativity, you will navigate back to Relativity.

- The Okta ‘Initiate login URI’ setting may need an HRD parameter. For more information, see Creating or editing a federated instance .

## Configuring Okta OpenID Connect

In Relativity, navigate to the Authentication Provider tab. On the Authentication Provider, fill in the fields as follows:

### Authentication provider information

- Name —enter a user-friendly name for the authentication provider.

- Provider Type —select OpenID Connect .

- Enabled —the provider is enabled by default. However, you can disable it.

- Site URL —set the URL that users enter in the browser to access an instance of Relativity.

- Example —https://company.relativity.one/Relativity

### Authentication provider settings

- OAuth2 Flow —select Implicit or Code .

- Client ID —enter the Client ID from your Okta parameters Client ID.

- Client Secret —enter the Client Secret from your Okta parameters client secret [Code flow] .

- Display on login screen —determines if the OpenID Connect button displays on the login page.

- Login Screen Button Text —determines the text that appears on the button displayed on the login page.

- Authority URL —[the Okta domain parameter] (i.e. http://customer.okta.com). The Authority URL can be retrieved from the Sign On tab in Okta. If you go to the OpenID Connect ID Token section and in the Issuer area.

- Scopes —the default value for this field is openid . The openid checkbox must be selected because it's a required setting. However, you can also select the email or profile option.

The identity provider responds with the claims associated with the scopes that you request. In other words, the scopes translate into claims that you can use.

- Subject Claim Type —the default value for this field is sub . Enter one of the following values based on the scopes that you set:

- If you selected only OpenID in the Scopes field, this field must be set to sub .

- If you selected OpenID and email in the Scopes field, set this field to email .

- If you selected OpenID and profile in the Scopes field, set this field to a property available from the identity provider. These properties differ for each provider.

The identity provider sends an identity token to you, which contains the claims for your selected scopes. When you request only the openid scope, then sub is used as the claim type. It often represents a unique identifier for the user within your system

### Configure Okta

Once you configure the authentication provider, you'll need to assign it as a login method to your users. To complete the configuration in Relativity, navigate to the User and Group Management > Users tab. For complete steps on configuring an OpenID Connect login method, see OpenID Connect .

On this page

- Okta OpenID Connect

- Pre-requisites

- Configuring Okta OpenID Connect

- Authentication provider information

- Authentication provider settings

- Configure Okta


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

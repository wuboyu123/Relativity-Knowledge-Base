---
title: "Custodian Portal Authentication Provider"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Custodian_portal_authentication_provider.htm
collection: user
fetched_at: 2026-06-22T06:12:48+00:00
sha256: aff16b2c7bb892046db866fd7b62a375182b67cd046254ee49563c8910a67bee
---

Custodian Portal Authentication Provider Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Custodian Portal Authentication Provider

The Custodian Portal Authentication Provider is a connection between Relativity Legal Hold and an organization's single sign-on (SSO) provider that confirms the client, URL, and claim type before letting the custodian into the portal.

Legal Hold Portal SSO authentication only supports OpenID Connect protocol with Implicit Flow (SAML is not supported).

## Enabling Custodian Portal SSO

Enable SSO for the Custodian Portal by navigating to the Custodian Portal Authentication Provider tab. In the Authentication Provider section, fill out the fields. If you use Azure AD Provider, see Integrating Azure AD for Importing Custodians .

In the Custodian Portal Authentication Provider tab,

- Click Edit .

- Enter in information in the Authentication Provider fields. For more information, see Authentication Provider fields .

- Click Save .

### Authentication Provider fields

- Name —enter the name of the application.

- Client ID —enter the organization's security and compliance identifier.

- Authority URL —enter the authenticated provided by organization's SSO provider. If login successful, Relativity redirects to the next Redirect URL which is typically a Relativity URL and is the Custodian Portal.

- Redirect URL —enter the URL of the Custodian Portal that Relativity will redirect the user to after a successful login. This URL is typically a Relativity URL.

- Subject Claim Type —enter the piece of information that the SSO provider confirms the custodian by a field.

- Claim ID Verification Field —select the value to be used to match value coming in selected Subject Claim Type.

- Enabled —select Yes to enable or No to disable the Custodian Portal SSO.

## Securing the custodian portal link

When the Custodian Portal Authentication provider is enabled, custodians are presented with your organization’s SSO provider login after clicking the portal link in the received hold notice communication email. If the portal recognizes that the custodian has not been authenticated, they will be redirected to their organizations sign on page. Upon successful entry of their SSO credentials, they will be redirected to the custodian portal.

On this page

- Custodian Portal Authentication Provider

- Enabling Custodian Portal SSO

- Authentication Provider fields

- Securing the custodian portal link


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

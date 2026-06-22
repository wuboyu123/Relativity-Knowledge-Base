---
title: "The Relativity hybrid model"
url: https://help.relativity.com/Server2025/Content/Relativity_Unified_Experience/Relativity_hybrid_model.htm
collection: user
fetched_at: 2026-06-22T06:17:18+00:00
sha256: 7e40aaae20b1908096373c2346a9ff2bfc344a82b1530dd0962b38fccadac269
---

The Relativity hybrid model

# The Relativity hybrid model

With the introduction of RelativityOne, hybrid environments (combining cloud and on-premises instances) are becoming a common deployment scenario. The Relativity hybrid model provides a compelling alternative to on-premises hosting of cases.

Hybrid environment business scenarios:

- Your organization decided to start migrating older cases to RelativityOne

- Your firm’s IT department then no longer has to provision more hardware for new cases

- Simply migrate old cases to RelativityOne to free up infrastructure in your local data center

Relativity hybrid model allows you to start new cases in the RelativityOne instance with benefits such as:

- Avoiding the hassle of provisioning hardware to support those cases

- Viewing/accessing cases in a different instance

- Single sign on across instances (when using OpenID Connect protocol)

Despite the benefits of this hybrid model, RelativityOne is a separate instance with a separate user store and separate credentials. You must manage user credentials across two different systems - a task that can be time consuming and prone to errors.

The following topic provides a comparison of the options for configuring single sign-on (SSO) workflow in hybrid Relativity environments with Okta, Azure AD, and Active Directory Federation Services as identity providers. It also describes how the Workspace Portal and Relativity User and Group Synchronization applications can be used in combination with SSO to create a more seamless Relativity experience across your connected Relativity instances.

## Basic high-level workflow for setting up the hybrid model

We recommend the following workflow when setting up the Relativity hybrid model:

- Set up single sign-on (SSO) in both your primary and duplicate instance to allow you to navigate between these instances without having to use two sets of credentials. See Single sign-on workflow (SSO) overview .

- Set up and install Workspace Portal to your Relativity Server instances in order to view all your workspaces from a single tab that exists in both your primary Relativity instance and your satellite RelativityOne instances. See Workspace Portal .

- Set up the Relativity User and Group Synchronization application. See Relativity User and Group Synchronization .

The User and Group Synchronization applications is only available for RelativityOne and on premise environments running Relativity 9.5.224.9 and above.

Workspace Portal is only available for on premise environments running Relativity 9.5.224.9 and above.

## Single sign-on workflow (SSO)

Relativity and RelativityOne allow administrators to bridge the gap between on-premises and the cloud using single sign-on (SSO). Relativity supports two authentication protocols for single sign-on:

- OpenID Connect - use this protocol if you plan to connect multiple instances

- SAML 2.0 - this protocol is not compatible with connecting multiple instances

OpenID Connect is a modern authentication protocol that is gaining popularity. SAML2 is an older but widespread protocol that is common in the enterprise. With support for both protocols, Relativity can support a wide range of single sign-on providers. Single sign-on between Relativity and RelativityOne works by selecting an external identity provider that is shared between the two environments. Examples of identity providers include Azure Active Directory, Okta, Active Directory Federation Services, and even Google.

When single sign-on is configured, the Relativity login page displays a button for the external identity provider. The user attempting to log in simply clicks the button and is redirected to the identity provider’s login page. Upon successful login at the provider, the user is now authenticated and redirected back to Relativity.

Now suppose the user, who is authenticated to on-premises Relativity, wants to access RelativityOne. The user navigates to RelativityOne, perhaps via the Workspace Portal or Federated Instances menu. RelativityOne will automatically forward them to the identity provider login page. Because the user recently logged in, the provider will recognize the browser session and automatically authenticate the user. The user is finally redirected back to RelativityOne and can begin working. From the perspective of the user, she can access many environments while only having to log in once.

### Setting up single sign-on in Relativity

System admins must assign users at least one authentication method in order for users to log in.

To create and to assign methods, follow these steps.

- Enable authentication provider types. Authentication Provider Types are Relativity dynamic object (RDOs) types that permit authentication processes. You can only enable or disable each provider type. See Enable authentication provider types in the Authentication documentation. By default, each authentication provider type is enabled.

- Create authentication providers. Authentication Providers are instances of an authentication provider type. Each provider type that you plan to use requires creating an instance of that type. See Creating authentication providers in the authentication documentation for an overview of authentication types or see the following commonly used examples to create and configure your authentication provider with Relativity.

- Configuring Okta as a SAML 2.0 identity provider

- Configuring Microsoft Azure AD as an OpenID Connect identity provider

- Configuring Active Directory Federation Services as a SAML 2.0 identity provider

- Assign a login method to individual users. You assign an authentication method to each user for them to log in with. Each user must have at least one authentication method in order for them to log in but you may assign multiple methods. See Managing user authentication methods .

To utilize Workspace Portal and User and Group Synchronization applications fully, you must configure SSO authentication for users in both your primary and duplicate instance.

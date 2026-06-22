---
title: "Identity (authentication and user accounts)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/Identity.htm
collection: developer
fetched_at: 2026-06-22T06:22:46+00:00
sha256: f0ad220c7544b5d05e090b5ccc5aaf4c499b3bb93e483898c1883d9ec453126e
---

Identity (authentication and user accounts)

# Identity (authentication and user accounts)

This page aims to collect and centralize any useful information on the Identity business domain which deals with authentication and user accounts.

Relativity uses several industry-standard technologies, enabling versatile authentication options. It supports local (such as password related) or external (such as smart cards, or external identification providers) authentication methods. You can add and enable each type individually, as well as assigning at least one, and in some instances multiple methods, for each user.

Update your IIS settings by changing the Web API to Anonymous Authentication rather than Windows Authentication . You must update this setting in order to publish documents to a workspace or process data to Data Grid.

## General concepts

### Authentication provider types and login profiles

#### Authentication provider types

These represent the different protocols for authenticating against Relativity, for example, Password, Integrated Authentication, and OpenID Connect. Using the API you can inspect enabled protocols for a particular environment. You can also enable or disable specific protocols. Disabling an authentication provider type completely disables that login workflow for the entire Relativity instance .

#### Login profiles

The Login Profile Manager is use to configure Relativity's authentication profile and user login profiles.

- Authentication profile. The authentication profile is a collection of authentication providers which user login methods are created from. For example, the authentication profile is where you configure Password settings such as min and max password length. It also is where you define external identity providers that use the OpenID Connect and SAML protocols. How you configure your authentication profile determines how the look and behavior of the Relativity login page.

- Login profile. Whereas the authentication profile applies to the environment, each user has a Login Profile that defines the user-specific options for various providers on the authentication profile. Each entry in the user's Login Profile corresponds to a matching entry in the environment's authentication profile. Each user automatically has a login profile upon creation, and you can not delete that profile.

#### Working with provider types and login profiles

This section outlines the steps required to configure authentication in your Relativity environment.

Step 1: Configure authentication provider types

The API allows you to enable or disable authentication protocols on an environment level. As a best practice, you should only enable the protocols that you actually want to use in the environment. Relativity currently ships with all Provider Types enabled by default, and you can disable the ones you do not want to use.

See Authentication provider type (.NET) for additional information and code samples.

In a future release we expect to ship with all authentication provider types disabled by default except for Password. You should write your update logic to explicitly enable or disable Provider Types based on your individual requirements.

Step 2: Configure the global profile

The Global Profile defines the environment-wide configuration options for each Authentication Provider (that is, Password, RSA, OpenID Connect). Some Providers have many options (such as Password) whereas some have just a few. The Global Profile has properties for each of the Provider Types. See Login Profile Manager (.NET) for additional information and code samples.

In the current implementation of the authentication API, there is a single global authentication profile. This single entity is called the Global Profile. Admins currently do not have the ability to create multiple profiles.

If you change any OpenID Connect or SAML 2.0 Providers on the authentication profile, you must perform an IIS reset on every web server in your environment. An upcoming release will correct this so that authentication profile dynamically updates on each server.

Step 3: Configure the login profile

See Login Profile Manager (.NET) for additional information and code samples.

### Client manager

In Relativity, a client is a company or organization, which is associated with users, matters, groups, and workspaces.

The Client Manager API exposes methods that provide the following functionality:

- CRUD operations on clients.

- Helper methods for retrieving lists of available groups, matters, users, and statuses.

- Methods for creating, submitting, and retrying client domain activation keys.

### Federated instance manager

Federated instances provide a way for administrators to manage a list of user displayed links to other Relativity instances. In the Relativity UI, links to federated instances appear in the User dropdown.

Federated instances in combination with an SSO configurations can enable users to seamlessly switch between multiple Relativity instances without the need to reenter their credentials.

### Group manager

The Group Manager service exposes the API to create, read, update, and delete groups. Sample use cases for Group Manager API include:

- creating a new group;

- adding users to a group;

- removing users from a group.

### Permissions manager

In Relativity, you can manage varying levels of security for users, system admins, and individual objects, such as views, tabs, and fields, across your instance of Relativity and in each workspace. You can also define custom permissions for Relativity Dynamic Objects (RDOs).

The Permissions manager API supports a set of operations for assigning system-defined permissions on the admin, workspace, and item level. You can manipulate either arbitrary sets of individual permissions, or entire admin, workspace, or item permission sets. Note that the logic for working with entire permission sets closely follows the logic of the Relativity permissions UI.

While you can't modify the system-defined permissions, you can programmatically create, update, and delete custom permissions for RDOs. You can perform read and query operations on both system-defined permissions and custom permissions. All operations on permissions are performed asynchronously.

### User manager

Users are individuals who have access to the Relativity environment. For general information, see Users on the Relativity Documentation site. The User Manager API exposes multiple operations that you can use to programmatically manage users in your Relativity environment. It includes the following features:

- Supports create, read, update, and delete operations on users.

- Supports read and update operations on the settings of the current users.

- Provides helper methods used to retrieve the available user types.

- Retrieval of all users from a workspace or admin-level context.

Sample use cases

- Developing a custom tool to import users in Relativity.

- Updating properties like the name or the email of the logged user or any other user in Relativity.

- Retrieve user information for display in a view for a custom application

## Current Identity API content

#### .NET API

- Authentication provider type (.NET)

- Client Manager (.NET)

- Federated Instance Manager (.NET)

- Group Manager (.NET)

- Login Profile Manager (.NET)

- OAuth2 Client Manager (.NET)

- Permission Manager (.NET)

- User Manager (.NET)

#### REST services

- Authentication provider type (REST)

- Client Manager (REST)

- Federated Instance Manager (REST)

- Group Manager (REST)

- Login Profile Manager (REST)

- OAuth2 Client Manager (REST)

- Permission Manager (REST)

- User Manager (REST)

## Version History

v5000.0.1

##### Release Notes

- Initial version for Server 2024 release

##### Supported Relativity Version Range

Lowest Version Highest Version

Server 2024 Server 2025

v2.6.2

##### Release Notes

- Initial version for Server 2023 release

##### Supported Relativity Version Range

Lowest Version Highest Version

Server 2023 Server 2024

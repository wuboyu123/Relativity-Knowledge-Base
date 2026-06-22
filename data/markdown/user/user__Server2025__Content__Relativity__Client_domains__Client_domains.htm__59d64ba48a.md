---
title: "Client domains"
url: https://help.relativity.com/Server2025/Content/Relativity/Client_domains/Client_domains.htm
collection: user
fetched_at: 2026-06-22T06:04:30+00:00
sha256: de11d33e0c1c4ce5946055ee3951c29fd47389c43ca530680a4c14c5043d80d3
---

Client domains

# Client domains

The client domains feature enables Relativity authorized partners to deliver more powerful managed service offerings for enterprise customers in a single Relativity instance by providing an easier way to securely isolate users, workspaces, groups, resource pools, and matters by client.

Using client domains, Relativity system admins can empower a user group that is not part of the System Administrator group (client domain admins) to perform common administrative tasks within their own client domain while limiting their visibility into the Relativity environment as a whole. The client domain admins can customize the permission settings to various objects according to their preferences within their own domain, but cannot access any permissions outside of that. This resource isolation functionality grants your enterprise clients more administrative control over their own portions of the environment while preventing back-end visibility and unauthorized changes to your Relativity instance as a whole.

Client Domains are targeted for the above use case only and it is important to consider all the limitations outlined in Client domain limitations and considerations .

Implementing client domains requires an additional license from Relativity ODA LLC. Each client domain license is unique, and client domains can have different terms encoded on their license keys. The license for a client domain is unrelated to any other license for Relativity (e.g., number of seats). Client domain licenses are not transferable from one client to another.

Client domains (formerly multi-tenancy) requires Relativity version 9.1 or later.

See the following related pages:

- Adding workspaces to a client domain

- Adding or removing users from a client domain

- Adding or removing groups from a client domain

- Adding or removing matters from a client domain

- Adding or removing resource pools from a client domain

## Considerations before enabling client domains

Consider the following before enabling client domains:

- If you enable client domains on a client:

- You can't disable it on that client later.

- You can't edit the name of the client, but you can edit the Client ID number.

- You can’t delete the client.

- Enabling client domains on a client involves generating a client domain request and then applying an activation key. By enabling it, you ensure that any content or other Relativity components associated with this client are visible only to a select group of users.

- Permissions - the root object of a client domain is the client object in the administrative workspace. By default, groups associated with a given client only have permission to perform actions on users, groups, matters, and workspaces associated with that client, unless a system administrator has given special permission across client domain boundaries. Additionally, each client domain has an associated group known as the client administrator group. By default, members of this group can create administrative objects (users, groups, matters, and workspaces) associated with the client. This group does not have permission to interact with or view objects of these types associated with other clients.

- You can add objects to a client domain after the client has client domains enabled, but it's best to verify that all objects you want to isolate within the client domain are child objects of the client. See Adding or removing objects from a client domain for more information.

- If you have client domains enabled, we recommend locking down System Administrator access to only those absolutely necessary.

You must set the ClientDomainFeatureAvailable instance setting value to True to view and edit client domain settings.

## Enabling client domains on a client

- The following things occur automatically after client domains are enabled:

- The system creates a new Everyone - [Client's Name] group and adds that group to the client domain. Only users whose client field is set to the client domain are included in the client domain everyone group. The system also removes those users from the default Relativity Everyone group. A system admin can add any users to any group regardless of client domain status.

The Everyone - [Client's Name] group should not be assigned as the workspace administrator group for a given workspace that is part of a Client Domain.

- The system creates a unique copy of all resource pools associated with any workspaces under the client domain.

Permissions assigned to groups override client domain isolation. If a non-client domain group has permissions to see a client domain's workspace or users, then those non-client domain users in the non-client domain group can still access client domain items. Enabling client domains does not change previously configured item level security settings applied to any objects within the client domain.

- The system creates a client domain admin group that permits its members to perform admin operations within the client domain.

- The Billing statistics - case rollup and Billing statistics - users reports include columns called Client Domain Name and Client Domain Artifact ID. These columns display client name and artifact ID when you enable client domains for a client.

After enabling client domains, system administrators needing to make group or permission changes should be extra cautious and thoroughly investigate the potential impact to client domain separation before implementing any new group/permission changes.

### Generating a client domain request

To enable client domain on a client, you first generate a client domain request key in Relativity.

- Create a new client or click the name of a client on the Client tab. The details view of the client appears.

- Click Create Client Domain Request Key and then the Client Domain Request Key window appears.

- Copy the Client Domain Request Key text and paste it into an email to Customer Support .

- Close the Client Domain Request Key window. See Applying the activation key .

### Applying the activation key

After you receive an activation key from us, you enable client domains by applying it to the client.

- Navigate to the Client tab.

- Click the name of a client associated with the client domain request.

You must select the client that you originally used to generate the request key. If you attempt to apply the activation key to a different client, Relativity displays an error message.

- Click Submit Client Domain Activation Key and then the Apply Client Domain Activation Key window appears.

- Copy the client domain activation key received in the email message that Customer Support sent. Paste it into Client Domain Key field in the Apply Client Domain Activation Key window.

- Click Apply .

If Relativity displays an error message, verify that you copied the activation key correctly. Contact Customer Support if you have any questions about applying your activation key.

- Verify that the Client Domain Status field in the Client Information section displays the word Client Domain.

Once client domains functionality is enabled for the client, you must assign a client domain admin .

## Client domain admins

Client domain admins are essentially workspace admins for workspaces within the client domain. Any limitations are based on the permissions you set for the user group in Relativity that the client domain admin belongs to. The administrative actions available to client domain admins are only in the scope of the client domain. For example, client domain admins can edit or delete users belonging to that client domain, but they cannot do the same action for users part of a different client domain or users not associated with a client domain.

Client domain admins can do things like:

- Modify, add, and remove groups, users, and workspaces.

- Create all workspace and admin objects across the Relativity Framework, such as matters, fields, layouts, choices, and views.

- Start jobs like processing, imaging, and productions.

- Tenants have access to the full complement of the Processing features, including inventory, discovery, publish, and errors.

- Import data.

### Client domain admin considerations

Consider the following when assigning a client domain admin:

-

We recommend users review Client Domain, and other Administrative type permissions for item-level security based on the workflow within your instance. Relativity recommends applying item-level security to all views for the following types within the Admin landing page, removing access from all non-administrative users:

-

Authentication Provider

Client Domain specific views can be used and configured to enable Client Domain administrators to configure and view their own users more easily. Ensure you have properly reviewed and tested all relevant permissions before doing so.

-

Authentication Provider Type

-

Code

-

Errors

-

Resource Pools

-

Resource Servers

- Client domain admins cannot perform tasks that are exclusive to Relativity System Administrators.

-

Client domain admins cannot add themselves to any group (even groups tied to their own client domain). Only a System Administrator can change a user’s group memberships.

- Client domain admins do not have access to Mass Operations on the Users tab.

- Permissions assigned to groups override client domain isolation . If a non-client domain group has permissions to see a client domain's workspace or users, then those non-client domain users in the non-client domain group can still access client domain items. Enabling client domains does not change previously configured item level security settings applied to any objects within the client domain.

- Transferring data via Integration Points uses a standard Relativity permissions check. If a client domain admin has access to a source and destination workspace and permissions for importing / exporting data, they can transfer data to the workspace even if it’s outside the client domain.

- Relativity displays a warning message when a system admin attempts to edit or copy permissions for any group in a client domain. This warning makes the sys admin aware that modifying permissions may have significant consequences. For example, changing permissions may allow client domain users to modify items outside their tenancy. The system admin can click Manage Permissions to proceed with the update or Cancel to exit the pop-up window.

- If a system admin assigns additional permissions for other Admin objects to a client domain admin (e.g., Queues), the client domain admin may be able to see information for other client domains.

- System Administrators should note the following behavior to avoid accidentally granting users access to data outside their domain: When you add a user that is already a member of a domain admin group to another group that has the Relativity Script system permission, that user will gain access to all users and groups in the Relativity instance. Once that user is removed from the new group, access will again be limited to users and groups associated with their own client.

- If you use the Relativity User Import Application to import a Client Domain Admin, the application adds that new user to the Everyone group by default, which will then break the Client Domain security in your Relativity instance. To resolve this issue, remove the user from the Everyone group and place it into the client-specific Everyone group by switching the user to any other client that is not linked to a domain and then back to the domain client.

- You can grant workspace admins within the client domain permission to edit security settings for groups within the client domain, but they can't edit permissions on groups outside of the client domain.

The following table provides a breakdown of the default instance permissions for a client domain admin:

Group Permission Type

Client Domain Admin for <Client> View Admin Repository Admin Operations

Client Domain Admin for <Client> Add Matter Add

Client Domain Admin for <Client> Add User Add

Client Domain Admin for <Client> View View View

Client Domain Admin for <Client> View Choice View

Client Domain Admin for <Client> Add Group Add

Client Domain Admin for <Client> Add Workspace Add

Client Domain Admin for <Client> View Error View

Client Domain Admin for <Client> Add Error Add

Client Domain Admin for <Client> Edit Error Edit

Client Domain Admin for <Client> View Relativity Script View

Client Domain Admin for <Client> View Server View

Client Domain Admin for <Client> View Tab Type View

Client Domain Admin for <Client> Authentication Provider* View

Client Domain Admin for <Client> Login Method View, Edit, Delete, Add

* The View Authentication Provider permission is required for Client Domain admins to add login methods to their users. Because the Authentication Provider object is not client-bound, it is highly recommended that you apply item-level security to ensure that Client Domain admins can see only the necessary Authentication Providers.

### Assigning a client domain admin

Once you enable client domains on a client, you must assign a client domain admin.

Use the following steps to assign a client domain admin.

- Navigate to the Groups tab.

- Select the client domain admin group.

- Click the Add button in the Users section.

- Select the user you want to be the client domain admin.

- Click OK .

A system admin can make any user a client domain admin by adding them to the client domain admin group. You can tailor the permission settings of a client domain admin group the same way you manage permissions for all other groups. See Setting instance permissions for more information. See Client domain admin considerations for more information on default permissions.

## Client domain limitations and considerations

The following items are features and operations that are not available when using client domains (if a feature or operation isn't listed, it is available when using client domains):

- Multi-tiered client domains - an enabled Client Domain cannot have their own sub/child client domains

- Unique logos or URLs per client domain

- Self-provisioning / enabling of client domains - requires request to Support

The following items are features and operations that are have limitations in client domains or can only be used or performed by top-level system admins or a Relativity staff resource.

If a feature, capability, or operation isn't listed, then there are no limitations on them when using client domains. For example, Relativity Legal Hold isn't listed and has full functionality when operating client domains.

Item

Limitation

Client domain admin

System admin

Client domains setup and configuration

SSO setup

A system admin can configure client domain user accounts to use an SSO provider provided that the provider is configured correctly.

No access

Yes

Client domain setup

-

Cannot be setup on a Client record that already has a workspace association.

- Cannot disable client domain on client once enabled.

- Cannot rename client once enabled.

- Cannot delete client once enabled.

No access

No access

Instance settings

Not available per client domain.

No access

No access

Feature access

ARM

ARM is not available to Client Domain Admins.

ARM archives can be restored directly to a client domain.

No access

Has access

Creating / editing Relativity scripts

Not available to Client Domain Admin.

- Admins can run scripts that have already been added to the workspace from the library.

- Admin scripts are not supposed to be run by client domain admins. These scripts should not be part of the template workspace.

No access

Has access

Migrate Migrate (similar to ARM) is supported for client domains, but migrations can only be performed by a Relativity System Admin. Migrate cannot be used by a client domain administrator due to security restrictions. N/A Has access

Relativity applications

- Client Domain Admin is not able to install or upgrade Relativity applications.

- No support of multiple app versions.

- Case Dynamics, Case Metrics and Transcripts applications have been tested and work without issue in environments with client domains.

- Most applications are typically not built or tested with client domain structure or concerns in mind.

No access

Has access

SFTP for Data Transfer SFTP is not available for client domain users. No access Has access

Tabs We do not recommend entering sensitive data in a tab name because it cannot be secured with client domains. Has access Has access

User and Group Synchronization application The User and Group Synchronization application is not compatible with Client Domains. No access Has access

View, edit or cancel jobs / queues

Jobs / queue status not available to Client Domain Admins.

Since client domain admins can't see or modify jobs in the queue, a system admin may need to inform client domain admins of the status of jobs they've start or if the job is still waiting in the queue.

No access

Has access

Views We do not recommend entering sensitive data in a view name because it cannot be secured with client domains. Has access Has access

## Adding or removing objects from a client domain

Any workspaces, users, groups, matters, or resource pools associated with a client domain during creation become automatically governed by that client's domain settings. When you move an object into a client domain, you're making it a child object of the client domain.

You can remove a Resource Pool and its associated servers if no other dependencies use them. Before removing these resources, verify that no active dependencies or references exist in the system.

The tenant admin group is tightly linked to the Client Domain. While you can revoke access or remove members from the group, Relativity does not support deleting the group.

See the following pages for more information on moving objects to and from client domains:

- Workspaces

- Adding or removing users from a client domain

- Adding or removing groups from a client domain

- Adding or removing matters from a client domain

- Adding or removing resource pools from a client domain

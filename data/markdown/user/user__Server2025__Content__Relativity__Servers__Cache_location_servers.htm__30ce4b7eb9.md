---
title: "Cache location servers"
url: https://help.relativity.com/Server2025/Content/Relativity/Servers/Cache_location_servers.htm
collection: user
fetched_at: 2026-06-22T06:03:37+00:00
sha256: 7f5b348327d7f57f5ac1c768f0d30e7aca0e89946265a21d62badc0df6a87663
---

Cache location servers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Cache location servers

Cache location servers temporarily store natives, images, productions, and other file types the viewer uses. These servers also provide you with the option to manually clear the cache locations in your environment during off-hours, which mitigates any difficulties your reviewers experience as they display documents in the viewer. It also helps to enhance the review experience.

## Adding a cache location server

Whether you've upgraded or installed Relativity for the first time, you can manually add a cache location server through the following steps:

For more information on the cache location parameter of the Relativity installer, see Primary SQL Server installation .

To add a cache location server:

- Click the Servers tab.

- Click New Resource Server .

- Complete the fields on the Resource Server Information layout. See Fields .

- Click Save .

After you save the new cache location server, Relativity updates its layout to include the Cache Details console on the right side, which provides information about the cache and the option for clearing it manually. See Cache location servers .

## Fields

The fields for a cache location server include:

- Name - the name of a cache location server.

- Type - select Cache Location Server . This option updates the layout so it appears only the fields required for adding a cache location server.

- Visible In Dropdown - select Yes or No in the drop-down to display the server as an available item within the drop-down list when creating a new workspace.

- UNC Path - enter the file path for the location where you want to store your cache for natives, images, productions, and other files types that the viewer uses. Relativity displays an error message and prevents you from creating the server if the UNC path is invalid. Additionally, don't enter a URL already in use by an existing cache location server.

## Editing a cache location server

You may need to edit a cache location server. For example, your workspace becomes too large and you need to move it to another location, which would then require you to update the UNC path of your cache location server.

To edit a cache location server:

- Click the Servers tab.

- Locate the server you need to edit and click the Edit link next to its name.

- Edit the UNC Path field on the layout for the cache location server. This is the only editable field on the layout.

-

If applicable, edit the Visible In Dropdown drop-down on the layout.

- Click Save .

## Adding a cache location to a resource pool

When you install or upgrade to Server 2025 , the installer automatically creates a new cache location server for each file repository currently used in your environment and updates the resource pool that the workspace uses with that cache location server.

If you manually add an additional cache location server to your environment, you need to add that new server to a resource pool. For more information, see Adding resources to a pool .

## Clearing the cache

You are not required to manually clear cache locations. Relativity provides the Conversion Cache Manager agent, which automatically clears the cache locations in your environment during off hours. This is useful because when the cache is full, the viewer can only display documents that are already cached.

The details view of a cache location server includes the Cache Details console as illustrated in the following screen shot:

The Cache Details console displays the following information:

- Capacity - indicates the total amount of space on the drive or partition where the cache location server resides.

- Free Space and % Free - indicates the amount of available space on the drive or partition in gigabytes and by percentage respectively.

## Resolving cache alerts

Relativity displays an alert when the cache size is greater than the upper threshold listed in the CacheLocationUpperThreshold instance setting. You can resolve this alert by completing one of the following tasks:

- Complete the steps in Cache location servers . The alert disappears when the cache size falls below the upper threshold.

- Wait for the Conversion Cache Manager agent to clear the cache. Depending on how you have set your instances settings, your cache may have met the value in the CacheLocationUpperThreshold instance setting value, but your drive may still have space on it.

- Increase the space on the hard drive where the server resides.

- Increase the value for the CacheLocationUpperThreshold instance setting value.

- Add a new cache location server to the hard drive with additional space. See Adding a cache location server .

On this page

- Cache location servers

- Adding a cache location server

- Fields

- Editing a cache location server

- Adding a cache location to a resource pool

- Clearing the cache

- Resolving cache alerts


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

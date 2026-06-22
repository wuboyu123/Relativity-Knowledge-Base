---
title: "Fileshare"
url: https://help.relativity.com/Server2025/Content/Relativity/Servers/Fileshare.htm
collection: user
fetched_at: 2026-06-22T06:16:41+00:00
sha256: 4ac32c1efb10c62df094c7752c28c42c6e8527db1ef4be31106a8084c178ca3e
---

Fileshare

# Fileshare

File share choices are file share resource server objects. Upon upgrade, all file share choices are mapped to resource servers.

This page describes how to create a new file share.

## Adding a File share

To manually add a new file share server to your environment:

- Click your name in the upper right corner of Relativity, and then click Home .

- Select the Servers tab.

- Click New Resource Server .

- Complete the fields on the form. See Fields .

- Click Save .

Relativity now attempts to retrieve information from the server. If this call fails, you receive an error. To save your changes, ensure that the web server can reach the server.

## Fields

The file share server fields are:

- Name - the name of the fileshare.

- Type - select Fileshare .

- UNC Path - enter the UNC path of the server. Relativity displays an error message and prevents you from creating the server if the UNC path is invalid. Additionally, don't enter a URL already in use by an existing cache location server.

-

Visible In Dropdown - select Yes or No in the drop-down to display the server as an available item within the drop-down list when creating a new workspace.

## Editing a File share

To edit certain settings for an existing file share server, follow these steps:

- Click your name in the upper right corner of Relativity, and click Home .

- Select the Servers tab.

- Click the Edit link next to the server's name to display the server form.

- Update the following fields as necessary:

- Name - enter a name for the fileshare.

You can't modify the Type assigned to a server.

- UNC Path - enter the UNC path of the server. Relativity displays an error message and prevents you from creating the server if the UNC path is invalid. Additionally, don't enter a URL already in use by an existing cache location server.

- Visible In Dropdown - select yes/no in the drop-down to display the resource server as an available item within the drop-down list when creating a new workspace.

- Click Save .

When you click save, Relativity attempts to retrieve information from the server. If this call fails, you'll receive an error message. To save your changes, ensure that the web server can reach the server.

## Adding a File share to a resource pool

When you add a files hare to your environment, you also need to add that file share to the resource pool referenced by the workspace. For more information, see Adding resources to a pool .

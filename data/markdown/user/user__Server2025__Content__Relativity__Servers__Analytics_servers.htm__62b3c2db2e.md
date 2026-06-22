---
title: "Analytics servers"
url: https://help.relativity.com/Server2025/Content/Relativity/Servers/Analytics_servers.htm
collection: user
fetched_at: 2026-06-22T06:04:24+00:00
sha256: 85e21b05621172a260896791abb32eab6eac283077d2b56dd976af562bdacf63
---

Analytics servers

# Analytics servers

An Analytics server is integral to performing the work of building and populating an Analytics index, which allows you to perform clustering, concept searching, and categorization. This server is also integral to Assisted Review, in that an Analytics index is required to create an Assisted Review project. This server also facilitates Structured Analytics operations, including email threading and the identification of textual near duplicates, language, and repeated content.

## Adding an Analytics server

To manually add new Analytics server to your environment:

- Click your name in the upper right corner of Relativity, and then click Home .

- Select the Servers tab.

- Click New Resource Server .

- Complete the fields on the form. See Fields .

- Click Save .

Relativity now attempts to retrieve information from the server. If this call fails, you receive an error. To save your changes, ensure that the web server can reach the server.

## Fields

The Analytics server fields are:

- Name - the name of the Analytics server.

- Type - select Analytics Server .

- Analytics operations - select which Analytics operations can run on the Analytics server. This field defaults to permitting Analytics Indexing and Structured Data Analytics operations. See Analytics for more information This field only appears when the server type is Analytics.

- URL - enter the URL of the server. An Analytics server URL should be in the following format: https://<servername.FQDN>:8443/

- REST API username - the username Relativity uses to authenticate the Analytics server's REST API. This value must match the username specified during installation of the Analytics server.

- REST API password - the password Relativity uses to authenticate the Analytics server’s REST API. This value must match the password specified during installation of the Analytics server. This field is required for Analytics servers on which a password as not yet been provided in Relativity. This field is optional if you’re editing an Analytics server that already has a password set. If you need to change the REST API password, you need to run the Analytics server installer and enter the new password. You must then enter the new password here. For information on installing the Analytics server, see Upgrading or installing your Analytics server .

The REST API password entered must be 20 characters or less.

- Status - select Active or Inactive . Relativity automatically updates this value to Inactive when the respective agent for an Analytics server exceeds the maximum connection attempts set in the Relativity Instance setting table. After this update is complete, you no longer receive email notifications indicating that the connection has failed. This change doesn’t affect the server functionality, and you can reset the value as necessary.

When you upgrade Relativity, some servers don’t list the updated version number until you start them. This means that if a server still lists an old version number after you’ve already upgraded, you need to click the Edit link next to the server name and change its Status field to Active.

- Version - a read-only field that Relativity automatically updates when you click Save . It also updates on a nightly basis to reflect any version changes. You should run the same version of Analytics on all Analytics servers that you add.

- Maximum connectors - the maximum number of connections allowed between the Analytics server and SQL for each index that uses this server. The default value is 4.

- Maximum total connectors - the maximum number of connections allowed between the Analytics server and SQL across all indexes using this server. The default value is 50.

Connectors pass data from the Analytics server to SQL during index population. Connectors have no impact on index build, enabling queries, or search performance. For more information, see Connectors functionality .

## Editing an Analytics server

To edit certain settings for an existing Analytics server, follow these steps:

- Click your name in the upper right corner of Relativity, and click Home .

- Select the Servers tab.

- Click the Edit link next to the server's name to display the server form.

- Update the following fields as necessary:

- Name - enter a name for the Analytics or worker manager server.

You can't modify the Type or URL assigned to a server.

- Analytics operations - select which Analytics operations can run on the Analytics server. This field defaults to permitting Analytics Indexing and Structured Data Analytics operations. See Analytics for more information This field only appears when the server type is Analytics.

- REST API username - the username Relativity uses to authenticate the Analytics server's REST API. This value must match the username specified during installation of the Analytics server.

- REST API password - the password Relativity uses to authenticate the Analytics server’s REST API. This value must match the password specified during installation of the Analytics server. This field is required for Analytics servers on which a password as not yet been provided in Relativity. This field is optional if you’re editing an Analytics server that already has a password set. If you need to change the REST API password, you need to run the Analytics server installer and enter the new password. You must then enter the new password here.

The REST API password entered must be 20 characters or less.

- Status - select Active or Inactive . Relativity automatically updates this value to Inactive when the respective agent for an Analytics or worker manager server exceeds the maximum connection attempts set in the Relativity Instance setting table. After this update is made, you'll no longer receive email notifications indicating that the connection has failed. This change doesn’t affect the server functionality, and you can reset the value as necessary.

- Maximum connectors - the maximum number of connections allowed between the Analytics server and SQL for each index that uses this server. The default value is 4.

- Maximum total connectors - the maximum number of connections allowed between the Analytics server and SQL across all indexes using this server. The default value is 50.

Connectors pass data from the Analytics server to SQL during index population. Connectors have no impact on index build, enabling queries, or search performance. For more information, see Connectors functionality .

- Click Save .

When you click save, Relativity attempts to retrieve information from the server. If this call fails, you'll receive an error message. To save your changes, ensure that the web server can reach the server.

## Adding an Analytics server to a resource pool

When you add an Analytics server to your environment, you also need to add that server to the resource pool referenced by the workspace so that you can select it when creating Analytics indexes. For more information, see Adding resources to a pool .

## Connectors functionality

Connectors increase performance when populating the index by allowing the Analytics server and the SQL Server to communicate directly with each other and not having to go through the agent to send and receive calls. This direct line between servers reduces the number of entities involved in index population and leads to faster population times.

Analytics index population involves the following:

- The Content Analyst Index Manager Agent queries SQL to see if it should populate any indexes.

- If there is an index to populate, the agent creates connectors, not exceeding the number of connectors specified on the Analytics server.

- The connectors allow the Analytics server to query the SQL database directly.

- The agent monitors the progress and reports back the status of the population.

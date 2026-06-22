---
title: "Configuring the worker manager server"
url: https://help.relativity.com/Server2025/Content/Relativity/Servers/Worker_Manager_server.htm
collection: user
fetched_at: 2026-06-22T06:04:25+00:00
sha256: 21bd9fe3695e6f2cb01e36a23d1b134721440d213b6592124a1e3fb16b867e09
---

Configuring the worker manager server

# Configuring the worker manager server

The worker manager server uses workers to perform imaging, and all phases of processing, including inventory, discovery, and publish. You can configure the default queue priorities for your entire environment on the Worker Manager Server layout. If you are not licensed for processing, then the worker manager server only handles save as PDF and imaging.

Even though Invariant is required for Relativity 9+, you are not required to purchase a Processing license unless you are using Processing.

The following graphic depicts the connections between your resource pool, worker manager server, and workers. This is meant for reference purposes only.

See this related page:

- Worker manager server installation

## Resource server information

Use the following steps to access the worker server manager settings:

- Navigate to the Servers sub-tab.

- Click the name of the worker manager server in the list of servers.

- If you want to edit the fields, click Edit , make the desired changes, and click Save .

The following fields are visible on a worker manager server:

- Name —give the worker manager server a name that appears on the Servers tab.

- Type —this is a read only field that displays the server's primary function.

- Server Name —the name of the server where the Invariant Queue Manager is installed. This value should include a fully qualified domain if the server is on a domain. For example, pt-func-sql02.testing.corp .

This value does not require a net.tcp reference that includes a port number. It also does not require a domain unless the worker manager server and Relativity are on different domain.

- Is Default —if checked, this worker manager server is the default worker manager server added to any resource pool upon creation and any resource pool that does not currently have a worker manager server. On upgrade, the default worker manager server automatically associates with all existing resource pools. If unchecked, you must manually add the worker manager server to each resource pool.

Every resource pool should have a worker manager server linked to it. If a resource pool does not have a worker manager server linked to it, any workspace linked to that resource pool is unable to perform imaging and processing.

- Status —when a worker manager server is added to Relativity, the server manager agent attempts to make a connection and get information about workers. The Status field is automatically set to Active if a server is online. Relativity automatically updates this value to Inactive when the server manager agent exceeds the maximum connection attempts set by the ServerManagerRetries instance setting.

- Temporary directory —a UNC share path used as a temporary location for storing files during Relativity processes.

- This field is available for all server types except Analytics servers. Use the format \\<server name>\ <shared folder name> for the path. Relativity validates the path you enter.

- If the path format is invalid, you receive an error message when trying to save.

- If a permission error occurs, Relativity writes a message to the Errors tab.

- A temp directory acts as an override of the default behavior, specifically the BCP path. It is not necessary for all servers.

- Version —this read only field displays the version of Invariant installed on the worker manager server.

Use the Priorities tab to specify which jobs the worker manager server gives precedence to when managing jobs. Only one job runs at a time, the lower numbered job runs first and the higher numbered job runs last.

- Inventory —holds the prioritization for inventory jobs.

- Discovery —holds the prioritization for discovery jobs.

- Publish —holds the prioritization for publish jobs.

- Imaging —holds the priority for imaging jobs, both native and basic.

- Image on the Fly —holds the priority for Image on the fly jobs.

- Save As PDF —holds the priority for Save as PDF jobs.

- Mass Imaging/Imaging Set —holds the priority of a mass imaging job or imaging set

- Single Save As PDF —holds the priority for when you execute Save as PDF on a single document.

- Mass PDF — holds the priority for all Mass PDF jobs. These occur when you select a group of documents from the Documents tab and then select the Save As PDF option from the mass operations drop-down menu.

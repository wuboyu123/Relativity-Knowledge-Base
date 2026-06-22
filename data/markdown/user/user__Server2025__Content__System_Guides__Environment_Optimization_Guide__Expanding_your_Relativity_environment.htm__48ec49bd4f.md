---
title: "Expanding your Relativity environment"
url: https://help.relativity.com/Server2025/Content/System_Guides/Environment_Optimization_Guide/Expanding_your_Relativity_environment.htm
collection: user
fetched_at: 2026-06-22T06:18:01+00:00
sha256: 4e5136910cba2871b51026f99c46cc5c5dbe0ddb27563e2e9efda774eb60669e
---

Expanding your Relativity environment Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Expanding your Relativity environment

Use the following additional features and tools to expand your Relativity environment.

## Agents

Agents are process managers that run in the background of Relativity. Use the Agents tab to see which agents are running in your environment and the status of those agents. Adding multiple instances of certain agents can increase the speed of imaging, productions, OCR jobs, and index builds.

In general, use one processor core and 1 GB of memory for each additional agent. You can house these agents on multiple servers in the Relativity environment. For example, you may want to incorporate another agent server to increase the speed of productions. Allocate eight processor cores and 8 GB of memory to house eight additional Branding Manager agents.

System administrators can adjust agent configurations through the Relativity interface. It's important for system admins to understand agent best practices before adjusting agent configurations. For more information, see the Agents .

## Analytics servers

Relativity supports multiple Analytics servers in order to allow jobs to run concurrently and to allocate resources among different workspaces.

When implementing a multi-server analytics environment, take the following considerations into account:

- What is the average dataset for analytics?

- What is the largest potential dataset for analytics?

- What type of jobs will be running on the server?

While the minimum system requirements for analytics are specified as 32 GB of RAM, this server has limitations. A server of this size could not build an index with more than five million training documents. Depending on the number of indexes enabled on the server, the limitation may be even smaller than this.

If heavy structured analytics usage is anticipated, it is highly recommended to have an analytics server dedicated to structured analytics.

Never install any Relativity agents on an Analytics server.

To implement this configuration, install the Analytics component on an additional server. For instructions on installing Analytics, see Upgrading or installing Analytics . After installing the Analytics component to the server, add the server to the Servers tab at Home. For instructions on adding analytic servers, see Adding an Analytics server . When adding the server in Relativity, select the analytics server type:

- structure analytics

- conceptual analytics indexing

## Dedicated web servers

You can install additional web servers for specific Relativity roles, such as Relativity Desktop Client (RDC) imports or exports.

### Relativity Desktop Client import or export

You can improve local data import and export performance by using a web server separate from the primary review web server. Doing so also reduces the load on the primary review web server.

To do this, install the web components of Relativity onto another web server that meets our web server requirement specifications. Next, update the WebService URL in the settings of the Relativity Desktop Client to reflect the new server name, http://servername/RelativityWebAPI/ .

You must install all web components, but you can disable the Relativity, RelativityREST, and RelativityServices application pools in IIS.

### Physical memory on the SQL Server(s)

Install additional memory on the Relativity SQL Server(s) for an overall performance gain. The more memory you install, the less SQL will have to access disks. Disk access is slower.

The majority of SQL Server memory is used for the following processes:

- Each time SQL Server reads from disk, it commits those pages to memory so that future requests for the same data are cached in the Buffer Pool and readily available.

- The Procedure Cache stores the most optimal Execution Plans in memory so that they don't need to be recompiled each time, which can be processor-intensive.

The more information that you can store in memory, the better. The following table specifies the maximum memory supported for each edition of SQL Server.

SQL Server Edition Maximum Memory Supported

Enterprise Operating system maximum

Standard

- 64 GB in SQL Server 2012

- 128 GB in SQL Server 2014 and SQL Server 2016

After installing additional memory, be sure to set the SQL Server Max Server Memory server configuration option. For more information, see Configuring SQL Server .

We suggest that you make enough memory available to cache the eddsdbo.Document table of your largest, most active workspace(s) in RAM. If you don't host any particularly large workspace databases but host many, you should have enough memory to cache the three largest workspaces combined. SQL Server page life expectancy is a good metric to monitor in order to determine if your SQL Server has enough memory.

## SQL Server failover clustering

SQL Server failover clustering ensures SQL Server availability and provides protection in the event of hardware failure. Failover to another node is quick and provides service availability, but it doesn't provide data redundancy. Instead, data protection is usually provided at the storage level.

(Source: http://www.mssqltips.com/tipprint.asp?tip=1882 .)

A SQL Server cluster appears on the network as a single SQL Server instance on a single computer. Internally, only one of the nodes owns the cluster resource group at a time, serving all the client requests for that failover cluster instance.

In case of a failure (hardware failures, operating system failures, and application or service failures) or a planned upgrade, group ownership is moved to another node in the failover cluster. This process is called failover.

By leveraging the Windows Server Failover Cluster functionality, SQL Server failover cluster provides high availability through redundancy at the instance level.

(Source: http://msdn.microsoft.com/en-us/library/ms189134.aspx .)

SQL Server clustering is only supported in Enterprise editions of Windows Server. The number of nodes supported for failover clustering depends on the operating system and the SQL Server Edition.

## Distributed Relativity SQL Servers

Scale out the existing Relativity environment by incorporating additional SQL Servers. This helps distribute the load and you can store larger, more demanding databases on their own dedicated set of resources. Any number of Relativity servers can be included in an environment.

Each additional Relativity SQL Server is referred to as a "Distributed" SQL Server, unlike the pimary SQL Server, which houses the EDDS database. There's only one EDDS database in a Relativity environment.

You can create new workspaces on any distributed SQL Server. You can also migrate existing workspaces between servers as needed.

For more information, see Distributed SQL Server installation .

## Data Grid nodes

As the business and data volumes keep growing, so will the Data Grid indexes. Indexes have a max of data and a max amount of shard that they can hold per Tier level. Scaling Data Grid data nodes is similar to scaling additional servers in Relativity in the sense that we add more and more Data Grid nodes to share the load of the data that is being placed on them and the queries that each data node has to service. Adding data nodes to the cluster does not require the cluster to be taken offline. When a data node comes online, the software automatically rebalances the indexes and shards among the data nodes to the most optimal configuration.

Client nodes are scaled in the same way. The more users and cases that are placed in the Relativity Data Grid cluster, the more requests will come into Data Grid. With more requests coming in, the more client nodes are needed to service those requests. The current Data Grid System Requirements call for 1 client node for a Tier 1 environment, 2 client nodes for a Tier 2 environment and 3 client nodes for a Tier 3 environment.

Monitoring system performance with Marvel is a good way to assess the need to scale in the environment. Marvel captures trending data and shows you how the environment has been performing over time with data and users increasing.

## Web load balancing

You can use multiple web roles to distribute Relativity user load.

### Microsoft network load balancing

Relativity supports different methods of web load balancing and the ability to distribute user sessions across multiple servers, which distributes the server load and allows for redundancy. Currently, Relativity supports Windows Load Balancer, set to Single affinity mode. Relativity doesn't support an affinity of None at this time.

Single affinity directs a specific IP address to the same server every time until the NLB Cluster is broken, a new server is added to the cluster, or a server is turned off. If you have multiple users behind a firewall, all of the users are directed to a specific server, and they stay there until the cluster is broken. This doesn't provide true NLB support, but it's required because the viewer uses an authentication token to create a second connection on the web server.

Contact Relativity Support to obtain NLB setup documentation.

### Relativity user load balancing

You can use Relativity's Enable User Load Balancing feature to equally distribute user loads across all web servers that have Enable User Load Balancing set to Yes. When a user connects to the login page, the platform looks at the user status table to determine how many users are logged in to each web server. The user will then be re-directed to the web server with the lowest number of logged in users.

This requires setting up multiple URLs in addition to having multiple web servers or VMs. For more information, see Servers .

This feature only load balances users logging in to the system, not Relativity Desktop Client sessions.

## Terminal services

To accommodate users with poor network connectivity, consider providing some type of a terminal services option. We suggest having Terminal Services solution available as a backup. The hardware required for this server role is dependent on the number of users it needs to support.

Deploying a program on a terminal server instead of on each device provides the following benefits:

- You can quickly deploy Windows-based programs to computing devices across an enterprise. Terminal Services is especially useful for programs that are frequently updated, infrequently used, or difficult to manage.

- It can significantly reduce the network bandwidth required to access remote applications.

- It improves user productivity. Users can access programs running on a terminal server from devices such as home computers, kiosks, low-powered hardware, and operating systems other than Windows.

- It provides better program performance for branch office workers who need access to centralized data stores. Data-intensive programs sometimes don't have client/server protocols that are optimized for low-speed connections. Programs of this kind frequently perform better over a Terminal Services connection than over a typical wide area network (WAN).

For this and more information on Terminal Services, see http://technet.microsoft.com/en-us/library/cc755053(WS.10).aspx .

## User notifications

There are several notifications available to help system admins better manage their Relativity environments.

### Disclaimer Message

When you want users to agree to a disclaimer message when using Relativity, you can create a custom message and an agreement button for users when they first log in to the Relativity environment. This type of message is useful to ensure that users acknowledge Relativity terms of use or the confidential nature of Relativity content.

To customize a disclaimer on a Relativity login page, use the following steps:

- Navigate to the web server(s) at C:\Program Files\ Relativity Corporation\Relativity\EDDS.

- Locate the text file, Disclaimer.txt, and update it with your disclaimer text. You must use plain text only; HTML will not display here.

- Update the DisplayDisclaimer instance setting value to true to display the disclaimer message.

For information, see Instance Settings descriptions .

### Message of the Day (MotD)

The Message of the Day (MotD) is a message displayed to all users when they log in to Relativity. MotD is most commonly used to inform users of planned system maintenance.

To activate or change the message of the day, navigate to the Instance Details tab from Home.

### User status

The user status page displays a list of users currently logged into the system. To access the user status page, navigate to the User Status tab from Home.

You can also send messages to any logged in users. This is helpful if you require emergency downtime during a review. System admins can also force log out users from the system on this page.

### Default workspace tabs

When a user enters a workspace within Relativity, they are usually taken to the Documents tab. You can change this default setting in the Tabs tab of any workspace.

Set the Is Default property to Yes for the tab that you want to designate the default tab in a workspace. If a user doesn't have access to the Default tab, he or she will be directed to the Documents tab.

Modifying the default tab may be helpful in informing users of any upcoming workspace-level maintenance. Additionally, system admins can direct users to custom pages that contain links to instructional items, important information about the matter, or an overview of workspace review progress.

On this page

- Expanding your Relativity environment

- Agents

- Analytics servers

- Dedicated web servers

- Relativity Desktop Client import or export

- Physical memory on the SQL Server(s)

- SQL Server failover clustering

- Distributed Relativity SQL Servers

- Data Grid nodes

- Web load balancing

- Microsoft network load balancing

- Relativity user load balancing

- Terminal services

- User notifications

- Disclaimer Message

- Message of the Day (MotD)

- User status

- Default workspace tabs


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

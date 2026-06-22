---
title: "Agents"
url: https://help.relativity.com/Server2025/Content/System_Guides/Agents_Guide/Agents.htm
collection: user
fetched_at: 2026-06-22T06:02:01+00:00
sha256: 126b8865c0fc953c9ca5ea140bd9daedb2fa708d5a28b3f86899f66380d1f38e
---

Agents

# Agents

Agents are process managers and workers that run in the background of Relativity to complete jobs that you or another user scheduled in your environment. Different agents exist for each type of job. To run a job, the agent for that job type must be assigned to a resource pool. Most agents only process jobs from workspaces assigned to the same resource pool. With the exception of a few agent types, this assignment determines job processing. These agents must still be assigned to a resource pool but can process jobs from any workspace, regardless of its resource pool assignment. For a complete list of these agents, see Resource pools . For example, you must have at least one Branding Manager agent and one Production Manager agent to run a production in Relativity.

Relativity agents are installed to your agent server during the Relativity installation process. You can have multiple agent servers in your Relativity environment, but one server generally functions as your primary agent server, which stores a full set of agents, and possibly an additional agents that support multiple installation. Depending on the agent type, you may add multiple instances of it to a secondary agent server.

In the Agents tab, you can manually add an agent type to a server to enable or improve the performance of a number of Relativity features.

Relativity developers can also build custom agents to handle scheduled jobs. See the Build agents for more information.

## Agent installation requirements

The installation requirements for Relativity agents include:

- Installation drive —Relativity installs agents in the following directory by default: [Installation drive]:\Program Files\kCura Corporation\Relativity\Agents.

- Total agents per server —a default Relativity installation includes a set of core feature agents. You can install additional agents on a Relativity server. The total number of additional agents should not exceed the number of processor cores available on the server.

You need to ensure that each server has the required minimum number of processor cores. For minimum hardware requirements, see System requirements .

- Agent instances —the recommended number of instances of each Relativity agent vary per feature and per environment setup. You should run at least one agent of each type in your environment. For a description of each agent and the recommended number of instances, see the List of agents .

If you are working in a large environment and need agent use recommendations to manage a large database, contact Relativity Support .

## List of agents

Relativity supports multiple agents to execute a variety of different processes. These agents can be divided into different categories based on the number of an agent type allowed per environment, the location where the agents run, and the number of type of resources that they require. The different categories of Relativity agents include:

- Single agent per environment

- Definitive number of agents per resource pool

- Scalable agents

- Web agents

- Isolated scalable agents

### Single agent per environment

For specific Relativity agent types, you are required to add one agent per environment. These agents execute during the off-hours that you configure for them to run. In addition, they require minimal resources so you run these agents on a virtual server that has 4 CPUs and 4 GB of RAM. If you do not meet these minimal requirements, your Relativity environment may experience a performance impact. These agents are not specific to a resource pool and are available across your Relativity environment.

If you add more than one of the agents in the following list, your Relativity application may not work properly or key components may not function properly. If you delete any of these agents, Relativity displays warning messages.

For the following agent types, Relativity requires a single agent per environment:

Alert Manager

Description

This agent is used for Environment Watch, and it runs every 30 seconds to fetch alert data from Kibana and populate it into corresponding Relativity Alert RDOs. The Alert Manager Agent is automatically added when the Relativity Alerts application is installed in the instance.

Audit Ingestion Worker

Description This agent is deprecated and should not be added to any environment.

Billing Agent

Description

Formerly known as the Case Statistics Manager, this agent collects usage metrics, as well as creates and send reports. The Billing Agent requires that the Workspace Housekeeping Agent has successfully completed processing.

If the Billing Agent is disabled for seven consecutive days, Relativity access becomes restricted.

See Billing Agent for details on this agent.

Cache Manager

Description This agent is deprecated and should not be added to any environment.

Choice Editor Rearrange Tabs Agent

Description This agent is responsible for rearranging the tab hierarchy for the Choices tab.

Conversion Cache Manager

Minimum number Requires one agent per environment.

Maximum number Do not install more than one agent.

Description Generates jobs per active Cache Location Server during off hours, which kicks off the cleanup process.

Data Grid Audit Manager

Description Populates filters in the Data Grid for Audit application.

Data Grid Audit Reporter

Maximum number One agent per environment

Agent type Reporter

Description The Data Grid Audit Reporter agent reviews the audit queue for errors that occurred during migration from SQL to Data Grid. This agent triggers a Relativity error based on the agent's run interval. This agent is set to an hourly run interval by default.

Data Grid Kepler Host

Description This agent is deprecated and should not be added to any environment.

Data Grid Manager

Description A Data Grid Manager agent is an off-hours agent responsible for Data Grid enabled workspace management, including delete outdated search results cache tables and monitoring Data Grid index conditions.

Data Grid Migration Manager

Description Identifies all documents with extracted text stored in SQL for any workspace with the Data Grid Text Migration application installed.

Group Membership Manager

Description Creates and coordinates tasks for jobs that act across multiple databases. This agent is currently used only for adding and removing users from groups.

File Deletion Manager

Description Deletes files from Relativity repositories once they are deleted from a workspace, using the DeleteFile queue on the EDDS database. This agent runs during off-hours.

Imaging Manager Agent

Minimum number

Requires one per environment.

Maximum number Do not install more than one agent.

Description

The agent ensures that Imaging is functioning properly. This includes tasks such as cleaning up stuck imaging jobs and deleting Imaging Warnings that are no longer linked to Documents.

The default interval is 3600 seconds. Do not modify the interval.

PDF Manager Agent

Minimum number

Requires one per environment.

Maximum number Do not install more than one agent.

Description The agent responsible for configuring the necessary artifacts for a newly created PDF job and also batching larger PDF jobs into smaller units in the mass PDF operations. This agent runs every five seconds by default, and should not be modified. If the Australian workflow is enabled in the instance, the PDF manager can also delete PDFs stored in Relativity.

Relativity Forms Metrics Collector Agent

Minimum number

Requires one per environment.

Maximum number Do not install more than one agent.

Description Runs once a day during Off Hours and collects data about Object Types and their usage of Relativity Forms.

Server Manager

Description Updates Relativity with version and job status information from Analytics servers and worker manager servers.

Telemetry Metrics Transmission Agent

Description Transmits metric data from the EDDSMetrics.Metrics table to Relativity . Maintains the Metrics table after transmitting the data.

Workspace Upgrade Manager

Description

Looks for workspaces that are pending application upgrade and delegates work to the application installation manager agent, if necessary.

Workspace Delete Agent

Description

Responsible for deleting workspaces during off-hours as configured for your instance.

The agent will continue deleting workspaces that are queued for deletion after the off-hours period expires.

Workspace Housekeeping Agent

Description

Responsible for cleaning up temporary and expired data on workspace and instance level. This agent runs during off-hours.

### Definitive number of agents per resource pool

For specific Relativity agent types, you are required to add one agent per resource pool. These agent types are grouped into the following categories:

- Job coordinators —these agent coordinate work that other processes perform. You can add multiple worker agents to a resource pool but usually only one job coordinator agent.

- Worker-managers —these agents manage the worker agents. You only add one manager agent to each resource pool on a server. Your server does not require any dedicated resources for them, since manager and worker agents do not run in performance-intensive operations at the same time.

You must include one of agents in the following table per resource pool. If a resource pool does not include one of these agents, key Relativity components may not function properly. You may not receive an error message if the resource pool does not include each of these agents.

For the following agent types, Relativity requires one of these agents per resource pool:

Active Learning Manager

Maximum number One per resource pool.

Agent type Worker-manager

Description Responsible for performing Active Learning tasks such as managing the Classification Index population and Index builds, Review Queues and updating the Review Statistics in the Active Learning Project.

Relativity Analytics Categorization Manager

Maximum number Add up to four agents per resource pool.

Agent type Job coordinator

Description Clears any previous job results from the population table, and then it categorizes the specific group of documents in the categorization set.

Analytics Core ARM Manager

Maximum number One agent per resource pool.

Agent type Worker-manager

Description Orchestrates the process of moving Analytics data using ARM. The corresponding worker is Analytics Core ARM Worker.

Relativity Analytics Index Progress Manager

Maximum number One agent per Analytics server per resource pool.

Agent type Job coordinator

Description Enables and facilitates automation of the Analytics index building process from population to activation.

Auto Batch Manager

Maximum number One agent per resource pool.

Agent type Job coordinator

Description Runs existing batch jobs marked as auto-batch in pre-configured intervals.

Relativity Analytics Cluster Manager

Maximum number One agent per resource pool.

Agent type Job coordinator

Description Clusters documents based on the Analytics index settings.

Relativity Analytics Index Manager

Maximum number One agent per Analytics server per resource pool.

If your environment includes more than one Analytics server, then you would need additional Relativity Analytics Index Manager agents.

Agent type Job coordinator

Description Populates Analytics indexes and pushes them to the Analytics server.

dtSearch Index Job Manager

Maximum number Only one agent per resource pool.

Agent type Worker-manager

Description Creates population tables and manages the indexing queue. For example, it checks to see if workers completed their work. During incremental build, it also does the work to balance the population tables and manages the status updates on sub-index tables.

OCR Job Manager

Minimum number At least one agent per resource pool. We recommend having one OCR Job Manager agent per agent server in the resource pool.

Agent type Worker-manager

Description Converts the options configured in an OCR set into individual jobs, by building tables, inserting records, and handling SQL queries, and then compiles output from the OCR Worker into a single result set for the user. It also recovers orphaned OCR jobs from dead agent servers.

Processing Migration Manager

Minimum number One agent per resource pool.

Agent type Job coordinator

Description Manages the running of processing archive jobs in ARM.

Production Manager

Maximum number We recommend at least one agent per resource pool.

Agent type Worker-manager

Description Creates production numbers and applies them to productions. This is also responsible for creating branding jobs and populating the branding queue. The Branding Manager agent is the corresponding worker.

Structured Analytics Manager

Maximum number One agent per resource pool.

Agent type Job coordinator

Description Oversees the Structured Analytics Worker agents by keeping the structured data analytics primary job up-to-date and creating worker jobs. For more information, see Analytics servers .

Text Extraction Manager

Maximum number One agent per resource pool.

Description Extracts the text from files associated with dynamic objects, and adds it to text fields on the file fields of the dynamic objects. When you create a File field for a custom object, an accompanying Long Text field is also created. When you upload a file to that file field, the Text Extraction Manager reads the text from that file's name and writes it into the long text field.

Transform Set Manager

Maximum number One agent per resource pool.

Description Runs transform jobs for domain parsing and conversation indexes by parsing regular expressions, and outputs these results to a Dynamic Object that has a destination field with a relation on the document object type.

### Scalable agents

Relativity includes agents that you can scale to the appropriate number for your environment needs. You can add any number of these agents, but you must include at least one per resource pool. Depending on your environment, you may need more than one agent. For example, you may need several worker agents to handle very large documents or Branding jobs. You can run these agents on a server with one CPU core per agent, and 1 GB of RAM. You may want to double these memory requirements to accommodate heavy workloads in your Relativity environment.

For the following agent types, Relativity requires at least one agent per resource, but you also have the option of adding multiple agents depending on your current needs:

Active Learning Worker

Minimum number At least one agent per resource pool. We recommend one agent for every 15-20 active reviewers in your resource pool.

Agent type Job coordinator

Description Responsible for managing the documents in the review queues in Active Learning projects.

Analytics Core ARM Worker

Minimum number Requires at least one agent.

Maximum number Add up to four agents per resource pool

Description Responsible for moving Analytics conceptual and classification indexes using ARM.

Application Installation Manager

Minimum number Requires at least one agent.

Description Detects applications that need to be installed or upgraded in a workspace. For more information, see Upgrading workspaces .

ARM agent

Minimum number Requires at least one agent.

Description Performs ARM backup, restore and move job functions.

Branding Manager

Minimum number May require more than one agent.

Description Creates production images and applies endorsements.

Conversion Cache Delete File Discovery Agent

Minimum number Requires at least one agent

Description Executes the first phase of the cleanup process, Discovery, identifies and batches up old/expired cache files for each workspace of Cache Location Server on a particular job.

Conversion Cache Delete File Worker Agent

Minimum number Requires at least one agent.

Description Executes the second phase where all cached files that were batched up in Discovery phase are deleted.

Conversion Complete Agent

Minimum number Requires at least one agent.

Maximum number Add up to two agents per instance.

Description

Writes to cache documents converted by the Conversion Agent and notifies the Relativity front end when conversion jobs are ready. This agent is created after a new Relativity installation. Upon upgrade, you must created the agent manually. We do not recommend putting this agent on the Conversion Agent server, as that server should be dedicated to the Conversion Agent, not the Conversion Complete Agent.

This Agent is not resource pool aware.

Data Grid Audit Deleter

Maximum number Any number of agents per resource pool.

Agent type Worker-manager

Description Off-hour agent that deletes all audits from SQL that have been successfully migrated to Data Grid. The agent will only delete audits in SQL older than the PostMigrationPersistencePeriod Instance setting value in days.

Data Grid Audit Migrator

Maximum number Any number of agents per resource pool. However, an excessive number of these agents may cause functionality issues with Data Grid.

Agent type Worker-manager

Description Migrates audit data from SQL to Data Grid for any workspace that has Data Grid for Audit installed. The frequency with which this agent checks for migrations and runs the migrations is controlled with the agent run interval value. Do not run the Data Grid Audit Deleter agent at the same time as the Data Grid Audit Migrator agent, as migration and deletion can conflict.

Data Grid Migration Worker

Minimum number Requires at least one agent. If you have a multi-workspace text migration, you can add a worker agent for each workspace being migrated. Adding multiple agents for a single-workspace text migration does not make the migration run any faster.

Description Migrates extracted text from SQL to Data Grid for any workspace with the Data Grid Text Migration application installed.

Group Membership Worker

Minimum number Requires a minimum of one agent per environment.

Description Execute tasks created for jobs that act across multiple databases. This agents is currently used only for adding and removing users from groups.

dtSearch Index Worker

Minimum number May require more than one agent. You can add multiple agents as necessary. The maximum is four agents per server. We recommend using one core and 2 GB of RAM for each additional agent.

Description Performs the indexing operation for each sub-index. Additionally, workers are responsible for compression and copying steps at the end of the indexing. During incremental build, the workers are responsible for removing documents that are no longer in the saved search.

Imaging Response Agent

Minimum number

One agent thread per eight Imaging Worker threads. You can add multiple agents as necessary.

By default, the thread count for the agent is two threads per Processor Count of the server on which the agent is running. You can change the default agent thread count on the MaxImagingResponseThreads instance setting in Relativity.Imaging section. Since we support adding multiple instances of this agent, modifying that instance setting is not required.

Description

Picks up imaging set, mass imaging and image-on-the-fly messages from Message Broker, as published by Workers, and directs them to the proper finalization logic in Relativity.

Imaging Request Agent

Minimum number At least one per environment. You can add multiple agents as necessary.

Description

Handles all submissions of Imaging Set, Mass Imaging, and Image on the Fly requests. It picks up a message from Message Broker, and based on the type of Imaging Job will execute the appropriate logic and submit the Documents to Invariant.

Mass Operation Manager Agent

Minimum number

At least one per environment. You can add multiple agents as necessary.

Description Works with Message Broker to complete mass operations within the environment. The number of parallel jobs the agent can work on is governed by the MassOperationManagerThreadCount instance setting.

OCR Job Worker

Minimum number May require more than one agent. The number of workers to one manager depends on how large the data set is, what any relevant batch sizes are, and whether a bottleneck occurs when you add more workers. We recommend managing any manager:worker relationship using these considerations.

Description Takes an OCR job created by the OCR Job Manager, and translates the images into text.

Processing Set Manager

Minimum

number

Multiple agents per environment. We recommend starting with two and adding more agents as needed.

Agent type Job coordinator

Description Manages the running of processing sets by handling the SQL queries involved in the job; retrieves errors encountered while sets are running; picks up processing set deletion jobs and submits them to the worker manager server. For more information, see Installing and configuring Processing .

Relativity Integration Points Agent

Minimum number

Requires at least one agent. However, you can also scale this agent as necessary. The maximum number allowed per instance is four.

Relativity Integration Points agents operate on a single agent per job basis. If you have four agents enabled and only one job running in your workspace, only one agent will be performing work while the other three agents will be idle until additional jobs are started. Likewise, if you have four agents enabled and three jobs running, three agents will be doing work, one for each job, and one will be idle waiting for an additional job to start.

Description

Responsible for batching up data from the source provider and pulling it into Relativity fields. Also responsible for stopping an integration points job when the user clicks Stop on the console.

Relativity Legal Hold Agent

Minimum number Requires at least one agent. However, you can also scale this agent as necessary.

Description Sends emails including reminders and escalations, pulls emails in from custodian responses, and purges custodians from a project.

RSMF Slicing Agent

Minimum number Requires at least one agent.

Description Works with the Message Broker to complete RSMF slicing operation to create subsets of larger RSMF documents and conversations.

Script Manager Agent / Script Run Manager

Maximum number No maximum, but minimum of one per resource pool.

Agent type Script Run Manager

Description Coordinates and runs Relativity Scripts.

Search Terms Report Agent

Maximum number No maximum, but minimum of one per resource pool. Only ten agents can work simultaneously in a workspace.

Agent type Job coordinator

Description Runs a search against an existing dtSearch index, and returns a count of matching terms found in this index.

Structured Analytics Worker

Minimum number May require more than one agent.

Description Performs all structured data analytics tasks, including setting up staging, exporting document information from Relativity, monitoring the Analytics Engine, importing document information into Relativity, and creating reports. For more information, see Analytics servers .

User Group Sync Agent

Minimum number Requires at least one agent.

Description

This agent is responsible for the synchronization from master instance to duplicate instance as part of the User Group Synchronization application.

Workspace Upgrade Worker

Minimum number Requires at least one agent.

Description

Runs the script required to update the workspace databases and Invariant stores. On an SQL Server profile, you can edit the Workspace Upgrade Limit field, which controls the number of agents accessing the server during an upgrade. The setting entered in this field can’t exceed the setting in the GlobalWorkspaceUpgradeLimit instance setting value. If you enter a number that exceeds this instance setting value, an error occurs that cancels your update. For more information, see Instance settings and Upgrading workspaces .

### Web agents

For specific Relativity agent types, you are required to add one agent per web server. If you add more than one of the following agent, your Relativity application may not work properly.

If you experience the following issues, verify that the following agent is running in your installation:

- Custom pages are not working properly —verify that the Custom Page Deployment Manager is running.

For the following agent type, Relativity requires one agent per web server:

Custom Page Deployment Manager

Description Polls the LibraryApplication and ApplicationServer tables in the EDDS database according to a configurable time interval to check for new versions of any application installed in the ApplicationLibrary table.If a new version is discovered, the Custom Page Deployment Manager runs and installs the updated version of the application's custom pages on that web server. The Application Server table in the EDDS database is then updated to reflect the new version number. This agent is installed on the kCura Web Processing Windows Service, which runs on each web server in your Relativity installation.

### Isolated scalable agents

Relativity includes isolated scalable agents which you can customize for your environment needs. This type of agent needs to be on its own agent server with no other Relativity agent types on the server. These agents are multi-threaded and will use all resources on the server when needed.

Depending on your environment, you may wish to scale the server up for better performance. Monitor both CPU and RAM during normal usage as well as during jobs. If needed, add more CPU and RAM to the server. You may also add another server with another agent by itself. You can add any number of these agents, but you must include at least one per resource pool.

Conversion Agent

Description Works with the Message Broker to complete document conversion for the document viewer. Deploy each Conversion agent on its own server. Do not use the server for any other purpose but running this agent.

Conversion Agent - Convert Ahead

Description Works with the Message Broker to complete document conversion when the user is on the document viewer. Deploy each Conversion agent on its own server. Do not use the server for any other purpose but running this agent.

Conversion Agent - Mass Convert

Description Works with the Message Broker to complete document conversion when using the mass convert action. Deploy each Conversion agent on its own server. Do not use the server for any other purpose but running this agent.

Conversion Agent - On the Fly

Description Works with the Message Broker to complete document conversion for the current document opening. Deploy each Conversion agent – On the fly on its own server. Do not use the server for any other purpose but running this agent.

dtSearch Search

Minimum number description

Requires at least one agent per resource pool. The agent must be on its own server with no other Relativity agents. The server should not be used for any other role, such as Web, Analytics, or something else. Hosts the search service and executes search requests that users submit. This agent is multi-threaded and will use all resources on the server when needed. Follow these guidelines for this agent:

- Monitor CPU, RAM, and disk I/O during normal usage and during Search Terms Report jobs.

- Disk I/O on the dtSearch Index Share may also become a bottleneck – monitor and configure as needed.

- If performance issues occur, add more server resources.

- You may also add another agent server with only the dtSearch Search agent. However, it is often preferred to scale up rather than out.

- For details on configuring the dtSearch service for HTTPS, see HTTPS setup for dtSearch service .

PDF Worker Agent

Minimum

number

Requires two agents per environment. However, you may add more agents as needed.

Description Responsible for the document/image to PDF conversion. It will also do the packaging of results into a ZIP/Portfolio/Single PDF if Download is selected for mass PDF operations. This agent runs every five seconds by default and should not be modified.

### Removable agents

Certain agents may be visible in your Server environment that have either been deprecated in previous versions or are relevant only to RelativityOne. You can ignore or remove these agents without disrupting your environment. These include:

- Cache Manager

- Case Statistics Manager

- Conceptual Index Resource Manager Agent

- RelativityOne Analytics Index Population Manager

- Secret Rotation Agent

- Manage Temporal Transcript Files

## Agents change log

This change log summarizes changes made to agents.

Agent name Change Description of change Version

Agent name Change Description of change Version

RSMF Slicing Agent Added Works with the Message Broker to complete RSMF slicing operation to create subsets of larger RSMF documents and conversations. Server 2024

Secret Agent Removed This agent has been deprecated. Server 2023

Assisted Learning Manager Agent Removed This agent has been deprecated and replaced with the Active Learning Manager Agent. Server 2023

Assisted Learning Worker Agent Removed This agent has been deprecated and replaced with the Active Learning Worker Agent. Server 2023

Arm Metric Agent Removed This agent has been deprecated in Server 2023. Server 2023

Transcript Manager Removed This agent is no longer needed in a server environment. Server 2023

Workspace Housekeeping Agent Added Responsible for cleaning up temporary and expired data on workspace and instance level. This agent runs during off-hours. Server 2023

Workspace Delete Agent Added Responsible for deleting workspaces during off-hours as configured for your instance. Server 2023

Case Manager Removed The roles of the Case Manager have been replaced by the Workspace Housekeeping Agent and the Workspace Delete Agent. Server 2023

Conceptual Index Resource Manager Removed This agent is only required for RelativityOne instances. It will no longer be installed with our Server products. Server 2023

Conversion Cache Delete File Worker Added Executes the second phase where all cached files that were batched up in Discovery phase are deleted. Server 2022

Integration Points Manager Removed This agent has been removed. It will no longer be installed with our Server products. Server 2022

Conversion Cache Delete File Discovery Added Executes the first phase of the cleanup process, Discovery, identifies and batches up old/expired cache files for each workspace of Cache Location Server on a particular job. Server 2022

Conversion Cache Manager Added Generates jobs per active Cache Location Server during off hours, which kicks off the cleanup process. Server 2022

Mass Operation Manager Added Works with Service Bus to complete mass operations within the environment. Server 2022

Relativity Forms Metrics Collector Added Runs once a day during off hours and collects data about Object Types and their usage of Relativity Forms. Server 2022

Analytics Core ARM Worker Added Responsible for moving Analytics conceptual and classification indexes using ARM. Server 2021

ECA and Investigation Agent Removed This agent has been removed, per the deprecation of the ECA and Investigation application. Server 2021

PDF Manager Agent Added Responsible for configuring the necessary artifacts for a newly created PDF job and also batching larger PDF jobs into smaller units in the mass PDF operations. This agent runs every five seconds by default, and should not be modified. If the Australian workflow is enabled in the instance, the PDF manager can also delete PDFs stored in Relativity. Server 2021

PDF Worker Agent Added Responsible for the document/image to PDF conversion. It will also do the packaging of results into a ZIP/Portfolio/Single PDF if Download is selected for mass PDF operations. This agent runs every 5 seconds by default and should not be modified. Server 2021

Analytics Core ARM Manager Added Orchestrates the process of moving Analytics data using ARM. The corresponding worker is Analytics Core ARM Worker. Server 2021

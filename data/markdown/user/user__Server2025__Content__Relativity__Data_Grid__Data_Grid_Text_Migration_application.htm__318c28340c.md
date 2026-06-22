---
title: "Data Grid Text Migration application"
url: https://help.relativity.com/Server2025/Content/Relativity/Data_Grid/Data_Grid_Text_Migration_application.htm
collection: user
fetched_at: 2026-06-22T06:09:37+00:00
sha256: 4d6f7601ded6490a7ef9acebae2b407108bbb750ad6655a0cdfddb8f05a718d8
---

Data Grid Text Migration application Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Data Grid Text Migration application

The Data Grid Text Migration application is an application you can use to migrate your long text fields from SQL to Data Grid.

You can use the Data Grid Text Migration application to migrate your long text fields from SQL to Data Grid. For optimal workspace performance when using SQL features, we strongly recommend using fixed-length text fields . Enabling Data Grid allows you to store long text document fields, such as extracted text, outside of the SQL document table. Data Grid utilizes the Relativity file share to store long text document fields, which is the same location where native and image file data is stored.

Once you start a migration job, the results are permanent. You can't delete a migration job once it has been started.

## Considerations

There are several considerations you should be aware of before and during text migration.

-

Minimizing the impact on your SQL document tables, particularly in larger cases with extensive long text document field data.

-

Decreasing your SQL footprint or reallocating resources to other workflows in your Relativity instance.

-

Storing long text document field data in a separate file share location from your natives and image file data.

-

Simple setup and inclusion in your workspace templates before loading data into the workspace.

-

Access to the Data Grid Text Migration application, a front-end tool for moving long text document fields in existing workspaces without downtime.

### Before running text migration

Before running a text migration job, review the following considerations:

- If your workspace has any custom solutions or third-party applications built on the long text field you're migrating, update them to use the Export API to read long text and metadata fields.

- If your environment is configured for FIPS, you cannot use the Text Migration application.

- If you have any custom data which relies on the long text field you're migrating being stored in the SQL Document table, contact Relativity Support to discuss alternative solutions before migration.

- Data Grid only supports the IS SET and IS NOT SET operators. If your workspace uses other operators to query on long text fields, you will need to perform a similar query using dtSearch.

- Mass operations are not supported with Data Grid. If you need to populate a long text field stored in Data Grid, perform an OCR and select the Data Grid field as the destination field.

- Once the text migration job completes, the only index search available for the migrated field is dtSearch. Keyword search is not supported. Data Grid supports all features of dtSearch. If you do not have an active dtSearch index in your workspace, you will need to build one. You can include a combination of Data Grid and SQL fields in your saved search. For more information, see Running the Breakage Report .

For a list of supported and unsupported Data Grid text functionality, see Supported and unsupported functionality .

### Running text migration

Review the following considerations for running a text migration job:

- The Data Grid Text Migration application runs at the instance level. However, you must install the application to at least one workspace.

- If you have index build in progress (like dtSearch or Analytics), let the index build finish before starting a migration job.

- If you have a mass replace in progress, let the operation finish before starting a migration job.

- We recommend running a migration job in off hours. However, it is not required.

- You can only have one job in progress at a time. If you start a new text migration job while another is in progress, the new job is added to the queue.

- Although the application automatically deletes the column in SQL, you are still required to reclaim the space that was taken up by your long text document field in SQL.

### Supported and unsupported functionality

Once you enable a long text field's access to Data Grid, you can't disable it, so it's important to understand the benefits and limitations of storing text in Data Grid.

Supported extracted text functionality Currently unsupported functionality

- Import/export through the Relativity Desktop Client

- Viewer

- Preview

- OCR

- dtSearch indexing and searching

- Persistent highlight sets

- Processing

- Integration Points

- Analytics

- ARM

- Keyword search

- SQL queries to long text fields stored in Data Grid

- Adding extracted long fields stored in Data Grid to layouts (including the Document panel)

- RSAPI query

- Pivot and Sort in the UI

- Filtering in the Document list on extracted text

- Mass operations:

- Edit

- Replace

- Tally/Sum/Average

- Export to File

## Installing the Data Grid Text Migration application

The Data Grid Text Migration application runs at the instance level. However, you must install the application to at least one workspace.

To install the Data Grid Text Migration application:

- Navigate to the Application Library tab.

- Select Data Grid Text Migration from the list of Relativity applications.

- Next to Workspaces Installed, click Install .

- Next to Workspaces, click , and then select a workspace.

- Click Ok .

- Click Save .

Once you install the Data Grid Text Migration application, the Text Migration Jobs tab appears under the Data Grid tab.

### Installing the text migration agents

After you install the Text Migration application, you must install one Data Grid Migration Manager agent and at least one Data Grid Migration Worker agent to your environment. We recommend installing one Data Grid Migration Worker agents.

You can run the Breakage Report without installing the text migration agents. We recommend running the Breakage Report and resolving any issues before running a migration job.

For more information on installing agents, see Adding and editing agents .

## Running text migration

Once you install the Data Grid Text Migration application and configure your migration agents, you can run text migration. See Running text migration .

On this page

- Data Grid Text Migration application

- Considerations

- Before running text migration

- Running text migration

- Supported and unsupported functionality

- Installing the Data Grid Text Migration application

- Installing the text migration agents

- Running text migration


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

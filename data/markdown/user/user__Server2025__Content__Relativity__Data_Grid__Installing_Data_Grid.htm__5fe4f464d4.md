---
title: "Installing Data Grid"
url: https://help.relativity.com/Server2025/Content/Relativity/Data_Grid/Installing_Data_Grid.htm
collection: user
fetched_at: 2026-06-22T06:12:23+00:00
sha256: 616420503bea86416ce96ce9639ab72a63c48b252a9e8d7bdc456bafd1ad0f69
---

Installing Data Grid Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Installing Data Grid

This page includes steps for configuring Data Grid Text (Core) in your environment. Before configuring Data Grid, ensure you've completed the pre-installation steps. For more information, see Pre-installation .

## Enabling your workspace and extracted text field for Data Grid

To enable your workspace for Data Grid, perform the following steps:

We recommend you only enable Data Grid for fields storing extracted text, OCR text, or translated text.

- Navigate to the Workspace Details tab, and then click Edit .

- Enable the Is Data Grid Enabled field.

- (Optional) Next to Data Grid File Repository , select the path for the physical location of the text files used by Data Grid. If no file repository is specified for this field, and Data Grid is enabled, Data Grid stores text in the default file repository.

If you run out of space in this repository, you can specify a new repository. Data Grid will continue to read from the old repository as well as the new repository.

- Click Save .

To enable the extracted text field for Data Grid, perform the following steps:

- Navigate to the Fields tab.

- Locate the extracted text field and click the Edit link next to it.

- Enable the Store in Data Grid field under the Advanced Settings tab.

If you are storing extracted text in Data Grid, the Include in Text Index field is set to No because there is no SQL text index. If you want to search using dtSearch, you must follow best practice of creating a saved search of fields you want to index.

- Click Save .

Enabling extracted text fields for Data Grid works for new workspaces only. You can't enable Data Grid for fields that already have text in SQL. If you want to migrate fields from SQL to Data Grid, you must use the Data Grid Text Migration application .

## Data Grid agent

Ensure that the Data Grid Manager agent is installed in your environment. This is a single-installation agent responsible for Data Grid-enabled workspace management (off-hours), including deleting outdated search results cache tables and monitoring Data Grid index conditions.

For more information on installing agents, see Adding and editing agents .

On this page

- Installing Data Grid

- Enabling your workspace and extracted text field for Data Grid

- Data Grid agent


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

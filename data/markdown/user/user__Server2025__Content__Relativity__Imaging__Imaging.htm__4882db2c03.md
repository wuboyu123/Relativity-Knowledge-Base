---
title: "Imaging Documents"
url: https://help.relativity.com/Server2025/Content/Relativity/Imaging/Imaging.htm
collection: user
fetched_at: 2026-06-22T06:06:08+00:00
sha256: 978ad6863240b45fb86368071b602a1dac6a8c45df21d3c2ad9eed4851a072b6
---

Imaging Documents Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Imaging

You can use imaging to convert a group of documents to images using imaging profiles and sets. You can fine-tune how your images generate by creating reusable profiles that use specific image settings.

With imaging sets, you can image a group of documents by selecting a saved search and a specific imaging profile. Imaging sets also provide error-handling functionality you can use to view error messages and rerun imaging on specific documents or jobs.

Oracle is not built into the Relativity agent framework, but is instead built into the Invariant worker. The required Worker Manager Server/Invariant component actually does the work of basic imaging by using Oracle's imaging capabilities.

See these related pages:

- Imaging profiles

- Imaging sets

- Imaging native types

- Monitoring imaging status

- Running an imaging set

- Imaging jobs in the worker manager queue

- Application Field Codes

## Security permissions for imaging

The following security permissions are relevant to imaging. These apply to all imaging options, including image-on-the-fly, mass image, and imaging sets, unless otherwise noted.

Object Security Tab Visibility Other Settings

- Document - Add, View

- Imaging Profile - View, Edit, Add

- Imaging Set - View, Edit, Add

- You can still use mass imaging and image-on-the-fly even if you don't have the Edit permission on the Imaging Set object.

- Native Type - View*

- Documents

- Imaging Profiles

- Imaging Sets

- Mass Operations

- Image

*View permission for the Native Type object is needed to create a new Basic and/or Native Imaging Profile.

When you run imaging on a specific saved search used in an imaging set, documents that don’t have the "Add Image" permission will be skipped.

## Installing imaging agents

To run any imaging job in your environment, you need the following agents:

- Imaging Manager Agent - ensures that Imaging is functioning properly. This includes tasks such as cleaning up stuck imaging jobs and deleting Imaging Warnings that are no longer linked to documents. For more information, see Imaging Manager Agent .

- Imaging Request Agent - performs background tasks when any imaging request is submitted via mass imaging, image on the fly, or imaging set. For more information, see Imaging Request Agent .

- Imaging Response Agent - picks up imaging set, mass imaging, and image-on-the-fly messages from Service Bus (as published by Workers) and directing them to the proper finalization logic in Relativity. For more information, see Imaging Response Agent .

These agents are automatically installed and enabled in your environment.

To install an additional agent:

- Navigate to the Agents tab.

- Click New Agent and complete the following required fields:

- Agent Type - access the list of agents, filter for the Imaging Request/Response Agent, select it, and click OK .

- Number of agents - enter the number of agents you want to add.

- Agent Server - select a server and click OK.

- Run interval - enter the interval, in seconds, at which the agent should check for available jobs.

- Logging level of event details - select Log critical errors only (recommended), Log warnings and errors, or Log all messages.

- Enabled - select Yes .

- Click Save .

Verify the Enable column displays Yes for the Imaging Request and Response agents.

You won't be able to start any imaging jobs in your workspace if this agent becomes disabled. To re-enable a disabled Imaging Request/Response Agent, click Edit on the appropriate agent, set the Enabled field to Yes, and click Save .

## Troubleshooting imaging

In the event a user reports missing Image commands (in the Viewer or mass operations menu), or the Imaging Sets Run button is disabled, address the following potential causes:

- The Imaging application was uninstalled from Relativity Applications

- The user is a member of a group that doesn't have one or both of the following security permissions granted:

- Mass Images (Mass Actions permissions)

- Add Image (Document security permissions)

## Image on the fly

By using the Imaging option in the Viewer, you can image a single document on the fly with any imaging profile you have permissions to. For more information, see Imaging on the fly .

## Mass image

You can image multiple documents at the same time by using the Mass Image operation in the document list. Select an Imaging Profile to use when imaging a group of documents. For more information on mass imaging, see Mass image .

On this page

- Imaging

- Security permissions for imaging

- Installing imaging agents

- Troubleshooting imaging

- Image on the fly

- Mass image


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

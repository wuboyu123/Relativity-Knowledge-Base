---
title: "Errors"
url: https://help.relativity.com/Server2025/Content/Relativity/Errors.htm
collection: user
fetched_at: 2026-06-22T06:06:33+00:00
sha256: 8dd95e5faa2d17e2fb00d54c38bad6ff9b4be1d6f5a8f93c1b2051a1f8f1ec0e
---

Errors Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Errors

The Errors admin tab shows all the errors that have occurred in the Relativity environment. Due to the number of servers and features involved in your environment, it's possible for there to be thousands of items listed in this tab.

You can also customize the Errors tab view to fit your needs. See Views .

## Fields

You can filter any of the fields to quickly find specific types of errors.

The default errors view includes the following fields:

- Timestamp - the date and time at which the error occurred.

- Workspace Artifact ID - the artifact ID of the workspace in which the error occurred.

- Message - describes the nature of the error. This is the same message the user receives when the error occurs. You can click on the linked error message to go to that error's layout, where you can view the error's complete stack trace. The following are examples of error messages you could see. The resolutions for these errors vary, and you may need to consult with a database or infrastructure administrator for steps on how to resolve them:

- Workspace with ID ####### is of a different version than Relativity.

- Index 0 is either negative or above rows count.

- Problem registering server.

- Timeout expired. The timeout period elapsed prior to completion of the operation or the server is not responding.

- Created By - the name of the user whose action received the error.

- Error Source - the component of the server in which the error occurred. This may be related to an application pool automatically added to the environment during Relativity installation. You may see any of the following listed as error sources:

- EDDS - Web - indicates that the error originated in the primary web server.

- EDDS - Agents - indicates that the error originated in the agents server.

- EDDS - Distributed: Forms Authentication - indicates that the error originated in the server that was put in place to accommodate authentication. The authentication is based on specific code for distributed web servers.

- EDDS - Template Manager - indicates that the error originated in the template manager component of the ADS due to an outdated or otherwise unusable application in the application library.

- Server - the name of the machine on which the error occurred.

- Workspace Name - the name of the workspace in which the error occurred.

- Artifact ID - the unique identifier of the error.

- URL - the location of the error. This may not be populated if the error wasn't logged. This may take the form of a file path or the name of a component of the error source, for example, Application Installer Agent .

On this page

- Errors

- Fields


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

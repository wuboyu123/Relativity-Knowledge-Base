---
title: "Debugging custom applications and support for custom applications"
url: https://platform.relativity.com/Server2025/Content/Site_Resources/Custom_Applications_Support.htm
collection: developer
fetched_at: 2026-06-22T06:28:48+00:00
sha256: 7f0372915f38a7660daa2a330a331a2638f45231328b225d984a90e207660a1a
---

Debugging custom applications and support for custom applications Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

Version: RelativityOne Server 2025 Server 2024

☰

# Debugging custom applications and support for custom applications

While Relativity provides developer environments, tools, and APIs to enable building applications, Relativity does not provide any bespoke developer services for troubleshooting, debugging, or overall consulting on custom development. If you are encountering errors or unexpected behaviors, this topic will help you troubleshoot your application.

## Troubleshooting for all extensibility points

### Unit Tests

Unit tests are your best tool for verifying the behavior of your application. Without unit tests, it is not possible to confirm the root cause of a potential defect. Full unit test coverage of the affected code is required.

### Logging

Logging provides essential information about how your application is running in Relativity. You must use the Relativity Logging helper to create the logs ; and then review the logs in the Relativity database . A few best practices:

- Log the code ingress: the part of your code that Relativity calls into to start executing your logic. It will help verify that your code is being executed in the correct order.

- Log the code egress: the last part of your code that is executed before handing control back to Relativity. It is very helpful to verify that your code is done being executed.

- Log all exceptions. If you are encountering unknown behavior within your application, wrap the top level of your code stack in an Exception and log it.

- To narrow down where an issue may be occurring, create logs:

- at key points in your application logic

- at the start and end of class methods

- when important data is retrieved or calculated

- when you call other APIs

### Templates

Relativity provides Visual Studio Templates for most Extensibility Points. These APIs, Agents, and Custom Pages are guaranteed to work out of the box. If you are having trouble getting your application to work, start from a raw template, and build up your application in several steps so that you can determine where it is encountering issues.

## Troubleshooting specific extensibility points

Extensibility Point Troubleshooting steps

Kepler APIs

- Use Postman or another API client and follow the instructions in the topic Troubleshooting Kepler services to determine if the API is responding to traffic correctly.

Agents

- Determine through the logs if your agent even starts up. Then gradually change parameters to meet your goals.

- Verify that Agents are the correct extensibility point for your use case. For example, if your application needs sub-second responses, you should use an API instead.

- If your Agent uses a workload discovery, troubleshoot it via the Kepler API troubleshooting steps, including instrumenting via logs.

Custom Pages

- Create a pure static custom page, and then build up to your page.

Non-UI Event Handlers

- Event handler usage should be minimal - verify that event handlers are the correct solution.

- Review the documentation for the event handler that you are trying to create. Each event handler type works differently from the others and may have special considerations.

## Contacting Relativity

If you believe that you have encountered a defect in how Relativity is executing your custom application, please contact our Support team through our Support page.

Please include the following information with your request, or Relativity will not be able to correctly handle your issue:

If you are creating a(n) Provide details on

Custom application of any kind

- The instance id that you are working in

- The username and authentication type you are using

- The type of extensibility point that you are creating

- GUIDs for all involved custom extensibility points

- Clear framing of the defect that you have discovered

- Steps to reproduce

Custom API, or consuming a Relativity API

- The API that you are trying to consume

- Either the Relativity API SDK that you are using, or the exact URI that you are calling

- The response code and any data returned

- The behavior when consumed through Postman

- Any data (anonymized and scrubbed as appropriate) that you are sending on the request

Agent

- Full information on URI for your workload discovery, if you have one:

- URI

- Response code

- Request and response data

- Run interval

- Log data, scrubbed as necessary

Custom Page

- The design of your customer page, and which frameworks you are using

- The URI to the custom page

Event Handler

- The type of event handler

- Input and output data, scrubbed if necessary

On this page

- Debugging custom applications and support for custom applications

- Troubleshooting for all extensibility points

- Unit Tests

- Logging

- Templates

- Troubleshooting specific extensibility points

- Contacting Relativity


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use

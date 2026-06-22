---
title: "Infrastructure considerations for logging"
url: https://help.relativity.com/Server2025/Content/Logging/Infrastructure_considerations_for_logging.htm
collection: user
fetched_at: 2026-06-22T06:21:07+00:00
sha256: 368f06b530760c23e9d38e4bd601c9d1882bd80c62b058379fe9976ec8a9a399
---

Infrastructure considerations for logging Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Infrastructure considerations for logging

Logging can be a resource-intensive operation. As a system admin or an infrastructure manager, you must consider the impact of logging on your IT infrastructure. Logging system-subsystem-application matrix

## File sink

Consider this when configuring a file sink for logging:

- Because Relativity application threads can't have an exclusive lock on a network share, we recommend you don't select a network share as a logging sink.

- Granular logging ( WARNING and lower) can fill disk space quickly. We recommend you don't select your primary ( C:/ ) drive as a destination for file logging..

## Storing database passwords

When you configure an alternative SQL Server database sink for logging (other than the RelativityLogs table in the EDDSLogging database) , the password in the connection string is stored as unencrypted (clear) text. This may not be allowed in certain high-security environments.

## Moving EDDSLogging database

Relativity logging relies on the EDDSLogging database for centralized configuration storage. It also uses it the database as the default sink. In a distributed database environment, EDDSLogging must be hosted on the primary database server (the server that hosts the EDDS database). If you move the EDDS database to a different database server, you must also move the EDDSLogging database to the same server.

On this page

- Infrastructure considerations for logging

- File sink

- Storing database passwords

- Moving EDDSLogging database


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

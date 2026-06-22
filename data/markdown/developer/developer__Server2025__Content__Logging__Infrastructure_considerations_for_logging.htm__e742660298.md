---
title: "Infrastructure considerations for logging"
url: https://platform.relativity.com/Server2025/Content/Logging/Infrastructure_considerations_for_logging.htm
collection: developer
fetched_at: 2026-06-22T06:29:41+00:00
sha256: 6e974ed36211a6f21ee27e572d7e119d079a9843c10578e2f5581f32e57591b8
---

Infrastructure considerations for logging

# Infrastructure considerations for logging

Logging can be a resource-intensive operation. As a system admin or an infrastructure manager, you must consider the impact of logging on your IT infrastructure.

See these related pages:

- Logging

- Log from a Relativity application

- Configure logging

- Troubleshoot Relativity using logging

- Logging system-subsystem-application matrix

## File sink

Consider this when configuring a file sink for logging:

- Because Relativity application threads can't have an exclusive lock on a network share, we recommend you don't select a network share as a logging sink.

- Granular logging ( WARNING and lower) can fill disk space quickly. We recommend you don't select your primary ( C:/ ) drive as a destination for file logging..

## Storing database passwords

When you configure an alternative SQL Server database sink for logging (other than the RelativityLogs table in the EDDSLogging database) , the password in the connection string is stored as unencrypted (clear) text. This may not be allowed in certain high-security environments.

## Moving EDDSLogging database

Relativity logging relies on the EDDSLogging database for centralized configuration storage. It also uses it the database as the default sink. In a distributed database environment, EDDSLogging must be hosted on the primary database server (the server that hosts the EDDS database). If you move the EDDS database to a different database server, you must also move the EDDSLogging database to the same server.

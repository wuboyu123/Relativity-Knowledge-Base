---
title: "Setting Up OpenTelemetry Java Agent for Relativity Analytics Engine (CAAT)"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Setting_Up_OpenTelemetry_Java_Agent_for_Relativity_Analytics_Engine__CAAT_.htm
collection: user
fetched_at: 2026-06-22T06:11:33+00:00
sha256: 9c76dd826e6df2f136e36dd50580ca1d3ffac5be1a68b32bc40793b5dabf5088
---

Setting Up OpenTelemetry Java Agent for Relativity Analytics Engine (CAAT) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Setting Up OpenTelemetry Java Agent for Relativity Analytics Engine (CAAT)

This guide provides step-by-step instructions for installing/updating Relativity Analytics Engine (CAAT) along with the OpenTelemetry Java Agent. This enables distributed tracing and observability with minimal code changes.

For other Other integrations, refer to the Environment Watch Install other Integrations Guide .

## Why use opentelemetry-javaagent?

- Automatic Instrumentation: The OpenTelemetry Java Agent automatically instruments supported libraries and frameworks, capturing telemetry data (traces, metrics, logs) without code changes.

- Observability: It provides deep visibility into application performance, dependencies, and bottlenecks.

- Standardization: OpenTelemetry is a vendor-neutral standard, ensuring compatibility with various observability backends (e.g., Azure Monitor, Jaeger, Zipkin).

## Why Auto-Instrumentation is safe

- Non-Intrusive: The agent works by attaching to the JVM at startup, using bytecode manipulation. It does not require code changes or recompilation.

- Widely Adopted: OpenTelemetry Java Agent is used in production by many organizations and is actively maintained.

- Configurable: Instrumentation can be enabled/disabled for specific libraries, and the agent can be removed by simply omitting the -javaagent flag.

- No Persistent Changes: The agent does not persistently modify your application or its dependencies.

## How to install/update CAAT

### Prerequisites

- CAAT (5.1.4.A1) installer package

- CAAT EW bundle (contains startup.cmd )

- Administrative access to the server

### Installation Steps

- Install or upgrade the CAAT 5.1.4.A1 installer. If this has already been completed, skip this step.

- Ensure no analytics jobs are currently running, then stop the Relativity Analytics Engine service

- Stop the Relativity Environment Watch service on the analytics server.

- Copy and replace the following file from the CAAT EW bundle into the bin directory of the installed CAAT application (not the bin directory inside the extracted CAAT installer package):

- startup.cmd

- Once the copying is complete, start the Relativity Analytics Engine and Relativity Environment Watch services and verify the engine is active

- Open Kibana and search for service.name: "relsvr.caat" in the metrics-* data view to confirm telemetry is being collected

## What's updated

- The startup.cmd file is updated to include the OpenTelemetry Java Agent. It references opentelemetry-javaagent.jar , which is provided by the CAAT installer package (not the CAAT EW bundle), to instrument the CAAT service for telemetry data collection.

- Check for these lines within startup.cmd : Copy

```text
-javaagent:..bin\opentelemetry-javaagent.jar

-Dotel.service.name="relsvr.caat"

-Dotel.metrics.exporter=otlp

-Dotel.exporter.otlp.endpoint="http://localhost:4318"

-Dotel.instrumentation.runtime-metrics.enabled=true

-Dotel.instrumentation.java-util-logging.enabled=false

```

## How to verify the changes

- Check Application Logs: On startup, the agent logs its initialization. Look for lines mentioning opentelemetry-javaagent in the CAAT logs.

- Verify Telemetry Export: Confirm that traces and metrics are being sent to your configured backend (e.g., OpenTelemetry Collector, Jaeger, Azure Monitor).

- Check Service Name: Ensure the service appears as Relativity Analytics Engine (or your configured name) in your observability backend.

On this page

- Setting Up OpenTelemetry Java Agent for Relativity Analytics Engine (CAAT)

- Why use opentelemetry-javaagent?

- Why Auto-Instrumentation is safe

- How to install/update CAAT

- Prerequisites

- Installation Steps

- What's updated

- How to verify the changes


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

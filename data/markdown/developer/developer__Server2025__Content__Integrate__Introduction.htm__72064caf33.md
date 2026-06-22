---
title: "Introduction to Relativity APIs"
url: https://platform.relativity.com/Server2025/Content/Integrate/Introduction.htm
collection: developer
fetched_at: 2026-06-22T06:22:03+00:00
sha256: 8a6554138083169e56459106cac6b1fc45da30d065e54065811d030cbed8353f
---

Introduction to Relativity APIs

# Introduction to Relativity APIs

## Conventions & Standards

Relativity publishes APIs in Relativity to expose functionality for integration and automation. The following architectural standards apply to all Relativity APIs:

- Representational State Transfer (REST)

- Semantic Versioning

- Relativity API Conventions

## API documentation

This site provides guidance to help you ramp up, discover and utilize Relativity’s APIs. Broadly speaking, the guidance includes:

- Tutorials to learn how to utilize Relativity’s REST APIs

- Individual API References that introduce the API’s functionality, version history, and OpenAPI Specification files

- Cross references to the RelativityOne User Documentation to explain key concepts, and how they influence the behavior of the application.

## Extending Relativity vs. Integrating with Relativity

This comparison describes main differences between integrating with Relativity with the available APIs, and extending Relativity with the available Extension Points

Extending Relativity Integrating with Relativity’s APIs

Languages and tooling Must use .NET Framework 4.6.2 and deploy using Relativity’s Application Deployment System. Integrate using any tool or language that supports REST.

Deployment Runs on Relativity’s platform, inside Relativity’s ecosystem and datacenter. Runs on your own private cloud, datacenter, and/or machines

Observability and troubleshooting Access to logs through the Log Extractor tool. Access to any observability tools that you use.

Maintainability Code must be kept updated multiple times each year as Relativity’s implementation continues to evolve Domain driven; stable abstractions allow integrations to remain unchanged for years at a time.

## Extensibility maturity journey

### A PaaS beginning

Extending and automating Relativity has historically relied on Relativity’s Platform as a Service (PaaS) capabilities. In this PaaS model, developers write software directly against Relativity SDKs then deploy that software to run in parallel with Relativity in a shared execution environment. More information on how to execute custom software within the Relativity environment can be found here .

### Adopting SaaS

Relativity has a long history of providing access to our APIs, to the point where over 95% of capabilities are accessible via the Kepler API surface. As the market leader in extensible EDRM products, initial strategy focused on adoption before pivoting to focus on consistency. In 2022, Relativity began an API Governance process to drive internally-developed REST APIs towards a consistent set of URI, Query, and Data Contract standards.

### Direct data access focused APIs

Initially, REST API development was prioritized based on the needs of the Relativity User Interface and specific requests from customers. The developers using these endpoints typically had a deep understanding of the data model, including its dynamic data modeling capabilities.

These factors yielded an API surface with many endpoints that provide granular access to the underlying data model. While this provides API consumers with the maximum access and control, it also requires a deep understanding which takes time to acquire, and therefore impedes time to value.

### SaaS evolution

In 2022, Relativity adopted an API-First mindset that focuses on optimizing integration developer experience. In practical terms this means shifting API endpoints away from direct data access and towards functionality-focused endpoints. You can anticipate a growing number of featured-focused endpoints that are easier to understand and utilized to achieve business goals.

This approach will reduce the level of effort required to make use of Relativity’s APIs by reducing the number of API requests required to reach a desired outcome, and reducing the depth of knowledge required to make effective use of Relativity’s APIs.

### Known challenges

#### SaaS to PaaS parity

The largest challenge facing Relativity’s APIs is the need to provide the same depth of functionality that is currently available from the ADS ecosystem. This means expanding the REST API capabilities to allow an integration to be hosted outside of Relativity, yet still extend and automate the user experience within the application.

#### Expanding consistency

Relativity’s API standards are evolving instep with its API Governance to ensure APIs converge on a unified set of API standards.

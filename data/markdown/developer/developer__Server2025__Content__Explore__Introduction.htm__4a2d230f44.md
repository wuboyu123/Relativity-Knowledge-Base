---
title: "Introduction to Relativity Server for Developers"
url: https://platform.relativity.com/Server2025/Content/Explore/Introduction.htm
collection: developer
fetched_at: 2026-06-22T06:21:52+00:00
sha256: 69dd9a2e20b611dfce18994b560902c827a8cc517deece4bbf5427bdbc687b7a
---

Introduction to Relativity Server for Developers

# Relativity Server for Developers

## Extending Relativity vs. Integrating with Relativity

This comparison describes main differences between integrating with Relativity with the available APIs, and extending Relativity with the available Extension Points

Extending Relativity Integrating with Relativity’s APIs

Languages and tooling Must use .NET Framework 4.6.2 and deploy using Relativity’s Application Deployment System. Integrate using any tool or language that supports REST.

Deployment Runs on Relativity’s platform, inside Relativity’s ecosystem and datacenter. Runs on your own private cloud, datacenter, and/or machines

Observability and troubleshooting Access to logs through the Log Extractor tool. Access to any observability tools that you use.

Maintainability Code must be kept updated multiple times each year as Relativity’s implementation continues to evolve Domain driven; stable abstractions allow integrations to remain unchanged for years at a time.

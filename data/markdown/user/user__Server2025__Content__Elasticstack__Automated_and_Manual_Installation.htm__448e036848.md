---
title: "Automated and Manual Installation"
url: https://help.relativity.com/Server2025/Content/Elasticstack/Automated_and_Manual_Installation.htm
collection: user
fetched_at: 2026-06-22T06:11:03+00:00
sha256: 7e690af4f2e917328eaf460a8b7500059174b7fd4b9791ea438afae9aa60097e
---

Automated and Manual Installation

# Automated and Manual Installation

## Overview

You can install Elastic Stack in a Relativity Server environment using either:

- Automated installation (recommended)

- Manual installation

Automated installation via the Relativity Server CLI is currently in Beta and supports single-node deployments only. For multi-node deployments, use manual installation. Automated multi-node support is planned for a future release.

Automated installation uses Relativity-provided automation to install and configure Elastic Stack with recommended defaults. Manual installation is available when you need to install or configure components individually.

## Automated Elastic Stack installation

Automated installation uses the Relativity Server CLI to install and configure Elastic Stack, applying Relativity-recommended defaults.

It performs the following actions:

- Applies Relativity-recommended defaults for storage layout, security configuration, and services

- Installs and configures required Elastic Stack components

- Performs required setup and configuration tasks

- Reduces the amount of manual configuration required during installation

- Helps ensure a consistent and repeatable deployment experience

See Automated Elastic Stack installation for installation instructions.

## Manual Elastic Stack installation

Manual installation installs Elastic Stack components individually and lets you configure each one directly. It offers additional control and may be appropriate for environments that require:

- Custom installation workflows

- Independent management of Elastic Stack components

- Non-standard deployment architectures

Instructions are organized by component:

- Install Elasticsearch

- Install Kibana

- Install APM Server

---
title: "Worker manager server installation"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Worker_manager_server_installation/Worker_manager_server_installation.htm
collection: user
fetched_at: 2026-06-22T06:03:44+00:00
sha256: 2da300331a60879479ef633211338ccc78bedc34baba0c9f95e6757071387213
---

Worker manager server installation

# Worker manager server installation

The Relativity worker manager server provides flexible options for processing electronically stored information (ESI). Use this content to perform an Invariant installation in your environment. To install the Invariant database, queue manager, and workers, you'll use an installation input file to enter your preferences into a text file that the installer then uses to install the Invariant components.

- Invariant Database —this database is a queue used to track jobs submitted to Invariant.

- Queue Manager —the Queue Manager is responsible for adding jobs to the Invariant Database as well as removing them. It also assigns jobs to the Invariant workers.

- Workers —the workers execute specific subtasks or jobs assigned to them by the worker manager server.

We use the terms worker manager server and Invariant interchangeably throughout this site.

Even though Invariant is required for Relativity 9+, you are not required to purchase a Processing license unless you are using Processing.

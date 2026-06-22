---
title: "Processing system requirements"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/System_requirements/Processing_system_requirements.htm
collection: user
fetched_at: 2026-06-22T06:04:01+00:00
sha256: d9ff77f934238a37f87cca910b7560bab395f0eecff026df4e26b9fae6e603ad
---

Processing system requirements

# Processing system requirements

The following information displays the system requirements for the Processing infrastructure.

This documentation contains references to third-party software, or technologies. While efforts are made to keep third-party references updated, the images, documentation, or guidance in this topic may not accurately represent the current behavior or user interfaces of the third-party software. For more considerations regarding third-party software, such as copyright and ownership, see Terms of Use .

## Processing worker hardware specifications

The following table displays the hardware specifications for Processing workers. These requirements are determined by the number of workers needed to achieve a specified range of throughput (# of GB/day).

Worker Specifications

CPU 8 core

RAM 16 GB

Network 1 Gbps

Storage Windows Temp SSD recommended

Server Physical recommended *

Expected throughput 100-150 GB/day **

* The primary reason for using physical workers is for performance. The overhead from virtualization can cause degradation in performance, particularly during text extraction and other CPU-intensive operations. If you do choose to virtualize your workers, beware of over-committing resources on the host. If you have hyper-threading enabled on the host, you may need to allocate 16 vCPUs to each worker to achieve results similar to those in the Processing performance baselines.

** Processing source data and system load may impact performance.

### Worker manager server software requirements

In addition to meeting the processing system requirements, we recommend referring to the Worker manager server pre-installation steps for information about other required and optional software on the processing worker.

## Tier hardware requirements

The following table displays the supporting infrastructure per number of workers you want to deploy. Refer to an applicable tier to locate the necessary hardware components to complete your processing infrastructure.

Tier 1

Entry Level Environment

Tier 2

Mid Level Environment

Tier 3

Large Scale Environment

# of Workers 1–2 3–7 8+

GB/day (source data) 100–300 300–800 800+

Invariant (worker manager server) SQL Server

- Processor: 4 cores

- Memory: 16 GB

- Storage I/O (Gbps): 4

- Processor: 4 - 8 cores

- Memory: 32 GB

- Storage I/O (Gbps): 4–8

- Processor: 4 - 8 cores

- Memory: 64 GB

- Storage I/O (Gbps): 4–8+

File Server

- Commodity NAS

- 1+ Gbps network

- Dedicated NAS (write-back cache available)

- 4+ Gbps network

- Enterprise class NAS (SSD tier available)

- 10+ Gbps network

By default, when you install Relativity, each worker in your environment is designated to do all available work, processing and imaging.

## Required Microsoft Visual C++ redistributables

The following table breaks down which versions of Microsoft Visual C++ are required for which versions of Relativity/Invariant. Note that you are required to install each version of Microsoft Visual C++ only if you are upgrading to the Relativity/Invariant version listed and not if you are installing it for the first time.

Required Microsoft Visual C++ version (Redistributable x86 and x64)

Relativity/Invariant version 2010 2012 2013 2015

Server 2022/7.1.431.1 √ √ √ √

Server 2023/ 7.3.841.24 √ √ √ √

Server 2024/ √ √ √ √

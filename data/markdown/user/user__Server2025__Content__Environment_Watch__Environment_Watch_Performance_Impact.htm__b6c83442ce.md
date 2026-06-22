---
title: "Environment Watch Performance Impact"
url: https://help.relativity.com/Server2025/Content/Environment_Watch/Environment_Watch_Performance_Impact.htm
collection: user
fetched_at: 2026-06-22T06:18:04+00:00
sha256: 62746fe695213ea6c398c2773ae44298713bf6fdad4ec06c7df3f90bfdddf982
---

Environment Watch Performance Impact Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Environment Watch Performance Impact

## Overview

This document provides transparent information about the performance overhead Environment Watch introduces to standard Relativity workloads, based on testing conducted in a controlled, production-like environment. Actual performance may vary depending on workload characteristics, environment size, infrastructure configuration, and usage patterns.

## Performance Impact on Relativity Workloads

Environment Watch has been rigorously tested to ensure minimal impact on your Relativity operations. Here's what you can expect:

### Performance Results Summary

The results below reflect observed outcomes from internal testing and are provided for transparency. These results should not be interpreted as guaranteed performance improvements for all Environment Watch deployments.

Workload Category Impact Summary

Processing +8% faster Processing operations demonstrated improved performance across all stages. Inventory was 3-8% faster, Discovery results matched closely (within a minute variance), and Publish operations were up to 19% faster, resulting in an approximate 8% overall improvement.

Review (Conversion) +5% faster Review operations saw a modest 5% improvement, providing slightly faster document conversion without any workflow disruption.

Imaging & Production Stable (±4%) Imaging and production performance remained stable, with changes within a ±4% range, resulting in no meaningful impact to customer workflows.

Data Transfer +6% faster Data transfer operations showed performance improvements with Imports demonstrating ~10% faster performance on average, while Exports (excluding RIP Images Export) were ~1% faster on average, resulting in an approximate 6% overall improvement.

## Test Environment Specifications

### Server Configuration Summary

Server Role Quantity Specs

Web Servers 3 Standard D8s v5 (8 vCPUs, 32 GiB RAM)

Core Agent Servers 6 Standard D8s v5 (8 vCPUs, 32 GiB RAM)

Processing Workers 4 Standard D16ls v6 (16 vCPUs, 32 GiB RAM)

Data Grid Servers 3 Standard D8s v4 (8 vCPUs, 32 GiB RAM)

SQL Primary 1 Standard D8as v5 (8 vcpus, 32 GiB RAM)

SQL Invariant 1 Standard DS13 v2 (8 vcpus, 56 GiB RAM)

SQL Distributed 1 Standard DS14-8 v2 (8 vcpus, 112 GiB RAM)

Analytics Server 1 Standard D8s v4 (8 vCPUs, 32 GiB RAM)

Conversion Agent 1 Standard D8s v5 (8 vCPUs, 32 GiB RAM)

DtSearch Agent 1 Standard D8ls v5 (8 vCPUs, 16 GiB RAM)

RabbitMQ Server 1 Standard D8ls v5 (8 vCPUs, 16 GiB RAM)

PDF Server 1 Standard D8s v5 (8 vCPUs, 32 GiB RAM)

This comprehensive test environment, ranging from Small to Medium scale, mirrors typical production Relativity deployments and ensures our performance results are representative of real-world customer workloads.

## Conclusion

Environment Watch has demonstrated minimal to positive impact on Relativity workloads based on comprehensive testing in a controlled, production-like environment. Most operations showed performance improvements, with Processing, Data Transfer, and Review performing faster, while Imaging and Production workflows remained stable. Environment Watch is designed to deliver observability and monitoring capabilities with minimal overhead; however, actual performance results may vary based on customer-specific configurations, environment size, and workload characteristics.

On this page

- Environment Watch Performance Impact

- Overview

- Performance Impact on Relativity Workloads

- Performance Results Summary

- Test Environment Specifications

- Server Configuration Summary

- Conclusion


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

---
title: "Supported Elastic Stack Versions"
url: https://help.relativity.com/Server2025/Content/Elasticstack/Supported_Elastic_Stack_Versions.htm
collection: user
fetched_at: 2026-06-22T06:11:00+00:00
sha256: c7c6fa1141da223a6aa8f258c1eebbd9718322fd43e2618d409efaba23271141
---

Supported Elastic Stack Versions

# Supported Elastic Stack Versions

The following table lists the Elastic Stack versions supported by Relativity Server products.

If you are running DataGrid Audit and Environment Watch on a shared Elasticsearch cluster, the Environment Watch compatibility requirements apply.

Elasticsearch Version Data Grid Audit Environment Watch

9.1.3 Yes Yes

8.19.8 Yes Yes

7.17.x Yes (with caveats)* No

The following Elasticsearch versions have specific support and security considerations:

- Elasticsearch 8.17.3 includes a bundled dependency with known security vulnerabilities.

- Elasticsearch 7.17 has reached end of vendor support as of January 15, 2026 and has not been tested or certified by Relativity for Server 2025. While we are not aware of any issues running Elasticsearch 7.17 with Data Grid Audit, this version is no longer supported by Elastic.

To ensure ongoing security, stability, compatibility, and supportability, Relativity strongly recommends upgrading to the latest supported Elasticsearch version.

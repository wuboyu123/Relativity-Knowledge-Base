---
title: "Relativity Data Grid"
url: https://help.relativity.com/Server2025/Content/Relativity/Data_Grid/Relativity_Data_Grid.htm
collection: user
fetched_at: 2026-06-22T06:12:21+00:00
sha256: a2902f8e27b9ae9c3d057c69259e7aff7195ae4e235097adc1c6addf67fcfa7b
---

Relativity Data Grid

# Relativity Data Grid

Relativity Data Grid allows you to store, search, and analyze extracted text and audit data at massive scale. Data Grid enables faster workflows through continuous indexing and distributed search to gain deeper insight to your extracted text and audit data. The benefits of using the Data Grid data store include:

- Scalability and more efficient review workflows on large case sizes and audits.

- More performant database maintenance, backup, and upgrades.

- A reduction in SQL server database sizes, leading to better performing SQL databases.

- Increased visibility into reviewer productivity and system performance.

Data Grid uses Elasticsearch to store and search audits.

Text or audit information stored in Relativity Data Grid is inaccessible for some third-party applications. It's recommended that you contact any vendors of third-party applications to confirm their compatibility with Relativity Data Grid.

This page provides a brief description of Data Grid terminology, functionality, and important considerations to take into account before implementing Data Grid for new workspaces .

Data Grid supports Windows servers only.

This page contains the following sections:

- Getting started

- Hardware and system requirements

- Relativity Data Grid

See these related pages:

- Installing Data Grid

- Infrastructure planning considerations

## Getting started

Use the following workflow to get started with Data Grid.

## Hardware and system requirements

The following table describes the hardware and system requirements per Data Grid feature.

Storage Audit

Hardware requirements Fileshare

Elasticsearch

System requirements Per Relativity specification For more information about system requirements and infrastructure recommendations, see Elasticsearch system requirements .

## Supported and unsupported functionality

The following sections describe supported and unsupported functionality for Data Grid.

### Storage (as compared to SQL storage)

To store text in Data Grid, you can use the same default file share as your natives and images, or you can designate a file share specifically Data Grid text. Once you enable a long text field's access to Data Grid, you can't disable it, so it's important to understand the benefits and limitations of storing text in Data Grid.

When you ARM restore to RelativityOne, extracted text is automatically stored in Data Grid.

Supported extracted text functionality Currently unsupported functionality

- Import/export through the Relativity Desktop Client

- Viewer

- Preview

- OCR

- dtSearch indexing and searching

- Persistent highlight sets

- Processing

- Integration Points

- Analytics

- ARM

- Keyword search

- SQL queries to long text fields stored in Data Grid

- Adding extracted long fields stored in Data Grid to layouts (including the Document panel)

- RSAPI query

- Pivot and Sort in the UI

- Filtering in the Document list on extracted text

- Mass operations:

- Edit

- Replace

- Tally/Sum/Average

- Export to File

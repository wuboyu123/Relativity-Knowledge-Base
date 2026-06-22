---
title: "Analytics billable estimate"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Analytics_billable_estimate.htm
collection: user
fetched_at: 2026-06-22T06:15:06+00:00
sha256: 564b18d7f6eff90dcf424c968c43011271e0940192cdea8124ef23a5c7889d3c
---

Analytics billable estimate

# Analytics billable estimate

This script allows a partner to assess the billable size of a potential Analytics index submission. This script allows a user to select a saved search, and returns the total number of native documents, the total number of image documents, the total number of text only documents, and the total file size of documents which are not already part of an Analytics index or structured analytics set.

## Special considerations

- This script must be run from a workspace.

- Documents already included in an Analytics index and structured analytics sets are not reported on during the execution of this script.

## Inputs

- Create a saved search that returns the documents you would like to index. No special fields are required.

- Navigate to the Scripts tab.

- Select the Relativity Analytics Billing Estimate script. If the script is not present in the workspace's script tab, you must add it.

- Click Run .

- Select the saved search created in step 1.

- Click Run .

## Results

The following fields are returned:

- Document Total

- Documents with Natives

- Documents with Images

- Documents with Text Only

- Total Billable Size in GB

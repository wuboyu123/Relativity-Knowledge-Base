---
title: "dtSearch index auto incremental build"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/dtSearch_index_auto_incremental_build.htm
collection: user
fetched_at: 2026-06-22T06:15:19+00:00
sha256: 6d8e36baf18b05d72651c3368dcb2d81378efeba67c7ae684edd2f568e2430b2
---

dtSearch index auto incremental build

# dtSearch index auto incremental build

This Relativity script runs a dtSearch incremental build on all dtSearch indexes in your environment. This is a system functionality script to be run over a Relativity environment. You can view instructions for downloading and running the script from the Relativity Community .

## Special considerations

Consider the following when running this script:

- This script can't be undone.

- The script may run for some time without reporting any progress.

- The script won't incrementally build any dtSearch index that has an invalid search specified as its Searchable Set. This includes a private search or a search associated with a deactivated search provider.

- The dtSearchIndexJob table on the EDDS database is populated with the dtSearch jobs for the dtSearch agent to run.

## Results

The dtSearch Indexes of all cases are incrementally built. There is no returned output for this script.

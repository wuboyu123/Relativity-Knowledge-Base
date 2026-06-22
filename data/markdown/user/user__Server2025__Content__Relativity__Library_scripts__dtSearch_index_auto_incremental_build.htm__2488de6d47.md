---
title: "dtSearch index auto incremental build"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/dtSearch_index_auto_incremental_build.htm
collection: user
fetched_at: 2026-06-22T06:15:19+00:00
sha256: 6d8e36baf18b05d72651c3368dcb2d81378efeba67c7ae684edd2f568e2430b2
---

dtSearch index auto incremental build Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

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

On this page

- dtSearch index auto incremental build

- Special considerations

- Results


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

---
title: "Multiple object searching"
url: https://help.relativity.com/Server2025/Content/Relativity/Searching/Multiple_object_searching.htm
collection: user
fetched_at: 2026-06-22T06:07:32+00:00
sha256: 309408c17c15126c6463e2347962fa96b1be8e21db39976d3f8b9fd34a73b6c8
---

Multiple object searching Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Multiple object searching

This page describes the logic behind multiple object searching.

When searching using These Conditions or NOT These Conditions, keep in mind the following:

- These Conditions - returns a document if any of the RDOs that document is associated with matches the search criteria.

- NOT These Conditions - returns all documents that are not associated with at least one RDO that meets the criteria.

- If a document is not associated with the object you're searching, it won't be returned in a search for These Conditions. Therefore, Document 3 will never get returned in a search for These Conditions because it is not associated with any objects.

The image below shows documents associated with Relativity Dynamic Objects (RDOs).

- Document 1 is associated with RDO1.

- Document 2 is associated with RDO2 and RDO3.

- Document 3 is not associated with any RDOs.

- Document 4 is associated with RDO4.

This page contains the following sections:

- These Conditions

- These Conditions and These Conditions

- NOT These Conditions

- These NOT

## These Conditions

The following example returns Document 1 because:

- Document 1 is associated with RDO1.

- RDO1 matches the search criteria (FirstName Jane, LastName Smith).

## These Conditions and These Conditions

The following example returns Document 1 and Document 2 because:

- Document 1 is associated with RDO1.

- RDO1 matches the search criteria (FirstName Jane) and (LastName Smith).

- Document 2 is associated with RDO2 and RDO3.

- RDO2 matches the search criteria (FirstName Jane).

- RDO3 matches the search criteria (LastName Smith).

## NOT These Conditions

The following example returns Document 3 and Document 4 because:

- Document 4 is associated with RDO4. RDO4 doesn't match the search criteria.

- Document 3 is not associated with any RDOs. Therefore, it doesn't match the search criteria.

## These NOT

The following example returns Document 2 and Document 4 because:

- Document 2 is associated with RDO2 and RDO3.

- Although RDO2 contains (FirstName Jane), RDO3 doesn't (FirstName John). Remember, if one RDO does not meet the criteria, the document is returned.

- Document 3 isn't returned because it isn't associated with any RDOs. Remember, you must associate a document with an object in order for it to return in a These Conditions search.

On this page

- Multiple object searching

- These Conditions

- These Conditions and These Conditions

- NOT These Conditions

- These NOT


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

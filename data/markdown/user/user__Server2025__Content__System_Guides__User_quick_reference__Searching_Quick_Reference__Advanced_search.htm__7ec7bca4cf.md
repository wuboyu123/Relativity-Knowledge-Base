---
title: "Advanced search quick reference guide"
url: https://help.relativity.com/Server2025/Content/System_Guides/User_quick_reference/Searching_Quick_Reference/Advanced_search.htm
collection: user
fetched_at: 2026-06-22T06:10:15+00:00
sha256: c9f388e3f75b5352e35e1c79ee8f9d8ed22befe0abaaf4a682406b1f3bdd6ec5
---

Advanced search quick reference guide Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Advanced search quick reference guide

When setting up a workspace in Relativity, admins need to consider what fields to search, which search indexes provide the most value, and how to optimize performance for the users (with minimal administrative overhead.)

This guide does not cover Analytics indexes, nor will it detail the operators acceptable for use in each of these search engines.

Search type Keyword search dtSearch

How is it enabled?

Relativity automatically indexes keyword searches when you load data into the system.

The Active field should read Yes. (Search Indexes > Keyword Search)

To access a dtSearch, you must first create a saved search. Search only on the Extracted Text field for optimal results.

Next, used the saved search as the Searchable Set when creating a dtSearch index.

What can be indexed? Available on all fields loaded into Relativity.* Available on all fields loaded into Relativity. See “Suggested Fields to be Indexed” below.

How is it used?

In the Documents tab:

-

Click Add Condition.

-

Click (Index Search).

-

Select Keyword Search from the drop-down menu.

-

Enter search terms.

-

Click Apply.

See the Searching Quick Reference for more details on available search operators.

In the Documents tab:

-

Click Add Condition.

-

Click (Index Search).

-

Select dtSearch from the drop-down menu.

-

Enter search terms.

-

Enable Fuzziness or Stemming, if necessary.

-

Click Apply.

See the Searching Quick Reference for more details on available search operators

*Except long text fields stored in Data Grid. In RelativityOne, extracted text is automatically stored in Data Grid.

## Common search scenarios

Leveraging the above search index knowledge, use the matrix below to reference behavior across common search scenarios and learn suggested index tips.

Keyword/Filters dtSearch

Engine SQL dtSearch

Noise words Yes Yes (customizable)

Search operators https://help.relativity.com/RelativityOne/Content/System_Guides/User_quick_reference/Searching_Quick_Reference/Searching_Quick_Reference.pdf

How to index https://help.relativity.com/RelativityOne/Content/System_Guides/User_quick_reference/Searching_Quick_Reference/Searching_Quick_Reference.pdf

When adding data (Add new records) Automatically updates Incremental build

When changing existing data (Overlay on existing records) Automatically updates Full build

When removing data (Remove existing records) Automatically updates Full build

Suggested fields to be indexed Fixed length fields: Some long text fields with small amounts of text (ex: File Names) that are not indexed by dtSearch Index Long text fields (ex: Extracted Text, Email To, Email CC.)

Suggested indexes N/A (not all fields flagged for indexing are grouped in an index.)

-

One for Extracted Text

-

One for Email To, Email CC, Email BCC

Searching on individual fields Yes (select the individual field to search or filter on.) Yes (set up separate Indexes that index individual fields.)

Advantages

- Instantaneous indexing,

- Ability to search on individual fields.

-

Ability to customize index

-

Ability to search on individual fields (involves separate index setup)

Disadvantages

- Lacks specialized search capabilities

- Inability to customize indexes

Manual index maintenance

**Only available on Data-Grid-Enabled Workspaces

## Is Like and Contains operators on field level searching

Is Like Contains

Behavior Wildcard (%) is applied to the front and back of the term. The field searches for the item entered.

Operators available None AND, OR, NOT, and Wildcard (%)

Multiple terms Terms entered on multiple lines are connected by an OR. Terms entered on multiple lines are connected by AND.

“Include in Text Index” Field does not need to be set to “Yes.” Only available for Fixed Length and Long Text Fields and needs to be set to “Yes.”

Comments Tends to run slowly. The best practice is to avoid running on large data sets N/A

For example, you see the term “Valet Parking” appear the following ways using the various search operators listed below:

“Valet parking” Exact phrase “Valet parking” Exact phrase “Valet parking”

Valet parking %valet parking% Valet AND parking

Valet park% %Valet park% Valet” AND “park%”

Valet park* %Valet park% “Valet” AND “park*”

Valet park%% %Valet park% “Valet” AND “park%%

On this page

- Advanced search quick reference guide

- Common search scenarios

- Is Like and Contains operators on field level searching


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

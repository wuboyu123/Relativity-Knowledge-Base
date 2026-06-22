---
title: "Structured Analytics"
url: https://help.relativity.com/Server2025/Content/Relativity/Analytics/Structured_analytics_set_tab.htm
collection: user
fetched_at: 2026-06-22T06:04:28+00:00
sha256: b92a2f134182972db16619f34f0776d70a0b70ec9c829f368ee29156a9fa7853
---

Structured Analytics Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Structured analytics

Structured analytics operations analyze text to identify the similarities and differences among the documents in a set.

Use structured analytics to quickly assess and organize a large, unfamiliar set of documents. On the Structured Analytics Set tab, you can run structured data operations to shorten review time, improve coding consistency, optimize batch set creation, and improve Analytics indexes.

See these related pages:

- Running structured analytics

- Email threading

- Name normalization

- Textual near duplicate identification

- Language identification

- Repeated content filters

## Structured analytics operations

Structured analytics consists of several operations that group documents based on their content, analyze that content, or create tools to more effectively filter content. You can run any or all of these operations on the same set of documents.

The operations are:

- Email threading :

- Determines the relationships among email messages by grouping related email items together.

- Identifies inclusive emails, which contain the most complete prior message content, and can bypass redundant content.

- Applies Email thread visualization to visually show replies, forwards, file types, and more. Visualization makes it easier to find the beginning and end of an email chain and track its progression.

- Name normalization :

- Identifies aliases within email headers. These include proper names, email addresses, and so on.

- Groups together aliases that refer to the same person, distribution group, and so on. These groups become entities.

- Textual near duplicate identification :

- Identifies documents that are textual near duplicates, meaning that most of their text appears in other documents in the group and in the same order.

- Returns a percentage value showing the level of similarity between documents.

- Language identification :

- Identifies the primary and secondary languages in each document. See the Supported languages matrix for a complete list of languages it can detect.

- Provides the percentage of the message text that appears in each detected language.

- Repeated content identification :

- Analyzes the linked text field to identify repeated content at the bottom of documents, such as email footers and signatures.

- Returns a repeated content filter, which you can apply to an Analytics index to improve Analytics search results.

These operations have several benefits:

Operation Optimizes batch set creation Improves coding consistency Optimizes quality of Analytics indexes Speeds up review

Email threading √ √ √

Name normalization √ √ √

Textual near duplicate identification √ √ √

Language identification √ √

Repeated content identification √ √

## Structured analytics versus conceptual analytics

Structured analytics and conceptual analytics are different from each other in several ways. Depending on your needs, one or the other may work better for you.

Structured analytics Conceptual analytics

Groups documents that have similar content, but may or may not have similar concepts Groups documents that have similar concepts, even if the words are different

Takes word order into consideration Does not consider word order

Takes into account the placement of words and looks to see if new changes or words were added to a document Uses Latent Semantic Indexing (LSI), which focuses more on concepts than on specific wording changes

Uses a structured analytics set, not an index Uses an Analytics index

## Setting up your environment

To use structured analytics within Relativity, you must have the Analytics application installed in your workspace. Installing the application will create an Indexing & Analytics tab, along with several new fields.

Because this adds some relational fields, we recommend installing the application during a low activity time via the Applications Library admin tab. For more information, see Installing applications .

After you have installed the application to at least one workspace, you must also add the Structured Analytics Manager and Structured Analytics Worker agents to your environment. For steps to add agents, see Adding and editing agents . Additionally, the workspace's resource pool must have at least one Analytics server with the Analytics operation Structured Data Analytics enabled. See Servers for more information.

Relativity template workspaces already have the Analytics application installed by default.

On this page

- Structured analytics

- Structured analytics operations

- Structured analytics versus conceptual analytics

- Setting up your environment


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

---
title: "Textual near duplicate identification"
url: https://help.relativity.com/Server2025/Content/Relativity/Analytics/Textual_near_duplicate_identification.htm
collection: user
fetched_at: 2026-06-22T06:05:13+00:00
sha256: 9e9c2dba2a53ef1113fe3143032f9715a184fdc885dcda1a900e717ed674e050
---

Textual near duplicate identification Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Textual near duplicate identification

Textual near duplicate identification scans the text of documents to find near matches. This makes it easier to tell at a glance whether two documents have minor or major differences.

This page talks about how textual near duplicate identification works. For steps to set it up, see Running structured analytics .

See the following related pages:

- Textual near duplicate identification results

- Structured analytics

- Running structured analytics

## Textual near duplicate identification overview

Textual near duplicate identification goes through a several-step process to identify document similarities:

- It takes the contents of all documents with 30 MB or less of text in the field you choose to analyze. This defaults to the Extracted Text field, but you can change it under Select field to analyze when setting up the structured analytics set.

- It scans the text and saves various statistics for later comparisons. The task operates on text only (which has been converted to lowercase). White space and punctuation characters are also ignored, except to identify word and sentence boundaries.

- The documents are sorted by the word count of the field being analyzed, in order from largest to smallest. This is also the order in which they are processed.

The most visible optimization and organizing notion is the principal document. The principal document is the document in a group with the most words. The analysis compares all other documents to the principal document to determine whether they are near duplicates. If the current document is a close enough match to the principal document—as defined by the Minimum Similarity Percentage—it is placed in that group. If no current groups are matches, the current document becomes a new principal document.

Analyzed documents that are not textually similar enough to any other documents will not have fields populated for Textual Near Duplicate Principal or Textual Near Duplicate Group. Documents that only contain numbers or that do not contain text will have the Textual Near Duplicate Group field set to numbers-only or empty, respectively.

- When the process is complete, only principal documents that have one or more near duplicates are shown in groups.

- Documents that have the Textual Near Duplicate Group field set to empty or numbers-only are also grouped together.

- Documents that are not textually similar to any other documents in your analysis group, based on the minimum similarity percentage chosen, end up as “standalone” documents that do not belong to a near duplicate group.

### How the principal document is determined

When the analysis job runs, it sorts the documents by word count, then chooses the document with the most words to be the principal document in a group. This may be different from the document with the most characters or the largest file size.

The word separation process can produce non-intuitive results. For example, the @ symbol is considered a word delimiter, so "alice.apple@appletown.gov" would count as two words: "alice.apple" and "appletown.gov."

## Minimum Similarity Percentage

The Minimum Similarity Percentage parameter controls how the task works. This parameter indicates how similar a document must be to a principal document to be placed into that principal's group. A value of 100% would indicate an exact textual duplicate. A higher setting requires more similarity and generally results in smaller groups. A higher setting also makes the process run faster because fewer comparisons have to be made.

## Fields

The following fields are created when you run textual near duplicate identification:

- <Structured Analytics Set prefix>::Textual Near Duplicate Principal - identifies the principal document with a "Yes" value. The principal is the document in the duplicate group with the most words. It acts as an anchor document to which all other documents in the near duplicate group are compared. If the document does not match with any other document in the data set, this field is set to No.

- <Structured Analytics Set prefix>::Textual Near Duplicate Similarity - the percent value of similarity between the near duplicate document and its principal document. If the document does not match with any other document in the data set, this field is set to 0.

- <Structured Analytics Set prefix>::Textual Near Duplicate Group - this is the field that acts as the identifier for a given group of textual near duplicate documents. If the document contains text but does not match with any other document in the data set, this field is empty. Documents that only contain numbers or that do not contain text will have the <Structured Analytics Set prefix>::Textual Near Duplicate Group field set to Numbers Only or Empty, respectively.

On this page

- Textual near duplicate identification

- Textual near duplicate identification overview

- How the principal document is determined

- Minimum Similarity Percentage

- Fields


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

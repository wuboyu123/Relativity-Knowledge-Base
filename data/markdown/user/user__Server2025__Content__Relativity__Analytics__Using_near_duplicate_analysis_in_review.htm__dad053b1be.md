---
title: "Using Near Duplicate Analysis in Review"
url: https://help.relativity.com/Server2025/Content/Relativity/Analytics/Using_near_duplicate_analysis_in_review.htm
collection: user
fetched_at: 2026-06-22T06:05:18+00:00
sha256: 4e52d2add6c92d21cb489c2f83360981a1c79b92fd393ac17ea4249b804e1691
---

Using Near Duplicate Analysis in Review Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Using near duplicate analysis in review

Relativity can identify textually similar documents to assist in and speed up the review process. Near duplicate analysis is best suited for grouping documents which can then be batched for review based on the similarity, or used to create new document sets for further analysis. The goal is for reviewers to have the ability to see similar documents at the same time based on their textual similarity.

## Near duplicate analysis overview

- Textual near duplicate identification sorts documents by the word count of the field being analyzed, then checks them for similarity to one another. It groups similar documents together and labels the group member with the most words as the principal document. For more details, see Textual near duplicate identification .

- When you set up a textual near duplicate identification job, you choose a Minimum Similarity Percentage. This percentage determines how similar a document must be to a principal document to be placed into that principal's group.

- After running the analysis, system admins can view the Textual Near Duplicates Summary on the set’s Structured Analytics console. This summary shows how many textual near duplicate groups have been identified, the average percentage of similarity, and number of documents per group.

## Creating a textual near duplicates view

System admins should create a Textual Near Duplicates (TND) view for the review team. This view will contain only documents that appear in TND groups, not documents which were submitted to the engine but found to be non-matches.

- In the Near Duplicate Identification view, add the following output fields (assuming the Structured Analytics Set was run with a prefix of “S1” and the S1::Textual Near Duplicate Group was mapped to a relational field called “Textual Near Duplicate Group”):

- S1:: Textual Near Duplicate Principal - identifies the principal document with a "Yes" value. The principal is the document in the duplicate group with the most words. It acts as an anchor document to which all other documents in the near duplicate group are compared.

- S1:: Textual Near Duplicate Similarity - the percent value of similarity between the near duplicate document and its principal document. If “ignore numbers” is set to “true”, this percentage considers only tokens (i.e. words) beginning with letters. Punctuation and whitespace are ignored, but word order is considered.

- Textual Near Duplicate Group - the identifier for a given group of textual near duplicate documents. This is a relational field which provides relational capabilities. However, you can map S1::Textual Near Duplicate Group to any relational field when you set up the Structured Analytics Set.

- Add a condition to only show documents where the Textual Near Duplicate Group field is set.

- Set the following sort orders on the Near Duplicate Identification view to list the textual near duplicate principals with the highest percentage of textual near duplicate similarity at the top:

- Textual Near Duplicate Group - Ascending

- S1::Textual Near Duplicate Principal - Descending

- S1::Textual Near Duplicate Similarity - Descending

- On the Other tab, set the Group Definition to Textual Near Duplicate Group . This ensures that bold blue bars will appear between each group.

### Using the TND view in review

You can use the grouping and similarity values in the TND view to speed up the review process. The Relativity Compare function can compare two documents to assess their similarities and differences.

Reviewers will be able to view documents that are extremely similar but not identical to each other. For example, the case team may need to ensure a series of very similar reports are coded the same way. Another possible use is to help locate additional privileged documents that might have been missed during first pass review. In situations like these, it is common to use a view that displays textual near duplicates. Note that exact word order is analyzed during this analysis, though punctuation and whitespace are not.

### Example

Consider the following example. The first document, BF000001, is the group’s principal, as indicated by the “Yes” value in the S1::Textual Near Duplicate Principal field. It has a score of 100 (as do all principals). Not all documents with a score of 100 are necessarily principals, however. The next three documents are part of BF000001’s relational group. The second document (JA060020) is identical to the principal. We know this because it is 100% similar, as shown in the S1::Textual Near Duplicate Similarity field. The last two documents (TJ000006 and JM00002) are very closely similar to the principal but are not exact duplicates; their scores indicate they are each 97% similar to the principal.

## Workflow considerations

Textual near duplicate groups have a relational field that can be used to code several documents at once. Documents contained in the near duplicate group are textually similar, but similarity is usually not enough to treat near-duplicates as identical documents for the purposes of review. As such:

- It is not recommended to propagate coding on near duplicates, unless other analysis or evidence points to their similarity to justify such a step.

- It is not recommended to delete or otherwise shelve near duplicates. However, focusing just on the principal document of each group can make sense in certain early-stage workflows, such as clustering to understand conceptuality of a data set, training an Active Learning classifier, or other types of investigative work. We do advise that you proceed with caution, and ensure that you are not misrepresenting your data when you conduct such a workflow.

On this page

- Using near duplicate analysis in review

- Near duplicate analysis overview

- Creating a textual near duplicates view

- Using the TND view in review

- Example

- Workflow considerations


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

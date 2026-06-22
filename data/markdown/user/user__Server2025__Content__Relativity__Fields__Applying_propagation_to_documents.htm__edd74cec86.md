---
title: "Applying propagation to documents"
url: https://help.relativity.com/Server2025/Content/Relativity/Fields/Applying_propagation_to_documents.htm
collection: user
fetched_at: 2026-06-22T06:14:40+00:00
sha256: 67dc209da69bcabedbcc0e385adfefed6547f7fbbfb3b0cd959af6078af053e2
---

Applying propagation to documents Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Applying propagation to documents

The propagation function can help enhance your document review workflow to save time spent coding documents. For example, you can tag a document as Responsive and have the value propagate to that document’s family members.

To enable propagation, toggle Propagation on. Click the icon in the Propagate To row. The available options depend on the relational fields set for the workspace.

When you code a document in a field on which propagation is enabled, the propagation function automatically codes related documents with the same value. Click Save or Save & Next in the layout to apply the field propagation rules.

Propagation works on all document object field types. Associative Object Lists do not work with propagation.

Propagation doesn't cascade or cause chain reactions, meaning that only the documents in the saved document’s groups receive the propagated values. For example, if you create a responsiveness field to propagate both family and duplicates, and you code a parent email as Responsive, these actions occur:

- Family propagation - codes child email attachments as responsive

- Duplicate propagation - codes duplicate emails of the parent as responsive

Duplicates of the child attachments aren't coded as responsive. This action would be a duplicate propagation triggered by family propagation.

## Propagating to documents in multiple groups

When you code a document that's a member of multiple related groups – for example, Duplicates and Email Families – it's important to understand how coding decisions propagate in specific scenarios.

The following scenarios illustrate how propagation applies to a set of documents. Assume that propagation is active for both email families and duplicates.

There are two email families:

- AS000001 – AS000005

- TS000007 – TS000011

Within these families, two documents are duplicates:

- AS000003

- TS000009

Coding AS000001 as Responsive tags only the family, shown in blue.

Coding AS000003 as Responsive tags the family, and the duplicate, shown in blue.

Mass editing AS0000001 and AS000002 as Responsive tags only the family, shown in blue.

Mass editing AS000002 and AS000003 as Responsive tags the family and the duplicate, shown in blue.

Mass editing AS000003 and TS000009 as Responsive tags all of the listed documents.

On this page

- Applying propagation to documents

- Propagating to documents in multiple groups


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

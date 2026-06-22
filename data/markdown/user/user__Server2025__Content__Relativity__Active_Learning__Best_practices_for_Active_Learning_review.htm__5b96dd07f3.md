---
title: "Best practices for Active Learning review"
url: https://help.relativity.com/Server2025/Content/Relativity/Active_Learning/Best_practices_for_Active_Learning_review.htm
collection: user
fetched_at: 2026-06-22T06:08:24+00:00
sha256: 9b930748f5abdde39060529648a80d1ca190749b262769207675534f821582f7
---

Best practices for Active Learning review Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Best practices for Active Learning review

This article is intended as a reference for reviewers in an Active Learning project. We’ve included best practices and overall considerations for working with computer-assisted review.

For more in-depth information on Active Learning, see Assisted Review .

## General coding tips

We recommend the following guidelines when reviewing documents:

- Consistency is crucial - consult fellow reviewers on difficult coding decisions to make sure your team is coding consistently.

- Double check - always check the extracted text of a document to be sure it matches the content in other views. Whenever possible, review from the Extracted Text viewer.

- When in doubt, ask - if something confuses you, don't guess. Ask a system admin or project manager about the right course of action.

## Coding according to the "four corners" rule

Active Learning predicts which documents will be responsive or nonresponsive based on the contents of the document itself. Family members, date range, custodian identity, and other outside factors do not affect the rankings. Because of this, the Active Learning engine learns best when documents are coded based only on text within the four corners of the document.

When you code documents as positive or negative in the Active Learning queue, you are both coding the document and teaching the engine what a responsive document looks like. Therefore, your positive or negative coding decisions should follow the "four corners" rule: code only based on text within the body of the document, not based on surrounding factors.

Having one or two documents that fail this rule will not harm the overall accuracy of Active Learning's predictions. However, if you want to track large numbers of documents which are responsive for reasons outside of the four corners, we recommend talking to the project manager about either setting up a third, neutral choice on the coding field for those, or adding a secondary coding field. Neutral choices and other coding fields are not used to train the Active Learning engine.

### Common scenarios which fail the "four corners" rule

The following scenarios violate the "four corners" rule, and will not train the Active Learning engine well:

- The document is a family member of another document which is responsive.

- The document comes from a custodian whose documents are presumptively responsive.

- The document was created within a date range which is presumptively responsive.

- The document comes from a location or repository where documents are typically responsive.

For example, the following email has a responsive attachment. However, the body of the email—the text within the four corners—is only a signature and a privacy disclaimer. Because the body of this email is not responsive, this document does not pass the "four corners" rule.

## Factors which affect Active Learning predictions

Not all responsive documents will inform the Active Learning engine equally. The following factors affect how much the engine will learn from each document:

-

Sufficient text - if there are only a few words or short phrases in a document, the engine will not learn very much from it.

-

Email headers and signatures - these are filtered out automatically by Active Learning. They are still visible, but they are not considered for Active Learning's predictions.

-

Images - text contained only in images, such as a photograph of a contract, cannot be read by Active Learning. The system works only with the extracted text of a document.

-

Numbers - numbers are not considered by the Active Learning engine.

On this page

- Best practices for Active Learning review

- General coding tips

- Coding according to the "four corners" rule

- Common scenarios which fail the "four corners" rule

- Factors which affect Active Learning predictions


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

---
title: "Choosing an Active Learning review queue"
url: https://help.relativity.com/Server2025/Content/Relativity/Active_Learning/Choosing_an_Active_Learning_review_queue.htm
collection: user
fetched_at: 2026-06-22T06:08:03+00:00
sha256: df56ea328b382e1f2b8a76450ce303f342ef6bd96ea6592fdc3eaddf6dc4a9aa
---

Choosing an Active Learning review queue Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Choosing an Active Learning review queue

Once you've created an Active Learning project, you're redirected to the Project Home tab. From here, you can view a dashboard with information about your project and select an Active Learning review queue to start your review. For more information about the Project Home dashboard, see Monitoring an Active Learning project .

There are two types of review queues in Active Learning: Prioritized Review and Coverage Review. An Active Learning workflow starts in either the Prioritized Review or Coverage Review queue, moving to the Project Validation queue when the project is nearing completion. See below for a description of the review queues.

## Prioritized Review

The Prioritized Review queue serves the highest ranking documents, in other words, documents that are most likely to be coded on the positive choice (ex. Responsive). The goal of Prioritized Review is to quickly identify and review the most relevant documents in your set. If you are unsure which queue to select, we recommend using the Prioritized Review queue.

When coding documents in the Prioritized Review queue, a small set of documents are included for index health. The documents included for index health are system-selected to help the model develop a better range of training.

Use the Prioritized Review queue if:

- You need to quickly locate and review the most relevant (responsive) documents in your set.

- For example, a standard request for production with a need to do redaction and/or privilege review.

- You want to review relevant documents and their family together.

- You have a document set with lower richness. For information on estimating richness, see Creating an Active Learning project .

- You are unsure which queue to select.

For more information, see Running Prioritized Review .

## Coverage Review

Coverage Review serves up documents that are optimal for training the model. The goal of Coverage Review is to quickly separate your documents into the positive choice and negative choice categories. Unlike Prioritized Review, which serves up the highest ranking documents, Coverage Review is intended for quick production use cases where you want to train the model as fast as possible.

The documents that are served during Coverage Review can be either relevant or non-relevant and are chosen by the engine solely to train the model. Coverage Review serves up the documents the model is most unsure about. Coverage Review continues serving up documents until there are no longer any documents to review. However, you should stop reviewing documents much earlier, once the model has stabilized.

Use the Coverage Review queue if:

- You need to quickly classify your documents into relevant/not relevant sets.

- For example, to respond to HSR second request or if you have an incoming production.

- You have a large case and don't necessarily need to review and code every relevant document. For example:

- A government production request with a tight timeline.

- An internal investigation where you are mining for information for your own benefit.

Coverage Review works best with document sets with greater richness (>2%).

For more information, see Running Coverage Review .

On this page

- Choosing an Active Learning review queue

- Prioritized Review

- Coverage Review


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

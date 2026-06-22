---
title: "Solving review case challenges with Analytics"
url: https://help.relativity.com/Server2025/Content/Solutions/Solving_review_case_challenges_with_Analytics/Solving_review_case_challenges_with_Analytics.htm
collection: user
fetched_at: 2026-06-22T06:05:40+00:00
sha256: 83aee08877023f9964774596cf4beb50f6dc3ee032c81e3d7630030f82a3552a
---

Solving review case challenges with Analytics

# Solving review case challenges with Analytics

Using Analytics speeds up review and identifies critical documents in a case by searching and quickly organizing document sets. Search results depend on how and where similar ideas and concepts in a document collection intersect. You can leverage Analytics throughout the review workflow to go faster and work smarter.

This page contains the following sections:

- Getting started with Analytics

- Going faster with Analytics

- Working smarter with Analytics

- Analytics resources

See these related pages:

- Implementing clustering and batching

- Implementing categorization

- Finding similar documents

- Using keyword expansion

## Getting started with Analytics

Analytics provides a powerful document searching and organizing toolset. Understanding real-world situations when Analytics cuts review costs, improves review speed, or aids in quickly identifying hot documents for a case is the key to unlocking the potential for Analytics to effectively improve your overall review process.

One common solution to case review challenges is implementing Analytics. To implement Analytics as a powerful solution for any case, the first required step is to create an Analytics index. See Creating an Analytics index.

You can use Analytics to:

- Go faster - Use Analytics to automatically cluster similar documents together. Organize discovery documents based on similarity to increase user doc-to-doc review speed and improve accuracy without changing your existing review workflow or requiring additional user input. The Analytics search engine does the additional work.

- Apply clustering to review a large number of documents with limited time and limited access to subject matter experts (SMEs). See Implementing clustering with batching .

- Apply categorization to identify and prioritize hot documents from opposing counsel. See Implementing categorization .

- Work smarter - Building the facts of a case is not always a linear process. With the average case today consisting of enormous numbers of documents, the task of following a pattern of thought within the documents quickly and effectively becomes increasingly difficult. Analytics provides tools to facilitate an investigative thought process despite a large number of case documents.

- Use Find Similar Documents to identify additional documents that match items in your Privilege log before producing documents for opposing counsel. See Finding similar documents .

- Use Keyword Expansion to identify relevant terms unknown at the start of a case review. See Using keyword expansion .

Analytics helps you move past discovery and tell a client's story by giving an overview of the document collection through clustering, helping users find similar documents with a right-click, allowing users to build example sets of key issues, and running advanced keyword analysis.

## Going faster with Analytics

Complete document reviews more efficiently by leveraging tools such as clustering and categorization. Clustering and categorization analyze and group documents together for you automatically. Grouping documents by conceptual relationships simplifies the review process and reduces the effort and resources required to complete document reviews.

The following example scenarios demonstrate the benefits of applying clustering and categorization to common document review scenarios you may encounter.

### Reviewing documents under time and SME constraints

The challenge: You must review a large number of documents quickly, for example approximately 40,000 documents, with limited time, and limited or no access to Subject Matter Experts (SME).

Factors and assumptions:

- Large number of documents (thousands, tens of thousands)

- Limited time to complete review

- Limited number of reviewers (fewer reviewers than normally required to perform a full manual review)

Solution: Clustering

Clustering groups conceptually similar documents together without the need for example documents. In this scenario:

- Use clustering to automatically organize documents into groups of related data.

- Batch documents and assign to reviewers based on the cluster groups.

- Bulk code groups of clustered documents

In some cases, you may find clusters of documents clearly irrelevant to your case, such as spam emails. Instead of reviewing hundreds, maybe thousands, of junk emails one at a time, reviewers can eliminate impertinent documents with minimal time, effort, or subject matter expertise.

For implementation steps, see Implementing clustering with batching .

### Identifying and prioritizing the opposition’s hot documents

The challenge: You received documents from opposing counsel and must identify the opposition's hot documents as soon as possible.

Factors and assumptions:

- Review of your own case documents is complete.

- Reviewed documents were coded with a multiple choice field for issues designation and set with a value of Hot when applicable.

Solution: Categorization

Categorization identifies and groups similar documents together based on a set of example documents. In this scenario, you will:

- Create a categorization set and use your designation multiple choice field as the categories and examples source.

- Click one button to use the Synchronize feature for your new categorization set.

- Click one button to categorize the opposing counsel's documents with your categorization set to identify opposing counsel documents similar to your Hot documents.

Setting the available Categories and Examples Source option to use your multiple choice designation field enables the Synchronize feature for categorization. The Synchronize feature automatically creates categories for all choices associated with the specified field and designates example records for all documents with this field coded. With the example document records identified in your data set, categorization identifies and organizes similar documents in the opposing counsel's data set.

For implementation steps, see Implementing categorization .

## Working smarter with Analytics

Analytics provides tools that help you find the needle in a haystack more efficiently. Find Similar Documents and Keyword Expansion allow you to hone in on the unknown in your case documents without the need for additional review resources.

The following example scenarios demonstrate the benefits of using Find Similar Documents and Keyword Expansion for the purpose of analyzing documents outside of the typical review process.

### Identifying additional privileged documents prior to production

The challenge: You must ensure that you identified all privileged documents possible in order to avoid producing privileged documents and giving them to opposing counsel.

Assumption: You've already identified a set of privileged documents.

Solution: Find similar documents

Use the following steps to locate documents conceptually related to previously identified privileged documents:

- Open a document from your current privilege log in the Documents view.

- Right-click on the document in the Viewer and click Find Similar Documents .

- Click to open each similar document from the Similar Documents pane on the left-hand side.

- Review the similar documents and add items to your privilege log as necessary.

For implementation steps, see Find similar documents .

### Identifying unknown relevant terms

The challenge: Your document set may contain unknown relevant terms you have not yet identified. You must research and identify any unknown relevant terms to organize the case data more accurately and improve the effectiveness of your document review.

Assumption: You've identified a starting list of keywords in your data set to expand upon.

Solution: Keyword expansion

Keyword Expansion identifies terms conceptually related to a specified word or highlighted text in a document. In this scenario, you will:

- Initiate a keyword expansion search for terms conceptually related to your current list of keywords using one of two methods:

- Open the Conceptual Keyword Expansion dialog from the Documents tab and perform your keyword search.

- In the viewer, highlight a keyword in a document and select Keyword Expansion from the Analytics right-click menu.

- Review the list of conceptually related keywords and identify additional relevant or potentially relevant terms.

Use the Conceptual Keyword Expansion search dialog to also perform keyword expansion searches on search results. Terms returned in your search results appear in the list with a hyperlink. Click the hyperlink to initiate a keyword expansion search for a selected term. Use this seamless process to build your list of relevant terms for your case.

For implementation steps, see Using keyword expansion .

## Analytics resources

### Documentation

See the complete Analytics guide.

### Educational resources

Analytics educational videos, tutorials, and webinars are available in the Training Center: https://www.relativity.com/relativity/ediscovery-resources/training.

### Support team

Support offers specialized Analytics workflow guidance with backgrounds consisting of extensive Relativity product knowledge, litigation support expertise, and custom development capabilities. To get in touch with someone for custom workflow development and implementation assistance, submit a request through the Customer Support form.

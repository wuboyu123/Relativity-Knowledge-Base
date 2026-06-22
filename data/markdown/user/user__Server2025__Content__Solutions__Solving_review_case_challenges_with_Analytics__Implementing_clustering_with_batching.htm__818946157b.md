---
title: "Implementing clustering with batching"
url: https://help.relativity.com/Server2025/Content/Solutions/Solving_review_case_challenges_with_Analytics/Implementing_clustering_with_batching.htm
collection: user
fetched_at: 2026-06-22T06:12:15+00:00
sha256: 78ae52453fde3bb231fd51d033699e096cfd0cf5921f27ba0052fff31e39f506
---

Implementing clustering with batching Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Implementing clustering with batching

The steps required to complete a large document review with limited time and limited access to subject matter experts involve creating document clusters automatically with Analytics, followed by batching documents for review based on the resulting clusters. The following sets of steps explain how to:

- Create document clusters

- Batch documents to users according to the clusters

You must have an Analytics index in order to use clustering. For information on creating Analytics index, see Analytics index.

## Creating clusters

To create a new cluster:

- Select the Documents tab.

- Select the container in which the documents to cluster reside:

- Select the top-level folder in the Folder browser to choose from all workspace documents.

- Select a subfolder in the Folder browser to choose from a specific subset of workspace documents.

- Select one of the following mass operation options:

- Checked - requires you to select target documents using the document checkboxes.

- All - includes all documents in the selected container.

- These - includes items in the current returned set.

- Select Cluster from the mass actions drop-down menu.

- Click Go .

- Select Create New Cluster for the Mode setting.

- Enter a cluster name in the Name field.

- Select an Analytics index that contains the selected documents for the Analytics Index setting.

- Click Submit for Clustering .

The Cluster Documents form also provides configuration control for advanced options, including maximum hierarchy depth, minimum coherence, and generality. See Clustering for details on these advanced clustering options.

### New fields

Creating a new cluster also creates the following new fields automatically:

- Multiple choice field with the naming convention Cluster :: clusterName —stores cluster node names.

- Decimal field with the naming convention Cluster :: clusterName :: Score —stores cluster score values.

The multiple choice and decimal fields created for each cluster allow you to:

- Search for documents contained in a specific cluster.

- Use the score threshold as search or view criteria.

- Add a cluster to the choice tree with the multiple choice field.

## Creating batches from clusters

In this scenario, the multiple choice field is the key ingredient in batching documents to reviewers based on clusters created by Analytics. The remaining steps only require the creation of a new saved search and a batch set in your workspace.

### Creating a new saved search

To create a new saved search:

- Select the Documents tab.

- Select the Saved Searches browser.

- Click New Search .

- Configure the new saved search with the following:

- Type a name in the Name field.

- Add a new condition in the Conditions section with the following settings:

- Field - select the new cluster multi-choice field, Cluster :: clusterName.

- Operator - select is set .

- Add the Cluster :: clusterName field to the list of included fields in the Fields section. Leave the default included fields: Edit, File Icon, and Control Number.

- Click Save.

### Creating a new batch set

To create a new batch set:

- Select the Batch Sets tab (Administration::Batch Sets).

- Click New Batch Set .

- Type a name in the Name field.

- In the Maximum Batch Size field, type a maximum number of documents to include in each batch.

- In the Batch Prefix field, type a batch numbering prefix. For example, CLS .

- Select the new saved search from the Batch Data Source drop-down menu.

- Select the Cluster :: clusterName field as the Batch Unit Field.

- Click Save.

- Click Create Batches on the Batch Set console.

## Assigning and coding

After completing a brief set of steps to create document clusters with Analytics, and to create document batches based on the clusters, you are ready to assign the batches to reviewers.

Since Analytics automatically clusters documents based on conceptual similarities, each batch may now potentially be bulk-coded with very little review effort from your review team.

On this page

- Implementing clustering with batching

- Creating clusters

- New fields

- Creating batches from clusters

- Creating a new saved search

- Creating a new batch set

- Assigning and coding


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

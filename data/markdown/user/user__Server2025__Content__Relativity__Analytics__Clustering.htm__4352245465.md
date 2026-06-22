---
title: "Clustering"
url: https://help.relativity.com/Server2025/Content/Relativity/Analytics/Clustering.htm
collection: user
fetched_at: 2026-06-22T06:05:31+00:00
sha256: 7e51c921e811ad118b2b5c42c4a0cf61af6781fb3e550b519a56aabbe3a64ae1
---

Clustering Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Clustering

Analytics uses clustering to create groups of conceptually similar documents. With clusters, you can identify conceptual groups in a workspace or subset of documents using an existing Analytics index. Unlike categorization, clustering doesn't require much user input. You can create clusters based on your selected documents without requiring example documents or category definitions. You can view the clusters identified by the index in the Cluster browser available on the Documents tab.

When you submit documents for clustering, the Analytics engine determines the positions of the documents in the conceptual index. Depending on the conceptual similarity, the index identifies the most logical groupings of documents and places them into clusters. Once the Analytics engine creates these clusters, it runs a naming algorithm to label each node in the hierarchy appropriately to refer to the conceptual content of the clustered documents.

Clustering is useful when working with unfamiliar data sets. However, because clustering is unsupervised, the Analytics engine doesn't indicate which concepts are of particular interest to you. Use investigative features such as Sampling , Searching , or Pivot in order to find the clusters that are of most interest.

Clustering doesn't perform conceptual culling of irrelevant documents, but there is a group created for documents without searchable text. The name of the group is UNCLUSTERED. This group can be used to find documents that don’t have enough searchable data. All documents with conceptual data get clustered somewhere once. Clustering may be used on any list of documents. For example: a saved search based on custodians, search term results, date ranges or the entire workspace.

After you've created clusters, you can use those clusters to create batches to speed up a linear review.

See these related pages:

- Cluster visualization

## Creating or replacing a cluster

You can create new clusters or replace existing ones. The steps for these tasks are similar, except that you need to select an existing cluster when you perform a replacement.

- You must have the add permission (for both field, Cluster Set, and choice objects) and the cluster mass operations permission to create or replace clusters.

- Permissions for the Cluster Set object and the multiple choice fields that hold cluster data should be kept in sync. Refer to the Cluster Set object description in Workspace permissions .

To automatically create a cluster when creating a conceptual index, leave the Cluster Documents option set to Yes. For more information, see the following:

-

Creating an Analytics index

-

Default settings for automatically created clusters

To manually create a new cluster or replace an existing one, perform the following steps:

- Navigate to the Documents tab and find the documents that you wish to cluster. This might be a saved search, folder, or all documents in the workspace.

- Select the documents you want to cluster. You can click the checkboxes of individual documents in the list and select Checked from the drop-down menu. Alternatively, you can select All to include all documents.

- Select Cluster from the Mass Operations drop-down menu.

The Cluster dialog displays.

- Complete the fields on the Cluster dialog. See Fields .

- Once you've completed the fields on the Cluster dialog, click Submit for Clustering . Relativity displays clusters in the Clusters browser.

### Fields

The following fields display on the Cluster window:

- Mode - determines whether this is a new cluster or a replacement

- Create New Cluster - creates a new cluster

- Replace Existing Cluster - replaces a cluster that already exists. See Replacing an existing cluster .

- Name - the name of the new cluster. If you are replacing an existing cluster this field becomes Cluster , in which you select the cluster you'd like to replace from a drop-down list of existing ones.

- Relativity Analytics Index - the Analytics index that is used to cluster your documents. The index you select here must have queries enabled for you to be able to submit the selected documents for clustering. All of the selected documents must be in the data source of this index; otherwise, they end up as Not Clustered .

Click + to display the following Advanced Options:

- Title Format - determines how the cluster appears in the browser tree.

- Outline only - displays the assigned number of the cluster along with the number of documents in the cluster and its coherence.

- Title only - displays the title of the cluster (up to 10 terms that best represent the cluster) along with the number of documents in the cluster and its coherence.

- Outline and title - displays the assigned number, title, number of documents in the cluster, and its coherence.

- Maximum Hierarchy Depth - the number of levels in a cluster hierarchy (e.g., a value of 1 results in the creation of only top-level clusters). Documents can only be in one cluster at each level. Lower level clusters are more tightly conceptually-related than higher level clusters. The maximum value for this field is 5. The default value is set to 3.

When Maximum Hierarchy Depth is set to be greater than 1, a maximum of 16 top-level clusters will be created.

- Minimum Coherence - the level of conceptual correlation that items must have to be included in the same cluster. The default value is 0.7. This affects the depth of the cluster tree, but it does so only in conjunction with the Maximum Hierarchy Depth setting. Each cluster has a coherence, which is a measure of tightness. A loose cluster node has a lower coherence, while that of a tighter cluster node of more-related documents is higher. When the Analytics engine sees a cluster node that it has built, it decides whether to break it into subclusters by looking at its coherence. If it is at or above the minimum coherence, it leaves it alone. If it’s below the minimum coherence, it breaks it up, but only if the maximum depth has not yet been reached. Cluster nodes that don't reach the full depth of the tree have a coherence higher than the Minimum Coherence setting, with rare exceptions.

- Generality - determines how vague (general) or specific the clusters will be at each level. Values range from 0 (most specific) to 1 (most general). The default value is 0.5. Low generality (closer to 0.0) results in more clusters that are tighter at each level of the cluster tree, including the root. High generality (closer to 1.0) gives you fewer and broader clusters . A low generality means that many top-level clusters are created, while a high generality means that few are created. However, as noted above, with Maximum Hierarchy Depth greater than 1, the number of top-level clusters is typically 16. As you move further down the tree, the same general principle applies. A low generality expands each level vertically.

- Create Cluster Score - checking this checkbox creates a decimal field on the Document object that stores the document's coherence score within the cluster. Enabling this will increase the duration of the cluster job significantly. This is unchecked by default.

See Renaming a cluster and Deleting a cluster .

## Default settings for automatically created clusters

If you choose to automatically create a cluster when setting up a new conceptual index, the cluster will behave as follows:

-

It will be called "Default Cluster [index name]."

-

It will be created immediately after the conceptual index has been activated.

-

It will be linked to the chosen conceptual index.

-

The cluster settings will have the following values:

-

Title Format: Outline and Title

-

Maximum Hierarchy Depth: 3

-

Minimum Coherence: 0.7

-

Generality: 0.5

-

Create Cluster Score Field: No

You can replace the default cluster at any time through the Mass Operations menu. For more information, see Creating or replacing a cluster .

## Replacing an existing cluster

Replace existing cluster is the same as Creating or replacing a cluster , except the results replace existing clustering options. When you select Replace Existing Cluster , you're prompted to select the existing cluster set you would like to replace.

## Viewing clusters

To view a cluster, navigate to the Cluster browser via the in the browser window. Click to refresh the list of clusters.

Expand a cluster to see the lower-level clusters below it.

When you create a new cluster, Relativity automatically creates one or both of the following two fields (the Score field is only created if Create Cluster Score was checked for the Cluster mass operation pop-up).

Name Function Field type

Cluster :: ClusterName Stores the cluster names for the cluster and each subcluster that the document is a part of. Multiple choice

Cluster :: ClusterName :: Score Stores the coherence score for the document, representing how close the document is to the center of the cluster. Decimal

These fields allow you to easily query for clustered documents in searches and views. You may also use the multiple choice field as the Batch Unit field in a batch set.

In the example above, cluster 1 contains the terms "agreement, kay, doc, draft," and the parentheses contain the numbers (14395, 0.40):

- 14395 is the number of documents in cluster 1 and all of its subclusters. You will also find that the number of documents in each of its lower-level clusters add up to this total. (10,064 + 4,331= 14,395)

- 0.40 is the conceptual closeness, or coherence score, of all of the documents in cluster 1. This indicates how closely related the documents are to each other. A higher coherence score (closer to 1.0) indicates that the cluster is a very highly related group of documents. A low coherence score (closer to 0.0) indicates that the documents are more loosely related to each other.

Also in the example above, cluster 1.1 contains the terms "agreement, kay, doc, attached," and the parentheses contain the numbers (10064, 0.51):

- 10064 is the number of documents in cluster 1.1, the highest-level cluster. You will also notice that this number (10,064) and the number of documents in the other cluster (4,331), add up to the number of documents found in the parent cluster 1 (14,395 documents).

- 0.51 is the coherence score of the documents within this cluster. This indicates how closely related the documents are to each other.

The following system-defined nodes may appear in your cluster list and are defined as follows:

- UNCLUSTERED (x, 0.00) - These documents are considered empty by CAAT. These documents might be completely void of text, or they might only contain noise words or text that has been filtered out (such as email headers, disclaimers, etc.).

- Not Clustered - These documents were submitted for clustering, but they are not part of the data source of the associated index.

- Pending - These documents were submitted for clustering and are currently in queue to be clustered. When this node returns no documents, the cluster operation has completed.

- Not set - This node displays all of the documents in the workspace that were not submitted for clustering.

To view and interact with your cluster data using Cluster Visualization, see Cluster visualization .

## Renaming a cluster

Perform the following steps to rename a cluster:

- Locate the cluster in the Cluster Browser.

- Right-click the cluster and select Rename .

- Enter a new name.

- Click OK .

## Deleting a cluster

To delete a cluster, perform the following steps:

- Navigate to the Analytics Indexes tab, and click on the Analytics index that was used to create the cluster.

- Select the checkbox next to the cluster you want to delete from the cluster list at the bottom of the Analytics index console.

- Click Delete .

On this page

- Clustering

- Creating or replacing a cluster

- Fields

- Default settings for automatically created clusters

- Replacing an existing cluster

- Viewing clusters

- Renaming a cluster

- Deleting a cluster


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

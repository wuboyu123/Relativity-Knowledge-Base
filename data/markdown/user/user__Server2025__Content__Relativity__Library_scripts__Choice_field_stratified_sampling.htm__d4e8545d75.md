---
title: "Choice field stratified sampling"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Choice_field_stratified_sampling.htm
collection: user
fetched_at: 2026-06-22T06:08:12+00:00
sha256: 982e136e6dfb735b5b47f08005a502973679baef702284c9abe6ba0a2c2070d4
---

Choice field stratified sampling

# Choice field stratified sampling

This script selects a specified number of sample documents across categories chosen by the user, ensuring that each category is represented equally. These documents can then be reviewed or set aside for any process which benefits from sampling a broad variety of documents.

Examples of how to use this script include:

-

Sampling documents with different coding tags

-

Sampling documents across different folders

-

Sampling across clusters

-

Sampling documents coded by different reviewers for quality checks

The most common use of this script is sampling documents from each cluster in a conceptual cluster, then pre-coding those documents before starting an active learning project. The variety of content in the sample gives the active learning engine a strong foundation for its relevance predictions, and it can increase the accuracy of those predictions early in the project.

## Special considerations

Consider the following when running this script:

- If you plan to sample documents across clusters, you must create the clusters first. For more information, see Clustering .

- You can use any single-choice or multiple-choice field to define the categories for the script.

- When used on a multiple choice field with parent and child choices, this script only considers the child choices. In a cluster visualization, these are represented as the outermost ring of clusters.

## Inputs

-

Before running the script, create a Yes/No field to track which documents have been selected by the script. If you use a previously created Yes/No field, the script will overwrite any existing values.

-

Create a saved search which includes documents from all categories you want to sample. If you are sampling from a specific set of clusters, make sure only the desired clusters are selected when creating your saved search.

-

Navigate to the Scripts tab.

-

Select the Choice Field Stratified Sampling script. If the script is not present in the workspace's Script tab, you must add it.

-

Click Run .

-

In the pop-up window, fill out the following fields:

-

Choice to sample from - select the choice field containing the categories you want to sample.

-

Saved Search - select the saved search created in step 2.

-

Number from each choice - enter the number of documents you want to sample from each category.

-

Is Sampled Field (Yes/No) - select the Yes/No field created in step 1.

-

Click Run .

## Results

Once run, this script updates the Yes/No field to Yes for the sampled documents. To view all sampled documents, go to the Document List view and search for a Yes value in that field. You can then code the documents or create a saved search to set them aside for later.

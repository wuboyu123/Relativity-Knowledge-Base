---
title: "Find similar documents"
url: https://help.relativity.com/Server2025/Content/Relativity/Analytics/Similar_document_detection.htm
collection: user
fetched_at: 2026-06-22T06:05:38+00:00
sha256: 8a6a4956ed50cdecf1e714e283a549b692960adbf0d13fe64cfa2146cf97f812
---

Find similar documents

# Find similar documents

You can use Find similar documents to identify documents that are conceptually similar to the one you are viewing. Relativity ranks the documents based on the conceptual similarity of their content in the concept space rather than a strict word comparison.

When you click Find Similar Documents in the Viewer, the entire document is submitted as a query string. The process is similar to a concept search, except instead of a query string, the whole document's position in the concept space is used as the query. A hit sphere with minimum concept rank of 60 is drawn around the document, and any documents that are within that hit sphere are returned as search results. This minimum rank value is not configurable.

## Special considerations

Note the following special considerations about running conceptual analytics operations:

- The following security permissions are required to run the operations:

Object Security Tab Visibility

- Document - View

- Analytics Index - View

- Analytics Categorization Set - View, Edit, Add

- Analytics Categorization Category - View, Edit, Add

- Analytics Example - View, Edit, Add

Documents

- In order to run an operation from the viewer, the document must be in the data set of an active Analytics index.

- You can only run operations in the Native Viewer and Extracted Text Viewer.

## Best practices

- Large documents with many topics are not optimal for finding similar documents. Instead of using this feature, select the text that is relevant to your query, and then submit that text as a concept search.

## Running find similar documents from the viewer

To find similar documents, perform the following steps:

- Select a document from the document list and open it in the Native Viewer or Extracted Text Viewer. This is your primary document.

- Click the View Similar Documents button at the bottom of the viewer. Alternatively, right-click in the white space of the document and select Find Similar Documents

When the operation is executed, all of the unfiltered text of the document is used as the query. The Documents list pane opens and displays the Similar Documents tab, which contains other conceptually similar documents. This tab contains the following information about the results:

- Rank - the conceptual similarity of the document to the primary document. The higher the rank, the higher the relevance to the query. A rank of 100 represents the closest possible distance. The rank doesn't indicate the percentage of shared terms or the percentage of the document that isn't relevant.

- Control Number - the control number of the document.

## Navigating results

Once the conceptual analytics operation is executed, the following takes place:

- The breadcrumb navigation includes Conceptual Analytics if you have run a concept search, find similar documents, or keyword expansion. If you navigate back to the Documents tab, this breadcrumb is removed.

- The Similar Documents card updates to display the results of the operation and the number of documents returned by the operation.

- Optionally, you can click on the Filters icon to enable filtering. Enter the desired terms in a column and press Enter on your keyboard to filter the results.

- Optionally, click the Export to CSV icon to download a .csv file that contains the results in the Similar Documents card.

- Optionally, to save the current documents in the Similar Documents card as a saved search, do the following:

- Click the Save as Search icon in the bottom-left.

The Saved Search pop-up displays.

- Enter the desired name in the Name field.

- Click Save .

## Changing the active index

If you have more than one active index, the Select Index icon displays in the upper-right of the card. The oldest active index (lowest Artifact ID) is chosen by default. To change indexes, click on the Select Index icon and select a different active index from the drop-down menu.

To change indexes, click on the Select Index icon and select a different active index from the drop-down menu.

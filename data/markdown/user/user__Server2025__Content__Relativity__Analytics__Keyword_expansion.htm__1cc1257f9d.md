---
title: "Keyword expansion"
url: https://help.relativity.com/Server2025/Content/Relativity/Analytics/Keyword_expansion.htm
collection: user
fetched_at: 2026-06-22T06:05:36+00:00
sha256: 34af42b4d1b2b8834532ca12c3066b0cea1c0e7c5203c65778470ab61bf09643
---

Keyword expansion Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Keyword expansion

Analytics can position any term, block of text, or document into its spatial index and return the closest documents. It can also return the closest terms. Submitting a single term provides you with a list of highly correlated terms, synonyms, or strongly related terms in your document set. When you submit a block of text, you get a list of single terms that are strongly related to that content. Therefore, because the terms returned are based on the concepts that comprise the search index's training space, any term that isn't included in the training data source won't produce any results.

Relativity limits the threshold of this function to 50. Only words with a coherence score greater than 50 will be returned.

You can use keyword expansion to see how different language is used to express the same or similar concepts. Keyword expansion can also be used on a word to identify other conceptually related terms and words in your index that you didn't expect. You can use these results in a dtSearch or search terms report.

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

## Running keyword expansion from the viewer

To run keyword expansion, perform the following steps:

- Select a document from the document list and open it in the Native Viewer or Extracted Text Viewer. This is your primary document.

- Select a section of text, and then right-click the text.

- Select Keyword Expansion from the right-click menu.

Once the operation is executed, the Documents list pane opens and displays the Keyword Expansion tab, which contains keywords that represent concepts similar to the search terms. This tab contains the following information about the results:

- Rank - the conceptual similarity of the document to the primary document. The higher the rank, the higher the relevance to the query. A rank of 100 represents the closest possible distance. The rank doesn't indicate the percentage of shared terms or the percentage of the document that isn't relevant.

- Keyword - the keyword that represents similar concepts to your search text.

The search text is automatically added to a textbox, which you can edit and then click Search to update your results.

### Navigating results

Once the conceptual analytics operation is executed, the following takes place:

- The breadcrumb navigation includes Conceptual Analytics if you have run a concept search, find similar documents, or keyword expansion. If you navigate back to the Documents tab, this breadcrumb is removed.

- The Keyword Expansion card updates to display the results of the operation and the number of documents returned by the operation.

- Optionally, you can click on the Filters icon to enable filtering. Enter the desired terms in a column and press Enter on your keyboard to filter the results.

- Optionally, click the Export to CSV icon to download a .csv file that contains the results in the Keyword Expansion card.

### Changing the active index

If you have more than one active index, the Select Index icon displays in the upper-right of the card. The oldest active index (lowest Artifact ID) is chosen by default. To change indexes, click on the Select Index icon and select a different active index from the drop-down menu.

To change indexes, click on the Select Index icon and select a different active index from the drop-down menu.

## Running keyword expansion from the Documents tab

To run keyword expansion from the Documents tab, perform the following steps:

- Navigate to the search panel .

- Click Add Condition .

- Select (Index Search) from the Add Condition drop-down menu.

The (Index Search) window opens.

- Select an Analytics index.

- Click Expand .

- Enter one or more search terms in the text box. Click Expand to display a list of keywords and their rank. The result set contains keywords that represent concepts similar to the search terms.

You can expand a keyword in the results set. Click on the keyword link to add the term to the textbox, and click the Expand button. The new results display in the grid.

On this page

- Keyword expansion

- Special considerations

- Running keyword expansion from the viewer

- Navigating results

- Changing the active index

- Running keyword expansion from the Documents tab


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

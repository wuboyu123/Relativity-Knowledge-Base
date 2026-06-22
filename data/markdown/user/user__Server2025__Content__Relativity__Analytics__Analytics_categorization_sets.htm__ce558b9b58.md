---
title: "Analytics categorization set tab"
url: https://help.relativity.com/Server2025/Content/Relativity/Analytics/Analytics_categorization_sets.htm
collection: user
fetched_at: 2026-06-22T06:05:29+00:00
sha256: 7a4688a4eceafe9e7e7c72416e8d670424ccae73f2b6b8482e0959c1001c649a
---

Analytics categorization set tab

# Analytics categorization sets

Using categorization, you can create a set of example documents that Analytics uses as the basis for identifying and grouping other conceptually similar documents. Categorization is useful early in a review project when you understand key concepts of a case and can identify documents that are representative examples of these concepts. As you review documents in the Relativity viewer, you can designate examples and add them to various categories. You can then use these examples to apply categories to the rest of the documents in your workspace.

Unlike clustering, categorization can be used to place documents into multiple categories if a document is a conceptual match with more than one category. Many documents deal with more than one concept or subject, so forcing a document to be classified according to its predominant topic may obscure other important conceptual content within it. When running categorization, you can designate how many categories a single document can belong to (maximum of five). If a document is placed into multiple categories, it is assigned a unique rank for each.

When documents are categorized, Analytics maps the examples submitted to the concept space, as if they were a document query, and pulls in any documents that fall within the set threshold. However, when you have multiple examples, the categorized documents consist of the combined hits on all of those queries. These results return with a rank, representing how conceptually similar the document is to the category.

Categorization is most effective for classifying documents under the following conditions:

- You've identified the categories or issues of interest.

- You know how you want to title the categories.

- You have one or more focused example documents to represent the conceptual topic of each category.

- You have one or more large sets of data that you want to categorize rapidly without any user input after setting up the category scheme.

## Identifying effective example documents

Each example document conceptually defines a category, so you need to know what your categories are before you can find the most appropriate example documents. Keep in mind that a category doesn't have to be focused around a single concept. For example, a category might deal with fraud, but different example documents for the category might reflect different aspects of fraud, such as fraudulent marketing claims, fraudulent accounting, and fraudulent corporate communications.

Example documents define the concepts that characterize a category, so properly defining example documents is one of the most important steps in categorization. In general, example documents should be:

- Focused on a single concept - the document should represent a single concept relevant to the category.

- Descriptive - the document should fully represent the single concept it is defining. Single terms, phrases, and sentences don't convey enough conceptual content for Analytics to learn anything meaningful. Aim for one to two fully developed paragraphs.

- Free of distracting text - example documents shouldn't contain headers, footers, repeated text, or garbage text such as OCR errors. When creating example documents, ensure that they are free of this type of verbiage.

- We do not recommend that you run categorization with more than 50,000 example documents. Having more examples than this will cause performance issues when running categorization.

- A document excluded by the Optimize training set feature can still be used as an example of categorization.

## Creating a categorization set

You must have an Analytics conceptual index set up before you can create a categorization set.

To create a categorization set:

- Create a saved search with the documents you want to categorize. See Searching for details.

- Under Indexing & Analytics, click the Analytics Categorization Set tab.

- Click New Analytics Categorization Set . The Analytics Categorization Set Layout appears.

- Complete the fields on the Analytics Categorization Set Layout to create the set. See Fields . Fields in orange are required.

- Click Save to save the categorization set.

### Fields

The following fields are included on the Analytics Categorization Set Layout.

- Name is the name of the set. If you attempt to save a set with a name that is either reserved by the system or already in use by another set in the workspace, you will be prompted to provide a different name.

- Documents To Be Categorized - the saved search containing the documents you want to categorize. Click the ellipsis to select a saved search.

- Analytics Index - the conceptual index to use for defining the space in which documents are categorized. Click the ellipsis to select an index.

- Minimum Coherence Score - the minimum conceptual similarity rank a document must have to the example document in order to be categorized. This document ranking is based on proximity of documents within the concept space. The default value is 50. If you enter 100, Relativity will only return and categorize exact conceptual matches for your examples.

- Maximum Categories Per Document - determines how many categories a single document can appear in concurrently. This can be set to a maximum of five. In some workspaces, a document may meet the criteria to be included in more than the maximum number of categories. If that maximum is exceeded, the document is categorized in the most conceptually relevant categories. The default value is 1. Keeping this value at 1 creates a single object relationship and lets you sort documents based on the Category Rank field in the Analytics Categorization Result object list or any view where the rank field is included. Raising this value above 1 creates a multi-object relationship and eliminates the ability to sort on documents by the rank field.

- Categories and Examples Source - the single- or multiple-choice field used as a source for categories and examples when using the Create Categories and Examples option on the Categorization Set console. Populating this field enables the Create Categories and Examples button on the console and eliminates the need to manually add categories and examples to the set before running a categorization job. Relativity creates categories for all choices associated with the specified field and creates example records for all documents where this field is set. Click the ellipsis to display a picker containing all single and multiple choice fields in the workspace, and select a field to use as the source.

- Example Indicator Field - used to create new examples when the Create Categories and Examples option is selected on the console. Click to display a picker containing all Yes/No fields in the workspace. Examples are created for only those documents marked with a “Yes” value in the field you select as the indicator.

- Auto-Synchronize on Categorize All - uses the value entered for the Categories and Example Source field to automatically create categories and examples before categorization is run.

- Yes - enables automatic category and example creation and eliminates the need to select this option on the console before every categorization job.

- No - disables automatic category and example creation. This is the default.

When Auto-Synchronize on Categorize All is set to yes, all existing categories are cleared and the new ones specified for the Categories and Example Source field are automatically created when you click Categorize All on the console.

- Email notification recipients - send email notifications when categorization is complete. Enter the email address(es) of the recipient(s), and separate them with a semicolon.

### Job information

The following information is displayed in the Job Information section of the Analytics Categorization Set Layout:

- Categorization Status - the current state of the categorization job.

- Categorization Last Run Error - the last error encountered in the categorization job.

- Synchronization Status - the current state of the synchronization process.

- Synchronization Last Run Error - the last error encountered during the synchronization process.

If you don't populate the Categories and Examples Source field on the set, and you haven't linked any categories or example objects to the set, no buttons on the console are enabled. Console buttons only become enabled after you add at least one category and one example object to the set. See Adding new categories and examples through the layout .

## Adding new categories and examples through the layout

If you choose not to make a selection for the Categories and Examples Source field on the categorization set, you can manually add new categories and assign example documents to a set using the Analytics Categorization Set layout. There are no limits to the number of categories you can add to a categorization set.

### Adding a new category through the layout

To add a new category from the layout, perform the following steps:

- Click New in the Analytics Category heading. The Add Analytics Category layout displays.

- Complete the fields on the layout.

- Analytics Categorization Set - the set the new category is applied to. This field is populated with the name of the current set. Click to select a different set.

- Name - the name of the category.

- Click Save . The category is now included in the categorization set.

### Adding a new example through the layout

You can add an entire document or a chunk of text as an example. To add a new example from the layout, perform the following steps:

- Click New in the Analytics Example heading. The Add Analytics Example layout appears.

- Complete the fields on the layout. Fields in orange are required.

- Analytics Categorization Set - the set the new example is applied to. This field is populated with the name of the current set. Click to select a different set.

- Category - the category the example is associated with. Click to select a different category.

- Document - the document to use as an example. Click to select a document.

- Text - the text to use as an example. Enter the appropriate text in the box.

If both the Document and Text fields in the example are populated, Text will override Document. Therefore, if you intend to select a document from the ellipsis to use in your category, do not supplement it with information in the Text field because only the text is considered.

- Click Save . The example is now included in the set.

#### Best practices for adding example documents

- The Relativity Analytics engine learns from concepts, not individual words or short phrases. Therefore, an example document should be at least a few paragraphs long.

- An example document should focus on a single concept. If you have a large document that covers several topics, use text excerpts to add a specific part of the document as an example, rather than the whole thing.

- Never add a document as an example based on metadata (for example, privileged documents might be privileged because of who sent them). Relativity Analytics will only consider the authored content of the document and not any outside metadata.

- Email headers and other types of repeated content are usually filtered out. These should not be considered when determining whether a document is a good example.

- Numbers are not considered when training the system; spreadsheets consisting largely of numbers do not make good examples.

- We don't recommend adding nearly duplicate documents as an example of a category as they will map to nearly the same (or possibly exactly the same) location in the concept space and categorize nearly the same documents.

- An example document should never be used as an example in more than one category in a single categorization set.

We recommend at least 5-20 examples per category to provide good coverage of the topic. It's not unusual in a workspace of several million documents to need a couple of thousand examples.

Furthermore, we strongly recommend you limit the number of examples you have per category to 15,000 documents. There is no system limitation to how many examples you can have, but the more examples you have, the longer it will take the system to run categorization.

- Some documents may be highly responsive but undesirable as examples. For example, the responsive text found in an image of a document may not be available when the reviewer switches to Extracted Text mode. Because the system only works with a document's extracted text, that document would be responsive but not a good example.

- The following scenarios do not yield good examples:

- The document is a family member of another document that is responsive.

- The document comes from a custodian whose documents are presumed responsive.

- The document was created within a date range which is presumed responsive.

- The document comes from a location or repository where documents are typically responsive.

## Adding new categories and examples automatically

If you haven't manually created any categories or examples, but you have populated the Categories and Examples Source field on the categorization set, the Create Categories and Examples button is enabled on the console. You can use this button to automatically add new categories and examples to your categorization set.

When you click Create Categories and Examples , Relativity clears all existing categories and examples and generates new ones. Categories are created for each choice in the Categories and Examples source field. If an Example Indicator Field is selected on the categorization set, examples are created for every document with a designation of Yes for the Example Indicator Field. The category is assigned to the example document based upon the value of Categories and Examples source field. If an Example Indicator Field is not selected on the categorization set, examples are created for every document with a value in the Categories and Examples source field. The category is assigned to the example document based upon the choice selected in the Categories and Examples source field.

During creation, the Create Categories and Examples button changes to Stop Creation , which you can click to stop the process.

Once category and example creation is complete, the Analytics Category and Analytics Example associative object lists reflect the results.

## Categorizing documents

When you have assigned categories and examples to your categorization set, the Categorize All Documents button becomes enabled on the Categorization Set console.

Clicking this button kicks off a categorization job based on the settings specified when you created the set. When you run a new categorization job, all results of the previous categorization job are deleted.

If the Auto-Synchronize on Categorize All field under Categorization Setup is set to Yes, all existing categories and examples will be cleared and the ones specified for the Categories and Example Source field will automatically be created when you click Categorize All on the console.

To begin categorizing, click Categorize All Documents . When the confirmation message appears, asking you if you want to run categorization, click OK .

We recommend running only two categorization sets at once for optimal performance.

Once the categorization has been kicked off, the following options are enabled in the Categorization Set console:

- Refresh Page - updates the page to reflect job progress. The Status field is updated, as well as any of the object lists, to show the progress of the categorization job.

- Show Errors - displays a list of all errors encountered during the categorization process.

- Retry Errors - reprocesses any errors encountered during the categorization process.

After the initial categorization process is complete, or after you have clicked Stop Categorization , the following button is enabled:

- Categorize New Documents - incrementally runs the categorization process by adding to the category set records that have been imported since the initial categorization job was run.

When you run a categorization set, the system creates the Categories - <name of categorization set> and Category Rank fields. Use Categories - <name of categorization set> to view the search results. Use Category Rank to see how closely related documents are to the category.

The Pivot On and Group By fields are set to Yes by default for all Categories - <name of categorization set> and Category Rank fields. For Categories - <name of categorization set>, you can change the Pivot On and Group By to No; however, you can't change the Category Rank fields to No. When you run a categorization set, all previously created Pivot On and Group By fields for Category Rank change to Yes.

After a categorization job is completed, you can view the results in the field tree. All category set names are appended with the word "Categories" in the format Categories - <name of categorization set> . Click + to display a list of categories in the set.

Documents that appear in the [Not Set] tag in the field tree were either not close enough to an example to get categorized, not in the data source of the conceptual index, or not submitted for categorization.

## Searching on categorization results

The fields created by your categorization set are available as conditions when you create a saved search. You can search on them and review the results.

To create a saved search to see your categorization results, perform the following steps:

- Launch the Saved Search form. See Searching .

- In the Conditions section, select Categories – <name of categorization set> from the Field drop-down menu.

- Select these conditions from the Operator drop-down menu.

- Click in the Value field. Select the value(s) you want to review. See Searching .

- Click Save & Search .

- Review the results of the search. The saved search displays the same number of documents that you would see by filtering in the field tree.

---
title: "Search terms reports"
url: https://help.relativity.com/Server2025/Content/Relativity/Search_terms_reports.htm
collection: user
fetched_at: 2026-06-22T06:07:12+00:00
sha256: 91b51bddc6aec9e4a3fa9e1291a796a73444a6c2f64eefa1f7df7ca97b6a1151
---

Search terms reports

# Search terms reports

Search terms reports provide the ability to identify documents containing specific keywords or terms. You can enter multiple terms and generate a report listing the number of hits for each term in a document. You can also select an option to create a multiple object field for the search terms report to use in your persistent highlight sets. When you select a search terms report for use with a persistent highlight set, the report determines which terms or phrases to highlight in the documents through the Review Interface.

For information on how to calculate and store the number of terms in a Search Terms Report (STR) that hit on a document, see Search terms report hit count .

## Guidelines for using search terms reports

Use the following guidelines to ensure that your search terms report properly highlights the required terms:

- Define a saved search using conditions that return the required group of documents for the Searchable Set . Persistent highlighting applies only to documents in the searchable set. Relativity also only counts hits that fall within the searchable set. Related items not included in the searchable set will not be searched for search terms.

-

Confirm that your dtSearch index includes all documents in the Searchable Set of the search terms report.

- Select the Tag Hits toggle to create a multiple object field for the search terms report. If this field is not created you cannot select it in the Highlight Fields option when creating a persistent highlights set. See Persistent highlight sets .

- When using a search terms report as a highlight source in a persistent highlight set, only the terms in documents associated with the current reports appear highlighted. If you add new search terms to the reports, you must run pending terms so that they appear highlighted in documents.

- The system automatically preserves the precise order in which the terms were entered when generating a report.

## Creating a search terms report

To create a new search terms report, follow these steps:

- Navigate to the Search Terms Report tab.

- Click New Search Terms Report .

- Complete the fields on the form. See Fields .

- Click Save .

After saving the search terms report, the Search Terms Report Status section and Search Terms Report console appear. As the status section indicates, you must add terms to your new report. See Adding terms and highlight colors .

### Fields

Search terms reports contain the following fields:

- Name —the search terms report’s name. This value cannot exceed 75 characters.

- Index —the dtSearch index used to create the report.

- Searchable set —a saved search that includes the set of documents used to create the report.

- Include relational group —includes the "Documents with Hits + [Group Name]" counts for each term in the search terms results. This value counts the documents with hits for each term as well as all documents in the same relational group as the documents with hits. Include relational group only includes hits of related items in the searchable set. Relativity does not look outside of the searchable set. Click Select and then choose a relational group to include.

- Tag Hits —if enabled, saves the results to a multiple object field named after the search terms report with the prefix STR, like STR - Industry terms , so the results can be reviewed later. Tags each document containing search hits using the search terms reports multiple object field with the search terms found in each document.

- Show in Field Tree —if enabled, automatically adds the terms to the field tree on the Documents view.

- Calculate unique hits —if enabled, includes a unique hits value for each term in the search terms results. Unique hits is the count of documents in the searchable set returned by only that particular term. If more than one term returns a particular document, that document is not counted as a unique hit. Unique hits reflect the total number of documents returned by a particular term and only that particular term.

Unique hits can help you identify terms in your search terms report that may be overly inclusive.

- Remove Hidden Characters —if enabled, automatically filters out hidden or non-displayable text control characters when creating or editing terms for the search terms report.

- These hidden control characters have been known to cause issues in searching and can be unknowingly copied from Word or Excel documents.

- The list of control characters that are filtered are the same as the default ignore section of the dtSearch alphabet file text .

- Email notification recipients —specifies recipients to send an email notification to when your search terms report finishes running. Enter the email addresses of the recipients. Separate entries with a semicolon.

- Notes —enter notes specific to the search terms report.

#### Creating search terms reports through workspace templates

Additionally, you can create search terms reports through workspace templates using the following steps:

-

From your active workspace, ensure that the Search Terms Report object type setting for Copy Instances On Workspace Creation is enabled .

-

Create a new workspace using the active workspace as your workspace template.

The search terms reports are copied over to the new workspace.

### Adding terms and highlight colors

To add terms to your search terms report:

You must create a persistent highlight set for highlighted terms to appear in your documents. See Persistent highlight sets for more information.

- Click the name of your search terms report.

- Click Add Terms .

- Enter your terms in the text box so that each term appears on a separate line.

Alternatively, you can also click the Dictionary link to display the Dictionary Search pop-up. In the pop-up you can perform searches using fuzziness, proximity, and stemming. Click Copy to List to add the Dictionary search results to the New Terms text box.

Each line is treated as an individual dtSearch query. For more information about dtSearch, refer to dtSearch .

- (Optional) Select a background color and text color using the color picker. See the preview text to verify that the resulting highlighted text is readable.

By default, highlighted terms appear as black text with an orange background.

- Click Add to add your new terms to the terms list.

A single term has a character limit of 450.

A confirmation message displays with the count of new terms added. Duplicate terms are ignored. After adding new search terms to an existing report, you must run the terms so that they appear highlighted in documents. For more information, see Running a search terms report .

### Editing terms and highlight colors

To edit a term in your search terms report:

-

Click the name of your search terms report.

-

In the Term column, click on the term you would like to change. The field will become editable.

-

Edit the text, then press Enter .

-

Run Pending Terms in order to update the search terms report. For more information, see Running a search terms report .

To edit the background and text color of terms:

- Click the name of your search terms report.

- Select the checkbox next to the terms you want to change, then click Edit .

- Choose the new background and text color, then click Save .

Changes to background and text color apply to all terms being edited.

### Deleting terms

To remove terms from the search terms report:

- Click the name of your search terms report.

- Select the checkbox next to the terms you want to edit, and then click Edit .

- Click Delete .

- Click Delete .

If you remove search terms from the reports, the terms automatically disappear from the search terms report results. You must run the report again for accurate totals in the status bar and when using View Term Report.

### Copying a search terms report

You can copy an existing search terms report using the mass copy operation.

To copy a search terms report:

- From the Search Terms Reports tab, click the checkbox next to the search terms report you want to copy.

- From the mass operations bar, select Checked . Alternatively, you can select All to copy all search terms reports.

- Select Copy in the drop-down menu.

The Copy window displays.

- Click Ok to copy the items.

## Running a search terms report

You generate a search terms report by using the options available in the search terms report console. The console appears after you save a search terms report or when you open an existing report from the Search Terms Report tab.

The console includes the following options:

- Run All Terms —generates counts for each term. Use this option when generating the report for the first time or if you want to regenerate counts for all terms in the report. Run all terms after adding new documents to the searchable set.

- Run Pending Terms —updates an existing report. It runs a report on only those terms with a Pending status.

- View Results —opens the Search Terms Results page. This page displays the report results, listing the number of document hits for each term.

The Search Terms Results page provides the following:

- Name —search term included in search terms report.

- Documents with hits —the number of documents in the searchable set that contain the search term.

Documents with hits is not security-aware or influenced by permissions. This means that it includes documents the user cannot view in a basic search. For example, a user could perform a dtSearch that returns a total of five documents, including two inaccessible documents. Even though the user can only view three documents, the search terms count still includes all five documents originally tagged with the search term.

- Documents with hits, including group —counts the documents with hits for each term as well as all documents in the same relational group as the documents with hits. The count only includes hits of related items in the searchable set. It will not look outside of the searchable set.

- Unique hits —counts the number of documents in the searchable set returned by only that particular term. If more than one term returns a particular document, that document is not counted as a unique hit. Unique hits reflect the total number of documents returned by a particular term and only that particular term.

- Last run time —timestamp when the search terms report last ran.

In this page, you can also access a list of any terms that failed during the creation of the Search Terms Report. To read these error messages, change your view to Search Terms Results Details .

- View Term Report —In the Search Terms Report console, click View Term Report to open the graphical search terms report. You can print or save the report. To save, select a file type at the top of the report.

- Retry Errors —attempts to regenerate the report for search terms that returned error messages.

You can now run multiple Search Terms Reports in parallel, simultaneously, by adding more Search Terms Reports agents to the same resource pool as the workspace. You can queue as many reports as needed and they will run when others complete.

### Search terms report status

After running a search terms report, the search terms report status section appears. It lists the search terms report name and status. The status indicates the current progress of the report. This field contains either Searching your terms, Completed, or Error.

This section also provides a summary of the search terms report and its results:

- Number of Terms —total number of terms run in the search terms report.

- Documents with Hits —the number of documents in the searchable set that contain the search term.

- Documents with Hits + Relational Groups —counts the documents with hits for each term as well as all documents in the same relational group as the documents with hits.

- Documents in Searchable Set —total documents in the designated searchable set.

## Accessing tagged documents using the Field Tree browser

After you run a search terms report with the Tag option enabled, Relativity creates a folder in the Field Tree browser with documents grouped by tags found by the search terms report. Each tag includes the count of documents containing that term. The folder is named after the search terms reports multiple object field created by the search terms report. For example, if your search terms report is named Produced Documents , the folder in the Field Tree browser is named STR - Produced Documents .

Click a search term tag in the Field Tree browser to view documents in your searchable set tagged with the selected term. You can also email a link to the tagged documents by right-clicking the tag results and selecting Email Link .

## Using tagged search terms in a saved search

After you run a search terms report with the Tag option enabled, Relativity creates choices for each of the terms that you specified. You can then use these choices as criteria in a saved search.

Use this procedure to create a saved search using tagged search terms:

- Follow the instructions for setting fields in the Information and Search Conditions sections on a saved search. See Creating or editing a saved search .

- Click on the Fields tab in the Saved Search pop-up.

- Select the desired field in the Unselected section and move it to the Selected section using the arrow icons.

- Click the Condition button and select an option from the pop-op.

- Perform the following tasks on the Select STR dialog:

- Select your search terms report in the Field box.

- Select an Operator, such as any of these .

- Select the STR option from the Condition drop-down menu to select search terms on the Select Items dialog.

- Set any other fields as necessary.

- Click OK .

For example, if you added the tagged search terms called money, crime, and oil, the Conditions section would appear as follows:

- Repeat steps 1 to 3 for each tagged search terms.

- Click Apply and Save & Search to run your query.

## Permissions

You may have an occasion where you want to grant limited permissions to a group of users outside of the site administrators. For example, you want to limit users from creating new search terms reports to keep your environment organized. However, at the same time, you want users to view, edit, and add to existing terms lists.

To add search terms report permissions to a user group:

- Create a new user group and add it to your workspace.

If you do not know how to create a new user group, see Groups . If you need help adding the group to your workspace, see Setting workspace permissions .

- From the Manage Workspace Permissions modal window, click Edit Permissions .

In the image below, the group name is Processing - STR Users .

- Scroll down to locate the two entries for search terms reports--Search Terms Report and Search Terms Result. You want to edit permissions for existing terms, so you will edit the Search Terms Result object. The Search Terms Report object grants permissions for reports overall and not the content within the report. Click one or more icons to enable the permission level. Available levels include Disable , View , Edit , Delete , Add , or Manage Security .

- Click Save .

- Click the Manage Workspace Permissions link.

- Click the Preview button for your group.

The workspace opens with the group permissions applied. This view is helpful if you want to see how the workspace looks and functions as a group member. A banner across the top of the page reminds you of the preview mode.

- Open a search terms report.

You now see buttons above the search terms list corresponding to the permissions granted. In the image below, add and edit permissions apply.

- Check the box next to one or more search terms.

The permission level buttons become active.

- Click the appropriate button to edit the search term.

If the only permission level granted is Edit, you will not see any buttons above the list. In this case, you can click any search term to enable a text box. Complete your edits and click Enter to save and exit.

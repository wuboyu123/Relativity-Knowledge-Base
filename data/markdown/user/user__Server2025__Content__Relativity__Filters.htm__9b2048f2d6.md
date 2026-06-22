---
title: "Filters"
url: https://help.relativity.com/Server2025/Content/Relativity/Filters.htm
collection: user
fetched_at: 2026-06-22T06:02:23+00:00
sha256: 224112e3f88ff370631cf54e149de079a45158e969e071c814ae20816f4d375b
---

Filters

# Filters

Filtering provides a fast and easy way to search for items in a list in Relativity. You can use filters to search for values in the fields on the active view, and across all records available in the searchable set. Filters are also available for item lists on tabs and pop-up windows.

The field type associated with each column determines the available filter types, such as textboxes, popup pickers, and drop-down lists. You don't need any specific security permissions to use filtering.

This page contains the following sections:

- Showing and hiding filters in the item list

- Setting a filter

- Filter types

- Changing item sets per page

- Saving filters as a search

## Showing and hiding filters in the item list

You can use filters to quickly narrow your searchable set, allowing you to browse through the key documents in the viewer efficiently.

The following filter buttons display above item lists in Relativity:

- Show/Hide filters - Displays the field column filters for an item list at the top of each column. This icon turns orange when filters are activated. Click the icon again to hide the filters if filtering options are displayed. Your filter settings remain unchanged.

- Clear all - Removes the current filter settings. This option is only available after you set a filter.

The filter type determines the steps required to set the search criteria that it uses. See Filter types

When you create or edit a field, you can select its Filter Type . See Fields .

In the following example, the active filters display on the Documents tab.

## Setting a filter

To activate the filter options at the top of each column in the item list, click the icon. The icon turns orange when filters are activated. Click the icon again to hide the filters.

Before defining a new search filter, click or click Clear Conditions in the search panel to remove any previous settings. For example, say you create a filter on the Privileged field, but now want to search only by the Custodian field. If you don't clear the filter, Relativity filters your documents by both the Privileged and Custodian fields, and your result set may include fewer documents than you expect.

Select a field or fields that you want to filter (e.g., Record Type). The filter type determines the steps required to set the search criteria that it uses. See Filter types

Make your selections from the filter drop-down menu or enter text in the filter textbox (if the field is a text field), and then click Enter .

The field column header is highlighted in orange and has a filter icon in the top right corner to let you know that filtering has been applied to that field. This will persist whether or not you have the filters shown or hidden.

The search panel is also updated with the applied filter conditions and displayed as a filter card in a List Conditions box.

You cannot edit the filter card by clicking on it. However, you can clear the list condition the same way you can clear any search conditions on the search panel. The item list will update accordingly.

See Filter types and Textbox filter search examples for more information on using specific filters.

## Filter types

Relativity includes the following filter types:

- Boolean filters

- Numeric filters

- List filters

- Date filters

- Multilist filters

- Textbox filters

### Using Boolean filters

Boolean filters are available only on Yes/No field types. To use a Boolean filter, click the drop-down menu arrow and select True , False , or <blank> from the list to apply the filter.

In the following example, selecting True would display only documents that have native files (where the field has a Yes value). If selected, <blank> displays only items that don't have the a True (Yes) or False (No) value assigned to the Boolean field (is not set).

If you click on Advanced , the pop-up for the Boolean filter appears where you can specify multiple filter conditions that are connected with explicit OR operators. Click Apply to apply the specified filter conditions to the field.

Click Add Condition to add an additional condition to the filter.

### Using numeric filters for numbers

The numeric filter type is available for the following field types only:

- Decimal

- Whole Number

- Currency

To use a numeric filter, click the drop-down menu arrow and select an operator (i.e., equal to (=), not equal to (!=), greater than (>), less than (<), less than or equal to (<=), or greater than or equal to (>=)), and then enter a numerical value in the Filter textbox.

Relativity will also correctly read the thousands separator (e.g., 100 , 000.00) in numeric filters.

After you enter the value in the textbox, hit Enter to apply the conditional expression for filtering the list (e.g., filter the list for File Size greater than a certain number).

If you click into the Filter textbox, a drop-down menu will appear. You can select the Advanced option that appears in the drop-down menu to display the pop-up for the numeric filter. This is where you can specify multiple filter conditions that are connected with explicit OR operators. Click Apply to apply the specified filter conditions to the field.

Click Add Condition to add an additional condition to the filter.

### Using List filters

The List filter type is available for the following field types only:

- Single Choice

- Single Object

- User

- Fixed Length Text

- Fields that contain a large number of items may also cause the List filter to take longer to populate. For fields that may contain a large number of choices, you can designate a Popup filter instead.

- Fixed Length Text fields - if the field contains more than 255 items, the List filter type you specify for the field will revert to the Textbox filter type and an error will be written to the Error Log when you visit a Document list view containing the field.

- Single Choice / Single Object fields - if the field contains more than 255 items, the List filter type you specify for the field will revert to None (disabled) and an error will be written to the Error Log when you visit a Document list view containing the field.

List filters are frequently associated with fields used for coding documents. The conditions displayed in the drop-down menu for this filter vary by the type and purpose of the associated field. For example, a field called Responsiveness might have the filter conditions of Responsive, Not Responsive, or Needs Further Review. You can select the checkboxes of the options that you want to filter for, and then click Apply to apply the filter to the item list. Alternatively, you can click Select all to select all filters in the list, you can click Clear to remove all selections in the menu or you can select (Not Set) to only show items where the field has not been set (null).

If there is a single choice that you would like to immediately apply as a filter to the document list, hover your cursor over that choice's row and then click Only on the right side of the row.

In this example, if you only select the Non-Responsive checkbox, then only documents that have been coded with this value will display in the item list.

You can find a specific option in a long list by entering all or part of the name of the option you are looking for in the Filter textbox under the Apply button. The list will filter automatically as you type.

Click the icon in the upper-right corner of the drop-down menu to launch a pop-up where you can select items in the list and use additional operators such as filtering for items that do NOT contain certain field values. Click Apply to apply the specified filter conditions to the field.

### Using date filters

The date filter type is only available for Date field types. Using the date filter, you can quickly and efficiently filter for items meeting the specific date criteria that you want.

The following operators are available:

- All

- Not Set

- Is

- Is before

- Is before or on

- Is after

- Is after or on

- Between

For example, you only want to view items that were sent before or on 7 AM on January 21, 2015. To set and apply a date filter for this scenario:

- Select your operator from the drop-down list underneath the Apply button (e.g., is before or on).

- Use the calendar interface to select the date criteria (e.g., January 21, 2015). There are drop-down menus for selecting a specific month and year or you can use the forward / backward arrows to navigate by month.

- Enter the time below the calendar (e.g., 7:00 AM).

Filtering on fields using the date/time format does not support using “@Today”. If you do not enter a specific time, a time of 12:00 AM will be entered explicitly for the filter.

- Click Apply to apply the date filter. Only items that were sent before 7 AM on January 21, 2015 will display in your item list.

When you select the Between operator, two calendars will display in the drop-down date filter, allowing you to pick the start and end date / time for the time range.

You can click the Advanced option in the drop-down date filter to launch a pop-up to take advantage of additional operators such as "is in" that let you filter for items where the date is in this week, last week, last month, this month, etc. and create more complex date filter criteria using multiple conditions. Click Apply to apply the specified filter conditions to the field.

### Using multilist filters

The multilist filter type is available for the following field types only:

- Multiple Choice

- Multiple Object

- Single Choice

Using multilist filters, you can select multiple conditions from a drop-down menu. These filters are frequently associated with fields used for coding documents.

To apply a multilist filter, click the drop-down arrow to display the conditions list. Select the conditions that you want to filter on. You can click Select all to select all filters in the list, you can click Clear to remove all selections in the menu or you can select (Not Set) to only show items where the field has not been set (null). Click Apply to apply the selected filter conditions.

If there is a single choice that you would like to immediately apply as a filter to the document list, hover your cursor over that choice's row and then click Only on the right side of the row.

You can find an specific option in a long list by entering all or part of the name of the option you are looking for in the Filter textbox under the Apply button. The list will filter automatically as you type.

Click the icon in the upper-right corner of the drop-down menu to launch a pop-up where you can select items in the list and use additional operators such as filtering for items that do NOT contain certain field values. Click Apply to apply the specified filter conditions to the field.

### Using textbox filters

The textbox filter type is available for the following field types only:

- Fixed-length Text

- Long Text

- Date

- Whole Number

- Decimal

- Currency

- Object

You can use textbox filters to search on specific terms, numbers, and dates. You can directly enter one or more terms in the filter textbox and connect multiple terms with any of the following operators:

- AND

- OR

- IS SET

- IS NOT SET

- BETWEEN

- = (equal)

- >= (greater than or equal to)

- <= (less than or equal to)

When entering terms and operators directly in a textbox filter, you must use the proper syntax. See Textbox filter search examples for more information.

The textbox filter treats each search term as if it were preceded and followed by a wildcard (*) and returns all versions of the term. Don't add an asterisk (*) to the beginning or ending of a search term. The filter won't return any results if you use this operator.

You can also use the advanced textbox filter feature to build more advanced filter queries on the selected text field. See Using advanced textbox filtering .

### Textbox filter search examples

You can perform text searches using Boolean operators by directly entering search strings in the filter textbox as follows or you can use the Advanced feature to build more advanced filter queries on the text field (see Using advanced textbox filtering ).

#### Boolean and other search operators

The following table lists examples of valid search strings using Boolean and other operators.

Valid search strings Returns items where…

cubs OR sox ([FIELD VALUE] like '*cubs*') OR ([FIELD VALUE] like '*sox*')

cubs AND sox ([FIELD VALUE] like '*cubs*') AND ([FIELD VALUE] like '*sox*')

cubs OR sox AND kcura ([FIELD VALUE] like '*cubs*') OR (([FIELD VALUE] like '*sox*') AND ([FIELD VALUE] like '*kcura*'))

percent sign ( % ) Use this operator to check whether the field is set to a value. It behaves like the "Is like" operator in a query.

underscore ( _ ) Wildcard for a missing character. Don't use the underscore to check if a field is set to a value; it's slower and more resource-intensive than using the percent sign (%).

= with term Returns an exact phrase.

cubs sox Returns the exact phrase (that is, the word "cubs" followed by a space and the word "sox").

IS SET Returns only items where the field has a value.

IS NOT SET Returns only items where the field does not have a value (null).

The following table shows examples of invalid search strings.

Invalid search strings Description

cubs AND The AND operator requires a right search term.

cubs OR The OR operator requires a right search term.

AND cubs The AND operator requires a left search term.

OR cubs The OR operator requires a left search term.

#### Alphabetical filtering

The following table lists examples of valid search strings you can use to filter text alphabetically.

Alphabetical filtering Returns items where…

>= cubs [FIELD VALUE] >= 'cubs'

<= cubs [FIELD VALUE] <= 'cubs'

= cubs [FIELD VALUE] = 'cubs'

= cubs AND sox [FIELD VALUE] = 'cubs AND sox'

cubs BETWEEN sox * ([FIELD VALUE] >= 'cubs') AND ([FIELD VALUE] <= 'sox')

kcura and cubs BETWEEN sox ([FIELD VALUE] >= 'kcura and cubs') AND ([FIELD VALUE] <= 'sox')

* If you attempt to use more than one BETWEEN operator in a single filter string (for example, 12/13/2000 BETWEEN 1/0/2008 BETWEEN 5/4/2009), you'll receive an Incorrect Syntax error in the filter box. If you need to search for documents based on multiple BETWEEN operators, you can create a saved search with multiple conditions, each of which uses a date field with a between operator and a date range value. For more information, see Saved search

#### Dates and numbers

The following table lists examples of valid date and number searches, as well as the expected result set.

Valid search strings Returns items where…

>= 7/24/2008 [FIELD VALUE] >= '7/24/2008'

<= 7/24/2008 [FIELD VALUE] <= '7/25/2008'

= 7/24/2008 ([FIELD VALUE] >= '7/24/2008') AND ([FIELD VALUE] < '7/25/2008')

>= 07/27/2008 1:23 PM [FIELD VALUE] >= '07/27/2008 1:23 PM'

<= 07/27/2008 1:23 PM [FIELD VALUE] <= '07/27/2008 1:23 PM'

= 07/27/2008 1:23 PM [FIELD VALUE] = '07/27/2008 1:23 PM'

7/24/2008 BETWEEN 8/24/2008 ([FIELD VALUE] >= '7/24/2008') AND ([FIELD VALUE] < '8/25/2008')

7/24/2008 1:23 PM BETWEEN 8/24/2008 3:45 PM ([FIELD VALUE] >= '7/24/2008 1:23 PM') AND ([FIELD VALUE] <= '8/24/2008 3:45 PM')

7/24/2008 BETWEEN 8/24/2008 ([FIELD VALUE] >= '7/24/2008') AND ([FIELD VALUE] <'8/25/2008')

07/27/2008 ([FIELD VALUE] >= '07/27/2008') AND ([FIELD VALUE] < '7/28/2008')

>= 100 [FIELD VALUE] >= '100'

<= 100 [FIELD VALUE] <= '100'

= 100 [FIELD VALUE] = '100'

The following table includes examples of invalid data and number search strings.

Invalid search strings Description

> 7/24/2008 The equal sign must be used with the greater than operator (as in >=).

< 7/24/2008 The equal sign must be used with the less than operator (as in <=).

>= 0/24/2008 The search string includes the value 0 for the month.

= 0/24/2008 The search string includes the value 0 for the month.

0/24/2008 BETWEEN 8/24/2008 The search string includes the value 0 for the month in the starting date.

7/24/2008 BETWEEN 0/24/2008 The search string includes the value 0 for the month in the ending date.

### Using advanced textbox filtering

You can use the following operators with advanced filtering:

- Is

- Is not

- Is set

- Is not set

- Is less than

- Is greater than

- Is like

- Is not like

- Contains

- Does not contain

To use advanced textbox filtering:

- Click inside the Filter textbox for the text field in the column header.

A drop-down filter displays the Advanced option.

- Click the Advanced option to launch the Filter popup screen.

- Choose an operator (e.g., is greater than). See Fixed-length, long, or extracted text operators for a list of definitions of the available operators.

- Enter the desired value (e.g., 100. The filter will only return items where the value of the field is greater than 100).

- (Optional) Click Add condition to add a new filter condition (e.g., you may want to also return items where the text field contains the word privilege).

Multiple conditions are automatically connected with an OR operator.

- Click Apply to apply the filter condition.

## Changing item sets per page

You can use the set selector menu to change the number of items that appear per page. The set selector menu appears at the top of the screen. The option you select remains the default setting during your session until you select another option.

## Saving filters as a search

To save your filtered item set as a saved search:

- Click next to the mass operations drop-down menu at the bottom of the item list to open the Saved Search window.

- Select or enter the following required information:

- Name - Enter a title for the search. The title appears in the saved searches browser.

- Owner - Select Public to make the search available to all users or choose a specific user from the list. Click Me to select your name from the list, making the search private. (Users must have the appropriate privileges to view searches.) See Controlling the visibility of saved searches .

- Search Folder - Click the Select button to launch a pop-up window where you can save the new search to a specific folder on the saved searches browser. Highlight the folder where you want to save the search, and then click OK to select it.

- Add to or modify the search criteria as needed. See Creating or editing a saved search .

- Click Save .

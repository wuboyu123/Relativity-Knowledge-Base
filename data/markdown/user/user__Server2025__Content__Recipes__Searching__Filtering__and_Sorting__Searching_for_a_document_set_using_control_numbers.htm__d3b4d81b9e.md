---
title: "Searching for a document set using control numbers"
url: https://help.relativity.com/Server2025/Content/Recipes/Searching__Filtering__and_Sorting/Searching_for_a_document_set_using_control_numbers.htm
collection: user
fetched_at: 2026-06-22T06:07:47+00:00
sha256: 96f59e698b2ca70c2c878c389fa3d50e2dc78259feccd2c5064b3b6ebb861a04
---

Searching for a document set using control numbers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Searching for a document set using control numbers

Occasionally, you may need to search for a large set of documents based only on a list of control numbers. This topic shows you how to use a dtSearch index, a Search Terms Report, and the Field Tree to return a set of documents from a list of control numbers.

## Security and permissions

Begin by setting (or confirming) the following permissions for your workspace:

- Search Index – Edit/Add and corresponding tab

- Search Terms Report – Edit/Add and corresponding tab

- Field Tree browser access

## Steps

- Create a Saved Search that returns all documents in your Workspace.

- Name the saved search Control Numbers Saved Search .

- Remove all fields except the control number field.

- Create a new dtSearch index of all control numbers in your Workspace.

- Name the dtSearch index Control Numbers dtSearch .

- Use the Control Numbers Saved Search as your Searchable Set . Click Yes to continue when you see the warning message about long text fields.

- Complete a Full Build of the index. Click Yes to activate the index after the build.

- Navigate to the Documents tab, then Saved Searches tab.

- Click the Control Numbers Saved Search to display the results in the list pane.

- Select all the records, then click Export to File from the Mass Action drop-down menu.

- For the Format value, select (or confirm) Excel Spreadsheet via HTML (.xls) is active.

- Click Export .

- Open the downloaded file in Excel, then select all the control numbers and copy them. (Highlight the column values, then click CTRL-C.) In a later step, you paste the numbers in your search terms report. If you have a many records, consider breaking them down into chunks of 100.)

- Create a new Search Terms Report for your list of control numbers.

- Name the search terms report Control Numbers STR .

- Use the Control Numbers dtSearch index as your index.

- Use the Control Numbers Saved Search as your Searchable Set .

- Confirm Show in Field Tree is active so that your results return in the Field Tree.

- Save the report. Click Yes to continue when you see the warning message about long text fields.

- Click Add Terms .

- Paste the control numbers from the exported Excel spreadsheet into the list box (CTRL-V.)

- Click Add .

- Click Run All Terms to run the report.

- Use the Field Tree browser to review the results. Click the folder icon for the Control Numbers STR to return all documents from your list of control numbers.

## Resources

- dtSearch —how to create a dtSearch index.

- Saved search —how to create a saved search.

- Search terms reports —how to create a search terms report.

On this page

- Searching for a document set using control numbers

- Security and permissions

- Steps

- Resources


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

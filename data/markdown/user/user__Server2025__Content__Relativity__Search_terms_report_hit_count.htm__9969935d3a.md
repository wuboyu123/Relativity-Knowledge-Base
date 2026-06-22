---
title: "Search terms report hit count"
url: https://help.relativity.com/Server2025/Content/Relativity/Search_terms_report_hit_count.htm
collection: user
fetched_at: 2026-06-22T06:16:39+00:00
sha256: f9b12c20ed509117e74388d250821f7bc5349bea602b3ff3950901a305101d92
---

Search terms report hit count Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Search terms report hit count

This topic describes how to calculate and store the number of terms in a Search Terms Report (STR) that hit on a document.

You can then sort, filter and search for documents based on the number of STR hits, allowing you to prioritize review based on STR hit count or create searches that return documents having a minimum number of STR hits

This workflow requires downloading and installing the Delimiter Count by Saved Search script. See NSerio / delimiter-count-by-saved-search on GitHub for a link to the script.

## Calculating and storing hits

To complete this workflow, perform the following steps:

- Create a Long Text field on the Document object named STR Hit Terms , which will store a semicolon delimited list of STR terms that hit on a document.

- Create a Whole Number field on the Document object named STR Hit Count , which will store the number of STR terms hitting on a document.

- Create a saved search that returns the documents that hit on one or more terms for a specific STR.

- The STR used must have the Type field set to Report and Tag. See Creating a search terms report .

- Ensure that the saved search includes the Control Number (Identifier) field and STR field.

- Export the results of the saved search.

- Perform an Export to File mass operation on the results of the above search.

- For the export Format, select Comma Separated Values (.csv).

- The STR terms will be populated in the file as semicolon delimited values.

- Using the RDC, import the file you exported above.

- In the RDC, select Tools > Import > Document Load File .

- Select the file you exported above as the Load File.

- Map the STR field in the load file to the STR Hit Terms field in the workspace.

- Map Control Number.

- Select Overlay Only and select Control Number as the Overlay Identifier.

- Select Import > Import File from the RDC menu.

- Navigate to the Scripts tab in the workspace and locate the Delimiter Count by Saved Search script.

- Run the script.

- Set the fields in the script pop-up:

- Saved Search – The search created above that returns documents where the STR is set.

- Source Field – The STR Hit Terms field that was updated above via the RDC import.

- Field Delimiter – Enter a semicolon (;).

- Count Destination Field – The STR Hit Count field created above. Note: this field is only populated when its value is null/blank; it will not be overwritten by the script.

- Click Run .

- The STR Hit Count field now contains the number of STR terms hitting on each document.

- You can use the STR Hit Count field in searches and views to sort and filter documents based on the STR Hit Count value.

On this page

- Search terms report hit count

- Calculating and storing hits


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

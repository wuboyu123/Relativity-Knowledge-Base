---
title: "Tally/sum/average"
url: https://help.relativity.com/Server2025/Content/Relativity/Mass_operations/Tally_sum_average.htm
collection: user
fetched_at: 2026-06-22T06:15:53+00:00
sha256: ebb9c2ec945b1150ea5d68be4899141be98cbd9bac0484d3fb1537ee1365118d
---

Tally/sum/average Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Tally/sum/average

You can use the tally/sum/average operation to tally, sum, or average the values of fields associated with documents or objects.

This operation is commonly used to determine the number of pages in a print job or production. For documents, it's recorded under the document history. Tally/sum/average is available from the mass operations bar.

#### Considerations

-

You can only use tally/sum/average on fixed-length text , choice , user , and number fields.

-

You can't use mass operations on Data Grid-enabled fields.

-

Tally/Sum/Average calculates the mean of a column without counting null as 0. When a column contains null values, the operation yields a different result from an average calculated by summing the column and dividing the total document count. To include null values in the denominator of a Tally/Sum/Average calculation, you must change the null value to 0 to ensure the inclusion of those documents.

To perform a tally/sum/average operation, perform the following steps:

- Choose whether to tally/sum/average Checked items or All items in the current returned set

- Select Tally/Sum/Average in the drop-down menu. The Tally/Sum/Average pop-up displays with options for the following fields:

- Field - used as the basis of the calculation. For example, you could select a custodian field if you want a tally of these entries.

- Function - the option performed on the field:

- Tally - lists a count for each item type in the specified fields of all selected documents or objects.

- Sum - adds the values in the specified numeric fields of all selected documents or objects.

- Average - calculates mean value of the specified numeric fields for all selected documents or objects.

The result of a tally is similar to a summary report; it outlines the values of a field and the count for each. The tally runs across the entire section, but only reports the top 100,000 values.

After your results appear, you can perform the following actions:

- Filter the results.

- Clear All filter text.

- Browse through the results using the blue arrows.

- Sort the results.

- Export results to an external file.

On this page

- Tally/sum/average


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

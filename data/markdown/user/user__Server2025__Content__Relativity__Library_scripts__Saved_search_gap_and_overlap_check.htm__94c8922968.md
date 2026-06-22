---
title: "Saved search gap and overlap check"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Saved_search_gap_and_overlap_check.htm
collection: user
fetched_at: 2026-06-22T06:15:31+00:00
sha256: 5e858282968697244f0ffe3f48af04f31bf35e007a97e151dcf29a280d374192
---

Saved search gap and overlap check Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Saved search gap and overlap check

This workspace script finds documents with gaps in Bates numbers or overlapping Bates numbers.

## Special considerations

Consider the following when working with this script:

- This script excludes Bates numbers that don't appear in the expected format (letters followed by numbers). For example, a Bates range of TEST1234.001-Test1234.009 would be skipped and excluded from the results.

- It looks at the values in the Bates number fields instead of the Production Document File table.

- The script may take a long time to run depending on the number of documents in the saved search.

## Inputs

This script requires the following inputs:

Field Options Description

Saved search A list of all the saved searches that the current user has permission to run in the current workspace.

Select the saved search that contains the documents you want to check for gaps and overlaps in Bates numbers. The script only checks the records in the selected saved search.

Beginning Bates A list of all the fixed-length text fields on the Document object. Select the field that contains the beginning Bates value.

End Bates A list of all of the fixed-length text fields on the Document object. Select the field that contains the ending Bates value.

## Outputs

After the script executes, the results appear as a list of duplicate Bates numbers and/or missing Bates numbers in the sequence.

The Results view includes the following fields:

- Begin Range - the begin Bates number of the range that includes a gap or overlap.

- Finish Range - the end Bates number of the range that includes a gap or overlap.

- Type

- Gap - indicates that there's a gap in the Bates numbers for documents included in the production.

- Overlap - indicates that there are overlapping Bates numbers for the documents included in the production.

- Invalid - indicates a NULL value for either the Beginning Bates field or the End Bates field.

## Running the script

To add the script to your workspace:

- In a workspace, go to the Administration > Scripts tab.

- Click the New Relativity Script button.

- For script type, choose Select From Script Library .

- Click next to Scripts.

- Find and select the Saved Search Gap and Overlap Check script.

- Click Ok .

- Click Save .

For additional assistance, contact Relativity Support .

On this page

- Saved search gap and overlap check

- Special considerations

- Inputs

- Outputs

- Running the script


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

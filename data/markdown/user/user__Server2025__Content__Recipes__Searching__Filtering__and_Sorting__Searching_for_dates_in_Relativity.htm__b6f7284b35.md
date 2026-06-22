---
title: "Searching for dates in Relativity"
url: https://help.relativity.com/Server2025/Content/Recipes/Searching__Filtering__and_Sorting/Searching_for_dates_in_Relativity.htm
collection: user
fetched_at: 2026-06-22T06:17:31+00:00
sha256: 3fe22cd4fff285a302adb29a7676bb9da27d4b208e2bb393cef2aae4903da595
---

Searching for dates in Relativity Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Searching for dates in Relativity

This recipe provides steps to search for dates within Relativity using a filter, a saved search, or a dtSearch.

## Requirements

Applicable to all versions of Relativity.

## Types of date searches

You can search for dates in Relativity using three different methods:

- Field filters

- Search for single date or single date range

- Requires metadata

- Saved search

- Search for multiple date or multiple date ranges

- Requires metadata

- dtSearch auto-recognize

- Search for dates within document text and in multiple formats

- Does not require metadata

## Directions

### Field filters

To search for a date using a field filter, perform the following steps:

- Ensure the date field you want to search for is in the current view. Add it to the view if necessary.

- Turn on filters, and then enter a valid search string in the text box filter.

The following table lists examples of valid date and number searches, as well as the expected result set.

Valid search strings Return items where...

>= 7/24/2008 [FIELD VALUE] >= '7/24/2008'

<= 7/24/2008 [FIELD VALUE] <'7/25/2008'

= 7/24/2008 ([FIELD VALUE] > '7/23/2008') AND ([FIELD VALUE] <'7/25/2008)

>= 07/27/2008 1:23 PM [FIELD VALUE] >= '07/27/2008 1:23 PM'

<= 07/27/2008 1:23 PM [FIELD VALUE] <= '07/27/2008 1:23 PM'

= 07/27/2008 1:23 pm [FIELD VALUE] = '07/27/2008 1:23 PM'

7/24/2008 BETWEEN 8/24/2008 ([FIELD VALUE] >= '7/24/2008') AND ([FIELD VALUE] <= '8/24/2008')

7/24/2008 1:23 PM BETWEEN 8/24/2008 3:45 PM ([FIELD VALUE] >= '7/24/2008 1:23 PM') AND ([FIELD VALUE] <= '8/24/2008 3:45 PM')

07/27/2008 ([FIELD VALUE] >= '07/27/2008') AND ([FIELD VALUE] < '7/28/2008')

>= 100 [FIELD VALUE] >= '100'

<= 100 [FIELD VALUE] <= '100'

= 100 [FIELD VALUE] = '100'

The following table includes examples of invalid data and number search strings.

Invalid search strings Invalid reason

> 7/24/2008 You must use the equal sign with the greater than operator (as in >=).

< 7/24/2008 You must use the equal sign with the less than operator (as in <=).

>= 0/24/2008 The search string includes the value 0 for the month.

= 0/24/2008 The search string includes the value 0 for the month.

0/24/2008 BETWEEN 8/24/2008 The search string includes the value 0 for the month in the starting date.

7/24/2008 BETWEEN 0/24/2008 The search string includes the value 0 for the month in the ending date.

### Saved search

To search for a date in Relativity using a saved search, perform the following steps:

- Create a saved search.

- Select the date field you want to search for in the Conditions section.

You can set additional conditions to search for non-consecutive dates, including non-consecutive date ranges.

### Index search

Some cases require you to search for dates contained within the text of a document. Because dates can appear in various formats, the auto-recognize feature in dtSearch is useful.

To use this feature, build a new dtSearch index with Auto-recognize date, email, and credit card numbers set to Yes . Once the index is complete and active, you can search for dates within the text of a document.

The auto-recognize feature searches for strings that appear to be dates. It uses English-language months, including common abbreviations, and numerical formats. For example, dtSearch recognizes the following date formats:

- January 15, 2006

- 15 Jan 06

- 2006/01/15

- 1/15/06

- 1-15-06

- The fifteenth of January, two thousand six

It doesn't recognize DD/MM/YYYY format.

Note the following date and date range search strings:

- To search for a date, enter a date expression between the parentheses in the string "date()"; for example, date(jan 10 2006)

- To search for range of dates, enter a date range between the parentheses in the string "date()"; for example, date(jan 10 2006 to jan 20 2006)

- To search for a range of dates near the word apple , enter date(jan 10 2006 to jan 20 2006) w/10 apple

- dtSearch doesn't support unterminated date. To search for any date after or before a particular date, enter a bounded range with a maximum or minimum value for the bounds. The maximum value for a year is 2900, and the minimum value is 1000. For example, DateField contains date(jan 10 2006 to jan 1 2900)

## Notes

- By default, date fields use the filter type of text box. However, you can change this to custom in the field information.

- If you need more complexity than the text box filter type can provide, you can set up a saved search.

On this page

- Searching for dates in Relativity

- Requirements

- Types of date searches

- Directions

- Field filters

- Saved search

- Index search

- Notes


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

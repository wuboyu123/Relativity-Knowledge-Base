---
title: "Searching workflows"
url: https://help.relativity.com/Server2025/Content/Relativity/Searching/Searching_workflows.htm
collection: user
fetched_at: 2026-06-22T06:07:57+00:00
sha256: 2f867c8afb9f4bb7fce20357c40d19a4676bc29af9351cad8193429c1b0d42d9
---

Searching workflows

# Searching workflows

Relativity provides flexibility to help you identify documents through searches so that you can ready them for further review and analysis.

This topic highlights setting up multiple search indexes, applying various search techniques, and using filters properly when executing searches.

For details on searching for dates within Relativity using a filter, a saved search, or a dtSearch, see the Searching for dates in Relativity knowledge base article on the Relativity Community.

## Workflow details

Relativity offers both Basic Keyword Search and Specialized dtSearch.

The Basic Keyword Search Index populates automatically, is available out of the box, and supports basic Boolean operations. These operations include AND, OR, NOT, and the wildcard (*) operator.

The Specialized dtSearch Index is custom built and must be set up with an index to query against. In addition to basic Boolean operations, it also supports the following functionality:

- Wildcard operator for a single digit (=)

- Stemming operations (~)

- Fuzzy search operation (%)

- Range Searching on Numeric fields (~~)

- Customize data set to be indexed via custom saved search

- Proximity Searching

- Customized Noise Word List

- Auto Recognition of email addresses, credit card numbers, and dates.

## Best practices for advanced operators

The following includes best practices for the use of advanced operators and workflow options:

### Proximity search

Proximity search uses operators to search certain terms in proximity to other terms in a document. Use the following recommendations when employing proximity searching:

- To use directional proximity searching use "pre /x " operators. To use non-directional proximity searching use "w /x" operators.

- To determine the beginning and end of a document, use reserved word with either ("xfirstword") or ("xlastword"). Use these operators to search for metadata like email addresses or footers within a document.

- To determine proximity. The distance between terms is important so you know whether you receive true hits or false positives. The following image illustrates the proper syntax for proximity searches:

The following image shows all correct and incorrect combinations of proximity searches that result in successful hits when using proximity operators:

Sometimes additional factors affect the distance between terms. The following image demonstrates a search for a string of words in proximity to another word. The search in the following image takes the following into account:

- Noise words count as words when calculating proximity.

- Punctuation counts as whitespace when using default settings.

- Relativity treats line breaks and consecutive space characters as single spaces.

- dtSearch default noise words and connector words like AND, OR, BETWEEN, and NOT count as words when calculating proximity.

In this case, we continue to calculate the distance of the string ("confidential and/or privileged information:) from the word ("message") as shown above. However, when using connector words, system admins should create an index that removes noise words from the noise word list.

Relativity reserves the following noise words and characters, which continue to behave as operators, as well as being noise words: and, or, not, to, contains, xfirstword, xlastword, ", ( ), *, ?, %, @, ~, #, &, :, =.

Once that index is available for query you can either place the search string in quotes or apply stemming to the connector words to override their function as a connector.

### Auto-Recognition

Auto-Recognition identifies email addresses, dates, and credit card numbers in the data set you want to index. You can turn this feature on and off when you build your index. The search returns the results regardless of the data format. Auto-Recognition adds some time to your index build, but, depending on your case, the benefits can be significant.

### Searching for times

If you want to search for times in the body of documents, perform a full-text search with your dtSearch index for a specific time. Keep in mind that some characters cause a word break, such as the colon and period. Searching for 12:15 p.m . results in searching for four words: 12 , 15 , p , and m .

### Filters

In addition to the Search Indexes, you can also use filters to search on metadata fields and narrow down the review set of documents.

The following list includes metadata fields, their corresponding field types, and the filter type available in Relativity:

- File Type - Single-Choice, List Filter

- Custodian - Single-Choice, Pop-Up Filter

- Date Sent - Date, Textbox Filter

- Email To - Long Text, Textbox Filter

- Email Subject - Fixed Length Text, Custom Filter

- Designation - Single Choice, Multi-Choice List

The following table shows different types of filters you can set up with available fields in Relativity.

### Troubleshooting workflow

To troubleshoot and test searches, use a white board approach to map out searches before you run them. As part of the process, try to take into account all possible variations, so you can see which documents Relativity returns and to gain a better understanding of the search. For instance, if you want to find email family groups with inconsistent coding, numerous possibilities for searches exist. The following illustration shows a mapping of nine email family groups, each with an email and two attachments.

Construct searches (1 and 2) and mark the corresponding documents, and their family members, with hits for each of the searches. At this point, when you look at the board, you can see that the four email family groups have one thing in common. The documents are responsive to both searches. So, to close it out, construct a third search that pulls back documents common to both searches.

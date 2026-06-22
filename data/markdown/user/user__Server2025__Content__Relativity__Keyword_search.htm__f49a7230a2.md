---
title: "Keyword search"
url: https://help.relativity.com/Server2025/Content/Relativity/Keyword_search.htm
collection: user
fetched_at: 2026-06-22T06:06:47+00:00
sha256: bd6d204fdac2f3b00210f033fda2461d23abee081c02e254b1ab6de5e26133d2
---

Keyword search

# Keyword search

Keyword search (or SQL index search) is Relativity's default search engine. You can use a keyword search to query a full text index. The long text and fixed-length text fields included in this index vary by workspace.

New workspaces created in RelativityOne have extracted text automatically stored in Data Grid. Workspaces restored into RelativityOne using the ARM application will automatically have the extracted text migrated to Data Grid. In order to search extracted text in workspaces, you must use dtSearch or Analytics searching; you cannot use Keyword Search.

You can use Boolean operators (AND, OR, NOT) in keyword searches, as well as quotation marks for exact matches, asterisks (*) for wildcards, and other features. However, if you perform a keyword search with multiple terms, documents where those terms exist in separate fields won't return.

If you want to draft queries outside of Relativity, use a plain text editor such as Microsoft Notepad to prevent adding characters or formatting that might return unexpected search results.

While the keyword search offers fewer options than other Relativity searches, it uses an index that's automatically populated, reducing maintenance and ensuring all required document fields are indexed.

For information on configuring and managing word breakers, go here .

This page contains the following sections:

- Example keyword search strings

- Using the NOT operator in keyword searches

- Understanding noise words

- Running a keyword search

## Fields

A keyword search index is available in the Search Indexes tab by default. Click the Keyword Search link.

The keyword search index details page contains the following fields:

- Name - the name of the keyword search index. The name is the display name for the index.

- Order - a number that represents the position of the index in the list. The lowest-numbered index will be at the top. The highest-numbered index is at the bottom. Items that share the same value are sorted in alphanumeric order. Index order can be any integer (positive or negative). No decimals are allowed.

- Active - determines whether the index should be activated or deactivated. Yes means that the index will be activated; No means that the index will be deactivated.

If you apply item-level security to a search index, users can’t run any public saved searches built on that index and will get an error. We recommend leaving the index unsecured and instead applying security to the Search indexes tab or to individual saved searches.

## Example keyword search strings

The following table lists search string examples with their expected results.

Search string Returns documents with...

wired the word wired

wired magazine the words wired and magazine

wired AND magazine the words wired and magazine

wired OR magazine the word wired or the word magazine

wired, magazine the word wired or the word magazine

"wired magazine" the exact phrase wired magazine

wired NOT magazine the word wired and not the word magazine

Do not start key word searches with the NOT operator, or use it with the OR operator. For example, these searches are invalid:

- not wired

- wired or not magazine

See NOT Operator Evaluation in Keyword searches.

wire* any words beginning with wire, such as wired, wires, wireless

Key word searches do not support the use of wildcards at the beginning of a word. (Keyword searches are SQL index searches run on the Microsoft SQL Server, which does not support leading wildcards in full text searches.)

computer AND (wired OR magazine) the word computer and the word wired OR the word computer and the word magazine

When a search string does not include parentheses, the order of precedence for a keyword search evaluates AND then OR expressions. For example, the search string A AND B OR C is evaluated as (A AND B) OR C.

Search terms with accented letters are recognized and return keyword search results.

## Using the NOT operator in keyword searches

When running a keyword search that is an SQL full text search, carefully format queries that use the NOT operator. For example, you may want to query for email messages that have Ryan as the author, but do not have Will as the recipient. The fields in the following record are included in the index used to demonstrate how this query is run:

Document OCR Recipient Author

AS00001 From: Ryan To: Will Will Ryan

A keyword search using the string Ryan NOT Will returns the document AS00001 even though you would not expect it in the result set. The following table illustrates the SQL logic used to evaluate the query Ryan NOT Will.

SQL queries this field... Returns these results...

OCR Field Finds both Ryan and Will, so no document is returned.

Recipient Field Does not find Ryan, so no document is returned.

Author Field Finds Ryan but not Will, so the document AS00001 is returned.

When these fields are searched using the SQL logic, the Author field matches the query Ryan NOT Will, and unexpectedly returns the document.

You can use the AND NOT operator in a dtSearch as an alternative approach to this type of keyword search. See dtSearch .

## Understanding noise words

Noise words in a keyword search include punctuation marks, single letters, single digits, and words such as "at", "a", "on" and "the".

### Keyword search noise words - without double quotes

Noise words used in Keyword searches are ignored if the search string is not surrounded by double quotes . In a search for the phrase sun on my head , both on and my are ignored. The result is that the words sun AND head are queried without respect to proximity. Thus, any documents that contain both the words sun and head will be returned.

The following table illustrates how Keyword search queries for phrases that contain noise words that are not surrounded by double quotes.

Searching string (without quotes) Queries for this string

sun on my head sun AND head

sun on head sun AND head

### Keyword search noise words - with double quotes

If a Keyword search string containing noise words is surrounded by double quotes , then the noise words' positions in the string are taken into account when the query is executed. However, only the positions of any intervening noise words are taken into account, not the noise words themselves. Noise words at the beginning or tail end of a Keyword search string are ignored.

For example, the search strings " sun on my head " and " sun my on head " (where on and my are switched) return the same records. This is because Keyword search evaluates both search strings as a query for the phrase sun ABC XYZ head , where ABC and XYZ represent any two words , not just noise words. Similarly, a query for the search string " sun on head " returns documents that contain the phrase sun ABC head , where ABC represents any word.

The following table illustrates how Keyword search queries for phrases that contain noise words, and that are surrounded by double quotes.

Searching string (with quotes) Queries for this string

"sun on my head" sun [AnyWord] [AnyWord] head

"sun on head" sun [AnyWord] head

"sun on my head and" sun [AnyWord] [AnyWord] head

"and sun on head" sun [AnyWord] head

### Single digits as noise words

Single digits 0-9 are default noise words, so you cannot query on them with a keyword search. Relativity doesn't return the expected results if you attempt to query on a single digit. Use the dtSearch feature to query on a specific number or letter.

However, you can use a keyword search to query on whole numbers greater than 9. You can search on more than one digit, such as 09 . While these digits may be used to represent a specific numeric value (such as 9), they are not considered single digits, and can be used in a keyword search.

### Punctuation as noise words

Certain punctuation marks are treated as noise words by default, so you cannot query on them with a keyword search. They include:

- Period (.)

- Colon (:)

- Semicolon (;)

- Slash (\,/)

### At sign (@) and dashes

The at sign (@) and dashes (-) are ignored from being indexed in a keyword search, when either is used at the beginning of a query. For example, if you search a domain name, the same number of documents return whether you include or exclude @ .

### Hyphens and dashes

When a search phrase includes a hyphen or dash, the query returns results that include terms containing other punctuation marks. For example, the following results return for a search on the term Pop-up :

- Pop.up

- Pop--up

### Default noise word list

Relativity comes with the following default noise words:

Begins with... Noise words

A about, after, all, also, another, any, are, as, at

B be, because, been, before, being, between, but, both, by

C came, can, come, could

D did, do, does

E each, else

F for, from

G get, got

H has, had, he, have, her, here, him, himself, his, how

I if, in, into, is, it, its

J just

L like

M make, many, me, might, more, most, much, must, my

N never, no, now

O of, on, only, other, our, out

S said, same, see, should, since, so, some, still, such

T take, than, that, the, their, them, then, there, these, they, this, those, through, to, too

U under, up, use

V very

W want, was, way, we, well, were, what, when, where, which, while, who, will, with, would

Y you, your

## Running a keyword search

### Running a keyword search in the search panel

Use the following steps to run a keyword search in the Search panel.

- Navigate to the Search panel in the Documents Tab.

- Click Add Condition .

- Select (Index Search) in the Add Condition drop-down menu. The (Index Search) window opens.

- Select Keyword Search from the drop-down Index.

- Enter terms for the search in the Search Terms box.

- Optionally, select the Sort By Rank option to return results in order by relevance. The most relevant documents are listed at the top of the result set.

- Click Apply .

- (Optional) Add any additional conditions through the Add Condition drop-down menu.

- Click Run Search . To stop a long running search, click Cancel .

### Running a keyword search in the Search browser

Use the following steps to run a keyword search in the Search browser.

- Click to access the search browser from the document list.

- Click New Search .

- Set required fields.

- Click Add Condition .

- Select (Index Search) in the Add Condition drop-down menu. The (Index Search) window opens.

- Select Keyword Search from the Index drop-down menu.

- Enter terms for the search in the Search Terms box.

- Optionally, select the Sort By Rank option to return results in order by relevance. The most relevant documents are listed at the top of the result set.

- Click Apply .

- (Optional) Add any additional conditions through the Add Condition drop-down menu.

- Click Save or Save As .

- Click the name of the keyword search in the search browser.

- Click Run Search . To stop a long running search, click Cancel .

---
title: "Using regular expressions with dtSearch"
url: https://help.relativity.com/Server2025/Content/Relativity/Regular_expressions/Using_regular_expressions_with_dtSearch.htm
collection: user
fetched_at: 2026-06-22T06:07:45+00:00
sha256: 01854ed6bce137f664ddc80ef22b93f8ec3a1604ef6a7006cef0e874540590d5
---

Using regular expressions with dtSearch Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Using regular expressions with dtSearch

You can use regular expressions with your dtSearch index to search for more complex items such as Bates numbers, zip codes, and phone numbers. You can also use regular expressions in conjunction with proximity, stemming, and fuzzy searching in dtSearch.

## Regular expression search strings

To activate regular expressions in dtSearch, use double pounds signs (##) at the beginning of your search string. You can start your search from the search bar on the List page, or by adding a condition from the search panel. For details on how to run a dtSearch, see Running a dtSearch .

Relativity breaks down the regular expression syntax as follows:

Regular Expression —"##RegularExpression". "##" signals to Relativity that the string following ##, and encapsulated by double quotes, should be interpreted as regular expression. Be sure to use straight double quotes ( "" ) and not curly quotes ( “” ). Curly quotes may cause the regular expression to fail . You also want to avoid using capital letters in your regular expression because all characters in a dtSearch index are normalized to lowercase. You can use the Dictionary to help troubleshoot an individual regular expression. If your expression does not match in the Dictionary, it will not match in the index.

Starting in Relativity 10.0.119.1, regular expression searches run from the Document List will highlight search hits in the Native Viewer for any returned documents. This does not apply to the Extracted Text mode of the Viewer.

All regular expressions with dtSearch must begin with the ## call sign. If any table entries below do not include the call sign, be sure to add them to your search string before executing.

## Regular expression metacharacters

Metacharacters are the building blocks of regular expressions. Characters in regular expression are understood to be either:

- a metacharacter with a special meaning, or

- a regular character with its literal meaning

### View regular expression metacharacters examples

Metacharacter Description Example

\d Whole number 0 - 9

\d\d\d = 327

\d\d = 81

\d = 4

\d\d\d ≠ 24631 \d\d\d does not return 24631 because 24631 contains 5 digits. \d\d\d only matches for a 3-digit string.

\w Alphanumeric character

\w\w\w = dog

\w\w\w\w = mule

\w\w = to

\w\w\w = 467

\w\w\w\w = 4673

\w\w\w ≠ boat

\w\w\w does not return boat because boat contains 4 characters.

\w ≠ !

\w does not return the exclamation point ! because it is a non-alphanumeric character.

\W Symbols

\W = %

\W = #

\W\W\W = @#%

\W\W\W\W ≠ dog8

\W\W\W\W does not return dog8 because d, o, g, and 8 are alphanumeric characters.

[a-z] [0-9] Character set, at least one of which must be a match, but no more than one unless otherwise specified. The order of the characters does not matter.

pand[ora] = panda

pand[ora] = pando

pand[ora] ≠ pandora pand[ora] does not bring back pandora because it is implied in pand[ora] that only 1 character in [ora] can return.

dtSearch does not accept white space characters, even with regular expressions.

## Regular expression groups

With regular expression groups you can match for groups of characters within a string. The following table provides examples of how to use groups in your regular expression. Groups are most useful when you use them in conjunction with alternation and quantifiers.

Metacharacter Description Example

(abc)

(123)

Character group, matches the characters abc or 123 in that exact order.

pand(ora) = pandora

pand(123) = pand123

pand(oar) ≠ pandora pand(oar) does not match for pandora because it is looking for the exact phrase pandoar.

## Escaping regular expression metacharacters

When using regular expression to search for a character that is a reserved metacharacter, use the backslash \ to escape the character so it can be recognized in its literal sense. The following table gives an example on how to escape a reserved metacharacter when searching.

Search for Regular expression Match results

International phone number (UK) \+[0-9]{12}

+447700900954

+447700900312

If the + sign is not escaped with a backslash, regular expression treats + as a quantifier instead of the literal plus sign character.

### Regular expression caveats in dtSearch

There are a few caveats to consider when using regular expressions in dtSearch. Consider the following caveats before constructing your regular expression.

- The metacharacter \s never matches a whitespace character in Relativity, because whitespace characters do not exist in a dtSearch index. Instead, spaces are word breaks in dtSearch.

- Unless you modify your dtSearch index to be case-sensitive, you cannot use capital letters when constructing a regular expression in dtSearch. Thus, if you are searching for varying strings that all begin with NLRT, such as:

- NLRT-0381

- NLRT-6334

- NLRT-9167

- The proper Relativity RegEx is: "##nlrt-\d{4}".

For more information about case-sensitive indexes, see Build a Case Sensitive dtSearch Index.htm .

- You cannot search characters which are ignored during indexing, such as punctuation. To index a punctuation character, confirm that it is listed as a letter in your dtSearch alphabet file, and that it is not listed as an ignored, hyphen, or space character.

## Common dtSearch regular expression examples

The following table includes examples of dtSearch regular expressions you can use to search for patterns in dtSearch.

You must make any hyphens or symbols represented in these examples searchable in your dtSearch index. For more information, see Regular expression searching - SSN and EIN .

Type

Regular Expression

Match Results

Bates numbers

"##rel[0-9]{7}"

"##rel\d{7}"

REL0000331

REL3728948

Zip codes

"##[a-z]{2}" "##[0-9]{5}"

"##[a-z]{2}" "##\d{5}"

IL 60606

MD 21218

ca 94115

United States Phone numbers

"##[0-9]{3}-[0-9]{4}"

"##\d{3}-\d{4}"

You must make the hyphen (-) searchable in your index.

373-8837

463-9391

819-3814

United States Phone numbers with or without area codes

"##([0-9]{3}-)?[0-9]{3}-[0-9]{4}"

You must make the hyphen (-) searchable in your index.

312-483-8372

463-9391

Serial numbers

"##[a-z]{4}-[0-9]{4}-[a-z]{4}-[0-9]{4}"

"##[a-z]{4}-\d{4}-[a-z]{4}-\d{4}"

You must make the hyphen (-) searchable in your index.

XRFD-8324-ERWF-3231

GHSR-3413-KWEJ-8173

MPFS-1357-QEGT-9376

Dates

"##[0-9]{2}/[0-9]{2}/[0-9]{2,4}"

10/17/2015

3/6/98

4/25/2006

12/04/87

95/94/93

Email addresses

"##([\w_\.]+)@([\w_\.]+)\.([\w_\.]{2,6})"

You must make the at (@) and period (.) searchable in your index.

Joe.Smith426@example.com

743.MaryJane@example.com

Brian.23.Voltaire@example.net.uk

On this page

- Using regular expressions with dtSearch

- Regular expression search strings

- Regular expression metacharacters

- View regular expression metacharacters examples

- Regular expression groups

- Escaping regular expression metacharacters

- Regular expression caveats in dtSearch

- Common dtSearch regular expression examples


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

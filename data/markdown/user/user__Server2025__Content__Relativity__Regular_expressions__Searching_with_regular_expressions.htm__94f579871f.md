---
title: "Searching with regular expressions"
url: https://help.relativity.com/Server2025/Content/Relativity/Regular_expressions/Searching_with_regular_expressions.htm
collection: user
fetched_at: 2026-06-22T06:07:55+00:00
sha256: 1bea12d3305e8fbcf5fa74992c2d6216dfff23cc5629cdb9bece8b814b3aa404
---

Searching with regular expressions

# Searching with regular expressions (regex)

A regular expression is a form of advanced searching that looks for specific patterns, as opposed to certain terms and phrases. With regular expressions, you can use pattern matching to search for particular strings of characters rather than constructing multiple, literal search queries.

Regular expressions uses metacharacters in conjunction with a search engine to retrieve specific patterns. Metacharacters are the building blocks of regular expressions. For example, “\d” in a regular expression is a metacharacter that represents a digit character. “d” stands for the literal character, “d.” You can use regular expressions to search for social security numbers, patent numbers, URLs, email addresses, Bates numbers, and other strings that follow a specific pattern.

There are several implementations of regular expressions. The differences in implementations usually include the way special characters are handled and how character classes are treated.

For more information about other uses for regular expressions, see the following:

- Using regular expressions with dtSearch

- Regular Expression Searching – SSN and EIN

- Regular Expression Searching - Symbols

## Use cases for regular expressions

Regular expressions can help you in cases where you need to find different numbers that contain the same pattern.

Take, for example, the serial numbers in the first cell below. Instead of writing three literal search strings to match each serial number, you can construct one regular expression to match the serial numbers’ pattern. This single regular expression returns any document that contains any of the three serial numbers. In the second cell, there is another serial number with a slightly different pattern. By making a few adjustments to your regular expression string, your search results return documents with the new pattern.

Text Pattern/Regular Expression

- XFRD-8324-ERWH-3231

- GHSR-3413-KBKV-8173

- Pattern: 4 letters-4 digits-4 letters-4 digits

- Regular expression: [a-zA-Z]{4}-[0-9]{4}-[a-z]{4}-[0-9]{4}

- ABC.001.001.0001_0001

- xyz.123.123.1234_1234

- Pattern: 3 letters.3 digits.3 digits.4 digits_4 digits

- Regular expression: [a-zA-Z]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{4}_[0-9]{4}

Think of each regular expression as a phrase when you construct your search string. If you switch the order of the string you will not receive the same results.

- Unless you modify your dtSearch index to be case-sensitive, you cannot use capital letters when constructing a regular expression in dtSearch. Thus, if you are searching for varying strings that all begin with NLRT, such as:

- NLRT-0381

- NLRT-6334

- NLRT-9167

- The proper Relativity RegEx is: "##nlrt-\d{4}".

For more information about case-sensitive indexes, see Build a Case Sensitive dtSearch Index.htm .

## Regular expression metacharacters

Metacharacters are the building blocks of regular expressions. Characters in regular expressions are understood to be either a metacharacter with a special meaning or a regular character with a literal meaning.

The following are some common regular expression metacharacters and examples of what they would match or not match in regular expression.

Metacharacter

Description

Examples

\d

Whole Number 0 - 9

\d\d\d = 327

\d\d = 81

\d = 4

-----------------------------------------

\d\d\d ≠ 24631

\d\d\d does not return 24631 because 24631 contains 5 digits. \d\d\d only matches for a 3-digit string.

\w

Alphanumeric Character

\w\w\w = dog

\w\w\w\w = mule

\w\w = to

-----------------------------------------

\w\w\w = 467

\w\w\w\w = 4673

-----------------------------------------

\w\w\w ≠ boat

\w\w\w does not return boat because boat contains 4 characters.

-----------------------------------------

\w ≠ !

\w does not return the exclamation point ! because it is a non-alphanumeric character.

\W

Symbols

\W = %

\W = #

\W\W\W = @#%

-----------------------------------------

\W\W\W\W ≠ dog8

\W\W\W\W does not return dog8 because d, o, g, and 8 are alphanumeric characters.

[a-z]

[0-9]

Character set, at least one of which must be a match, but no more than one unless otherwise specified.

The order of the characters does not matter.

pand[ora] = panda

pand[ora] = pando

-----------------------------------------

pand[ora] ≠ pandora

pand[ora] does not bring back pandora because it is implied in pand[ora] that only 1 character in [ora] can return.

Quantifiers that allow pand[ora] to match for pandora is discussed below.

(abc)

(123)

Character group, matches the characters abc or 123 in that exact order.

pand(ora) = pandora

pand(123) = pand123

-----------------------------------------

pand(oar) ≠ pandora

pand(oar) does not match for pandora because it's looking for the exact phrase pandora.

|

Alternation—allows for alternate matches. | operates like the Boolean OR.

pand(abc|123) = pandabc OR pand123

?

Question mark matches when the character preceding ? occurs 0 or 1 time only, making the character match optional.

colou?r = colour (u is found 1 time)

colou?r = color (u is found 0 times)

*

Asterisk matches when the character preceding * matches 0 or more times.

The asterisk (*) in regular expression is different from * in dtSearch. Regular expression * is asking to find where the character, or grouping, preceding * is found ZERO or more times. dtSearch * is asking to find where the string of characters preceding * or following * is found 1 or more times.

tre*= tree (e is found 2 times)

tre* = tre (e is found 1 time)

tre* = tr (e is found 0 times)

-----------------------------------------

tre* ≠ trees

tre* does not match the term trees because although "e" is found 2 times, it is followed by "s", which is not accounted for in the regular expression.

+

Plus sign matches when the character preceding + matches 1 or more times. The + sign makes the character match mandatory.

tre+ = tree (e is found 2 times)

tre+ = tre (e is found 1 time)

-----------------------------------------

tre+ ≠ tr (e is found 0 times)

tre+ does not match for tr because e is found zero times in tr.

. (period)

The period matches any alphanumeric character or symbol.

ton. = tone

ton. = ton#

ton. = ton4

-----------------------------------------

ton. ≠ tones

ton. does not match for the term tones because . by itself will only match for a single character, here, in the 4th position of the term.Â In tones, s is the 5th character and is not accounted for in the regular expression.

.*

Combine the metacharacters . and *, in that order .* to match for any character 0 or more times.

.* in regular expression is equivalent to dtSearch wildcard * operator.

tr.* = tr

tr.* = tre

tr.* = tree

tr.* = trees

tr.* = trough

tr.* = treadmill

### Regular expression quantifiers

Regular expressions uses quantifiers to indicate the scope of a search string. You can use multiple quantifiers in your search string. The following table gives examples of the quantifiers you can use in your regular expression:

Quantifier Description Examples

{n}

Matches when the preceding character, or character group, occurs n times exactly.

\d{3} = 836

\d{3} = 139

\d{3} = 532

-----------------------------------------

pand[ora]{2} = pandar

pand[ora]{2} = pandoo

pand(ora){2} = pandoraora

-----------------------------------------

pand[ora]{2} ≠ pandora

pand[ora]{2} does not match for pandora because the quantifier {2} only permits for 2 letters from the character set [ora].

{n,m}

Matches when the preceding character, or character group, occurs at least n times, and at most m times.

\d{2,5} = 97430

\d{2,5} = 9743

\d{2,5} = 97

-----------------------------------------

\d{2,5} ≠ 9

9 does not match because it is 1 digit, thus outside of the character range.

### Escaping regular expression metacharacters

When using regular expressions to search for a character that is a reserved metacharacter, use the backslash \ to escape the character so it can be recognized. The following table gives an example on how to escape a reserved metacharacter when searching.

Search For Regular Expression Match Results

UK phone number

\+[0-9]{11}

+14528280001

+38119930978

-----------------------------------------

If the + sign is not escaped with a backslash, regular expressions treat + as a quantifier instead of the literal plus sign character.

## Additional resources

The following list contains additional resources for more information about using regular expressions:

- Regular expressions C++

- RegExr —useful for testing whether your regular expression is valid.

- Regular Expressions Cheat Sheet

- Regular Expressions - Users Guide

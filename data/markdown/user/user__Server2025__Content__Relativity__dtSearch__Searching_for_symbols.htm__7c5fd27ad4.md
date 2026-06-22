---
title: "Searching for symbols"
url: https://help.relativity.com/Server2025/Content/Relativity/dtSearch/Searching_for_symbols.htm
collection: user
fetched_at: 2026-06-22T06:07:33+00:00
sha256: 1f5719ffb1bd30e4626e689a15719ed9c7addb4e35e746283a145466f11687b9
---

Searching for symbols

# Searching for symbols

This topic describes how to make symbols searchable in a dtSearch index and how to use regular expressions to search for certain symbols reserved as search operators, such as the % sign.

## Searching for symbols

To search for symbols, perform the following steps:

- Create a dtSearch index.

- Update the alphabet file to include the % sign as an indexed character:

- Enter the following under [Letters] // Original letter, lower case, upper case, unaccented:

- [Space] [%] [Space] [%] [Space] [%] [Space] [%]

You must have a leading space. You cannot have a trailing space.

- Delete the % sign from the [Ignore] section. Take care not to remove the gray boxes, which represent non-printable characters. Removing them may break the index.

Before:

After:

- Repeat these steps for any other symbols that you need to make indexed. Delete the appropriate symbols from the [Spaces], [Ignore], or [Hyphens] sections. Please note, if you edit the hyphen, space, or ignore section, you will need to also keep the leading space. Removal of leading spaces will cause errors in Relativity.

- Perform a full build of the dtSearch index.

You can now search for terms containing the % sign using a regular expression. For example, if you need to search for documents that contain the term 75%, you would enter the following in your search box (ensuring you select the proper dtSearch index):

```text
"##75\u0025"
```

To break this regular expression down:

- ## signals to Relativity to treat the string as a regular expression

- \u indicates a search using a character's Unicode value (to follow in the next four characters)

- 0025 indicates the hexadecimal Unicode value for the % sign.

For most symbols, once you have indexed the character in the alphabet file, you can type them directly into the dtSearch box without using regular expressions. Thus to search for 30!, enter 30! into the dtSearch box after you have made ! an indexed character. You only need to employ RegEx for certain symbols.

For characters outside of the ASCII code range, such as § and £, you cannot make them searchable by adding them to the letters section. Instead, create an AdditionalLetters section at the bottom of the alphabet file and insert the characters' Unicode value.

## Symbol searching quick reference

Use the following table to quickly reference how to search for special characters. Note that you can search for the ampersand symbol without using RegEx.

Symbols Directions Example search term Example search string

$ & @ \ / + , . ; - ' ` ! < > { } ^ _ [ ] | Update the alphabet file and search.

- $75

- @75

- $75

- @75

? * ( ) # = Update the alphabet file and use RegEx with an escape character (\).

- #75

- 75?

- "##\#75"

- "##75\?"

" % : ~

Update the alphabet file and use RegEx with the hexadecimal Unicode value.

- 75~

- "##75\u007e"

Characters outside the ASCII code range such as § and £ Create an AdditionalLetters section at the bottom of the alphabet file and insert the character's Unicode value.

- £75

- £75

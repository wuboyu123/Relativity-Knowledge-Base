---
title: "Making the noise word and alphabet list searchable"
url: https://help.relativity.com/Server2025/Content/Relativity/dtSearch/Making_the_stop_word_and_alphabet_list_searchable.htm
collection: user
fetched_at: 2026-06-22T06:07:48+00:00
sha256: e524f3e9226b4eb9120ff8b936cd4555f2833248f62708fbc5b9b0abe2929b97
---

Making the noise word and alphabet list searchable

# Making the dtSearch noise word and alphabet list searchable

Relativity ignores words that don't act as meaningful criteria when you create dtSearch and keyword queries. Ignored words are known as noise words. Search indexes automatically include the default list of noise words. However, you can edit this list in the dtSearch list to suit your needs. This recipe includes an overview of noise words and steps to create custom lists.

## Default noise word list

Relativity references the default list of noise words each time you create a new index. System admins can't edit noise words in keyword searches. The default noise word list consists of punctuation marks, single letters and numbers, and the following words:

Begins with... Noise words

A a, about, after, all, also, an, and, another, any, are, as, at

B be, because, been, before, being, between, both, but, by

C came, can, come, could

D did, do

E each, even

F for, from, further, furthermore

G get, got

H had, has, have, he, her, here, hi, him, himself, his, how, however

I i, if, in, indeed, into, is, it, its

J just

L like

M made, many, me, might, more, moreover, most, much, must, my

N never, not, now

O of, on, only, or, other, our, out, over

S said, same, see, she, should, since, some, still, such

T take, than, that, the, their, them, then, there, therefore, these, they, this, those, through, thus, to, too

U under, up

V very

W was, way, we, well, were, what, when, where, which, while, who, will, with, would

Y you, your

Relativity ignores noise words. However, Relativity doesn't ignore their position in the search phrase set. So, if you execute the query apple w/6 pear , the search returns the phrase apple tree is far from the pear even though it contains the noise words is , from and the .

## dtSearches and noise words

The default list of noise words is the same in a dtSearch as in a keyword search. The primary difference is that you can customize the dtSearch index list. For example, if the word never is important to your litigation, remove it from the noise words list, so that your search results always return that word.

To create a custom noise word list, perform the following:

- Create a new dtSearch index, and then name it "dtSearch - updated noise words."

- Select your extracted text search for the Searchable set.

- Delete the word "never" from the Noise Words list.

- Save the list, and then perform a full build on your new index.

## Noise words in languages other than English

You can set up noise words to search documents in other languages. If the workspace primarily contains of documents in a different language, see this page for an overview of suggested noise words for use in nineteen additional languages.

## dtSearch alphabet file

The following descriptions are for characters in the ASCII 33-127 range.

### Letters

dtSearch defines letters as characters to index. This includes all alphabetic characters (a-z and A-Z) and all digits (0-9).

dtSearch is case insensitive.

### Hyphens

dtSearch defines hyphens as characters that receive special processing in dtSearch. By default, dtSearch only classifies the - character as a hyphen.

### Spaces

dtSearch defines a space character as a character that causes a word break. By default, dtSearch treats the following characters as spaces:

\09\0a\0c\0d !@"#$&'()*+,./:;<=>?[\5c]^`{|}~

Values listed as \## are Unicode code points. Their definitions are:

- \09 - horizontal tab

- \0a - line feed

- \0c - form feed

- \0d - carriage return

- \5c - backslash (\)

For more information, see dtSearch Unicode values for Special Characters . This article is found in the Relativity Community and you must log in to access it.

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

### Ignore

dtSearch defines an ignored character as a character that's ignored when processing text. By default, dtSearch ignores the following characters:

\08%

Values listed as \## are Unicode code points. Their definitions are:

\08 - backspace character

### End

dtSearch has defined ranges for CJK characters and these will make each Thai, Chinese, and Japanese character a separate word. See Setting up CJK document workspaces in Relativity for more detail.

### Searching for a symbol or character

To search for a symbol or character in Relativity, see Searching for a symbol .

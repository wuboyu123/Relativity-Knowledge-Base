---
title: "Language identification"
url: https://help.relativity.com/Server2025/Content/Relativity/Analytics/Language_identification.htm
collection: user
fetched_at: 2026-06-22T06:05:15+00:00
sha256: f3f2b9a3c2c0c46de19aab702fdbac2f11b148f11310eb279fe2c1c418d927fe
---

Language identification

# Language identification

Language identification examines the text of each document to determine the primary language and up to two secondary languages present. This allows you to see how many languages are present in your collection, and the percentages of each language by document. You can then easily separate documents by language and batch out files to native speakers for review.

This page talks about how language identification works. For steps to set it up, see Running structured analytics .

See the following related pages:

- Language identification results

- Structured analytics

- Running structured analytics

## How language identification works

For multi-language documents, language identification returns the top three languages found and their approximate percentages of the total text bytes. For example, 80% English and 20% French out of 1000 bytes of text means about 800 bytes of English and 200 bytes of French.

The operation analyzes each document for the following qualities to determine whether it contains a known language:

- Character set. For example, Thai and Greek are particularly distinctive.

- Letters and the presence or absence of accent marks.

- Spelling of words. For example, words that end in “-ing” are likely English.

Language identification is a naive Bayesian classifier, using one of three different token algorithms:

- For Unicode scripts such as Greek and Thai that map one-to-one to detected languages, the script defines the result.

- For Chinese, Japanese, and Korean languages, single letters are scored instead of multi-letter combinations.

- For all other languages, language identification ignores single letters and instead uses sequences of four letters, known as quadgrams.

It also ignores punctuation and HTML tags. Language identification is done exclusively on lowercase Unicode letters and marks; after expanding HTML entities; and after deleting digits, punctuation, and <tags>. For each letter sequence, the scoring uses the 3-6 most likely languages and their quantized log probabilities.

The analysis does not use a word list or dictionary. Instead, the engine examines the writing to determine the language. The training corpus is manually constructed from chosen web pages for each language, then augmented by careful automated scraping of over 100M additional web pages. The algorithm is designed to work best on sets of at least 200 characters, or roughly two sentences.

## Choosing a field for analysis

When you set up the structured analytics set, the optional Select field to analyze field controls what text the operation analyzes. By default, this is set to the Extracted Text field. Languages contained in other fields will not be analyzed.

For more information, see Creating a structured analytics set .

## Supported languages

Language identification supports 173 languages. See the Supported languages matrix for a complete list of the languages it can detect.

The analysis considers all Unicode characters, and it understands which characters are associated with each of the supported languages. For example, Japanese has several different character sets—kanji, katakana, and hiragana—all of which are supported.

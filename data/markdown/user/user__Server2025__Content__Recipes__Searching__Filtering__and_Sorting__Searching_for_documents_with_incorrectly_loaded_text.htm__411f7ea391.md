---
title: "Searching for documents with incorrectly loaded text"
url: https://help.relativity.com/Server2025/Content/Recipes/Searching__Filtering__and_Sorting/Searching_for_documents_with_incorrectly_loaded_text.htm
collection: user
fetched_at: 2026-06-22T06:17:33+00:00
sha256: a165404e6ea6fb31ec142ea19a8f035392db32c4d3e47f804100e6328da9c3cc
---

Searching for documents with incorrectly loaded text

# Searching for documents with incorrectly loaded text

If data is loaded with the wrong encoding selected, you must locate those documents and ensure they load into Relativity properly.

## Recipe overview

This recipe shows you how to search for documents that loaded into Relativity with encoding set incorrectly.

## Requirements

Applicable to all versions of Relativity.

## Directions

- Create a new dtSearch index with all of the noise words removed.

- Create a search terms report with all of the noise words using the index created above.

- Create a saved search with the following conditions:

- the STR field is not set AND

- the Extracted Text field is set

The results yield all documents with extracted text, but don't contain any noise words. Documents that fall into this category are the documents with the wrong encoding.

Documents in other languages may also appear in your results.

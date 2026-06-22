---
title: "Searching for documents with incorrectly loaded text"
url: https://help.relativity.com/Server2025/Content/Recipes/Searching__Filtering__and_Sorting/Searching_for_documents_with_incorrectly_loaded_text.htm
collection: user
fetched_at: 2026-06-22T06:17:33+00:00
sha256: a165404e6ea6fb31ec142ea19a8f035392db32c4d3e47f804100e6328da9c3cc
---

Searching for documents with incorrectly loaded text Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

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

On this page

- Searching for documents with incorrectly loaded text

- Recipe overview

- Requirements

- Directions


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

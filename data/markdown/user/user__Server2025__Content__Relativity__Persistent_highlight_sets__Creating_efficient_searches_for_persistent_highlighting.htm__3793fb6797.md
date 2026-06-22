---
title: "Creating efficient searches for persistent highlighting"
url: https://help.relativity.com/Server2025/Content/Relativity/Persistent_highlight_sets/Creating_efficient_searches_for_persistent_highlighting.htm
collection: user
fetched_at: 2026-06-22T06:16:12+00:00
sha256: 045a0f4319ebdd5541598aace135dd6c10154eff0fdf5b814aaf9c83e79ab9c8
---

Creating efficient searches for persistent highlighting

# Creating efficient searches for persistent highlighting

Creating efficient searches improves the performance of persistent highlighting, whether you're working with a Terms Search or Highlight Fields. Use the following guidelines to create efficient searches.

## Using terms search

Avoid the following when writing searches for persistent highlighting:

- Do not use "AND" or "OR" connectors. Persistent highlighting looks for the exact phrase, trade and complete, instead of the word, trade, and the word, complete.

- Proximity, fuzziness, and stemming logic cannot be used in a Terms Search. Consider using Highlight Fields to access these search features as described below. The system ignores the dtSearch syntax. Terms receive no highlight if you use these advanced searching features. The search terms report Count column still lists the number of matching terms. For example:

- The search term, oil w/10 water, searches for the exact phrase oil w/10 water.

- If you enter the term apply~ as a search term, persistent highlighting technology looks for the term apply followed by any special character.

- Avoid using terms with a large number of hits per document. Persistent highlighting highlights each hit. For example, it takes longer to load a Word document containing 1,000 instances of a single term.

- Avoid using terms that only occur once in a document. Use search terms reports for those terms instead.

- Avoid long lists of numbers, such as Bates numbers or account numbers.

- Do not use duplicate terms.

Use the following techniques to optimize your searches:

- Use the dtSearch Dictionary to identify variations of a term instead of using wildcards.

- Identify which terms should be in the highlight set and which terms are not necessary.

- You may want to avoid highlighting terms with high word counts.

To highlight terms using objects, create a fixed-length text field for your object called Highlight Colors. You can enter color-coding in this field using the format: [highlight color];[text color].

## Using highlight fields

Consider the following guidelines when creating or adding terms using Search Terms Reports as the highlight fields source:

- Enter terms exactly as they appear in the document.

- You can use operators such as AND and OR. For example, if you enter these search terms: Apple AND Banana, Relativity would highlight the two terms “apple" and "banana” in the document. See Search terms reports for more information.

- Wildcards are useful in some cases. For example, the search term appl* highlights apple, application, applies, and so on. An excessive use of wildcards affects performance. Leading wildcards such as *itting, are not recommended. Using asterisks in the middle of a term don't count as wildcards.

- dtSearch operators can be used to highlight searches when used for a Persistent Highlight Sets in the Native Viewer. You must use a Highlight Fields source (such as a Search Terms Report results field) to use dtSearch syntax. Relativity dtSearch operators are not supported in the Extracted Text Viewer. The highlights for these searches use the active and inactive highlighting functionality. Actively navigated highlights are the highlights that the Viewer is focused on and display with full opacity. Inactive highlights display at a lower opacity level.

The increase of dtSearch operators does decrease performance.

- Proximity searching logic can be used with Highlight Fields. If you enter the phrase "Relativity w/5 software" as a search term, the search term report uses a dtSearch to find and tag all documents that meet the criteria. When viewed in the Viewer, the persistent highlighting functions as a dtSearch. See Search terms reports for information.

- Stemming, including the stemming character (~), can also be used with Highlight Fields. If you enter the term "apply~" as a search term, the search term report finds and tags all documents with the word apply, or any document that stems from apply; including applied, applies, application, and so on. When looking at the document in the Viewer, the persistent highlight functions as a dtSearch. See Search terms reports for information.

- In Search Terms Reports, you can work around these limitations by using the Dictionary Search function to identify search terms using stemming or fuzziness. Copy the list of terms returned in this search. Paste them in the Add Terms box on the Search Terms Report form. Doing this enhances your search term list, while avoiding errors caused by special characters.

- Use the dtSearch Dictionary to identify variations of a term instead of using wildcards.

- Identify which terms should be in the highlight set and which terms are not necessary.

- You may want to avoid highlighting terms with high word counts.

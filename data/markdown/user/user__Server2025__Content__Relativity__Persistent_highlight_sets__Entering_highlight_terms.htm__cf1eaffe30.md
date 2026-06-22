---
title: "Entering highlight terms"
url: https://help.relativity.com/Server2025/Content/Relativity/Persistent_highlight_sets/Entering_highlight_terms.htm
collection: user
fetched_at: 2026-06-22T06:16:07+00:00
sha256: 70ba93fdfadd0ca6e9ba7a0eacd1bb9a4fc232bdbef9ac7b4b6603fd83ff53c3
---

Entering highlight terms

# Entering highlight terms

If you choose Terms as the source of your highlighting, you have to enter the terms in the Terms field text box to save the new highlight set. You also have the option of applying color-coding to these terms in the Viewer.

## Color-coding persistent highlights

When you enter a term in the Highlight Terms box, you can also specify the color for both the text and the background. Use the following format to color-code your persistently highlighted text:

[background color];[text color];[term to be highlighted]

For example, enter “3;16;Relativity” to highlight Relativity with dark green background and white text.

The auto-contrast feature automatically determines the text color based off the background color you select to ensure readability no matter which colors are selected. For example, if the background color is closer to black, the text will automatically be white or if the background color is closer to white, the text will automatically be black.

Highlights are rendered at full opacity (using the original highlight color) when they are active. When they are not active, they will be rendered in a lighter shade of the original highlight color.

The opacity level of the highlights can be adjusted by editing the value of the ViewerHighlightStyleDefault instance setting.

The following table includes available color codes.

Color name Highlight Color Number

[Default] 0

Black 1

Dark red 2

Dark green 3

Dark yellow 4

Dark blue 5

Dark magenta 6

Dark cyan 7

Light gray 8

Gray 9

Red 10

Green 11

Yellow 12

Blue 13

Magenta 14

Cyan 15

White 16

Light green 17

Light blue 18

Light yellow 19

Light purple 20

Light red 21

Light orange 22

Purple 23

Orange 24

Dark purple 25

Dark orange 26

If you enter terms with no color-coding, the background defaults to magenta and black text.

Default has different implications for text and background. The default background color is white and the default text color is black.

## Guidelines for adding terms or phrases

Use the following guidelines when adding terms or phrases into the Terms text box:

- Enter a term that you want highlighted and press Enter . You can enter multiple terms but each one must be on a separate line.

- Enter terms for persistent highlighting exactly as they appear in the document. Don't use quotation marks and connectors.

Quotation marks are not compatible with persistent highlighting with terms as a source, which automatically searches for an exact phrase. Quotation marks are compatible when using highlight fields as a source however. Using highlight fields as a source can result in slower document loading speeds.

- Keep lists simple. Do not use punctuation, special characters, or operators. Do not use dtSearch syntax when entering a list of terms as the source for the set. You may use dtSearch index terms in a search terms report, then use Fields as the Persistent Highlight Source instead to support highlights for dtSearch syntax.

- AND or OR operators are not used in keyword searching. If used, Relativity looks for the exact phrase including AND or OR . For example, you entered these search terms: Apple AND Banana . Relativity highlights the entire phrase apple and banana in the document. Separate occurrences of apple , and occurrences of banana , are not highlighted.

- Persistent highlight set terms do support wildcards. You can view highlighted terms that contain an * (asterisk) character, including a wildcard in the middle of a term. For example:

- term* matches and highlights any word that starts with term with zero or more following characters.

- *term matches and highlights any word that ends with term with zero or more preceding characters.

- *term* matches and highlights any word that has term in it with zero or more preceding or following characters.

- Do not enter duplicate terms.

- Identify and remove terms with large hit counts.

- List variations of a term first and enter the root term last.

- If the list of terms is large (>100 terms), use Highlight Fields with a Search Terms Report. For more information, see Search terms reports .

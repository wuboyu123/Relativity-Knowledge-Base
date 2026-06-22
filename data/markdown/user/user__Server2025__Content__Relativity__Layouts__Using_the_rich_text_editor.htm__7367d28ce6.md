---
title: "Using the rich text editor"
url: https://help.relativity.com/Server2025/Content/Relativity/Layouts/Using_the_rich_text_editor.htm
collection: user
fetched_at: 2026-06-22T06:08:50+00:00
sha256: c8dc0e9a07eb59fc18e841be73fecf1f7531b2a8faf8852fb5ab6571356b4e2e
---

Using the rich text editor

# Using the rich text editor

The rich text editor provides support for hyperlinks, images, and tables.

It also features the following:

- Supports both inline and pop-up display type for a more seamless experience. See Adding fields and text .

- You can configure the maximum text values for long text fields using the instance setting MaximumNumberOfCharactersSupportedByLongText .

The rich text editor is available in several circumstances:

- Long Text field - the Enable HTML field option is enabled on a long text field which is added to a layout. See Enable HTML in Field Information .

- Set the long text field with the Display Type: Inline Rich Text.

- On the layout builder, make the long text field two column. This will render the inline text editor as a two column width in an RDO layout. See Adding fields and text .

- Contextual help or Custom text - when adding contextual help or custom text to a layout. See Layouts .

- Custom Label - when adding a custom label to a field.

The Sanitizer object controls whether HTML attributes are sanitized and how specific HTML content is sanitized from fields on page render. You can modify the sanitizer object to add HTML alerts and links. We recommend not modifying the default setting. For more information, see Sanitizer object .

## Rich text editor features

The rich text editor contains the following features:

- - change the font type. Arial is the default font type. You can configure the default font using the instance setting, RichTextEditorFontDefault. See RichTextEditorFontDefault .

In Microsoft Internet Explorer and Edge, the font type drop-down menu does not appear. You can, however, change the default font face in IE using the RichTextEditorFontDefault instance setting. See RichTextEditorFontDefault .

- - change text font size.

- - changes selected text background highlight color.

- - changes selected text color.

- - bolds selected text.

- - italicizes selected text.

- - underlines selected text.

- - adds a strikethrough to selected text.

- - add subscript or superscript to selected text.

- - arrange content in a bulleted or numbered list, outdent or indent text, and align text left, center, or right.

- - customize the space between each line of text.

- - insert hyperlink. Here, you can specify the URL, link text, and whether the link opens in a new tab.

If the default HTMLSanitizerWhitelist is in place, links will need to follow the following format: start with https://, and can include forward slashes, periods, and alphanumeric characters. Example: <a href=”https://www.relativity.com/customers/” >Relativity Customers</a>.

- - insert an image from a URL. You can re-size the image in the text editor.

If the default HTMLSanitizerWhitelist is in place, links will need to follow the following format: start with https://, and can include forward slashes, periods, and alphanumeric characters. Example: <img src="https://i.imgur.com/m1TEWWW.png" />.

- - insert a table.

- - cut or copy selected content.

- - select to enable spell check as you type and de-select to disable spell check. You can configure whether spell check is turned on or off by default using the instance setting, RichTextEditorSpellCheckDefault. See RichTextEditorSpellCheckDefault .

- - use to undo or redo actions taken in the rich text editor.

### Copying and pasting

You can copy and paste from Microsoft Word with most formatting staying intact. Always double-check formatting before saving the communication because formatting from another application may not be carried over.

Copying and pasting bullet or numbered lists from MS Word, Chrome, and Firefox convert into HTML lists in the rich text editor. The HTML lists will consist of <ul/> and <ol/> tags in the editor. These pasted lists can then be edited in like other lists in the editor.

Copying and pasting into the rich text editor only works when copying from MS Word, Chrome, and Firefox. This is currently not possible for Internet Explorer 11.

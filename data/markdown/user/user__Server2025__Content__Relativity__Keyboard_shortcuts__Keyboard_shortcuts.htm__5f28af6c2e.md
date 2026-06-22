---
title: "Keyboard Shortcuts"
url: https://help.relativity.com/Server2025/Content/Relativity/Keyboard_shortcuts/Keyboard_shortcuts.htm
collection: user
fetched_at: 2026-06-22T06:06:46+00:00
sha256: e4034dbdb693a28541d6a3c80524eaeb5a36327da58400186ddbdfb202a05c3b
---

Keyboard Shortcuts

# Keyboard shortcuts

With keyboard shortcuts you can edit and navigate in the Review Interface. Using keyboard shortcuts, you can change Viewers, populate choices, save edits, cancel edits, and move between and within documents. Keyboard shortcuts are enabled by default. To disable shortcuts while using the Review Interface, click on the Viewer Settings menu in the upper-right and select the Disable Keyboard Shortcuts option.

Users with permissions to edit fields and choices can create additional shortcuts using the Keyboard Shortcuts property on the choice.

You can modify the key combinations for system keyboard shortcuts if you have security permission for the Admin Operation called Modify System Keyboard Shortcuts . For more information about this permission see workspace security .

## Keyboard shortcuts legend

By default, standard user actions use system keyboard shortcuts. Keyboard shortcuts are listed in the Keyboard Shortcut Legend along with those used by the browser. You can access the legend by clicking on the Viewer Settings menu in the upper-right of the Review Interface and selecting the Keyboard Shortcut Legend option.

Within the legend, you can sort, filter, Export to Excel, and print. You can print by right-clicking and choosing the browser's print option.

The Keyboard Shortcuts Legend includes the following sortable columns:

- Keyboard Shortcut - the key combination used to execute the shortcut during document review.

- Action - the action that results from using the keyboard shortcut.

- Viewer Mode - the type of Viewer for which each shortcut is available. You can use most of the system category shortcuts in all viewer modes.

- Category - the shortcut type. Below, the legend displays only those shortcuts designated by the System and the browser. This column also lists all field and choice shortcuts that your system admin configured via field and choice properties.

## Special considerations for keyboard shortcuts

Keep in mind the following when working with Relativity’s keyboard shortcuts feature:

- For Mac users, keyboard shortcuts marked with Ctrl map over to the Command key.

- Keyboard shortcuts are active when:

- Keyboard shortcuts are enabled.

- Focus is in the Review Interface.

- The Viewer is either docked or undocked while the browser only has one tab open.

- If the shortcut overlaps with a Windows shortcut, both shortcuts are triggered. For example, if a program installed on a user’s computer uses the Ctrl + Alt + R shortcut, clicking Ctrl + Alt + R triggers that action regardless of whether a user is in any of Relativity's supported browsers.

- Keyboard shortcuts aren't triggered when:

- Keyboard shortcuts are disabled.

- Focus is not in the Review Interface.

- The Viewer is undocked or in standalone mode, and the browser has more than one tab open.

- When the numbers 0-9 are used as shortcuts, they only fire when you press these digits in the main section of the keyboard. The shortcut doesn't fire if you press those digits found in the keypad.

- Keyboard shortcuts only execute in the Review Interface.

- Keyboard shortcuts only execute in the Viewer Modes listed in the legend.

- If the document viewer is undocked, shortcuts that move the cursor focus to a text box only execute if the browser has a single tab open.

## Document field type shortcuts

The following table outlines what document field types users can define shortcuts for and what behavior the shortcuts trigger. You can also define keyboard shortcuts on individual choices for single & multiple choice fields, rather than the field itself. See the Document choice shortcuts table below for information on setting keyboard shortcuts for individual choices.

Field Type Can define shortcut? Layout Display Type Behavior

Fixed Length Text Yes Text Focus jumps to textbox

Long Text Yes Text Only Focus jumps to textbox

Rich Text

NO ACTION

Date Yes Date Focus jumps to textbox

Whole Number Yes Integer Focus jumps to textbox

Decimal Yes Decimal

Currency Yes Currency

User Yes Drop-down menu Drop-down menu choices are toggled

Picker

NO ACTION

Boolean Yes Checkbox Checkbox state is toggled

Drop-down menu

Drop-down menu choices are toggled

Radiobutton

Radio button selected

Single Choice No

Multiple Choice No

Single Object No

Multiple Object No

File No

## Document choice shortcuts

The following table outlines what document individual choices users can define shortcuts for and what behavior the shortcuts trigger:

Choice Type Can define shortcut? Layout Display Type Behavior

Choice associated with Document Single Choice Field Yes Radio button Choice is selected/deselected

Drop-down menu Choice is selected/deselected

Choice associated with Document Multiple Choice Field Yes Checkbox Choice is selected/deselected

Popup Picker NO ACTION

---
title: "Creating persistent highlight sets"
url: https://help.relativity.com/Server2025/Content/Relativity/Persistent_highlight_sets/Creating_persistent_highlight_sets.htm
collection: user
fetched_at: 2026-06-22T06:16:05+00:00
sha256: 104d2102f237d7e0d24bcce8b2e7dddf1e415762d8ffb5d193650a927fecf5ea
---

Creating persistent highlight sets

# Creating persistent highlight sets

To create a new persistent highlight set, follow these steps.

If you plan to use the Source: Highlight Fields, you may need to create a search terms report. For more information, see Using the highlight fields source .

- Navigate to the Persistent Highlight Sets tab.

- Click New Persistent Highlight Set .

- Complete all required fields in the Persistent Highlight Set Information section. See Fields for details.

- Click Save .

Verify that reviewers are not actively reviewing documents when creating persistent highlight sets. Creating persistent highlight sets while reviewers are actively reviewing documents can cause errors.

## Fields

Persistent highlight sets include the following fields.

- Name - the descriptive name under which you want this set to appear in the Viewer and item list.

- Order -the order in which you want this set to appear.

- Source - determines the area the set draws from when designating characters to be highlighted and displayed in the Viewer. There are two options:

- Highlight Fields - designates fields as the source of highlighting. Highlight Fields is capable of using dtSearch functionality. Selecting this radio button means you must select a Highlight Field in order to save this set.

- Terms - designates terms as the source of highlighting. Selecting this radio button means you must enter terms into the Terms field below to save this set.

- Highlight Fields - choose the field referencing the list of terms to be highlighted. Click the button to bring up the system view called Field Picker on Persistent Highlight Sets, which displays the Name and Object Type for applicable multiple object fields. It also includes those created by search terms reports. To select the desired Highlight Field, check the field’s box, click Add, and click Set. The field displays on the layout. See Using the highlight fields source .

If your search terms report is run against a dtSearch index with a customized alphabet file, the hits on the STR may not match the highlights rendered in the Viewer. Depending on how the alphabet file has been customized, you may see fewer highlight hits rendered in the Review Interface.

- Terms - enter terms you wish to highlight and select the color code to distinguish them in the Viewer. See Entering highlight terms .

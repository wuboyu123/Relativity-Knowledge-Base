---
title: "Mass edit"
url: https://help.relativity.com/Server2025/Content/Relativity/Mass_operations/Mass_edit.htm
collection: user
fetched_at: 2026-06-22T06:08:02+00:00
sha256: 7cc565b978ae9115fd6e60b0085c1446a8d2ecfe2d35b52c0057c3d16a83c41f
---

Mass edit

# Mass edit

You can use the mass edit operation to modify fields and coding values for multiple documents or objects at the same time. You can use any layout that you have rights to. Mass edit is available from the mass operations bar.

You can't use mass operations on Data Grid-enabled fields.

To perform a mass edit operation, perform the following steps:

- From the mass operations bar on the document list, choose whether to edit All searchable items, Checked items or These items in the current returned set.

- Select Edit in the drop-down menu.

The Mass Edit form displays. Using the drop-down menu, you can select from all layouts you have rights to see.

- Select to edit the layout and fields.

There are three options for multiple-choice field values, known as a tri-state check box:

- Blank removes the value from any of the selected documents.

- Shaded leaves any values on the selected documents as-is.

When mass editing Yes/No fields, the shaded check box sets the value to null.

- Checked applies the option to all selected documents.

- Click Save to apply your changes.

## Working with multi-choice fields on the mass edit form

In the mass edit form, there are two options for editing multi-choice fields: a checkbox or a pop-up picker. When you select the pop-up picker as the display type during the layout build, there are two options to edit the field: Check and Uncheck .

Click Check to create a list of items to add to the field. Click Uncheck to create a list of items to remove from the field. Items not selected remain unchanged. Clicking either Check or Uncheck opens the Available Items window.

From the Available Items window, you can move choices and objects into the Selected Items list below. Select the check box next to the desired selection, and then click Add . This builds a list in the bottom window of selected items. To remove something from this list, select it and click Remove . Click Set to proceed with the action to Check or Uncheck the items from the field. Cancel stops any action.

Below, the mass edit form reflects checked and unchecked objects and choices.

Once values have been set, a Clear link displays next to the Check and/or Un-Check buttons. You can then clear the set values without returning to the Items to Check window to remove them. You can add a new choice to a multi-choice field using the Add link.

Click Save to apply your updates and redisplay the item list. If the item list loads slowly, and you cancel the request, your updates to the documents remain saved.

When you attempt to mass edit documents in the Related Items pane while there are unsaved changes in the current layout, Relativity displays a message indicating that your changes will be lost. If you continue, the coding values in the layout are updated to match those selected for the mass edit.

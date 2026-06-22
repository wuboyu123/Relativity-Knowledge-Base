---
title: "Imaging native types"
url: https://help.relativity.com/Server2025/Content/Relativity/Imaging/Imaging_native_types.htm
collection: user
fetched_at: 2026-06-22T06:14:21+00:00
sha256: f4fc44d2e733633d252673af5afd4d4094a1df88896917b4ef7252682a882cf0
---

Imaging native types

# Imaging native types

On the Native Types tab, you see a list of file types that Relativity supports. Refer to this list when selecting file types that you want to restrict from imaging. The Relativity Desktop Client also supports the same list of file types.

To locate specific file types, use the Show Filters option or create a new view to customize the content that appears on the tab. Default restricted file types propagate to new imaging profiles. You can edit the default value for the option that restricts the imaging of a file type and also edit the option that prevents native download for specific file types by clicking the Edit link.

If you restrict a particular file type, Relativity doesn't apply the restriction you choose to previously-existing Imaging Profiles. Restricted file type settings only affect Imaging Profiles that you create after you edit the setting.

## Editing a native type

- Click the Edit link for a file type. You can also click the Edit button on the details page.

- On the edit form, select the Yes or No radio button for the Restricted From Imaging By Default option. This value is set to No by default.

- Select the Yes or No radio button for the Prevent Native Download option. This value is set to No by default. If the Prevent Native Download option is set to Yes, all users of that workspace will not see the Native button in the Viewer for files of that particular type.

- Click Save.

## Generating a complete list of native types and their respective imaging engines

Use the following steps to generate a .CSV file that lists all native types and their imaging methods, categories, restriction status, and native download prevention status:

- Navigate to the Native Types tab.

- Select All in the mass action drop-down menu in the lower left.

- Select Export to File in the mass action drop-down menu.

- Click Go .

Relativity doesn't support Framesets in MHT files.

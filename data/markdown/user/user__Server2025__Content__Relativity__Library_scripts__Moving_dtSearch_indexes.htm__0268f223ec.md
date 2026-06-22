---
title: "Moving dtSearch indexes"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Moving_dtSearch_indexes.htm
collection: user
fetched_at: 2026-06-22T06:07:44+00:00
sha256: 5836f92a4bf292553a17393ec39515bd9060075ee8c2c0f8c7f72ca74fa18277
---

Moving dtSearch indexes

# Moving dtSearch indexes

This page outlines the steps for moving dtSearch indexes from their current location to a new location.

## Requirements

In order to perform this task, you need access to a SQL Server where the Relativity custom SQL utility was automatically installed with Relativity and a system admin account within Relativity.

The custom SQL utility is located at the following file path:

C:\Program Files\kCura Corporation\Relativity\Procuro\kCura.EDDS.CustomSQL.exe

Before you begin, verify the size of the existing dtSearch indexes and confirm that the new location has adequate disk space to house this and any new indexes which may be created.

## Special considerations

Moving indexes is a reasonably safe procedure. However, problems can arise if Relativity attempts to access the indexes during the move. Accordingly, ensure:

- No new indexes are created during the move.

- Existing indexes are not incrementally built during the move.

We recommend that you perform the move during off hours or a down period to minimize any potential issues.

## Moving dtSearch indexes

In order to successfully move the dtSearch indexes the following steps must be completed.

### Pre-move

First, prepare the new location.

- Create a new shared folder.

- Grant the Relativity Service Account full rights to the new folder.

- Verify that the share is accessible from the Relativity Web Server and the Agent server.

- Add the new index share as a choice for the dtSearch Index Share Location field via the Choices tab from Home.

- Add the share to the appropriate Resource Pools to make it available for use.

### Moving the indexes

Once the new location is prepared, you can move the dtSearch indexes.

- Copy over the indexes to the new location.

- Open the custom SQL utility on any RelativitySQL Server where it's installed and click Select All to select all of the workspace databases, unless you are only planning to move indexes for certain workspaces.

- Select the Execute Custom SQL button and copy the contents of the dtSearch Move.sql script into the Execute Custom SQL window.

- Be sure to follow the instructions noted in the script, updating the appropriate lines to specify the old and new IndexShareCodeArtifactIDs.

- This will only update indexes at the specified old location to the specified new location. Any other locations must be updated separately.

- To find the IndexShareCodeArtifactID of the old and new index shares, you can run the following query against the EDDS database and reference the ArtifactID column in the results for the corresponding locations:

SELECT * FROM [EDDS].[eddsdbo].[Code] WHERE CodeTypeID = 8

- Leave the Include EDDS Database checkbox unchecked and click the Execute button. This script updates the appropriate tables in the SQL database for each workspace to reference the new location of the dtSearch indexes.

### Verifying the move

The final step is to confirm the move was successful.

- Login to Relativity and select a workspace that has a dtSearch index.

- Click on the Search Indexes tab, and select the existing dtSearch index.

- Ensure that the dtSearch index references the new location.

- Create a new dtSearch index and confirm it populates with the new index location.

- Navigate to the Documents tab.

- Select a dtSearch index from the Search drop-down menu.

- Run a dtSearch query to verify the success of the move.

---
title: "Check for production conflicts"
url: https://help.relativity.com/Server2025/Content/Relativity/Production/Production_console/Check_for_production_conflicts.htm
collection: user
fetched_at: 2026-06-22T06:08:46+00:00
sha256: 077749c0ae9c2ddac43ae97001b4f28af840dfb0ea12cc06537f35754cdba663
---

Check for production conflicts

# Check for production conflicts

You can perform a conflict check that compares the documents in the production against those in a saved search selected in the Production Restrictions field on the workspace details page. For example, the saved search may include conditions that identify privileged documents and their families, which you would not want to produce. See Production restrictions .

You must have permissions to the documents included in a production to remove production restrictions.

When you click Check for Conflicts , a Production Restrictions warning may appear if a saved search is being used to restrict productions.

Click one of these buttons to resolve the conflict:

- Remove Conflicts - deletes documents identified as conflicts from the production set (based on the Production Restrictions setting). If all the documents are conflicts, they are removed from the production set.

To view a list of documents removed from the production, navigate to the History tab, and filter on the Production - Remove Document action. See History for more information .

- Cancel - stops the conflict check and displays the production page.

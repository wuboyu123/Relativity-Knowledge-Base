---
title: "Building views for checked-out documents"
url: https://help.relativity.com/Server2025/Content/Relativity/Batches/Building_views_for_checked-out_documents.htm
collection: user
fetched_at: 2026-06-22T06:14:32+00:00
sha256: 812823658e91e95ddc74e25d04b87ee5b3c7a2d3c71a533c21a6f3c11c305c66
---

Building views for checked-out documents

# Building views for checked-out documents

You can build views for checked-out documents to better assist users in keeping track of the documents they have checked out in a batch.

Also see the following pages:

- Batches

- Assigning batches and checking batches in and out

## Build a checked-out documents view

You can build views for a reviewer to access their checked-out documents. For more details about creating a view, see Views . Use this procedure to create a view for checked-out documents.

- Click the Views subtab from the Administration tab.

- Click New View .

- Complete the required fields. See Views for details.

- In the Set Conditions section, choose Batch in the Field drop-down list.

- Click in the Value field. The Batch Criteria Selector displays.

To create a simple view that shows the reviewer their checked-out documents, you could create the following conditions; however, you can make your conditions as simple or complex as your workspace's workflow requires.

- Field - Batch::Assigned To

- Operator - is logged in user

and

- Field - Batch::Status

- Operator - any of these

- Value - In progress

- Click OK .

- Click Save .

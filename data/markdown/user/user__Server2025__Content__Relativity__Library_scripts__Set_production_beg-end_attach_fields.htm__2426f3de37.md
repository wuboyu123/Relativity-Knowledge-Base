---
title: "Set production beg/end attach fields"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Set_production_beg-end_attach_fields.htm
collection: user
fetched_at: 2026-06-22T06:15:37+00:00
sha256: 4d420cca5071d0267d8694ecce1ed9b2025311f148a63a66cdfc8ed044dd03e2
---

Set production beg/end attach fields

# Set production beg/end attach fields

This script populates the production beginning and end attachment range fields for each document included in a production. This is a case functionality script to be run at a case level.

## Special considerations

The risks outlined below must be considered when running this script:

- This script can't be undone.

- The script may run for some time without reporting any progress.

- This script utilizes the Family Identifier field, which must be present and valid.

- This script updates the Document table.

## Inputs

Before running the script:

- Run a production

Also, ensure that the Attachment relational field is set in the production settings for the following multi-object fields:

- Production::BegAttach

- Production::EndAttach

You can still run this script after running a production if the Attachment relational field wasn’t set on the production.

## Results

Once run, this script updates:

- The BegAttach field with the beginning bates of the family group

- The EndAttach field with the end bates of the family group

If you want to combine the attachment bates range data into one field for a singular range, run the Copy to Legacy Document Fields script, then mass replace those fields into the document object fields. See Copy To Legacy Document Fields .

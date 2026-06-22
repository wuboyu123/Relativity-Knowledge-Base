---
title: "Propagate sent date to family documents"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Propagate_sent_date_to_family_documents.htm
collection: user
fetched_at: 2026-06-22T06:15:27+00:00
sha256: 375a507055c0f20bd330e27161dc9e6af69c5d004a66c380d9949131cae79342
---

Propagate sent date to family documents

# Propagate sent date to family documents

This Relativity script sets all email families documents to the same sent date as their parent documents in a case. This allows for chronological sorting within all documents.

This is a case functionality script to be run at a case level.

## Special considerations

Consider the following when running this script.

- This script cannot be undone.

- The script may run for some time without reporting any progress.

- This script updates the Document table.

## Inputs

Before running the script, complete the following inputs:

- Date Field - Original - the date field that is read.

- Date Field Sort - the date field that date is written to.

- Family Identifier - the relational field used to identify which documents are grouped together.

- Date Propagated - a Yes/No field that indicates which documents the script updates, also letting the user know where data is changed.

- Document Sort Field - instead of using ArtifactID to order documents in each family, use this input to select your choice field in which to order documents by. This accounts for some document families where the lowest ArtifactID isn't the parent.

## Results

Once this script has been run, the Sent Date field will be updated so all family documents in a case have the same value as their parent document. The parent must be the record with the lowest ArtifactID.

This script ignores records where the field assigned to Date Propagated field is set to Yes. As a result, this script will only affect documents where this field is empty or set to No.

---
title: "Searching for custom object information on the Document object"
url: https://help.relativity.com/Server2025/Content/Recipes/Searching__Filtering__and_Sorting/Searching_for_custom_object_information_on_the_Document_object.htm
collection: user
fetched_at: 2026-06-22T06:17:30+00:00
sha256: c2125d6775016adb8c53138494008eb7092fac8b3c9d7307313c261b8df5a960
---

Searching for custom object information on the Document object

# Searching for custom object information on the Document object

To search for custom object information on the Document object create a multiple object field that links both objects together.

## Recipe overview

You can search for the custodians' information from the document object using a custom custodian object. The workspace should also contain documents associated with certain custodians.

## Requirements

This recipe is applicable to all Relativity versions.

## Directions

To search for custom object information on the Document object, perform the following steps:

- Create a multiple object that links the Document object to the custom Custodian object. In this example, Custodian Obj Linker is the name of the multiple object .

- Set Open to Associations to Yes on the Custodian object fields you want to make searchable on the Document object (in this example, the Start Date and End Date).

When creating a new Saved Search, or toggling search conditions on, you can search across your Custodian object Start Date and End Date fields. Look for the field name that starts with the name of your multiple object. In this example, it is Custodian Obj Linker.

You can also filter on the Custodian object Start Date and End Date fields by adding them to a view on your Document object.

You can now filter on these date fields on this Document view.

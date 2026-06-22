---
title: "Language identification setup basics"
url: https://help.relativity.com/Server2025/Content/System_Guides/User_quick_reference/Analytics/Language_identification_setup_basics.htm
collection: user
fetched_at: 2026-06-22T06:10:38+00:00
sha256: 7b0b0597549963148658d545a0ce6e262c2ba9ede75938fb45a0b6007f150a89
---

Language identification setup basics

# Language identification setup basics

This quick reference guide contains a basic workflow for identifying the languages used in your documents. For more detailed information, see Analytics .

## Language identification setup

The setup for running language identification is comprised of three components:

- Saved search

- Structured analytics set

- View

### 1. Saved Search Setup

Use the following conditions and fields to create the saved search used for language identification. You do not need to set a sort order on this search.

- Search Name —there is no recommendation for the saved search name. Follow your team’s normal protocol for naming searches.

- Conditions —extracted text size is greater than 0KB.

- Fields —any fields are acceptable.

### 2. Structured Analytics Set

Here are the steps and choices for creating a structured analytics set.

- Name —enter a name for the structured analytics set.

- Prefix —keep the default prefix or add your own prefix. Shorter prefixes (even just two characters, such as “LI”) take up less space in your views.

- Operations to run —select Language identification .

- Data source —select the saved search you created above.

### 3. Language ID view

Once you run the structured analytics set, create the following view to see the results of your language identification operation.

- Fields

- Control Number

- [SAS Prefix]::Primary Language

- [SAS Prefix]::Docs_Languages

- [SAS Prefix]::Docs_Languages:Language

- Conditions —[SAS Prefix]::Primary Language is set

- Sort —you do not need a specific sort order for this view. However, you can create separate searches and views for each document set as well as widgets and dashboards.

---
title: "Common Saved Searches application"
url: https://help.relativity.com/Server2025/Content/Relativity/Saved_search/Common_Saved_Searches_application.htm
collection: user
fetched_at: 2026-06-22T06:16:38+00:00
sha256: 6658c8efc8f5f6bc76077f81d1976d925a865f264c3956afae86bfff9d4f507a
---

Common Saved Searches application

# Common Saved Searches application

This topic describes how to install and use the Common Saved Searches application, which contains a group of searches that can assist you in your basic usage of Relativity.

## Installing the application

The installation process follows the same steps used to install other Relativity applications. For more information, see Installing applications .

You must have system admin permissions to install an application. See Workspace security .

To install the application:

- To download the application rap file, go to Common Saved Searches Application .

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

- Click Download .

- Add the application to the Application Library:

- On the Applications & Scripts tab, click the Application Library tab.

- Click Upload Application .

- Click Choose File , navigate to and select the Common Saved Searches Application rap file, and then click Open .

- Click Save .

- Click Install in the Workspaces Installed section to install the application on workspaces.

- Click in the Workspaces field to display the Select Workspaces dialog.

- Select a workspaces to install the application, and then click Ok .

- (Optional) Click Clear to remove a workspace from the list.

- Click Save to install the application to the selected workspaces.

There may be a need to map fields if you have a template already created with the same common fields. For more information, see Mapping fields .

## Using the application

The table below lists the search name and the description of why this search is used and/or what it returns.

Search Name Description

All Documents

A quick, easy way to return all documents in the workspace. This is useful for many reasons, including building Search Term Reports and is a method to quickly grab everything.

01.01 Processing Errors Returns all documents in document table that have an error from processing. Use this to find items that might provide reviewers issues.

02.01 dtSearch Returns all documents, but more importantly, returns only the extracted text field. Use to build a dtSearch index.

02.02 Structured Analytics Set Used to check for documents with text and is used for any of the structured analytics sets.

02.03 Email Threading - Parent Emails Search for emails, but only parent level items, not attachment emails. Previously used for email threading. Items used for threading.

02.04 Near Duplicate Analysis (No Parent Emails) Returns all files that are identified for near duplication analysis, but are not parent emails.

02.05 Language ID or Repeated Content Records with text to be used for Language ID or Repeated content similar to Structured set.

02.06 Analytics Not Included

Returns items not included in Analytics because of text size.

02.07 Analytics Index Returns documents containing text and returns only extracted text for Analytics Indexes.

02.08 All docs Email Metadata fields Returns all emails with all metadata fields returned.

03.01 Extracted Text is Empty Includes documents not returned for use in Analytics Index for lack of text.

04.01 Parent Level Documents Returns top-level documents that are not attachments, but can be emails or other.

04.02 Document Level Documents Returns child-level documents.

04.03 Parent Level Dupes + Family Returns parent duplicates with family added. Duplicate not determined on family.

05.01 Single Recipient Emails + Family Returns emails with one recipient and their attachments.

05.02 Bulk Emails (50+) + Family Returns emails with 50 or more recipients and attachments.

06.01 Search Term Report Search across all emails with text for STR.

06.01 Responsive and Family Returns documents with Designation set to Responsive and family included.

06.02 Conflicts with Family Returns items not coded the same as parent items.

06.03 Produce with Images Placeholders Returns items marked with choice in Productions field, Nothing in Bates field, and Check on type of production as Images with Placeholders.

06.04 Produce Natives Only Returns items marked with choice in Productions field, Nothing in Bates field, and Check on type of production as Native only.

06.05 Produce Natives with Placeholders Returns items marked with choice in Productions field, Nothing in Bates field, and Check on type of production as Native with Placeholders.

By Filetype Returns all documents with a filetype sorted by filetype.

By Folder Returns all documents with a folder path and sorted by folder path.

---
title: "Installing the Transcripts application"
url: https://help.relativity.com/Server2025/Content/Relativity/Transcripts_application/Installing_the_Transcripts_application.htm
collection: user
fetched_at: 2026-06-22T06:08:52+00:00
sha256: 5c66920bb6dab88c42446caaee5926df6abfc40334a30f7d68dae46cf8e45b4e
---

Installing the Transcripts application

# Installing the Transcripts application

The latest version of the Transcripts application can be found in the Application Library and is part of the upgrade process. See Installing applications .

This application is also available for download in the Relativity Community . Search for the name of the file, and then select the Files tab in the search results.

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

## Transcripts application compatibility matrix

Transcripts application version Relativity Server 2024 Relativity Server 2023

Transcripts application 24000.0.3 X

Transcripts application 13.1.0 X

## Installing the Transcripts application

In Relativity, confirm that you have the appropriate system admin permissions to install the application. See Installing applications .

To add the application to the Application Library:

- On the Applications & Scripts tab, click the Application Library tab.

- Click Upload Application .

- Click Select File , navigate to and select the Transcripts rap file, and then click Open .

- Click Save .

- Click Select in the Workspaces Installed section to install the application on workspaces.

-

In the column on the left, select the workspace(s) you want to install the application to.

-

Use the single arrow between the columns to move the selected workspaces over to the column on the right.

-

Click Apply .

- Click Save to install the application to the selected workspaces.

## Security permissions

You must configure certain permissions for proper functionality of the Transcripts application.

To configure the Transcripts application:

- Navigate to the Workspace Details tab.

- Click Manage Workspace Permissions .

- Click Edit Permissions for a group on the Group Management tab. Or, click Object Security and select a group from the Current Group drop-down menu.

- Enable the following security permissions:

Object Security Tab Visibility Other settings

-

Document - Add

The Document - Add permission enables users to upload both transcripts and other documents to Relativity. See Simple File Upload .

- Transcripts - Designation - View, Edit, Delete, Add

- Transcripts - Designation Reference - View, Edit, Delete, Add

- Transcripts - Fact - View, Edit, Delete, Add

- Transcripts - Interview Question - View, Edit, Delete, Add

- Transcripts - Issue - View, Edit, Delete, Add

- Transcripts - Link to document - View, Edit, Delete, Add

- Transcripts - Link to Url - View, Edit, Delete, Add

- Transcripts - Location - View, Edit, Delete, Add

- Transcripts - Note - View, Edit, Delete, Add

- Transcripts - Note - Comment - View, Edit, Delete, Add

- Transcripts - Organization - View, Edit, Delete, Add

- Transcripts - People - View, Edit, Delete, Add

- Transcripts - Video Clip - View, Edit, Delete, Add

- Transcripts (parent)

- Exhibits (child)

- Designations (child)

- Designations Type (child)

- Notes (child)

- Comments (child)

- URL (child)

- Video Clips (child)

- Mass operations

- Delete

- Transcript Report

- Admin Operations: Allow Import

## Reviewer security permissions

A system administrator can assign the following permissions to reviewers so that they can only add and apply designations when annotating transcripts.

Object Security Tab Visibility Other settings

- Transcripts - Designation - View, Edit, Delete, Add

- Transcripts - Designation Reference - View, Edit, Delete, Add

- Transcripts - Link to document - View, Edit, Delete, Add

- Transcripts - Location - View, Edit, Delete, Add

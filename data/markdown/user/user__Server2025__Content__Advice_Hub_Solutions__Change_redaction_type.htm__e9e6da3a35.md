---
title: "Change redaction type"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Change_redaction_type.htm
collection: user
fetched_at: 2026-06-22T06:09:54+00:00
sha256: 129b79b9f614eb9ab914859930e0b55951b5666b218ff4e9258626948e075006
---

Change redaction type Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Change redaction type

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

The Change Redaction Type solution changes existing black, white, cross, or text redactions in a specific set of imaged documents to a type of redaction that you specify. This solution does not change redactions on native files. To download the solution files, visit the Relativity Community .

## Before you begin

The Change Redaction Type solution changes black, white, cross, or text redactions that were applied to a specific set of documents by using a specific markup set. It changes those redactions to black, white, cross, or text redactions, depending on the options that you select when you configure the solution. Each time you prepare to run the solution, you specify:

- A saved search that returns the documents that you want to change redactions in.

- The markup set that reviewers used to apply the redactions that you want to change.

- The type of redaction that you want to change—black, white, cross, or text.

- The type of redaction that you want to change existing redactions to—black, white, cross, or text.

For text redactions, you can also specify the words or phrases that you want to use in the new text redaction.

### Components

This solution consists of a Relativity script that runs at the workspace level.

### Considerations

- This script should only be run by a system admin. If you are not a system admin, we recommend you do not run this script.

- This solution changes document files and those changes cannot be undone. We recommend that you create a back-up copy of all redactions before you run the solution.

- If you select text redaction for both the existing and new redaction type, the solution changes the text in all existing text redactions with the text that you specify when you configure the solution.

- This solution doesn't support the client domains (multi-tenancy) and Data Grid features of Relativity.

## Deploying and configuring the solution

To begin using this solution, download and add it to the Application Library as a Relativity application.

To download the solution files, visit the Relativity Community .

To add the solution to the Application Library:

- Navigate to the Application Library tab.

- Click Upload Application .

- Click Select File .

- Navigate to and select the application file included in the solution, and then click Open .

- Click Save to upload the file to the Application Library.

## Running the solution

After you prepare the workspace, you can configure and run the solution by doing the following:

- In the workspace, click the Administration tab, and then click the Scripts tab.

- Click the name of the Change Redaction Type script. The Change Reaction Type script page displays fields that let you specify which documents and redactions you want to change and how you want to change them.

- Complete the following fields:

- Saved Search - Click the name of the saved search that returns the documents that you want to change redactions in. The solution changes redactions only in documents that are returned by the saved search that you select.

- Markup Set - Click the name of the markup set that reviewers used to apply the redactions that you want to change in the documents. The solution changes redactions only if they are part of the markup set that you select.

- Source Redaction Type - Click the type of redaction that you want to change in the documents. You can change black, white, cross, or text redactions.

- Destination Redaction Type - Click the type of redaction that you want to add to the documents. You can add black, white, cross, or text redactions.

- Destination Redaction Text - Type the words or phrases that you want to use in the new text redaction. If you don't want to change existing redactions to text redactions, you can leave this field blank.

- Click Run .

## Viewing the results

When you run the solution, it changes the specified redaction type to the new redaction type in all the appropriate documents that are returned by the saved search that you specified when you configured the solution. After the solution finishes running, it displays the following message:

SUCCESS: x redactions were updated for y documents.

Where x is the number of redactions that were changed and y is the number of unique documents that were updated.

On this page

- Change redaction type

- Before you begin

- Components

- Considerations

- Deploying and configuring the solution

- Running the solution

- Viewing the results


Why was this not helpful?

Check one that applies.

I could not find the information I was looking for.

The information was incorrect.

The instructions are confusing or unclear.

The instructions did not work.

Thank you for your feedback.

Want to tell us more?


Great!

Thanks for taking the time to provide feedback.


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use

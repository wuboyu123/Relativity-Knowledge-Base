---
title: "Copy redactions across markup sets"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Copy_redactions_across_markup_sets.htm
collection: user
fetched_at: 2026-06-22T06:09:56+00:00
sha256: f5093b4a2865cd7ff6c655bd0a9d0927899a36c0df9450244a0fb5453244ff7d
---

Copy redactions across markup sets Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Copy redactions across markup sets

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

The Copy Redactions Across Markup Sets application copies redactions placed on images from one markup set to another. This application does not copy redactions to native files. To download the solution files, visit the Relativity Community .

## Before you begin

The Copy Redactions Across Markup Sets application copies redactions from one markup set to another. The solution does not remove original redactions. It only appends new ones to the selected destination markup set.

You can specify which markup set to copy redactions from, which markup set to copy the redactions to, and the saved search that contains the documents to copy redactions between markup sets.

### Supported versions

This application is supported in Relativity 8.0 – Server 2024 and RelativityOne.

Solution version Supported Relativity version

1.2 9.4.254.2 - Server 2024, RelativityOne

### Components

This application consists of a Relativity script that runs at the workspace level.

### Considerations

- This application should only be run by a system admin. If you are not a system admin, we recommend you do not run this application.

- Specifying the same markup set for both destination and source duplicates all redactions on the markup set.

## Deploying and configuring the solution

To deploy the solution, you first add it to the Application Library as a Relativity application. You can then install it from the Application Library to one or more workspaces.

This script runs from the Admin level, you must install this application into a workspace for it to appear in the Script Library (at the instance level).

To add the solution to the Application Library:

- Log in to Relativity.

- Navigate to the Application Library tab.

- Click New Library Application .

- Either click Select File, or drag and drop the file into the Application.

- Navigate to and select the application file included in the solution, and then click Open .

- Click Save to upload the file to the Application Library.

To add the solution to a workspace:

- In the Workspaces Installed section, click Select to install the application to one or more workspaces.

- Select the workspace(s) where you want to install the application, and then click the Move selected left to right icon.

- Click Apply .

The application is installed to the selected workspace(s). A list of workspace(s) where the application has been installed displays in the Workspaces Installed section.

## Running the solution

After installing the application, you can configure and run the script by doing the following:

- In the workspace, navigate to the Scripts tab.

- Click Run in the row of the Copy Redactions Across Markup Sets script.

- Complete the following fields:

- Source Markup Set - Select the name of the markup set you wish to copy redactions from.

- Destination Markup Set - Select the name of the markup set you wish to copy redactions to.

- Saved Search - Select the name of the saved search which contains the documents to copy redactions between markup sets.

- Click Run and then Accept .

## Viewing the results

When you run the Copy Redactions Across Markup Sets script, it copies the redactions from the selected source markup set to the selected destination markup set. After the script runs, the report displays a message indicating that redactions were copied to the selected destination markup set.

On this page

- Copy redactions across markup sets

- Before you begin

- Supported versions

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

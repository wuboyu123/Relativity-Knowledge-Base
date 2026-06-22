---
title: "Production gap and overlap check"
url: https://help.relativity.com/Server2025/Content/Advice_Hub_Solutions/Production_gap_and_overlap_check.htm
collection: user
fetched_at: 2026-06-22T06:09:48+00:00
sha256: e4f9d8780d37288e1d9af0a117220a5e647120d97da0bd8bbaddcc8abbc47e4c
---

Production gap and overlap check Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Production gap and overlap check

You must have valid Relativity Community credentials in order to download any Community file linked to the documentation site. You'll need to enter those credentials on the Community login screen if you're not already logged in. If you're already logged in to the Community at the time you click a link, the file is automatically downloaded in the bottom left corner of your screen. If you get an error message stating "URL No Longer Exists" after clicking a Community link, it may be due to a single sign-on error related to the SAML Assertion Validator, and you should contact your IT department.

The Production Gap and Overlap Check solution checks Bates numbers in a production set for gaps or overlaps.

This page includes the following sections:

## Before you begin

The Production Gap and Overlap Check solution checks Bates numbers in a production set for gaps or overlaps. The script looks at the ProductionDocumentFile Bates number field instead of the Document Beg Bates and End Bates. The Saved Search Gap and Overlap Check script looks at the Document.

The performance of the script depends on the number of documents in a production and the type of documents (native vs. image).

### Supported versions

This solution is supported in Relativity 9.2 and above .

Click on any of these links to download the appropriate version from the Relativity Community:

Solution version Supported Relativity version

3.2 9.3+

3.0 9.3

2.1 9.2

### Components

This solution consists of a Relativity script that runs at the workspace level.

### Special considerations

- This script should only be run by a system admin. If you are not a system admin, we recommend you do not run this script.

- The script assumes that all the documents within a production have the same prefix.

- For native-only productions, the Bates numbers are only stored in the Beg Bates and End Bates fields. If these fields are overwritten, the report doesn't provide the correct results.

- Any Bates numbers that are not in the format of letters followed by numbers aren't included when determining gaps and overlaps.

- This solution doesn't support the client domains (multi-tenancy) and Data Grid features of Relativity.

## Deploying and configuring the solution

To install the Relativity application to the library, complete the following:

- Log in to Relativity.

- Click the Applications & Scripts tab, and then click the Application Library tab.

- Click the Upload Application button

- Click Browse… for the Application File field

- Select the location of the Production Gap and Overlap Check.rap file, and then click Open .

- Click Save .

- In the Workspaces Installed section, click Install .

- In the Workspaces section, click the ellipsis (…) button

- In the pop-up window, select the desired workspace(s), and then click Ok .

- Click Save .

## Running the solution

After you prepare the workspace, you can configure and run the solution by doing the following:

- In the workspace, click the Administration tab, and then click the Scripts tab.

- Click the name of the Production Gap and Overlap Check script.

- In the Production drop-down field, click the name of the production you wish to check for gaps and overlaps.

- Click Run .

## Viewing the results

After you run the solution using the Production Gap and Overlap Check script, the results appear as a report on the script page.

The following table lists and describes the columns in the report:

Column Description

Begin Range The range start.

Finish Range The range end.

Type Gap or Overlap.

On this page

- Production gap and overlap check

- Before you begin

- Supported versions

- Components

- Special considerations

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

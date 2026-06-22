---
title: "Copy To Legacy Document Fields"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Copy_to_Legacy_Document_Fields.htm
collection: user
fetched_at: 2026-06-22T06:08:38+00:00
sha256: b6b3feacdf96636fa8e43b39d787fed9ddd834667953082cfa4a39080dd1cf59
---

Copy To Legacy Document Fields Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Copy To Legacy Document Fields

This script updates Bates fields you create on the Document table with the Bates numbering information stored in the Production Information RDO of a production you select.

This script is available as a feature in Post Production. Using Post Production has several benefits over using script. It is run automatically, improves performance, provides information about progress and gives an indication on the Production Set console that something has been run. See Production sets for more information.

## Special considerations

Consider the following risks before running this script:

- You can't undo this script after you run it.

- This script updates the Document table and may impact performance. Run this script during off-hours.

- Users must have View Script permissions to run this script.

## Inputs

Before running the script, perform the following tasks:

- Run and produce a production. For more information, see Production console .

Before running the script, ensure you create the following Document fields in the workspace:

- Begin Bates

- End Bates

- (Optional) Begin Bates Attachment

- (Optional) End Bates Attachment

- (Optional) Batch Size (Default 10000)

Running the script populates these fields on the Document table.

## Results

This script updates and stores the Bates fields you create on the Document table so you may continue using previous production workflows.

On this page

- Copy To Legacy Document Fields

- Special considerations

- Inputs

- Results


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

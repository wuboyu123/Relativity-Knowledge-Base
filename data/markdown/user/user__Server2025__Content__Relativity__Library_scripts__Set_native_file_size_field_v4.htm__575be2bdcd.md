---
title: "Set native file size field v4"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Set_native_file_size_field_v4.htm
collection: user
fetched_at: 2026-06-22T06:15:35+00:00
sha256: 7b2df504901b75f43153fc5fd5b57e3da20a11b3d83b6f4f89a81f126cc30559
---

Set native file size field v4 Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Set native file size field v4

This Relativity script stores the native file size for each document in the workspace in a decimal field.

This script only populates the size field if it was blank before running the script, and in those cases, it populates that field with a kilobyte (KB) value. If the size field was already set in bytes and not KB, the script does not change that value, and it remains in bytes.

This is a case functionality script to be run at a case level.

## Special considerations

Consider the following when running this script:

- This script cannot be undone.

- The script may run for some time without reporting any progress.

- This script updates the Document table.

- This script will populate the file size field for any files, including third party documents not processed in Relativity, as well as those that were transferred into the workspace as ‘Links only’ Natives via Integration Points.

## Inputs

Before running the script, create a decimal field to store the native file size.

## Results

Once run, this script updates the Native File Size field with the file size for any document in the workspace. Note that there could be a mix of file size values in KB and bytes.

On this page

- Set native file size field v4

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

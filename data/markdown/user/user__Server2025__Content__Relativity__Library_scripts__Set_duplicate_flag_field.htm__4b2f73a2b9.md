---
title: "Set duplicate flag field"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Set_duplicate_flag_field.htm
collection: user
fetched_at: 2026-06-22T06:15:32+00:00
sha256: 6f00fdc638640305cbb784cc6c71a0b543d875e4316323d545d167a21daaf556
---

Set duplicate flag field Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Set duplicate flag field

This Relativity script identifies and sets a Yes/No field on all case documents to indicate them as original or duplicate.

This is a case functionality script to be run at a case level.

## Special considerations

Consider the following when running this script:

- This script cannot be undone.

- The script may run for some time without reporting any progress.

- The script skips any documents which already have their duplicate flag field already set to Yes. (It updates only documents on which this field isn't set.)

## Inputs

Before running this script, you must create a Yes/No field to act as the Duplicate Indicator.

- Duplicate Indicator - the Yes/No field that determines whether documents are duplicates.

- Relational Field - the field that shows document relationship (such as MD5 Hash).

- Document Sort Field - the sort order field for duplicate documents. For example, if MD5 Hash is specified as the Relational Field and Control Number as the Document Sort Field, the document with the lowest Control Number will be flagged as original; the other documents with the same MD5 Hash field value will be flagged as duplicates.

## Results

When you run this script, all documents that are duplicates are marked Yes and all documents that are original are marked No .

On this page

- Set duplicate flag field

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

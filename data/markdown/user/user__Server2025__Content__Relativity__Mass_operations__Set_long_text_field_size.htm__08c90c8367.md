---
title: "Set long text size"
url: https://help.relativity.com/Server2025/Content/Relativity/Mass_operations/Set_long_text_field_size.htm
collection: user
fetched_at: 2026-06-22T06:15:52+00:00
sha256: 50bc1495b5b71a44fa8f73b44f879dbb7807c80c4c19c506666ee2529ef9ab74
---

Set long text size Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Set long text field size

You can use the set long text field size operation to calculate long text size and save the value in a decimal field for each selected document. The mass operation is available from the mass operations bar. You can use the mass operation with Data Grid-enabled or SQL extracted text fields. This feature is useful when creating views and saved searches of documents based on long text size. In Relativity, long text is declared as an uncompressed nvarchar(max). This means it will always hold each character as 2 bytes in terms of how this operation calculates the size of the long text field.

## Before you begin

To enable the mass operation in your Relativity instance, you must import the Long Text Size application from the application library. To do this, you must have the appropriate admin rights.

To install the Set Long Text Field Size application in your workspace:

- Navigate to the Relativity Applications tab.

- Click New Relativity Application .

- Select Select from Application Library .

- Click on Choose from Application Library .

- Select Set LongText Field Size , and click OK .

- Click Import .

After the application is installed, review the workspace permissions and remove the Set Long Text Field Size permission for the groups that should not have access to the mass operation.

### Set long text field size considerations

- There’s no hard limit on the number of documents you can update with the Set Long Text Fields Size script.

- Because this is a mass operation, run it during a maintenance window or other low-usage hours to minimize performance impact.

- Run time varies by document size and total volume. Larger documents take longer, and benchmark metrics aren’t available to predict duration for very large sets (for example, 1,000,000 documents). To plan, run a small test batch, review results, and then scale up.

## Using the mass operation

To set long text size:

- Create a decimal field for saving the extracted text size. For more information, see Fields .

- From the mass operations bar on the document list, choose whether to select Checked items or All items in the current returned set.

The set long text size mass operation permits the user to edit documents even if they have read-only permissions.

- Select Set long text field size in the mass operations drop-down menu.

The Set LongText Size form displays.

- Select a source field to calculate long text size. The drop-down menu includes all long text fields you have permissions to see.

- Select a decimal field to store the calculated long text size. The drop-down menu includes all decimal fields you have permissions to see.

- Click Run to apply your changes.

The mass operation stores the size of the text, in kilobytes, in the decimal field.

On this page

- Set long text field size

- Before you begin

- Set long text field size considerations

- Using the mass operation


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

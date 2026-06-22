---
title: "Application Field Codes"
url: https://help.relativity.com/Server2025/Content/Relativity/Imaging/Application_Field_Codes.htm
collection: user
fetched_at: 2026-06-22T06:14:06+00:00
sha256: f68fa6d7bb07da24adb2f12c9e23b63118f9da6e2a7d620a82783d8413d4f78b
---

Application Field Codes Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Application Field Codes

Application Field Codes is how Relativity refers to fields that Microsoft documents use to store document data. For example, [Date] is a field code in Microsoft that shows the date of document creation. Excel and PowerPoint refer to these fields as header and footer, Word refers to them as field codes, and Visio refers to them as fields. But for simplicity, Relativity refers to them as field codes, regardless of which Microsoft application document you’re viewing.

When imaging Microsoft application documents in Relativity, field codes embedded within a document can contain incorrect or irrelevant information. The imaged field code functions as it should, but instead of using the original Date, for example, the field code captures the date the document was imaged within Relativity instead of the date the document was actually created. By creating Application Field Codes in Relativity, however, you can determine how various field codes appear on imaged documents.

Relativity comes with 17 of the most commonly-used field codes automatically linked to the default native imaging profile with the most common rendering options supported. You can edit these linked field codes or remove them from the default native imaging profile based on your rendering preferences. You can also add additional field codes to Relativity beyond the 17 we include.

Application Field Codes are only configurable with native imaging.

## Application Field Codes in Relativity

Use the following table to view the 17 Application Field Codes that come with Relativity. An asterisk denotes the default rendering behavior.

Field Code

Supported Rendering Options

Show Field Code Show Nothing Document Default Replace with Relativity Field

Microsoft Word

Date ✓ * ✓ ✓ ✓

FileName ✓ ✓ ✓ * ✓

NumPages ✓ ✓ ✓ * ✓

Pages ✓ ✓ ✓ * ✓

Time ✓ * ✓ ✓ ✓

Microsoft Excel

Date ✓ * ✓ ✓ ✓

File ✓ * ✓ ✓ ✓

Page ✓ ✓ ✓ * ✓

Pages ✓ ✓ ✓ * ✓

Path ✓ * ✓ ✓ ✓

Time ✓ * ✓ ✓ ✓

Microsoft Powerpoint

DateTime ✓ * ✓ ✓ ✓

Footer ✓ ✓ ✓ * ✓

Slide Number ✓ ✓ ✓ * ✓

Microsoft Visio

Directory ✓ * ✓ ✓ ✓

FileName ✓ * ✓ ✓ ✓

Now ✓ ✓ ✓ * ✓

For PowerPoint, Relativity only supports field codes for headers and footers. Field codes for speaker notes and text boxes are not supported.

If you need to add field codes beyond the 17 that come pre-loaded, Relativity provides additional field codes you can select via a pop-up picker or enter manually. Those field codes are:

Field Code Supported Rendering Options

Relativity Availability

Show Field Code Show Nothing Document Default Replace with Relativity Field Popup Picker Manual Entry

Microsoft Word

Author ✓ ✓ ✓ ✓ ✓ ✓

Citation ✓ ✓ ✓

CreateDate ✓ ✓ ✓ ✓ ✓ ✓

Embed ✓ ✓

Link ✓ ✓

PrintDate ✓ ✓ ✓ ✓ ✓ ✓

SaveDate ✓ ✓ ✓ ✓ ✓ ✓

Microsoft Excel

Picture ✓ ✓ ✓ ✓ ✓ ✓

Tab ✓ ✓ ✓ ✓ ✓ ✓

Microsoft Visio

DocCreation ✓ ✓ ✓ ✓ ✓ ✓

DocLastEdit ✓ ✓ ✓ ✓ ✓ ✓

DocLastPrint ✓ ✓ ✓ ✓ ✓ ✓

PageCount ✓ ✓ ✓ ✓ ✓ ✓

PageNumber ✓ ✓ ✓ ✓ ✓ ✓

Please note that Relativity currently does not support the following Microsoft Word field codes:

- AutoNum

- AutoNumLgl Time

- AutoNumOut

- Custom

- GoToButton

- IncludePicture

- MacroButton

- PageRef

- Seq

## Application Field Code formats

If you want to add field codes beyond the 17 that come with Relativity or the field codes available in the pop-up picker, you can manually enter the field code for each Microsoft application. Code means any string of non-special characters, for example, DateTime.

Microsoft Word format

Acceptable formats are {Code}, [Code], and Code.

Microsoft Excel format

Acceptable formats are [Code], Code, &Code, &[Code].

Microsoft PowerPoint format

Acceptable formats are [Code] and Code.

Microsoft Visio format

Acceptable formats are [Code] and Code.

## Creating or editing an Application Field Code

You can create a field that's available in the pop-up picker, create a field code that isn't available already in Relativity, or edit one of the pre-loaded 17 field codes or a field code you've already created. To create a new Application Field Code:

When creating Application Field Code RDOs, when the option is Relativity Field, you cannot use the following system fields: System Modified By, System Created By, or Folder Name.

- In a workspace, navigate to the Job Admin tab and select the Application Field Code tab.

- Click New Application Field Code , or click the Edit link of an existing Application Field Code. The Application Field Code Information layout opens.

- Complete all required fields. See Fields for details.

- Click Save .

## Fields

The Application Field Code Information fields are:

- Field Code - The field code that appears on your document set. Click to see a full list of available field codes. See Application Field Codes for details.

You can add a field code to your imaging profile even if the field code isn't a part of the default or available lists. See Application Field Code formats for details.

- Application - The application used to create the documents. This field automatically populates once a field code is selected.

- Option - The way field codes render on the imaged document set.

- Select from the following options:

- Show Field Code - This option displays the field code in the imaged document.

- Show Nothing - This option hides the selected field code in the imaged document.

- Document Default - This option applies the default setting of the document to the field code in the imaged document.

- Replace with Relativity Field - This option replaces the selected field code text with a Relativity date, fixed-length, or whole number field value that you choose in the imaged document.

- Relativity Field - The Relativity field value to replace the selected field code text. This option is required when Replace with Relativity Field is selected.

## Linking an Application Field Code to a native imaging profile

View permission needs to be selected on Application Field Code for the Application Field Code layout to display in the imaging profile page.

Once you create your Application Field Code, link the field code to the appropriate native imaging profile. This is only required if you create a new Application Field Code that isn't linked to a native imaging profile by default. The Imaging Profile (Field Codes) section lists the available native imaging profiles in a workspace.

To link an Application Field Code to an existing native imaging profile:

- Click Link . The Select Items - Imaging Profile (Field Codes) popup picker opens.

- Select the imaging profile where you want to link the Application Field Code.

- Click Add .

- Click Set .

On this page

- Application Field Codes

- Application Field Codes in Relativity

- Application Field Code formats

- Creating or editing an Application Field Code

- Fields

- Linking an Application Field Code to a native imaging profile


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

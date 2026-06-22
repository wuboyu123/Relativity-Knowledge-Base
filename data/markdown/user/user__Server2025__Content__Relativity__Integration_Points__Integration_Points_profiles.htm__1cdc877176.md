---
title: "Integration Points profiles"
url: https://help.relativity.com/Server2025/Content/Relativity/Integration_Points/Integration_Points_profiles.htm
collection: user
fetched_at: 2026-06-22T06:09:25+00:00
sha256: d05df1c38b62ccbdacf1788a8f0d28c1ad844063e6f4e8c1bbc8cc180c28a271
---

Integration Points profiles Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Integration Points profiles

You have the option of creating and saving profiles, which you can use to run future import or export jobs through Integration Points.

You can make your profiles specific to each data source provider so that you can then reuse those settings and avoid having to remap fields multiple times.

You can save a profile through the Transfer Options console on an integration point that you're currently creating or editing, or you can create one through the Integration Point Profile tab.

To save a just-created integration point as a profile, click the Save as a Profile button on the Transfer Options console.

Enter a name in the Profile Name field and click Save as Profile . Note that the profile name defaults to the name you originally gave the integration point you created.

To create a profile through the Integration Point Profile tab:

- Select the Integration Point Profile tab.

- Click New Integration Point Profile .

- Complete the required fields as you would for any integration point you're creating. For more information, see Importing data through Integration Points or Exporting data through Integration Points . The fields and layouts for creating a profile are identical to those for creating any integration point that intend to run, except that after you save the profile, you don't have the option to run it. Instead, you see a detailed layout of the profile you just created.

Once you save the profile, it is visible in the Integration Point Profiles tab, and you have the option of applying it to a new integration point through the Profile field on the Setup layout.

If the Destination workspace is changed after the fields have been mapped, the fields will automatically be remapped.

The artifacts are mapped based on their names only if the ArtifactIDs are different in the new destination workspace. They are mapped so they the integration points job won't fail. This means that if the source workspace fields can't match to the new destination workspace fields, those unmatched are presented at the end of the mappings list for easy identification. Relativity also informs the user that the original source fields from the profile were mapped with corresponding fields from the destination workspace.

Once they are, a pop-up modal displays "We restored the fields mapping as destination workspace has changed."

## Copying Integration Point profiles

You can copy the configuration of a Relativity Integration Point profile from a template workspace to a new workspace. The integration type needs to be set as an Export with the destination set to Relativity. This profile configuration is considered a non-document object. For a list of non-document objects that can be copied, see Creating and editing a workspace .

The configuration of the Integration Point Profiles with Type: Import or Export and Destination: Loadfile will not be carried over.

When copied over, the profile's fields are mapped and are editable.

### Configuring an Integration Point Profile for copying

To create an Integration Point profile that can be copied to another Relativity workspace, follow the configurations below.

### Setup

- Name - enter a name of your choice.

- Type - select Export. Needs to be Export for profile to be copied.

- Source - select Relativity . Needs to be Relativity for profile to be copied.

- Destination - select Relativity . Needs to be Relativity for profile to be copied.

- Transferred Object - Document is automatically populated here and can't be modified.

- Profile - select a profile of your choice.

- Include in ECA Promote List - select yes or no.

### Connect to Source

When updating the connection to source for the copied profile, the Source field defaults to Saved Search. The Saved Search field is empty and you need to select the saved search of your choice whether it's the same saved search as the original profile or a different saved search.

The Location field defaults to Folder and the drop-down menu is empty for you to choose their destination folder.

- Source - defaults to saved search.

- Saved Search - select saved search of your choice.

- Destination Workspace - select Relativity

- Location - select a location of your choice.

- Create Saved Search - select yes or no.

During the creation of a new workspace, click the Template Workspace field. Select the workspace with the Integration Points profile. For more information on creating a workspace template, see Workspaces .

On this page

- Integration Points profiles

- Copying Integration Point profiles

- Configuring an Integration Point Profile for copying

- Setup

- Connect to Source


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

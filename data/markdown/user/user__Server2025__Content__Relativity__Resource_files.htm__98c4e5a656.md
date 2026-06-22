---
title: "Resource files"
url: https://help.relativity.com/Server2025/Content/Relativity/Resource_files.htm
collection: user
fetched_at: 2026-06-22T06:02:04+00:00
sha256: 8b96916c08589704286b3653e389a78e787faa5ad2ad051b02aa2486a29f697a
---

Resource files Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Resource files

On the Resource Files tab, you can upload files or assemblies with custom code for use in applications. You can customize functionality for a Dynamic Object or other features by uploading these files. See Editing Relativity objects .

Relativity assigns each file or assembly that you upload to a single application. To reuse a file in several applications, you must upload a copy of the file to each application. Relativity assigns the files to different application domains. Consequently, you can upload different versions of the same file without causing conflicts. Relativity stores these files in the ResourceFile table on the EDDS database.

You can upload most file types, including .dll, .txt, .xml, and others. However, you can't upload these restricted file types to Relativity:

- Executable files (.exe)

- COM file (.com)

- Program information file (.pif)

- Batch file (.bat)

- Windows screensaver file (.scr)

You can also upload files that aren't associated with a specific application. For example, you can upload an event handler for use on a Dynamic Object. Choose Default as the application when you upload these files.

## Uploading a resource file

To add a resource file, use the following steps:

- Click your name in the upper right corner of Relativity, and click Home .

- Click Applications & Scripts > Resource Files tabs.

- Click New Resource File to upload a file.

- Click Select File in the Resource File field.

- Select the .dll file.

- Click Select in the Application field .

- Select the application that you want associated with .dll file. Select Default if you don't want to associate a specific application with the file. If your application isn't listed on the Select Library Application dialog, complete step 8. Otherwise, go to step 9.

- To add your application to the library, complete these steps:

- Verify that you have system admin rights to add an application to the library.

- Select the Relativity Applications tab in the workspace where you developed the application.

- View the details page for the application.

- Click Push to Library in the console. You can now associate a resource file with your application by repeating step 7.

- Click OK .

- Click Save .

On this page

- Resource files

- Uploading a resource file


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

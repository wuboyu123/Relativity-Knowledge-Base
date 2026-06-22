---
title: "Hot fixes and patches"
url: https://help.relativity.com/Server2025/Content/Installing_and_Upgrading/Hot_fixes_and_patches.htm
collection: user
fetched_at: 2026-06-22T06:04:19+00:00
sha256: eec7d5d794195c9bc7652844521e05d2f9e3f057c09bdc2fcd1bd54928185243
---

Hot fixes and patches Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Hot fixes and patches

This topic provides contextual information and procedures for applying a hot fix or patch to your Relativity Server instance.

## Server hot fix and patch overview and versioning

Learn more about hot fixes and patches

- Relativity releases hot fixes and patches to remediate select defects and vulnerabilities found in supported Relativity Server versions. Hot fixes are unscheduled update releases to resolve higher impact defects or vulnerabilities. Patches are scheduled update releases that also include fixes for less severe/lower impact issues

- Hot fixes and patches are associated with a specific version of Relativity Server. In other words, Relativity Server 2025 hot fix #1 is built for Relativity Server 2025 and cannot be applied to Relativity Server 2024.

- Hot fixes and patches are cumulative for a base version of Relativity Server. Each hot fix and patch that Relativity Releases includes all previously-released hot fix and patch content for that base version. In other words, hot fix #2 for Relativity Server 2025 includes hot fix #1 for Relativity Server 2025. Patch #2 for Relativity Server 2025 includes patch #1, as well as any hot fixes released between patch #1 and patch #2.

- This means you do not need to separately install previous hot fixes; the latest hot fix/patch will always include all preceding hot fixes and patches for that version of Relativity server.

- The first digit represents the patch number, and the second digit represents the hot fix number relative to the patch. This new versioning attribute is referred to as the update version.

Consider the diagram below, which illustrates how the new update versioning scheme for Server 2025 would be applied during sequential hot fix and patch releases. In this diagram:

- Hot fix #2 (update.0.2) also includes hot fix #1 (update.0.1) changes

- Patch #1 (update.1.0) includes hot fix #1 and #2, as well as additional new fixes for the patch. (Since hot fix #2 includes hot fix #1, patch #1 includes hot fix #1 as well.)

- Hot fix #3 (update.1.1) includes everything in patch #1. (Therefore, hot fix #3 includes hot fixes #1 and #2, as well as the additional fixes included in patch #1.)

- Hot fix #4 (update.1.2) includes everything in hot fix #3. (And since hot fix #3 includes patch #1, everything up to an including hot fix #3 is included in hot fix #4.)

- Patch #2 (update 2.0) includes patch #1 (update 1.0), hot fixes #3 and #4 (updates 1.1 and 1.2), and additional new fixes for the patch.

## Relativity Server release cadence and patches

Relativity Server releases are scheduled and announced based on product development timelines. Hot fixes and patch packages for currently supported versions of server are provided regularly to address specific needs.

- Hot fix – an unscheduled update release to resolve higher impact defects or vulnerabilities.

- Patch – a scheduled update release that also includes fixes for less severe/lower impact issues.

### Server patch overview

A Server patch includes all previously released hot fixes and some additional defect fixes deemed necessary to address in the current Relativity Server release. All Server hot fixes and patches are cumulative, meaning content released in any hot fix or patch is also includes in all subsequent hot fixes and patches. Server hot fixes and patches are delivered using the Server Update Tool.

The DropIt tool is used as part of the Server Update Tool. For more information on using DropIt outside of the full Server Update Tool workflow, see Standalone DropIt deployment instructions (legacy workflow) .

You can download patches from the appropriate file library on the Relativity Community . For guidance on determining which patch is installed on your Server instance, see How to determine which Patch has been installed on a Server instance . You need valid Community credentials to sign in.

## Downloading and applying a hot fix or patch

The instructions for applying a hot fix or patch are included in the update package for each release. See the Relativity Server Hot fixes knowledge base article on the Community Site to download an update package.

## Confirming your Relativity version

Beginning in Server 2024, you are able to view the detailed Server patch/hot fix version number in the About display.

The hot fix or patch update version is only updated in the database and displayed if you deploy the package using the Relativity Server Update Tool CLI. If you deploy update package content independently (for example, using the legacy standalone DropIt workflow or manually/programmatically uploading RAP files), the update version will not be updated or displayed.

The first digit represents the patch, and the second digit represents the hot fix within the patch.

The version displayed does not reflect the current version for all the servers in the environment. To view the version number per server, access and run the Relativity Update Version Check script from the About display or via the following steps:

- Navigate to the Application & Scripts tab and select the Relativity Script Library tab.

- Filter for the Relativity Update Version Check script and select it.

- Click Run Script .

- Once it is done, note the hot fix and patch versions listed for each web and agent server in the environment. Specifically, note which servers have not yet received the latest patch and update those servers accordingly. All update deployment and version details are stored in the eddsdbo.UpdateLogs table.

## Standalone DropIt deployment instructions (legacy workflow)

This page documents the legacy workflow for applying a hot fix or patch using DropIt. While the DropIt tool is still used for applying hot fixes and patches. For details on the standard deployment process as of January 2024, see Applying a Server hot fix or patch .

DropIt assists in applying hotfixes across a Relativity Server environment. Use the DropIt utility to drop assemblies, such as Dynamic-link libraries (.dll) and Executable files (.exe), for an installed instance of Relativity Server.

This topic is a high-level overview of the processing of applying hotfixes. To learn more about specific hotfixes and where to apply them, visit the Relativity Community .

DropIt can only drop .dll files. Any scripts mentioned within hotfixes need to be ran manually. You need to upload .rap files manually.

Starting DropIt

You only need the DropIt.exe file when you use DropIt. There is not an installer. Simply copy the single DropIt file to the location of your choice.

Administrator privileges are required to run DropIt because some parts of DropIt copy files to C:\Program Files, which Windows regards as protected files. The requirement to have Administrative privileges is indicated by the shield which appears next to the DropIt icon.

As of version 1.4.6.1, DropIt automatically opens with Administrator privileges. DropIt fails to open if you do not have Administrative privileges.

Main screen

Upon opening DropIt, an empty CMD window displays. After a few seconds, the CMD window closes and the main screen appears.

The File menu contains an About item which shows the current version of DropIt.

This window provides access to the three actions available in DropIt:

- Save Original Dlls

- Drop New Dlls

- Restore Original Dlls

Each button opens a dialog that will be used to perform the action. After completing the action and closing the dialog, the Result and DateTime rows are updated. For example, after clicking Save Original Dlls , performing the action, and closing the dialog box, you will see something similar to the image below.

Saving original DLLs

Click Save Original Dlls to save the originally installed DLLs from Relativity or Invariant to a folder.

Clicking Save Original Dlls opens a dialog with the following:

- Manifest.xml file —to use DropIt, each package of DLL files must include an .xml file that specifies where the files will be dropped. Click the ellipses to navigate to the location of this file. You can also manually enter a value for this field by typing the location.

- DllDrop folder —the DllDrop folder is where you specific the location of the assemblies, .dll and .exe files, that are part of the DLL drop. There are two ways to populate the field:

- Select a a DllDrop.xml file to automatically populate the empty field with the name of the folder that contains the DllDrop.xml file.

- Manually enter a value for this field by typing. You can modify this field after it's initially populated through selecting a DllDrop.xml file.

- Placeholder and Replacement Text table —this table allows you to specify locations for the known placeholders which are present in the Manifest XML file. If your Manifest XML file does not contain placeholders, then this table is not available.

For most placeholders, you will see an initial default value for Replacement Text. You can change this to a custom location before clicking Go. If the value %WorkerNetworkPath% is present, you must specify a location because there is no default location. The best way to get the correct field value is to run the following query against the Invariant database:

```text
SELECT [Value1]
FROM [Invariant].[dbo].[AppSettings]
WHERE [Category] = 'WorkerNetworkPath'
```

- Folder to save original dlls in —select the radio button next to the location where you want to save the original .dll files. You can save them in a folder on your Desktop, to the C: drive, or to any custom location. If you choose Custom, enter a folder location.

- Open original dlls folder in Windows Explorer —click this link to open Windows Explorer and verify that all .dll files were copied to the original Dlls folder.

After you set all the values in the dialog, click Go to copy the original .dll and .exe files that will later be replaced by files from the DLL drop.

The .dll files are copied from locations in C:\Program Files\kCura Corporation\Relatiivty or C:\Program Files\kCura Corpration\Invariant. The .files are copied to the location you specified in the Folder to save original dlls in field.

Any DLL files that already exist at the location are not overwritten. If you want to check the contents of the original DLLs folder, click the Open original dlls folder in Windows Explorer link.

Results

After clicking the Go button, detailed results appear in the Result section.

If there is a failure, a pop-up dialog box appears with a message. In addition, there a red Failed message displays next to the Results label. After closing the dialog, the Success or Failed message will also show up on the main window.

If you want to copy the results in the Results area, highlight the text and copy it. Supported keyboard shortcuts include CTRL+A to select all text after initially clicking in the Results area. CTRL+C to copy the highlighted text. Also, once you click in the Results area, a context menu can be used to copy the text.

Click the Clear button to remove the text in the Results text area. You do not have to do this, but you might find it helpful in certain cases. For example, you may want to retry clicking the Go button again after an initial failure, but you only want to see the new results. In this case, click the Clear button before clicking the Go button again.

DLL drops without DropIt

There can be a problem if you have already done a DLL drop without using DropIt. If you have used another program, Relativity or Invariant will contain a mixture of original .dll files and dropped .dll files. You must use the Copy Original DLLs dialog accordingly otherwise it may end up saving the previously dropped .dll files instead of the original .dll files.

If this has happened, check to see if you saved the original .dll files to a folder before doing the previous DLL drop. If this DLL drop contains the same assemblies as the previous DLL drop, then you do not need to use this feature.

If you have already saved the original .dll files to a folder before doing the previous DLL Drop, but the current DLL drop contains additional .dll files that need to be saved, you have choices:

- You can restore the .dll files and then use the Copy Original DLLs feature from DropIt.

- You can manually copy a few additions .dll files to the location of the previously saved DLLs.

- You can use the Copy Original DLLs feature from DropIt to copy the .dll files that are currently on the server to a new location. Then, copy the previously saved original .dll files to the custom location. This replaces any .dll files which DropIt copied that were not the original .dll files.

Drop New DLLs

Click Drop New DLLs dialog to drop files from the DLL drop into installed versions of Relativity, Invariant, or both.

Before starting, stop all processing that may be using these files. For Invariant Queue Manager, you may need to stop the following:

- Invariant Queue Manager service in the Services window.

- Invariant Launcher and Invariant Workstation in Task Manager.

For other Servers in the Relativity environment, you may need to stop the following services, depending on what version of Relativity you are using.

- Agent Servers —kCura EDDS Agent Manager, kCura Service Host Manager

- Web Servers —kCura EDDS Web Processing Manager, kCura Service Host Manager

- Analytic Servers —Relativity Analytics Engine

Use the Drop New DLLs dialog by following the steps:

- Enter the correct information into the Manifest .xml file and DllDrop folder fields.

- Manifest xml file —to use DropIt, each package of .dll files must include an .xml file that specifies where the files will be dropped. Click the ellipses to navigate to the location of this file. You can also manually enter a value for this field by typing the location.

- DllDrop folder —the DllDrop folder is where you specific the location of the assemblies, .dll and .exe files, that are part of the DLL drop. There are two ways to populate the field:

- Select a a DllDrop.xml file to automatically populate the empty field with the name of the folder that contains the DllDrop.xml file.

- Manually enter a value for this field by typing. You can modify this field after it's initially populated through selecting a DllDrop.xml file.

- Confirm that the Placeholders and Replacement Text information is correct.

- Read the Before clicking Go section.

- Click Go .

Results

After clicking the Go button, detailed results appear in the Result section.

If there is a failure, a pop-up dialog box appears with a message. In addition, there is a red Failed message displays next to the Results label. After closing the dialog, the Success or Failed message will also show up on the main window.

If you want to copy the results in the Results area, highlight the text and copy it. Supported keyboard shortcuts include CTRL+A to select all text after initially clicking in the Results area. CTRL+C to copy the highlighted text. Also, once you click in the Results area, a context menu can be used to copy the text.

Click the Clear button to remove the text in the Results text area. You do not have to do this, but you might find it in certain cases.

For example, you may want to retry clicking the Go button again after an initial failure, but you only want to see the new results. In this case, click the Clear button before clicking the Go button again.

Restoring Original DLLs

The Drop New DLLs dialog is also used to restore originally installed assemblies that are a part of Relativity and Invariant, that were previously replaced in a DLL drop.

The fields and mechanics of this dialog are very similar to the Save Original DLLs dialog. For information, see Hot fixes and patches .

The Folder with original dlls field should be set to the same value as the Folder to save original dlls in field in the Save Original DLLs dialog.

Settings file

When you run the DropIt application for Windows, it automatically populates and uses the settings.xml file. The DropIt application automatically saves the settings.xml file as you modify the fields on the screen.

You can find the settings.xml file in %appdata%\kCura\DropIt\settings.xml.

Running DropIt from the Command Line

When running DropIt from Command Line, use the following arguments:

```text
DropIt [[-s] [-d] [-r] -m <file> [-p:<placeholder> <folder>]* [-
```

```text
replaceWorkerNetworkPath <folder>]] | [-h]
```

Basic options for copying .dll files.

Basic options for copying .dll files

-s or -save Save original .dll files.

-d or -drop Drop new .dll files.

-r or -restore Restore original .dll files.

-m or -manifestFile The <file> is the location of the manifest .xml file, which specifies where to drop each .dll file. This option is required.

Other options

Other options

-p:<placeholder> The <placeholder> is a standard placeholder, without the surrounding % characters. The supported placeholders are Relativity, WorkerNetworkPath, InvariantRPC. The <folder> is a path. The patch can also be a network path.

-replaceWorkerNetworkPath The <folder> is the value of %WorkerNetworkPath% which is a placeholder in the manifest file for the Invariant worker network opath. Get this value from the Invartiant database, in the [Invariant].[dbo].[AppSettings] table.

-h or -help Show the usage information.

Examples

```text
DropIt -s -m "C:\Temp\hot fix 2\manifest.xml" –p:WorkerNetworkPath "\\EMTTEST\InvariantNetworkShare" –p:InvariantRPC "D:\Program Files\kCura Corporation\Invariant\RPC"
```

```text
DropIt -s -m "C:\Temp\hot fix 5\manifest.xml" –p:Relativity "D:\Program Files\kCura Corporation\Relativity"
```

```text
DropIt -s -m "C:\Temp\hot fix 2\manifest.xml" -replaceWorkerNetworkPath "\\EMTTEST\InvariantNetworkShare"
```

All arguments are optional and case-insensitive. The arguments can be in any order. If Save and Drop actions are both specified, the Save will occur before the drop. If there are no arguments, the DropIt window version will open.

In the case of failure, due to invalid arguments, or if one of the save, drop, or restore actions fails, the command line version will return with a non-zero exit code.

When running DropIt from the command line, the Settings XML file is not used. Any configurable values that are needed must be supplied from the command line arguments. The defaults used are

- Instead of specifying a folder for the .dll files, the folder for the .dll files must be the folder that contains the manifest .xml file.

- Instead of specifying a folder for the original .dll files, create a new folder inside the folder that contains the manifest .xml file. The new folder is called "_Original Dlls".

If the WorkerNetworkPath is not specified as an argument, either -pWorkerNetorkPath or -replaceWorkerNetworkPath, DropIt will use the registry value for HKLM\SOFTWARE\KCURA\INVARIANT\WorkerNetworkPath.

On this page

- Hot fixes and patches

- Server hot fix and patch overview and versioning

- Relativity Server release cadence and patches

- Server patch overview

- Downloading and applying a hot fix or patch

- Confirming your Relativity version

- Standalone DropIt deployment instructions (legacy workflow)


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

---
title: "Command line import overview"
url: https://help.relativity.com/Server2025/Content/System_Guides/Command_line_import.htm
collection: user
fetched_at: 2026-06-22T06:08:25+00:00
sha256: c402fa7f3a57af70260fe356f5fcfd34dc56bb231a71a563a7439006a9fd2a10
---

Command line import overview Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Command line import

You can kick off an import using the Windows command line. This type of import provides the same features as an import from the Relativity Desktop Client.

- The executable for the RDC has been renamed to Relativity.Desktop.Client.exe . If you use an antivirus scan in your environment, you may want to update your settings to accommodate the renamed RDC executable.

- The object type for the import is set in the KWE for the load, which is created by exporting the settings using the RDC.

## Integrated help file

The command line import tool offers a help file, retrievable from the command line. To retrieve the help file, enter the following:

C:\Program Files\kCura Corporation\Relativity Desktop Client> Relativity.Desktop.Client.exe –h

The following displays:

Relativity Desktop Client Command-Line Arguments:

---------------------------------------------------------------------

-h or /h

Displays this help file.

: encoding

Displays a list of supported text encoding types on this machine.

### Set arguments

Set the Desktop Client arguments in the form as follows:

[flag]: value]

e.g. -f: "\ Documents and Settings\relativityuser\Desktop\load file.dat"

Desktop Client command line arguments are as follows:

- [-f or /f]:[file path] required

Sets the import metadata file path - either native or Opticon

- [-c or /c]:[case artifact id] required

Points the client toward the case you want to import

You have the option to use either OAuth2 client credentials for logging in through the command line import utility, or username and password credentials.

- [-clientID or /clientID]:[Relativity OAuth2 Client ID] required for OAuth2 client credential login

Sets the Relativity OAuth2 client that performs the import

- [-clientSecret or /clientSecret]:[Relativity OAuth2 Client Secret] required for OAuth2 client credential login

Validation for the OAuth2 client

- [-u or /u]:[Relativity username] required for username and password login

Sets the Relativity user account that performs the import

- [-p or /p]:[Relativity password] required for username and password login

Validation for the user account

- [-k or /k]:[saved settings kwe or kwi file path] required

Saved settings to perform the run

- [-m or /m]:[image or native or object or i or n or o] required

Sets the import type you want to run– image, native, or object

- [-e or /e]:[code page id]

Sets the encoding of the load file. This defaults to Windows’ default encoding. For a list of active encodings, use -h:encoding.

- [-x or /x]:[code page id]

Sets the encoding of any full text files. This defaults to Windows' default encoding. For a list of active encoding code page ids use -h:encoding.

- [-r or /r]:[repository path]

Sets the destination repository for loaded files. This defaults to the case default.

- [-l or /l]:[boolean value]

Determines whether files actually copy to a Relativity repository. This defaults to true.

- [-d or /d]:[folder artifact id]

Sets the destination folder for the upload. This defaults to the case root folder.

- [-s or /s]:[start line number]

Sets the starting line number of the load file for the upload. This defaults to 0.

- [-ef or /ef]:[Error line file path]

Specifies the file path to dump the error line file from the import. If no path is specified, an error line file creates in the run directory with an extension matching that of the load file. If this option is not selected, no error line file is created.

- [-er or /er]:[Error report file path]

Specifies the file path to dump the error report file from the import. If no path is specified, an error report file is created in the run directory with a CSV extension. If this option is not selected, no error report file is created.

## Import considerations

When you're running an import through the command line, consider the following:

- In the installation directory, there is a file called runit.bat. If you insert the complete path of the import in the runit.bat file, you should be able to call runit.bat in the command line from that directory.

- The folder count option is unavailable when running the command line import.

- Once an import begins, clicking Ctrl + c ends the import. Clicking on the command prompt pauses the import.

- Error files are only generated after the import is complete. Error files contain:

- Line level errors

- Append/Overlay errors

## Example command line load

This example describes the process to complete a successful command line import. Each section builds on the previous, adding information to the statement. The added token is highlighted in green . The added value for the token is highlighted in yellow .

- Open a command line and browse to Relativity Desktop Client .

- Enter Relativity.Desktop.Client.exe . The path is:

[Installation Directory] \kCura Corporation\Relativity Desktop Client> Relativity.Desktop.Client.exe

Traditionally, the exact path is, including the default installation directory:

C:\Program Files\kCura Corporation\Relativity Desktop Client> Relativity.Desktop.Client.exe

- Set the file path to the load file - either document-level dat or a page-level Opticon file.

- Token = [-f or /f]:[file path]

- Add to command line:

PATH> Relativity.Desktop.Client.exe -f: "C:\LOAD\Loadfile.dat"

- Add the token for the case artifact ID of the target case.

- Token = [-c or /c]:[case artifact id]

- Add to command line:

PATH> Relativity.Desktop.Client.exe -f:"C:\LOAD\Loadfile.dat" -c: 125015

- You can find the target case’s artifact ID by browsing to the case in Relativity and locating the AppID listed in the URL. For example:

- To use OAuth2 client credentials, complete the tasks in this step. To use a username and password login, skip to step 6.

- Set valid Relativity OAuth2 clientID for the load.

- Token = [-clientID or /clientID]:[Relativity OAuth2 Client ID]

- Add to command line:

PATH> Relativity.Desktop.Client.exe -f:"C:\LOAD\Loadfile.dat" -c:1250154 -clientID:<Relativity OAuth2 ClientID>

- Set a corresponding secret for the clientID.

- Token = [-clientSecret or /clientSecret]:[Relativity OAuth2 Client Secret]

- Add to command line:

PATH> Relativity.Desktop.Client.exe -f:"C:\LOAD\Loadfile.dat" -c:1250154 -clientSecret:<Relativity OAuth2 Client Secret>

- To use username and password login, complete the tasks in this step. If you completed step 5, you can go to step 7, because you have already entered your credentials.

- Set a valid Relativity user account for the load.

- Token = [-u or /u]:[Relativity username]

- Add to command line:

PATH> Relativity.Desktop.Client.exe -f:"C:\LOAD\Loadfile.dat" -c:1250154 -u :jsmith@example.com

- Set the password for the user account.

- Token = [-p or /p]:[Relativity password]

- Add to command line:

PATH> Relativity.Desktop.Client.exe -f:"C:\LOAD\Loadfile.dat" -c:1250154 -u:jsmith@example.com -p: <your Relativity password>

- Specify saved settings for the run to be performed (field map – kwe file).

- Token = [-k or /k]:[saved settings kwe or kwi file path]

Make sure that the kwe file doesn't contain any errors. The Append/Overlay options are retrieved from this kwe file.

- Add to command line:

PATH> Relativity.Desktop.Client.exe -f:"C:\LOAD\Loadfile.dat" -c:1250154 -u:jsmith@example.com -p: <your Relativity password> -k :"C:\LOAD\loadfile.kwe"

- Set the import type you want to run - image or native or object

- Token = [-m or /m]:[image or native or object or i or n or o]

- Add to command line:

PATH> Relativity.Desktop.Client.exe -f:"C:\LOAD\Loadfile.dat" -c:1250154 -u:jsmith@example.com -p: <your Relativity password> -k:"C:\LOAD\loadfile.kwe" -m :n

- Set the encoding of the load file.

- Token = [-e or /e]:[code page id]

For a list of active encoding, enter:

C:\Program Files\kCura Corporation\Relativity Desktop Client> Relativity.Desktop.Client.exe - h:encoding.

Each encoding value has a specified code. Enter that code following the token.

See Encoding values for details.

- Set the default encoding for full text files. The system auto-detects the encoding of each file. However if the system is unable to determine the encoding, it uses the selected encoding.

- Token = [-x or /x]:[code page id]

For a list of active encoding, enter:

C:\Program Files\kCura Corporation\Relativity Desktop Client> Relativity.Desktop.Client.exe - h:encoding.

Each encoding value has a specified code. Enter that code following the token.

See Encoding values for details.

- Set the destination repository for files being loaded. This defaults to the case default.

- Token = [-r or /r]:[repository path]

Specify whether files are actually copied to a Relativity repository. This defaults to true.

- Token = [-l or /l]:[boolean value] File Repository

- Specify the destination folder for the upload. This defaults to the case root folder.

- Token = [-d or /d]:[folder artifact id]

The folder artifact ID can only retrieved through SQL. Open eddsdbo.folder table within a given database to retrieve the folder artifact ID by matching it to the name of the folder.

- Add to command line:

PATH> Relativity.Desktop.Client.exe -f:"C:\LOAD\Loadfile.dat" -c:1250154 -u:jsmith@example.com -p: <your Relativity password> -k:"C:\LOAD\loadfile.kwe" -m:n - d: 1476826

- Specify the starting line number of the load file for the upload. This defaults to 0.

- Token = [-s or /s]:[start line number]

- Specify the file path to dump the error line file from the import. If no path is specified, an error line file is created in the run directory with an extension matching that of the load file. If this option is not selected, no error line file is created.

- Token = [-ef or /ef]:[Error line file path]

- Specify the file path to dump the error report file from the import. If no path is specified, an error report file is created in the run directory with a CSV extension. If this option is not selected, no error report file is created.

- Token = [-er or /er]:[Error report file path]

- Once the complete path is entered in the command line, press Enter for the import to begin.

## Common errors

The following are common errors encountered during a command line import.

- If the web service URL is not entered correctly (misspelled or invalid), the following error displays:

ERROR: Invalid credentials specified. Please specify an active Relativity account's username and password.

- If a different/valid version’s web service URL is specified, an error appears stating that your version of WinRelativity is out of date.

- If the same version of the Relativity Desktop Client is being used, but the web service URL is pointing to a different environment, the following error displays:

In this example, 1250154 was the specified case artifact ID that is invalid because the web service URL was pointing to a different Relativity environment.

- If there is an error/invalid entry on a line level within an import file, the following error displays:

The created error files (-ef,-er) log the error above as well.

- If you're performing an append mode import and these files already exist in the case, the following error displays:

## Encoding values

The following table displays the list of encodings used for load files and full text files.

- Load files - [-e or /e]:[code page id]

- Full text files - [-x or /x]:[code page id]

Code Page ID Entry Encoding Value

1256 Arabic (Windows)

775 Baltic (DOS)

28594 Baltic (ISO)

1257 Baltic (Windows)

852 Central European (DOS)

28592 Central European (ISO)

10029 Central European (Mac)

1250 Central European (Windows)

936 Chinese Simplified (GB2312)

52936 Chinese Simplified (HZ)

950 Chinese Traditional (Big5)

10082 Croatian (Mac)

866 Cyrillic (DOS)

28595 Cyrillic (ISO)

20866 Cyrillic (KOI8-R)

21866 Cyrillic (KOI8-U)

10007 Cyrillic (Mac)

1251 Cyrillic (Windows)

863 French Canadian (DOS)

737 Greek (DOS)

28597 Greek (ISO)

10006 Greek (Mac)

1253 Greek (Windows)

869 Greek, Modern (DOS)

1255 Hebrew (Windows)

875 IBM EBCDIC (Greek Modern)

500 IBM EBCDIC (International)

1026 IBM EBCDIC (Turkish Latin-5)

37 IBM EBCDIC (US-Canada)

861 Icelandic (DOS)

10079 Icelandic (Mac)

51932 Japanese (EUC)

50220 Japanese (JIS)

50222 Japanese (JIS-Allow 1 byte Kana - SO/SI)

50221 Japanese (JIS-Allow 1 byte Kana)

932 Japanese (Shift-JIS)

949 Korean

50225 Korean (ISO)

865 Nordic (DOS)

855 OEM Cyrillic

437 OEM United States

860 Portuguese (DOS)

10010 Romanian (Mac)

20261 T.61

874 Thai (Windows)

857 Turkish (DOS)

28599 Turkish (ISO)

10081 Turkish (Mac)

1254 Turkish (Windows)

10017 Ukrainian (Mac)

1200 Unicode

1201 Unicode (Big-Endian)

65000 Unicode (UTF-7)

65001 Unicode (UTF-8)

1258 Vietnamese (Windows)

850 Western European (DOS)

28591 Western European (ISO)

10000 Western European (Mac)

1252 Western European (Windows)

On this page

- Command line import

- Integrated help file

- Set arguments

- Import considerations

- Example command line load

- Common errors

- Encoding values


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

---
title: "Keyboard Shortcuts Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Review/Keyboard_Shortcuts_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:23:26+00:00
sha256: f9faa6f8c1ac62a029dae1484ff93452c1f19bd03b64d6c3116b292cdee46b77
---

Keyboard Shortcuts Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Keyboard Shortcuts Manager (REST)

The Keyboard Shortcuts Manager service supports retrieving all keyboard shortcuts available in a workspace, or a specific subset of them, such as those assigned to the system, choices, or fields. It also provides information about the actions that these shortcuts trigger.

As a sample use case, you might want to implement custom keyboard shortcuts in layouts, such as the review interface. You could use this service to retrieve the information required to attach the appropriate shortcut to a specific field or choice, or for global use at the system level. Users could then navigate with the custom keyboard shortcuts through fields and choices or trigger global actions with them.

You can also use the Keyboard Shortcuts Manager service through .NET. For more information, see Keyboard Shortcuts Manager (.NET) .

## Client code sample

You can use the following .NET code as a sample client for retrieving keyboard shortcuts.

Copy

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
public async Task<IList<KeyboardShortcutInformation>> ReadKeyboardShortcutsViaREST(int workspaceID)

{

    IList<KeyboardShortcutInformation> results;

    string email = "username@email.com";

    string password = "password";

    using (HttpClient client = new HttpClient())

    {

        client.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

        client.DefaultRequestHeaders.Add("Authorization", "Basic " + Convert.ToBase64String(Encoding.GetEncoding("ISO-8859-1").GetBytes($"{email}:{password}")));

        client.DefaultRequestHeaders.Add("X-Kepler-Version", "2.0");



        var url = $"http://localhost/Relativity.REST/api/relativity-review/v1/workspaces/{workspaceID}/keyboard-shortcuts";

        var response = await client.GetAsync(url);

        response.EnsureSuccessStatusCode();

        var content = await response.Content.ReadAsStringAsync();

        results = JsonConvert.DeserializeObject<IList<KeyboardShortcutInformation>>(content);

    }



    return results;

}
```

## URLs

- The URLs for REST endpoints contain path parameters that you need to set before making a call:

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number , for example v1 .

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

- Ensure that the X-CSRF-Header is set.

## Retrieve keyboard shortcut

To retrieve the keyboard shortcuts for a workspace, use these guidelines:

- Don't use the admin level context, specified by -1, as the target workspace.

- Ensure that the user has permissions to view documents in the workspace.

- Ensure that the user has permissions to view any fields associate with keyboard shortcuts. This requirement includes fields used for choices.

Send a GET request with a URL in the following format:

Copy

```text
1
<host>/Relativity.Rest/API/relativity-review/{versionNumber}/workspaces/{workspaceID}/keyboard-shortcuts?includeSystemShortcuts=<true|false>&includeChoiceShortcuts=<true|false>&includeFieldShortcuts=<true|false>
```

Set the following optional query string parameters in any order delimited by ampersands:

- includeSystemShortcuts - a Boolean value indicating whether to retrieve System shortcuts. The default value is true.

- includeChoiceShortcuts - a Boolean value indicating whether to retrieve Choice shortcuts. The default value is true.

- includeFieldShortcuts - a Boolean value indicating whether to retrieve Field shortcuts. The default value is true.

The body of the request is empty.

### Response field descriptions

The response contains the following fields:

- KeyboardShortcutID - a number used as the identifier for the keyboard shortcut.

- Type - a string indicating the type of keyboard shortcut, such as system, choice, or field. Copy

```text
1
2
3
4
5
{

   "System",

  "Choice",

   "Field"

}
```

- ArtifactID - a number representing the Artifact ID of a field or choice associated with the keyboard shortcut. This property is only returned when the type is "Choice" or "Field".

- Action - a string indicating an action taken when a keyboard shortcut is triggered. The following types of action are available:

- ToggleChoice - an action of this type is returned for Choice type keyboard shortcuts.

- SelectField - an action of this type is returned for Field type keyboard shortcuts.

- Other actions - include those for System type keyboard shortcuts.

The following strings are used in the Action field:

Copy

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
{

    "NavigateLastDocument",

    "NavigateFirstDocument",

    "NavigatePreviousDocument",

    "NavigateNextDocument",

    "DocumentProfileSave",

    "DocumentProfileCancel",

    "DocumentProfileSaveAndNext",

    "DocumentProfileEdit",

    "CSAPCopy",

    "ToggleChoice",

    "SelectField",

    "ViewerSwitchModeExtractedText",

    "ViewerSwitchModeNative",

    "ViewerSwitchModeProductions",

    "ViewerSwitchModeViewer",

    "ViewerSwitchModeImage",

    "ViewerFindNext",

    "ViewerPageDown",

    "ViewerPageUp",

    "ViewerFindPrevious",

    "ViewerToggleQualityMode",

    "CreateFullPageRedaction"

}
```

- KeysCombination - indicates whether additional keys are used as part of the shortcut. The following properties are available:

- Shift - a Boolean value indicating whether the Shift key is used in the key combination.

- Ctrl - a Boolean value indicating whether the Control key is used in the key combination.

- Alt - a Boolean value indicating whether the Alt key is used in the key combination.

- Key - a number indicating a key used in a specific keyboard shortcut combination.

The list contains number and key combinations.

Copy

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
{

    13, // Return

    32, // Space

    33, // Page Up

    34, // Page Down

    35, // End

    36, // Home

    37, // Left Arrow

    38  // Up Arrow

    39, // Right Arrow

    40, // Down Arrow

    48, // 0

    49, // 1

    50, // 2

    51, // 3

    52, // 4

    53, // 5

    54, // 6

    55, // 7

    56, // 8

    57, // 9

    65, // A

    66, // B

    67, // C

    68, // D

    69, // E

    70, // F

    71, // G

    72, // H

    73, // I

    74, // J

    75, // K

    76, // L

    77, // M

    78, // N

    79, // O

    80, // P

    81, // Q

    82, // R

    83, // S

    84, // T

    85, // U

    86, // V

    87, // W

    88, // X

    89, // Y

    90  // Z

}
```

### Sample JSON response

Copy

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
[

  {

    "KeyboardShortcutID": 44,

    "Type": "System",

    "Action": "ViewerSwitchModeExtractedText",

    "KeyCombination": {

      "Shift": false,

      "Ctrl": false,

      "Alt": true,

      "Key": 69

    }

  },

  {

    "KeyboardShortcutID": 45,

    "Type": "System",

    "Action": "NavigateLastDocument",

    "KeyCombination": {

      "Shift": false,

      "Ctrl": false,

      "Alt": true,

      "Key": 35

    }

  }

]
```

On this page

- Keyboard Shortcuts Manager (REST)

- Client code sample

- URLs

- Retrieve keyboard shortcut

- Response field descriptions

- Sample JSON response


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use

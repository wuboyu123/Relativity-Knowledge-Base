---
title: "Keyboard Shortcuts Manager (.NET)"
url: https://platform.relativity.com/Server2025/Content/BD_Review/Keyboard_Shortcuts_Manager_API.htm
collection: developer
fetched_at: 2026-06-22T06:23:24+00:00
sha256: f8076f55995fc7409280e4fd80efceaaaad1d1eaf20cb6f4285c02595e147190
---

Keyboard Shortcuts Manager (.NET)

# Keyboard Shortcuts Manager (.NET)

The Keyboard Shortcuts Manager API supports retrieving all keyboard shortcuts available in a workspace, or a specific subset of them, such as those assigned to the system, choices, or fields. It also provides information about the actions that these shortcuts trigger.

As a sample use case, you might want to implement custom keyboard shortcuts in layouts, such as the review interface. You could use this service to retrieve the information required to attach the appropriate shortcut to a specific field or choice, or for global use at the system level. Users could then navigate with the custom keyboard shortcuts through fields and choices or trigger global actions with them.

You can also use the Keyboard Shortcuts Manager API through REST. For more information, see Keyboard Shortcuts Manager (REST) .

## Fundamentals for the Keyboard Shortcuts Manager API

The Keyboard Shortcuts Manager API contains the following methods and classes.

### Methods

The Keyboard Shortcuts Manager API exposes the following method on the IKeyboardShortcutsManager interface in the Relativity.Review.Server.Versioned.<VersionNumber>.KeyboardShortcuts namespace:

- ReadAsync() method - retrieves all the keyboard shortcuts for a workspace. This method takes the Artifact ID of the workspace containing the keyboard shortcuts and an optional Boolean value indicating the type of shortcuts to return, such as those for the system, choices, or fields. It returns a list of KeyboardShortcutInformation objects. See Retrieve keyboard shortcuts

### Classes

The Keyboard Shortcuts Manager API includes the following classes available in the Relativity.Review.<VersionNumber>.KeyboardShortcuts.Models namespace:

- KeyboardShortcutInformation class - represents information about a keyboard shortcut, including the type of shortcut such as choice, field, or system, the action triggered by executing the shortcut, and other information.

View a list of properties The following table lists the properties for the KeyboardShortcutInformation class:

Property Name Type Description

KeyboardShortcutID int A unique identifier for the keyboard shortcut.

Type string The type of the keyboard shortcut: System, Choice, or Field.

ArtifactID int? The Artifact ID of the associated field or choice. This property is only returned when the type is Choice or Field .

Action string The action taken when a keyboard shortcut is triggered. The following types of actions are available:

- ToggleChoice - this action is returned for Choice type keyboard shortcuts.

- SelectField - this action is returned for Field type keyboard shortcuts.

The actions taken for System type keyboard shortcuts include:

- TBD

- TBD

KeyCombination KeyCombination The key combinations used as part of the shortcut.

- KeyCombination class - represents of a key combination used to activate a keyboard shortcut.

View a list of properties The following table lists the properties for the KeyCombination class:

Property Name Type Description

Shift bool Indicates whether the Shift key is used in the key combination.

Ctrl bool Indicates whether the Ctrl key is used in the key combination.

Alt bool Indicates whether the Alt key is used in the key combination.

Key int A number indicating a key used in a specific keyboard shortcut combination.

## Retrieve keyboard shortcuts

To retrieve a list of all keyboard shortcuts in a workspace, call the ReadAsync() method and pass the Artifact ID of a workspace to it. This method also supports filtering on choice, field, or system shortcuts by passing a set of Boolean arguments. You can set these properties to the type of shortcuts that you want to return.

Use these guidelines to retrieve keyboard shortcuts:

- Don't use the admin level context, specified by -1, as the target workspace.

- Ensure that the user has permissions to view documents in the workspace.

- Ensure that the user has permissions to view any fields associate with keyboard shortcuts. This requirement includes fields used for choices.

View code sample Copy

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
public async Task<IList<KeyboardShortcutInformation>> ReadKeyboardShortcuts(int workspaceID)

{

    IList<KeyboardShortcutInformation> keyboardShortcuts;

    var restUri = new Uri(@"http://localhost/Relativity.REST/api");

    Credentials credentials = new UsernamePasswordCredentials("username@email.com", "password");

    var settings = new ServiceFactorySettings(restUri, credentials);

    var serviceFactory = new ServiceFactory(settings);

    using (var keyboardShortcutManager = serviceFactory.CreateProxy<IKeyboardShortcutsManager>())

    {

        keyboardShortcuts = await keyboardShortcutManager.ReadAsync(workspaceID);

    }

    return keyboardShortcuts;

}
```

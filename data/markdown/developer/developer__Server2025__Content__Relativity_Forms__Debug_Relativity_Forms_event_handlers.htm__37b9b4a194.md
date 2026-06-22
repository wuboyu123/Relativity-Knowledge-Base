---
title: "Debug Relativity Forms Event Handlers"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Debug_Relativity_Forms_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:31:52+00:00
sha256: a7a4dd2734da0f5ae5f004d393305978d8d41d92ec5878c97648323b087f26cd
---

Debug Relativity Forms Event Handlers

# Debug Relativity Forms Event Handlers

When an error occurs in a Relativity Forms Event Handlers, Relativity will redirect to the default error page. To make it easier for Relativity Developers to debug their forms event handlers there is a debug object that can be set in the windows session storage to prevent the page to redirect to the error page.

## RelativityFormsDebugObject

Holds properties that makes it easier for developers to debug errors that occur in form event handlers.

Property

Type

Description

haltRedirectionOnApplicationError

Boolean

Defaults to false, but when set to true, Liquid Forms page will not redirect to native Relativity error screen.

##### How to prevent redirection for debugging

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
// get relativity debug object

var DEBUG_NS = "RelativityFormsDebugObject";

var DEBUG_OBJECT_STR = window.sessionStorage.getItem(DEBUG_NS);

var DEBUG_OBJECT_OBJ = !DEBUG_OBJECT_STR ? {} : JSON.parse(DEBUG_OBJECT_STR);

// manipulate the halt redirection property

DEBUG_OBJECT_OBJ["haltRedirectionOnApplicationError"] = true;

// set the session storage object to have manipulated properties

window.sessionStorage.setItem(DEBUG_NS, JSON.stringify(DEBUG_OBJECT_OBJ));
```

## Adding Breakpoints To Event Handler Code

The event handler files are not requested by the browser as script files and so by default will not appear in the browser's developer tools debugger. Some browsers support debugging dynamically generated script through adding a special comment to the script.

Copy

```text
1
//# sourceURL=MyEventHandlerFile.js
```

For example, adding the above comment at the start or end of the script file will in some browsers make it appear as the source file 'MyEventHandlerFile.js' in the debugger. This allows breakpoints to be set in the script.

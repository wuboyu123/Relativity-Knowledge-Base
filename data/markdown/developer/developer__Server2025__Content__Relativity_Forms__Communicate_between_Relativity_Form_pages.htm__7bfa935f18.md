---
title: "Communicate between Relativity Form pages"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Communicate_between_Relativity_Form_pages.htm
collection: developer
fetched_at: 2026-06-22T06:32:08+00:00
sha256: 1f2c4e72156f3a199a8dea5fa87f997e3128b707cfbdef5f71b353acdac26f21
---

Communicate between Relativity Form pages Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Communicate between Relativity Form pages

When using the relativityFormsPopup methods, a common use case involves the Relativity Forms page opening a pop-up window that expects to know when certain events occur within the pop-up window, particularly when items are added.

For example, when clicking the Add link on a single object field and creating an object, you might expect that the newly created object appears as the value in the parent form, and the pop-up window is closed.

To support this behavior, the relativityFormsPopup can add Event Handlers to the pop-up window. All of the Event Handlers available to Relativity Forms API pipelines and their supported event handlers are available for addition by the calls to relativityFromsPopup's functions.

See these related items:

- popupControlApi object

- Popup eventHandlerFactory function

## Guidelines for adding event handlers to a pop-up window

Although writing these event handlers for pop-up windows is similar to the process used for Relativity forms, the following differences exist:

- In the general case for an event handler, the event handler factory is an immediately invoked function expression (IIFE) of a separate file. The event handlers applied to a pop-up window are written as a factory function. This function is supplied as an optional eventHandlerFactory property in the settings object passed to any of the functions on relativityFormsPopup API, such as the openAdd(), openEdit() and, openView() functions.

- While the IIFE expects the eventNames and convenienceApi arguments, the event handler factory function expects the following three parameters: popupControlApi, eventNames, and convenienceApi. In the case of eventNames and convenienceApi, these variables will be access to the items within the pop-up's Relativity Forms application, not the opener form. The popupControlApi is provided to your event handler factory in order to give the event handlers the ability to close their executing application pop-up window. For more information, see popupControlApi object .

- If the popup is launched from the parent form by an event handler, and the event handler factory function is written within the parent's event handlers, the event handlers put on the pop-up window can access the convenienceApi in either window. This makes it possible to control both forms from within the event handler run on the popup. If you want this behavior, the event handler factory function's parameters have names that differ from the eventNames and convenienceApi variables than the parent form's IIFE for its convenienceApi. For code samples, see Write code to add event handlers to a pop-up window .

## Write code to add event handlers to a pop-up window

The most common use case for a call against the relativityFormsPopup API is from an event handler. This scenario makes it possible to give the event handlers for the pop-up window access to convenienceAPI objects for both the pop-up window and the opener simultaneously.

The following code samples illustrate these scenarios:

- Example One - The event handlers in the pop-up window only has access to the convenienceApi pop-up window.

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
(function(eventNames, convenienceApi) {



       var eventHandlers = {};



       eventHandlers[eventNames.SOME_EVENT_NAME] = function() {





            function eventHandlerFactory(popupControlApi, eventNames, convenienceApi) {

                 // ... etc -- this will ONLY have access to the convenienceApi in the popup, and NOT the parent

            }





            var popupControlApi = convenienceApi.relativityFormsPopup.openAdd({

                 workspaceId:  this .workspaceId,

                 artifactTypeId:  this .artifactTypeId,

                 parentArtifactId:  this .parentArtifactId,

                 eventHandlerFactory: eventHandlerFactory

            });

       }



       return eventHandlers;

 }(eventNames, convenienceApi));
```

- Example Two - The event handlers added to the pop-up window may access the convenienceApi of the pop-up window or of the opener.

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
(function(openerEventNames, openerConvenienceApi) {



       var eventHandlers = {};



       eventHandlers[openerEventNames.SOME_EVENT_NAME] = function() {





            function eventHandlerFactory(popupControlApi, popupEventNames, popupConvenienceApi) {

                 // ... etc





                 // event handlers produced by this function will have access to anything

                 // accessible to the opener's "SOME_EVENT_NAME" including the opener's

                 // convenienceApi, via "openerConvenienceApi"





                 // the event handlers produced by this function have access to the popup's

                 // convenienceApi via "popupConvenienceApi"

            }





            var popupControlApi = convenienceApi.relativityFormsPopup.openAdd({

                 workspaceId:  this .workspaceId,

                 artifactTypeId:  this .artifactTypeId,

                 parentArtifactId:  this .parentArtifactId,

                 eventHandlerFactory: eventHandlerFactory

            });

       }



       return eventHandlers;

 }(eventNames, convenienceApi));
```

In both of the previous examples, the event handler of the opener for SOME_EVENT_NAME has access to the opener's convenienceApi. After running the openAdd function, it also has access to the popupControlApi, which is returned by the relativityFormsPopup methods. Because the eventHandlerFactory is defined within SOME_EVENT_NAME , it can be written so that the code within has access to the opener's code.

In Example One, the factory has parameter names that overshadow the opener's variable names for the eventNames and convenienceApi. It produces event handlers that have access to the convenienceApi of the pop-up window.

Example Two illustrates a simple console event handler with buttons to open a relativityFormsPopup, which can be closed by another button in the console. It also closes when postSave event handler for the pop-up window is fired. The eventHandlerFactory adds the postSave event handler.

In the following complete code sample, the pop-up window closes from the event handler of the opener and from the event handler of the pop-up window.

### Example

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
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
(function(openerEventNames, openerConvenienceApi) {





       var eventHandlers = {};



       eventHandlers[openerEventNames.CREATE_CONSOLE] = function() {

                 // "this" context here is viewModel information about the opener Relativity Forms app





                 var consoleApi = openerConvenienceApi.console;





                 var workspaceId =  this .workspaceId;

                 var parentArtifactId =  this .artifactId;

                 var artifactTypeId =  // type id of RDOs which are child to this instance of the opener's type





                 var obj = { popupControlApi: ( void 0) };





                 var openButton = consoleApi.generate.button({

                      innerText:  "Execute openAdd"

                 });

                 var closeButton = consoleApi.generate.button({

                      innerText:  "Close popup"

                 });













                 function eventHandlerFactory(popupControlApi, popupEventNames, popupConvenienceApi) {



                      var popupEventHandlers = {};

                      popupEventHandlers[popupEventNames.POST_SAVE] = function(relativityObjectRef) {

                                // "this" context here is viewModel information about the POPUP Relativity Forms app

                                // so the exit dialog deactivation below turns off the volatile data warning which

                                // would otherwise appear in the POPUP when a postSave event handler tries to close

                                // the popup





                                // here, openerConvenienceApi would be used to update the opener's form

                                // as appropriate, given the "ArtifactID" from the relativityObjectRef passed

                                // into this event handler, and a prior knowledge of the field name being

                                // updated in the opener layout. (omitted to keep this sample clean)



                                if (popupControlApi.isPopupSafeAndLive()) {

                                     // Deactivating Popup exitDialog...

                                     this .exitDialog.deactivate();



                                     // Closing Popup...

                                     popupControlApi.closePopup();

                                }





                                return relativityObjectRef;

                           }  // end of the POPUP's postSave event handler



                      return popupEventHandlers;

                 }  // end of eventHandlerFactory













                 function openButtonClickHandler() {

                      closeButtonClickHandler();  // keep it clean!





                      popupControlApi = openerConvenienceApi.relativityFormsPopup.openAdd({

                           workspaceId: workspaceId,

                           artifactTypeId: artifactTypeId,

                           parentArtifactId: parentArtifactId,

                           eventHandlerFactory: eventHandlerFactory

                      });





                      obj.popupControlApi = popupControlApi;

                 }  // end of the open button click handler





                 function closeButtonClickHandler() {

                      if (!!obj.popupControlApi) {





                           // NOTE: because the code context/scope here is the opener Relativity Forms app / window

                           //       there is no access to the popup Relativity Forms' view model information.

                           //       so if the popup is in a changed (aka "dirty") state, the close attempt below

                           //       will result in a volatile data warning in the POPUP, prompting the user to

                           //       allow the navigation away (popup window close)





                           obj.popupControlApi.closePopup();

                           obj.popupControlApi = ( void 0);

                      }

                 }  // end of the close button click handler









                 openButton.onclick = openButtonClickHandler;

                 closeButton.onclick = closeButtonClickHandler;











                 var section = consoleApi.generate.section({}, [

                      openButton,

                      closeButton

                 ]);





                 consoleApi.containersPromise.then(function(containers) {

                      containers.rootElement.appendChild(section);

                 });

       }  // end of opener's CREATE_CONSOLE event handler
```

On this page

- Communicate between Relativity Form pages

- Guidelines for adding event handlers to a pop-up window

- Write code to add event handlers to a pop-up window

- Example


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

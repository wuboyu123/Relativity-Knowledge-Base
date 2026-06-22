---
title: "Pre Cascade Delete event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Pre_Cascade_Delete_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:28:57+00:00
sha256: a981639f3df94fdd91940e0b8fe06bab9a449b201ef5e62adf1a4371b7f5f333
---

Pre Cascade Delete event handlers Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Pre Cascade Delete event handlers

You call a Pre Cascade Delete event handler when a user attempts to force the deletion of an object with dependent objects. The user must have Delete Object Dependencies permissions to perform this action.

You can use this type of event handler to verify that no restrictions exist on an object selected for deletion. For example, the Processing Set Pre Cascade Delete event handler prevents the deletion of a processing set while it is undergoing processing.

In a forced delete operation, the Pre Cascade Delete event runs before Relativity begins deleting child objects or unlinking associative objects. After completing these operations, Relativity deletes the parent object. The Pre Cascade Delete event handler ensures that the system initiates a forced delete operation only when it can successfully remove the objects.

To view the items for deletion, use the TempTableNameWithParentArtifactsToDelete string property of the PreCascadeDeleteEventHandler base class. It holds the name of the scratch table that contains the ArtifactIDs marked for deletion.

We recommend using a Pre Delete event handler in conjunction with Pre Cascade Delete event handler. The Pre Cascade Delete event handler won't run when no associated or child objects exist. For more information, see Pre Delete event handlers .

## Guidelines for Pre Cascade Delete event handlers

- Create a new class in Visual Studio .

You can also use a template to create this event handler type. For more information, see Visual Studio templates .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages.

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from the PreCascadeDeleteEventHandler class – extend the PreCascadeDeleteEventHandler base class.

- Override the RequiredFields property – you must override this property even though a Pre Cascade Delete event handler doesn't use it.

- The ActiveArtifact.Fields collection includes the fields returned by the RequiredFields property, and those on the current layout. It also includes the values of these fields.

- Any Field in ActiveArtifact.Fields that is referenced in this event handler must be placed in the RequiredFields property.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

## Code sample for a Pre Cascade Delete event handler

Review the following code sample for a Pre Cascade Delete event handler.

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
using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using kCura.EventHandler;



namespace CustomEventHandler

{

     [kCura.EventHandler.CustomAttributes.Description("A description of the event handler.")]

     public class TaskPreCascadeDeleteEventHandeler :  PreCascadeDeleteEventHandler

     {

          public override Response Execute() {

               Response resp = new Response() {

                    Success = true,

                    Message = ""

               };



               try {

                    // Execute code for the specific event here.

                    // To prevent the cascade delete operation, the event handler must return an exception and set success = false.

                    // For example, resp.Success = false; resp.Exception = new SystemException(“Some exception message”);

               }

               catch (Exception e) {

                    resp.Success = false;

               resp.Exception = new SystemException("ProcessPreDeleteFailure failure: "

                    + e.Message);

               }

               return resp;

          }

          public override FieldCollection RequiredFields

          {

               // Add any required fields.

               // If none are required, you can initialize a new collection instead.

               get { return new FieldCollection(); }

          }

          public override void Commit()

          {

               // Commit is unused (never gets called) in a Pre Cascade Delete event.



          }

          public override void Rollback()

          {

               // Code executes when an error occurs in the process.



               // If you're retrieving information that requires a rollback in Execute() method, then handle this operation here. Otherwise, leave this method blank.

          }

     }

}
```

On this page

- Pre Cascade Delete event handlers

- Guidelines for Pre Cascade Delete event handlers

- Code sample for a Pre Cascade Delete event handler


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

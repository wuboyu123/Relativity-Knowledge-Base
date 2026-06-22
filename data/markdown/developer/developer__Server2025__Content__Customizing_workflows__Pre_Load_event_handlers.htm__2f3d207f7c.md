---
title: "Pre Load event handlers"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Pre_Load_event_handlers.htm
collection: developer
fetched_at: 2026-06-22T06:29:01+00:00
sha256: d4115d149f8cf6a2e816466f3638ad358658a99f8f76d149440f5ae2cf220f0b
---

Pre Load event handlers

# Pre Load event handlers

For object types using Relativity Forms, Pre Load event handlers will implement only for view and edit layouts, and only if replaceRead is either not implemented, or is implemented using Object Manager API. Pre-population of field values for new object instances in Relativity Forms is accomplished by implementing replaceGetNewObjectInstance. Additionally, Relativity Forms only supports script execution via Page Interaction event handlers, so script contained in a Pre Load event handler's Response.Message property must be moved into a Relativity Forms Page Interaction event handler in order to be executed.

Pre Load event handlers execute before the new, edit, or view page layouts load. Pre Load event handlers can be used populate default values. You can use Pre Load event handlers for all fields on Dynamic Objects and documents. The event handlers have the following behavior:

- Support both normal and read-only field modes.

- Read-only fields that are updated by a Pre Load event handler aren't saved to the database on Edit pages.

- Reflected fields are properly passed into Pre Load event handlers. However, changes made to reflected fields won't persist on the page.

See these related pages:

- Redirect a user to a layout in a Pre Load event handler

## Guidelines for Pre Load event handlers

Use these guidelines when developing Pre Load event handlers:

- Create a new class in Visual Studio .

You can also use a template to create this event handler type. For more information, see Visual Studio templates .

- Add NuGet packages - ensure your Visual Studio project has installed the relevant NuGet packages, including at a minimum the Relativity.EventHandler and Relativity.Api packages.

- Add a GUID for the event handler - set the System.Runtime.InteropServices.Guid to the GUID identifying your event handler. Use the GUID generator in Visual Studio.

- Set the CustomAttributes.Description attribute - provide a description that you want to appear in the Relativity UI for the event handler.

- Inherit from the PreLoadEventHandler class – extend the PreLoadEventHandler base class.

- Override the RequiredFields property – use to specify additional fields that the event handler can access. The layout doesn't need to include these fields. All Pre Load event handlers must override this property.

- The ActiveArtifact.Fields collection includes the fields returned by the RequiredFields property, and those on the current layout. It also includes the values of these fields.

- Any Field in ActiveArtifact.Fields that is referenced in this event handler must be placed in the RequiredFields property.

- Upload your event handler assembly to Relativity - use the Resource Files tab to upload your compiled .dll file to Relativity. See Add event handlers to applications .

- Optionally use event handlers to construct HTTP responses - event handlers can't access the request header, cookies, or session information using the HTTPContext object, although they can assisted in constructing an HTTP response.

## Code sample for a Pre Load event handler

Review the following code sample for a Pre Load event handler.

The following code sample uses the IsNew property to test whether an artifact is new before populating default Fields. You can only use this property to check for new RDOs. You can't use it to check for Document objects.

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
using System;

namespace ExampleEventHandlers

{

    /// <summary>

    /// This example presumes the existence of an object type with

    /// a fixed-length text field that serves as a unique identifier

    /// for each instance of that object type.  This event handler populates

    /// the identifier field each time a new instance (RDO) is created.

    /// </summary>

    [kCura.EventHandler.CustomAttributes.Description("Example pre-load event handler")]

    [System.Runtime.InteropServices.Guid("CB6ED881-F432-4F9A-8187-B87B1FA89D50")]

    class ExamplePreLoadEventHandler : kCura.EventHandler.PreLoadEventHandler

    {

        public static readonly Guid IDENTIFIER_FIELD_GUID = new Guid("24402D3C-4EAF-4C33-B244-A145EEB7C6C1");

        public override kCura.EventHandler.Response Execute()

        {

            // Construct a response object with default values.

            kCura.EventHandler.Response retVal = new kCura.EventHandler.Response();

            retVal.Success = true;

            retVal.Message = String.Empty;

            try

            {

                // Check that this is a new artifact.

                if (this.ActiveArtifact.IsNew)

                {

                    // Ensure the identifier field is uniquely populated.

                    this.ActiveArtifact.Fields[IDENTIFIER_FIELD_GUID.ToString()].Value.Value = Guid.NewGuid().ToString();

                }

            }

            catch (System.Exception ex)

            {

                retVal.Success = false;

                retVal.Message = ex.ToString();

            }

            return retVal;

        }

        /// <summary>

        /// By overriding the RequireFields method you can specify fields needed in the Execute method.

        /// Fields that are on the object type but not specified here may not be populated on the

        /// ActiveArtifact.Fields property when the Execute method (above) is invoked.

        /// </summary>

        public override kCura.EventHandler.FieldCollection RequiredFields

        {

            get

            {

                kCura.EventHandler.FieldCollection retVal = new kCura.EventHandler.FieldCollection();

                retVal.Add(new kCura.EventHandler.Field(IDENTIFIER_FIELD_GUID));

                return retVal;

            }

        }

    }

}
```

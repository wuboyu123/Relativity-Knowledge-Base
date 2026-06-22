---
title: "Redirect a user to a layout in a Pre Load event handler"
url: https://platform.relativity.com/Server2025/Content/Customizing_workflows/Redirecting_a_user_to_layout_in_a_Pre_Load_event_handler.htm
collection: developer
fetched_at: 2026-06-22T06:31:31+00:00
sha256: 135e65962a14abb9d97bed6b22c441e4e84f036764448e3489dfc58a0009c238
---

Redirect a user to a layout in a Pre Load event handler

# Redirect a user to a layout in a Pre Load event handler

You can use a Pre Load event handler to control workflows for your users. You can use them to redirect users to layouts for their specific business needs. This page includes a code sample that illustrates how to create an instance of the RedirectToLayout class in the Execute() method of an event handler to perform this action.

For example, you can use a Pre Load event handler to redirect users to a read-only layout, when they view produced documents that shouldn’t be edited. You can also use these event handlers to display layouts that contain only fields relevant to a specific document type. The event handler could redirect the users to one layout for email messages and another designed for PDFs.

The RedirectToLayout class offers an alternative to using object rules, which don’t support querying the database and aren't optimal for use with complex conditions. You can use this redirect functionality with a query that determines if a document is already produced, or with a series of conditions used to determine the layout that appears for a specific document type.

The following information only describes how to change the layout of the existing object.

## Sample code

The following code sample illustrates how to build a Pre Load event handler that redirects the user to a specific layout:

- Ensure that you follow the general guidelines for developing a Pre Load event handler, including overriding its Execute() method. See Pre Load event handlers .

- Create a new instance of the RedirectToLayout class using the layout name or Artifact ID, and the constant View in the Helper.PageMode enumeration. The PageMode enum indicates how the page layout appears to the user. For example, you can display the layout to the user in View mode when the document is read-only, or in Edit mode when the user has the option to update the document.

- Add your new instance of the RedirectToLayout class to the list of actions that need to complete after the event handler runs.

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
using System;

using System.Collections.Generic;

namespace SampleEventHandlers

{

    [kCura.EventHandler.CustomAttributes.Description("Pre-load event handler to redirect to another layout when a choice field is set.")]

    [System.Runtime.InteropServices.Guid("CB6ED881-F432-4F9A-8187-B87B1FA89D50")]

    class PreLoadEventHandler : kCura.EventHandler.PreLoadEventHandler

    {

        private Guid _fieldGuid = new Guid("22541210-287E-430B-B7D0-D92CDC711ADA");

        public override kCura.EventHandler.Response Execute()

        {

            var retVal = new kCura.EventHandler.Response { Success = true, Message = String.Empty };

            try

            {

                const int layoutArtifactId = 1041936;

                var fieldArtifactId = GetArtifactIdByGuid(_fieldGuid);

                if (ActiveArtifact.Fields[fieldArtifactId] != null)

                {

                    var fieldValue = (kCura.EventHandler.ChoiceFieldValue)ActiveArtifact.Fields[fieldArtifactId].Value;

                    if (fieldValue.Choices.Count > 0)

                    {

                        var redirect = new kCura.EventHandler.PostExecuteAction.RedirectToLayout(layoutArtifactId, kCura.EventHandler.Helper.PageMode.View);

                        retVal.PostExecuteActions = new List<kCura.EventHandler.PostExecuteAction.Base> { redirect };

                        return retVal;

                    }

                }

            }

            catch (Exception ex)

            {

                retVal.Success = false;

                retVal.Message = ex.ToString();

            }

            return retVal;

        }

        public override kCura.EventHandler.FieldCollection RequiredFields

        {

            get

            {

                var retVal = new kCura.EventHandler.FieldCollection();

                retVal.Add(new kCura.EventHandler.Field(_fieldGuid));

                return retVal;

            }

        }

    }

}
```

---
title: "Relativity Objects"
url: https://platform.relativity.com/Server2025/Content/Managing_Relativity_dynamic_objects/RDO/Relativity_objects.htm
collection: developer
fetched_at: 2026-06-22T06:29:22+00:00
sha256: d5a2e5ea552f4090e1ef668c3fafdba0c3ddb7dfd0aa3c75ff8388c653023fb3
---

Relativity Objects Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Relativity Objects

Relativity contains two kinds of objects: System objects and Relativity Dynamic Objects (RDOs). Both kinds, collectively called objects, are the building blocks of Relativity applications. Objects connect together, whether implicitly resulting from a workflow, or explicitly by you defining the connections. Through these connections or links, you extend functionality by storing data and making efficient use of its organization. You can attach many kinds of objects to additional features or functionality, such as object rules and event handlers. By attaching objects to additional features you can introduce custom features specific to your needs.

As an example of using objects to extend data reach, from within a workspace, you can create your own RDO for storing custodian information, including not only custodian names but also their emails, sent and received dates, and recipients. This information can then link to other documents or for greater granularity in sorting, searching, or listing those documents.

See these related pages:

- Creating, editing, and deleting Relativity Objects

- Deleting object dependencies

- Creating a question object

- Building Media Tracker with Relativity Dynamic Objects

- Creating a tab to bookmark an object

## System objects

System objects are objects that come with Relativity applications by default. They are predefined objects that either load during installation or Relativity automatically creates during a process. These are created for items such as workspaces, documents, fields, and OCR sets. However, Relativity sets their capabilities and you cannot change the design of them. For example, a system object may limit the number of fields that attach to it, or prohibit adding event handlers and object rules.

## Relativity Dynamic Objects (RDOs)

RDOs are objects you define. You can set their capabilities, manage data links to other objects, and incorporate additional features including attaching event handlers and object rules. You can create RDOs from home as well as from a workspace. See Editing Relativity Objects .

Read a scenario for Relativity Dynamic Objects

Using Relativity Dynamic Objects

Imagine you're a system admin and your firm's latest case involves email exchanges between many people with various roles at many different companies. The lead attorney approaches you with ideas for organizing all the custodians, their companies, and their various roles within those companies. You decide to use RDOs to store information about a custodian by creating a custodian object. This object stores information about the custodian - their name, company, role, start date, and so on.

You then connect the custodian object to any related objects such as the document and company objects in the following example.

Using objects in your workspace helps keep items organized in your doc set.

## Programmatically using Relativity objects and RDOs

You can also create and use objects programmatically with the Services API. For information about programmatically working with objects, see Object Type Manager (.NET) Object Type Manager (.NET) Object Type Manager (.NET) .

On this page

- Relativity Objects

- System objects

- Relativity Dynamic Objects (RDOs)

- Programmatically using Relativity objects and RDOs


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

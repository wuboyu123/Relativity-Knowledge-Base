---
title: "Deleting object dependencies"
url: https://help.relativity.com/Server2025/Content/Managing_Relativity_dynamic_objects/RDO/Deleting_object_dependencies.htm
collection: user
fetched_at: 2026-06-22T06:08:40+00:00
sha256: 6a803803a5bea35a09e23cadd733e84e025c2cfd1bfdcb499d7dd86cdb2115a7
---

Deleting object dependencies Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Deleting object dependencies

Deleting object dependencies removes that object's interactions, or dependencies, from other objects. Because the purpose of objects is to interact with other objects, there may be a certain amount of dependencies. Most are created at the time the object is initially instantiated, although you can add some later, either implicitly as a result of a workflow, or manually adding one, such as an event handler. However, deleting some dependencies may have unexpected effects on other objects. To mitigate those effects, Relativity may display a dependencies report, and asks you to confirm before deleting.

You also need to have the correct level of permissions. See your system admin for additional details. With the Delete Object Dependencies permission, you can force delete the current object, which includes deleting its children and unlinking associative objects.

## Force deleting object dependencies

The option to delete object dependencies appears only when you have the corresponding delete object dependencies security permission. See Security and permissions .

Before you force delete an object, you should:

- View a report listing the affected objects by clicking Dependencies . For more information, see Displaying and interpreting the dependencies report .

- Think about the fields of the selected object before forcing a delete. For more information, see Considering the fields of force deleted objects .

To force delete one or more documents or RDOs:

- Navigate to the parent or child tab of the object you want to delete.

- Click the name of the single object that you want to delete, and then click Delete on the object details page. If you want to mass delete objects, select the items you want to delete, and then select Delete from the mass operations menu. See Mass delete .

- Click Delete to remove the object and its children and to unlink associative objects.

If the Delete button is disabled, then you don't have the security permission Delete Object Dependencies . See Security and permissions .

For information about programmatically deleting dependent objects, see Object Manager (.NET) .

## Displaying and interpreting the dependencies report

The dependencies report helps you understand how deleting an object affects its child and associative objects. You can run this report before deleting an object or group of objects to determine how this operation changes your workspace. The dependencies report is available for workspace-level objects in Relativity, including documents. You can display this report when you delete a single object or perform a mass delete operation.

To display the dependencies report, click View Dependencies in the Delete Object Type pop-up. If the object(s) you're trying to delete doesn't have any children or associative objects, the View Dependencies button is disabled.

The dependencies report displays a list of the object's child and associative objects as well as a count of each object type.

Use Relativity's filter, sort, and page features to manage your report results. You can also mass export the report results to an Excel file. See Mass export to file .

A dependency report contains the following fields:

- Object Type - identifies child and associative objects that have a dependency on the selected object.

- Action - displays Delete for child objects and Unlink for most associative objects. When you force delete the selected object, Relativity automatically performs these actions on child and associative objects.

- Count - indicates the number of object instances for each object type dependency on the selected object.

- Connection - indicates the type of dependency that exists between the selected object and the object type listed in the report.

## Considering the fields of force deleted objects

The dependencies report provides information about the relationship between the selected object and other child or associative objects. However, it doesn't list objects that reference the fields on the selected object because they're not identified as children or linked by association.

When you force delete an object, Relativity may modify the content of the object’s fields or delete them. Because other objects may reference these fields, make sure that you have a clear understanding of how they're used in Relativity.

The following examples illustrate how the force delete of an object affects references to its fields.

### Analytics categorization set example

When you create a categorization set, Relativity generates a Category Set Result field, which users can add to searches, views, and pivot profiles. If you force delete the categorization set, the Category Set Result field becomes blank. As a result, any saved searches referencing this field are blank, and any views using this field as a condition no longer list it.

### Search terms reports example

Relativity generates a Search Terms Results field when you create a search terms report. You can use terms from the search terms report to create a persistent highlight set. If you force delete the search terms report, Relativity also deletes the Search Terms Results field, and the viewer no longer displays persistent highlights based on the search terms report. In this case, the persistent highlight set still references the Search Terms Results field, but it doesn't contain any results.

On this page

- Deleting object dependencies

- Force deleting object dependencies

- Displaying and interpreting the dependencies report

- Considering the fields of force deleted objects

- Analytics categorization set example

- Search terms reports example


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

---
title: "Lesson 2 - Build an application without any code"
url: https://platform.relativity.com/Server2025/Content/Get_started/Lesson_2_-_Build_an_application_without_any_code.htm
collection: developer
fetched_at: 2026-06-22T06:24:53+00:00
sha256: 226dd4547c8bb5923146874eaaf947999f2c25260d5b9653e43593ab568bee8f
---

Lesson 2 - Build an application without any code

# Lesson 2 - Build an application without any code

Relativity applications (RAPs) are custom developed applications that utilize Relativity’s APIs to perform certain functions or solve specific problems.

In this lesson, you will learn how to complete these tasks:

- Navigate through the Relativity UI and use its features.

- Create a workspace.

- Build a Relativity application without writing any code.

- Create and update object types, fields, layouts, views, tabs, and dashboards for use in an application.

- Link object types and other features to an application.

- Create sample data for your Relativity application on the object types and fields linked to it.

- Export your Relativity application as a RAP file for use in another workspace.

Estimated completion time - 1 hour

PREVIOUS LESSON

‹‹ Lesson 1 - Set up your developer environment

NEXT LESSON

Lesson 3 - Create a RESTful API ›› You can download and install the completed RAP for this lesson from https://github.com/relativitydev/server-doc-tutorials/tree/main/AdvancedTutorial/CompletedNoCodeRAP . To compare the no-code RAP, you can deploy it to a workspace, and then inspect the components in the Relativity Applications tab

## Step 1 - Create a new workspace through the Relativity UI

In a Relativity instance, users generally interact with data and other features within a workspace. The core workflows for Relativity are performed in a workspace, including coding documents, or running processing and productions. For more information, see Workspaces on the Relativity Documentation site.

As a developer, you may also conceptualize a workspace as a separate SQL database, and an environment for developing and testing new applications. This step illustrates how to create a workspace.

Tab naming in Relativity is highly customizable. Depending on how these customizations are made, you may see different tab names when navigating in your Relativity instance.

Use the following steps to create a workspace:

- Log in to your Relativity instance.

- Click New Workspace on this tab. The Workspace Information dialog appears.

- Enter the following information in the required fields. An asterisk appears next to a required field.

- Name - My First Workspace

- Matter - Relativity Template

- Template Workspace - New Case Template

- Default File Repository - \\RELATIVITYDEVVM\Fileshare

- Default Cache Location - Default Cache Location

- Click Save .

## Step 2 - Create an application in the workspace

Creating an applications is done at the Relativity workspace level. You can create an application without writing any code by adding object types, fields, views, and other components to it through the Relativity UI. In this step, you learn how to add an application to a workspace.

Use the following steps to create an application:

- Click to display your home page.

- Click My First Workspace in the list to display your workspace.

If your workspace isn't listed, complete the steps to update the view. Update the view to display your workspace

If workspace isn't listed, update the view as follows:

- Click for All Workspaces .

- Navigate to the Conditions tab.

- Click Clear All Conditions .

- Click Save . You should now see all workspaces.

- Click on My First Workspace .

- In the Sidebar, click > Application Admin > Relativity Applications .

- Click New Relativity Application . The Application dialog appears.

- Enter the following information in the required fields:

- Application Type - Create new Application

-

New Application Name - Hello Wikipedia

- Click Save .The details view of your new application appears. (Note: in the screenshot below, some of the buttons in the Relativity Applications console only appear if DeveloperMode is set to True. This is an Instance Setting. If DeveloperMode is set to True, then you will see it in a bar on the top of the screen. It looks like this

To enable Developer Mode, set the DeveloperMode Instance Setting to True (see screenshot below). If you change it to True, it will take a couple of minutes before it shows up on your web pages.

This instance setting is not recommended for Production environments.

- Click in center top of the page.

This page is added to your Favorites for quick reference while you work on the completing the tutorial.To access the page from Favorites, click and select it from the list.

## Step 3 - Create object types for your application

Object types encapsulate components of an application within Relativity. They contain one or more fields for data entry, views to display the data, tabs for navigation, and other features. They are essential elements for application development because they control how other items link to the application. This step illustrates how to create the object types required for the application. For more information, see Creating and editing Relativity Objects on the Relativity Documentation site.

Use the following steps to create new object types:

- Open the details view of your application.

See step 7 in Step 2 - Create an application in the workspace .

- Locate the Object Type section of the page and click New .

The Object Type Information dialog appears.

- In the Name field, enter Article Reference .

- Set Use Relativity Forms to Yes .

- Click Save and New .

Your Article Reference object type is created, and an empty Object Type Information dialog appears.

- In the Name field, enter Article Category .

- Click Save and Back . The Object Type section now displays the new object types that you created.

- (Optional) If the Object Type section doesn't list your updates, complete the steps to link an item. Link an item to the application

You can use these steps to link any item in the detail view to an application. This example uses the Object type section of the detail view.

- Click Link in the section title bar. The Select Items dialog appears.

- Use the filter boxes to locate an item. In this example, the Object Type filter is set to Article Category .

- Select the checkboxes for the items. This example shows the Article Reference and Article Category items selected.

- Click Add . The items now appear in the Selected Items section.

- Select the checkboxes again and click Set .The items should now appear in the application details view.

## Step 4 - Create fields for the application

Fields are used to store information for an object type. You can define how fields are validated and the type of information that they store. Additionally, fields link to object types and characterize the object type for the application. In this lesson, you create fields to associate with the object types added to the application. For more information, see Fields on the Relativity Documentation site.

Use the following steps to create new fields:

- Open the details view of your application.

See step 7 in Step 2 - Create an application in the workspace

- Locate the Fields section of the page, and click New .

The Field Information dialog appears.

- Enter the following information in the required fields. An asterisk appears next to a required field.

- Name - URL

- Object Type - Article Reference

- Field Type - Fixed-Length Text

- Maximum Length - 255

- Required - enabled

- Click Save and New .

Your new field is created, and an empty Field Information dialog appears.

- Repeat step 3 to create the following field.

After you create the field, click Save and Back .

Object type Field settings

Article Reference

- Name - Article Categories

- Object Type - Article Reference

- Field Type - Multiple Object

- Associative Object Type - Article Category

- Required - enabled

- Verify that the Field section lists the following fields.

- (Optional) If the Field section doesn't list your updates, complete the steps to link an item.

Filter on the appropriate field name. Link an item to the application

You can use these steps to link any item in the detail view to an application. This example uses the Object type section of the detail view.

- Click Link in the section title bar. The Select Items dialog appears.

- Use the filter boxes to locate an item. In this example, the Object Type filter is set to Article Category .

- Select the checkboxes for the items. This example shows the Article Reference and Article Category items selected.

- Click Add . The items now appear in the Selected Items section.

- Select the checkboxes again and click Set .The items should now appear in the application details view.

- Make the Name field required for Article Reference and Article Category by completing these steps:

- Click Link in the Field section.

- Set the Object Type filter to Article Category and the Name filter to name.

- Complete the steps for adding this field through the Select Items dialog.

- In the Field section, click the Edit link for Article Category.

- Enabled the Required field on the Field Information dialog and click Save .

- Repeat steps a - e for the Article Reference object type.

- Repeat steps 3 and 4 to create the following fields.

After you create the last field, click Save and Back .

Object type Field settings

Article Category

- Name - Automatic Updates Enabled

- Object Type - Article Category

- Field Type - Yes/No

Article Category

- Name - Overwrite Article Text

- Object Type - Article Category

- Field Type - Yes/No

- Verify that the Field section lists all fields that you created.

Complete the steps to link an item. Link an item to the application

You can use these steps to link any item in the detail view to an application. This example uses the Object type section of the detail view.

- Click Link in the section title bar. The Select Items dialog appears.

- Use the filter boxes to locate an item. In this example, the Object Type filter is set to Article Category .

- Select the checkboxes for the items. This example shows the Article Reference and Article Category items selected.

- Click Add . The items now appear in the Selected Items section.

- Select the checkboxes again and click Set .The items should now appear in the application details view.

- On the application details page, locate the Application console.

It displays the Show Errors link.

- Click Show Errors to display the Errors list.

Fix the error by linking the field created automatically when the Multiple Object field was tied to Article Category.

- Click Close on the Error list.

- Verify that the Field section lists all fields that you created.

See the following screen shot:

If any fields are missing, complete the steps to link an item.

Link an item to the application

You can use these steps to link any item in the detail view to an application. This example uses the Object type section of the detail view.

- Click Link in the section title bar. The Select Items dialog appears.

- Use the filter boxes to locate an item. In this example, the Object Type filter is set to Article Category .

- Select the checkboxes for the items. This example shows the Article Reference and Article Category items selected.

- Click Add . The items now appear in the Selected Items section.

- Select the checkboxes again and click Set .The items should now appear in the application details view.

- View the Application console and verify Show Error link is disabled, indicating that the issue was resolved.

## Step 5 - Update layouts to include fields for the application

Layouts represent the data entry portion for an object type and its fields. You can define how and where fields are placed when a user populates that object type with data by modifying its layout. This step illustrates how to update the default layouts for the object types with all the new fields created for them. For more information, see Layouts on the Relativity Documentation site.

Use the following steps to update layouts with application fields:

- Open the details view of your application.

See step 7 in Step 2 - Create an application in the workspace

- Locate the Layout section of the page.

- Update layouts automatically created for the Article Reference and Article Category object types by clicking Link .

The Select Items dialog appears.

- Verify that the Layout section lists the required layouts.

If necessary, complete the steps to link an item. Use the Object Type filter to locate the Article Reference and Article Category object types. Link an item to the application

You can use these steps to link any item in the detail view to an application. This example uses the Object type section of the detail view.

- Click Link in the section title bar. The Select Items dialog appears.

- Use the filter boxes to locate an item. In this example, the Object Type filter is set to Article Category .

- Select the checkboxes for the items. This example shows the Article Reference and Article Category items selected.

- Click Add . The items now appear in the Selected Items section.

- Select the checkboxes again and click Set .The items should now appear in the application details view.

- In Layout section, click the Article Reference Layout link.

The Layout Information dialog appears.

- Click Build Layout in the Layout console.

- In the Layout editor, drag and drop the URL field to the Drop Field box.

The center canvas changes in response to selected field as illustrated in the following screen shot.

- Drop and drag the Article Categories to the Drop Field box.

The canvas updates in response to selected fields as illustrated in the following screen shot.

- Click Save and Close .

- Click Back on the application tab or use your Favorites link to display the applications page.

See Step 2 - Create an application in the workspace .

- Repeat steps 5 - 9 for the Article Category Layout.

## Step 6 - Update views to include fields for the application

Relativity uses views to display object types and their fields when it displays data in the UI. You can edit a view by updating its layout. For example, you can determine which fields you want displayed for an object type by editing its views. In this step, you update the views associated with the object types in the application. For more information, see Views on the Relativity Documentation site.

Use the following steps to update views for the application:

- Open the details view of your application.

See step 7 in Step 2 - Create an application in the workspace

- Locate the View section of the page.

- Add the views automatically created for the Article Reference and Article Category object types by completing the steps to link an item.

Use the Object Type filter to locate the Article Reference and Article Category object types. Link an item to the application

You can use these steps to link any item in the detail view to an application. This example uses the Object type section of the detail view.

- Click Link in the section title bar. The Select Items dialog appears.

- Use the filter boxes to locate an item. In this example, the Object Type filter is set to Article Category .

- Select the checkboxes for the items. This example shows the Article Reference and Article Category items selected.

- Click Add . The items now appear in the Selected Items section.

- Select the checkboxes again and click Set .The items should now appear in the application details view.

- In View section, click the All Article Reference link.

The View Information appears.

- Click Edit Fields .

The Set Fields dialog appears.

- Select Article Categories and URL , and click .

The following screen shot displays the selected fields.

- Click Save .

- Click Back on the application tab or use your Favorites link to display the applications page.

See Step 2 - Create an application in the workspace .

- Repeat steps 5 - 8 for the All Article Category view.

## Step 7 - Set up tabs for the application

To access the views and layouts for an object type, you use a tab that links to the pages containing this information. New object types automatically have tabs, but they aren't linked to the application by default. In this step, you learn how to link tabs to your application. For more information, see Tabs on the Relativity Documentation site.

Use the following steps to link tabs to the application:

- Open the details view of your application.

See step 7 in Step 2 - Create an application in the workspace

- Locate the Tab section of the page.

- Add the tabs automatically created for the Article Reference and Article Category object types by completing the steps to link an item.

Use the Object Type filter to locate the Article Reference and Article Category object types. Link an item to the application

You can use these steps to link any item in the detail view to an application. This example uses the Object type section of the detail view.

- Click Link in the section title bar. The Select Items dialog appears.

- Use the filter boxes to locate an item. In this example, the Object Type filter is set to Article Category .

- Select the checkboxes for the items. This example shows the Article Reference and Article Category items selected.

- Click Add . The items now appear in the Selected Items section.

- Select the checkboxes again and click Set .The items should now appear in the application details view.

- After you have linked the two object type tabs, create a parent tab. The object type tabs will be associated with this parent tab.

- Click New in the Tab section.

- Enter the information for the parent tab as follows:

- Verify that it now appear on the left hand navigation bar with the folder icon.

- Use these steps to link the object type tabs to the parent tab:

- Click Edit for the Article Reference in the Tabs category and select Hello Wikipedia in the Parent field.

- Click Save .

- Repeat steps a-b for the Article Category tab.

- Verify that the tabs appear as follows in the left hand navigation bar:

## Step 8 - Add sample data through the Relativity UI

At this point in the lesson, you have completed the setup for structured data. You can populate the object types with data by entering it using the layouts, views, and tabs that you created.

Use the following steps to add sample data to your application:

- Log in to My First Workspace.

See Step 1 - Create a new workspace through the Relativity UI .

- In the Sidebar, find the Hello Wikipedia tab and navigate to the Article Category .

- Click the Article Category tab, and then click New Article Category .

The dialog for adding article categories appears.

- Enter Computer engineering in the Name field.

- Click Save .

- In the Sidebar, click to display a list of tabs.

- Click the Article Reference tab, and then click New Article Reference .

The dialog for adding article references appears.

- Enter the following information:

- Name - Computer engineering compendium

- URL - https://en.wikipedia.org/wiki/Computer_engineering_compendium

- For Article categories, click to display the Select Items dialog.

- Select and add the Computer engineering as in steps 7a - 7e in Step 3 - Create object types for your application .

- Verify that the completed form matches the following screen shot:

- Click Save .

## Step 9 - Create a dashboard

You can use widgets on a dashboard to organize data. These widgets are useful as the data in your workspace increases. Dashboards contain a pre-defined look and feel, as well as charts associated with a specific object type. For more information, see Dashboards on the Relativity Documentation site.

In this step, you create and update a dashboard on the Article Reference object. The dashboard lists the number of Article Reference instances grouped by Article Category.

Use the following steps to create a dashboard:

- In the Sidebar, click to display a list of tabs.

- Click the Article Reference tab.

(If you are currently on the Article Reference page, click Back .)

- Click the Dashboards drop-down menu in the top right corner of the window. Then click New Dashboard .

- Enter Article Reference Count by Category in the Name field.

- (Optional) To change the dashboard, select one from the Dashboards drop-down menu.

The newly created dashboard is currently in focus.

- To add a chart to the dashboard, click Add Widget .

- Enter the following widget settings:

- Group By - Article Categories

- Pivot On - <Grand Total>

- Review the result chart.

The results are based on your data. Because the subset of data is small, a simple chart appears, but it will expand in complexity as more data is added.

- In the Dashboards drop-down menu, click Save .

- Open the details view of your application to associate the dashboard with it.

See step 7 in Step 2 - Create an application in the workspace

- Locate the Dashboard section of the page.

- Click Link to associate the dashboard with the application. The Select Items dialog appears.

- Add the dashboard to the application by completing the steps to link an item.

Use the Name filter to locate the Article Reference Count by Category dashboard. Link an item to the application

You can use these steps to link any item in the detail view to an application. This example uses the Object type section of the detail view.

- Click Link in the section title bar. The Select Items dialog appears.

- Use the filter boxes to locate an item. In this example, the Object Type filter is set to Article Category .

- Select the checkboxes for the items. This example shows the Article Reference and Article Category items selected.

- Click Add . The items now appear in the Selected Items section.

- Select the checkboxes again and click Set .The items should now appear in the application details view.

- Verify that the dashboard is linked to the application.

## Step 10 - Finalize and export application

After you link the required items to your application, you can export it for installation in other workspaces and Relativity Instances. Relativity performs the following tasks when you export an application:

- Packages and versions the application.

- Locks the application to prevent further edits to its structural components, such as linked objects, object types, fields, and others. Although you can still add new Relativity Dynamic Objects (RDOs) to the application. The application must be unlocked to modify any other components using the Unlock Application button.

- Adds the application to the Application Library for easier distribution across workspaces.

To distribute an application, you can install it to other workspaces through the Application Library, or you can export a RAP file for uploading to other workspaces. You can also install the application on another workspace in a different Relativity instance using the RAP file.

Use these steps to export an application to a RAP file for distribution:

- Open the details view of your application.

See step 7 in Step 2 - Create an application in the workspace

- Verify that all the items required for the application are displayed on the detail view.

Use the information in the prior lessons for this purpose.

- Click Push to Library in the Application console.

- Located the Schema Version field on the application details view. The first time you press Push to Library, the Schema Version and the Application Version are both set to 0.0.0.1.

- To download a RAP file, click Export Application in the Application console.

## Step 11 - Install the application in a workspace

You can install an application created in one workspace on another workspace. In this step, you use a RAP file for installing the application. For more information, see Installing applications on the Relativity Documentation site.

Use the following steps to install the application in a workspace:

- Click to display the workspace list page.

- Navigate to the Sample Workspace application.

- In the Sidebar, click > Application Admin > Relativity Applications .

- Click New Relativity Application .

- In the Application Type field, select Import from File .

- In the File field, click Choose File to select your application RAP file for upload.

The upload process may take a few minutes.

- Expand tree in the Application Artifacts section to see a list of items in your application.

- Click Import when the upload successfully completes and the button is enabled.

- Click Yes on the Installation Alert pop-up window.

The Import Status window displays with a list of imported items.

- Click View Application Details .

The items displayed in this view for the Sample Workspace should match those displayed in My First Workspace.

## Step 12 - Verify that the application built

In this final step, you run the application on another workspace for verification.

Use the following steps to verify the application build:

- Navigate to the Sample Workspace .

- In the Sidebar, find the Hello Wikipedia tab.

- Navigate to the Article Category and confirm that it is empty.

The RDOs don't transfer between the workspaces.

They are unique to each workspace.

- Try out the features of your application in the new workspace.

Your application is ready for use.

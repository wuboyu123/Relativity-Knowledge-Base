---
title: "Migrating applications to Relativity Forms"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Migrating_To_Relativity_Forms.htm
collection: developer
fetched_at: 2026-06-22T06:31:49+00:00
sha256: 5831b6e3faf1ad1c567abbedbc8e8ac31912a1fe482f5c21d815c3b2c06bb4f3
---

Migrating applications to Relativity Forms Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Migrating applications to Relativity Forms

Relativity Forms is our solution for rendering all layouts in Relativity, which provides more controlled Relativity object customization through robust JavaScript APIs and granular front-end page lifecycles, on an evolving framework.

If you have customized user interfaces with Classic Forms, you will most likely need to update these customizations to use the new Relativity Forms approach.

Review the information in this topic to understand how your applications may be impacted. For an example of converting from Classic Forms to Relativity Forms, The Sample: Converting a Classic Form to a Relativity Form walkthrough demonstrates converting a Classic Form with event handlers to a Relativity Form.

## Determining if your applications are affected

If your applications use any of the customizations listed in the table below, you may need to make changes to ensure your applications function as desired after enabling Relativity Forms. If your application does not use any of the listed customizations, your application should be safe to enable with Relativity Forms, without modification.

Customization

Additional Notes

Console or PageInteraction event handlers

PreLoad event handlers to supply default values PreLoad is not fired for NEW object creation. You will need to Implement replaceGetNewObjectInstance to do value defaulting in Relativity Forms.

HTML-enabled fields, custom text fields, or custom labels that modify content elsewhere on the page

The only supported mechanism for adding script to a form in Relativity Forms is via the front-end javascript specified within ScriptFileName , or assets loaded from within them. Custom Text, Custom Label, and HTML-enabled values are no longer vectors for script.

Relativity Forms actively sanitizes all of these. HTML-enabled fields continue to work for a large amount of markup (and in some cases may support more than you can use in classic forms); but some tags, attributes, or attribute values are sanitized-away when displayed.

Script is removed when rendered, as are attributes that cause script, for example onclick properties, or an <a> tag’s href property if its value contains something like “javascript:[something]” (<a href=”javascript:alert(‘something’)”>example</a> will be changed to <a>example</a>)

Custom Text Fields and Custom Labels will not allow script, but allow a subset of markup when the rich text editor is used to write the content. Existing database values for labels, custom text, or html field values are not guaranteed to work within Relativity Forms, and should not be relied upon.

HTML or JavaScript content as part of PreLoad , PreSave , or PostSave event handlers

Any markup or JavaScript presence in Relativity Forms must be added within the JavaScript files referenced by ScriptFileNames property of Page Interaction Event Handlers.

Server-side logic in PreLoad event handlers will still occur for existing object instances (view or edit mode), as PreLoad .NET event handlers are executed by the ObjectManager in a default Read. (Note that because ObjectManager Read is what executes PreLoad Event Handlers, these do not execute on forms for creating new objects. For PreLoad functionality on NEW objects, the logic must move into the JavaScript, where you’ll implement a handler for replaceGetNewObjectInstance).

Server-side logic executed by PreSave and PostSave event handlers will still occur, as these .NET event handlers will still be executed by the ObjectManager in a default Save. However, If any of these event handlers used to inject HTML or JavaScript into the page (most commonly done via markup within the Message string) this is no longer supported, and will be treated as plain-text by Relativity Forms.

Object type event handler return values where the Message property is more than just plain-text (such as script or markup) The Message property will be treated as plain-text by Relativity Forms.

Event handlers employing PostExecutionAction , RedirectToLayout , or other redirections In Relativity Forms, the .NET event handlers are fired by the ObjectManager API, which has no access the Request or Response for the page itself. Run in this way, .NET handlers haves no ability to cause redirections. Redirections may be done in JavaScript code within the relevant pipelines.

To enable or switch to Relativity Forms, use the Object Type Settings screen to set Use Relativity Forms to Yes , as shown below:

## Classic Forms Deprecation Compliance Identification Tool

To assist in the migration from Classic Forms to Relativity Forms, we are providing an identification tool to determine if an object type will be negatively impacted by the migration. By default, this identification tool attempts to return every object type in every workspace, listing whether at least one .NET PageInteractionEventHandler, Pre-Load event handler, or Console event handler is present. The presence of these three event handlers on a Classic Forms page indicates action may be necessary to migrate to Relativity Forms.

This Identification tool is only provided for convenience. Do not rely on this tool for comprehensive reporting or absolute accuracy.

To use the provided tool:

- Download the SQL script provided at https://community.relativity.com/s/contentdocument/0691T00000I9d8jQAB (Note: Relativity Community login is required to access this resource)

- Create a new Relativity Script in the Relativity Script Library and copy the contents of the SQL script you downloaded in Step 1 into your new script.

- Give the script a name and description, provide other settings as needed, and set the timeout value to 180 seconds.

- The script can be freely used in the Relativity Script Library on the admin level

In the Modifiable Filters section at the start of the script, four variables are available that you can change to 1 or 0 to filter the list down to relevant results. Once the results appear, you can export them to a CSV file for further manipulation and filtering. Note that Relativity-provided objects will be included in the results and do not require action on your part, provided that you have not added your own custom event handlers to those Relativity-provided objects.

## Conceptual Differences

The table below lists the main conceptual differences between Classic Forms and Relativity Forms.

Classic Forms

Relativity Forms

Rendering

Server-side.

The page load life cycle occurs mostly on the web server before it is delivered to the browser. After this load, the page is delivered to the browser, and any embedded script is executed as the page renders in the client-side.

Front-end (in the browser), with server-side work accomplished by services invoked by the front-end.

A nearly empty page is delivered to the browser, which makes an API call to get Layout information and a list of file names of JavaScript files, which define the handlers for the front-end's page life cycle. Upon receipt of the API's response, the page requests each of the script files and turns them into code which handles the page's life cycle events.

The page then completes its rendering, executing the handlers for the load life cycle which were defined in the scripts which the page downloaded moments beforehand.

PageInteraction JavaScript Source String literal content or link generated in PopulateScriptBlocks function of a PageInteraction event handler

JavaScript resource files in your Application, referenced by ScriptFileNames property of the object type’s PageInteraction event handler.

Any script addition in Relativity Forms must be accomplished within JavaScript files specified by ScriptFileNames in a PageInteractionEventHandler . In some cases, markup changes/additions may be achievable by Custom Labels, Custom Texts, and HTML enabled fields; but this does not include script.

Consoles

Output of server-side Console event handler embedded into the page.

Sever-side work done within the same code which constructs the markup.

Server-side Console event handlers are ignored.

Consoles are created by PageInteraction JavaScript.

Server-side work done by services invoked by front-end script.

Lifecycle

Primarily server-side.

Embedded JavaScript is run as the page renders in the browser, placing the burden to control timing on the developer, with no explicit JavaScript API support from Relativity.

Lifecycle tailoring is most significantly handled via server-side event handlers allowing augmentation of reads, saves, and deletions.

Primarily front-end, divided into four main page operations:

- Load

- Change (interaction)

- Submit (save)

- Delete

Each operation consists of multiple named events which the JavaScript may handle to specifically time code execution.

Server-side create, read, update and delete operations can be completely replaced.

Default behavior of Relativity Forms will fire the server-side event handlers related to these operations.

JavaScript API support Nothing explicit

Named events that you can handle, allowing timing of code execution.

Each script handler is provided with script APIs consisting of:

- A this binding which contains methods and metadata specific to the currently active object and layout.

- A robust convenienceApi object supplying functionality to perform operations like directly accessing and manipulating fields without DOM lookup, making http requests, populating the page's Console, and more

Server-side object type event handlers for CRUD (create, read, update, and delete)

- PreLoad

- PreSave

- PostSave

- PreMassDelete

- PreCascadeDelete

- PreDelete

PreLoad does execute for new objects. PreLoad does not execute for new objects; value defaulting for new objects must be done in JavaScript.

## Considerations

- Long Text Fields : In Relativity Forms, long text field line endings are saved in a different format than Classic Forms. In Classic Forms, long text line endings get saved in the Windows format. In Relativity Forms, on the other hand, long text line endings are saved in whichever format is defined by the browser and operating system of the user. We do not recommend using the long text field as a means of saving a delimited value field. What is saved and rendered could change depending on how and where the field is saved.

## Frequently Asked Questions

What will happen if I do nothing?

If your applications are affected because they use functionality listed above and you do not make any changes, your customizations will fail when your applications are switched over to Relativity Forms..

I currently handle specific lifecycle customizations in place using Classic Forms. I need to make sure they still work when I convert to Relativity Forms. What do I need to do?

Refer to the load, change, submit, and delete pipeline differences described above, and see the corresponding documentation links: Load pipeline , Change pipeline (interaction), Submit pipeline (save), and Delete pipeline

I currently use the console event handler in my application that runs on Classic Forms. What do I need to do?

Console event handlers will not fire in Relativity Forms, but are instead triggered through the page interaction event handlers. You can see an example of the required changes in the Sample: Converting a Classic Form to a Relativity Form guide.

Is it possible to create a Page Interaction Event Handler that supports both Relativity Forms and Classic Forms?

Yes. The PopulateScriptBlocks() method will be ignored by Relativity Forms, and the ScriptFileNames() property will be ignored by Classic Forms. You can implement both PopulateScriptBlocks() and ScriptFileNames() in a Page Interaction Event Handler, and they will behave appropriately depending on whether Relativity Forms is enabled, or not.

On this page

- Migrating applications to Relativity Forms

- Determining if your applications are affected

- Classic Forms Deprecation Compliance Identification Tool

- Conceptual Differences

- Considerations

- Frequently Asked Questions


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

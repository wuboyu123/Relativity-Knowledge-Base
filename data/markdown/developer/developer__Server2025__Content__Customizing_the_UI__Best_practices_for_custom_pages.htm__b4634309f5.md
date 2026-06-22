---
title: "Best practices for custom pages"
url: https://platform.relativity.com/Server2025/Content/Customizing_the_UI/Best_practices_for_custom_pages.htm
collection: developer
fetched_at: 2026-06-22T06:31:19+00:00
sha256: 6e981faba194761951e6cb5214dd4277154c2ed710bf8b81e456c5b38e188c5d
---

Best practices for custom pages Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Best practices for custom pages

Use these guidelines to optimize your application development with custom pages.

## Use helper classes

Use the helper classes so that you program to an interface. This interface provides functionality for returning a database context and connecting to the Services API. These helper classes are in Relativity API Helpers available when you reference the Relativity.API.dll in your projects. Codes samples for custom pages illustrate how to establish this connection with the helper classes. For more information, see Basic concepts for custom pages and Using Relativity API Helpers.

## Secure custom pages as necessary

Set up security for custom pages if you're including sensitive data. Consider storing this information in a database or in a Relativity Dynamic Object (RDO), so that you can control the security on these items.

You set the security on the custom pages. A custom page verifies that the user is logged in to Relativity and has access to the application, but it doesn't validate any of the user's permissions.

## Authorize users for operations

Relativity automatically verifies that user is authenticated prior to displaying the custom page. However, you must authorize the user within the context of a custom page for operations, such as creating, updating, and deleting data.

## Avoid using underscores to begin file names

File names that begin with an underscore aren't deleted when you upgrade an application with custom pages. For example, the file called _filename.aspx won't be deleted, but it is overwritten if contained in the new package used for upgrade.

## Don't use restricted file types for custom pages

Don't use these restricted file types for custom page development:

- .exe (Executable program file)

- .com (MS-DOS program file)

- .pif (Shortcut to MS-DOS program file)

- .bat (Batch file)

- .scr (Screen saver file)

The instance setting called CustomPageRestrictedFileTypes determines which file types can't be uploaded to Relativity. See the Instance settings' descriptions on the Relativity Documentation site.

On this page

- Best practices for custom pages

- Use helper classes

- Secure custom pages as necessary

- Authorize users for operations

- Avoid using underscores to begin file names

- Don't use restricted file types for custom pages


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

---
title: "Relativity Forms API"
url: https://platform.relativity.com/Server2025/Content/Relativity_Forms/Relativity_Forms_API.htm
collection: developer
fetched_at: 2026-06-22T06:24:24+00:00
sha256: ed443145fb63889b17111570de0d05e0ce39432782477d051611eb61e3edfc6c
---

Relativity Forms API Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Relativity Forms API

## What is Relativity Forms?

We know that developers heavily customize Forms pages (view, edit, and new Layout pages). For this reason, we make it a priority to keep customization use cases top-of-mind. Relativity Forms is a Layout-rendering option, providing the developer with robust JavaScript APIs and a granular front-end page life cycle for easier, more controlled Relativity object customization.

If you have customized Classic Forms pages, be aware that Relativity Forms may introduce breaking changes to your classic forms customizations. See the Migrating applications to Relativity Forms topic for more information on migrating to Relativity Forms. .

The Implementing Relativity Forms event handlers topic provides details on how to use the Relativity Forms API.

## Concepts

Conceptually, a forms page has four main workflows:

- Load

- Change (also known as interaction)

- Submit (also known as save)

- Delete

Relativity Forms moves the page load into the life cycle to the front-end. A nearly empty page is delivered to the browser, which makes an API call to get Layout information and a list of file names of JavaScript files, which define the handlers for the front-end's page life cycle. Upon receipt of the API's response, the page requests each of the script files and turns them into code which handles the page's life cycle events.

The page then completes its rendering, executing the handlers for the load life cycle which were defined in the scripts which the page downloaded moments beforehand.

In the context of Relativity Forms, the four main workflows are referred to as pipelines:

- Load pipeline

- Change pipeline

- Submit pipeline

- Delete pipeline

In Relativity Forms, each of these pipelines has a set of life cycle events for which you may register handlers by name within one or more JavaScript files. This granularity removes any need on your part to write code which decides when code executes, and does not require you to manually wire logic up to UI components to accomplish that timing.

To aid you, each handler which you implement is provided with:

- A this binding which contains methods and metadata specific to the currently active object.

- A robust convenienceApi object supplying functionality to do things like directly access and manipulate fields without DOM lookup, make http requests , populate the page's Console, and more.

On this page

- Relativity Forms API

- What is Relativity Forms?

- Concepts


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

---
title: "Searching behind the scenes"
url: https://help.relativity.com/Server2025/Content/System_Guides/Searching_behind_the_scenes.htm
collection: user
fetched_at: 2026-06-22T06:21:16+00:00
sha256: dda4ae1d70ea11e2407bd9b3489733c20018b1525bd4e31bb50e8451cf39a0fd
---

Searching behind the scenes Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Searching behind the scenes

When you run a search in Relativity, depending on your data set, sometimes it takes a while for the search to return results. That's because there's a lot going on behind the scenes that can affect the speed of the search. This page explains the processes that the system goes through in order to execute the searches that you build in Relativity and to present the results to you in an item list. This information is designed for reference purposes only and doesn't include any required user action items.

By default, Relativity doesn’t check object security when executing a search, only Document security.

## Building the search in Relativity

Before Relativity can execute a search and return results to you in an item list, the system first constructs the search to determine which searches need to be part of the search that you're running and how to pass the results between them.

This is necessary in situations in which the search you're running references other saved searches. If you're running an isolated search that doesn't require existing saved searches as conditions, then this construction isn't necessary. In this case, the leaf search described below actually becomes the root search, as no other search relies upon its output.

The following searches are involved in a first pass construction of a complex search:

- Root search - the search you're running in Relativity.

- Branch search - a saved search that relies upon the output of a leaf search and is then referenced by the search you're running (the root search).

- Leaf search - a saved search that doesn't rely on the output of another saved search but is referenced by a branch search.

In the following abstract example, the system constructs a search that's based on the root that you're running, which references two levels of saved searches and works to the left from the leaf searches. Once it applies the conditions and relational filter for Leaf 1 and Leaf 2, it has the information needed to build Branch 1 (but not yet Branch 2, Branch 3, or Root). Once the system completes Branch 1, it can move on to Branch 2 and 3 and then proceed to the Root search on the left, which is the search you're running.

The following scenario provides an example of a first pass construction of a conflict check search, as described in the Advice recipe Using saved searches to complete conflict checks .

For details on how the system executes an internal search based on the constructions in the above abstract and scenario, see Executing the search in Relativity .

## Executing the search in Relativity

Once Relativity builds the complex search that you've started to run, it executes that search through the following process before sending the results back to you in an item list.

To execute the search, the system:

- Applies conditions to the leaf searches. This includes:

- Anything added as a condition on a search or view, not applied through a filter. This includes folder restrictions set through the Selected Folders choice on the Scope field on the saved search.

- The search index, which is any search provider (dtSearch, Analytics, Keyword Search, and custom search providers).

- Document permissions.

- Applies relational filters to the leaf searches. This includes places in which you’ve included family or duplicates, whether you’ve done so from the search page or the item list.

- Re-applies document permissions to the leaf searches.

- Applies conditions to the branch searches. For branch searches, this includes:

- Anything added as a condition on a search or view, not applied through a filter. This includes folder restrictions set through the Selected Folders choice on the Scope field on the saved search.

- Filtering by all child searches.

- The search index, which is any search provider (dtSearch, Analytics, Keyword Search, and custom search providers).

- Document permissions.

- Applies relational filters to the branch searches. This includes places in which you’ve included family or duplicates, whether you’ve done so from the search page or the item list.

- Re-applies Document permissions to the branch searches.

- Applies conditions to the root search. For the root search, this includes:

- Anything added as a condition on a search or view, not applied through a filter. This includes folder restrictions set through the Selected Folders choice on the Scope field on the saved search.

- Filtering by all child searches.

- The search index – any search provider (dtSearch, Analytics, Keyword Search, and custom search providers).

- The folder browser, cluster browser, or so on.

- Document permissions.

- Applies relational filters to the root search. This includes places in which you’ve included family or duplicates, whether you’ve done so from the search page or the item list.

- Re-applies Document permissions to the root search.

See Returning the search results for information on how Relativity actually shows the results of the search that it executed through the behind-the-scenes operations described in this section.

## Returning the search results

Once the system completes all the steps for the internal execution of a search, it performs the following steps to display the results of that search in an item list.

Starting with the root search, Relativity applies:

- Anything in the pop-out conditions pane on the item list, specifically through the Add a condition option. Note that a view is its own root search.

- The relational filter on the item list.

- Document permissions again.

- Any filters on the item list. This includes anything you've applied through the filter interface on the item list and nothing else.

- Sort conditions:

- If you selected no columns on the view, Relativity uses the root search or the view’s sort.

- If you selected a column, Relativity sorts by that column (ascending or descending, depending on which one you selected) and then ArtifactID in ascending order.

Once Relativity applies these items, it displays all search returns to you in an item list.

On this page

- Searching behind the scenes

- Building the search in Relativity

- Executing the search in Relativity

- Returning the search results


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

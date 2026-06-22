---
title: "Implementing categorization"
url: https://help.relativity.com/Server2025/Content/Solutions/Solving_review_case_challenges_with_Analytics/Implementing_categorization.htm
collection: user
fetched_at: 2026-06-22T06:12:17+00:00
sha256: 133eb3d76aa14bd8edbccd9c920cc36c536c0f026b9795e9077a012bbd7be310
---

Implementing categorization Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Implementing categorization

You must use categorization to identify the opposition's hot documents based on coding values assigned to your existing documents. In this scenario, your reviewers have already identified hot documents in your data set and coded them as hot with a multiple choice field. The coded documents serve as example documents for categorization to automatically find the opposition's hot documents.

The following sets of steps explain how to:

- Create a new saved search for use with creating the Analytics categorization set.

- Create a new Analytics categorization set.

- Synchronize and categorize all documents in your saved search.

The Analytics Categorization feature requires an Analytics search index. See Creating an Analytics index .

Categorizing an opponent's documents based on existing document coding requires you to first identify all the opponent's documents in your workspace with a saved search. Create a saved search for use when creating the Analytics categorization set:

- On the Documents tab, open the Saved Searches browser.

- Click New Search .

- Configure a new saved search with the following settings:

- Name - type the name of your new saved search. Be sure to use a relevant, unique name.

- Condition - select a Field and Operator combination that identifies only the opponent's documents in your workspace. For example, assuming the opponent's documents are not yet coded in your workspace, set Field to use the multiple choice field that includes the Hot choice used to code your documents. In some cases this field name may be "Issues". Set Operator to is not set .

- Fields - the default field selection is sufficient. Add additional fields if desired.

- Click Save & Search to save and execute the new saved search.

Use the following steps to implement categorization:

- Select the Analytics Categorization Set tab.

- Click New Analytics Categorization Set .

- Configure the following Categorization Setup options:

- Name - type a name for your new Analytics categorization set.

- Documents to Be Categorized - click the ellipsis and select your new saved search that includes only the opponent's documents not yet coded.

- Analytics Index - click the ellipsis and select an Analytics index that includes the opponent's documents.

- Categories and Examples Source - choose the field that indicates hot documents.

- Click Save .

- Click Create Categories and Examples on the Categorization Set console.

- Click OK to generate new categories and examples.

- (Optional) Click Refresh Page on the console to update the page and view the most current categorization status.

- Once synchronization completes, click Categorize All Documents on the console.

- Click OK to run categorization.

On this page

- Implementing categorization


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

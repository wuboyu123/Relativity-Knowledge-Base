---
title: "Search"
url: https://help.relativity.com/Server2025/Content/System_Guides/User_quick_reference/Searching_Quick_Reference/Search.htm
collection: user
fetched_at: 2026-06-22T06:10:23+00:00
sha256: c4ce66e9932a66ac2518dfa257ba27d7bf25eb7b5af7a0a427f69dba890df4e6
---

Search Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Searching quick reference guide

Use this search quick reference to improve your understanding of searching within Relativity.

## Fields types and filter types

Field type Boolean Text box Single-choice list Multi-choice list Pop up Custom/Advanced

Fixed-length text √ √ √

Long text √ *

Date

√ √

Number

Whole, decimal, currency √ √

Yes/No √

Single choice √ √

Multiple choice √ √

Single object √ √ √

Multiple object √ √ √

Long text search in text box only works if the field is not enabled for data grid.

## dtSearch strings and operators

dtSearch string Results

salt pepper The exact phrase salt pepper .

salt and pepper The word salt and the word pepper .

"salt and pepper shaker" * The exact phrase salt and pepper shaker .

salt or pepper Either salt or pepper .

salt w/5 pepper Salt appears within five words of pepper .

salt NOT w/5 pepper Salt does not appear within five words of pepper .

salt pre/5 pepper Salt appears within five words before pepper .

salt and not pepper Salt appears but pepper does not.

salt* Any word that begins with salt . For example, salted or saltiness .

When searching "salt and pepper shaker", dtSearch assumes the word and was removed from the noise words list.

## dtSearch fuzzy searching and stemming

Character Definition Example

% Fuzzy searching "app%%" matches apply and apple, but not applied

~ Stemming "apply~" matches apply, applied, applies, and so on

## Search operators and field types for saved searches

Operator Fixed-length text, long text, extracted text Whole number, decimal, currency User Date Yes/No Single choice, multiple choice

All of these, Not all of these √

Any of these √ √

Between √

Contains √ *

Does not contain √ *

Is √ * √ √ √

Is after, Is after or on √

Is before, Is before or on √

Is greater than √ * √

Is in √

Is less than √ * √

Is like √ *

Is logged in user √

Is not √ * √ √ √

Is not like √ *

Is not set √ √ √ √ √ √

Is set √ √ √ √ √ √

None of these √ √

Fixed-length text, long text, extracted text fields marked with an asterisk only work if the field is not enabled for data grid.

Filter Description

Boolean Available for Yes/No field types. Conditions display a drop-down list similar to list filters.

CustomOnly Uses filtering criteria from advanced and Boolean operators.

List Usually associated with fields used for coding documents. Conditions vary by the type and purpose of the field associated with it.

Multi list Uses multiple conditions from a drop-down menu. You can connect the conditions with the OR or AND operator.

Pop-up pickers Contains values for multiple or single choice fields, as well as multiple or single choice objects.

Textbox

Used to search on specific terms, numbers, and dates. You can enter multiple terms connected by any of the following operators:

-

AND

-

OR

-

BETWEEN

-

= (equal)

-

>= (greater than or equal to)

-

<= (less than or equal to)

-

% (to filter for NOT null)

On this page

- Searching quick reference guide

- Fields types and filter types

- dtSearch strings and operators

- dtSearch fuzzy searching and stemming

- Search operators and field types for saved searches


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

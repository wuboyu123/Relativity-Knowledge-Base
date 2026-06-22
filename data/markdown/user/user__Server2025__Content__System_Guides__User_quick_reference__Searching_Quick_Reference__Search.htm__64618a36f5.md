---
title: "Search"
url: https://help.relativity.com/Server2025/Content/System_Guides/User_quick_reference/Searching_Quick_Reference/Search.htm
collection: user
fetched_at: 2026-06-22T06:10:23+00:00
sha256: c4ce66e9932a66ac2518dfa257ba27d7bf25eb7b5af7a0a427f69dba890df4e6
---

Search

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

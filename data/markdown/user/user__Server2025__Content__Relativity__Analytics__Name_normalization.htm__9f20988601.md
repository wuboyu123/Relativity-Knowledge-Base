---
title: "Name normalization"
url: https://help.relativity.com/Server2025/Content/Relativity/Analytics/Name_normalization.htm
collection: user
fetched_at: 2026-06-22T06:05:04+00:00
sha256: 44a53bed346e01460e036ea8a979ccaf17bfe9d84b405c224558e510ec04f4b5
---

Name normalization Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Name normalization

Name Normalization analyzes email document headers to identify all aliases (proper names, email addresses, etc.) and the entities (person, distribution group, etc.) those aliases belong to. Name normalization automatically merges entities with those created by Legal Hold, Processing, or Case Dynamics.

See these related pages:

- Name normalization results

- Alias object

- Entity object

- Name normalization quick reference guide (PDF)

- Common searches with the entity object and name normalization

- Structured analytics

- Running structured analytics

## Name normalization overview

The name normalization process includes the following steps at a high level:

First, the operation parses header data (From, To, Cc, Bcc) from every segment within an email document using the same logic as email threading. Once the header data is parsed, name normalization identifies aliases within each section, looking for semi-colon delimiters to identify multiple aliases. Each unique alias is stored and matched with an unnamed entity.

Consider the following email segment:

Segment

From: john.doe@example.com

To: jason.smith@example.com; mary.adams@example.com

Cc:

Bcc:

Date: 11/01/2018 10:00AM

Subject: Let's talk about NN

Hey Jason, How's Name Normalization going?

Does your team need any help? Cheers, John

Name normalization identifies the following aliases:

Entity Alias

Entity 1 john.doe@example.com

Entity 2 jason.smith@example.com

Entity 3 mary.adams@example.com

If an alias is in one of the formats below, the full alias is stored as well as separate aliases for the description (Doe, John) and the email address (john.doe@example.com). All three aliases are joined to the same entity.

- "Doe, John" <john.doe@example.com>

- 'Doe, John' <john.doe@example.com>

- Doe, John <john.doe@example.com>

- 'Doe, John' [john.doe@example.com]

- Doe, John [john.doe@example.com]

For example, if an email segment contains "Doe, John" <john.doe@example.com> , name normalization identifies the following aliases:

Entity Alias

Entity 1

- "Doe, John" <john.doe@example.com>

- Doe, John

- john.doe@example.com

Generic aliases, such as Mom or John , are not created to limit over-merging.

If a newly identified alias matches an existing alias, it isn't created again. However, name normalization uses logic to match alias siblings to the same entity.

For example, imagine after identifying "Doe, John" <john.doe@example.com> , like in the example above, "Doe, John" <jdog99@domain.com> is identified. All of the aliases are linked to the same entity based on the matching "Doe, John" alias:

Name normalization limits the number of aliases assigned to a single entity to prevent over merging.

Entity Alias

Entity 1

- "Doe, John" <john.doe@example.com>

- Doe, John

- john.doe@example.com

- "Doe, John" <jdog99@domain.com>

- jdog99@domain.com

To further improve results, entities with the same first name and last name values are automatically merged with each other. Also, entities identified by name normalization are automatically merged with those created by Legal Hold, Processing, or Case Dynamics when their first and last name values match.

Name normalization also uses segment matching to infer relationships between different aliases that appear in the email headers. Consider the segments below from two different documents:

Segment 1 (from Document X) Segment 2 (from Document Y)

From: Doe, John

To: jason.smith@example.com

Cc:

Bcc:

Date: 11/01/2018 10:00AM

Subject: Let's talk about NN

Hey Jason, How's Name Normalization going?

Does your team need any help? Cheers, John From: johnathan.doe@example.com

To: jason.smith@example.com

Cc:

Bcc:

Date: 11/01/2018 10:55AM

Subject: Let's talk about NN

Hey Jason, How's Name Normalization going?

Does your team need any help? Cheers, John

By analyzing the body text and date sent, name normalization identifies these two segments as matching. It then uses different strategies to determine if the aliases match.

## Using enhanced domain filtering

When you create a structured analytics set for name normalization, the Enable additional domain filtering option controls the types of filtering available for extracted email domains. By default, this option is set to No . This puts all extracted email domains into a set of fields with simple text filtering.

If you choose Yes for Enable additional domain filtering , the name normalization operation also puts the extracted email domains into a set of additional fields. These fields have enhanced filtering capabilities, stronger text standardization, and support for tracking all domains in a single list.

The names of the default and enhanced domain fields are as follows:

Default field name Enhanced field name Definition

Alias To::Domain Alias Email To Domain Email domain identified in the To section of the document's top-most segment header

Alias From::Domain Alias Email From Domain Email domain identified in the From section of the document's top-most segment header

Alias CC::Domain Alias Email Cc Domain Email domain identified in the CC section of the document's top-most segment header

Alias BCC::Domain Alias Email Bcc Domain Email domain identified in the BCC section of the document's top-most segment header

Alias Recipient::Domain Alias Email Recipients Domain Email domain identified in the To, CC, or BCC section of the document's top-most segment header

For full instructions on creating a structured analytics set for name normalization, see Running structured analytics .

### Differences between default and enhanced domain fields

The following are the key benefits of the enhanced domain fields:

-

They standardize all domain names to lowercase, regardless of letter case in the original email.

-

They remove all empty values.

-

They remove duplicates of the same domain in the same field.

-

They have multi-select filtering options when viewed from the document list.

Click to expand comparison images:

Key difference Default field example Enhanced field example

Lowercase domains

Removing empty values

Note the empty value in the second row, marked by red.

Removing duplicate domains in the same field

Multi-select filtering options instead of text filtering

### Creating and exporting a list of domains

The enhanced domain fields store data as Relativity dynamic objects (RDOs). This format gives extra flexibility for manipulating and exporting the data as needed. One use is to create an exportable list of all email domains in the document set. This list can also be saved as an easy-to-access tab in the sidebar.

To track domains in a single list and export them to other formats, complete the following:

#### Prerequisites for creating a domain list tab

To extract the domains before creating a list, complete the following:

-

Create a saved search containing the documents you want to extract email domains from.

-

Run name normalization on that saved search with the Enable additional domain filtering option set to Yes . For full instructions, see Running structured analytics .

The results will be stored in the enhanced domain fields. For a list of field names, see Using enhanced domain filtering .

#### Creating a domain list tab

To create a tab containing a list of all domains, complete the following:

-

Under Configure , go to Workspace Admin , then Tabs .

-

Click New Tab .

-

Fill out the fields as follows:

-

Name - enter "Domains" or similar.

-

Tab Type - select Object .

-

Object Type - select Alias Domain .

-

Show in Sidebar - to create an icon for the domains list tab in the sidebar, toggle this On . If you do not want the icon in the sidebar, leave this Off . The tab will still be accessible from the All Tabs menu.

-

Order - enter an integer value. Lower numbers make the tab appear higher in the sidebar, but the exact position will depend on the numbers assigned to your other tabs.

-

Click Save . Your Domains tab will now appear in the All Tabs menu. If you selected Show in Sidebar , it will also appear there.

For more information on creating new tabs, see Tabs .

#### Exporting a domain list

To export the domain list to CSV format, complete the following:

-

Navigate to the newly created Domains tab.

-

Select all domains, then choose Export to File from the Mass Actions drop-down at the bottom of the grid. An options modal will appear.

-

Select Comma Separated Values (.csv) , then click Export .

## Adding a Classification value for Legal Hold

If Processing or Legal Hold are installed in your workspace with Analytics, we strongly recommend that you add a Classification value to your existing entities so that you can differentiate between them and the entities created by the name normalization operation. A Custodian - Processing value exists, but you must manually create a value for Legal Hold.

To do this, complete the following:

- Create a choice called Custodian - Legal Hold on the Classification field on the Entity object.

- Select all of your existing Legal Hold entities and perform a Mass Edit to add the Custodian - Legal Hold classification value to these objects.

- Select all of your existing Processing entities and perform a Mass Edit to add the Custodian - Processing classification value to these objects.

- Once completed, you can search or filter on the Classification field to observe specific entities.

## Special considerations

Before running the name normalization operation, note the following:

-

We generally recommend that you run name normalization in its own structured analytics set for maximum flexibility. While it is faster to run multiple structured analytics operations together in one set, you may find that you are ultimately constrained if you want to make modifications to the document set or the settings.

-

In order to run name normalization, you must have at least a From field and one other email header field such as To, CC, BCC, Subject, or Date Sent. If these fields do not exist, name normalization will attempt to analyze the extracted text and locate a From field within it.

- You can add aliases by importing through the RDC, manually creating them from an Entity layout page, or manually creating them on the Alias page and then linking them to an entity via the Assign to Entity mass operation.

We recommend adding aliases like email addresses, unique variations of the entity's name (e.g. John Doe; Doe, John), or any other unique identifiers that may be used by this entity.

If you do not add these values prior to running name normalization, you can still use the Merge mass operation to consolidate duplicate entities. For more information, see Entity object .

On this page

- Name normalization

- Name normalization overview

- Using enhanced domain filtering

- Differences between default and enhanced domain fields

- Creating and exporting a list of domains

- Adding a Classification value for Legal Hold

- Special considerations


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

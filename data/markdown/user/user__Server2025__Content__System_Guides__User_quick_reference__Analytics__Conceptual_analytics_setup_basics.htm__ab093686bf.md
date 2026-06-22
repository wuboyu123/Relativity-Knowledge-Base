---
title: "Conceptual analytics setup basics"
url: https://help.relativity.com/Server2025/Content/System_Guides/User_quick_reference/Analytics/Conceptual_analytics_setup_basics.htm
collection: user
fetched_at: 2026-06-22T06:10:30+00:00
sha256: cc7a285dc5e1752cdf2856d787d8f26365051d9f17d2275f02cfeecb4974cf1b
---

Conceptual analytics setup basics Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Conceptual analytics setup basics

This quick reference guide contains basic workflows for setting up an Analytics conceptual index and the conceptual analytics tools. For more detailed information, see Analytics .

## Analytics index setup

The analytics index is the cornerstone for conceptual analytics tools.

### Creating a data source

Set up a saved search which will become the data source for the index. This searches for documents with Extracted Text smaller than 30 MB.

Use the following conditions and fields:

- Name —enter a name for your search such as Conceptual Analytics Index Search.

- Conditions

- Extracted Text Size > 0

- Extracted Text Size < 30000

- Fields —Extracted Text Including the Extracted Text Size field assumes you used Relativity Processing. If you did not use Relativity Processing, first populate the Extracted Text Size field with data.

### Creating the Analytics index

Use the following settings to set up the Analytics index:

- Index Information

- Name —enter Conceptual Analytics Index.

- Index Type —select Conceptual .

- Data source —select the saved search created above.

- Order —set the order or leave as default.

- Advanced Settings

- Training data source —this will default to the same saved search as the data source.

- Optimize training set —set to Yes .

- Dimensions —leave as default.

- Remove English signatures and footers —set to Yes .

- Enable email header filter —set to Yes . Note that you can’t alter this setting unless you set the previous setting to No.

- Stop words —leave as default.

- Optional Settings

- Email notification recipients —enter any email address for those who need to be contacted when the index has been created or if there is an error.

### Adding repeated content filters

Repeated content filters are created in structured analytics and can also be added by hand. They are added to an Analytics index to remove any boilerplate text that would distort the conceptual relationship of the documents. For more information, see Repeated content filters .

To add a repeated content filter to an existing index:

- Click on the Repeated Content Filters tab in the bottom panel of the console.

- Click Link .

- On the Repeated Content Filter modal, find and select the repeated content filters to link to the profile. We recommend sorting by largest number of occurrences.

- Click Apply .

## Analytics categorization sets

Analytics categorization uses manually selected example documents as a basis for identifying and grouping other conceptually similar documents. Unlike clustering, you can use categorization to place documents into multiple categories if a document is a conceptual match with more than one category. It also takes user decisions on a few example documents and categorizes all other documents based on those decisions.

### Creating workspace fields

Unless your template has the fields listed below, you must create them to use categorization sets in a project.

Field name Object Field type

Category Designation Document Single choice or multiple choice

Category Indicator Document Yes/No

Additionally, you must add choices for the Category Designation field.

### Creating a category designations layout and assigning examples

Have your reviewers go through a sample of documents and assign designations to those determined to be good examples for the category. Tag at least 5 to 20 documents and no more than a few thousand. For explanation about what makes a good example document, see Identifying effective example documents .

Only documents that are part of the data source of your conceptual index can serve as examples.

If you want to add a pre-existing Issue field to a categorization set, you may want to conduct a QC review of the example documents that will be used for categorization. We recommend setting up a designated layout for reviewers to tag documents, and do not use the right-click functionality in the viewer.

### Sample layout

- Layout name —enter a name for the layout.

- Fields

- Category Designation

- Category Indicator

### Creating the categorization set

The Analytic categorization set is used to identify the documents, Analytics index, fields and other criteria needed for categorization

Use the following settings to set up the Analytics categorization set:

- Name —enter a name for the categorization set.

- Documents To Be Categorized —select the saved search containing the documents to be categorized. Only include documents that are also part of the data source of your Analytics index.

- Analytics Index —select the index you created that defines the conceptual space.

- Minimum Coherence Score —leave as default.

- Maximum Categories Per Document —leave as default.

- Categories and Examples Source —select the Category Designation field.

- Example Indicator Field —select the Category Indicator field.

- Auto-Synchronize on Categorize All —set to No to disable automatic category and example creation.

- Email notification recipients —enter any email address for those who need to be contacted when categorization is complete.

## Clustering

Once the Analytics index has been created, you can execute the clustering mass action from the Document list. You can create multiple clustering sets based on a search or sub-set of documents.

To use the clustering mass action:

- Navigate to the Documents tab and find the documents you want to cluster.

- Select the documents you want to cluster individually or select All from the drop-down menu.

- Select Cluster from the mass operations drop-down menu.

- Select Cluster .

- Complete the following fields:

- Cluster Options

- Name —enter a name for the cluster set

- Relativity Analytics Index —select the conceptual index that includes the documents you want to cluster.

- Advanced Options

- Title Format —leave as default.

- Maximum Hierarchy Depth —leave as default.

- Minimum Coherence —leave as default.

- Generality —leave as default.

- Create Cluster Score Field —leave this as No unless you want to know each document’s coherence score. Setting this to Yes significantly slows down the clustering process.

- Click Submit for Clustering .

## Find similar documents, keyword expansion, and concept searching

These conceptual analytics tools do not require any additional setup. For more information on them, see Analytics .

On this page

- Conceptual analytics setup basics

- Analytics index setup

- Creating a data source

- Creating the Analytics index

- Adding repeated content filters

- Analytics categorization sets

- Creating workspace fields

- Creating a category designations layout and assigning examples

- Sample layout

- Creating the categorization set

- Clustering

- Find similar documents, keyword expansion, and concept searching


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

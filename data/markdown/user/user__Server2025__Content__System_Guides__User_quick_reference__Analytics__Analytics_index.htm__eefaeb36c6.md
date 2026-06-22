---
title: "Analytics index quick reference guide"
url: https://help.relativity.com/Server2025/Content/System_Guides/User_quick_reference/Analytics/Analytics_index.htm
collection: user
fetched_at: 2026-06-22T06:10:29+00:00
sha256: eeacc3de5a00226b61e222bcb71d79c657d18ca6b18dfce973326a617fa84d9a
---

Analytics index quick reference guide Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Analytics index quick reference guide

This quick reference guide provides basic instructions for creating an Analytics conceptual index. This index can be used for concept searching, finding similar documents, categorization, clustering, and keyword expansion.

For more detailed information, see the Analytics section of the documentation site.

## Creating an Analytics conceptual index

- Create a saved search to serve as your data source. The data source is the collection of documents on which you want to perform any conceptual analytics operation. This search should only pull back authored content fields (ex. extracted text) and typically needs no additional conditions.

- Click the Indexing & Analytics tab and select Analytics Indexes .

- Click New Analytics Index .

The Analytics Index Information form appears.

- Complete the following fields on the Analytics Index Information form.

- Name —enter a name for the index.

- Index type —select Conceptual .

- Data source —select the saved search you created in Step 1. The Training data source field automatically populates with this same saved search.

- Order —enter an order for the index. The order determines the relative position of the index in the search drop-down along with other search providers such as dtSearch and keyword search.

Leave all other fields under Advanced Settings as default. For a complete description of the Analytics index fields, see Analytics indexes .

- Click Save .

The index console will appear.

- Click Run .

If this is your first time running the index, it will automatically build the full index. Otherwise, select Full .

## Index stages

Index creation consists of three stages: Population, Building, and Activating. The following steps occur during each stage:

### Population

- All documents from the data source and training data source are staged and flagged for pre-processing.

- Document pre-processing occurs to clean up text in the following ways:

- Numbers and symbols are ignored.

- All words are made lowercase.

- Filters found under Advanced Settings are applied, such as regular expression filters.

- Repeated content filters are applied.

### Building

- Training data source documents and Latent Semantic Indexing (LSI) are used to build the concept space based on the relationships between words and documents.

- Data source documents are mapped into the concept space.

- Stop words are filtered from the index to improve quality. These are very common words such as "an" or "the".

### Activating

- Makes the index active and available in the search indexes drop-down menu.

- Saves the index to RAM which loads the index into memory. If you find yourself running out of free RAM on the Analytics server, deactivate your index. Analytics indexes are automatically deactivated after 15 days of inactivity. You can reactivate the index from the index console.

### Common workflows

There may be times when you need to update your index. Depending on the update you’re making, you can save time by running an incremental population. The following table outlines workflows for different index updates.

Workflow Index update

Adding new documents that:

- Introduce new concepts.

- Make up more than 10%-30% of your document population.

- Add documents to both the data source and training data source.

- Click Run , then select Incremental .

Adding new documents that:

- Do not introduce new concepts.

- Make up less than 10%-30% of your document population.

- Add documents to the data source only.

- Click Run , then select Incremental .

Removing documents from the data source or training data source.

- Remove documents from the data source or training data source.

- Click Run , then select Incremental .

Updating stop words.

- Update stop words.

- Click Run , then select Full .

Updating extracted text. For example, updating low-quality OCR text.

- Update extracted text.

- Click Run , then select Full .

Updating filters. For example. email header and repeated content.

- Update filters.

- Click Run , then select Full .

On this page

- Analytics index quick reference guide

- Creating an Analytics conceptual index

- Index stages

- Population

- Building

- Activating

- Common workflows


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

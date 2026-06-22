---
title: "Transform sets"
url: https://help.relativity.com/Server2025/Content/Relativity/Transform_sets.htm
collection: user
fetched_at: 2026-06-22T06:08:29+00:00
sha256: 18387c0723f3d8c998ff550e9428ef6571d79d25f1b4f219f64bfe215f0c833f
---

Transform sets Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

Version: RelativityOne Server 2025 Server 2024

☰

# Transform sets

Transform sets are a feature of Relativity that uses custom code to extract data from a source Relativity field and output it to a destination field. The custom code is referred to as a handler, which is defined by specific rules about how to manipulate the data stored in the Relativity source field.

Relativity contains two types of transform sets: domain and conversation index parsing.

## Domain parsing

Domain parsing is a Relativity-defined handler that extracts email domains from email addresses in a document set. For example, "jsmith@example.com" yields "example.com." The domain parsing transform set places the domains in a destination field that you define.

Domain parsing now offers two handler options:

- Domain Parsing - SMTP Only —the SMTP Only handler will only parse domains from properly formatted SMTP email addresses. Source fields must contain the @ symbol and a . extension.

- Domain Parsing - SMTP, X400, X500 —the SMTP, X400, X500 handler domain will parse domains from properly formatted SMTP, X400, and X500 email addresses.

### Prerequisites

Before creating a new transform set, you need to create an object to hold the output, a field to hold the output, and a saved search that contains the documents to extract the domains from. Use the following sections to complete the prerequisites.

To create a new object, see Relativity objects .

When you create your object, make sure to configure the following fields correctly:

- Name —the name of your object appears as a tab on your screen. Consider naming your domain parsing object Domain for ease of use.

- Parent Object Type —this should remain the default of Workspace .

- Enable Snapshot Auditing On Delete —this should remain the default of Yes .

To create a new field to hold the data connected to your object, see Creating and editing fields .

When you create the field, make sure to configure the following fields correctly:

- Object Type —Document.

- Name —consider naming this field Recipient Domain for ease of use. However, you can use whatever name you like.

- Field Type - Multiple Object .

- Associative Object Type —select the Object you just created (Domain).

You also have the option to set the Object Type field to Domain and set the Associative Object Type to Document .

To create a saved search, see Creating or editing a saved search .

This saved search contains the documents you want to extract the data from. When you create the saved search, select documents for which the email from field is set.

### Creating a domain parsing transform set

To create a domain parsing transform set:

- Navigate to the Transform Sets tab.

- Click New Transform Set .

- Complete the fields on the form. See Fields .

- Click Save .

### Fields

The domain parsing transform set contains the following fields:

- Name —the name of the Transform Set.

- Data Source —the saved search on which the transform will run. Select the newly created saved search.

- Handler —the handler on which the transform will run. Choose one of the following:

- Domain Parsing - SMTP Only —use this handler if the fields you are parsing from only include SMTP email addresses.

- Domain Parsing - SMTP, X400, X500 —use this handler if the fields you are parsing from include X400 and/or X500 email addresses

- Status —the status of the job after it has been run. The possible choices for this field include:

- Pending

- Processing

- Completed

- Completed with Errors

- Stopped by User

- Last Run Error —lists the last error encountered if the job was completed with errors.

### Adding a transform

To add a transform to the email domain parsing transform set:

- Click New on the transform you just created.

The Add Transform window appears.

- Fill out the fields on the form. See Fields .

- Click Save .

### Fields

The Add Transform window contains the following fields:

- Transform Set —automatically populates with the transform set you created.

- Name —the name of the transform you are adding.

- Source Field —the field that holds the data to be processed. You can choose any email field. For example, To, From, CC, BCC.

- A popup picker displays all fields that you have rights to see, as well as the object type, field name, and field type. The transform can only be saved if this field is a Document object of fixed length type or long text field type.

- The source field must be a standard text field. No identifier, associative, relational, or system fields can be used.

- Destination Field —the field that holds the results of the process. Choose the field you created above, Recipient Domain.

If you use a Destination Field that is tied to an existing object, you will overwrite the field. You will not be able to add the results of new records without overwriting the existing data.

### Running the transform set

After you create the domain parsing transform set and add a transform to it, you can run the transform set. To run your transform, click Start Transform: Full from the console.

The console contains the following options:

- Start Transform: Full —wipes out all content in the Destination field and runs all transforms.

- A confirmation message states, "Performing a full run will erase all content in the selected destination field(s). Are you sure?"

- This is available when:

- There is at least one transform.

- There is no active job.

- Start Transform: Incremental —runs the transform set on all documents that have not yet been run. No values are deleted. This is available when:

- There is at least one transform.

- There is no active job.

- At least one document has gone through the transform process. The new documents should be added to an existing Transform data source.

- Stop Transform —active when a run has been submitted and is still running. You can stop the transform process.

- Retry Errors —attempts to re-run documents containing errors. This is available when:

- There is at least one document in error state.

- There is no active job.

- Show Errors —shows the documents containing errors. This is available when at least one document is in error state.

- Refresh Page —refreshes the page to see the current processing status. When the transform set runs, it goes through source fields, finds email addresses, and extracts the domains.

When the transform set finishes running, the Status field in the Transform Set Information section updates to Completed , and the domain results appear on the page.

To more easily review the results of your domain parsing transform set, use the following steps to edit the layout to include the results:

- Navigate to the layout you want to include the transform set results.

- Click Edit .

- Click Add Associative Object List , and then set the associative object to the Domain object you created when building the transform set.

- Set both the View and Link View fields to Documents .

Consider the following when reviewing your returned domains:

- If no text exists in the source field, nothing will be written to the destination field.

- If the text is unidentifiable in the source field, nothing will be written to the destination field.

- If more than one domain is in a field, more than one domain will be connected to the document.

- If you use Domain Parsing - SMTP, X400, X500 , and a domain is both in the X400 or X500 email format and contains an "@" symbol, domain parsing may return multiple domains from the same email address.

- If you use Domain Parsing - SMTP, X400, X500 , the time to run and complete the domain parsing will be longer than Domain Parsing - SMTP Only .

- Domain Parsing - SMTP, X400, X500 is a new feature that might not correctly parse domains from every variation of those email formats. Please review the formatting and delimiters of your email addresses as well as the output of your Domain Parsing in order to confirm domains were correctly parsed.

### Domain Parsing - SMTP, X400, X500

Please see below for more information and examples of key-value pairs, delimiters, and parsing domains logic:

#### Email domains

- SMTP —jane@example.com

- SMTP, X400, X500

- Variation 1 - <o=Example/ou=Lawyer/cn=Recipients/cn=Jane Doe>

- Variation 2 - Doe, Jane <IMCEAEX-_O=EXAMPLE_OU=EXCHANGE+20ADMINISTRATIVE+20GROUP+20+28SFJKDFDJK498NBU+29_CN=RECIPIENTS_CN=JANE@EXAMPLE.COM>

- Variation 3 - Doe, Jane [/O=EXAMPLE/OU=FIRST ADMINISTRATIVE GROUP/CN=RECIPIENTS/CN=JDOE]

#### Delimiters

Email addresses must be delimited from one another using a semi-colon (;) or a comma (,). Email addresses formatted in X400 and X500 must be internally delimited using commas or forward slashes (/). This does not apply to IMCEAEX format, which is delimited internally using underscores.

#### Key-value pairs

Within email addresses, key-value pairs are identified using an equal sign within comma-delimited or forward-slash delimited groups.

Domain Parsing – SMTP, X400, X500 is a new domain parsing option. If you would like to share feedback, use the form at the bottom of this page.

## Conversation index parsing

Conversation index parsing is a Relativity-defined handler that parses the Microsoft Exchange field Conversation Index to group all replies and forwards in an email conversation.

### Prerequisites

Prior to creating a new transform set for conversation index parsing, you need to create a new field to hold the data and a saved search from which to extract the data. Use the following sections to complete the prerequisites.

To create a new field, see Creating and editing fields .

#### Creating a field for conversation index parsing

When you create the field, make sure to configure the following fields correctly:

- Object Type —Document.

- Name —consider naming this field Conversation Family for ease of use; however, you can use whatever name you like.

- Field Type —Fixed-Length Text

- Length —50

- Relational —Yes

- Friendly Name —enter a recognizable friendly name like "Conversation Family" for the relational field.

- Import Behavior —leave blank values unchanged

- Pane icon —browse for and select an icon file for use in the Related Items pane of the Review Interface.

- Order —enter a display order value to specify the pane icon order at the bottom of the Related Items pane.

- Relational View —select the view you want to use in the Related Items pane, for example Family Documents.

See the Fields section for more details on relational field settings, including a link to download relational field icons provided by kCura for the Pane icon field.

#### Creating a saved search for conversation index parsing

To create a saved search, see Creating or editing a saved search .

This saved search should contain all documents that have the Conversation Index field populated.

### Creating a conversation index transform set

To create a conversation index transform set:

- Navigate to the Transform Sets tab.

- Click New Transform Set .

- Complete the fields on the form. See Fields .

- Click Save .

### Fields

The conversation index transform set contains the following fields:

- Name —the name of the Transform Set.

- Data Source —the saved search on which the transform will run. Select the newly created saved search.

- Handler —the handler on which the transform will run. Choose Conversation Index Parsing .

- Status —the status of the job after it has been run. The possible choices for this field include:

- Pending

- Processing

- Completed

- Completed with Errors

- Stopped by User

- Last Run Error —lists the last error encountered if the job was completed with errors.

### Adding a transform

To add a transform to the conversation index parsing transform set:

- Click New on the transform you just created.

The Add Transform window appears.

- Fill out the fields on the form. See Fields .

- Click Save .

### Fields

The Add Transform window contains the following fields:

- Transform Set —automatically populates with the transform set you just created.

- Name —the name of the transform you're adding.

- Source Field —the field that holds the data to be processed. Choose Conversation Index .

- Destination Field —the field that holds the results of the process. Choose the field you created above, Relational.

Non-email items in your database will not have a conversation ID. The transform process will not fill the destination field for these items.

### Running the transform set

After you create the conversation index transform set and add a transform to it, you can run the transform set. You run the transform by clicking Start Transform: Full in the console.

When the run finishes, you can view the results in the destination field you specified while creating the transform set by adding the field to a view.

On this page

- Transform sets

- Domain parsing

- Prerequisites

- Creating a domain parsing transform set

- Fields

- Adding a transform

- Fields

- Running the transform set

- Domain Parsing - SMTP, X400, X500

- Conversation index parsing

- Prerequisites

- Creating a conversation index transform set

- Fields

- Adding a transform

- Fields

- Running the transform set


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

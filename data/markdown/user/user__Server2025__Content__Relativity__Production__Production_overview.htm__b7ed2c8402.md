---
title: "Production"
url: https://help.relativity.com/Server2025/Content/Relativity/Production/Production_overview.htm
collection: user
fetched_at: 2026-06-22T06:02:52+00:00
sha256: 3a80d3651fab612bc2fc25459ccc134ac626b7db2540e2b5818b7b9dd5dea290
---

Production Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Production

With the Production application you can prepare relevant and non-privileged documents to turn over to opposing counsel after review. Relativity's production application makes it easy to customize your productions from placeholders to custom branding.

If you are upgrading to Server 2025 from a previous version of Relativity, consider the Production upgrade considerations in the Relativity Upgrade Guide before you begin your upgrade.

For more information about working with productions, see the following pages:

- Production queue

- Branding queue

- Importing a production file

- Exporting a production set

- Production sets

- Production console

- Production errors

- Re-productions

- Production data source

- Production Placeholders

Also see these related recipes:

- Locking produced documents from editing

- Displaying production fields in a layout

- Importing productions in Relativity as Natives

- Maintaining previous Bates numbers between production sets

- Using tokens to customize stamps in a production

For information about troubleshooting the production application through the Service Host Manager, see Service Host Manager in the system guides section.

## Security permissions to run a production

The following security permissions are required to run a production:

Object security Tab visibility Other settings

- Production – View, Edit, Add

- Production Data Source - View, Edit, Add, Delete

- Production Information - View, Edit, Add

- Production Placeholder - View, Edit, Add

- Production Sets

- Production Placeholder

- Production

Mass Operations

- Re-Produce

Admin Operations

- Override Production Restrictions

## Upgrading production

Production application upgrades occur concurrently with Relativity product updates. You can find information about production updates in the Relativity release notes and What's new.

To upgrade the application, use one of the following methods:

- Upgrade to the latest Relativity product update - Upgrading to the latest Relativity update automatically upgrades production to the latest version.

- Upgrade production only - Download the newly released RAP file from the Relativity Community and import it into the Application Library.

## Basic production workflow

In order to produce documents, ensure you use the following workflow to create the necessary production components. Use the links in the image below for more information on each part of the production workflow.

## Production information

The production information object stores important information about your production. Staging a production populates this object in your workspace. As an example, the production information object is useful when you want to look at the amount of documents with redactions, the control number of the documents in your production, which documents were produced with a placeholder, and which documents were produced as a native. The production information object also stores the automatically created Bates numbers associated with the production. Because the Bates numbers automatically populate on production documents, the Bates numbers fields automatically clear when you delete productions.

To quickly view the information stored on this object, click View Documents in the production console. The View Documents pop-up displays information on both documents and individual pages. You can also view information about the documents produced by looking at the saved search that is automatically created when the production job finishes.

Once you run a production, you can view the aforementioned information on the documents list for each produced document by adding the fields to a view and then creating a tab from that view. See Views and Tabs for more information.

### Production information tab

To view production information in greater detail you can create a production information tab and associate it with the production information object.

- Navigate to Tabs.

- Select New Tab .

- Enter Production Information as the name for the tab.

- Select Object as the tab type.

- Select Production Information as the object type.

- Configure the tab location.

- Click Save.

- Navigate to the Production Information tab to view information about your production set.

The following fields are stored on the production information object and can be viewed on the production information tab:

- Artifact id

- Begin attachment

- Begin bates

- Data source

- Document

- Document id

- Edit

- End attachment

- End bates

- Has redactions

- Identifier

- Image count

- Name

- Production type

- Production set

- Security

- Sort order

- System created by

- System created on

- System last modified by

- System last modified on

- With images

- With natives

- With pdf

- With placeholder

On this page

- Production

- Security permissions to run a production

- Upgrading production

- Basic production workflow

- Production information

- Production information tab


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

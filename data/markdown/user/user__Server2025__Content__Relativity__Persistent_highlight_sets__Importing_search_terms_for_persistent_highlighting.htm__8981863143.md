---
title: "Importing search terms for persistent highlighting"
url: https://help.relativity.com/Server2025/Content/Relativity/Persistent_highlight_sets/Importing_search_terms_for_persistent_highlighting.htm
collection: user
fetched_at: 2026-06-22T06:16:10+00:00
sha256: a67eaffe757d0b35911ebbd97f4b92eb00299c9470093b45398a7b73d8c47fc0
---

Importing search terms for persistent highlighting

# Importing search terms for persistent highlighting

To import search terms to use as a source for persistent highlighting perform the following procedures.

## Relativity component setup

Before importing search terms, use the following steps to create a Relativity Dynamic Object to handle the data.

- Navigate to the Object Type tab in your workspace.

- Click New Object Type .

- Provide a name for the new object in the required Name property.

- Keep all remaining properties at their default values.

- Click Save .

- Navigate to the Fields tab.

- Click New Field to create the field that to hold the persistent highlight color information. This field also connects your Dynamic Object to the Document object.

- In the New Field form, specify the following properties:

- Object Type - <Dynamic Object created in step 2>

- Name - Highlight Colors

- Field Type - Fixed-Length Text

- Length - 10

- Keep all remaining properties at their default values.

- Click Save and New .

- Create a new field to link your Dynamic Object and the Document object. Specify the following properties:

- Object Type - Document

- Name - <User preference>

- Field Type - Multiple Object

- Associative Object Type - <Dynamic Object created in step 2>

- Keep all remaining properties at their default values.

- Click Save .

- Navigate to the Persistent Highlight Sets tab in your workspace.

- Click New Persistent Highlight Set .

- Create a new set with the following properties:

- Name - <User preference>

- Order - <User preference>; this controls the position of this set in the Persistent Highlight Tree in the Viewer.

- Source - Highlight Fields

- Highlight Fields - <The name of the field created in step 6b.>

- Click Save .

## Importing terms

To import a CSV or other Relativity-supported load file containing terms, use the following procedure.

- Open the Relativity Desktop Client .

- Select the workspace you are importing into.

- Select the Dynamic Object you created above from the object drop-down menu.

- Select Tools from the top menu.

- Select Import | <Dynamic Object> load file.

- Select your terms load file and corresponding delimiters.

- Map the field in your load file that contains the terms to the Name field in Relativity.

Here you can also import Relativity Highlight Color. You must have this information in the load file contained in a field in the following format: highlight color; text color (for example, 15;9). If you do not have this information in the load file, you can manually enter it for terms in Relativity. Because the latter can be time consuming, we recommend having this information in the load file if possible.

Color name Highlight Color Number

[Default] 0

Black 1

Dark red 2

Dark green 3

Dark yellow 4

Dark blue 5

Dark magenta 6

Dark cyan 7

Light gray 8

Gray 9

Red 10

Green 11

Yellow 12

Blue 13

Magenta 14

Cyan 15

White 16

Light green 17

Light blue 18

Light yellow 19

Light purple 20

Light red 21

Light orange 22

Purple 23

Orange 24

Dark purple 25

Dark orange 26

- Click Import to import the terms.

- Navigate to the object tab you created in step two of the Relativity component setup section.

- Click on a term.

- Select the layout you want to use from the drop-down menu.

- Click the pencil icon to edit the layout.

- Click Add Object list .

- Use the drop-down menu to select the field you created in 6b of the Relativity component setup section.

- Set the View field to your preferred document view.

- Set the Link View field to your preferred document view.

- Click Save .

- Click Link .

- Select all documents.

- Click Add .

- Click Set .

- Repeat steps 10 through 22 on each term.

- Verify that the terms are highlight through the following:

- Open a document in the workspace.

- Open the Persistent Highlight Tree in the Viewer.

- Note the presence of the newly created Persistent Highlight Set and verify that terms are highlight in the appropriate colors.

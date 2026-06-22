---
title: "Populate parent ID to child"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Populate_parent_ID_to_child.htm
collection: user
fetched_at: 2026-06-22T06:09:45+00:00
sha256: 0d74fc2e126db1e6a5cc0a25a86cb85e19571664bca1e70bd4e6cd8fac6baf71
---

Populate parent ID to child

# Populate parent ID to child

Populate parent ID to child is a workspace-level script that propagates the Document ID of the parent document to any children of that document. The child document has a field which points to its parent.

Populate parent ID to child is a separate solution from Populate Parent ID and Child ID, which is a workspace-level script that populates a production Parent ID and Child ID on a document for a production set. See Populate Parent ID and Child ID for more details about that solution.

## Special considerations

When running email threading (under the Structured analytics set tab ), attachments aren't threaded with their parent emails if the Parent Document ID field is blank for the attachment, or if it's mapped to a field that doesn't use a supported format. If your document set includes attachments with unpopulated Parent Document ID fields, run the Populate parent ID to child script before running email threading. For information on supported formats, see See Analytics profiles .

The populate parent to child script propagates the Document ID (e.g. Control Number) of the parent document to any children of that document. The parent document is determined by the record with the lowest ArtifactID in the group.

Document ID refers to whichever document field has is identifier set. The most common example is the Control Number field, or the Document ID field.

### Recommended prep work

Before running the script, create a Yes/No field called “Emails and attachments to be updated”. This field should be set to Yes for all documents you want the script to analyze. This is typically parent emails and their attachments. Mass edit all such documents and assign the Emails and attachments to be updated field to Yes. Next, if you don't already have one, create a fixed-length text field that's the same length as your Document ID field and name it "Parent Doc ID." See Layouts for more information on creating a layout and tagging documents.

## Inputs

This script requires the following inputs:

Input Description

Group Identifier field Relational field which is the family group identifier used to group emails with their attachments.

Document to be updated flag Yes/No field that Identifies which records to update (e.g. Emails and attachments to be updated). Tag all documents with a Yes value (both parent emails and attachments) before running the script. After script execution, child records with a Yes value in this field will be updated with the Parent Document ID, provided the parent is also tagged with "Document to be updated=Yes". Parents are left unchanged as they don't have parent documents.

Parent ID source Set this to the Document ID field in the workspace; the document field flagged as Is Identifier , typically Control Number, or DocID in the workspace.

Parent ID destination The text field that the script writes parent information to. After running the script, this fixed-length text field will be populated with the Document ID of the parent email for all child documents. For the parent email, this field will remain empty.

## Running the script

After you've tagged the documents to be updated (see Recommended prep work ), perform the following steps to run the populate parent to child script.

- In a workspace, point to the Administration tab, and then click Scripts .

- Click New Relativity Script .

- From the Script Type section, select the Select from Script Library . A new Scripts field displays.

- Click to the right of the new Scripts field.

- Select the Populate Parent ID to Child script from the list of scripts.

- Click OK , and then click Save . On the Script Console, click Run . The Script Inputs dialog appears.

- Select the appropriate script inputs. See Prep work and inputs.

- Click Run . When the script completes running, the results display in the Results pane. The Parent ID destination field displays the Parent Document ID propagated to all child documents. This field is blank for the parent document of each group.

You can't select Artifact ID or Parent ID source as the Parent ID destination because you can’t propagate to a Parent ID source field. If the field specified in the Parent ID source input has a value of NULL, the script won't output any results.

If the document with the lowest ArtifactID is not consistently the parent, you can't use this script on the data set. Also note that leaving the Parent Document ID field blank on the Analytics Profile when running Email Threading will prevent the attachments from being threaded. See Analytics profiles .

You can now run the email threading operation and populate the Parent ID field. See Running structured analytics .

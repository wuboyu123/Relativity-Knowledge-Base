---
title: "Reviewer access"
url: https://help.relativity.com/Server2025/Content/Relativity/Active_Learning/Reviewer_Access.htm
collection: user
fetched_at: 2026-06-22T06:02:49+00:00
sha256: 0b9c47f63ce53bc84829e9f27eae605bb623e73f4f4f69bfc27aeb20f7374458
---

Reviewer access Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Reviewer access

After a project admin creates and saves a new Active Learning project, Relativity creates a new document list view that's tied to the Active Learning project. This view is automatically secured to the reviewers added to the project. As an Active Learning reviewer, this view is the only place you can enter the review queue.

Before assigning a document to a reviewer, Relativity ensures the following conditions are met:

- The current reviewer has permission to the document.

- The document has not been coded already.

- The document is not assigned to any other active reviewer.

Documents can only be assigned to one reviewer except in cases where the reviewer leaves the viewer without making a coding decision or is automatically logged out. When this happens, the queue can reassign the document to another reviewer. Once a document has been coded by a reviewer, the Project Reviewers::User field will show that reviewer's name.

Reviewers code documents on the review field specified for the project and then click Save and Next to get a new document. They can also code other fields not associated with the project.

## Project admin considerations

We recommend waiting until non-business hours to update security permissions for document folders containing a large number of documents. Doing the update during business hours could lead to your workspace not loading and a delay in your document review project.

- If you don't want reviewers to skip documents, make the project review field a required field.

- We recommend turning off family propagation with Active Learning.

- Make sure all reviewers assigned to the project are enabled users in the Relativity environment. For more information, see Creating and editing a user .

- You can grant permissions to specific users or groups for certain icons in the Viewer. Any permissions changes will affect how those groups see the Viewer for both Active Learning and non-Active Learning projects.

- Reviewers can change the coding decision on documents they previously reviewed. These documents aren't considered manually-selected documents. The next model build will include the most recent coding update.

## Accessing the Active Learning review queue

To enter the Active Learning review queue, navigate to the Documents tab and ensure you are on the view named after the Active Learning project. This document view returns a list of all documents previously reviewed by you in the queue. When you first access the view, no documents appear because none have been coded. As you code documents from the Active Learning queue, documents appear in the list.

The project document view enables or disables reviewer access based on whether you are added to the queue and whether the queue is active.

If you are added to the queue and the queue is enabled, a blue banner appears in the project document view with a Start Review button. Clicking Start Review begins the review process.

If the Start Review button is not appearing as expected, have the project admin try these troubleshooting steps:

- Ensure reviewers are added to the group associated with the Active Learning project.

- Ensure the reviewers have the proper security permissions. For more information, see Reviewer permissions .

- Ensure the saved search associated with the Active Learning project contains documents with extracted text.

- Ensure the classification index associated with the Active Learning project is active.

- On the Project Home tab, ensure the Start Review button is selected.

- When previewing permissions, ensure that you are previewing user permissions, not group permissions. The Start Review button does not appear in permissions group previews.

- Ensure the following agents are installed and running:

- Active Learning Manager

- Active Learning Worker

- Analytics Categorization Manager

- In SQL, ensure there aren't orphaned jobs in the EDDS.ActiveLearningProjects table that don't correspond with an existing project. In other words, you look for projects that were deleted on the front end but still exist in the EDDS.ActiveLearningProjects table.

- Check the EDDS.AnalyticsCategorizationSetQueue table and look for any 'ERROR' jobs.

- Ensure rows exist (records) in the EDDSDBO.DRQ_<long guid> table in the workspace database. If there are no records here that means documents are not being properly submitted to the Active Learning Review Queue.

-

Ensure the language is English on the agent server where the Active Learning agents reside.

If the queue is disabled or you're removed from the queue while reviewing documents, a warning message will appear in the viewer.

If you aren't added to the queue or if the queue is paused, you can't access the Active Learning queue from the project document view. You can still access the view itself but only for reviewing previously coded documents. You may still code documents outside the queue if you have permissions to do so.

## Review workflow

Click Start Review to access the Active Learning queue viewer and start reviewing documents. The Viewer looks the same no matter which type of queue is active, contains the same functionality available for a standard queue, and relies on the same permissions.

Code documents on the review field specified for the project and then click Save and Next to get a new document. You can also code other fields not associated with the project as determined by your project admin.

Reviewers must code documents based on the so-called "four corners" rule. This means that a document should be judged relevant or not relevant based solely on the extracted text of that document only. Documents that are relevant based on family members should not be coded relevant on the Active Learning review field. Although individual anomalies will not hurt the algorithm, too many in aggregate could cause the model to perform worse. For more information on reviewer protocol and best practices, see Best practices for Active Learning review .

### Skipping documents

You can skip documents without making a coding decision unless the review field is a required field. You can also click to skip the current document and open a new document. In the upper right of the Viewer, you can see a running count of all documents coded in the project, including skipped documents. Skipped documents are also reflected in the Project Home dashboard.

Reviewers can change the coding decision on documents they previously reviewed. These documents aren't considered manually-selected documents. The next model build will include the most recent coding update.

On this page

- Reviewer access

- Project admin considerations

- Accessing the Active Learning review queue

- Review workflow

- Skipping documents


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

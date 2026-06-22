---
title: "Creating a communication"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Creating_communications.htm
collection: user
fetched_at: 2026-06-22T06:13:08+00:00
sha256: 5704e126b844390c748f7b971e00ce23de834c6820a90a79a706d3c2b6590680
---

Creating a communication

# Creating a communication

You can use communications or notices to send hold notices, questionnaires, follow-up communications, or anything else you need to send to a custodian or group of specified custodians regarding their involvement in the project or hold. Create a custom communications using the rich text editor and email merge fields. For more information, see Email merge fields .

To create a communication:

- From the Projects tab > Project console > Manage Project, click Create Communication .

The Create New Communication dialog appears.

-

Select one of the following options:

- Communication Type - select a communication type. Default communications types include General Hold Notice, Release Notice, Email Acknowledgement, and Alert Group. For more information, see Communication detail layout fields .

- Create From:

- Template - create a new communication using an existing template. Legal Hold only displays templates with the same type as the selected Communication Type. When creating a communication from a template, the following items carry over with the following pre-populated field information.

- Name

- Type

- Description

- Acknowledgment Required

- Attachments

- Questionnaire

- Portal Content

- Email Send As

- Email Subject

- Email Body

- Automatic Reminders

- Email Reminder Subject

- Email Reminder Body

- Automatic Escalations

- Email Escalation Body

- BCC Email Subject

Legal Hold respects secured template items, so not all template items may carry over, depending on the item-level permissions.

- Blank Communication - create a new communication from scratch.

- Click Create .

- Complete the fields on the New Communication layout. See Communication detail layout fields .

- Click Save . The Communication details appears. See Communication details .

- (Optional) From the communication details, click Edit to update more communication detail fields. See Communication detail layout fields .

- Click Save . The new communication appears in the Project Details Communication tab.

## Communication detail layout fields

The Create communication layout contains the following fields:

Detail tab

- Name - the communication name.

- Type - the communication type. Click Add to add a new type. Legal Hold ships with several generic communication types.

- Send To for Approval - the admin that communications need to be approved by before they are sent to custodians. This only appears if you do not have approval permissions. For more information, see Securing a project .

- Response Due Date - the communication response deadline. This value potentially updates the Past Due Communication value on the Custodians sub tab of the Project layout.

Exceeding the Response Due Date on a communication doesn't trigger an alert such as a legal hold communication or email.

- Description - (Optional) a communication description.

- Save As Template - select checkbox to make this communication available as a template.

- Project - the project to which the communication is associated.

Email tab

- Send As Alias - the specified email address you want the communication to be sent from. This feature allows you to send a communication on someone else's behalf. For example, a junior attorney may send the email, but may want the email to appear as coming from the general counsel. If no email address is entered, the email address set From Email Address field of the Legal Hold Settings. For more information, see Adding Outgoing Email settings .

To use this feature, you must use SMTP. This feature is not available when using Microsoft Graph API to send messages.

- Subject - the subject that appears in the email.

- Body - the email body that appears in the communication. The [PortalLink] merge field is required if any of the following conditions are met:

- Acknowledgement required is set to Yes .

- There is any text in the Portal Detail.

- There is a questionnaire included.

- There is a linked attachment included.

See Using the editor window and Email merge fields .

Portal Content tab

- Acknowledgement Required - select Yes to require an acknowledgement and be able to schedule reminders and escalations for a questionnaire attached to a communication.

When creating a General Hold notice and the Acknowledgement Required is set to No , and also doesn't have an attached questionnaire, no portal link needs to be present in the communication body.

- Is Legal Hold - Select Yes or No to visually indicate whether the communication is a Legal Hold from the Custodian portal. If this field is set to Yes, the Global Reminder is enabled.

- Attachments - click to attach an existing file from the Attachment Library. See Attachments library .

- Questionnaire - click to select an existing questionnaire from the Questionnaire Library. See Question types . Click Add to create a new questionnaire. See To create a questionnaire: .

When creating a General Hold notice no questionnaire is selected, and the Acknowledgement Required field is set to No , no portal link needs to be present in the communication body.

- Use Email Body for Portal Detail - select Yes or No to copy the email body to used as the portal content. If set to Yes, the HTML editor is removed and the content in the email body is duplicated as the portal content. If set to No, the HTML editor is available and the content in the editor is used in the custodian portal.

- Portal Detail - portal content for this communication. See Using the editor window .

Reminder & Escalation tab

- Reminder

- Automatic Reminders - select Yes for Legal Hold to send automatic reminder emails to custodians that haven't yet acknowledged the communication or completed the associated questionnaire. Select No to disable automatic reminders to the custodians who haven't completed the required acknowledgement or questionnaire.

- Allotted Reminders - the number of reminders allowed for this communication until the reminders expire and, if selected, escalations begin to be sent.

- Reminder Interval (in days) - the number of days between each reminder. For example, if you enter 7, reminders are sent weekly.

The interval clock starts counting down from the time the communication was sent or from the last sent reminder time.

- Reminder Subject - the email subject that appears in the reminder email.

- Reminder Body - the email message that appears in the reminder email. See Using the editor window .

- Escalation

- Automatic Escalations - select Yes to indicate whether Legal Hold should send an escalated communication, typically to a custodian’s manager, often after automatic reminders have expired. Legal Hold sends the escalation email one iteration after the scheduled reminder or reminders ends. For example, if an automatic reminder is configured to send a total of two reminders every five days, the first automatic escalation would get sent on the 15th day, five days after the last automatic reminder was sent to the assigned custodian, or custodians. Select No to disable automatic escalations.

- Allotted Escalations - the number of escalations allowed for this communication.

- Escalation Interval (days) - the number of days between each escalation. For example, if you enter 7, reminders are sent weekly.

The interval clock starts counting down from the time the communication was sent or from the last sent escalation time.

- Escalation Recipient - select the recipient of the escalations, and by default, sends an escalation to the entity's designated manager. You can also select a manager, project owner, or other entity. Click Manage to add, update, or remove recipients. If no recipient is entered, the escalation is sent to project owner.

- Other Entity Recipient - select an existing entity within the workspace to receive escalations. For example, if you want someone to receive all escalations, confirm they are an entity within the workspace and select them as the escalation recipient.

Click Add to create a new custodian to send the escalation to.

- CC Recipients - sends an escalation to entities that need to be included in addition to the escalation recipient that was previously selected. Click the ellipsis button next to CC Recipients to send the escalation to multiple recipients.

- Escalation Subject - the email subject that appears in the escalation emails.

- Escalation Body - the message that appears in the email. See Using the editor window .

The merge field on the escalation should be the custodian name, not the manager name.

Summary BCC tab

The BCC tab allows you to send a customized email to any custodian or group in Legal Hold. The email includes the text you specify, a line break, the original communication that's sent to other people through non-BCC, and an attachment listing all the people the original communication was sent to.

The Legal Hold BCC feature isn't a "true" BCC to all of the original emails, but rather a unique email that goes out once with the associated set of hold notices and consolidates the details from many emails into a single email.

- BCC Recipients - the custodian that you want to send the BCC email to. See Creating legal hold entities .

- BCC Subject - the subject that appears in the email.

- BCC Body - the message that appears in the email. See Using the editor window .

People you send BCC emails to aren't included in Legal Hold reports.

## Communication types

Relativity Legal Hold projects include multiple communications that are sent through Relativity to custodians. These communications range from a general legal hold notice to a release notice. These communications have different purposes such as notifying a custodian about being added to a legal hold, answering questions regarding the hold, and being released from the hold. The recipients of the communications can be legal hold custodians, data stewards, executives, or legal team members.

Communications can be scheduled for automatic reminders and escalations, particularly when a custodian isn't responsive, you would schedule the automation from the communication details. For more information, see Legal hold reminders .

### General notice

The general notice is sent to active custodians in the project and describes the background, claims, and the position of the entity involved in the legal matter. It also includes a secure link to the custodian portal.

In the portal, custodians can acknowledge their participation in a hold, answer questionnaires, view all active projects they're associated with, and easily address any other outstanding tasks. For more information, see Custodian portal.

Relativity includes different templates to choose from when creating this communication. You can include merge fields and instructions tailored to your organizations.

When using a General Hold Notice communication, the [PORTALLINK] merge field is no longer required when the Acknowledgment Required field is No and there is no questionnaire.

### Alert group

The alert group notice is sent to a pre-identified group of employees within an organization to notify that they are potentially involved in a legal hold. The alert groups may include human resources, legal, and IT or any group of individuals impacted by the custodian’s response to the question.

Their involvement, and the release of the alert communication, is based on custodians’ questionnaire responses. For example, if a response involves another individual or group in the alert group, the alert notice is sent. This communication is a custodian notification that includes a mention of future communications. For more information, see Sending questionnaires .

### Email acknowledgement

The email acknowledgement lets a custodian acknowledge participation in the legal hold without having to visit the Custodian Portal. The acknowledgement via email includes an in-depth description of the legal hold and a link for the custodian to click to acknowledge that the legal hold has been received.

The response to the acknowledgement email is sent to the email address listed in the Reply to Email Address field in the email settings. For more information, see Adding email settings .

### Release notice

The release notice is sent to a custodian when they are no longer needed in the legal hold. This is the final communication to a custodian and no further communications are sent from that legal hold project. The release notice states that the matter does not include any other pending legal holds that apply to the custodian, including any separate legal holds that may relate in any way to the same subject matter.

## Using the editor window

Use the rich text editor window to compose portal content, emails, reminders and escalations, and BCC emails. The rich text editor provides support for hyperlinks, images, and tables, and is optimized for copying and pasting from Microsoft Word to customize your communications to custodians. You can customize text with the editor icons and utilize email merge fields to insert field values in Legal Hold. See Using the rich text editor .

When adding embedded links in the text editor, you must prefix the links with http or https, otherwise the text editor treats the link as relative to the current page. For example, but "http://google.com" is a valid, absolute link and will render correctly as a rich text field.

### Email merge fields

You can use email merge fields in the editor window to embed in a communication's subject line and body text, which translates into the corresponding Legal Hold field value upon sending. For example, if you type the merge field, [Communication.Name], using brackets, Legal Hold will translate that merge field to whatever value is in the Communication Name field in the Communication details tab.

One useful example for using merge fields is the Project.SubjectMatterStartDate. You can save this information in a project template so that you don't have to customize this information each time you create a project.

You can use email merge fields from the drop-down list in the editor window above the text to embed in a communication's subject line and body text, which translates into the corresponding Legal Hold field value upon sending. For example, the merge field Communication. Name would translate to the value in the Communication Name field in the Communication details tab.

Each communication has its own list of merge fields. The merge fields in one communication can't be used in different types of communications. For example, adding a merge field from the Alert Notice communication list may not work in the Acknowledgement communication. Only use what's available in the Merge Fields drop-down menu.

Email merge fields are case insensitive, so if typing the keyword, you can enter the same merge field in different ways:

- [Custodian.FirstName]

- [custodian.firstname]

- [CUSTODIAN.FIRSTNAME]

If you use a merge field that doesn't contain any content in the field value, the merged field displays as the merge field name in the communication. For example, the merge field displays in the communication as "Custodian.FirstName" instead of "Jane".

The [ID] merge field is not supported. Also note that the [PHONE] merge field is now [PHONENUMBER] and the [CURRENTTITLE] merge field is now [JOBTITLE]. If you were using any of these merge fields in communications prior to upgrading, be sure to manually update or remove them.

### Email merge fields list

View merge fields

#### Communication

Communication email merge fields return information relevant to the communication for that particular project.

Merge field Object Field UI location

[Communication.AcknowledgementReminderInterval] Communication Reminder Interval (in days) Reminder & Escalation tab

[Communication.Name] Communication Name Detail tab

[Communication.ReminderLastSentDate] (Calculated) - -

#### Custodian

Custodian email merge fields return information relevant to the entity assigned to the project communication.

Merge field Object Field UI location

[Custodian.Address1] Entity Address 1 Entity details > Location tab

[Custodian.Address2] Entity Address 2 Entity details > Location tab

[Custodian.ActiveProjects] Entity - (Calculated)

[Custodian.AllProjects] The Custodian.Projects merge field returns all projects that the Custodian is linked: Open, Closed, and other projects from which they have been released. Entity - (Calculated)

[Custodian.City] Entity City Entity details > Location tab

[Custodian.Company] Entity Company Entity details > Company tab

[Custodian.Country] Entity Country Entity details > Location tab

[Custodian.CurrentTitle] Entity Current Title Entity details > Company tab

[Custodian.Department] Entity Department Entity details > Company tab

[Custodian.Email] Entity Email Entity details > Basic Contact

[Custodian.EmploymentEndDate] Entity Employment End Date Entity details > Company tab

[Custodian.EmployeeNumber] Entity Employee Number Entity details > Company tab

[Custodian.EmploymentStartDate] Entity Employment Start Date Entity details > Company tab

[Custodian.EmploymentStatus] Entity Employment Status Entity details > Company tab

[Custodian.FirstName] Entity First Name Entity details > Basic Contact

[Custodian.LastName] Entity Last Name Entity details > Basic Contact

[Custodian.LegalHoldCommunicationLastAcknowledgeDate] Entity - (Calculated)

[Custodian.LegalHoldCommunicationLastSentDate] Entity - (Calculated)

[Custodian.LegalHoldCommunicationLastViewedDate] Entity - (Calculated)

[Custodian.LegalHoldReminderLastSentDate] Entity - (Calculated)

[Custodian.LeaveDate] Entity Employment End Date Entity details > Company tab

[Custodian.Location] Entity Location Entity details > Location tab

[Custodian.MiddleName] Entity Middle Name Entity details > Basic Contact

[Custodian.Notes] Entity Notes Entity details > Other tab

[Custodian.Phone] Entity Phone Number Entity details > Company tab

[Custodian.QuestionnaireLastCompletedDate] Entity - (Calculated)

[Custodian.SecondaryEmail] Entity Secondary Email Entity details > Other tab

[Custodian.StartDate] Entity Start Date Entity details > Company tab

[Custodian.State/Province] Entity State/Province Entity details > Location tab

[Custodian.UnacknowledgedReminderCount] Entity - (Calculated)

[Custodian.UnacknowledgedReminderLastSentDate] Entity - (Calculated)

[Custodian.UniqueId] Entity Unique ID Entity details > Other tab

[Custodian.Username] Entity Username Entity details > Company tab

[Custodian.Zip/PostalCode] Entity Zip/Postal Code Entity details > Location tab

#### Acknowledge Email

Acknowledgement email merge field provides the recipient with a link to acknowledge the hold within the email itself, removing further navigation. After the custodian clicks the link, there will be a page confirming the acknowledgement.

Merge field Object Field UI Location

[AcknowledgeLink] (Calculated) Hold Admin > Legal Hold Settings tab > Custodian Portal

#### Manager

Manager email merge fields return information relevant to the custodian's manager.

Merge field Object Field UI Location

[Manager.Address1] Custodian Address 1 Entity details > Location tab

[Manager.Address2] Custodian Address 2 Entity details > Location tab

[Manager.City] Custodian City Entity details > Location tab

[Manager.Company Custodian Company Entity details > Company tab

[Manager.Country] Custodian Country Entity details > Location tab

[Manager.Department] Custodian Department Entity details > Company tab

[Manager.Email] Custodian Email Entity details > Basic Contact

[Manager.EmploymentEndDate] Custodian Leave Date Entity details> Company tab

[Manager.EmployeeNumber] Custodian Employee Number Entity details > Company tab

[Manager.EmploymentStartDate Custodian Start Date Entity details > Company tab

[Manager.EmploymentStatus] Custodian Employment Status Entity details > Company tab

[Manager.FirstName] Custodian First Name Entity details > Basic Contact

[Manager.LastName] Custodian Last Name Entity details > Basic Contact

[Manager.Location] Custodian Location Entity details > Location tab

[Manager.MiddleName] Custodian Middle Name Entity details > Contact tab

[Manager.Notes] Custodian Notes Entity details > Other tab

[Manager.Phone] Custodian Phone Number Entity details > Basic Contact

[Manager.SecondaryEmail] Custodian Secondary Email Entity details > Basic Contact

[Manager.StartDate] Custodian Start Date Entity details > Company tab

[Manager.State/Province] Custodian State/Province Entity details > Location tab

[Manager.UniqueId] Custodian Unique ID Entity details > Other tab

[Manager.UserName] Custodian Username Entity details > Company tab

[Manager.Zip/PostalCode] Custodian Zip/Postal Code Entity details > Company tab

#### Portal

Merge field Object Field UI Location

[PortalLink] (Calculated) Portal URL Hold Admin > Legal Hold Settings tab > Custodian Portal

[PortalHomeLink] (Calculated) Portal Home URL PORTALHOMELINK is not available in the drop-down menu on general hold notices, but can be used. It's available on communication types, such as email acknowledgements, and when sending a custodian a portal link directly via the Entity > Send Portal Link button.

#### Project

Project email merge fields return information relevant to the project or hold.

Merge field Object Field UI Location

[Project.Case] Project Case -

[Project.CloseDate] Project Close Date (Calculated)

[Project.Company] Project Company (Calculated)

[Project.Custodians] Project All of the people on a specific project. (Calculated)

[Project.Description] Project Description Project Details

[Project.ExternalCounsel] Project External Counsel Project Details

[Project.Id] Project Artifact ID (Calculated)

[Project.GeneralCounsel] Project General Counsel Project Details

[Project.Name] Project Name Project Details

[Project.OwnerEmail] Project Owner Email Project Details

[Project.OwnerName] Project Owner Name Project Details

[Project.ScopeRationale] Project Scope Rationale (Calculated)

[Project.StartDate] Project Start Date (Calculated)

[Project.Status] Project Hold Status (Calculated)

[Project.SubjectMatterEndDate] Project Subject Matter End Date Project Details

[Project.SubjectMatterStartDate] Project Subject Matter Start Date Project Details

#### Respondent

Respondent email merge fields return information relevant to the custodian filling out the information. This is useful for alert communications. For example, if you send a system admin a communication informing them to collect from a certain person who filled out a questionnaire in a certain way, you can use these merge fields to have Legal Hold automatically list who that was.

Merge field Object Field UI Location

[Respondent.Answers] Custodian (Calculated) (Calculated)

[Respondent.CurrentTitle] Custodian Current Title Entity details > Company tab

[Respondent.Department] Custodian Department Entity details > Company tab

[Respondent.Email] Custodian Email Entity details > Company tab

[Respondent.EmployeeNumber] Custodian Employee Number Entity details > Company tab

[Respondent.EmploymentEndDate] Custodian Employment Leave Date Entity details > Company tab

[Respondent.EmploymentStartDate] Custodian Employment Start Date Entity details > Company tab

[Respondent.EmploymentStatus] Custodian Employement Status Entity details > Company tab

[Respondent.FirstName] Custodian First Name Entity details > Basic Contact

[Respondent.Id] Custodian ArtifactID

[Respondent.LastName] Custodian Last Name Entity details > Basic Contact

[Respondent.LegalHoldCommunicationLastAcknowledgeDate] Custodian (Calculated) (Calculated)

[Respondent.LegalHoldCommunicationLastSentDate] Custodian (Calculated) (Calculated)

[Respondent.LegalHoldCommunicationLastViewedDate] Custodian (Calculated) (Calculated)

[Respondent.LegalHoldReminderLastSentDate] Custodian (Calculated) (Calculated)

[Respondent.PastManager] Custodian Past Manager

[Respondent.Phone] Custodian Phone Number Entity details > Basic Contact

[Respondent.Projects] Custodian (Calculated) (Calculated)

[Respondent.Question] Custodian (Calculated) (Calculated)

[Respondent.Questionnaire] Custodian (Calculated) (Calculated)

[Respondent.QuestionnaireLastCompletedDate] Custodian (Calculated) (Calculated)

[Respondent.SecondaryEmail] Custodian Secondary Email Entity details > Basic Contact

[Respondent.UnacknowledgedReminderCount] Custodian (Calculated) (Calculated)

[Respondent.UnacknowledgedReminderLastSentDate] Custodian (Calculated) (Calculated)

#### Questionnaire

Merge field Object Field UI Location

[Questionnaire.Name] Questionnaire Name Library tab > Questionnaire > Name

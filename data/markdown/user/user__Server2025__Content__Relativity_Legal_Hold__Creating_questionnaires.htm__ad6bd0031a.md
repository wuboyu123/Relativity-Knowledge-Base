---
title: "Creating a questionnaire"
url: https://help.relativity.com/Server2025/Content/Relativity_Legal_Hold/Creating_questionnaires.htm
collection: user
fetched_at: 2026-06-22T06:13:09+00:00
sha256: 00f2a57d938dd571a28f738e509ac26cc528e3cb21ade13dcbd115e62c0522e4
---

Creating a questionnaire Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Creating a questionnaire

Use questionnaires to collect any information needed for the project. For example, an initial legal hold questionnaire might ask what kinds of hardware an individual uses at work, whether they work from home, how long they've been employed at the company, etc. These kinds of questions assist the general counsel in managing a custodian's involvement in the project or compliance.

To create a questionnaire:

- Navigate to the Questionnaires tab.

- Click New Questionnaire .

- Complete the question fields. For more information, see Questionnaire fields .

-

Click Save . Relativity Legal Hold adds the question to your questionnaire.

- If adding questions from the Question library, click Cancel , then click Import Questions .

- Select the questions you want to add, click Assign , then Save . Legal Hold adds the imported questions to your questionnaire.

- (Optional) You can add conditional logic to questions. Add conditions to Legal Hold to supply another question or send another communication only if the user responds to that question in a particular manner that you specify. See Adding conditions .

- (Optional) Re-order questions by clicking on each question and dragging the question up or down to the desired order.

- When finished, click Done . See Sending a questionnaire .

Edit the questionnaire name by clicking next to the questionnaire Name in edit mode.

## Questionnaire fields

Complete these fields when creating a new questionnaire.

- Question —enter the question in the Question field.

- Type —select a Question Type from the Type drop-down menu. See Question types .

- Answer Required —select Yes to make this a required question. Select No to not make the question required.

- Save Question to Library? —select Yes to include the new question in the Question Library. Select No to not add the new question to the Question Library.

- Question Library —if you include the question in the library, select a Question Category from the drop-down list. See Question categories .

## Adding conditions

Add conditions to questions to supply another question or send another communication only if the user responds to that question in a particular manner that you specify. You can add conditions to every question type except Text.

To add conditional logic to a question:

- From the question toolbar, click .

- In the new conditions window, complete the following:

- Conditions will be active when

- Depending on the question type, perform the following to set the condition to active. See Question types .

- Date - select the Start and End dates.

- Multi Choice

- From the drop-down menu select Contains or Is .

- Contains - select this to set conditional logic only if the answer contains any of the answers you indicate.

- Is - select this to set conditional logic only if the answer is exactly the answer(s) you indicate.

- Select the appropriate answer(s), depending on whether you selected Contains or Is .

- Single Choice - select one answer.

- Yes/No - select Yes or No.

- When Activated

- Upon setting conditional logic, select one or all of the following actions:

- Send Follow Up - sends any communication in Legal Hold that you can select using the item picker.

- Send Alert - sends an alert communication from the Alert Group that you can select using the item picker to a specific individual.

- Display Question - create a new question or import a question from the library. See To create a questionnaire: .

- Click Save . The conditional question appears as an alphabetic letter underneath the question you added the condition to. Here you can view the specific condition details.

You can add multiple conditions to questions.

- When finished, click Done .

## Question types

The Question Type drop-down list contains the following types:

- Date - provides a date picker for the user to select from.

- Multi Choice - user can select multiple answers. Enter each answer on a new line in the provided text box.

- Single Choice - limits the user to select only one answer from potential multiple answers. Enter each answer on a new line.

- Text - provides a free form text box for the user to enter a response.

- Yes/No - provides a yes or no option for the user to select from.

## Question categories

Use Question categories to organize your questions and easily sort through questions in the Library. See Question types .

The Question Category drop-down list contains the following categories:

- Class Action

- Employment Matter

- Intellectual Property

- Legal Hold

- Other

- Regulatory/Compliance

- Backup Tapes

- Databases

- Electronic Mail

- File Servers

- General Information

- Legacy Systems

- Workstations, PCs, Laptops

- Other Media

You can add a new Question category by clicking Add next to the Question Category drop-down list in the Questionnaire builder.

### Creating a questionnaire

Create a questionnaire to send to custodians. To add a questionnaire, navigate to the Questionnaire tab and click New Questionnaire . In the questionnaire, you can add any number of questions.

To add a new question to a questionnaire,

- Click New Question .

- Enter question into text box.

- Select the type of question.

- Date - a response that requires a valid date format. Attempting to load an invalid date produces an error.

- Multi Choice - a response that requires a selection of one or more values in a set of predetermined values.

- Single Choice - a response that requires selecting one value out of a set of predetermined values.

- Text - a question response that requires a long or fixed length text response.

You can't add a condition to a Text question type.

- Yes/No - a response that requires a selection of Yes or No.

- Set answer requirement.

- Set saving to library option.

- Click Save .

After clicking save, you're brought back to the questionnaire. Next to the new question, you'll see three icons. You'll only see two icons if you selected Text as the question type. For more information, see Adding conditions . Click to edit the question. Click to delete the question. Click to add a condition the question.

#### Adding a condition

Click to add a condition to a question. The question must be a date, multiple choice, single choice, or yes/no question type. Text responses do not activate a condition.

##### Activating a condition

When a condition is activated, optional next steps can take place. These steps include sending a follow-up communication to the responder, sending a notice to an alert group, and adding a follow-up question.

###### Sending a follow-up communication

Select Yes to send a follow-up communication to the responding custodian. When Yes is selected, a Choose Communication button is available. Click the button to open a pop-up modal to select a communication. Click a radio button next to the communication you want and click Save .

###### Sending an alert notice

Send an alert notice to a previously created alert group. For more information, see Alert group .

- Select Yes to send a notice to an alert group. When Yes is selected, a Choose Communication and Choose Custodian button are available.

- Click Choose Communication to open a pop-up modal. Click the radio button next to the alert notice you'd like to send.

- Click Save .

- Click Choose Custodian to open a pop-up picker.

- Click the check boxes by the custodian or custodians that you would like to notify.

- Click Select .

- Click Save .

###### Sending a follow-up question

Select Yes to add a follow-up question to the original question. Add, or import a question, to follow up after the custodian's condition activating response.

On this page

- Creating a questionnaire

- Questionnaire fields

- Adding conditions

- Question types

- Question categories

- Creating a questionnaire


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

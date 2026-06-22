---
title: "Inclusive emails"
url: https://help.relativity.com/Server2025/Content/Relativity/Analytics/Inclusive_emails.htm
collection: user
fetched_at: 2026-06-22T06:05:01+00:00
sha256: f6fe23383cbf3dd101db9edb8827eff28567706e223890c380530e3ff226715f
---

Inclusive emails

# Inclusive emails

There are two types of email messages in Structured Analytics:

- Inclusive - an email that contains unique content not included in any other email, and thus, must be reviewed. An email with no replies or forwards is by definition inclusive. The last email in a thread is also by definition inclusive.

- Non-inclusive - an email whose text and attachments are fully contained in other (inclusive) emails.

By reviewing only inclusive emails and skipping duplicates, your review process will be much more efficient. The Analytics engine derives the email threads and determines which subset of each conversation constitutes the minimal inclusive set. Non-inclusive emails are redundant because all non-inclusive content is also contained in inclusive emails. The inclusiveness analysis ensures that even small changes in content will not be missed by reviewers.

## Common inclusive emails

- The last email in a thread - the last email in a particular thread is marked inclusive, because any text added in this last email (even just a "forwarded" indication) will be unique to this email and this one alone. If nobody used attachments, and nobody ever changed the subject line, or went "below the line" to change text, this would be the only type of inclusiveness.

- The end of attachments - when an email has attachments, and the recipient replies, the attachments are often dropped. For this reason, the end of the thread will not contain all of the text and attachments of the email. Structured Analytics will flag one of the emails containing the attachments as inclusive.

- Change of text - it's not completely unheard of for an unethical employee to try to cover their behavior by modifying an original email during a reply. So if Person A tells Person B, "You may not use company funds to buy yourself a new hat", Person B might remove the word "not" and forward the email to Finance, claiming that he had prior permission from Person A to expense his new sombrero. In this case, the Analytics engine would recognize that the email from Person A to Person B contained different text than that from Person B to Finance, and flag both emails as inclusive. Note that this "change of text" rule can apply to situations other than employee malfeasance. So-called "inline replies", where someone writes "answers below" and then types in the body of a previous email's text is one example . Another common example is emails that have been processed by a non-standard processing engine. For instance, if a processing tool applies a Bates stamp to the top of each page's extracted text, then a forwarded email will not contain the Bates stamp of the original embedded in its own text, and will thus mark all emails as inclusive. The solution is to process cleanly or to apply Regex filters to remove extraneous text.

- Change of sender or time - if the Analytics engine finds what seems like a prior email, but the sender or time of that email doesn't match what's expected, it can trigger an extra inclusiveness tag. Note that there is a certain amount of tolerance built in for things like different email address display formats ("Einstein, Albert" versus "Albert Einstein" versus "albert.einstein@example.com"). There is also the understanding that date stamps can be deceiving due to clock discrepancies on different email servers and time zone changes.

Inclusiveness doesn't consider recipients. It's possible for two emails to have different recipients but the same content and for either of them to receive the inclusive designation.

- Duplication - while not necessarily a reason for inclusiveness, when duplicate emails exist, either both or neither are marked inclusive by Structured Analytics. Duplicates most commonly occur in a situation where person A sends an email to B and to C, and you collect data from two or more of the three people. To avoid redundant review, you should look at the Email Duplicate Spare field. This will be set to Yes for all but one duplicate in each group of duplicate emails. So the rule should not just be to review the inclusives and their attachments, but rather to review the inclusives and their attachments while skipping the duplicate spares and their attachments.

Blank attachments are considered unique by the Analytics engine. A duplicate email with a blank attachment is considered inclusive.

- Draft emails - draft emails are considered unique and are always marked inclusive. They are not considered for duplicate spare analysis.

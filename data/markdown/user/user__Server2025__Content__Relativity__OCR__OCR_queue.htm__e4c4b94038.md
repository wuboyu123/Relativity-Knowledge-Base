---
title: "OCR queue"
url: https://help.relativity.com/Server2025/Content/Relativity/OCR/OCR_queue.htm
collection: user
fetched_at: 2026-06-22T06:14:26+00:00
sha256: 49740469e8d5af625c6f3e8ba9dd7436025533249dc0a343229aa0249404b2e7
---

OCR queue

# OCR queue

Your permission settings determine whether or not you have access to the OCR Queue tab from Home. You can view all submitted OCR jobs in the environment to check their status, priority, and the workspace to which they belong. You can only access the OCR Queue tab from Home.

To display the default OCR Queue view, select the Queue Management tab, and then click OCR Queue . This list displays all OCR jobs submitted by users in your workspace that haven't yet successfully completed.

OCR queue columns

- Workspace - the name of the workspace containing the OCR set.

- OCR Set Name - the name of the OCR set that has a job running.

- Artifact ID - the OCR set’s artifact ID.

- Status - displays the status of the submitted job; this field updates as the OCR job progresses.

- Priority - the priority of the OCR set job. This value defaults to 100.

- Submitted Date - the date and time at which one of two actions occurred:

- A user clicked Run on the OCR Set console.

- A user clicked Resolve Errors on the OCR Set console when the set was completed with errors.

Jobs are sent to the OCR engine first by priority and then by submitted date. You can change the priority of the OCR job by clicking Change Priority in the bottom left of the view. Only one job runs at a time, the lower numbered job runs first and the higher numbered job runs last.

When you click Change Priority, you can specify a new priority for an OCR job in the queue. To change the queue priority, enter a new value in the Priority field and click Update .

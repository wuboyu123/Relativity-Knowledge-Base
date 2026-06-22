---
title: "Forgotten password reset audit"
url: https://help.relativity.com/Server2025/Content/Relativity/Library_scripts/Forgotten_password_reset_audit.htm
collection: user
fetched_at: 2026-06-22T06:15:21+00:00
sha256: da4be97e7a9ba55b09d4c9d0925cd8f8ba5031cf8a2298637e878dfc29303613
---

Forgotten password reset audit

# Forgotten password reset audit

This Relativity script provides audit records for user password reset requests generated using the Forgot your password? link on the login screen.

## Inputs

After clicking Run on the Script Console, enter values for the following inputs:

- Start Date - the starting date for the report.

- End Date - the ending date for the report.

- Display Audit Records determines which password reset requests the report includes. Your options are:

- All requests

- Valid user requests

- Invalid user requests

- Failed requests

- Maximum Number Of Results determines the maximum number of results that are included in the report. The default value is 1,000.

## Results

When you select your inputs and click Run , the Results section displays the selected password reset requests for the date range you've specified.

The following columns are included in the report:

Column Description

Action The action taken by the user who submitted the password reset request.

Details Results of the action or details about why the action was unsuccessful.

DateTime The date and time the password reset request was submitted.

FirstName The first name of the user associated with the submitted email address.

LastName The last name of the user associated with the submitted email address.

UserArtifactId The artifact ID of the user associated with the submitted email address.

EmailAddress The email address submitted during the password reset request.

IPAddress The IP address the request came from.

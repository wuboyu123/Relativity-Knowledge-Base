---
title: "Query SMTP settings when sending email"
url: https://platform.relativity.com/Server2025/Content/Relativity_API_Helpers/Querying_SMTP_settings_when_sending_email.htm
collection: developer
fetched_at: 2026-06-22T06:33:22+00:00
sha256: ea676870ed71801c94ff45e567211cd4b3ae58cca82455c5220467c7160d5335
---

Query SMTP settings when sending email

# Query SMTP settings when sending email

You can query the Relativity database for SMTP server settings by using the Relativity API Helpers from an extensibility point. Use this functionality when sending email from agents, custom pages, or event handlers in conjunction with the .NET mail interface as illustrated in the following code sample.

This code sample uses the IInstanceSettingsBundle interface available in Relativity 9.6.134.78 above .

Copy

```text
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
using kCura.Agent;

using Relativity.API;

using System;

using System.Collections.Generic;

using System.Net;

using System.Net.Mail;

namespace SendRelativityEmail

{

    [System.Runtime.InteropServices.Guid("ad664098-f186-4b4d-9219-728f82a5fa15")]

    [kCura.Agent.CustomAttributes.Name("Send Relativity Email")]

    public class SendRelativityEmail : AgentBase

    {

        static string smtpPasswordValue;

        static int smtpPortValue;

        static string smtpUserValue;

        static string smtpServerValue;

        public override void Execute()

        {

            SMTPSetting smtpPassword = new SMTPSetting { Section = "kCura.Notification", Name = "SMTPPassword" };

            SMTPSetting smtpPort = new SMTPSetting { Section = "kCura.Notification", Name = "SMTPPort" };

            SMTPSetting smtpServer = new SMTPSetting { Section = "kCura.Notification", Name = "SMTPServer" };

            SMTPSetting smtpUser = new SMTPSetting { Section = "kCura.Notification", Name = "SMTPUserName" };

            List<SMTPSetting> smtpSettings = new List<SMTPSetting> { smtpPort, smtpServer, smtpUser, smtpPassword };

            IInstanceSettingsBundle instanceSettingsBundle = this.Helper.GetInstanceSettingBundle();

            foreach (var smtpInstanceSettingSingle in smtpSettings)

            {

                RaiseMessage("Beginning query", 1);

                try

                {

                    GetSMTPValue(smtpInstanceSettingSingle.Name, smtpInstanceSettingSingle, instanceSettingsBundle);

                }

                catch (Exception ex)

                {

                    RaiseError("Failed to pull data values", ex.Message + "\r\n " + ex.StackTrace);

                }

            }

            try

            {

                string toAddress = "ToAddress@Email.Com";

                string fromAddress = "NoReply@relativity.one";

                string subject = "This is only a test!";

                SendEmail(toAddress, fromAddress, subject);

                RaiseMessage("Sending email now...", 1);

            }

           catch (Exception ex)

            {

                RaiseError("Failed to send E-mail! ", ex.Message + "\r\n " + ex.StackTrace);

            }

        }

        private static void SendEmail(string emailTo, string emailFrom, string emailSubject)

        {

            MailMessage emailOut = new MailMessage(emailFrom, emailTo);

            SmtpClient client = new SmtpClient();

            client.Port = smtpPortValue;

            client.DeliveryMethod = SmtpDeliveryMethod.Network;

            client.UseDefaultCredentials = false;

            client.Host = smtpServerValue;

            emailOut.Subject = emailSubject;

            emailOut.IsBodyHtml = true;

            client.Credentials = new NetworkCredential(smtpUserValue, smtpPasswordValue);

            client.Send(emailOut);

        }

        private static void GetSMTPValue(string settingName, SMTPSetting smtpInstanceSettingSingle, IInstanceSettingsBundle instanceSettingsBundle)

        {

            switch (settingName)

            {

                case "SMTPPassword":

                    var singleSettingValuePass = instanceSettingsBundle.GetStringAsync(smtpInstanceSettingSingle.Section, smtpInstanceSettingSingle.Name);

                    smtpPasswordValue = singleSettingValuePass.Result;

                    break;

                case "SMTPPort":

                    int singleSettingValuePort = Convert.ToInt32(instanceSettingsBundle.GetUIntAsync(smtpInstanceSettingSingle.Section, smtpInstanceSettingSingle.Name).Result.Value);

                    smtpPortValue = singleSettingValuePort;

                    break;

                case "SMTPUserName":

                    var singleSettingValueUser = instanceSettingsBundle.GetStringAsync(smtpInstanceSettingSingle.Section, smtpInstanceSettingSingle.Name);

                    smtpUserValue = singleSettingValueUser.Result;

                    break;

                case "SMTPServer":

                    var singleSettingValueServer = instanceSettingsBundle.GetStringAsync(smtpInstanceSettingSingle.Section, smtpInstanceSettingSingle.Name);

                    smtpServerValue = singleSettingValueServer.Result;

                    break;

            }

        }

        public override string Name

        {

            get

            {

                return "Send Relativity Email";

            }

        }

    }

    public class SMTPSetting

    {

        public string Section { get; set; }

        public string Name { get; set; }

    }

}
```

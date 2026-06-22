---
title: "Permission Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Identity/Permission_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:27:16+00:00
sha256: e042e86fae19d067a7c0a14efcb08d36e23d100ee541cd24a81d18f202ab2d8e
---

Permission Manager (REST) Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://platform.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Permission Manager (REST)

The Relativity REST API supports operations on permissions though the Permission Manager service. The operations available through the service are equivalent to the asynchronous methods for interacting with the permissions in the Relativity Services API. For more information, see Permissions .

You can only use the POST method when interacting with the service.

## Client code sample

The following is an example of .NET REST code for returning groups with admin permissions. You can use this code for all Permission Manager service operations with different endpoint URLs and input JSON values.

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
//Set up the REST client.



HttpClient httpClient = new HttpClient();

httpClient.BaseAddress = new Uri("http://localhost/");

//Set the required headers.



httpClient.DefaultRequestHeaders.Add("X-CSRF-Header", "-");

httpClient.DefaultRequestHeaders.Add("Authorization", "Basic c2FtcGxlYWRtaW5AcmVsYXRpdml0eS5yZXN0OlMwbTNwQHNzdzByZA==");

//Call get groups with admin permissions.



string url = "/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetAdminGroupSelectorAsync";

StringContent content = new StringContent(CreateInputJSON, Encoding.UTF8, "application/json");

HttpResponseMessage response = httpClient.PostAsync(url, content).Result;

string result = response.Content.ReadAsStringAsync().Result;

bool success = HttpStatusCode.Created == response.StatusCode;

//Parse the result with Json.NET.



JObject resultObject = JObject.Parse(result);
```

## Get admin groups

Use this Permission Manager service URL to return groups with admin permissions enabled and disabled:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetAdminGroupSelectorAsync
```

The request does not include any input parameters.

The response returns a GroupSelector object. Group Selector includes the EnabledGroups and DisabledGroups properties that list groups with and without admin permissions.

Sample JSON response Copy

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
{

  "DisabledGroups": [



    {

      "ArtifactID": 762,

      "Name": "Domain Users"

    },

    {

      "ArtifactID": 1015025,

      "Name": "First Level Group"

    },

    {

      "ArtifactID": 1015006,

      "Name": "Relativity Script Admins"

    },

    {

      "ArtifactID": 1015026,

      "Name": "Second Level Group"

    },

    {

      "ArtifactID": 1015027,

      "Name": "Third Level Group"

    }

  ],

  "EnabledGroups": [

    {

      "ArtifactID": 1015005,

      "Name": "Everyone"

    },

    {

      "ArtifactID": 1015028,

      "Name": "Level 1"

    },

    {

      "ArtifactID": 1015029,

      "Name": "Level 2"

    },

    {

      "ArtifactID": 1015030,

      "Name": "Level 3"

    }

  ],

  "LastModified": "2015-02-23T16:29:11.59"

}
```

## Get workspace groups

Use this Permission Manager service URL to return groups with workspace permissions enabled and disabled:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetWorkspaceGroupSelectorAsync
```

The request must include the workspace Artifact ID:

Copy

```text
1
2
3
{

  "workspaceArtifactID": 13758822

}
```

The response includes the EnabledGroups and DisabledGroups properties that list groups with and without workspace permissions.

Sample JSON response Copy

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
{

  "DisabledGroups": [



    {

      "ArtifactID": 762,

      "Name": "Domain Users"

    },

    {

      "ArtifactID": 1015025,

      "Name": "First Level Group"

    },

    {

      "ArtifactID": 1015006,

      "Name": "Relativity Script Admins"

    },

    {

      "ArtifactID": 1015026,

      "Name": "Second Level Group"

    },

    {

      "ArtifactID": 1015027,

      "Name": "Third Level Group"

    }

  ],

  "EnabledGroups": [

    {

      "ArtifactID": 1015005,

      "Name": "Everyone"

    },

    {

      "ArtifactID": 1015028,

      "Name": "Level 1"

    },

    {

      "ArtifactID": 1015029,

      "Name": "Level 2"

    },

    {

      "ArtifactID": 1015030,

      "Name": "Level 3"

    }

  ],

  "LastModified": "2015-02-23T17:03:23.413"

}
```

## Get item groups

Use this Permission Manager service URL to return groups with item permissions enabled and disabled:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetItemGroupSelectorAsync
```

The request must include the Artifact IDs for the workspace and the item:

Copy

```text
1
2
3
4
{

  "workspaceArtifactID": 13758822,

  "artifactID": 17234345

}
```

The response returns includes the EnabledGroups and DisabledGroups properties that list groups with and without item permissions.

Sample JSON response Copy

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
{

  "DisabledGroups": [



    {

      "ArtifactID": 762,

      "Name": "Domain Users"

    },

    {

      "ArtifactID": 1015025,

      "Name": "First Level Group"

    },

    {

      "ArtifactID": 1015006,

      "Name": "Relativity Script Admins"

    },

    {

      "ArtifactID": 1015026,

      "Name": "Second Level Group"

    },

    {

      "ArtifactID": 1015027,

      "Name": "Third Level Group"

    }

  ],

  "EnabledGroups": [

    {

      "ArtifactID": 1015005,

      "Name": "Everyone"

    },

    {

      "ArtifactID": 1015028,

      "Name": "Level 1"

    },

    {

      "ArtifactID": 1015029,

      "Name": "Level 2"

    },

    {

      "ArtifactID": 1015030,

      "Name": "Level 3"

    }

  ],

  "LastModified": "2015-02-23T17:03:23.413"

}
```

## Add and remove admin groups

Use this Permission Manager service URL to add and remove groups to and from admin permissions:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/AddRemoveAdminGroupsAsync
```

The request must include a valid JSON representation of the GroupSelector object. It is recommended that you first return a GroupSelector, and then manipulate it by moving the groups into the EnabledGroups and DisabledGroups collections as GroupRef objects. For simplicity you can set the enabled and disabled groups to only the groups you wish to modify. All other groups will not be altered within the GroupSelector object when setting the values.

The GroupSelector object must have the latest value of LastModified, and every call that returns GroupSelector will update this value. This prevents a user from reading a value and modifying it if another user has read that value with the intent of changing it as well. Item-level security must be enabled to add or remove groups to the permissions for individual items.

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
{

  "groupSelector": {

    "DisabledGroups": [

      {

        "ArtifactID": 1015027,

      }

    ],

    "EnabledGroups": [

      {

        "ArtifactID": 1015005,

      },

      {

        "ArtifactID": 1015028,

      },

      {

        "ArtifactID": 1015029,

      },

      {

        "ArtifactID": 1015030,

      }

    ],

    "LastModified": "2015-02-23T17:03:23.413"

  }

}
```

The response does not contain any data. Success or failure is indicated by the HTTP status code. For more information, see HTTP status codes .

## Add and remove workspace groups

Use this Permission Manager service URL to add and remove groups to and from workspace permissions:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/AddRemoveWorkspaceGroupsAsync
```

The request must include a workspace Artifact ID and a valid JSON representation of the GroupSelector object. It is recommended that you first return a GroupSelector, and then manipulate it by moving the groups into the EnabledGroups and DisabledGroups collections as GroupRef objects. For simplicity you can set the enabled and disabled groups to only the groups you wish to modify. All other groups will not be altered within the GroupSelector object when setting the values.

The GroupSelector object must have the latest value of LastModified, and every call that returns GroupSelector will update this value. This prevents a user from reading a value and modifying it if another user has read that value with the intent of changing it as well. Item-level security must be enabled to add or remove groups to the permissions for individual items.

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
{

  "workspaceArtifactID": 1343243,

  "groupSelector": {

    "DisabledGroups": [

      {

        "ArtifactID": 1015027

      }

    ],

    "EnabledGroups": [

      {

        "ArtifactID": 1015005

      },

      {

        "ArtifactID": 1015028

      },

      {

        "ArtifactID": 1015029

      },

      {

        "ArtifactID": 1015030

      }

    ],

    "LastModified": "2015-02-23T17:03:23.413"

  }

}
```

The response does not contain any data. Success or failure is indicated by the HTTP status code. For more information, see HTTP status codes .

## Add and remove item groups

Use this Permission Manager service URL to add and remove groups to and from item permissions:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/AddRemoveItemGroupsAsync;
```

The request must include the workspace and item Artifact IDs and a valid JSON representation of the GroupSelector object. It is recommended that you first return a GroupSelector, and then manipulate it by moving the groups into the EnabledGroups and DisabledGroups collections as GroupRef objects. For simplicity you can set the enabled and disabled groups to only the groups you wish to modify. All other groups will not be altered within the GroupSelector object when setting the values.

The GroupSelector object must have the latest value of LastModified, and every call that returns GroupSelector will update this value. This prevents a user from reading a value and modifying it if another user has read that value with the intent of changing it as well. Item-level security must be enabled to add or remove groups to the permissions for individual items.

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
{

    "workspaceArtifactID": 1343243,

    "artifactID": 1673243,

    "groupSelector": {

    "DisabledGroups": [

      {

        "ArtifactID": 1015027,

      }

    ],

    "EnabledGroups": [

      {

        "ArtifactID": 1015005,

      },

      {

        "ArtifactID": 1015028,

      },

      {

        "ArtifactID": 1015029,

      },

      {

        "ArtifactID": 1015030,

      }

    ],

    "LastModified": "2015-02-23T17:03:23.413"

  }

}
```

The response does not contain any data. Success or failure is indicated by the HTTP status code. For more information, see HTTP status codes .

## Get admin permissions

Use this Permission Manager service URL to return the admin permissions for a group:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetAdminGroupPermissionsAsync
```

The request must include a valid JSON representation of the GroupRef object.

Copy

```text
1
2
3
4
5
{

  "group": {

    "ArtifactID": 13761061

  }

}
```

The response contains the group's admin permissions.

Click to display JSON response Copy

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
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
{"group":{"artifactID":1015005}}

{

  "ArtifactID": -1,

  "GroupID": 1015005,

  "ObjectPermissions": [

    {

      "ArtifactGroupingID": 1000006,

      "Name": "Agent",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 20,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 1000007,

      "Name": "Agent Type",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 35,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 1000009,

      "Name": "Application Install",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 37,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 1000010,

      "Name": "Application Install Result",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 38,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 1000005,

      "Name": "Application Library",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 0,

      "ParentArtifactTypeID": -1

    },

    {

      "ArtifactGroupingID": 6,

      "Name": "Choice",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 7,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 2,

      "Name": "Client",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 5,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 14,

      "Name": "Error",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": true,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": true,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 18,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 7,

      "Name": "Group",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 3,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 1000011,

      "Name": "License",

      "ViewSelected": false,

      "EditEditable": false,

      "EditSelected": false,

      "DeleteEditable": false,

      "DeleteSelected": false,

      "AddEditable": false,

      "AddSelected": false,

      "EditSecurityEditable": false,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 39,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 3,

      "Name": "Matter",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 6,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 1000001,

      "Name": "Relativity Script",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 28,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 1000002,

      "Name": "Resource File",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 30,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 1000003,

      "Name": "Resource Pool",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 31,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 1000004,

      "Name": "Server",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 0,

      "ParentArtifactTypeID": -1

    },

    {

      "ArtifactGroupingID": 1000000,

      "Name": "Tab",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 23,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 4,

      "Name": "User",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 2,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 13,

      "Name": "View",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 4,

      "ParentArtifactTypeID": 0

    },

    {

      "ArtifactGroupingID": 5,

      "Name": "Workspace",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 0,

      "ParentArtifactTypeID": -1

    },

    {

      "ArtifactGroupingID": 1000008,

      "Name": "Workspace Application",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 36,

      "ParentArtifactTypeID": 0

    }

  ],

  "TabVisibility": [

    {

      "Name": "Workspaces",

      "Editable": true,

      "Selected": false,

      "Value": 1029123,

      "Children": []

    },

    {

      "Name": "Clients",

      "Editable": true,

      "Selected": false,

      "Value": 1014954,

      "Children": []

    },

    {

      "Name": "Matters",

      "Editable": true,

      "Selected": false,

      "Value": 1014955,

      "Children": []

    },

    {

      "Name": "Users",

      "Editable": true,

      "Selected": false,

      "Value": 1014956,

      "Children": []

    },

    {

      "Name": "Groups",

      "Editable": true,

      "Selected": false,

      "Value": 1014957,

      "Children": []

    },

    {

      "Name": "Views",

      "Editable": true,

      "Selected": false,

      "Value": 1014958,

      "Children": []

    },

    {

      "Name": "Choices",

      "Editable": true,

      "Selected": false,

      "Value": 1014959,

      "Children": []

    },

    {

      "Name": "Agents",

      "Editable": true,

      "Selected": false,

      "Value": 1014960,

      "Children": []

    },

    {

      "Name": "Queue Management",

      "Editable": true,

      "Selected": false,

      "Value": 1015136,

      "Children": [

        {

          "Name": "Production Queue",

          "Editable": true,

          "Selected": false,

          "Value": 1015127,

          "Children": []

        },

        {

          "Name": "Branding Queue",

          "Editable": true,

          "Selected": false,

          "Value": 1014984,

          "Children": []

        },

        {

          "Name": "Worker Manager Queue",

          "Editable": true,

          "Selected": false,

          "Value": 1014983,

          "Children": []

        },

        {

          "Name": "OCR Queue",

          "Editable": true,

          "Selected": false,

          "Value": 1015093,

          "Children": []

        },

        {

          "Name": "Workspace Upgrade Queue",

          "Editable": true,

          "Selected": false,

          "Value": 1029131,

          "Children": []

        }

      ]

    },

    {

      "Name": "Relativity Script Library",

      "Editable": true,

      "Selected": false,

      "Value": 1014995,

      "Children": []

    },

    {

      "Name": "User Status",

      "Editable": true,

      "Selected": false,

      "Value": 1014996,

      "Children": []

    },

    {

      "Name": "Instance Details",

      "Editable": true,

      "Selected": false,

      "Value": 1014963,

      "Children": []

    },

    {

      "Name": "Resource Files",

      "Editable": true,

      "Selected": false,

      "Value": 1015008,

      "Children": []

    },

    {

      "Name": "Tabs",

      "Editable": true,

      "Selected": false,

      "Value": 1014962,

      "Children": []

    },

    {

      "Name": "Resource Pools",

      "Editable": true,

      "Selected": false,

      "Value": 1015033,

      "Children": []

    },

    {

      "Name": "Servers",

      "Editable": true,

      "Selected": false,

      "Value": 1015039,

      "Children": []

    },

    {

      "Name": "License",

      "Editable": true,

      "Selected": false,

      "Value": 1015083,

      "Children": []

    },

    {

      "Name": "Application Library",

      "Editable": true,

      "Selected": false,

      "Value": 1015292,

      "Children": []

    },

    {

      "Name": "Platform Status",

      "Editable": true,

      "Selected": false,

      "Value": 1029125,

      "Children": []

    }

  ],

  "BrowserPermissions": [],

  "MassActionPermissions": [],

  "AdminPermissions": [

    {

      "Name": "Agent Operations",

      "Editable": true,

      "Selected": false,

      "Value": 504,

      "Children": []

    },

    {

      "Name": "Change Queue Priority",

      "Editable": true,

      "Selected": false,

      "Value": 503,

      "Children": []

    },

    {

      "Name": "Force Logout on User Status",

      "Editable": true,

      "Selected": false,

      "Value": 500,

      "Children": []

    },

    {

      "Name": "Manage Object Types",

      "Editable": true,

      "Selected": false,

      "Value": 103,

      "Children": []

    },

    {

      "Name": "Send Message",

      "Editable": true,

      "Selected": false,

      "Value": 502,

      "Children": []

    },

    {

      "Name": "Use Quick Nav",

      "Editable": true,

      "Selected": true,

      "Value": 177,

      "Children": []

    },

    {

      "Name": "View Audits",

      "Editable": true,

      "Selected": false,

      "Value": 1000031,

      "Children": []

    }

  ],

  "LastModified": "2015-02-22T00:14:51.87"

}
```

## Get workspace permissions

Use this Permission Manager service URL to return the workspace permissions for a group:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetWorkspaceGroupPermissionsAsync
```

The request must include a workspace Artifact ID and a valid JSON representation of the GroupRef object.

Copy

```text
1
2
3
4
5
6
{

  "workspaceArtifactID": 13758822,

  "group": {

    "ArtifactID": 13761061

  }

}
```

The response contains the group's permissions to the workspaces.

Click to display JSON response Copy

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
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
941
942
943
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
982
983
984
985
986
987
988
989
990
991
992
993
994
995
996
997
998
999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
1528
1529
1530
1531
1532
1533
1534
1535
1536
1537
1538
1539
1540
1541
1542
1543
1544
1545
1546
1547
1548
1549
1550
1551
1552
1553
1554
1555
1556
1557
1558
1559
1560
1561
1562
1563
1564
1565
1566
1567
1568
1569
1570
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
1588
1589
1590
1591
1592
1593
1594
1595
1596
1597
1598
1599
1600
1601
1602
1603
1604
1605
1606
1607
1608
1609
1610
1611
1612
1613
1614
1615
1616
1617
1618
1619
1620
1621
1622
1623
1624
1625
1626
1627
1628
1629
1630
1631
1632
1633
1634
1635
1636
1637
1638
1639
1640
1641
1642
1643
1644
1645
1646
{

  "ArtifactID": 1003663,

  "GroupID": 1036399,

  "ObjectPermissions": [

    {

      "ArtifactGroupingID": 1000037,

      "Name": "Agent Type",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 35,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000028,

      "Name": "Analytics Categorization Result",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 2,

      "ArtifactTypeID": 1000020,

      "ParentArtifactTypeID": 1000021

    },

    {

      "ArtifactGroupingID": 1000029,

      "Name": "Analytics Categorization Set",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000021,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000030,

      "Name": "Analytics Category",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 2,

      "ArtifactTypeID": 1000022,

      "ParentArtifactTypeID": 1000021

    },

    {

      "ArtifactGroupingID": 1000031,

      "Name": "Analytics Example",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 2,

      "ArtifactTypeID": 1000023,

      "ParentArtifactTypeID": 1000021

    },

    {

      "ArtifactGroupingID": 1000023,

      "Name": "Analytics Profile",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000015,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000044,

      "Name": "Application Field Code",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000031,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000007,

      "Name": "Batch",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 2,

      "ArtifactTypeID": 27,

      "ParentArtifactTypeID": 24

    },

    {

      "ArtifactGroupingID": 1000004,

      "Name": "Batch Set",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 24,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000016,

      "Name": "Case Info",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000010,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 6,

      "Name": "Choice",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 7,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000015,

      "Name": "Contacts",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000009,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000036,

      "Name": "Custom Page",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000026,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 9,

      "Name": "Document",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": true,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [

        {

          "PermissionID": 1000002,

          "Name": "Print / Save As PDF",

          "Selected": false

        },

        {

          "PermissionID": 1000005,

          "Name": "Local Access (Download, Copy Text)",

          "Selected": false

        },

        {

          "PermissionID": 1000006,

          "Name": "Redact Document",

          "Selected": true

        },

        {

          "PermissionID": 1000007,

          "Name": "Highlight Document",

          "Selected": true

        },

        {

          "PermissionID": 1000018,

          "Name": "Add Image",

          "Selected": true

        },

        {

          "PermissionID": 1000019,

          "Name": "Delete Image",

          "Selected": false

        }

      ],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 2,

      "ArtifactTypeID": 10,

      "ParentArtifactTypeID": 9

    },

    {

      "ArtifactGroupingID": 1000034,

      "Name": "Event Handler",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 2,

      "ArtifactTypeID": 1000002,

      "ParentArtifactTypeID": 25

    },

    {

      "ArtifactGroupingID": 15,

      "Name": "Field",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [

        {

          "PermissionID": 88,

          "Name": "Add Field Choice By Link",

          "Selected": false

        }

      ],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 14,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 10,

      "Name": "Folder",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 9,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000026,

      "Name": "Imaging Profile",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000018,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000027,

      "Name": "Imaging Set",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000019,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000039,

      "Name": "Install Event Handler",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 40,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 16,

      "Name": "Layout",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 16,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000042,

      "Name": "Lists",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000030,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000000,

      "Name": "Markup Set",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 22,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000043,

      "Name": "Mass Operation",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 2,

      "ArtifactTypeID": 41,

      "ParentArtifactTypeID": 25

    },

    {

      "ArtifactGroupingID": 1000025,

      "Name": "Native Type",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000017,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000033,

      "Name": "Object Rule",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 2,

      "ArtifactTypeID": 33,

      "ParentArtifactTypeID": 25

    },

    {

      "ArtifactGroupingID": 1000005,

      "Name": "Object Type",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 25,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000021,

      "Name": "OCR Profile",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000012,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000022,

      "Name": "OCR Set",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000013,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000040,

      "Name": "Password Bank",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000028,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000041,

      "Name": "Password Entry",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 2,

      "ArtifactTypeID": 1000029,

      "ParentArtifactTypeID": 1000028

    },

    {

      "ArtifactGroupingID": 1000032,

      "Name": "Persistent Highlight Set",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000024,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000017,

      "Name": "PivotProfile",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000011,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 17,

      "Name": "Production",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 17,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000020,

      "Name": "Relativity Application",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000014,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000008,

      "Name": "Relativity Script",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 28,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000035,

      "Name": "Relativity Time Zone",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000025,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000024,

      "Name": "Repeated Content Filter",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000016,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 18,

      "Name": "Report",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 19,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 14,

      "Name": "Search",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 15,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000006,

      "Name": "Search Folder",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 0,

      "ParentArtifactTypeID": -1

    },

    {

      "ArtifactGroupingID": 1000009,

      "Name": "Search Index",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [

        {

          "PermissionID": 119,

          "Name": "Dictionary Access",

          "Selected": false

        }

      ],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 29,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000012,

      "Name": "Search Terms Report",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000006,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000013,

      "Name": "Search Terms Result",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 2,

      "ArtifactTypeID": 1000007,

      "ParentArtifactTypeID": 1000006

    },

    {

      "ArtifactGroupingID": 1000001,

      "Name": "Tab",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 23,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000011,

      "Name": "Transform",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 2,

      "ArtifactTypeID": 1000005,

      "ParentArtifactTypeID": 1000004

    },

    {

      "ArtifactGroupingID": 1000010,

      "Name": "Transform Set",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000004,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 13,

      "Name": "View",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 4,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 1000014,

      "Name": "Work Product",

      "ViewSelected": false,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": true,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": true,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 1,

      "ArtifactTypeID": 1000008,

      "ParentArtifactTypeID": 8

    },

    {

      "ArtifactGroupingID": 5,

      "Name": "Workspace",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": false,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": false,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 0,

      "ArtifactTypeID": 8,

      "ParentArtifactTypeID": -1

    }

  ],

  "TabVisibility": [

    {

      "Name": "Documents",

      "Editable": true,

      "Selected": true,

      "Value": 1034251,

      "Children": []

    },

    {

      "Name": "Summary Reports",

      "Editable": true,

      "Selected": false,

      "Value": 1034253,

      "Children": []

    },

    {

      "Name": "Review Batches",

      "Editable": true,

      "Selected": true,

      "Value": 1035256,

      "Children": []

    },

    {

      "Name": "Administration",

      "Editable": true,

      "Selected": false,

      "Value": 1035260,

      "Children": [

        {

          "Name": "Workspace Details",

          "Editable": true,

          "Selected": false,

          "Value": 1034252,

          "Children": []

        },

        {

          "Name": "Markup Sets",

          "Editable": true,

          "Selected": false,

          "Value": 1034254,

          "Children": []

        },

        {

          "Name": "Production Sets",

          "Editable": true,

          "Selected": false,

          "Value": 1034255,

          "Children": []

        },

        {

          "Name": "Batch Sets",

          "Editable": true,

          "Selected": false,

          "Value": 1035223,

          "Children": []

        },

        {

          "Name": "Object Type",

          "Editable": true,

          "Selected": false,

          "Value": 1035225,

          "Children": []

        },

        {

          "Name": "Fields",

          "Editable": true,

          "Selected": false,

          "Value": 1034256,

          "Children": []

        },

        {

          "Name": "Choices",

          "Editable": true,

          "Selected": false,

          "Value": 1034257,

          "Children": []

        },

        {

          "Name": "Layouts",

          "Editable": true,

          "Selected": false,

          "Value": 1034258,

          "Children": []

        },

        {

          "Name": "Views",

          "Editable": true,

          "Selected": false,

          "Value": 1034259,

          "Children": []

        },

        {

          "Name": "Search Indexes",

          "Editable": true,

          "Selected": false,

          "Value": 1035270,

          "Children": []

        },

        {

          "Name": "Scripts",

          "Editable": true,

          "Selected": false,

          "Value": 1035264,

          "Children": []

        },

        {

          "Name": "Tabs",

          "Editable": true,

          "Selected": false,

          "Value": 1034261,

          "Children": []

        },

        {

          "Name": "History",

          "Editable": true,

          "Selected": false,

          "Value": 1034264,

          "Children": []

        },

        {

          "Name": "Transform Sets",

          "Editable": true,

          "Selected": false,

          "Value": 1035286,

          "Children": []

        },

        {

          "Name": "Relativity Applications",

          "Editable": true,

          "Selected": false,

          "Value": 1036634,

          "Children": []

        },

        {

          "Name": "Persistent Highlight Sets",

          "Editable": true,

          "Selected": false,

          "Value": 1037542,

          "Children": []

        }

      ]

    },

    {

      "Name": "User Status",

      "Editable": true,

      "Selected": false,

      "Value": 1035275,

      "Children": []

    },

    {

      "Name": "Pivot Profiles",

      "Editable": true,

      "Selected": false,

      "Value": 1036455,

      "Children": []

    },

    {

      "Name": "OCR",

      "Editable": true,

      "Selected": false,

      "Value": 1036667,

      "Children": [

        {

          "Name": "OCR Profiles",

          "Editable": true,

          "Selected": false,

          "Value": 1036641,

          "Children": []

        },

        {

          "Name": "OCR Sets",

          "Editable": true,

          "Selected": false,

          "Value": 1036642,

          "Children": []

        }

      ]

    },

    {

      "Name": "Analytics",

      "Editable": true,

      "Selected": false,

      "Value": 1036701,

      "Children": [

        {

          "Name": "Analytics Profiles",

          "Editable": true,

          "Selected": false,

          "Value": 1036702,

          "Children": []

        },

        {

          "Name": "Repeated Content Filters",

          "Editable": true,

          "Selected": false,

          "Value": 1036703,

          "Children": []

        },

        {

          "Name": "Analytics Categorization Set",

          "Editable": true,

          "Selected": false,

          "Value": 1037489,

          "Children": []

        }

      ]

    },

    {

      "Name": "Imaging",

      "Editable": true,

      "Selected": false,

      "Value": 1036759,

      "Children": [

        {

          "Name": "Imaging Profiles",

          "Editable": true,

          "Selected": false,

          "Value": 1036733,

          "Children": []

        },

        {

          "Name": "Imaging Sets",

          "Editable": true,

          "Selected": false,

          "Value": 1036753,

          "Children": []

        },

        {

          "Name": "Native Types",

          "Editable": true,

          "Selected": false,

          "Value": 1036717,

          "Children": []

        },

        {

          "Name": "Password Bank",

          "Editable": true,

          "Selected": false,

          "Value": 1038258,

          "Children": []

        },

        {

          "Name": "Application Field Code",

          "Editable": true,

          "Selected": false,

          "Value": 1038483,

          "Children": []

        }

      ]

    },

    {

      "Name": "Work Product",

      "Editable": true,

      "Selected": false,

      "Value": 1036398,

      "Children": [

        {

          "Name": "Pleadings",

          "Editable": true,

          "Selected": false,

          "Value": 1035405,

          "Children": []

        },

        {

          "Name": "Contacts",

          "Editable": true,

          "Selected": false,

          "Value": 1035429,

          "Children": []

        },

        {

          "Name": "Case Info",

          "Editable": true,

          "Selected": false,

          "Value": 1035439,

          "Children": []

        }

      ]

    },

    {

      "Name": "Custom Pages",

      "Editable": true,

      "Selected": false,

      "Value": 1038010,

      "Children": []

    },

    {

      "Name": "Search Terms Report",

      "Editable": true,

      "Selected": false,

      "Value": 1038279,

      "Children": [

        {

          "Name": "Search Terms Reports",

          "Editable": true,

          "Selected": false,

          "Value": 1035314,

          "Children": []

        },

        {

          "Name": "Search Terms Results",

          "Editable": true,

          "Selected": false,

          "Value": 1038298,

          "Children": []

        }

      ]

    },

    {

      "Name": "Persistent Lists",

      "Editable": true,

      "Selected": false,

      "Value": 1038387,

      "Children": [

        {

          "Name": "Lists",

          "Editable": true,

          "Selected": false,

          "Value": 1038392,

          "Children": []

        }

      ]

    }

  ],

  "BrowserPermissions": [

    {

      "Name": "Folders",

      "Editable": true,

      "Selected": true,

      "Value": 1000032,

      "Children": []

    },

    {

      "Name": "Field Tree",

      "Editable": true,

      "Selected": true,

      "Value": 1000034,

      "Children": []

    },

    {

      "Name": "Advanced & Saved Searches",

      "Editable": true,

      "Selected": false,

      "Value": 1000033,

      "Children": []

    },

    {

      "Name": "Clusters",

      "Editable": true,

      "Selected": false,

      "Value": 104,

      "Children": []

    }

  ],

  "MassActionPermissions": [

    {

      "Name": "Cluster",

      "Editable": true,

      "Selected": false,

      "Value": 94,

      "Children": []

    },

    {

      "Name": "Convert",

      "Editable": true,

      "Selected": false,

      "Value": 1000219,

      "Children": []

    },

    {

      "Name": "Export to File",

      "Editable": true,

      "Selected": true,

      "Value": 1000035,

      "Children": []

    },

    {

      "Name": "Copy",

      "Editable": true,

      "Selected": false,

      "Value": 107,

      "Children": []

    },

    {

      "Name": "Delete",

      "Editable": true,

      "Selected": false,

      "Value": 1000022,

      "Children": []

    },

    {

      "Name": "Edit",

      "Editable": true,

      "Selected": false,

      "Value": 1000001,

      "Children": []

    },

    {

      "Name": "Images",

      "Editable": true,

      "Selected": false,

      "Value": 1000025,

      "Children": []

    },

    {

      "Name": "Move",

      "Editable": true,

      "Selected": false,

      "Value": 1000021,

      "Children": []

    },

    {

      "Name": "Print Image",

      "Editable": true,

      "Selected": false,

      "Value": 1000026,

      "Children": []

    },

    {

      "Name": "Produce",

      "Editable": true,

      "Selected": false,

      "Value": 1000023,

      "Children": []

    },

    {

      "Name": "Replace",

      "Editable": true,

      "Selected": false,

      "Value": 1000024,

      "Children": []

    },

    {

      "Name": "Process Transcript",

      "Editable": true,

      "Selected": false,

      "Value": 100,

      "Children": []

    },

    {

      "Name": "Send To Case Map",

      "Editable": true,

      "Selected": false,

      "Value": 1000028,

      "Children": []

    },

    {

      "Name": "Tally/Sum/Average",

      "Editable": true,

      "Selected": true,

      "Value": 1000027,

      "Children": []

    }

  ],

  "AdminPermissions": [

    {

      "Name": "Allow dtSearch Index Swap",

      "Editable": true,

      "Selected": false,

      "Value": 141,

      "Children": []

    },

    {

      "Name": "Allow Export",

      "Editable": true,

      "Selected": false,

      "Value": 159,

      "Children": []

    },

    {

      "Name": "Allow Import",

      "Editable": true,

      "Selected": false,

      "Value": 158,

      "Children": []

    },

    {

      "Name": "Assign Batches",

      "Editable": true,

      "Selected": false,

      "Value": 101,

      "Children": []

    },

    {

      "Name": "Delete Object Dependencies",

      "Editable": true,

      "Selected": false,

      "Value": 140,

      "Children": []

    },

    {

      "Name": "Download Relativity Desktop Client",

      "Editable": true,

      "Selected": false,

      "Value": 126,

      "Children": []

    },

    {

      "Name": "Manage Object Types",

      "Editable": true,

      "Selected": false,

      "Value": 103,

      "Children": []

    },

    {

      "Name": "Manage Relativity Applications",

      "Editable": true,

      "Selected": false,

      "Value": 138,

      "Children": []

    },

    {

      "Name": "Modify System Keyboard Shortcuts",

      "Editable": true,

      "Selected": false,

      "Value": 139,

      "Children": []

    },

    {

      "Name": "Override Production Restrictions",

      "Editable": true,

      "Selected": false,

      "Value": 127,

      "Children": []

    },

    {

      "Name": "Use Pivot/Chart",

      "Editable": true,

      "Selected": true,

      "Value": 120,

      "Children": []

    },

    {

      "Name": "Use Quick Nav",

      "Editable": true,

      "Selected": true,

      "Value": 177,

      "Children": []

    },

    {

      "Name": "Use Sampling",

      "Editable": true,

      "Selected": false,

      "Value": 1000198,

      "Children": []

    },

    {

      "Name": "View All Audits",

      "Editable": true,

      "Selected": false,

      "Value": 1000031,

      "Children": []

    },

    {

      "Name": "View Batch Pane",

      "Editable": true,

      "Selected": false,

      "Value": 1000046,

      "Children": []

    },

    {

      "Name": "View Image Thumbnails",

      "Editable": true,

      "Selected": false,

      "Value": 1000172,

      "Children": []

    },

    {

      "Name": "View Images Hidden for QC Review",

      "Editable": true,

      "Selected": false,

      "Value": 157,

      "Children": []

    },

    {

      "Name": "View User Status",

      "Editable": true,

      "Selected": false,

      "Value": 125,

      "Children": []

    },

    {

      "Name": "View User's Personal Items",

      "Editable": true,

      "Selected": false,

      "Value": 501,

      "Children": []

    },

    {

      "Name": "View Workspace Details",

      "Editable": true,

      "Selected": false,

      "Value": 124,

      "Children": []

    }

  ],

  "LastModified": "2015-02-22T00:27:21.443"

}
```

## Get item permissions

Use this Permission Manager service URL to return the item permissions for a group:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetItemGroupPermissionsAsync
```

The request must include Artifact IDs of the workspace and the item and a valid JSON representation of the GroupRef object.

Copy

```text
1
2
3
4
5
6
7
{

  "workspaceArtifactID": 13758822,

  "ArtifactID": 1038413,

  "group": {

    "ArtifactID": 1036399

  }

}
```

The response contains the group's permissions to the item. Note that the set of permissions can be different depending on the item's object type. The following is an example of Document permissions.

Click to display JSON response Copy

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
{

  "ArtifactID": 1038413,

  "GroupID": 1036399,

  "ObjectPermissions": [

    {

      "ArtifactGroupingID": 9,

      "Name": "Document",

      "ViewSelected": true,

      "EditEditable": true,

      "EditSelected": true,

      "DeleteEditable": true,

      "DeleteSelected": false,

      "AddEditable": false,

      "AddSelected": false,

      "EditSecurityEditable": true,

      "EditSecuritySelected": false,

      "CanRemovePermissions": false,

      "SubPermissions": [

        {

          "PermissionID": 1000002,

          "Name": "Print / Save As PDF",

          "Selected": false

        },

        {

          "PermissionID": 1000005,

          "Name": "Local Access (Download, Copy Text)",

          "Selected": false

        },

        {

          "PermissionID": 1000006,

          "Name": "Redact Document",

          "Selected": true

        },

        {

          "PermissionID": 1000007,

          "Name": "Highlight Document",

          "Selected": true

        },

        {

          "PermissionID": 1000018,

          "Name": "Add Image",

          "Selected": true

        },

        {

          "PermissionID": 1000019,

          "Name": "Delete Image",

          "Selected": false

        }

      ],

      "CustomPermissions": [],

      "HasChildPermissions": false,

      "HierarchyIndent": 2,

      "ArtifactTypeID": 10,

      "ParentArtifactTypeID": 9

    }

  ],

  "TabVisibility": [],

  "BrowserPermissions": [],

  "MassActionPermissions": [],

  "AdminPermissions": [],

  "LastModified": "2015-02-22T00:34:43.813"

}
```

## Set admin permissions

Use this Permission Manager service URL to set the admin permissions for a group:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/SetAdminGroupPermissionsAsync
```

The request must include a valid JSON representation of the GroupPermissions object containing the admin permissions set. It is recommended that you first return GroupPermissions object and then inspect and manipulate the permissions within it.

Click to display JSON response Copy

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
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
{

  "GroupPermissions": {

    "ArtifactID": -1,

    "GroupID": 1015005,

    "ObjectPermissions": [

      {

        "ArtifactGroupingID": 1000006,

        "Name": "Agent",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 20,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 1000007,

        "Name": "Agent Type",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 35,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 1000009,

        "Name": "Application Install",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 37,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 1000010,

        "Name": "Application Install Result",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 38,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 1000005,

        "Name": "Application Library",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 0,

        "ParentArtifactTypeID": -1

      },

      {

        "ArtifactGroupingID": 6,

        "Name": "Choice",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 7,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 2,

        "Name": "Client",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 5,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 14,

        "Name": "Error",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": true,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": true,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 18,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 7,

        "Name": "Group",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 3,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 1000011,

        "Name": "License",

        "ViewSelected": false,

        "EditEditable": false,

        "EditSelected": false,

        "DeleteEditable": false,

        "DeleteSelected": false,

        "AddEditable": false,

        "AddSelected": false,

        "EditSecurityEditable": false,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 39,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 3,

        "Name": "Matter",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 6,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 1000001,

        "Name": "Relativity Script",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 28,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 1000002,

        "Name": "Resource File",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 30,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 1000003,

        "Name": "Resource Pool",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 31,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 1000004,

        "Name": "Server",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 0,

        "ParentArtifactTypeID": -1

      },

      {

        "ArtifactGroupingID": 1000000,

        "Name": "Tab",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 23,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 4,

        "Name": "User",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 2,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 13,

        "Name": "View",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 4,

        "ParentArtifactTypeID": 0

      },

      {

        "ArtifactGroupingID": 5,

        "Name": "Workspace",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 0,

        "ParentArtifactTypeID": -1

      },

      {

        "ArtifactGroupingID": 1000008,

        "Name": "Workspace Application",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 36,

        "ParentArtifactTypeID": 0

      }

    ],

    "TabVisibility": [

      {

        "Name": "Workspaces",

        "Editable": true,

        "Selected": false,

        "Value": 1029123,

        "Children": []

      },

      {

        "Name": "Clients",

        "Editable": true,

        "Selected": false,

        "Value": 1014954,

        "Children": []

      },

      {

        "Name": "Matters",

        "Editable": true,

        "Selected": false,

        "Value": 1014955,

        "Children": []

      },

      {

        "Name": "Users",

        "Editable": true,

        "Selected": false,

        "Value": 1014956,

        "Children": []

      },

      {

        "Name": "Groups",

        "Editable": true,

        "Selected": false,

        "Value": 1014957,

        "Children": []

      },

      {

        "Name": "Views",

        "Editable": true,

        "Selected": false,

        "Value": 1014958,

        "Children": []

      },

      {

        "Name": "Choices",

        "Editable": true,

        "Selected": false,

        "Value": 1014959,

        "Children": []

      },

      {

        "Name": "Agents",

        "Editable": true,

        "Selected": false,

        "Value": 1014960,

        "Children": []

      },

      {

        "Name": "Queue Management",

        "Editable": true,

        "Selected": false,

        "Value": 1015136,

        "Children": [

          {

            "Name": "Production Queue",

            "Editable": true,

            "Selected": false,

            "Value": 1015127,

            "Children": []

          },

          {

            "Name": "Branding Queue",

            "Editable": true,

            "Selected": false,

            "Value": 1014984,

            "Children": []

          },

          {

            "Name": "Worker Manager Queue",

            "Editable": true,

            "Selected": false,

            "Value": 1014983,

            "Children": []

          },

          {

            "Name": "OCR Queue",

            "Editable": true,

            "Selected": false,

            "Value": 1015093,

            "Children": []

          },

          {

            "Name": "Workspace Upgrade Queue",

            "Editable": true,

            "Selected": false,

            "Value": 1029131,

            "Children": []

          }

        ]

      },

      {

        "Name": "Relativity Script Library",

        "Editable": true,

        "Selected": false,

        "Value": 1014995,

        "Children": []

      },

      {

        "Name": "User Status",

        "Editable": true,

        "Selected": false,

        "Value": 1014996,

        "Children": []

      },

      {

        "Name": "Instance Details",

        "Editable": true,

        "Selected": false,

        "Value": 1014963,

        "Children": []

      },

      {

        "Name": "Resource Files",

        "Editable": true,

        "Selected": false,

        "Value": 1015008,

        "Children": []

      },

      {

        "Name": "Tabs",

        "Editable": true,

        "Selected": false,

        "Value": 1014962,

        "Children": []

      },

      {

        "Name": "Resource Pools",

        "Editable": true,

        "Selected": false,

        "Value": 1015033,

        "Children": []

      },

      {

        "Name": "Servers",

        "Editable": true,

        "Selected": false,

        "Value": 1015039,

        "Children": []

      },

      {

        "Name": "License",

        "Editable": true,

        "Selected": false,

        "Value": 1015083,

        "Children": []

      },

      {

        "Name": "Application Library",

        "Editable": true,

        "Selected": false,

        "Value": 1015292,

        "Children": []

      },

      {

        "Name": "Platform Status",

        "Editable": true,

        "Selected": false,

        "Value": 1029125,

        "Children": []

      }

    ],

    "BrowserPermissions": [],

    "MassActionPermissions": [],

    "AdminPermissions": [

      {

        "Name": "Agent Operations",

        "Editable": true,

        "Selected": false,

        "Value": 504,

        "Children": []

      },

      {

        "Name": "Change Queue Priority",

        "Editable": true,

        "Selected": false,

        "Value": 503,

        "Children": []

      },

      {

        "Name": "Force Logout on User Status",

        "Editable": true,

        "Selected": false,

        "Value": 500,

        "Children": []

      },

      {

        "Name": "Manage Object Types",

        "Editable": true,

        "Selected": false,

        "Value": 103,

        "Children": []

      },

      {

        "Name": "Send Message",

        "Editable": true,

        "Selected": false,

        "Value": 502,

        "Children": []

      },

      {

        "Name": "Use Quick Nav",

        "Editable": true,

        "Selected": true,

        "Value": 177,

        "Children": []

      },

      {

        "Name": "View Audits",

        "Editable": true,

        "Selected": false,

        "Value": 1000031,

        "Children": []

      }

    ],

    "LastModified": "2015-02-22T00:14:51.87"

  }

}
```

The response does not contain any data. Success or failure are indicated by the HTTP status code. For more information, see HTTP status codes .

## Set workspace permissions

Use this Permission Manager service URL to set a group's workspace permissions:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/SetWorkspaceGroupPermissionsAsync
```

The request must include a workspace Artifact ID and a GroupPermissions object containing the workspace permissions set. It is recommended that you first return the GroupPermissions object and then inspect and manipulate the permissions within it.

Click to display JSON response Copy

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
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
941
942
943
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
982
983
984
985
986
987
988
989
990
991
992
993
994
995
996
997
998
999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
1528
1529
1530
1531
1532
1533
1534
1535
1536
1537
1538
1539
1540
1541
1542
1543
1544
1545
1546
1547
1548
1549
1550
1551
1552
1553
1554
1555
1556
1557
1558
1559
1560
1561
1562
1563
1564
1565
1566
1567
1568
1569
1570
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
1588
1589
1590
1591
1592
1593
1594
1595
1596
1597
1598
1599
1600
1601
1602
1603
1604
1605
1606
1607
1608
1609
1610
1611
1612
1613
1614
1615
1616
1617
1618
1619
1620
1621
1622
1623
1624
1625
1626
1627
1628
1629
1630
1631
1632
1633
1634
1635
1636
1637
1638
1639
1640
1641
1642
1643
1644
1645
1646
1647
1648
1649
{

  "workspaceArtifactID": 1234567,

  "groupPermissions": {

    "ArtifactID": 1003663,

    "GroupID": 1036399,

    "ObjectPermissions": [

      {

        "ArtifactGroupingID": 1000037,

        "Name": "Agent Type",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 35,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000028,

        "Name": "Analytics Categorization Result",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 2,

        "ArtifactTypeID": 1000020,

        "ParentArtifactTypeID": 1000021

      },

      {

        "ArtifactGroupingID": 1000029,

        "Name": "Analytics Categorization Set",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000021,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000030,

        "Name": "Analytics Category",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 2,

        "ArtifactTypeID": 1000022,

        "ParentArtifactTypeID": 1000021

      },

      {

        "ArtifactGroupingID": 1000031,

        "Name": "Analytics Example",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 2,

        "ArtifactTypeID": 1000023,

        "ParentArtifactTypeID": 1000021

      },

      {

        "ArtifactGroupingID": 1000023,

        "Name": "Analytics Profile",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000015,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000044,

        "Name": "Application Field Code",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000031,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000007,

        "Name": "Batch",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 2,

        "ArtifactTypeID": 27,

        "ParentArtifactTypeID": 24

      },

      {

        "ArtifactGroupingID": 1000004,

        "Name": "Batch Set",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 24,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000016,

        "Name": "Case Info",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000010,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 6,

        "Name": "Choice",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 7,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000015,

        "Name": "Contacts",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000009,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000036,

        "Name": "Custom Page",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000026,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 9,

        "Name": "Document",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": true,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [

          {

            "PermissionID": 1000002,

            "Name": "Print / Save As PDF",

            "Selected": false

          },

          {

            "PermissionID": 1000005,

            "Name": "Local Access (Download, Copy Text)",

            "Selected": false

          },

          {

            "PermissionID": 1000006,

            "Name": "Redact Document",

            "Selected": true

          },

          {

            "PermissionID": 1000007,

            "Name": "Highlight Document",

            "Selected": true

          },

          {

            "PermissionID": 1000018,

            "Name": "Add Image",

            "Selected": true

          },

          {

            "PermissionID": 1000019,

            "Name": "Delete Image",

            "Selected": false

          }

        ],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 2,

        "ArtifactTypeID": 10,

        "ParentArtifactTypeID": 9

      },

      {

        "ArtifactGroupingID": 1000034,

        "Name": "Event Handler",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 2,

        "ArtifactTypeID": 1000002,

        "ParentArtifactTypeID": 25

      },

      {

        "ArtifactGroupingID": 15,

        "Name": "Field",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [

          {

            "PermissionID": 88,

            "Name": "Add Field Choice By Link",

            "Selected": false

          }

        ],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 14,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 10,

        "Name": "Folder",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 9,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000026,

        "Name": "Imaging Profile",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000018,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000027,

        "Name": "Imaging Set",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000019,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000039,

        "Name": "Install Event Handler",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 40,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 16,

        "Name": "Layout",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 16,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000042,

        "Name": "Lists",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000030,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000000,

        "Name": "Markup Set",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 22,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000043,

        "Name": "Mass Operation",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 2,

        "ArtifactTypeID": 41,

        "ParentArtifactTypeID": 25

      },

      {

        "ArtifactGroupingID": 1000025,

        "Name": "Native Type",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000017,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000033,

        "Name": "Object Rule",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 2,

        "ArtifactTypeID": 33,

        "ParentArtifactTypeID": 25

      },

      {

        "ArtifactGroupingID": 1000005,

        "Name": "Object Type",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 25,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000021,

        "Name": "OCR Profile",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000012,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000022,

        "Name": "OCR Set",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000013,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000040,

        "Name": "Password Bank",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000028,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000041,

        "Name": "Password Entry",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 2,

        "ArtifactTypeID": 1000029,

        "ParentArtifactTypeID": 1000028

      },

      {

        "ArtifactGroupingID": 1000032,

        "Name": "Persistent Highlight Set",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000024,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000017,

        "Name": "PivotProfile",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000011,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 17,

        "Name": "Production",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 17,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000020,

        "Name": "Relativity Application",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000014,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000008,

        "Name": "Relativity Script",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 28,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000035,

        "Name": "Relativity Time Zone",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000025,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000024,

        "Name": "Repeated Content Filter",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000016,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 18,

        "Name": "Report",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 19,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 14,

        "Name": "Search",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 15,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000006,

        "Name": "Search Folder",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 0,

        "ParentArtifactTypeID": -1

      },

      {

        "ArtifactGroupingID": 1000009,

        "Name": "Search Index",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [

          {

            "PermissionID": 119,

            "Name": "Dictionary Access",

            "Selected": false

          }

        ],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 29,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000012,

        "Name": "Search Terms Report",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000006,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000013,

        "Name": "Search Terms Result",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 2,

        "ArtifactTypeID": 1000007,

        "ParentArtifactTypeID": 1000006

      },

      {

        "ArtifactGroupingID": 1000001,

        "Name": "Tab",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 23,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000011,

        "Name": "Transform",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 2,

        "ArtifactTypeID": 1000005,

        "ParentArtifactTypeID": 1000004

      },

      {

        "ArtifactGroupingID": 1000010,

        "Name": "Transform Set",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000004,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 13,

        "Name": "View",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 4,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 1000014,

        "Name": "Work Product",

        "ViewSelected": false,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": true,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": true,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 1,

        "ArtifactTypeID": 1000008,

        "ParentArtifactTypeID": 8

      },

      {

        "ArtifactGroupingID": 5,

        "Name": "Workspace",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": false,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": false,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 0,

        "ArtifactTypeID": 8,

        "ParentArtifactTypeID": -1

      }

    ],

    "TabVisibility": [

      {

        "Name": "Documents",

        "Editable": true,

        "Selected": true,

        "Value": 1034251,

        "Children": []

      },

      {

        "Name": "Summary Reports",

        "Editable": true,

        "Selected": false,

        "Value": 1034253,

        "Children": []

      },

      {

        "Name": "Review Batches",

        "Editable": true,

        "Selected": true,

        "Value": 1035256,

        "Children": []

      },

      {

        "Name": "Administration",

        "Editable": true,

        "Selected": false,

        "Value": 1035260,

        "Children": [

          {

            "Name": "Workspace Details",

            "Editable": true,

            "Selected": false,

            "Value": 1034252,

            "Children": []

          },

          {

            "Name": "Markup Sets",

            "Editable": true,

            "Selected": false,

            "Value": 1034254,

            "Children": []

          },

          {

            "Name": "Production Sets",

            "Editable": true,

            "Selected": false,

            "Value": 1034255,

            "Children": []

          },

          {

            "Name": "Batch Sets",

            "Editable": true,

            "Selected": false,

            "Value": 1035223,

            "Children": []

          },

          {

            "Name": "Object Type",

            "Editable": true,

            "Selected": false,

            "Value": 1035225,

            "Children": []

          },

          {

            "Name": "Fields",

            "Editable": true,

            "Selected": false,

            "Value": 1034256,

            "Children": []

          },

          {

            "Name": "Choices",

            "Editable": true,

            "Selected": false,

            "Value": 1034257,

            "Children": []

          },

          {

            "Name": "Layouts",

            "Editable": true,

            "Selected": false,

            "Value": 1034258,

            "Children": []

          },

          {

            "Name": "Views",

            "Editable": true,

            "Selected": false,

            "Value": 1034259,

            "Children": []

          },

          {

            "Name": "Search Indexes",

            "Editable": true,

            "Selected": false,

            "Value": 1035270,

            "Children": []

          },

          {

            "Name": "Scripts",

            "Editable": true,

            "Selected": false,

            "Value": 1035264,

            "Children": []

          },

          {

            "Name": "Tabs",

            "Editable": true,

            "Selected": false,

            "Value": 1034261,

            "Children": []

          },

          {

            "Name": "History",

            "Editable": true,

            "Selected": false,

            "Value": 1034264,

            "Children": []

          },

          {

            "Name": "Transform Sets",

            "Editable": true,

            "Selected": false,

            "Value": 1035286,

            "Children": []

          },

          {

            "Name": "Relativity Applications",

            "Editable": true,

            "Selected": false,

            "Value": 1036634,

            "Children": []

          },

          {

            "Name": "Persistent Highlight Sets",

            "Editable": true,

            "Selected": false,

            "Value": 1037542,

            "Children": []

          }

        ]

      },

      {

        "Name": "User Status",

        "Editable": true,

        "Selected": false,

        "Value": 1035275,

        "Children": []

      },

      {

        "Name": "Pivot Profiles",

        "Editable": true,

        "Selected": false,

        "Value": 1036455,

        "Children": []

      },

      {

        "Name": "OCR",

        "Editable": true,

        "Selected": false,

        "Value": 1036667,

        "Children": [

          {

            "Name": "OCR Profiles",

            "Editable": true,

            "Selected": false,

            "Value": 1036641,

            "Children": []

          },

          {

            "Name": "OCR Sets",

            "Editable": true,

            "Selected": false,

            "Value": 1036642,

            "Children": []

          }

        ]

      },

      {

        "Name": "Analytics",

        "Editable": true,

        "Selected": false,

        "Value": 1036701,

        "Children": [

          {

            "Name": "Analytics Profiles",

            "Editable": true,

            "Selected": false,

            "Value": 1036702,

            "Children": []

          },

          {

            "Name": "Repeated Content Filters",

            "Editable": true,

            "Selected": false,

            "Value": 1036703,

            "Children": []

          },

          {

            "Name": "Analytics Categorization Set",

            "Editable": true,

            "Selected": false,

            "Value": 1037489,

            "Children": []

          }

        ]

      },

      {

        "Name": "Imaging",

        "Editable": true,

        "Selected": false,

        "Value": 1036759,

        "Children": [

          {

            "Name": "Imaging Profiles",

            "Editable": true,

            "Selected": false,

            "Value": 1036733,

            "Children": []

          },

          {

            "Name": "Imaging Sets",

            "Editable": true,

            "Selected": false,

            "Value": 1036753,

            "Children": []

          },

          {

            "Name": "Native Types",

            "Editable": true,

            "Selected": false,

            "Value": 1036717,

            "Children": []

          },

          {

            "Name": "Password Bank",

            "Editable": true,

            "Selected": false,

            "Value": 1038258,

            "Children": []

          },

          {

            "Name": "Application Field Code",

            "Editable": true,

            "Selected": false,

            "Value": 1038483,

            "Children": []

          }

        ]

      },

      {

        "Name": "Work Product",

        "Editable": true,

        "Selected": false,

        "Value": 1036398,

        "Children": [

          {

            "Name": "Pleadings",

            "Editable": true,

            "Selected": false,

            "Value": 1035405,

            "Children": []

          },

          {

            "Name": "Contacts",

            "Editable": true,

            "Selected": false,

            "Value": 1035429,

            "Children": []

          },

          {

            "Name": "Case Info",

            "Editable": true,

            "Selected": false,

            "Value": 1035439,

            "Children": []

          }

        ]

      },

      {

        "Name": "Custom Pages",

        "Editable": true,

        "Selected": false,

        "Value": 1038010,

        "Children": []

      },

      {

        "Name": "Search Terms Report",

        "Editable": true,

        "Selected": false,

        "Value": 1038279,

        "Children": [

          {

            "Name": "Search Terms Reports",

            "Editable": true,

            "Selected": false,

            "Value": 1035314,

            "Children": []

          },

          {

            "Name": "Search Terms Results",

            "Editable": true,

            "Selected": false,

            "Value": 1038298,

            "Children": []

          }

        ]

      },

      {

        "Name": "Persistent Lists",

        "Editable": true,

        "Selected": false,

        "Value": 1038387,

        "Children": [

          {

            "Name": "Lists",

            "Editable": true,

            "Selected": false,

            "Value": 1038392,

            "Children": []

          }

        ]

      }

    ],

    "BrowserPermissions": [

      {

        "Name": "Folders",

        "Editable": true,

        "Selected": true,

        "Value": 1000032,

        "Children": []

      },

      {

        "Name": "Field Tree",

        "Editable": true,

        "Selected": true,

        "Value": 1000034,

        "Children": []

      },

      {

        "Name": "Advanced & Saved Searches",

        "Editable": true,

        "Selected": false,

        "Value": 1000033,

        "Children": []

      },

      {

        "Name": "Clusters",

        "Editable": true,

        "Selected": false,

        "Value": 104,

        "Children": []

      }

    ],

    "MassActionPermissions": [

      {

        "Name": "Cluster",

        "Editable": true,

        "Selected": false,

        "Value": 94,

        "Children": []

      },

      {

        "Name": "Convert",

        "Editable": true,

        "Selected": false,

        "Value": 1000219,

        "Children": []

      },

      {

        "Name": "Export to File",

        "Editable": true,

        "Selected": true,

        "Value": 1000035,

        "Children": []

      },

      {

        "Name": "Copy",

        "Editable": true,

        "Selected": false,

        "Value": 107,

        "Children": []

      },

      {

        "Name": "Delete",

        "Editable": true,

        "Selected": false,

        "Value": 1000022,

        "Children": []

      },

      {

        "Name": "Edit",

        "Editable": true,

        "Selected": false,

        "Value": 1000001,

        "Children": []

      },

      {

        "Name": "Images",

        "Editable": true,

        "Selected": false,

        "Value": 1000025,

        "Children": []

      },

      {

        "Name": "Move",

        "Editable": true,

        "Selected": false,

        "Value": 1000021,

        "Children": []

      },

      {

        "Name": "Print Image",

        "Editable": true,

        "Selected": false,

        "Value": 1000026,

        "Children": []

      },

      {

        "Name": "Produce",

        "Editable": true,

        "Selected": false,

        "Value": 1000023,

        "Children": []

      },

      {

        "Name": "Replace",

        "Editable": true,

        "Selected": false,

        "Value": 1000024,

        "Children": []

      },

      {

        "Name": "Process Transcript",

        "Editable": true,

        "Selected": false,

        "Value": 100,

        "Children": []

      },

      {

        "Name": "Send To Case Map",

        "Editable": true,

        "Selected": false,

        "Value": 1000028,

        "Children": []

      },

      {

        "Name": "Tally/Sum/Average",

        "Editable": true,

        "Selected": true,

        "Value": 1000027,

        "Children": []

      }

    ],

    "AdminPermissions": [

      {

        "Name": "Allow dtSearch Index Swap",

        "Editable": true,

        "Selected": false,

        "Value": 141,

        "Children": []

      },

      {

        "Name": "Allow Export",

        "Editable": true,

        "Selected": false,

        "Value": 159,

        "Children": []

      },

      {

        "Name": "Allow Import",

        "Editable": true,

        "Selected": false,

        "Value": 158,

        "Children": []

      },

      {

        "Name": "Assign Batches",

        "Editable": true,

        "Selected": false,

        "Value": 101,

        "Children": []

      },

      {

        "Name": "Delete Object Dependencies",

        "Editable": true,

        "Selected": false,

        "Value": 140,

        "Children": []

      },

      {

        "Name": "Download Relativity Desktop Client",

        "Editable": true,

        "Selected": false,

        "Value": 126,

        "Children": []

      },

      {

        "Name": "Manage Object Types",

        "Editable": true,

        "Selected": false,

        "Value": 103,

        "Children": []

      },

      {

        "Name": "Manage Relativity Applications",

        "Editable": true,

        "Selected": false,

        "Value": 138,

        "Children": []

      },

      {

        "Name": "Modify System Keyboard Shortcuts",

        "Editable": true,

        "Selected": false,

        "Value": 139,

        "Children": []

      },

      {

        "Name": "Override Production Restrictions",

        "Editable": true,

        "Selected": false,

        "Value": 127,

        "Children": []

      },

      {

        "Name": "Use Pivot/Chart",

        "Editable": true,

        "Selected": true,

        "Value": 120,

        "Children": []

      },

      {

        "Name": "Use Quick Nav",

        "Editable": true,

        "Selected": true,

        "Value": 177,

        "Children": []

      },

      {

        "Name": "Use Sampling",

        "Editable": true,

        "Selected": false,

        "Value": 1000198,

        "Children": []

      },

      {

        "Name": "View All Audits",

        "Editable": true,

        "Selected": false,

        "Value": 1000031,

        "Children": []

      },

      {

        "Name": "View Batch Pane",

        "Editable": true,

        "Selected": false,

        "Value": 1000046,

        "Children": []

      },

      {

        "Name": "View Image Thumbnails",

        "Editable": true,

        "Selected": false,

        "Value": 1000172,

        "Children": []

      },

      {

        "Name": "View Images Hidden for QC Review",

        "Editable": true,

        "Selected": false,

        "Value": 157,

        "Children": []

      },

      {

        "Name": "View User Status",

        "Editable": true,

        "Selected": false,

        "Value": 125,

        "Children": []

      },

      {

        "Name": "View User's Personal Items",

        "Editable": true,

        "Selected": false,

        "Value": 501,

        "Children": []

      },

      {

        "Name": "View Workspace Details",

        "Editable": true,

        "Selected": false,

        "Value": 124,

        "Children": []

      }

    ],

    "LastModified": "2015-02-22T00:27:21.443"

  }

}
```

The response does not contain any data. Success or failure are indicated by the HTTP status code. For more information, see HTTP status codes .

## Get item-level security

Use these Permission Manager service endpoints to check if item-level security is enabled:

- GetItemLevelSecurityAsync - returns item-level security settings for a specified artifact.

- GetItemLevelSecurityListAsync - returns item-level security settings for a list of artifacts.

### GetItemLevelSecurityAsync

Use this Permission Manager service URL to check if item-level security is enabled for a single artifact:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetItemLevelSecurityAsync
```

The request must include Artifact IDs of the workspace and the item:

Copy

```text
1
2
3
4
{

  "workspaceArtifactID": 13758822,

  "ArtifactID": 1038413

}
```

The response indicates whether item-level security is enabled:

Copy

```text
1
2
3
4
5
{

  "ArtifactID": 1038593,

  "Enabled": false,

  "LastModified": "2015-02-24T02:17:14.07"

}
```

### GetItemLevelSecurityListAsync

Use this Permission Manager service URL to check if item-level security is enabled for multiple artifacts:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetItemLevelSecurityListAsync
```

The request must include Artifact IDs of the workspace and a list of ArtifactIDs of the items:

Copy

```text
1
2
3
4
{

  "workspaceArtifactID": -1,

  "artifactIDs": [13757815, 13766087, 13766089]

}
```

The response indicates whether item-level security is enabled for each artifact:

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
{

  "13757815": {

    "ArtifactID": 13757815,

    "Enabled": true,

    "LastModified": "2015-08-11T20:17:57.463"

  },

  "13766087": {

    "ArtifactID": 13766087,

    "Enabled": false,

    "LastModified": "2015-08-11T20:17:57.463"

  },

  "13766089": {

    "ArtifactID": 13766089,

    "Enabled": true,

    "LastModified": "2015-08-11T20:17:57.463"

  }

}
```

## Set item-level security

Use this Permission Manager service URL to enable or disable item-level security:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/SetItemLevelSecurityAsync
```

The request must include Artifact IDs of the workspace and the item, and a valid itemLevelSecurity object:

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
{

  "workspaceArtifactID": 13758841,

  "itemLevelSecurity": {

    "ArtifactID": 1038593,

    "Enabled": true,

    "LastModified": "2015-02-24T02:17:14.07"

  }

}
```

Note that the value of the LastModified property must match the existing value on the itemLevelSecurity object. You can retrieve it using the GetItemLevelSecurityAsync or GetItemLevelSecurityListAsync endpoints described above.

The response does not contain any data. Success or failure are indicated by the HTTP status code. For more information, see HTTP status codes .

## Set item permissions

If security is enabled, use this Permission Manager service URL to set item permission:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/SetItemGroupPermissionsAsync
```

The request must include a workspace Artifact ID and a GroupPermissions object containing the item permissions set. It is recommended that you first return GroupPermissions object and then inspect and manipulate the permissions within it. Note that the permissions can be different depending on the object type of the item. The following is an example of Document permissions.

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
{

  "workspaceArtifactID": 1234567,

  "artifactID": 2334435,

  "groupPermissions": {

    "ArtifactID": 1038413,

    "GroupID": 1036399,

    "ObjectPermissions": [

      {

        "ArtifactGroupingID": 9,

        "Name": "Document",

        "ViewSelected": true,

        "EditEditable": true,

        "EditSelected": true,

        "DeleteEditable": true,

        "DeleteSelected": false,

        "AddEditable": false,

        "AddSelected": false,

        "EditSecurityEditable": true,

        "EditSecuritySelected": false,

        "CanRemovePermissions": false,

        "SubPermissions": [

          {

            "PermissionID": 1000002,

            "Name": "Print / Save As PDF",

            "Selected": false

          },

          {

            "PermissionID": 1000005,

            "Name": "Local Access (Download, Copy Text)",

            "Selected": false

          },

          {

            "PermissionID": 1000006,

            "Name": "Redact Document",

            "Selected": true

          },

          {

            "PermissionID": 1000007,

            "Name": "Highlight Document",

            "Selected": true

          },

          {

            "PermissionID": 1000018,

            "Name": "Add Image",

            "Selected": true

          },

          {

            "PermissionID": 1000019,

            "Name": "Delete Image",

            "Selected": false

          }

        ],

        "CustomPermissions": [],

        "HasChildPermissions": false,

        "HierarchyIndent": 2,

        "ArtifactTypeID": 10,

        "ParentArtifactTypeID": 9

      }

    ],

    "TabVisibility": [],

    "BrowserPermissions": [],

    "MassActionPermissions": [],

    "AdminPermissions": [],

    "LastModified": "2015-02-22T00:34:43.813"

  }

}
```

The response does not contain any data. Success or failure are indicated by the HTTP status code. For more information, see HTTP status codes .

## Get admin group users

Use this Permission Manager service URL to return a list of users in a group with admin permissions:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetAdminGroupUsersAsync
```

The request must specify the group:

Copy

```text
1
2
3
4
5
{

  "group": {

    "ArtifactID": 1015029

  }

}
```

The response contains the list of users in the group:

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
[

  {

    "ArtifactID": 13758829,

    "Name": "Doe, Jane"

  },

  {

    "ArtifactID": 13758839,

    "Name": "Doe, John"

  },

  {

    "ArtifactID": 13758845,

    "Name": "Sample, JC"

  }

]
```

## Get workspace group users

Use this Permission Manager service URL to return a list of users in a group with workspace permissions:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetWorkspaceGroupUsersAsync
```

The request must specify the workspace Artifact ID and the group:

Copy

```text
1
2
3
4
5
6
{

  "workspaceArtifactId": 13758822,

  "group": {

    "ArtifactID": 1015029

  }

}
```

The response contains the list of users in the group:

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
[

  {

    "ArtifactID": 13758829,

    "Name": "Doe, Jane"

  },

  {

    "ArtifactID": 13758839,

    "Name": "Doe, John"

  },

  {

    "ArtifactID": 13758845,

    "Name": "Sample, JC"

  }

]
```

## Get item group users

Use this Permission Manager service URL to return a list of users in a group with item permissions:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetItemGroupUsersAsync
```

The request must specify the Artifact IDs, the item, and the group:

Copy

```text
1
2
3
4
5
6
7
{

  "workspaceArtifactId": 13758822,

  "artifactID": 1038524,

  "group": {

    "ArtifactID": 1015029

  }

}
```

The response contains the list of users in the group:

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
[

  {

    "ArtifactID": 13758829,

    "Name": "Doe, Jane"

  },

  {

    "ArtifactID": 13758839,

    "Name": "Doe, John"

  },

  {

    "ArtifactID": 13758845,

    "Name": "Sample, JC"

  }

]
```

## Query permissions

Use this Permission Manager service URL to query permissions:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/QueryAsync
```

The request must specify the workspace Artifact ID, the query, and optionally the number of results to return as the length property. To query admin permissions, specify -1 as workspace Artifact ID. The following is an example of a query request for view permissions with the result set sorted by ArtifactID in descending order.

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
{

  "workspaceArtifactID": 13758822,

  "query": {

    "Condition": "'PermissionType' == 'View'",

    "Sorts": [

      {

        "FieldIdentifier": {

          "Name": "PermissionID"

        },

        "Order": 0,

        "Direction": 1

      }

    ]

  },

  "length":5

}
```

If more results are available than initially specified in the length property, the query returns a token value that is not null. The results can subsequently be retrieved by a call to the QuerySubsetAsync operation.

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/QuerySubsetAsync
```

Note that the QuerySubsetAsync request can specify the starting index of the result subset and the number of results to be returned.

Copy

```text
1
2
3
4
5
{

  "queryToken": "a5079c32-e080-473d-846e-941ef6a5f086",

  "start": 6,

  "length": 5

}
```

To return all permissions in a workspace or all admin permissions, omit the Condition property in the Query object. When the length parameter is not specified, its value defaults to 0, and the number of returned results defaults to the Configuration Table value of PDVDefaultQueryCacheSize of 10000. For more information, see Searching Relativity .

You can use this query to generate a list of the PermissionIDs and permission Names for your instance. PermissionIDs vary from one Relativity instance to another.

The response is a collection of permissions.

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
{

  "QueryToken": "614b4e40-8c67-47cb-b09d-57b150b8167e",

  "TotalCount": 5,

  "Success": true,

  "Message": "",

  "Results": [

    {

      "Success": true,

      "Artifact": {

        "Name": "Add ProductionDataSource",

        "ArtifactType": {

          "ID": 1000034,

          "Guids": [

            "7528c416-3706-4909-8805-edddcf75542d"

          ]

        },

        "PermissionID": 1000240,

        "PermissionType": {

          "ID": 6,

          "Name": "Add"

        }

      },

      "Message": "",

      "WarningMessages": []

    },

    {

      "Success": true,

      "Artifact": {

        "Name": "Secure ProductionDataSource",

        "ArtifactType": {

          "ID": 1000034,

          "Guids": [

            "7528c416-3706-4909-8805-edddcf75542d"

          ]

        },

        "PermissionID": 1000239,

        "PermissionType": {

          "ID": 4,

          "Name": "Secure"

        }

      },

      "Message": "",

      "WarningMessages": []

    },

    {

      "Success": true,

      "Artifact": {

        "Name": "Delete ProductionDataSource",

        "ArtifactType": {

          "ID": 1000034,

          "Guids": [

            "7528c416-3706-4909-8805-edddcf75542d"

          ]

        },

        "PermissionID": 1000238,

        "PermissionType": {

          "ID": 3,

          "Name": "Delete"

        }

      },

      "Message": "",

      "WarningMessages": []

    },

    {

      "Success": true,

      "Artifact": {

        "Name": "Edit ProductionDataSource",

        "ArtifactType": {

          "ID": 1000034,

          "Guids": [

            "7528c416-3706-4909-8805-edddcf75542d"

          ]

        },

        "PermissionID": 1000237,

        "PermissionType": {

          "ID": 2,

          "Name": "Edit"

        }

      },

      "Message": "",

      "WarningMessages": []

    },

    {

      "Success": true,

      "Artifact": {

        "Name": "View ProductionDataSource",

        "ArtifactType": {

          "ID": 1000034,

          "Guids": [

            "7528c416-3706-4909-8805-edddcf75542d"

          ]

        },

        "PermissionID": 1000236,

        "PermissionType": {

          "ID": 1,

          "Name": "View"

        }

      },

      "Message": "",

      "WarningMessages": []

    }

  ]

}
```

## Read a single permission

If you already know the permission ID, for example, by performing a query, you can quickly read the permission without constructing a query.

Use this Permission Manager service URL to get selected permissions for the current user:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetPermissionSelectedAsync
```

The request must specify the workspace Artifact ID and the permission ID.

Copy

```text
1
2
3
4
{

  "workspaceArtifactID": 13758822,

  "permissionID": 1000238

}
```

The response represents a single permissions object.

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
{

  "Name": "Delete ProductionDataSource",

  "ArtifactType": {

    "ID": 1000034,

    "Guids": [

      "7528c416-3706-4909-8805-edddcf75542d"

    ]

  },

  "PermissionID": 1000238,

  "PermissionType": {

    "ID": 3,

    "Name": "Delete"

  }

}
```

## Get selected permissions for current user

Permission Manager service provides the following endpoints for returning the specified permissions for the current user:

- GetPermissionSelectedAsync - returns a collection of permission values for the current user. You can also specify an ArtifactID to return permissions of an item with security enabled.

- GetPermissionSelectedListAsync - is similar to GetPermissionSelectedAsync, but instead of only returning permissions for one artifact, you can pass in a list of ArtifactIDs to return a dictionary that maps the ArtifactID to the permissions.

### GetPermissionSelectedAsync

Use this Permission Manager service URL to get selected permissions for the current user:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetPermissionSelectedAsync
```

The request must specify the workspace Artifact ID and a collection of permissions objects. The following is an example of a payload to check if the current user has the View, Add, Delete, and Update permissions for documents. Note that the permissions are identified by the combination of the artifact type ID (10) and permission type ID (1, 2, 3, and 6).

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
{

  "workspaceArtifactID": 13772405,

  "permissions": [

   {

    "ArtifactType": {

      "ID": 10

    },



    "PermissionType": {

      "ID": 1

    }

  },

  {

    "ArtifactType": {

      "ID": 10

    },



    "PermissionType": {

      "ID": 2

    }

  },

  {

    "ArtifactType": {

      "ID": 10

    },



    "PermissionType": {

      "ID": 3

    }

  },

  {

    "ArtifactType": {

      "ID": 10

    },



    "PermissionType": {

      "ID": 6

    }

  },

  ]

}
```

To return permissions for an object with item-level security enabled, you must also pass in the Artifact ID of the object. The following is the payload for returning the edit permissions for an agent security enabled. Note that because an agent is an admin-level object, -1 is specified as workspace ArtifactID.

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
{

  "workspaceArtifactID": -1,

  "permissions": [

    {

      "ArtifactType": {

        "ID": 20

      },

      "PermissionType": {

        "ID": 2

      }

    }

  ],

  "ArtifactID": 13757815

}
```

The "Selected" attribute of the objects returned by the response indicates whether the specified permissions are enabled for the current user.

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
[

  {

    "Selected": true,

    "Name": "View Document",

    "ArtifactType": {

      "ID": 10,

      "Guids": [

        "15c36703-74ea-4ff8-9dfb-ad30ece7530d"

      ]

    },

    "PermissionID": 44,

    "PermissionType": {

      "ID": 1,

      "Name": "View"

    }

  },

  {

    "Selected": true,

    "Name": "Edit Document",

    "ArtifactType": {

      "ID": 10,

      "Guids": [

        "15c36703-74ea-4ff8-9dfb-ad30ece7530d"

      ]

    },

    "PermissionID": 45,

    "PermissionType": {

      "ID": 2,

      "Name": "Edit"

    }

  },

  {

    "Selected": true,

    "Name": "Delete Document",

    "ArtifactType": {

      "ID": 10,

      "Guids": [

        "15c36703-74ea-4ff8-9dfb-ad30ece7530d"

      ]

    },

    "PermissionID": 46,

    "PermissionType": {

      "ID": 3,

      "Name": "Delete"

    }

  },

  {

    "Selected": true,

    "Name": "Add Document",

    "ArtifactType": {

      "ID": 10,

      "Guids": [

        "15c36703-74ea-4ff8-9dfb-ad30ece7530d"

      ]

    },

    "PermissionID": 43,

    "PermissionType": {

      "ID": 6,

      "Name": "Add"

    }

  }

]
```

### GetPermissionSelectedListAsync

Use this Permission Manager service URL to get the current user's permissions to specified artifacts:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetPermissionSelectedListAsync
```

The request must specify the workspace Artifact ID, a collection of permissions objects, and a collection of ArtifactIDs of Relativity objects. The following is an example of a payload to check if the current user has the View, Add, Delete, and Update permissions for agents. Note that because an agent is an admin-level object, -1 is specified as workspace ArtifactID and the permissions are identified by the combination of the artifact type ID (20) and permission type ID (1, 2, 3, and 6).

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
{

  "workspaceArtifactID": -1,

  "permissions": [

    {

      "ArtifactType": {

        "ID": 20

      },

      "PermissionType": {

        "ID": 1

      }

    },

    {

      "ArtifactType": {

        "ID": 20

      },

      "PermissionType": {

        "ID": 2

      }

    },

    {

      "ArtifactType": {

        "ID": 20

      },

      "PermissionType": {

        "ID": 3

      }

    },

    {

      "ArtifactType": {

        "ID": 20

      },

      "PermissionType": {

        "ID": 6

      }

    }

  ],

  "artifactIDs": [13757815, 13757821,13766087]

}
```

The response is a dictionary of permissions values for each ArtifactID. The "Selected" attribute indicates whether the specified permissions are enabled for the current user.

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
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
{

  "13757815": [

    {

      "Selected": true,

      "Name": "View Agent",

      "ArtifactType": {

        "ID": 20,

        "Guids": []

      },

      "PermissionID": 147,

      "PermissionType": {

        "ID": 1,

        "Name": "View"

      }

    },

    {

      "Selected": true,

      "Name": "Edit Agent",

      "ArtifactType": {

        "ID": 20,

        "Guids": []

      },

      "PermissionID": 148,

      "PermissionType": {

        "ID": 2,

        "Name": "Edit"

      }

    },

    {

      "Selected": true,

      "Name": "Delete Agent",

      "ArtifactType": {

        "ID": 20,

        "Guids": []

      },

      "PermissionID": 149,

      "PermissionType": {

        "ID": 3,

        "Name": "Delete"

      }

    },

    {

      "Selected": true,

      "Name": "Add Agent",

      "ArtifactType": {

        "ID": 20,

        "Guids": []

      },

      "PermissionID": 151,

      "PermissionType": {

        "ID": 6,

        "Name": "Add"

      }

    }

  ],

  "13757821": [

    {

      "Selected": true,

      "Name": "View Agent",

      "ArtifactType": {

        "ID": 20,

        "Guids": []

      },

      "PermissionID": 147,

      "PermissionType": {

        "ID": 1,

        "Name": "View"

      }

    },

    {

      "Selected": true,

      "Name": "Edit Agent",

      "ArtifactType": {

        "ID": 20,

        "Guids": []

      },

      "PermissionID": 148,

      "PermissionType": {

        "ID": 2,

        "Name": "Edit"

      }

    },

    {

      "Selected": true,

      "Name": "Delete Agent",

      "ArtifactType": {

        "ID": 20,

        "Guids": []

      },

      "PermissionID": 149,

      "PermissionType": {

        "ID": 3,

        "Name": "Delete"

      }

    },

    {

      "Selected": true,

      "Name": "Add Agent",

      "ArtifactType": {

        "ID": 20,

        "Guids": []

      },

      "PermissionID": 151,

      "PermissionType": {

        "ID": 6,

        "Name": "Add"

      }

    }

  ],

  "13766087": [

    {

      "Selected": true,

      "Name": "View Agent",

      "ArtifactType": {

        "ID": 20,

        "Guids": []

      },

      "PermissionID": 147,

      "PermissionType": {

        "ID": 1,

        "Name": "View"

      }

    },

    {

      "Selected": true,

      "Name": "Edit Agent",

      "ArtifactType": {

        "ID": 20,

        "Guids": []

      },

      "PermissionID": 148,

      "PermissionType": {

        "ID": 2,

        "Name": "Edit"

      }

    },

    {

      "Selected": true,

      "Name": "Delete Agent",

      "ArtifactType": {

        "ID": 20,

        "Guids": []

      },

      "PermissionID": 149,

      "PermissionType": {

        "ID": 3,

        "Name": "Delete"

      }

    },

    {

      "Selected": true,

      "Name": "Add Agent",

      "ArtifactType": {

        "ID": 20,

        "Guids": []

      },

      "PermissionID": 151,

      "PermissionType": {

        "ID": 6,

        "Name": "Add"

      }

    }

  ]

}
```

## Get selected permissions for a group

Use this Permission Manager service URL to get selected permissions for a specified group:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/GetPermissionSelectedforGroupAsync
```

The request must specify the workspace Artifact ID, a collection of permissions objects, and the group. The following is an example of a payload to check if the group has the Add permissions for documents.

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
{



  "workspaceArtifactID": 13772405,

  "permissions": [

  {

    "ArtifactType": {

      "ID": 10

    },



    "PermissionType": {

      "ID": 6

    }

  }

  ],

  "group": {"ArtifactID": 1015028}

}
```

To return permissions for an object with item-level security enabled, you must also pass in the Artifact ID of the object. The following is the payload for returning a groups edit permissions for an agent with security enabled.

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
{

  "workspaceArtifactID": -1,

  "permissions": [

    {

      "ArtifactType": {

        "ID": 20

      },

      "PermissionType": {

        "ID": 2

      }

    }

  ],

  "group": {

    "ArtifactID": 1015028

  },

  "ArtifactID": 13757815

}
```

The "Selected" attribute of the objects returned by the response indicates whether the specified permissions are enabled for the group.

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
[

  {

    "Selected": false,

    "Name": "Edit Agent",

    "ArtifactType": {

      "ID": 20,

      "Guids": []

    },

    "PermissionID": 148,

    "PermissionType": {

      "ID": 2,

      "Name": "Edit"

    }

  }

]
```

## Set selected permissions for a group

Use this Permission Manager service URL to set selected permissions for a group:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/SetPermissionSelectedforGroupAsync
```

The request must specify the workspace Artifact ID, a collection of permissionValues objects, and the group. The permissionsValues objects must identify the permission and specify whether the permission is enabled (selected). The following is an example of a payload to disable the edit and delete document permissions for a group.

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
{

  "workspaceArtifactID": 13772405,

  "permissionValues": [



    {

      "PermissionID": 45,

      "Selected": false

    },

        {

      "PermissionID": 46,

      "Selected": false

    }

  ],

  "group": {

    "ArtifactID": 13772407

  }

}
```

To set selected permissions for an object with item-level security enabled, you must also pass in the Artifact ID of the object. The following is the payload for setting a group's edit permissions for an agent with security enabled. Note that the group must be already associated with the item.

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
{

  "workspaceArtifactID": -1,

  "permissionValues": [

    {

      "PermissionID": 148,

      "Selected": true

    }

  ],

  "group": {

    "ArtifactID": 1015028

  },

  "ArtifactID": 13757815

}
```

The response does not contain any data. Success or failure is indicated by the HTTP status code. For more information, see HTTP status codes .

## Create a custom permission

Use this Permission Manager service URL to create a custom permission for a Relativity Dynamic Object (RDO):

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/CreateSingleAsync
```

The request must include a valid JSON representation of a permission. The ArtifactType ID must match the ArtifactType ID of the RDO, and the PermissionType of "Custom" must be specified.

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
{

  "workspaceArtifactID": 13772535,

  "permissionDTO": {

    "Name": "Additional Comments",

    "ArtifactType": {

      "ID": 1000035

    },

    "PermissionType": {

      "ID": 11,

      "Name": "Custom"

    }

  }

}
```

The response is the ID of the created custom permission.

## Update a custom permission

Use this Permission Manager service URL to update a custom permission for an RDO:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/CreateSingleAsync
```

The request must identify the permission by Permission ID and include an updated permission name.

Copy

```text
1
2
3
4
5
6
7
{

  "workspaceArtifactID": 13772535,

  "permissionDTO": {

    "Name": "Reviewer Notes",

    "PermissionID": 1000251

  }

}
```

The response does not contain any data. Success or failure are indicated by the HTTP status code. For more information, see HTTP status codes .

## Delete a custom permission

Use this Permission Manager service URL to delete a custom permission:

Copy

```text
1
<host>/Relativity.REST/api/Relativity.Services.Permission.IPermissionModule/Permission%20Manager/CreateSingleAsync
```

The request must identify include the workspace Artifact ID and the permission the permission ID.

Copy

```text
1
2
3
4
{

  "workspaceArtifactID": 13772535,

  "permissionID": 1000251

}
```

The response does not contain any data. Success or failure are indicated by the HTTP status code. For more information, see HTTP status codes .

On this page

- Permission Manager (REST)

- Client code sample

- Get admin groups

- Get workspace groups

- Get item groups

- Add and remove admin groups

- Add and remove workspace groups

- Add and remove item groups

- Get admin permissions

- Get workspace permissions

- Get item permissions

- Set admin permissions

- Set workspace permissions

- Get item-level security

- GetItemLevelSecurityAsync

- GetItemLevelSecurityListAsync

- Set item-level security

- Set item permissions

- Get admin group users

- Get workspace group users

- Get item group users

- Query permissions

- Read a single permission

- Get selected permissions for current user

- GetPermissionSelectedAsync

- GetPermissionSelectedListAsync

- Get selected permissions for a group

- Set selected permissions for a group

- Create a custom permission

- Update a custom permission

- Delete a custom permission


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


#### Additional Resources

Developer Group GitHub Release Notes NuGet

- © Relativity

- Privacy and Cookies

- Terms of Use

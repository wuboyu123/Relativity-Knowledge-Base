---
title: "Pivot Manager (REST)"
url: https://platform.relativity.com/Server2025/Content/BD_Pivot/Pivot_Manager_service.htm
collection: developer
fetched_at: 2026-06-22T06:30:25+00:00
sha256: 316f8df53653931037bea96d3da8c05c0aec4711240beb9caf645a3083417f09
---

Pivot Manager (REST)

# Pivot Manager (REST)

The Relativity REST API includes a Pivot Manager service that provides operations for working with custom Pivot queries and Pivot profiles. You can use the service to create and run custom Pivot queries and to read and run queries that are based on existing Pivot profiles. The supported operations are equivalent to the supported methods for interacting with Pivot objects in the Relativity Services API. Unlike the Services API however, the Pivot Manager service doesn’t support use of progress indicators or cancellation tokens.

Note that the Pivot Manager service doesn’t provide operations for creating, updating, or deleting Pivot queries that persist in Relativity. This means that you can use the service to create and run a custom query but you can’t store and subsequently update or delete the query or query results in Relativity. Similarly, you can use the service to read an existing Pivot profile and run a query that’s based on the profile, but you can’t create, update, or delete a Pivot profile. Overall, the service is designed to help you transfer data to other applications and tools, such as a third-party software application or web-based visualization tool, for deeper analysis and reporting. For example, you might use the service to implement a Pivot query as part of a larger solution that captures query results, writes the results to a specified table, object, or other location, and then manipulates the results in that location.

## Pivot fundamentals

To interact with the Pivot Manager service, you send HTTP(S) requests that use the POST method and specify query conditions in the body of the request.

- Set the {versionNumber} placeholder to the version of the REST API that you want to use, using the format lowercase v and the version number, for example v1 or v2

- Set other path parameters in the URLs to the Artifact ID of a given entity, for example setting {workspaceID} to the Artifact ID of a workspace.

To indicate the admin-level context, set the {workspaceID} path parameter to -1.

Set the path parameters as follows:

- {versionNumber} to the version of the service, such as v1.

- {workspaceID} to the Artifact ID of the workspace that contains the index.

All Pivot requests use the following base URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-pivot/{versionNumber}/workspaces/{workspaceID}/
```

For example, use the following URL to create and run a custom Pivot query:

Copy

```text
1
<host>/Relativity.REST/api/relativity-pivot/{versionNumber}/workspaces/{workspaceID}/queries
```

Or use the following URL to read and run a query based on a Pivot profile:

Copy

```text
1
<host>/Relativity.REST/api/relativity-pivot/{versionNumber}/workspaces/{workspaceID}/profiles/{pivotProfileID}/execute
```

Note that the base URL format for the Pivot Manager service is different from most other Relativity REST services.

Like other query-based services of the Relativity REST API, request bodies and server responses for the Pivot Manager service are sent in JSON payloads. The body of a POST request for a query includes a JSON representation of fields, conditions, and other parameters for the query. The body of a response returns all the query results as a single result set; the Pivot Service Manager doesn’t provide built-in support for paging. For information about the options and syntax that you can use for Pivot and other query services in the Relativity REST API, see Query for resources .

### Fields

The Pivot Manager service uses a combination of unique fields and fields that are common to the Relativity REST API. The following table lists and describes the required fields for the Pivot Manager service and indicates whether each field is common to the REST API or specific to a type of Pivot query.

Field Type Description Scope

ArtifactTypeID Number The Artifact Type identifier of the type of DTO to query—for example, “10” for documents. Common

GroupBy Object The view field identifier, Artifact identifier, GUID, or name of the field to use for grouping data. Custom Pivot queries only

GroupByDateGrouping Number The calendar-based time interval to use when calculating data for the GroupBy field, if the GroupBy field is a Date field:

0 = Day, month, and year

1 = Month

2 = Year

3 = Month and year

Custom Pivot queries only

objectSetQuery Object The name of a query that defines the criteria that objects or documents must meet to be included in the Pivot query. To query all objects or documents in a workspace, don’t specify a value for the condition of this field. Common

PivotOn Object The view field identifier, Artifact identifier, GUID, or name of the field to use for pivoting data. Custom Pivot queries only

PivotOnDateGrouping Number The calendar-based time interval to use when calculating data for the PivotOn field, if the PivotOn field is a Date field:

0 = Day, month, and year

1 = Month

2 = Year

3 = Month and year

Custom Pivot queries only

pivotProfileId Number The Artifact identifier of the Pivot profile to read and run. Profile-based queries only

RawDataOnly Boolean Whether to apply a Pivot view to query results. If “true”, only the data is returned. Custom and profile-based queries

Timeout Number The maximum amount of time, in seconds, to run the query before timing out. Custom and profile-based queries

Toggles Object The Toggles property on a Pivot profile contains various options that control how data in a chart is displayed. For example, these options control the display of labels, blank values, sub-charts, and others. Custom and profile-based queries

workpsaceId Number The Artifact identifier of the workspace to query. Common

Before you can use any type of field to group data in a Pivot query, the field must be enabled for grouping. Similarly, a field must be enabled for pivot before you can use it to pivot data. In addition, you can pivot data by using a Date field only if you also use a Date field to group data, and you can pivot data by month only if you also group data by year. For information about getting a list of workspace fields that you can use to group or pivot data, see Helper operations .

Note that you must have permission to view a field before you can use it in a Pivot query. Otherwise, an error occurs when you try to run the query because the Pivot Service Manager uses the permission settings of the active user account.

### HTTP headers and status codes

The Pivot Manager service uses the same HTTP(S) headers and status codes as other services in the Relativity REST API. For details about required headers and fields, see HTTP headers . For details about HTTP status codes, see HTTP status codes in Relativity REST APIs .

## Create a Pivot profile

To create a Pivot profile, send a request to this URL for the Pivot Manager service:

Copy

```text
1
<host>/Relativity.REST/api/relativity-pivot/{versionNumber}/workspaces/{workspaceID}/profiles
```

The request includes the fields listed in the following sample JSON code. For more information about these fields, see Pivot profiles on the Relativity Documentation site.

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
{

  "workspaceId": 1015337,

  "profile": {

    "Name": "Create",

    "SortOn": "GrandTotal",

    "SortOrder": "Ascending",

    "PageSize": 10,

    "SwitchSeries": "false",

    "Toggles": {

      "ShowBlankValues": false,

      "ShowLegend": true

      "ShowSubChart": true

    },

    "ObjectType": {

      "Name": "Document"

    },

    "GroupByField": {

      "ArtifactID": 1035357

    },

    "PivotOnField": {

      "ArtifactID": 1035351

    },

    "ChartType": "Bar",

    "ChartOrientation": "Vertical"

  }

}
```

The response returns a JSON object with the fields set in the new Pivot profile.

View a JSON response for a new Pivot profile Copy

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
{

  "ID": 0,

  "GroupByField": {

    "ArtifactID": 0,

    "ViewFieldID": 0,

    "Guids": [

      "string"

    ],

    "Name": "string"

  },

  "GroupByDateTimePart": "Date",

  "PivotOnField": {

    "ArtifactID": 0,

    "ViewFieldID": 0,

    "Guids": [

      "string"

    ],

    "Name": "string"

  },

  "PivotOnDateTimePart": "Date",

  "GroupByResultLimit": "All",

  "GroupByResultLimitValue": 0,

  "PivotOnResultLimit": "All",

  "PivotOnResultLimitValue": 0,

  "ChartType": "Bar",

  "ChartOrientation": "Horizontal",

  "SortOn": "GrandTotal",

  "SortOrder": "Ascending",

  "Toggles": {

    "ShowBlankValues": true,

    "ShowGrandTotal": true,

    "ShowLegend": true,

    "RotateLabels": true,

    "StaggerLabels": true,

    "ShowLabels": true,

    "ShowSubChart": true

  },

  "PageSize": 0,

  "SwitchSeries": true,

  "ObjectType": {

    "ArtifactTypeID": 0,

    "Name": "string",

    "ArtifactID": 0,

    "Guids": [

      "string"

    ]

  },

  "Name": "string"

}
```

## Read a Pivot profile

To read and run a query based on a Pivot profile, send a request to the following Pivot Manager service URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-pivot/{versionNumber}/workspaces/{workspaceID}/profiles/{pivotProfileID}/execute
```

Ensure that the request includes required headers for the Relativity REST API and required fields for the Pivot Manager service. The required fields are: workspaceId, pivotProfileId, and objectSetQuery.

In the following example, a client reads and runs a query based on a Pivot profile. The profile is stored in a workspace that has the Artifact identifier value “1032131”. The profile has the Artifact identifier value “1081794”. The query isn’t limited to a subset of documents or objects in the workspace, as indicated by a Null value for the objectSetQuery field condition.

Copy

```text
1
2
3
4
5
6

{

     workspaceId: 1032131,

     pivotProfileId: 1081794,

     objectSetQuery: { Condition: " " }

}
```

To see the JSON response to the preceding request, see Sample JSON response . For insight into the Pivot profile settings that generated the response, see the next section, which demonstrates how to execute a custom Pivot query and uses the same settings as the Pivot profile in the preceding example.

## Update a Pivot profile

To update a Pivot profile, send a request to this URL for the Pivot Manager service:

Copy

```text
1
<host>/Relativity.REST/api/relativity-pivot/{versionNumber}/workspaces/{workspaceID}/profiles/{pivotProfileID}
```

The request includes the fields listed in the following sample JSON code. For more information about these fields, see on the Relativity Documentation site.

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

{

  "workspaceId": 1015337,

  "profile": {

    "Name": "Update",

    "SortOn": "GrandTotal",

    "SortOrder": "Ascending",

    "PageSize": 10,

    "SwitchSeries": "false",

    "Toggles": {

      "ShowBlankValues": false,

      "ShowLegend": true

      "ShowSubChart": true

    },

    "ObjectType": {

      "Name": "Document"

    },

    "ID": 1040623,

    "GroupByField": {

      "ArtifactID": 1035357

    },

    "PivotOnField": {

      "ArtifactID": 1035351

    },

    "ChartType": "Bar",

    "ChartOrientation": "Vertical"

  }

}
```

The response returns a JSON object with the fields set in the updated Pivot profile.

View a JSON response for an updated Pivot profile Copy

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

{

  "ID": 0,

  "GroupByField": {

    "ArtifactID": 0,

    "ViewFieldID": 0,

    "Guids": [

      "string"

    ],

    "Name": "string"

  },

  "GroupByDateTimePart": "Date",

  "PivotOnField": {

    "ArtifactID": 0,

    "ViewFieldID": 0,

    "Guids": [

      "string"

    ],

    "Name": "string"

  },

  "PivotOnDateTimePart": "Date",

  "GroupByResultLimit": "All",

  "GroupByResultLimitValue": 0,

  "PivotOnResultLimit": "All",

  "PivotOnResultLimitValue": 0,

  "ChartType": "Bar",

  "ChartOrientation": "Horizontal",

  "SortOn": "GrandTotal",

  "SortOrder": "Ascending",

  "Toggles": {

    "ShowBlankValues": true,

    "ShowGrandTotal": true,

    "ShowLegend": true,

    "RotateLabels": true,

    "StaggerLabels": true,

    "ShowLabels": true,

    "ShowSubChart": true

  },

  "PageSize": 0,

  "SwitchSeries": true,

  "ObjectType": {

    "ArtifactTypeID": 0,

    "Name": "string",

    "ArtifactID": 0,

    "Guids": [

      "string"

    ]

  },

  "Name": "string"

}
```

## Execute a custom Pivot query

To execute a custom Pivot query, send a request to the following Pivot Manager service URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-pivot/{versionNumber}/workspaces/{workspaceID}/queries
```

Ensure that the request includes required headers for the Relativity REST API and required fields for the Pivot Manager service. Required fields are:

- ArtifactTypeID

- GroupBy

- GroupByDateGrouping if you want to group data by using a Date field

- objectSetQuery

- PivotOn if you want to pivot data

- PivotOnDateGrouping if you want to pivot data by using a Date field

- RawDataOnly

- Timeout

- workpsaceId

To determine which fields you want to use to group and pivot data, you can use Pivot Service Manager helper operations to get a list of workspace fields that are enabled for grouping and pivoting.

The following code example defines a custom query that primarily does the following:

- Queries all documents in a workspace.

- Groups data by the email address stored in a Fixed-Length Text field named “Email From”.

- Pivots data based on the values in a Yes/No field named “Designation”.

To optimize workspace performance and query results, the example also limits the number of results returned and specifies a timeout value for stopping the query.

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

{

     //Specify which workspace to query.

     workspaceId: 1032131,

     settings: {

          /*

          Set the Artifact Type identifier of the DTO to query. This example queries documents, which

          have an ArtifactTypeID value of “10”.

          */

          ArtifactTypeID: 10,

          //Group data by using the “Email From” field, which has a view field identifier value of “1000566”.

          GroupBy: {

               ViewFieldID: 1000566

          },

          //Pivot data by using the “Designation” field, which has a view field identifier value of “1000555”.

          PivotOn: {

               ViewFieldID: 1000555

          },

          //Limit the results to a specific number of columns and rows.

          MaximumNumberOfColumns: 50,

          MaximumNumberOfRows: 1200,

          //Run the query for no more than 1,020 seconds (17 minutes).

          Timeout: 1020,

          //Return only the data in query results; do not apply Pivot view settings to the results.

          RawDataOnly: false,

          //Query all documents in the workspace; do not limit the query to a subset of documents.

          ObjectSetQuery: { Condition: " " },

     }

}
```

## Export a Pivot query

To export a Pivot query, send a request to this URL for the Pivot Manager service:

Copy

```text
1
<host>/Relativity.REST/api/relativity-pivot/{versionNumber}/workspaces/{workspaceID}/queries/export
```

The request includes the fields listed in the following sample JSON code. For more information about these fields, see on the Relativity Documentation site.

View a JSON request for exporting a Pivot query Copy

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
curl --request POST \

  --url https://doc-web-01.kcura.corp/Relativity.REST/api/relativity-pivot/v1/workspaces/workspaceID/queries/export \

  --header 'Content-Type: application/json' \

  --header 'x-csrf-header: -' \

  --data '{

  "DashboardName": "string",

  "Pivots": [

    {

      "PivotProfileID": 0,

      "PivotSettings": {

        "ID": 0,

        "GroupByField": {

          "ArtifactID": 0,

          "ViewFieldID": 0,

          "Guids": [

            "string"

          ],

          "Name": "string"

        },

        "GroupByDateTimePart": "Date",

        "PivotOnField": {

          "ArtifactID": 0,

          "ViewFieldID": 0,

          "Guids": [

            "string"

          ],

          "Name": "string"

        },

        "PivotOnDateTimePart": "Date",

        "GroupByResultLimit": "All",

        "GroupByResultLimitValue": 0,

        "PivotOnResultLimit": "All",

        "PivotOnResultLimitValue": 0,

        "ChartType": "Bar",

        "ChartOrientation": "Horizontal",

        "SortOn": "GrandTotal",

        "SortOrder": "Ascending",

        "Toggles": {

          "ShowBlankValues": true,

          "ShowGrandTotal": true,

          "ShowLegend": true,

          "RotateLabels": true,

          "StaggerLabels": true,

          "ShowLabels": true,

          "ShowSubChart": true

        },

        "PageSize": 0,

        "SwitchSeries": true,

        "ObjectType": {

          "ArtifactTypeID": 0,

          "Name": "string",

          "ArtifactID": 0,

          "Guids": [

            "string"

          ]

        },

        "Name": "string"

      },

      "Top": 0,

      "Left": 0,

      "Width": 0,

      "Height": 0

    }

  ],

  "Images": [

    {

      "ImageBase64Encoded": "string",

      "Name": "string",

      "Top": 0,

      "Left": 0,

      "Width": 0,

      "Height": 0

    }

  ],

  "AddFullDashboardSheet": true,

  "HeaderSettings": {

    "IncludeWorkspace": true,

    "IncludeView": true,

    "IncludeDashboard": true,

    "IncludeUser": true,

    "IncludeLogo": true,

    "IncludeDateAndTime": true

  },

  "ShowChildSheets": true,

  "SavedSearchID": 0,

  "ViewID": 0,

  "WorkspaceName": "string",

  "ViewName": "string",

  "UserName": "string",

  "CellRatio": 0

}'
```

The response contains the Content Type, and Content field, which has been truncated in the following example. It also includes a Success field, which indicates the status of the export.

Copy

```text
1
2
3
4
5
6

   {

  "ContentType": "string",

  "Content": "string",

  "Success": true

}
```

## Sample JSON response

The following JSON sample shows the response to the custom Pivot query and the profile-based query discussed in the preceding sections. The Results fields report the total number of documents (891) that are in the workspace and contain data in the Email From field. They also report how many of those documents are coded as responsive (True) and non-responsive (False).

Subsequent objects are grouped by the email address stored in the Email From field. The object fields report the applicable email address, the number of documents tagged as responsive (True) and non-responsive (False) for the address, and the total number of documents that have the address in the Email From field. The last four fields in the response provide information about the Pivot query overall—the query returned 277 objects, a Query object was not used, and the query ran successfully.

Sample response Copy

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
1650
1651
1652
1653
1654
1655
1656
1657
1658
1659
1660
1661
1662
1663
1664
1665
1666
1667
1668
1669
1670
1671
1672
1673
1674
1675
1676
1677
1678
1679
1680
1681
1682
1683
1684
1685
1686
1687
1688
1689
{

     "Results": [

     {

     "False": 664,

     "True": 227,

     "Grand Total": 891

     },

     {

     "EmailFrom": "SCS_2 scslooptions@attglobal.net@ENRON",

     "False": 203,

     "True": 0,

     "Grand Total": 203

     },

     {

     "EmailFrom": "SCS_2 <scslooptions@attglobal.net>",

     "False": 27,

     "True": 148,

     "Grand Total": 175

     },

     {

     "EmailFrom": "Zipper",

     "False": 80,

     "True": 19,

     "Grand Total": 99

     },

     {

     "EmailFrom": "Forster  David <David.Forster@ENRON.com>",

     "False": 53,

     "True": 3,

     "Grand Total": 56

     },

     {

     "EmailFrom": "Kitchen",

     "False": 49,

     "True": 0,

     "Grand Total": 49

     },

     {

     "EmailFrom": "Schmidt  Ann M. <Ann.M.Schmidt@ENRON.com>",

     "False": 47,

     "True": 0,

     "Grand Total": 47

     },

     {

     "EmailFrom": "Griffith",

     "False": 41,

     "True": 0,

     "Grand Total": 41

     },

     {

     "EmailFrom": "Schoppe  Tammie <Tammie.Schoppe@ENRON.com>",

     "False": 35,

     "True": 0,

     "Grand Total": 35

     },

     {

     "EmailFrom": "Votaw  Courtney <Courtney.Votaw@ENRON.com>",

     "False": 33,

     "True": 0,

     "Grand Total": 33

     },

     {

     "EmailFrom": "Calger  Christopher F. <Christopher.F.Calger@ENRON.com>",

     "False": 32,

     "True": 0,

     "Grand Total": 32

     },

     {

     "EmailFrom": "Oxley  David <David.Oxley@ENRON.com>",

     "False": 31,

     "True": 0,

     "Grand Total": 31

     },

     {

     "EmailFrom": "CarrFuturesEnergy@carrfut.com@ENRON",

     "False": 24,

     "True": 0,

     "Grand Total": 24

     },

     {

     "EmailFrom": "Unspecified Sender",

     "False": 24,

     "True": 4,

     "Grand Total": 28

     },

     {

     "EmailFrom": "Mike Griffith Griff@odessapumps.com@ENRON",

     "False": 23,

     "True": 0,

     "Grand Total": 23

     },

     {

     "EmailFrom": "Andy Weingarten andy@apbenergy.com@ENRON",

     "False": 19,

     "True": 0,

     "Grand Total": 19

     },

     {

     "EmailFrom": "feedback@intcx.com@ENRON <IMCEANOTES-feedback+40intcx+2Ecom+40ENRON@ENRON.com> - on behalf

     of - IntercontinentalExchange feedback",

     "False": 18,

     "True": 0,

     "Grand Total": 18

     },

     {

     "EmailFrom": "McLaughlin Jr.  Errol <Errol.McLaughlin@ENRON.com>",

     "False": 16,

     "True": 0,

     "Grand Total": 16

     },

     {

     "EmailFrom": "Steffes  James D. <James.D.Steffes@ENRON.com>",

     "False": 16,

     "True": 0,

     "Grand Total": 16

     },

     {

     "EmailFrom": "ARSystem ARSystem@mailman.enron.com@ENRON",

     "False": 14,

     "True": 0,

     "Grand Total": 14

     },

     {

     "EmailFrom": "Bradford  William S. <William.S.Bradford@ENRON.com>",

     "False": 13,

     "True": 0,

     "Grand Total": 13

     },

     {

     "EmailFrom": "Mrha  Jean <Jean.Mrha@ENRON.com>",

     "False": 13,

     "True": 0,

     "Grand Total": 13

     },

     {

     "EmailFrom": "John Phillips <john.phillips@clarionenergy.com>",

     "False": 3,

     "True": 12,

     "Grand Total": 15

     },

     {

     "EmailFrom": "Ballou  Chris Chris_Ballou@bmc.com@ENRON",

     "False": 11,

     "True": 0,

     "Grand Total": 11

     },

     {

     "EmailFrom": "Enron General Announcements <mbx_anncenron@ENRON.com>",

     "False": 11,

     "True": 0,

     "Grand Total": 11

     },

     {

     "EmailFrom": "Cook  Mary <Mary.Cook@ENRON.com>",

     "False": 10,

     "True": 0,

     "Grand Total": 10

     },

     {

     "EmailFrom": "enron_update@concureworkplace.com@ENRON",

     "False": 10,

     "True": 0,

     "Grand Total": 10

     },

     {

     "EmailFrom": "Taylor",

     "False": 10,

     "True": 0,

     "Grand Total": 10

     },

     {

     "EmailFrom": "Angel.Flight.South.Central.Pilots.List@angelflightsc.org",

     "False": 0,

     "True": 9,

     "Grand Total": 9

     },

     {

     "EmailFrom": "Angelica Paez ampaez@earthlink.net@ENRON",

     "False": 8,

     "True": 0,

     "Grand Total": 8

     },

     {

     "EmailFrom": "Nicolay  Christi L. <Christi.L.Nicolay@ENRON.com>",

     "False": 8,

     "True": 0,

     "Grand Total": 8

     },

     {

     "EmailFrom": "Smith  Mark <Mark.Smith@ENRON.com>",

     "False": 8,

     "True": 3,

     "Grand Total": 11

     },

     {

     "EmailFrom": "St. Clair  Carol <Carol.St.Clair@ENRON.com>",

     "False": 8,

     "True": 0,

     "Grand Total": 8

     },

     {

     "EmailFrom": "Atwood  Mechelle <Mechelle.Atwood@ENRON.com>",

     "False": 6,

     "True": 0,

     "Grand Total": 6

     },

     {

     "EmailFrom": "Belden  Tim <Tim.Belden@ENRON.com>",

     "False": 6,

     "True": 0,

     "Grand Total": 6

     },

     {

     "EmailFrom": "E. M. Malone <lottyplace@yahoo.com>",

     "False": 6,

     "True": 0,

     "Grand Total": 6

     },

     {

     "EmailFrom": "gregwhalley 8777865122@skytel.com@ENRON",

     "False": 6,

     "True": 0,

     "Grand Total": 6

     },

     {

     "EmailFrom": "Huan  George <George.Huan@ENRON.com>",

     "False": 6,

     "True": 0,

     "Grand Total": 6

     },

     {

     "EmailFrom": "Johnson  Heather A. <Heather.A.Johnson@ENRON.com>",

     "False": 6,

     "True": 0,

     "Grand Total": 6

     },

     {

     "EmailFrom": "Longoria  Jennifer K. <Jennifer.K.Longoria@ENRON.com>",

     "False": 6,

     "True": 0,

     "Grand Total": 6

     },

     {

     "EmailFrom": "Shah  Kal <Kal.Shah@ENRON.com>",

     "False": 6,

     "True": 0,

     "Grand Total": 6

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com> - on

     behalf of - Office of ",

     "False": 5,

     "True": 0,

     "Grand Total": 5

     },

     {

     "EmailFrom": "Haedicke  Mark E. <Mark.Haedicke@ENRON.com>",

     "False": 5,

     "True": 0,

     "Grand Total": 5

     },

     {

     "EmailFrom": "Hansen  Leslie <Leslie.Hansen@ENRON.com>",

     "False": 5,

     "True": 0,

     "Grand Total": 5

     },

     {

     "EmailFrom": "Kolle  Brian <Brian_Kolle@ENRON.net>",

     "False": 5,

     "True": 0,

     "Grand Total": 5

     },

     {

     "EmailFrom": "Milnthorp  Rob <Rob.Milnthorp@ENRON.com>",

     "False": 5,

     "True": 0,

     "Grand Total": 5

     },

     {

     "EmailFrom": "Presto  Kevin M. <Kevin.M.Presto@ENRON.com>",

     "False": 5,

     "True": 0,

     "Grand Total": 5

     },

     {

     "EmailFrom": "Zipper  Andy <Andy.Zipper@ENRON.com>",

     "False": 5,

     "True": 0,

     "Grand Total": 5

     },

     {

     "EmailFrom": "Adrian Clark AClark@firstcallassociates.com@ENRON",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Barkley  Tom <Tom.Barkley@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Diamond  Russell <Russell.Diamond@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com> - on

     behalf of - The Prince",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Enron Media Cuttings <enron.london.mediacuttings@Enron.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Fairley  David DFairley@tractebelusa.com@ENRON",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Hayden  Frank <Frank.Hayden@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Hodge  Jeffrey T. <Jeffrey.T.Hodge@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Hull  Bryan <Bryan.Hull@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Lu  Zimin <Zimin.Lu@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Mark.Bridges@ubsw.com@ENRON",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Mattias Palm Mattias.Palm@paconsulting.com@ENRON",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Pearson  Peter <Peter.Pearson@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Robinson  Claudia claudia.robinson@ubsw.com@ENRON",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Rostant  Justin <Justin.Rostant@ENRON.com>",

     "False": 4,

     "True": 2,

     "Grand Total": 6

     },

     {

     "EmailFrom": "Slagle  Carrie <Carrie.Slagle@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Smith  Will <Will.Smith@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Superty  Robert <Robert.Superty@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Taylor  Liz <Liz.Taylor@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Taylor  Mark E (Legal) <Mark.Taylor@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "UBSW Energy Global Infrastructure <mbx_ubswGlobalInf@ENRON.com>",

     "False": 4,

     "True": 0,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com> - on

     behalf of - Enron In A",

     "False": 1,

     "True": 4,

     "Grand Total": 5

     },

     {

     "EmailFrom": "Jay Rickerts <eCenter@williams.com>",

     "False": 0,

     "True": 4,

     "Grand Total": 4

     },

     {

     "EmailFrom": "John Phillips <jtp497@rcn.com>",

     "False": 0,

     "True": 4,

     "Grand Total": 4

     },

     {

     "EmailFrom": "Rangel  Ina <Ina.Rangel@ENRON.com>",

     "False": 1,

     "True": 4,

     "Grand Total": 5

     },

     {

     "EmailFrom": "Blair  Kit <Kit.Blair@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Cash  Michelle <Michelle.Cash@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Caudle  Becky <Becky.Caudle@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Clyatt  Julie <Julie.Clyatt@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Crawford, Sharon <Sharon.Crawford@ENRON.com> - on behalf of - Keohane

     Peter <Peter.Keohane@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "David Good dgood@solarc.com@ENRON",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Jacoby  Ben <Ben.Jacoby@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Jafry  Rahil <Rahil.Jafry@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Jolly  Kevin <Kevin.Jolly@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "karimrashid karim@karimrashid.com@ENRON",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Keohane  Peter <Peter.Keohane@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Koehler  Anne C. <Anne.C.Koehler@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Lisk  Daniel <Daniel.Lisk@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Meyn  Jim <Jim.Meyn@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Miller  Don (Asset Mktg) <Don.Miller@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Piper  Greg <Greg.Piper@ENRON.com>",

     "False": 3,

     "True": 3,

     "Grand Total": 6

     },

     {

     "EmailFrom": "Schneider  Chip <Chip.Schneider@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Shapiro  Richard <Richard.Shapiro@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Shepperd  Tammy R. <Tammy.R.Shepperd@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Sherman  Cris <Cris.Sherman@ENRON.com>",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "soblander@carrfut.com@ENRON",

     "False": 3,

     "True": 0,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Beth <beth@angelflightsc.org>",

     "False": 0,

     "True": 3,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Bob Nimocks <BNimocks@ZeusDevelopment.com>",

     "False": 0,

     "True": 3,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com> - on

     behalf of - ClickAtHom",

     "False": 0,

     "True": 3,

     "Grand Total": 3

     },

     {

     "EmailFrom": "General Announcement/Corp/Enron@ENRON <IMCEANOTES-General+20Announcement_Corp_Enron+40ENRON@ENRON.com> - on

     behalf of - Enron Ch",

     "False": 0,

     "True": 3,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Human Resources <mbx_humanresources@ENRON.com>",

     "False": 2,

     "True": 3,

     "Grand Total": 5

     },

     {

     "EmailFrom": "Jackson  Mark <Mark.Jackson@ENRON.com>",

     "False": 0,

     "True": 3,

     "Grand Total": 3

     },

     {

     "EmailFrom": "May  Larry <Larry.May@ENRON.com>",

     "False": 0,

     "True": 3,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Miller  Tim <millertr@bp.com>",

     "False": 0,

     "True": 3,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Whitney Casso <WCasso@ZeusDevelopment.com>",

     "False": 0,

     "True": 3,

     "Grand Total": 3

     },

     {

     "EmailFrom": "7133540022@skytel.com@ENRON",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Aaron Marks aamarks@apmrecruiting.com@ENRON",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "avillarreal73@yahoo.com@ENRON",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Beck  Sally <Sally.Beck@ENRON.com>",

     "False": 2,

     "True": 1,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Bolton  Stacey <Stacey.Bolton@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Brackett  Debbie R. <Debbie.R.Brackett@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Brownfeld  Gail <Gail.Brownfeld@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Buckley  Karen <Karen.Buckley@ENRON.com>",

     "False": 2,

     "True": 1,

     "Grand Total": 3

     },

     {

     "EmailFrom": "Coleman  Mike <Mike.Coleman@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Daniels  Eddy <Eddy.Daniels@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Dodgen  Kathy <Kathy.Dodgen@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Douglas  Stephen H. <Stephen.H.Douglas@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Edwin Fitts edwinfitts@hotmail.com@ENRON",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Elbertson  Janette <Janette.Elbertson@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com> - on

     behalf of - Enron Prop",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com> - on

     behalf of - Ken Lay - ",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "enronmediacuttings@enron.com",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Fitzsimmons  Brendan <Brendan.Fitzsimmons@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Foster  Chris H. <Chris.H.Foster@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Gandhi  Sachin <Sachin.Gandhi@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "General Announcement/Corp/Enron@ENRON <IMCEANOTES-General+20Announcement_Corp_Enron+40ENRON@ENRON.com> - on

     behalf of - Enron Ge",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "General Announcement/Corp/Enron@ENRON <IMCEANOTES-General+20Announcement_Corp_Enron+40ENRON@ENRON.com> - on

     behalf of - Enron Hu",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Gilbert  Gerald <Gerald.Gilbert@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Gossett  Jeffrey C. <Jeffrey.C.Gossett@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Grigsby  Mike <Mike.Grigsby@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Herndon  Rogers <Rogers.Herndon@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Joyce  Mary <Mary.Joyce@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Ken Lay - Office of the Chairman <mbx_klayofficechair@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Lavorato  John <John.Lavorato@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Lea & Loftus Fitzwater Loftuslea@worldnet.att.net@ENRON",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Legal - James Derrick  Jr. <mbx_annclegal@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "McCullough  Travis <Travis.McCullough@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Mena  Luis <Luis.Mena@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Moon  Eric <Eric.Moon@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Novosel  Sarah <Sarah.Novosel@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Ortiz  Lucy <Lucy.Ortiz@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Radford  Pat <Pat.Radford@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "rajib saha rajibsaha59@hotmail.com@ENRON",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Rodriguez  Grace <Grace.Rodriguez@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Rostant jtrostant@yahoo.com@ENRON",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Rub  Jenny <Jenny.Rub@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Sager  Elizabeth <Elizabeth.Sager@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Slone  Jeanie <Jeanie.Slone@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Stock  Steve <Stephen.Stock@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Vu  Steven <Steven.Vu@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Vuittonet  Laura <Laura.Vuittonet@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Watson  Kimberly <Kimberly.Watson@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Webb",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Wiggs  Brett <Brett.R.Wiggs@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Zivic  Robyn <Robyn.Zivic@ENRON.com>",

     "False": 2,

     "True": 0,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com> - on

     behalf of - Enron Chan",

     "False": 0,

     "True": 2,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Good Morning from Money.net <scoop@mailer.money.net>",

     "False": 0,

     "True": 2,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Webb  Jay <Jay.Webb@ENRON.com>",

     "False": 0,

     "True": 2,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Abel  Chris <Chris.Abel@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Arora  Harry <Harry.Arora@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Audrey.Martin@ubsw.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Baughman Jr.  Don <Don.Baughman@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Becker  Lorraine <Lorraine.Becker@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Berquist  Thomas thomas.berquist@gs.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Bess  Erica <Erica.Bess@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Beth.Barrett@ubsw.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "bo.normark@ch.abb.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Bowen Jr.  Raymond <Raymond.Bowen@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Bradford",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Brewster  Jessica JYBrewster@SWIDLAW.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Brooks  Loretta <Loretta_Brooks@ENRON.net>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Bryan.Murtagh@ubsw.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Cantrell  Rebecca W. <Rebecca.W.Cantrell@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Cappelletto, Nella <Nella.Cappelletto@ENRON.com> - on behalf of - Milnthorp

     Rob <Rob.Milnthorp@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Castleman  Kent <Kent.Castleman@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Chris Hanson chris.hanson@excambria.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Clyatt",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "colette.dow@ubsw.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Curry  Mike <Mike.Curry@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Curt Chrestman curt@libation.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Dasovich  Jeff <Jeff.Dasovich@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Davies  Neil <Neil.Davies@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Delgado  Lydia <lydia.delgado@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Denne  Karen <Karen.Denne@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Domain.Manager@register.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Dugger  Tony <Tony.Dugger@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Duran  W. David <W.David.Duran@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Elbertson, Janette <Janette.Elbertson@ENRON.com> - on behalf of - Haedicke

     Mark E. <Mark.Haedicke@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com>

     - on behalf of - eSource@EN",

     "False": 1,

     "True": 1,

     "Grand Total": 2

     },

     {

     "EmailFrom": "Espinoza",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Exchange System Administrator <postmaster@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "fashion@kingshilldirect.co.uk@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Fels  Nicholas nfels@cov.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Fitzpatrick  Amy <Amy.Fitzpatrick@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Forster",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Garland  Kevin <Kevin.Garland@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Gil  Mercy <Mercy.Gil@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Golden  Jeff <Jeff.Golden@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Gray  Chris <Chris.Gray@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Gray  Dortha <Dortha.Gray@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Guadarrama  Michael <Michael.Guadarrama@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Guerrero  Janel <Janel.Guerrero@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Hall  Joe <Joe.Hall@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Hall  Steve C. (Legal) <Steve.C.Hall@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Harry Arora harrysarora@yahoo.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Hedstrom  Peggy <Peggy.Hedstrom@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Hodges  Georganne <Georgeanne.Hodges@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Hodges  Georgeanne <Georgeanne.Hodges@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Intellor Group info@intellor.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Jeff McMahon - President & COO <mbx_anncjmcmahon@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "JJMagovern@aol.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "John Phillips jtp497@rcn.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "John.Costas@ubsw.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "John.Magovern@ubsw.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "JPCJPC57@aol.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Kimmel  Debra [FI] debra.kimmel@ssmb.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Legal - James Derrick Jr. <mbx_annclegal@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Llodra  John <John.Llodra@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Lowry",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Luce  Laura <Laura.Luce@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Mara  Susan <Susan.J.Mara@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Mark.Jones@rwetrading.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Mcginnis  Stephanie <Stephanie.McGinnis@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Melodick  Kim <Kim.Melodick@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "MHeffner@carrfut.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Migden  Janine <Janine.Migden@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Miller  Kevin <Kevin.Miller@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Neal  Scott <Scott.Neal@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Nord  Sue <Sue.Nord@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "O'Donnell - UBS  Pat <Pat.O'Donnell@enron.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "orders@gymboree.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "pat odonnell pat2od@yahoo.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Portz  David <David.Portz@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "postmaster@ENRON.com",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Reck  Daniel <Daniel.Reck@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Richter  Brad <Brad.Richter@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Robinson  Mitch <Mitch.Robinson@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Sanjeev.Karkhanis@ubs.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Scrimshaw  Matthew <matthew.scrimshaw@enron.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Shankman  Jeffrey A. <Jeffrey.A.Shankman@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Sherriff  John <john.sherriff@enron.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "St. Clair, Carol <Carol.St.Clair@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Stuckey  Richard A [FI] richard.a.stuckey@ssmb.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Sulistio  Franky <Franky.Sulistio@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Tamekia e18736@newmail.ru@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Taylor  Mitch <Mitchell.Taylor@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Theriot  Kim S. <Kim.S.Theriot@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Thode  Eric <Eric.Thode@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Tribolet  Michael <Michael.Tribolet@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Tycholiz  Barry <Barry.Tycholiz@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "UBSW Energy General Announcements <mbx_anncubsw@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "uu002000@yahoo.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Van Vuuren  Dirk <dirk.van.vuuren@enron.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Vandor  David <David.Vandor@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Vickers  Frank <Frank.Vickers@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Wallumrod  Ellen <Ellen.Wallumrod@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "White  Stacey W. <Stacey.W.White@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Whitman  Britt <Britt.Whitman@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Williamson  Joannie <Joannie.Williamson@ENRON.com>",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "X. George Huan xjhuan@yahoo.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Xuan Pollard xpollard@richardfreemanco.com@ENRON",

     "False": 1,

     "True": 0,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Andrew Zipper <aazccb@swbell.net>",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Arnold  John <John.Arnold@ENRON.com>",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Bibi  Philippe A. <Philippe.A.Bibi@ENRON.com>",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Boyd  Justin <justin.boyd@enron.com>",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Carter  Carl <Carl.Carter@ENRON.com>",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com> -

     on behalf of - Corporate ",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com> -

     on behalf of - Derryl Cle",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com> -

     on behalf of - Enron Amer",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com> -

     on behalf of - Jim Derric",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Enron Announcements/Corp/Enron@ENRON <IMCEANOTES-Enron+20Announcements_Corp_Enron+40ENRON@ENRON.com> -

     on behalf of - Ken Lay- C",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "FTD.COM@mail2.ftdi.com",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Johnson  Adam <Adam.Johnson@ENRON.com>",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Khanna  Sanjeev <Sanjeev.Khanna@ENRON.com>",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Mcquade  Jennifer <Jennifer.McQuade@ENRON.com>",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Miertschin  Beth <Beth.Miertschin@ENRON.com>",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Office of the Chairman <OfficeoftheChairman6@ENRON.com>",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Puthigai  Savita <Savita.Puthigai@ENRON.com>",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     },

     {

     "EmailFrom": "Solis  Felicia <Felicia_Solis@ENRON.net>",

     "False": 0,

     "True": 1,

     "Grand Total": 1

     }

  ],

  "TotalCount": 277,

  "QueryToken": "",

  "Success": true,

  "Message": "SUCCESS"

}
```

## Helper operations

To help you determine which fields you can use to group and pivot data in a Pivot query, the Pivot Manager Service provides the following helper operations:

- getGroupByFieldsForDocuments – Returns a list of fields that are in a workspace and enabled for grouping data.

- getPivotOnFieldsForDocuments – Returns a list of fields that are in a workspace and enabled for pivoting data.

Note that the list of fields that is returned includes only those fields that you have permission to view. As is the case with Pivot queries, the helper operations use the permission settings of the active user account.

### getGroupByFieldsForDocuments

To get a list of all the fields that you can use to group data in a workspace, send an HTTP(S) POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-pivot/{versionNumber}/workspaces/{workspaceID}/fields/group-by/{artifactTypeID}
```

Required fields for the request are workspaceId and ArtifactTypeId. For example, the following request returns a list of fields that are in a workspace that has an Artifact identifier value of “1234567”, apply to the Document object, can be used to group data, and the active user has permission to view:

Copy

```text
1
2
3
4
5

{

     workspaceId: 1234567,

     ArtifactTypeId: 10

};
```

The JSON response returns the Artifact identifier, view field identifier, and name of each field:

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

[

  {

    "ArtifactID": 0,

    "ViewFieldID": 0,

    "Guids": [

      "string"

    ],

    "Name": "string"

  }

]
```

When you create a custom query, you can use any of those identifiers to specify the field that you want to use to group data.

### getPivotOnFieldsForDocuments

To get a list of all the fields that you can use to pivot data in a workspace, send an HTTP(S) POST request to the following URL:

Copy

```text
1
<host>/Relativity.REST/api/relativity-pivot/{versionNumber}/workspaces/{workspaceID}/fields/pivot-on/{artifactTypeID}
```

Required fields for the request are workspaceId and ArtifactTypeId. In the following example, the request returns a list of fields that are in a workspace that has an Artifact identifier value of “1234567”, apply to the Document object, can be used to pivot data, and the active user has permission to view:

Copy

```text
1
2
3
4
5

{

     workspaceId: 1234567,

     ArtifactTypeId: 10

};
```

The JSON response returns the Artifact identifier, view field identifier, and name of each field:

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
[

  {

    "ArtifactID": 0,

    "ViewFieldID": 0,

    "Guids": [

      "string"

    ],

    "Name": "string"

  }

]
```

When you create a custom query, you can use any of those identifiers to specify the field that you want to use to pivot data.

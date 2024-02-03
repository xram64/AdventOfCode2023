# [Day 5] Map rates achieved in attempts at optimizing code

## Attempt 1: No paralellization
```
Mapping seed     1,000,000 of 1,753,244,662 ||  Time elapsed: 00:17 ||  Average map rate:    58,083.49 maps/sec ||  Projected total run time:  8:23:04
Mapping seed     2,000,000 of 1,753,244,662 ||  Time elapsed: 00:31 ||  Average map rate:    63,695.03 maps/sec ||  Projected total run time:  7:38:45
Mapping seed     3,000,000 of 1,753,244,662 ||  Time elapsed: 00:45 ||  Average map rate:    66,566.64 maps/sec ||  Projected total run time:  7:18:58
Mapping seed     4,000,000 of 1,753,244,662 ||  Time elapsed: 00:59 ||  Average map rate:    67,018.94 maps/sec ||  Projected total run time:  7:16:00
Mapping seed     5,000,000 of 1,753,244,662 ||  Time elapsed: 01:12 ||  Average map rate:    68,573.35 maps/sec ||  Projected total run time:  7:06:07
Mapping seed     6,000,000 of 1,753,244,662 ||  Time elapsed: 01:27 ||  Average map rate:    68,811.60 maps/sec ||  Projected total run time:  7:04:38
Mapping seed     7,000,000 of 1,753,244,662 ||  Time elapsed: 01:40 ||  Average map rate:    69,640.22 maps/sec ||  Projected total run time:  6:59:35
Mapping seed     8,000,000 of 1,753,244,662 ||  Time elapsed: 01:54 ||  Average map rate:    70,155.38 maps/sec ||  Projected total run time:  6:56:30
Mapping seed     9,000,000 of 1,753,244,662 ||  Time elapsed: 02:07 ||  Average map rate:    70,609.49 maps/sec ||  Projected total run time:  6:53:50
Mapping seed    10,000,000 of 1,753,244,662 ||  Time elapsed: 02:21 ||  Average map rate:    70,768.57 maps/sec ||  Projected total run time:  6:52:54
Mapping seed    11,000,000 of 1,753,244,662 ||  Time elapsed: 02:34 ||  Average map rate:    70,990.79 maps/sec ||  Projected total run time:  6:51:36
Mapping seed    12,000,000 of 1,753,244,662 ||  Time elapsed: 02:50 ||  Average map rate:    70,456.55 maps/sec ||  Projected total run time:  6:54:44
Mapping seed    13,000,000 of 1,753,244,662 ||  Time elapsed: 03:04 ||  Average map rate:    70,553.94 maps/sec ||  Projected total run time:  6:54:09
Mapping seed    14,000,000 of 1,753,244,662 ||  Time elapsed: 03:18 ||  Average map rate:    70,553.78 maps/sec ||  Projected total run time:  6:54:09
Mapping seed    15,000,000 of 1,753,244,662 ||  Time elapsed: 03:32 ||  Average map rate:    70,552.64 maps/sec ||  Projected total run time:  6:54:10
Mapping seed    16,000,000 of 1,753,244,662 ||  Time elapsed: 03:46 ||  Average map rate:    70,529.58 maps/sec ||  Projected total run time:  6:54:18
Mapping seed    17,000,000 of 1,753,244,662 ||  Time elapsed: 04:00 ||  Average map rate:    70,636.08 maps/sec ||  Projected total run time:  6:53:40
Mapping seed    18,000,000 of 1,753,244,662 ||  Time elapsed: 04:14 ||  Average map rate:    70,652.19 maps/sec ||  Projected total run time:  6:53:35
Mapping seed    19,000,000 of 1,753,244,662 ||  Time elapsed: 04:28 ||  Average map rate:    70,879.60 maps/sec ||  Projected total run time:  6:52:15
Mapping seed    20,000,000 of 1,753,244,662 ||  Time elapsed: 04:42 ||  Average map rate:    70,767.08 maps/sec ||  Projected total run time:  6:52:54
```

----

## Attempt 2: Using paralellization (4 processes)
```
Mapping seed   166,491,471 of 1,753,244,662 ||  Time elapsed: 0:41:31 ||  Average map rate:    66,815.10 maps/sec ||  Projected total run time:  7:17:20
Mapping seed   321,346,886 of 1,753,244,662 ||  Time elapsed: 0:48:16 ||  Average map rate:   110,932.92 maps/sec ||  Projected total run time:  4:23:24
Mapping seed   531,850,240 of 1,753,244,662 ||  Time elapsed: 0:59:07 ||  Average map rate:   149,913.24 maps/sec ||  Projected total run time:  3:14:55
Mapping seed   553,125,324 of 1,753,244,662 ||  Time elapsed: 1:03:21 ||  Average map rate:   145,486.78 maps/sec ||  Projected total run time:  3:20:50
Mapping seed   646,149,315 of 1,753,244,662 ||  Time elapsed: 1:16:17 ||  Average map rate:   141,168.56 maps/sec ||  Projected total run time:  3:26:59
Mapping seed   958,226,567 of 1,753,244,662 ||  Time elapsed: 1:24:14 ||  Average map rate:   189,560.93 maps/sec ||  Projected total run time:  2:34:08
Mapping seed 1,123,468,569 of 1,753,244,662 ||  Time elapsed: 1:37:20 ||  Average map rate:   192,363.93 maps/sec ||  Projected total run time:  2:31:54
Mapping seed 1,293,875,798 of 1,753,244,662 ||  Time elapsed: 2:03:46 ||  Average map rate:   174,232.82 maps/sec ||  Projected total run time:  2:47:42
Mapping seed 1,526,931,771 of 1,753,244,662 ||  Time elapsed: 2:12:04 ||  Average map rate:   192,694.48 maps/sec ||  Projected total run time:  2:31:38
Mapping seed 1,753,244,662 of 1,753,244,662 ||  Time elapsed: 2:19:33 ||  Average map rate:   209,376.65 maps/sec ||  Projected total run time:  2:19:33
[Part 2] Lowest location number found: 51399228
```
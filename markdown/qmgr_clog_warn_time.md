# qmgr_clog_warn_time (default: 300s)

The minimal delay between warnings that a specific destination is
clogging up the Postfix active queue. Specify 0 to disable.



 Specify a non-negative time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



This feature is enabled with the helpful\_warnings parameter.




This feature is available in Postfix 2.0 and later.




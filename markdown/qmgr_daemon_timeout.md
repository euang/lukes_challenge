# qmgr_daemon_timeout (default: 1000s)
 How much time a Postfix queue manager process may take to handle
a request before it is terminated by a built-in watchdog timer.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 2.8 and later. 



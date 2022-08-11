# postlogd_watchdog_timeout (default: 10s)
 How much time a postlogd(8) process may take to process a request
before it is terminated by a built-in watchdog timer. This is a
safety mechanism that prevents postlogd(8) from becoming non-responsive
due to a bug in Postfix itself or in system software. This limit
cannot be set under 10s. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 3.4 and later. 



# tlsproxy_watchdog_timeout (default: 10s)
 How much time a tlsproxy(8) process may take to process local
or remote I/O before it is terminated by a built-in watchdog timer.
This is a safety mechanism that prevents tlsproxy(8) from becoming
non-responsive due to a bug in Postfix itself or in system software.
To avoid false alarms and unnecessary cache corruption this limit
cannot be set under 10s. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 2.8 and later 



# application_event_drain_time (default: 100s)

How long the postkick(1) command waits for a request to enter the
Postfix daemon process input buffer before giving up.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



This feature is available in Postfix 2.1 and later.




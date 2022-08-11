# trigger_timeout (default: 10s)

The time limit for sending a trigger to a Postfix daemon (for
example, the pickup(8) or qmgr(8) daemon). This time limit prevents
programs from getting stuck when the mail system is under heavy
load.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



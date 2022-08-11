# max_idle (default: 100s)

The maximum amount of time that an idle Postfix daemon process waits
for an incoming connection before terminating voluntarily. This
parameter
is ignored by the Postfix queue manager and by other long-lived
Postfix daemon processes.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



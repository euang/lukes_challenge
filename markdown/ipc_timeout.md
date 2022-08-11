# ipc_timeout (default: 3600s)

The time limit for sending or receiving information over an internal
communication channel. The purpose is to break out of deadlock
situations. If the time limit is exceeded the software aborts with a
fatal error.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



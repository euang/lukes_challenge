# ipc_ttl (default: 1000s)

The time after which a client closes an active internal communication
channel. The purpose is to allow Postfix daemon processes to
terminate voluntarily
after reaching their client limit. This is used, for example, by
the Postfix address resolving and rewriting clients.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



This feature is available in Postfix 2.1 and later.




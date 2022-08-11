# ipc_idle (default: version dependent)

The time after which a client closes an idle internal communication
channel. The purpose is to allow Postfix daemon processes to
terminate voluntarily after they become idle. This is used, for
example, by the Postfix address resolving and rewriting clients.



 With Postfix 2.4 the default value was reduced from 100s to 5s. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



# postscreen_dnsbl_ttl (default: 1h)
 The amount of time that postscreen(8) will use the result from
a successful DNS-based reputation test before a client
IP address is required to pass that test again. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is h (hours). 


 This feature is available in Postfix 2.8-3.0. It was
replaced by postscreen\_dnsbl\_max\_ttl in Postfix 3.1. 



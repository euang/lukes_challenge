# postscreen_dnsbl_timeout (default: 10s)
 The time limit for DNSBL or DNSWL lookups. This is separate from
the timeouts in the dnsblog(8) daemon which are defined by system
resolver(3) routines. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 3.0. 



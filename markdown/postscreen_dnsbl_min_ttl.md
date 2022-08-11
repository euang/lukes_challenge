# postscreen_dnsbl_min_ttl (default: 60s)
 The minimum amount of time that postscreen(8) will use the
result from a successful DNS-based reputation test before a
client IP address is required to pass that test again. If the DNS
reply specifies a larger TTL value, that value will be used unless
it would be larger than postscreen\_dnsbl\_max\_ttl. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 3.1. 



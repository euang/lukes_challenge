# postscreen_dnsbl_max_ttl (default: ${postscreen_dnsbl_ttl?{$postscreen_dnsbl_ttl}:{1}}h)
 The maximum amount of time that postscreen(8) will use the
result from a successful DNS-based reputation test before a
client IP address is required to pass that test again. If the DNS
reply specifies a shorter TTL value, that value will be used unless
it would be smaller than postscreen\_dnsbl\_min\_ttl. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is h (hours). 


 This feature is available in Postfix 3.1. The default setting
is backwards-compatible with older Postfix versions. 



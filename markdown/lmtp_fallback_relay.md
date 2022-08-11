# lmtp_fallback_relay (default: empty)
 Optional list of relay hosts for LMTP destinations that can't be
found or that are unreachable. In main.cf elements are separated by
whitespace or commas. 


 By default, mail is returned to the sender when a destination is not
found, and delivery is deferred when a destination is unreachable. 


 The fallback relays must be TCP destinations, specified without
a leading "inet:" prefix. Specify a host or host:port. Since MX
lookups do not apply with LMTP, there is no need to use the "[host]" or
"[host]:port" forms. If you specify multiple LMTP destinations, Postfix
will try them in the specified order. 



This feature is available in Postfix 3.1 and later.




# postscreen_greet_wait (default: normal: 6s, overload: 2s)
 The amount of time that postscreen(8) will wait for an SMTP
client to send a command before its turn, and for DNS blocklist
lookup results to arrive (default: up to 2 seconds under stress,
up to 6 seconds otherwise). 




 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 2.8. 



# postscreen_non_smtp_command_ttl (default: 30d)
 The amount of time that postscreen(8) will use the result from
a successful "non\_smtp\_command" SMTP protocol test. During this
time, the client IP address is excluded from this test. The default
is long because a client must disconnect after it passes the test,
before it can talk to a real Postfix SMTP server. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is d (days). 


 This feature is available in Postfix 2.8. 



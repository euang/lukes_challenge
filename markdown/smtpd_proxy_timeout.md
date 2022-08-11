# smtpd_proxy_timeout (default: 100s)

The time limit for connecting to a proxy filter and for sending or
receiving information. When a connection fails the client gets a
generic error message while more detailed information is logged to
the maillog file.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



This feature is available in Postfix 2.1 and later.




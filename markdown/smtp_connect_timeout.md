# smtp_connect_timeout (default: 30s)

The Postfix SMTP client time limit for completing a TCP connection, or
zero (use the operating system built-in time limit).




When no connection can be made within the deadline, the Postfix
SMTP client
tries the next address on the mail exchanger list. Specify 0 to
disable the time limit (i.e. use whatever timeout is implemented by
the operating system).



 Specify a non-negative time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



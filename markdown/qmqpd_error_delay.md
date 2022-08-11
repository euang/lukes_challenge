# qmqpd_error_delay (default: 1s)

How long the Postfix QMQP server will pause before sending a negative
reply to the remote QMQP client. The purpose is to slow down confused
or malicious clients.



 Specify a non-negative time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



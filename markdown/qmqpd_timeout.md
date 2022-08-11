# qmqpd_timeout (default: 300s)

The time limit for sending or receiving information over the network.
If a read or write operation blocks for more than $qmqpd\_timeout
seconds the Postfix QMQP server gives up and disconnects.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



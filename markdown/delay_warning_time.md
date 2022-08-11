# delay_warning_time (default: 0h)

The time after which the sender receives a copy of the message
headers of mail that is still queued. The confirm\_delay\_cleared
parameter controls sender notification when the delay clears up.




To enable this feature, specify a non-zero time value (an integral
value plus an optional one-letter suffix that specifies the time
unit).




Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is h (hours).




See also: delay\_notice\_recipient, notify\_classes, confirm\_delay\_cleared.




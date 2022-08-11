# default_transport_rate_delay (default: 0s)
 The default amount of delay that is inserted between individual
message deliveries over the same message delivery transport,
regardless of destination. Specify a non-zero value to rate-limit
those message deliveries to at most one per $default\_transport\_rate\_delay.



Use *transport*\_transport\_rate\_delay to specify a
transport-specific override, where the initial *transport* is
the master.cf name of the message delivery transport. 


 Example: throttle outbound SMTP mail to at most 3 deliveries
per minute. 



```

/etc/postfix/main.cf:
    smtp\_transport\_rate\_delay = 20s

```

 To enable the delay, specify a non-zero time value (an integral
value plus an optional one-letter suffix that specifies the time
unit). 


 Time units: s (seconds), m (minutes), h (hours), d (days), w
(weeks). The default time unit is s (seconds). 


 NOTE: the delay is enforced by the queue manager. 


 This feature is available in Postfix 3.1 and later. 



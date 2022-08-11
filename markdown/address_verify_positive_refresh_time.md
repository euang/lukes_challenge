# address_verify_positive_refresh_time (default: 7d)

The time after which a successful address verification probe needs
to be refreshed. The address verification status is not updated
when the probe fails (optimistic caching).



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is d (days). 



This feature is available in Postfix 2.1 and later.




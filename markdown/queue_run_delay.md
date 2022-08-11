# queue_run_delay (default: 300s)

The time between deferred queue scans by the queue manager;
prior to Postfix 2.4 the default value was 1000s.



 This parameter should be set less than or equal to
$minimal\_backoff\_time. See also $maximal\_backoff\_time. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



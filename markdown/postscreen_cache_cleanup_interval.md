# postscreen_cache_cleanup_interval (default: 12h)
 The amount of time between postscreen(8) cache cleanup runs.
Cache cleanup increases the load on the cache database and should
therefore not be run frequently. This feature requires that the
cache database supports the "delete" and "sequence" operators.
Specify a zero interval to disable cache cleanup. 


 After each cache cleanup run, the postscreen(8) daemon logs the
number of entries that were retained and dropped. A cleanup run is
logged as "partial" when the daemon terminates early after "**postfix
reload**", "**postfix stop**", or no requests for $max\_idle
seconds. 


 Specify a non-negative time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is h (hours). 


 This feature is available in Postfix 2.8. 



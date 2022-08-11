# postscreen_cache_retention_time (default: 7d)
 The amount of time that postscreen(8) will cache an expired
temporary allowlist entry before it is removed. This prevents clients
from being logged as "NEW" just because their cache entry expired
an hour ago. It also prevents the cache from filling up with clients
that passed some deep protocol test once and never came back. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is d (days). 


 This feature is available in Postfix 2.8. 



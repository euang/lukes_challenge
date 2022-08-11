# tls_random_reseed_period (default: 3600s)
 The maximal time between attempts by tlsmgr(8) to re-seed the
in-memory pseudo random number generator (PRNG) pool from external
sources. The actual time between re-seeding attempts is calculated
using the PRNG, and is between 0 and the time specified. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 2.2 and later. 



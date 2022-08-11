# tls_random_prng_update_period (default: 3600s)
 The time between attempts by tlsmgr(8) to save the state of
the pseudo random number generator (PRNG) to the file specified
with $tls\_random\_exchange\_name. 


 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 2.2 and later. 



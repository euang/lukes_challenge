# anvil_rate_time_unit (default: 60s)

The time unit over which client connection rates and other rates
are calculated.




This feature is implemented by the anvil(8) service which is available
in Postfix version 2.2 and later.




The default interval is relatively short. Because of the high
frequency of updates, the anvil(8) server uses volatile memory
only. Thus, information is lost whenever the process terminates.



 Specify a non-zero time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 



# transport_transport_rate_delay (default: $default_transport_rate_delay)
 A transport-specific override for the default\_transport\_rate\_delay
parameter value, where the initial *transport* in the parameter
name is the master.cf name of the message delivery transport. 


 Specify a non-negative time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 Note: *transport*\_transport\_rate\_delay parameters will
not show up in "postconf" command output before Postfix version
2.9. This limitation applies to many parameters whose name is a
combination of a master.cf service name and a built-in suffix (in
this case: "\_transport\_rate\_delay"). 



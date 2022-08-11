# default_destination_rate_delay (default: 0s)
 The default amount of delay that is inserted between individual
message deliveries to the same destination and over the same message
delivery transport. Specify a non-zero value to rate-limit those
message deliveries to at most one per $default\_destination\_rate\_delay.



 The resulting behavior depends on the value of the corresponding
per-destination recipient limit.




* With a corresponding per-destination recipient limit >
1, the rate delay specifies the time between deliveries to the
*same domain*. Different domains are delivered in parallel,
subject to the process limits specified in master.cf.
* With a corresponding per-destination recipient limit equal
to 1, the rate delay specifies the time between deliveries to the
*same recipient*. Different recipients are delivered in
parallel, subject to the process limits specified in master.cf.


 To enable the delay, specify a non-zero time value (an integral
value plus an optional one-letter suffix that specifies the time
unit). 


 Time units: s (seconds), m (minutes), h (hours), d (days), w
(weeks). The default time unit is s (seconds). 


 NOTE: the delay is enforced by the queue manager. The delay
timer state does not survive "**postfix reload**" or "**postfix
stop**".



 Use *transport*\_destination\_rate\_delay to specify a
transport-specific override, where *transport* is the master.cf
name of the message delivery transport.



 NOTE: with a non-zero \_destination\_rate\_delay, specify a
*transport*\_destination\_concurrency\_failed\_cohort\_limit of 10
or more to prevent Postfix from deferring all mail for the same
destination after only one connection or handshake error. 


 This feature is available in Postfix 2.5 and later. 



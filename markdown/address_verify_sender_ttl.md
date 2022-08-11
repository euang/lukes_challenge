# address_verify_sender_ttl (default: 0s)
 The time between changes in the time-dependent portion of address
verification probe sender addresses. The time-dependent portion is
appended to the localpart of the address specified with the
address\_verify\_sender parameter. This feature is ignored when the
probe sender addresses is the null sender, i.e. the address\_verify\_sender
value is empty or <>. 


 Historically, the probe sender address was fixed. This has
caused such addresses to end up on spammer mailing lists, and has
resulted in wasted network and processing resources. 


 To enable time-dependent probe sender addresses, specify a
non-zero time value. Specify a value of at least several hours,
to avoid problems with senders that use greylisting. Avoid nice
TTL values, to make the result less predictable. 


 Specify a non-negative time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 2.9 and later. 



# default_destination_recipient_limit (default: 50)

The default maximal number of recipients per message delivery.
This is the default limit for delivery via the lmtp(8), pipe(8),
smtp(8) and virtual(8) delivery agents.



 Setting this parameter to a value of 1 affects email deliveries
as follows:


* It changes the meaning of the corresponding per-destination
concurrency limit, from concurrency of deliveries to the *same
domain* into concurrency of deliveries to the *same recipient*.
Different recipients are delivered in parallel, subject to the
process limits specified in master.cf.
* It changes the meaning of the corresponding per-destination
rate delay, from the delay between deliveries to the *same
domain* into the delay between deliveries to the *same
recipient*. Again, different recipients are delivered in parallel,
subject to the process limits specified in master.cf.
* It changes the meaning of other corresponding per-destination
settings in a similar manner, from settings for delivery to the
*same domain* into settings for delivery to the *same
recipient*.


 Use *transport*\_destination\_recipient\_limit to specify a
transport-specific override, where *transport* is the master.cf
name of the message delivery transport.




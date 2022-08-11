# default_recipient_refill_delay (default: 5s)

The default per-transport maximum delay between refilling recipients.
When not all message recipients fit into memory at once, keep loading
more of them at least once every this many seconds. This is used to
make sure the recipients are refilled in a timely manner even when
$default\_recipient\_refill\_limit is too high for too slow deliveries.



 Use *transport*\_recipient\_refill\_delay to specify a
transport-specific override, where *transport* is the master.cf
name of the message delivery transport.



 This feature is available in Postfix 2.4 and later. 



# default_destination_concurrency_limit (default: 20)

The default maximal number of parallel deliveries to the same
destination. This is the default limit for delivery via the lmtp(8),
pipe(8), smtp(8) and virtual(8) delivery agents.
With a per-destination recipient limit > 1, a destination is a domain,
otherwise it is a recipient.



 Use *transport*\_destination\_concurrency\_limit to specify a
transport-specific override, where *transport* is the master.cf
name of the message delivery transport.




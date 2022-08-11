# initial_destination_concurrency (default: 5)

The initial per-destination concurrency level for parallel delivery
to the same destination.
With per-destination recipient limit > 1, a destination is a domain,
otherwise it is a recipient.



 Use *transport*\_initial\_destination\_concurrency to specify
a transport-specific override, where *transport* is the master.cf
name of the message delivery transport (Postfix 2.5 and later). 



Warning: with concurrency of 1, one bad message can be enough to
block all mail to a site.




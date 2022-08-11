# default_minimum_delivery_slots (default: 3)

How many recipients a message must have in order to invoke the
Postfix queue manager's scheduling algorithm at all. Messages
which would never accumulate at least this many delivery slots
(subject to slot cost parameter as well) are never preempted.



 Use *transport*\_minimum\_delivery\_slots to specify a
transport-specific override, where *transport* is the master.cf
name of the message delivery transport.




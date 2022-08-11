# default_delivery_slot_cost (default: 5)

How often the Postfix queue manager's scheduler is allowed to
preempt delivery of one message with another.




Each transport maintains a so-called "available delivery slot counter"
for each message. One message can be preempted by another one when
the other message can be delivered using no more delivery slots
(i.e., invocations of delivery agents) than the current message
counter has accumulated (or will eventually accumulate - see about
slot loans below). This parameter controls how often the counter is
incremented - it happens after each default\_delivery\_slot\_cost
recipients have been delivered.




The cost of 0 is used to disable the preempting scheduling completely.
The minimum value the scheduling algorithm can use is 2 - use it
if you want to maximize the message throughput rate. Although there
is no maximum, it doesn't make much sense to use values above say
50.




The only reason why the value of 2 is not the default is the way
this parameter affects the delivery of mailing-list mail. In the
worst case, delivery can take somewhere between (cost+1/cost)
and (cost/cost-1) times more than if the preemptive scheduler was
disabled. The default value of 5 turns out to provide reasonable
message response times while making sure the mailing-list deliveries
are not extended by more than 20-25 percent even in the worst case.



 Use *transport*\_delivery\_slot\_cost to specify a
transport-specific override, where *transport* is the master.cf
name of the message delivery transport.




Examples:




```

default\_delivery\_slot\_cost = 0
default\_delivery\_slot\_cost = 2

```


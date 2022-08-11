# in_flow_delay (default: 1s)
 Time to pause before accepting a new message, when the message
arrival rate exceeds the message delivery rate. This feature is
turned on by default (it's disabled on SCO UNIX due to an SCO bug).




With the default 100 Postfix SMTP server process limit, "in\_flow\_delay
= 1s" limits the mail inflow to 100 messages per second above the
number of messages delivered per second.




Specify 0 to disable the feature. Valid delays are 0..10.




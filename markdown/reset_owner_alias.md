# reset_owner_alias (default: no)
 Reset the local(8) delivery agent's idea of the owner-alias
attribute, when delivering mail to a child alias that does not have
its own owner alias. 


 This feature is available in Postfix 2.8 and later. With older
Postfix releases, the behavior is as if this parameter is set to
"yes". 


 As documented in aliases(5), when an alias *name* has a
companion alias named owner-*name*, this will replace the
envelope sender address, so that delivery errors will be
reported to the owner alias instead of the sender. This configuration
is recommended for mailing lists. 




 A less known property of the owner alias is that it also forces
the local(8) delivery agent to write local and remote addresses
from alias expansion to a new queue file, instead of attempting to
deliver mail to local addresses as soon as they come out of alias
expansion. 


 Writing local addresses from alias expansion to a new queue
file allows for robust handling of temporary delivery errors: errors
with one local member have no effect on deliveries to other members
of the list. On the other hand, delivery to local addresses as
soon as they come out of alias expansion is fragile: a temporary
error with one local address from alias expansion will cause the
entire alias to be expanded repeatedly until the error goes away,
or until the message expires in the queue. In that case, a problem
with one list member results in multiple message deliveries to other
list members. 


 The default behavior of Postfix 2.8 and later is to keep the
owner-alias attribute of the parent alias, when delivering mail to
a child alias that does not have its own owner alias. Then, local
addresses from that child alias will be written to a new queue file,
and a temporary error with one local address will not affect delivery
to other mailing list members. 


 Unfortunately, older Postfix releases reset the owner-alias
attribute when delivering mail to a child alias that does not have
its own owner alias. To be precise, this resets only the decision
to create a new queue file, not the decision to override the envelope
sender address. The local(8) delivery agent then attempts to
deliver local addresses as soon as they come out of child alias
expansion. If delivery to any address from child alias expansion
fails with a temporary error condition, the entire mailing list may
be expanded repeatedly until the mail expires in the queue, resulting
in multiple deliveries of the same message to mailing list members.




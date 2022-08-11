# masquerade_classes (default: envelope_sender, header_sender, header_recipient)

What addresses are subject to address masquerading.




By default, address masquerading is limited to envelope sender
addresses, and to header sender and header recipient addresses.
This allows you to use address masquerading on a mail gateway while
still being able to forward mail to users on individual machines.




Specify zero or more of: envelope\_sender, envelope\_recipient,
header\_sender, header\_recipient




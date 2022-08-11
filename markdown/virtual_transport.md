# virtual_transport (default: virtual)

The default mail delivery transport and next-hop destination for
final delivery to domains listed with $virtual\_mailbox\_domains.
This information can be overruled with the transport(5) table.




Specify a string of the form *transport:nexthop*, where *transport*
is the name of a mail delivery transport defined in master.cf.
The *:nexthop* destination is optional; its syntax is documented
in the manual page of the corresponding delivery agent.




This feature is available in Postfix 2.0 and later.




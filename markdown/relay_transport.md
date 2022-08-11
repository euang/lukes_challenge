# relay_transport (default: relay)

The default mail delivery transport and next-hop destination for
remote delivery to domains listed with $relay\_domains. In order of
decreasing precedence, the nexthop destination is taken from
$relay\_transport, $sender\_dependent\_relayhost\_maps, $relayhost, or
from the recipient domain. This information can be overruled with
the transport(5) table.




Specify a string of the form *transport:nexthop*, where *transport*
is the name of a mail delivery transport defined in master.cf.
The *:nexthop* destination is optional; its syntax is documented
in the manual page of the corresponding delivery agent.




See also the relay domains address class in the ADDRESS\_CLASS\_README
file.




This feature is available in Postfix 2.0 and later.




# default_transport (default: smtp)

The default mail delivery transport and next-hop destination for
destinations that do not match $mydestination, $inet\_interfaces,
$proxy\_interfaces, $virtual\_alias\_domains, $virtual\_mailbox\_domains,
or $relay\_domains. This information can be overruled with the
sender\_dependent\_default\_transport\_maps parameter and with the
transport(5) table. 



In order of decreasing precedence, the nexthop destination is taken
from $sender\_dependent\_default\_transport\_maps, $default\_transport,
$sender\_dependent\_relayhost\_maps, $relayhost, or from the recipient
domain.




Specify a string of the form *transport:nexthop*, where *transport*
is the name of a mail delivery transport defined in master.cf.
The *:nexthop* destination is optional; its syntax is documented
in the manual page of the corresponding delivery agent. In the case of
SMTP or LMTP, specify one or more destinations separated by comma or
whitespace (with Postfix 3.5 and later).




Example:




```

default\_transport = uucp:relayhostname

```


# best_mx_transport (default: empty)

Where the Postfix SMTP client should deliver mail when it detects
a "mail loops back to myself" error condition. This happens when
the local MTA is the best SMTP mail exchanger for a destination
not listed in $mydestination, $inet\_interfaces, $proxy\_interfaces,
$virtual\_alias\_domains, or $virtual\_mailbox\_domains. By default,
the Postfix SMTP client returns such mail as undeliverable.




Specify, for example, "best\_mx\_transport = local" to pass the mail
from the Postfix SMTP client to the local(8) delivery agent. You
can specify
any message delivery "transport" or "transport:nexthop" that is
defined in the master.cf file. See the transport(5) manual page
for the syntax and meaning of "transport" or "transport:nexthop".




However, this feature is expensive because it ties up a Postfix
SMTP client process while the local(8) delivery agent is doing its
work. It is more efficient (for Postfix) to list all hosted domains
in a table or database.




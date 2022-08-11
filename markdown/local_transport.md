# local_transport (default: local:$myhostname)
 The default mail delivery transport and next-hop destination
for final delivery to domains listed with mydestination, and for
[ipaddress] destinations that match $inet\_interfaces or $proxy\_interfaces.
This information can be overruled with the transport(5) table. 



By default, local mail is delivered to the transport called "local",
which is just the name of a service that is defined the master.cf file.




Specify a string of the form *transport:nexthop*, where *transport*
is the name of a mail delivery transport defined in master.cf.
The *:nexthop* destination is optional; its syntax is documented
in the manual page of the corresponding delivery agent.




Beware: if you override the default local delivery agent then you
need to review the LOCAL\_RECIPIENT\_README document, otherwise the
SMTP server may reject mail for local recipients.




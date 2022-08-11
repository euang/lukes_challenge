# inet_interfaces (default: all)
 The local network interface addresses that this mail system receives
mail on. Specify "all" to receive mail on all network
interfaces (default), and "loopback-only" to receive mail
on loopback network interfaces only (Postfix version 2.2 and later). The
parameter also controls delivery of mail to user@[ip.address].




Note 1: you need to stop and start Postfix when this parameter changes.



 Note 2: address information may be enclosed inside [],
but this form is not required here. 


 When inet\_interfaces specifies just one IPv4 and/or IPv6 address
that is not a loopback address, the Postfix SMTP client will use
this address as the IP source address for outbound mail. Support
for IPv6 is available in Postfix version 2.2 and later. 



On a multi-homed firewall with separate Postfix instances listening on the
"inside" and "outside" interfaces, this can prevent each instance from
being able to reach remote SMTP servers on the "other side" of the
firewall. Setting
smtp\_bind\_address to 0.0.0.0 avoids the potential problem for
IPv4, and setting smtp\_bind\_address6 to :: solves the problem
for IPv6. 



A better solution for multi-homed firewalls is to leave inet\_interfaces
at the default value and instead use explicit IP addresses in
the master.cf SMTP server definitions. This preserves the Postfix
SMTP client's
loop detection, by ensuring that each side of the firewall knows that the
other IP address is still the same host. Setting $inet\_interfaces to a
single IPv4 and/or IPV6 address is primarily useful with virtual
hosting of domains on
secondary IP addresses, when each IP address serves a different domain
(and has a different $myhostname setting). 



See also the proxy\_interfaces parameter, for network addresses that
are forwarded to Postfix by way of a proxy or address translator.




Examples:




```

inet\_interfaces = all (DEFAULT)
inet\_interfaces = loopback-only (Postfix version 2.2 and later)
inet\_interfaces = 127.0.0.1
inet\_interfaces = 127.0.0.1, [::1] (Postfix version 2.2 and later)
inet\_interfaces = 192.168.1.2, 127.0.0.1

```


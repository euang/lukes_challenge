# inet_protocols (default: see 'postconf -d output')
 The Internet protocols Postfix will attempt to use when making
or accepting connections. Specify one or more of "ipv4"
or "ipv6", separated by whitespace or commas. The form
"all" is equivalent to "ipv4, ipv6" or "ipv4", depending
on whether the operating system implements IPv6. 


 With Postfix 2.8 and earlier the default is "ipv4". For backwards
compatibility with these releases, the Postfix 2.9 and later upgrade
procedure appends an explicit "inet\_protocols = ipv4" setting to
main.cf when no explicit setting is present. This compatibility
workaround will be phased out as IPv6 deployment becomes more common.



 This feature is available in Postfix 2.2 and later. 


 Note: you MUST stop and start Postfix after changing this
parameter. 


 On systems that pre-date IPV6\_V6ONLY support (RFC 3493), an
IPv6 server will also accept IPv4 connections, even when IPv4 is
turned off with the inet\_protocols parameter. On systems with
IPV6\_V6ONLY support, Postfix will use separate server sockets for
IPv6 and IPv4, and each will accept only connections for the
corresponding protocol. 


 When IPv4 support is enabled via the inet\_protocols parameter,
Postfix will look up DNS type A records, and will convert
IPv4-in-IPv6 client IP addresses (::ffff:1.2.3.4) to their original
IPv4 form (1.2.3.4). The latter is needed on hosts that pre-date
IPV6\_V6ONLY support (RFC 3493). 


 When IPv6 support is enabled via the inet\_protocols parameter,
Postfix will do DNS type AAAA record lookups. 


 When both IPv4 and IPv6 support are enabled, the Postfix SMTP
client will choose the protocol as specified with the
smtp\_address\_preference parameter. Postfix versions before 2.8
attempt to connect via IPv6 before attempting to use IPv4. 



Examples:




```

inet\_protocols = ipv4
inet\_protocols = all (DEFAULT)
inet\_protocols = ipv6
inet\_protocols = ipv4, ipv6

```


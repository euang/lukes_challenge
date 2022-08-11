# smtp_tls_per_site (default: empty)
 Optional lookup tables with the Postfix SMTP client TLS usage
policy by next-hop destination and by remote SMTP server hostname.
When both lookups succeed, the more specific per-site policy (NONE,
MUST, etc.) overrides the less specific one (MAY), and the more secure
per-site policy (MUST, etc.) overrides the less secure one (NONE).
With Postfix 2.3 and later smtp\_tls\_per\_site is strongly discouraged:
use smtp\_tls\_policy\_maps instead. 


 Use of the bare hostname as the per-site table lookup key is
discouraged. Always use the full destination nexthop (enclosed in
[] with a possible ":port" suffix). A recipient domain or MX-enabled
transport next-hop with no port suffix may look like a bare hostname,
but is still a suitable *destination*. 


 Specify a next-hop destination or server hostname on the left-hand
side; no wildcards are allowed. The next-hop destination is either
the recipient domain, or the destination specified with a transport(5)
table, the relayhost parameter, or the relay\_transport parameter.
On the right hand side specify one of the following keywords: 



 NONE   Don't use TLS at all. This overrides a less
specific **MAY** lookup result from the alternate host or next-hop
lookup key, and overrides the global smtp\_use\_tls, smtp\_enforce\_tls,
and smtp\_tls\_enforce\_peername settings. 
 MAY   Try to use TLS if the server announces support,
otherwise use an unencrypted connection. This has less precedence
than a more specific result (including **NONE**) from the alternate
host or next-hop lookup key, and has less precedence than the more
specific global "smtp\_enforce\_tls = yes" or "smtp\_tls\_enforce\_peername
= yes". 
 MUST\_NOPEERMATCH   Require TLS encryption, but do not
require that the remote SMTP server hostname matches the information
in the remote SMTP server certificate, or that the server certificate
was issued by a trusted CA. This overrides a less secure **NONE**
or a less specific **MAY** lookup result from the alternate host
or next-hop lookup key, and overrides the global smtp\_use\_tls,
smtp\_enforce\_tls and smtp\_tls\_enforce\_peername settings. 
 MUST   Require TLS encryption, require that the remote
SMTP server hostname matches the information in the remote SMTP
server certificate, and require that the remote SMTP server certificate
was issued by a trusted CA. This overrides a less secure **NONE**
or **MUST\_NOPEERMATCH** or a less specific **MAY** lookup
result from the alternate host or next-hop lookup key, and overrides
the global smtp\_use\_tls, smtp\_enforce\_tls and smtp\_tls\_enforce\_peername
settings. 

 The above keywords correspond to the "none", "may", "encrypt" and
"verify" security levels for the new smtp\_tls\_security\_level parameter
introduced in Postfix 2.3. Starting with Postfix 2.3, and independently
of how the policy is specified, the smtp\_tls\_mandatory\_ciphers and
smtp\_tls\_mandatory\_protocols parameters apply when TLS encryption
is mandatory. Connections for which encryption is optional typically
enable all "export" grade and better ciphers (see smtp\_tls\_ciphers
and smtp\_tls\_protocols). 


 As long as no secure DNS lookup mechanism is available, false
hostnames in MX or CNAME responses can change the server hostname
that Postfix uses for TLS policy lookup and server certificate
verification. Even with a perfect match between the server hostname and
the server certificate, there is no guarantee that Postfix is connected
to the right server. See TLS\_README (Closing a DNS loophole with obsolete
per-site TLS policies) for a possible work-around. 


 This feature is available in Postfix 2.2 and later. With
Postfix 2.3 and later use smtp\_tls\_policy\_maps instead. 



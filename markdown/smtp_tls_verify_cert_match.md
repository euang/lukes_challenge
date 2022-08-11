# smtp_tls_verify_cert_match (default: hostname)
 How the Postfix SMTP client verifies the server certificate
peername for the
"verify" TLS security level. In a "verify" TLS policy table
($smtp\_tls\_policy\_maps) entry the optional "match" attribute
overrides this main.cf setting. 


 This parameter specifies one or more patterns or strategies separated
by commas, whitespace or colons. In the policy table the only valid
separator is the colon character. 


 Patterns specify domain names, or domain name suffixes: 



*example.com*  Match the *example.com* domain,
i.e. one of the names in the server certificate must be *example.com*.
Upper and lower case distinctions are ignored. 
*.example.com*
 Match subdomains of the *example.com* domain, i.e. match
a name in the server certificate that consists of a non-zero number of
labels followed by a *.example.com* suffix. Case distinctions are
ignored.

 Strategies specify a transformation from the next-hop domain
to the expected name in the server certificate: 



nexthop
 Match against the next-hop domain, which is either the recipient
domain, or the transport next-hop configured for the domain stripped of
any optional socket type prefix, enclosing square brackets and trailing
port. When MX lookups are not suppressed, this is the original nexthop
domain prior to the MX lookup, not the result of the MX lookup. For
LMTP delivery via UNIX-domain sockets, the verified next-hop name is
$myhostname. This strategy is suitable for use with the "secure"
policy. Case is ignored.
dot-nexthop
 As above, but match server certificate names that are subdomains
of the next-hop domain. Case is ignored.
hostname  Match against the hostname of the server, often
obtained via an unauthenticated DNS MX lookup. For LMTP delivery via
UNIX-domain sockets, the verified name is $myhostname. This matches
the verification strategy of the "MUST" keyword in the obsolete
smtp\_tls\_per\_site table, and is suitable for use with the "verify"
security level. When the next-hop name is enclosed in square brackets
to suppress MX lookups, the "hostname" strategy is the same as the
"nexthop" strategy. Case is ignored.


Sample main.cf setting:




```

smtp\_tls\_verify\_cert\_match = hostname, nexthop, dot-nexthop

```


Sample policy table override:




```

example.com     verify  match=hostname:nexthop
.example.com    verify  match=example.com:.example.com:hostname

```

 This feature is available in Postfix 2.3 and later. 



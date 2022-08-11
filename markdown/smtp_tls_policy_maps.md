# smtp_tls_policy_maps (default: empty)
 Optional lookup tables with the Postfix SMTP client TLS security
policy by next-hop destination; when a non-empty value is specified,
this overrides the obsolete smtp\_tls\_per\_site parameter. See
TLS\_README for a more detailed discussion of TLS security levels.




Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.



 The TLS policy table is indexed by the full next-hop destination,
which is either the recipient domain, or the verbatim next-hop
specified in the transport table, $local\_transport, $virtual\_transport,
$relay\_transport or $default\_transport. This includes any enclosing
square brackets and any non-default destination server port suffix. The
LMTP socket type prefix (inet: or unix:) is not included in the lookup
key. 


 Only the next-hop domain, or $myhostname with LMTP over UNIX-domain
sockets, is used as the nexthop name for certificate verification. The
port and any enclosing square brackets are used in the table lookup key,
but are not used for server name verification. 


 When the lookup key is a domain name without enclosing square brackets
or any *:port* suffix (typically the recipient domain), and the full
domain is not found in the table, just as with the transport(5) table,
the parent domain starting with a leading "." is matched recursively. This
allows one to specify a security policy for a recipient domain and all
its sub-domains. 


 The lookup result is a security level, followed by an optional list
of whitespace and/or comma separated name=value attributes that override
related main.cf settings. The TLS security levels in order of increasing
security are: 



**none**
No TLS. No additional attributes are supported at this level. 
**may**
Opportunistic TLS. Since sending in the clear is acceptable,
demanding stronger than default TLS security merely reduces
interoperability. The optional "ciphers", "exclude", and "protocols"
attributes (available for opportunistic TLS with Postfix ≥ 2.6)
and "connection\_reuse" attribute (Postfix ≥ 3.4) override the
"smtp\_tls\_ciphers", "smtp\_tls\_exclude\_ciphers", "smtp\_tls\_protocols",
and
"smtp\_tls\_connection\_reuse" configuration parameters. In the policy table,
multiple ciphers, protocols or excluded ciphers must be separated by colons,
as attribute values may not contain whitespace or commas. When opportunistic
TLS handshakes fail, Postfix retries the connection with TLS disabled.
This allows mail delivery to sites with non-interoperable TLS
implementations.
**encrypt**
Mandatory TLS encryption. At this level
and higher, the optional "protocols" attribute overrides the main.cf
smtp\_tls\_mandatory\_protocols parameter, the optional "ciphers" attribute
overrides the main.cf smtp\_tls\_mandatory\_ciphers parameter, the
optional "exclude" attribute (Postfix ≥ 2.6) overrides the main.cf
smtp\_tls\_mandatory\_exclude\_ciphers parameter, and the optional
"connection\_reuse" attribute (Postfix ≥ 3.4) overrides the
main.cf smtp\_tls\_connection\_reuse parameter. In the policy table,
multiple ciphers, protocols or excluded ciphers must be separated by colons,
as attribute values may not contain whitespace or commas. 
**dane**
Opportunistic DANE TLS. The TLS policy for the destination is
obtained via TLSA records in DNSSEC. If no TLSA records are found,
the effective security level used is may. If TLSA records are
found, but none are usable, the effective security level is encrypt. When usable
TLSA records are obtained for the remote SMTP server, the
server certificate must match the TLSA records. RFC 7672 (DANE)
TLS authentication and DNSSEC support is available with Postfix
2.11 and later. The optional "connection\_reuse" attribute (Postfix
≥ 3.4) overrides the main.cf smtp\_tls\_connection\_reuse parameter.
When the effective security level used is may, the optional "ciphers",
"exclude", and "protocols" attributes (Postfix ≥ 2.6) override the
"smtp\_tls\_ciphers", "smtp\_tls\_exclude\_ciphers", and "smtp\_tls\_protocols"
configuration parameters.
When the effective security level used is encrypt, the optional "ciphers",
"exclude", and "protocols" attributes (Postfix ≥ 2.6) override the
"smtp\_tls\_mandatory\_ciphers", "smtp\_tls\_mandatory\_exclude\_ciphers", and
"smtp\_tls\_mandatory\_protocols" configuration parameters.

**dane-only**
Mandatory DANE TLS. The TLS policy for the destination is
obtained via TLSA records in DNSSEC. If no TLSA records are found,
or none are usable, no connection is made to the server. When
usable TLSA records are obtained for the remote SMTP server, the
server certificate must match the TLSA records. RFC 7672 (DANE) TLS
authentication and DNSSEC support is available with Postfix 2.11
and later. The optional "ciphers", "exclude", and "protocols" attributes
(Postfix ≥ 2.6) override the "smtp\_tls\_mandatory\_ciphers",
"smtp\_tls\_mandatory\_exclude\_ciphers", and "smtp\_tls\_mandatory\_protocols"
configuration parameters. The optional "connection\_reuse" attribute
(Postfix ≥ 3.4) overrides the main.cf smtp\_tls\_connection\_reuse parameter.

**fingerprint**
Certificate fingerprint
verification. Available with Postfix 2.5 and later. At this security
level, there are no trusted Certification Authorities. The certificate
trust chain, expiration date, ... are not checked. Instead,
the optional "match" attribute, or else the main.cf
**smtp\_tls\_fingerprint\_cert\_match** parameter, lists the certificate
fingerprints or the public key fingerprint (Postfix 2.9 and later)
of the valid server certificate. The digest
algorithm used to calculate the fingerprint is selected by the
**smtp\_tls\_fingerprint\_digest** parameter. Multiple fingerprints can
be combined with a "|" delimiter in a single match attribute, or multiple
match attributes can be employed. The ":" character is not used as a
delimiter as it occurs between each pair of fingerprint (hexadecimal)
digits. The optional "ciphers", "exclude", and "protocols" attributes
(Postfix ≥ 2.6) override the "smtp\_tls\_mandatory\_ciphers",
"smtp\_tls\_mandatory\_exclude\_ciphers", and "smtp\_tls\_mandatory\_protocols"
configuration parameters. The optional "connection\_reuse" attribute
(Postfix ≥ 3.4) overrides the main.cf smtp\_tls\_connection\_reuse
parameter. 
**verify**
Mandatory TLS verification. At this security
level, DNS MX lookups are trusted to be secure enough, and the name
verified in the server certificate is usually obtained indirectly via
unauthenticated DNS MX lookups. The optional "match" attribute overrides
the main.cf smtp\_tls\_verify\_cert\_match parameter. In the policy table,
multiple match patterns and strategies must be separated by colons.
In practice explicit control over matching is more common with the
"secure" policy, described below. The optional "ciphers", "exclude",
and "protocols" attributes (Postfix ≥ 2.6) override the
"smtp\_tls\_mandatory\_ciphers", "smtp\_tls\_mandatory\_exclude\_ciphers", and
"smtp\_tls\_mandatory\_protocols" configuration parameters. The optional
"connection\_reuse" attribute (Postfix ≥ 3.4) overrides the main.cf
smtp\_tls\_connection\_reuse parameter. 
**secure**
Secure-channel TLS. At this security level, DNS
MX lookups, though potentially used to determine the candidate next-hop
gateway IP addresses, are **not** trusted to be secure enough for TLS
peername verification. Instead, the default name verified in the server
certificate is obtained directly from the next-hop, or is explicitly
specified via the optional "match" attribute which overrides the
main.cf smtp\_tls\_secure\_cert\_match parameter. In the policy table,
multiple match patterns and strategies must be separated by colons.
The match attribute is most useful when multiple domains are supported by
a common server: the policy entries for additional domains specify matching
rules for the primary domain certificate. While transport table overrides
that route the secondary domains to the primary nexthop also allow secure
verification, they risk delivery to the wrong destination when domains
change hands or are re-assigned to new gateways. With the "match"
attribute approach, routing is not perturbed, and mail is deferred if
verification of a new MX host fails. The optional "ciphers", "exclude",
and "protocols" attributes (Postfix ≥ 2.6) override the
"smtp\_tls\_mandatory\_ciphers", "smtp\_tls\_mandatory\_exclude\_ciphers", and
"smtp\_tls\_mandatory\_protocols" configuration parameters. The optional
"connection\_reuse" attribute (Postfix ≥ 3.4) overrides the main.cf
smtp\_tls\_connection\_reuse parameter. 


Example:




```

/etc/postfix/main.cf:
    smtp\_tls\_policy\_maps = hash:/etc/postfix/tls\_policy
    # Postfix 2.5 and later.
    #
    # The default digest is sha256 with Postfix ≥ 3.6 and
    # compatibility level ≥ 3.
    #
    smtp\_tls\_fingerprint\_digest = sha256

```


```

/etc/postfix/tls\_policy:
    example.edu                 none
    example.mil                 may
    example.gov                 encrypt protocols=TLSv1
    example.com                 verify ciphers=high
    example.net                 secure
    .example.net                secure match=.example.net:example.net
    [mail.example.org]:587      secure match=nexthop
    # Postfix 2.5 and later
    [thumb.example.org]          fingerprint
        match=b6:b4:72:34:e2:59:cd:...:c2:ca:63:0d:4d:cc:2c:7d:84:de:e6:2f
        match=51:e9:af:2e:1e:40:1f:...:64:0a:30:35:2d:09:16:31:5a:eb:82:76

```

 **Note:** The "hostname" strategy if listed in a non-default
setting of smtp\_tls\_secure\_cert\_match or in the "match" attribute
in the policy table can render the "secure" level vulnerable to
DNS forgery. Do not use the "hostname" strategy for secure-channel
configurations in environments where DNS security is not assured. 


 This feature is available in Postfix 2.3 and later. 



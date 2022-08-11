# smtp_tls_security_level (default: empty)
 The default SMTP TLS security level for the Postfix SMTP client.
When a non-empty value is specified, this overrides the obsolete
parameters smtp\_use\_tls, smtp\_enforce\_tls, and smtp\_tls\_enforce\_peername;
when no value is specified for smtp\_tls\_enforce\_peername or the obsolete
parameters, the default SMTP TLS security level is
none. 


 Specify one of the following security levels: 



**none**
 No TLS. TLS will not be used unless enabled for specific
destinations via smtp\_tls\_policy\_maps. 
**may**
 Opportunistic TLS. Use TLS if this is supported by the remote
SMTP server, otherwise use plaintext. Since
sending in the clear is acceptable, demanding stronger than default TLS
security merely reduces interoperability.
The "smtp\_tls\_ciphers" and "smtp\_tls\_protocols" (Postfix ≥ 2.6)
configuration parameters provide control over the protocols and
cipher grade used with opportunistic TLS. With earlier releases the
opportunistic TLS cipher grade is always "export" and no protocols
are disabled.
When TLS handshakes fail, the connection is retried with TLS disabled.
This allows mail delivery to sites with non-interoperable TLS
implementations. 
**encrypt**
Mandatory TLS encryption. Since a minimum
level of security is intended, it is reasonable to be specific about
sufficiently secure protocol versions and ciphers. At this security level
and higher, the main.cf parameters smtp\_tls\_mandatory\_protocols and
smtp\_tls\_mandatory\_ciphers specify the TLS protocols and minimum
cipher grade which the administrator considers secure enough for
mandatory encrypted sessions. This security level is not an appropriate
default for systems delivering mail to the Internet. 
**dane**
Opportunistic DANE TLS. At this security level, the TLS policy
for the destination is obtained via DNSSEC. For TLSA policy to be
in effect, the destination domain's containing DNS zone must be
signed and the Postfix SMTP client's operating system must be
configured to send its DNS queries to a recursive DNS nameserver
that is able to validate the signed records. Each MX host's DNS
zone should also be signed, and should publish DANE TLSA (RFC 7672)
records that specify how that MX host's TLS certificate is to be
verified. TLSA records do not preempt the normal SMTP MX host
selection algorithm, if some MX hosts support TLSA and others do
not, TLS security will vary from delivery to delivery. It is up
to the domain owner to configure their MX hosts and their DNS
sensibly. To configure the Postfix SMTP client for DNSSEC lookups
see the documentation for the smtp\_dns\_support\_level main.cf
parameter. When DNSSEC-validated TLSA records are not found the
effective tls security level is "may". When TLSA records are found,
but are all unusable the effective security level is "encrypt". For
purposes of protocol and cipher selection, the "dane" security level
is treated like a "mandatory" TLS security level, and weak ciphers
and protocols are disabled. Since DANE authenticates server
certificates the "aNULL" cipher-suites are transparently excluded
at this level, no need to configure this manually. RFC 7672 (DANE)
TLS authentication is available with Postfix 2.11 and later. 
**dane-only**
Mandatory DANE TLS. This is just like "dane" above, but DANE
TLSA authentication is required. There is no fallback to "may" or
"encrypt" when TLSA records are missing or unusable. RFC 7672
(DANE) TLS authentication is available with Postfix 2.11 and later.

**fingerprint**
Certificate fingerprint verification.
At this security level, there are no trusted Certification Authorities.
The certificate trust chain, expiration date, etc., are
not checked. Instead, the **smtp\_tls\_fingerprint\_cert\_match**
parameter lists the certificate fingerprint or public key fingerprint
(Postfix 2.9 and later) of the valid server certificate. The digest
algorithm used to calculate the fingerprint is selected by the
**smtp\_tls\_fingerprint\_digest** parameter. Available with Postfix
2.5 and later. 
**verify**
Mandatory TLS verification. At this security
level, DNS MX lookups are trusted to be secure enough, and the name
verified in the server certificate is usually obtained indirectly
via unauthenticated DNS MX lookups. The smtp\_tls\_verify\_cert\_match
parameter controls how the server name is verified. In practice explicit
control over matching is more common at the "secure" level, described
below. This security level is not an appropriate default for systems
delivering mail to the Internet. 
**secure**
Secure-channel TLS. At this security level,
DNS MX lookups, though potentially used to determine the candidate
next-hop gateway IP addresses, are **not** trusted to be secure enough
for TLS peername verification. Instead, the default name verified in
the server certificate is obtained from the next-hop domain as specified
in the smtp\_tls\_secure\_cert\_match configuration parameter. The default
matching rule is that a server certificate matches when its name is equal
to or is a sub-domain of the nexthop domain. This security level is not
an appropriate default for systems delivering mail to the Internet. 


Examples:




```

# No TLS. Formerly: smtp\_use\_tls=no and smtp\_enforce\_tls=no.
smtp\_tls\_security\_level = none

```


```

# Opportunistic TLS.
smtp\_tls\_security\_level = may
# Do not tweak opportunistic ciphers or protocols unless it is essential
# to do so (if a security vulnerability is found in the SSL library that
# can be mitigated by disabling a particular protocol or raising the
# cipher grade).
smtp\_tls\_ciphers = medium
smtp\_tls\_protocols = >=TLSv1
# Legacy (Postfix < 3.6) syntax:
smtp\_tls\_protocols = !SSLv2, !SSLv3

```


```

# Mandatory (high-grade) TLS encryption.
smtp\_tls\_security\_level = encrypt
smtp\_tls\_mandatory\_ciphers = high

```


```

# Authenticated TLS 1.2 or better matching the nexthop domain or a
# subdomain.
smtp\_tls\_security\_level = secure
smtp\_tls\_mandatory\_ciphers = high
smtp\_tls\_mandatory\_protocols = >=TLSv1.2
smtp\_tls\_secure\_cert\_match = nexthop, dot-nexthop

```


```

# Certificate fingerprint verification (Postfix ≥ 2.5).
# The CA-less "fingerprint" security level only scales to a limited
# number of destinations. As a global default rather than a per-site
# setting, this is practical only when mail for all recipients is sent
# to a central mail hub.
relayhost = [mailhub.example.com]
smtp\_tls\_security\_level = fingerprint
smtp\_tls\_mandatory\_protocols = >=TLSv1.2
smtp\_tls\_mandatory\_ciphers = high
smtp\_tls\_fingerprint\_cert\_match =
    3D:95:34:51:...:40:99:C0:C1
    EC:3B:2D:B0:...:A3:9D:72:F6

```

 This feature is available in Postfix 2.3 and later. 



# smtp_dns_support_level (default: empty)
 Level of DNS support in the Postfix SMTP client. With
"smtp\_dns\_support\_level" left at its empty default value, the legacy
"disable\_dns\_lookups" parameter controls whether DNS is enabled in
the Postfix SMTP client, otherwise the legacy parameter is ignored.



 Specify one of the following: 



**disabled**
Disable DNS lookups. No MX lookups are performed and hostname
to address lookups are unconditionally "native". This setting is
not appropriate for hosts that deliver mail to the public Internet.
Some obsolete how-to documents recommend disabling DNS lookups in
some configurations with content\_filters. This is no longer required
and strongly discouraged. 
**enabled**
Enable DNS lookups. Nexthop destination domains not enclosed
in "[]" will be subject to MX lookups. If "dns" and "native" are
included in the "smtp\_host\_lookup" parameter value, DNS will be
queried first to resolve MX-host A records, followed by "native"
lookups if no answer is found in DNS. 
**dnssec**
Enable DNSSEC
lookups. The "dnssec" setting differs from the "enabled" setting
above in the following ways: * Any MX lookups will set
RES\_USE\_DNSSEC and RES\_USE\_EDNS0 to request DNSSEC-validated
responses. If the MX response is DNSSEC-validated the corresponding
hostnames are considered validated.
* The address lookups of
validated hostnames are also validated, (provided of course
"smtp\_host\_lookup" includes "dns", see below).
* Temporary
failures in DNSSEC-enabled hostname-to-address resolution block any
"native" lookups. Additional "native" lookups only happen when
DNSSEC lookups hard-fail (NODATA or NXDOMAIN).

 

 The Postfix SMTP client considers non-MX "[nexthop]" and
"[nexthop]:port" destinations equivalent to statically-validated
MX records of the form "nexthop. IN MX 0 nexthop." Therefore,
with "dnssec" support turned on, validated hostname-to-address
lookups apply to the nexthop domain of any "[nexthop]" or
"[nexthop]:port" destination. This is also true for LMTP "inet:host"
and "inet:host:port" destinations, as LMTP hostnames are never
subject to MX lookups. 


The "dnssec" setting is recommended only if you plan to use the
dane or dane-only TLS security
level, otherwise enabling DNSSEC support in Postfix offers no
additional security. Postfix DNSSEC support relies on an upstream
recursive nameserver that validates DNSSEC signatures. Such a DNS
server will always filter out forged DNS responses, even when Postfix
itself is not configured to use DNSSEC. 


 When using Postfix DANE support the "smtp\_host\_lookup" parameter
should include "dns", as DANE is not applicable
to hosts resolved via "native" lookups. 


 As mentioned above, Postfix is not a validating stub
resolver; it relies on the system's configured DNSSEC-validating
recursive
nameserver to perform all DNSSEC validation. Since this
nameserver's DNSSEC-validated responses will be fully trusted, it
is strongly recommended that the MTA host have a local DNSSEC-validating
recursive caching nameserver listening on a loopback address, and
be configured to use only this nameserver for all lookups. Otherwise,
Postfix may remain subject to man-in-the-middle attacks that forge
responses from the recursive nameserver


DNSSEC support requires a version of Postfix compiled against a
reasonably-modern DNS resolver(3) library that implements the
RES\_USE\_DNSSEC and RES\_USE\_EDNS0 resolver options. 


 This feature is available in Postfix 2.11 and later. 



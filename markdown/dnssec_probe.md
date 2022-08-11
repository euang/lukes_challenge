# dnssec_probe (default: ns:.)
 The DNS query type (default: "ns") and DNS query name (default:
".") that Postfix may use to determine whether DNSSEC validation
is available.



 Background: DNSSEC validation is needed for Postfix DANE support;
this ensures that Postfix receives TLSA records with secure TLS
server certificate info. When DNSSEC validation is unavailable,
mail deliveries using *opportunistic* DANE will not be protected
by server certificate info in TLSA records, and mail deliveries
using *mandatory* DANE will not be made at all. 


 By default, a Postfix process will send a DNSSEC probe after
1) the process made a DNS query that requested DNSSEC validation,
2) the process did not receive a DNSSEC validated response to this
query or to an earlier query, and 3) the process did not already
send a DNSSEC probe. 




 When the DNSSEC probe has no response, or when the response is
not DNSSEC validated, Postfix logs a warning that DNSSEC validation
may be unavailable. 


 Example: 



```

warning: DNSSEC validation may be unavailable
warning: reason: dnssec\_probe 'ns:.' received a response that is not DNSSEC validated
warning: reason: dnssec\_probe 'ns:.' received no response: Server failure

```

 Possible reasons why DNSSEC validation may be unavailable: 


* The local /etc/resolv.conf file specifies a DNS resolver that
does not validate DNSSEC signatures (that's
$queue\_directory/etc/resolv.conf when a Postfix daemon runs in a
chroot jail).
* The local system library does not pass on the "DNSSEC validated"
bit to Postfix, or Postfix does not know how to ask the library to
do that.


 By default, the DNSSEC probe asks for the DNS root zone NS
records, because resolvers should always have that information
cached. If Postfix runs on a network where the DNS root zone is not
reachable, specify a different probe, or specify an empty dnssec\_probe
value to disable the feature. 


 This feature is available in Postfix 3.6 and later. It was backported
to Postfix versions 3.5.9, 3.4.19, 3.3.16. 3.2.21. 



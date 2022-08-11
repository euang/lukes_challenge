# smtp_address_preference (default: any)
 The address type ("ipv6", "ipv4" or "any") that the Postfix
SMTP client will try first, when a destination has IPv6 and IPv4
addresses with equal MX preference. This feature has no effect
unless the inet\_protocols setting enables both IPv4 and IPv6. 


 Postfix SMTP client address preference has evolved. With Postfix
2.8 the default is "ipv6"; earlier implementations are hard-coded
to prefer IPv6 over IPv4. 


 Notes for mail delivery between sites that have both IPv4 and
IPv6 connectivity: 


* The setting "smtp\_address\_preference = ipv6" is unsafe.
It can fail to deliver mail when there is an outage that affects
IPv6, while the destination is still reachable over IPv4.
* The setting "smtp\_address\_preference = any" is safe. With
this, mail will eventually be delivered even if there is an outage
that affects IPv6 or IPv4, as long as it does not affect both.


 This feature is available in Postfix 2.8 and later. 



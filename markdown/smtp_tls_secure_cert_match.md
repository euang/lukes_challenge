# smtp_tls_secure_cert_match (default: nexthop, dot-nexthop)
 How the Postfix SMTP client verifies the server certificate
peername for the "secure" TLS security level. In a "secure" TLS policy table
($smtp\_tls\_policy\_maps) entry the optional "match" attribute
overrides this main.cf setting. 


 This parameter specifies one or more patterns or strategies separated
by commas, whitespace or colons. In the policy table the only valid
separator is the colon character. 


 For a description of the pattern and strategy syntax see the
smtp\_tls\_verify\_cert\_match parameter. The "hostname" strategy should
be avoided in this context, as in the absence of a secure global DNS, using
the results of MX lookups in certificate verification is not immune to active
(man-in-the-middle) attacks on DNS. 



Sample main.cf setting:




> 
> 
> ```
> 
> smtp\_tls\_secure\_cert\_match = nexthop
> 
> ```
> 
> 



Sample policy table override:




> 
> 
> ```
> 
> example.net     secure match=example.com:.example.com
> .example.net    secure match=example.com:.example.com
> 
> ```
> 
> 


 This feature is available in Postfix 2.3 and later. 



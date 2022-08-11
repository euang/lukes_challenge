# smtp_tls_dane_insecure_mx_policy (default: see "postconf -d" output)
 The TLS policy for MX hosts with "secure" TLSA records when the
nexthop destination security level is **dane**, but the MX
record was found via an "insecure" MX lookup. The choices are:




**may**
 The TLSA records will be ignored and TLS will be optional. If
the MX host does not appear to support STARTTLS, or the STARTTLS
handshake fails, mail may be sent in the clear. 
**encrypt**
 The TLSA records will signal a requirement to use TLS. While
TLS encryption will be required, authentication will not be performed.

**dane**
The TLSA records will be used just as with "secure" MX records.
TLS encryption will be required, and, if at least one of the TLSA
records is "usable", authentication will be required. When
authentication succeeds, it will be logged only as "Trusted", not
"Verified", because the MX host name could have been forged. 

 The default setting for Postfix ≥ 3.6 is "dane" with
"smtp\_tls\_security\_level = dane", otherwise "may". This behavior
was backported to Postfix versions 3.5.9, 3.4.19, 3.3.16. 3.2.21.
With earlier Postfix versions the default setting was always "dane".



 Though with "insecure" MX records an active attacker can
compromise SMTP transport security by returning forged MX records,
such attacks are "tamper-evident" since any forged MX hostnames
will be recorded in the mail logs. Attackers who place a high value
on staying hidden may be deterred from forging MX records. 



This feature is available in Postfix 3.1 and later. The **may**
policy is backwards-compatible with earlier Postfix versions.




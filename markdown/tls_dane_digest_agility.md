# tls_dane_digest_agility (default: on)
 Configure RFC7671 DANE TLSA digest algorithm agility.
Do not change this setting from its default value. 


 See Section 8 of RFC7671 for correct key rotation procedures. 


 This feature is available in Postfix 2.11 through 3.1. Postfix
3.2 and later ignore this configuration parameter and behave as
though it were set to "on". 



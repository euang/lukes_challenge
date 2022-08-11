# tls_dane_trust_anchor_digest_enable (default: yes)
 Enable support for RFC 6698 (DANE TLSA) DNS records that contain
digests of trust-anchors with certificate usage "2". Do not change
this setting from its default value. 


 This feature is available in Postfix 2.11 through 3.1. It has
been withdrawn in Postfix 3.2, as trust-anchor TLSA records are now
widely used and have proved sufficiently reliable. Postfix 3.2 and
later ignore this configuration parameter and behaves as though it
were set to "yes". 



# tls_legacy_public_key_fingerprints (default: no)
 A temporary migration aid for sites that use certificate
*public-key* fingerprints with Postfix 2.9.0..2.9.5, which use
an incorrect algorithm. This parameter has no effect on the certificate
fingerprint support that is available since Postfix 2.2. 


 Specify "tls\_legacy\_public\_key\_fingerprints = yes" temporarily,
pending a migration from configuration files with incorrect Postfix
2.9.0..2.9.5 certificate public-key finger prints, to the correct
fingerprints used by Postfix 2.9.6 and later. To compute the correct
certificate public-key fingerprints, see TLS\_README. 


 This feature is available in Postfix 2.9.6 and later. 



# smtp_sasl_tls_verified_security_options (default: $smtp_sasl_tls_security_options)
 The SASL authentication security options that the Postfix SMTP
client uses for TLS encrypted SMTP sessions with a verified server
certificate. 


 When mail is sent to the public MX host for the recipient's
domain, server certificates are by default optional, and delivery
proceeds even if certificate verification fails. For delivery via
a submission service that requires SASL authentication, it may be
appropriate to send plaintext passwords only when the connection
to the server is strongly encrypted **and** the server identity
is verified. 


 The smtp\_sasl\_tls\_verified\_security\_options parameter makes it
possible to only enable plaintext mechanisms when a secure connection
to the server is available. Submission servers subject to this
policy must either have verifiable certificates or offer suitable
non-plaintext SASL mechanisms. 


 This feature is available in Postfix 2.6 and later. 



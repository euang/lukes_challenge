# tls_session_ticket_cipher (default: Postfix ≥ 3.0: aes-256-cbc, Postfix < 3.0: aes-128-cbc)
 Algorithm used to encrypt RFC5077 TLS session tickets. This
algorithm must use CBC mode, have a 128-bit block size, and must
have a key length between 128 and 256 bits. The default is
aes-256-cbc. Overriding the default to choose a different algorithm
is discouraged. 


 Setting this parameter empty disables session ticket support
in the Postfix SMTP server. Another way to disable session ticket
support is via the tls\_ssl\_options parameter. 


 This feature is available in Postfix 3.0 and later. 



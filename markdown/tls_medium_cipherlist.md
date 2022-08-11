# tls_medium_cipherlist (default: see "postconf -d" output)
 The OpenSSL cipherlist for "medium" or higher grade ciphers. This
defines the meaning of the "medium" setting in smtpd\_tls\_ciphers,
smtpd\_tls\_mandatory\_ciphers, smtp\_tls\_ciphers, smtp\_tls\_mandatory\_ciphers,
lmtp\_tls\_ciphers, and lmtp\_tls\_mandatory\_ciphers. This is the
default cipherlist for mandatory TLS encryption in the TLS client
(with anonymous ciphers disabled when verifying server certificates).
This is the default cipherlist for opportunistic TLS with Postfix
releases after the middle of 2015. You are strongly encouraged not
to change this setting. 


 This feature is available in Postfix 2.3 and later. 



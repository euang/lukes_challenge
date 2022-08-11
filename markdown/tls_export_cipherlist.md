# tls_export_cipherlist (default: see "postconf -d" output)
 The OpenSSL cipherlist for "export" or higher grade ciphers. This
defines the meaning of the "export" setting in smtpd\_tls\_ciphers,
smtpd\_tls\_mandatory\_ciphers, smtp\_tls\_ciphers, smtp\_tls\_mandatory\_ciphers,
lmtp\_tls\_ciphers, and lmtp\_tls\_mandatory\_ciphers. With Postfix
releases before the middle of 2015 this is the default cipherlist
for the opportunistic ("may") TLS client security level and also
the default cipherlist for the SMTP server. You are strongly
encouraged not to change this setting. 


 This feature is available in Postfix 2.3 and later. 



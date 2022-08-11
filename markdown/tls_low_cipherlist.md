# tls_low_cipherlist (default: see "postconf -d" output)
 The OpenSSL cipherlist for "low" or higher grade ciphers. This defines
the meaning of the "low" setting in smtpd\_tls\_ciphers,
smtpd\_tls\_mandatory\_ciphers, smtp\_tls\_ciphers, smtp\_tls\_mandatory\_ciphers,
lmtp\_tls\_ciphers, and lmtp\_tls\_mandatory\_ciphers. You are strongly
encouraged not to change this setting. 


 This feature is available in Postfix 2.3 and later. 



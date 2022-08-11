# tls_null_cipherlist (default: eNULL:!aNULL)
 The OpenSSL cipherlist for "NULL" grade ciphers that provide
authentication without encryption. This defines the meaning of the "null"
setting in smtpd\_tls\_mandatory\_ciphers, smtp\_tls\_mandatory\_ciphers and
lmtp\_tls\_mandatory\_ciphers. You are strongly encouraged not to
change this setting. 


 This feature is available in Postfix 2.3 and later. 



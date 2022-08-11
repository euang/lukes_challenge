# smtp_tls_eccert_file (default: empty)
 File with the Postfix SMTP client ECDSA certificate in PEM format.
This file may also contain the Postfix SMTP client ECDSA private key.
With Postfix ≥ 3.4 the preferred way to configure client keys and
certificates is via the "smtp\_tls\_chain\_files" parameter. 


 See the discussion under smtp\_tls\_cert\_file for more details.



 Example: 



```

smtp\_tls\_eccert\_file = /etc/postfix/ecdsa-ccert.pem

```

 This feature is available in Postfix 2.6 and later, when Postfix is
compiled and linked with OpenSSL 1.0.0 or later. 



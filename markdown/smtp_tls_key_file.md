# smtp_tls_key_file (default: $smtp_tls_cert_file)
 File with the Postfix SMTP client RSA private key in PEM format.
This file may be combined with the Postfix SMTP client RSA certificate
file specified with $smtp\_tls\_cert\_file. With Postfix ≥ 3.4 the
preferred way to configure client keys and certificates is via the
"smtp\_tls\_chain\_files" parameter. 


 The private key must be accessible without a pass-phrase, i.e. it
must not be encrypted. File permissions should grant read-only
access to the system superuser account ("root"), and no access
to anyone else. 


 Example: 



```

smtp\_tls\_key\_file = $smtp\_tls\_cert\_file

```

 This feature is available in Postfix 2.2 and later. 



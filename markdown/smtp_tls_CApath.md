# smtp_tls_CApath (default: empty)
 Directory with PEM format Certification Authority certificates
that the Postfix SMTP client uses to verify a remote SMTP server
certificate. Don't forget to create the necessary "hash" links
with, for example, "$OPENSSL\_HOME/bin/c\_rehash /etc/postfix/certs".



 To use this option in chroot mode, this directory (or a copy)
must be inside the chroot jail. 


 Specify "smtp\_tls\_CApath = /path/to/system\_CA\_directory" to
use ONLY the system-supplied default Certification Authority certificates.



 Specify "tls\_append\_default\_CA = no" to prevent Postfix from
appending the system-supplied default CAs and trusting third-party
certificates. 


 Example: 



```

smtp\_tls\_CApath = /etc/postfix/certs

```

 This feature is available in Postfix 2.2 and later. 



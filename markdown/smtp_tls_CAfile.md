# smtp_tls_CAfile (default: empty)
 A file containing CA certificates of root CAs trusted to sign
either remote SMTP server certificates or intermediate CA certificates.
These are loaded into memory before the smtp(8) client enters the
chroot jail. If the number of trusted roots is large, consider using
smtp\_tls\_CApath instead, but note that the latter directory must be
present in the chroot jail if the smtp(8) client is chrooted. This
file may also be used to augment the client certificate trust chain,
but it is best to include all the required certificates directly in
$smtp\_tls\_cert\_file (or, Postfix ≥ 3.4 $smtp\_tls\_chain\_files). 


 Specify "smtp\_tls\_CAfile = /path/to/system\_CA\_file" to use
ONLY the system-supplied default Certification Authority certificates.



 Specify "tls\_append\_default\_CA = no" to prevent Postfix from
appending the system-supplied default CAs and trusting third-party
certificates. 


 Example: 



```

smtp\_tls\_CAfile = /etc/postfix/CAcert.pem

```

 This feature is available in Postfix 2.2 and later. 



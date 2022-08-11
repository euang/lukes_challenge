# smtpd_tls_CApath (default: empty)
 A directory containing (PEM format) CA certificates of root CAs
trusted to sign either remote SMTP client certificates or intermediate CA
certificates. Do not forget to create the necessary "hash" links with,
for example, "$OPENSSL\_HOME/bin/c\_rehash /etc/postfix/certs". To use
smtpd\_tls\_CApath in chroot mode, this directory (or a copy) must be
inside the chroot jail. 


 Specify "smtpd\_tls\_CApath = /path/to/system\_CA\_directory" to
use ONLY the system-supplied default Certification Authority certificates.



 Specify "tls\_append\_default\_CA = no" to prevent Postfix from
appending the system-supplied default CAs and trusting third-party
certificates. 


 By default (see smtpd\_tls\_ask\_ccert), client certificates are
not requested, and smtpd\_tls\_CApath should remain empty. In contrast
to smtpd\_tls\_CAfile, DNs of Certification Authorities installed
in $smtpd\_tls\_CApath are not included in the client certificate
request message. MUAs with multiple client certificates may use the
list of preferred Certification Authorities to select the correct
client certificate. You may want to put your "preferred" CA or
CAs in $smtpd\_tls\_CAfile, and install the remaining trusted CAs in
$smtpd\_tls\_CApath. 


 Example: 



```

smtpd\_tls\_CApath = /etc/postfix/certs

```

 This feature is available in Postfix 2.2 and later. 



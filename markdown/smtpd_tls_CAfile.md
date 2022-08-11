# smtpd_tls_CAfile (default: empty)
 A file containing (PEM format) CA certificates of root CAs trusted
to sign either remote SMTP client certificates or intermediate CA
certificates. These are loaded into memory before the smtpd(8) server
enters the chroot jail. If the number of trusted roots is large, consider
using smtpd\_tls\_CApath instead, but note that the latter directory must
be present in the chroot jail if the smtpd(8) server is chrooted. This
file may also be used to augment the server certificate trust chain,
but it is best to include all the required certificates directly in the
server certificate file. 


 Specify "smtpd\_tls\_CAfile = /path/to/system\_CA\_file" to use ONLY
the system-supplied default Certification Authority certificates.



 Specify "tls\_append\_default\_CA = no" to prevent Postfix from
appending the system-supplied default CAs and trusting third-party
certificates. 


 By default (see smtpd\_tls\_ask\_ccert), client certificates are not
requested, and smtpd\_tls\_CAfile should remain empty. If you do make use
of client certificates, the distinguished names (DNs) of the Certification
Authorities listed in smtpd\_tls\_CAfile are sent to the remote SMTP client
in the client certificate request message. MUAs with multiple client
certificates may use the list of preferred Certification Authorities
to select the correct client certificate. You may want to put your
"preferred" CA or CAs in this file, and install other trusted CAs in
$smtpd\_tls\_CApath. 


 Example: 



```

smtpd\_tls\_CAfile = /etc/postfix/CAcert.pem

```

 This feature is available in Postfix 2.2 and later. 



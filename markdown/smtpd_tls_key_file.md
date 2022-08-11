# smtpd_tls_key_file (default: $smtpd_tls_cert_file)
 File with the Postfix SMTP server RSA private key in PEM format.
This file may be combined with the Postfix SMTP server RSA certificate
file specified with $smtpd\_tls\_cert\_file. With Postfix ≥ 3.4 the
preferred way to configure server keys and certificates is via the
"smtpd\_tls\_chain\_files" parameter. 


 The private key must be accessible without a pass-phrase, i.e. it
must not be encrypted. File permissions should grant read-only
access to the system superuser account ("root"), and no access
to anyone else. 



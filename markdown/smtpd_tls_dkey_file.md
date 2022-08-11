# smtpd_tls_dkey_file (default: $smtpd_tls_dcert_file)
 File with the Postfix SMTP server DSA private key in PEM format.
This file may be combined with the Postfix SMTP server DSA certificate
file specified with $smtpd\_tls\_dcert\_file. The DSA algorithm is obsolete
and should not be used. 


 The private key must be accessible without a pass-phrase, i.e. it
must not be encrypted. File permissions should grant read-only
access to the system superuser account ("root"), and no access
to anyone else. 


 This feature is available in Postfix 2.2 and later. 



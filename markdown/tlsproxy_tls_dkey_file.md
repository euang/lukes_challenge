# tlsproxy_tls_dkey_file (default: $smtpd_tls_dkey_file)
 File with the Postfix tlsproxy(8) server DSA private key in PEM
format. This file may be combined with the Postfix tlsproxy(8) server
DSA certificate file specified with $smtpd\_tls\_dcert\_file. DSA is
obsolete and should not be used. See smtpd\_tls\_dkey\_file for further
details. 


 This feature is available in Postfix 2.8 and later. 



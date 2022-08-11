# tlsproxy_tls_eckey_file (default: $smtpd_tls_eckey_file)
 File with the Postfix tlsproxy(8) server ECDSA private key in PEM
format. This file may be combined with the Postfix tlsproxy(8) server
ECDSA certificate file specified with $smtpd\_tls\_eccert\_file. See
smtpd\_tls\_eckey\_file for further details. With Postfix ≥ 3.4 the
preferred way to configure tlsproxy server keys and certificates is via
the "tlsproxy\_tls\_chain\_files" parameter. 


 This feature is available in Postfix 2.8 and later. 



# tlsproxy_tls_cert_file (default: $smtpd_tls_cert_file)
 File with the Postfix tlsproxy(8) server RSA certificate in PEM
format. This file may also contain the Postfix tlsproxy(8) server
private RSA key. See smtpd\_tls\_cert\_file for further details. With
Postfix ≥ 3.4 the preferred way to configure tlsproxy server keys and
certificates is via the "tlsproxy\_tls\_chain\_files" parameter. 


 This feature is available in Postfix 2.8 and later. 



# tlsproxy_tls_dh512_param_file (default: $smtpd_tls_dh512_param_file)
 File with DH parameters that the Postfix tlsproxy(8) server
should use with export-grade EDH ciphers. See smtpd\_tls\_dh512\_param\_file
for further details. The default SMTP server cipher grade is
"medium" with Postfix releases after the middle of 2015, and as a
result export-grade cipher suites are by default not used. 


 With Postfix ≥ 3.6 export-grade Diffie-Hellman key exchange
is no longer supported, and this parameter is silently ignored. 


 This feature is available in Postfix 2.8 and later. 



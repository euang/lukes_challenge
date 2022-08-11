# smtpd_tls_dh512_param_file (default: empty)
 File with DH parameters that the Postfix SMTP server should
use with export-grade EDH ciphers. The default SMTP server cipher
grade is "medium" with Postfix releases after the middle of 2015,
and as a result export-grade cipher suites are by default not used.



 With Postfix ≥ 3.6 export-grade Diffie-Hellman key exchange
is no longer supported, and this parameter is silently ignored. 


 See also the discussion under the smtpd\_tls\_dh1024\_param\_file
configuration parameter. 


 Example: 



```

smtpd\_tls\_dh512\_param\_file = /etc/postfix/dh\_512.pem

```

This feature is available in Postfix 2.2 and later,
but is ignored in Postfix 3.6 and later.



# smtpd_tls_ask_ccert (default: no)
 Ask a remote SMTP client for a client certificate. This
information is needed for certificate based mail relaying with,
for example, the permit\_tls\_clientcerts feature. 


 Some clients such as Netscape will either complain if no
certificate is available (for the list of CAs in $smtpd\_tls\_CAfile)
or will offer multiple client certificates to choose from. This
may be annoying, so this option is "off" by default. 


 This feature is available in Postfix 2.2 and later. 



# smtpd_tls_wrappermode (default: no)
 Run the Postfix SMTP server in TLS "wrapper" mode,
instead of using the STARTTLS command. 


 If you want to support this service, enable a special port in
master.cf, and specify "-o smtpd\_tls\_wrappermode=yes" on the SMTP
server's command line. Port 465 (submissions/smtps) is reserved for
this purpose. 


 This feature is available in Postfix 2.2 and later. 



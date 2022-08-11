# smtpd_use_tls (default: no)
 Opportunistic TLS: announce STARTTLS support to remote SMTP clients,
but do not require that clients use TLS encryption. 


 Note: when invoked via "**sendmail -bs**", Postfix will never offer
STARTTLS due to insufficient privileges to access the server private
key. This is intended behavior. 


 This feature is available in Postfix 2.2 and later. With
Postfix 2.3 and later use smtpd\_tls\_security\_level instead. 



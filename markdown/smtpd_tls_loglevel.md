# smtpd_tls_loglevel (default: 0)
 Enable additional Postfix SMTP server logging of TLS activity.
Each logging level also includes the information that is logged at
a lower logging level. 



   0 Disable logging of TLS activity. 
   1 Log only a summary message on TLS handshake completion
— no logging of client certificate trust-chain verification errors
if client certificate verification is not required. With Postfix 2.8 and
earlier, log the summary message, peer certificate summary information
and unconditionally log trust-chain verification errors. 
   2 Also log levels during TLS negotiation. 
   3 Also log hexadecimal and ASCII dump of TLS negotiation
process. 
   4 Also log hexadecimal and ASCII dump of complete
transmission after STARTTLS. 

 Do not use "smtpd\_tls\_loglevel = 2" or higher except in case
of problems. Use of loglevel 4 is strongly discouraged. 


 This feature is available in Postfix 2.2 and later. 



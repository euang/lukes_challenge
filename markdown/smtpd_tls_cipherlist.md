# smtpd_tls_cipherlist (default: empty)
 Obsolete Postfix < 2.3 control for the Postfix SMTP server TLS
cipher list. It is easy to create interoperability problems by choosing
a non-default cipher list. Do not use a non-default TLS cipherlist for
MX hosts on the public Internet. Clients that begin the TLS handshake,
but are unable to agree on a common cipher, may not be able to send any
email to the SMTP server. Using a restricted cipher list may be more
appropriate for a dedicated MSA or an internal mailhub, where one can
exert some control over the TLS software and settings of the connecting
clients. 


 **Note:** do not use "" quotes around the parameter value. 


This feature is available with Postfix version 2.2. It is not used with
Postfix 2.3 and later; use smtpd\_tls\_mandatory\_ciphers instead. 



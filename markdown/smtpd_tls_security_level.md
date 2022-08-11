# smtpd_tls_security_level (default: empty)
 The SMTP TLS security level for the Postfix SMTP server; when
a non-empty value is specified, this overrides the obsolete parameters
smtpd\_use\_tls and smtpd\_enforce\_tls. This parameter is ignored with
"smtpd\_tls\_wrappermode = yes". 


 Specify one of the following security levels: 



**none**  TLS will not be used. 
**may**  Opportunistic TLS: announce STARTTLS support
to remote SMTP clients, but do not require that clients use TLS encryption.

**encrypt** Mandatory TLS encryption: announce
STARTTLS support to remote SMTP clients, and require that clients use TLS
encryption. According to RFC 2487 this MUST NOT be applied in case
of a publicly-referenced SMTP server. Instead, this option should
be used only on dedicated servers. 

 Note 1: the "fingerprint", "verify" and "secure" levels are not
supported here.
The Postfix SMTP server logs a warning and uses "encrypt" instead.
To verify remote SMTP client certificates, see TLS\_README for a discussion
of the smtpd\_tls\_ask\_ccert, smtpd\_tls\_req\_ccert, and permit\_tls\_clientcerts
features. 


 Note 2: The parameter setting "smtpd\_tls\_security\_level =
encrypt" implies "smtpd\_tls\_auth\_only = yes".


 Note 3: when invoked via "sendmail -bs", Postfix will never
offer STARTTLS due to insufficient privileges to access the server
private key. This is intended behavior.


 This feature is available in Postfix 2.3 and later. 



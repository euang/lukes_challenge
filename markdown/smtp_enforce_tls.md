# smtp_enforce_tls (default: no)
 Enforcement mode: require that remote SMTP servers use TLS
encryption, and never send mail in the clear. This also requires
that the remote SMTP server hostname matches the information in
the remote server certificate, and that the remote SMTP server
certificate was issued by a CA that is trusted by the Postfix SMTP
client. If the certificate doesn't verify or the hostname doesn't
match, delivery is deferred and mail stays in the queue. 


 The server hostname is matched against all names provided as
dNSNames in the SubjectAlternativeName. If no dNSNames are specified,
the CommonName is checked. The behavior may be changed with the
smtp\_tls\_enforce\_peername option. 


 This option is useful only if you are definitely sure that you
will only connect to servers that support RFC 2487 \_and\_ that
provide valid server certificates. Typical use is for clients that
send all their email to a dedicated mailhub. 


 This feature is available in Postfix 2.2 and later. With
Postfix 2.3 and later use smtp\_tls\_security\_level instead. 



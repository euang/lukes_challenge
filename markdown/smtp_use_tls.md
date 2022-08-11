# smtp_use_tls (default: no)
 Opportunistic mode: use TLS when a remote SMTP server announces
STARTTLS support, otherwise send the mail in the clear. Beware:
some SMTP servers offer STARTTLS even if it is not configured. With
Postfix < 2.3, if the TLS handshake fails, and no other server is
available, delivery is deferred and mail stays in the queue. If this
is a concern for you, use the smtp\_tls\_per\_site feature instead. 


 This feature is available in Postfix 2.2 and later. With
Postfix 2.3 and later use smtp\_tls\_security\_level instead. 



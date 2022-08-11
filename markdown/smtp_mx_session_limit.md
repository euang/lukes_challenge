# smtp_mx_session_limit (default: 2)
 The maximal number of SMTP sessions per delivery request before
the Postfix SMTP client
gives up or delivers to a fall-back relay host, or zero (no
limit). This restriction ignores sessions that fail to complete the
SMTP initial handshake (Postfix version 2.2 and earlier) or that fail to
complete the EHLO and TLS handshake (Postfix version 2.3 and later). 


 This feature is available in Postfix 2.1 and later. 



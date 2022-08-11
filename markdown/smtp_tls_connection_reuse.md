# smtp_tls_connection_reuse (default: no)
 Try to make multiple deliveries per TLS-encrypted connection.
This uses the tlsproxy(8) service to encrypt an SMTP connection,
uses the scache(8) service to save that connection, and relies on
hints from the qmgr(8) daemon. 


 See "Client-side
TLS connection reuse" for background details. 


 This feature is available in Postfix 3.4 and later. 



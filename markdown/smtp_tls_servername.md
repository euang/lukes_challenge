# smtp_tls_servername (default: empty)
 Optional name to send to the remote SMTP server in the TLS Server
Name Indication (SNI) extension. The SNI extension is always on when
DANE is used to authenticate the server, and in that case the SNI name
sent is the one required by RFC7672 and this parameter is ignored. 


 Some SMTP servers use the received SNI name to select an appropriate
certificate chain to present to the client. While this may improve
interoperability with such servers, it may reduce interoperability with
other servers that choose to abort the connection when they don't have a
certificate chain configured for the requested name. Such servers
should select a default certificate chain and continue the handshake,
but some may not. Therefore, absent DANE, no SNI name is sent by
default. 


 The SNI name must be either a valid DNS hostname, or else one of the
special values **hostname** or **nexthop**, which select either the
remote hostname or the nexthop domain respectively. DNS names for SNI must be
in A-label (punycode) form. Invalid DNS names log a configuration error
warning and mail delivery is deferred. 


 Except when using a relayhost to forward all email, the only
sensible non-empty main.cf setting for this parameter is
**hostname**. Other non-empty values are only practical on a
per-destination basis via the **servername** attribute of the Postfix
TLS policy table. When
in doubt, leave this parameter empty, and configure per-destination SNI
as needed. 


 This feature is available in Postfix 3.4 and later. 



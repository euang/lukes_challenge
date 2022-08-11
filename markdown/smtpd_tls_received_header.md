# smtpd_tls_received_header (default: no)
 Request that the Postfix SMTP server produces Received: message
headers that include information about the protocol and cipher used,
as well as the remote SMTP client CommonName and client certificate issuer
CommonName. This is disabled by default, as the information may
be modified in transit through other mail servers. Only information
that was recorded by the final destination can be trusted. 


 This feature is available in Postfix 2.2 and later. 



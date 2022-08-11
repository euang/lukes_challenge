# tlsproxy_tls_mandatory_protocols (default: $smtpd_tls_mandatory_protocols)
 The SSL/TLS protocols accepted by the Postfix tlsproxy(8) server
with mandatory TLS encryption. If the list is empty, the server
supports all available SSL/TLS protocol versions. See
smtpd\_tls\_mandatory\_protocols for further details. 


 This feature is available in Postfix 2.8 and later. 



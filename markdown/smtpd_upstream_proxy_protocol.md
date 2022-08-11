# smtpd_upstream_proxy_protocol (default: empty)
 The name of the proxy protocol used by an optional before-smtpd
proxy agent. When a proxy agent is used, this protocol conveys local
and remote address and port information. Specify
"smtpd\_upstream\_proxy\_protocol = haproxy" to enable the haproxy
protocol; version 2 is supported with Postfix 3.5 and later. 


 NOTE: To use the nginx proxy with smtpd(8), enable the XCLIENT
protocol with smtpd\_authorized\_xclient\_hosts. This supports SASL
authentication in the proxy agent (Postfix 2.9 and later). 




 This feature is available in Postfix 2.10 and later. 



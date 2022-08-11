# tls_fast_shutdown_enable (default: yes)
 A workaround for implementations that hang Postfix while shutting
down a TLS session, until Postfix times out. With this enabled,
Postfix will not wait for the remote TLS peer to respond to a TLS
'close' notification. This behavior is recommended for TLSv1.0 and
later. 



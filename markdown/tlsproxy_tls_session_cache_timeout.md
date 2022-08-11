# tlsproxy_tls_session_cache_timeout (default: $smtpd_tls_session_cache_timeout)
 Obsolete expiration time of Postfix tlsproxy(8) server TLS session
cache information. Since the cache is shared with smtpd(8) and managed
by tlsmgr(8), there is only one expiration time for the SMTP server cache
shared by all three services, namely smtpd\_tls\_session\_cache\_timeout. 


 This feature is available in Postfix 2.8 and later. 



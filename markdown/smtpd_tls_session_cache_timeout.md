# smtpd_tls_session_cache_timeout (default: 3600s)
 The expiration time of Postfix SMTP server TLS session cache
information. A cache cleanup is performed periodically
every $smtpd\_tls\_session\_cache\_timeout seconds. As with
$smtpd\_tls\_session\_cache\_database, this parameter is implemented in the
tlsmgr(8) daemon and therefore per-smtpd-instance master.cf overrides
are not possible. 


 As of Postfix 2.11 this setting cannot exceed 100 days. If set
≤ 0, session caching is disabled, not just via the database, but
also via RFC 5077 TLS session tickets, which don't require server-side
storage. If set to a positive value less than 2 minutes, the minimum
value of 2 minutes is used instead. TLS session tickets require
an OpenSSL library (at least version 0.9.8h) that provides full
support for this TLS extension. 


 Specify a non-negative time value (an integral value plus an optional
one-letter suffix that specifies the time unit). Time units: s
(seconds), m (minutes), h (hours), d (days), w (weeks).
The default time unit is s (seconds). 


 This feature is available in Postfix 2.2 and later, and updated
for TLS session ticket support in Postfix 2.11. 



# smtpd_client_new_tls_session_rate_limit (default: 0)

The maximal number of new (i.e., uncached) TLS sessions that a
remote SMTP client is allowed to negotiate with this service per
time unit. The time unit is specified with the anvil\_rate\_time\_unit
configuration parameter.




By default, a remote SMTP client can negotiate as many new TLS
sessions per time unit as Postfix can accept.




To disable this feature, specify a limit of 0. Otherwise, specify
a limit that is at least the per-client concurrent session limit,
or else legitimate client sessions may be rejected.




WARNING: The purpose of this feature is to limit abuse. It must
not be used to regulate legitimate mail traffic.




This feature is available in Postfix 2.3 and later.




Example:




```

smtpd\_client\_new\_tls\_session\_rate\_limit = 100

```


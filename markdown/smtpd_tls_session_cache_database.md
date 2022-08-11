# smtpd_tls_session_cache_database (default: empty)
 Name of the file containing the optional Postfix SMTP server
TLS session cache. Specify a database type that supports enumeration,
such as **btree** or **sdbm**; there is no need to support
concurrent access. The file is created if it does not exist. The smtpd(8)
daemon does not use this parameter directly, rather the cache is
implemented indirectly in the tlsmgr(8) daemon. This means that
per-smtpd-instance master.cf overrides of this parameter are not
effective. Note that each of the cache databases supported by tlsmgr(8)
daemon: $smtpd\_tls\_session\_cache\_database, $smtp\_tls\_session\_cache\_database
(and with Postfix 2.3 and later $lmtp\_tls\_session\_cache\_database), needs to be
stored separately. It is not at this time possible to store multiple
caches in a single database. 


 Note: **dbm** databases are not suitable. TLS
session objects are too large. 


 As of version 2.5, Postfix no longer uses root privileges when
opening this file. The file should now be stored under the Postfix-owned
data\_directory. As a migration aid, an attempt to open the file
under a non-Postfix directory is redirected to the Postfix-owned
data\_directory, and a warning is logged. 


 As of Postfix 2.11 the preferred mechanism for session resumption
is RFC 5077 TLS session tickets, which don't require server-side
storage. Consequently, for Postfix ≥ 2.11 this parameter should
generally be left empty. TLS session tickets require an OpenSSL
library (at least version 0.9.8h) that provides full support for
this TLS extension. See also smtpd\_tls\_session\_cache\_timeout. 


 Example: 



```

smtpd\_tls\_session\_cache\_database = btree:/var/lib/postfix/smtpd\_scache

```

 This feature is available in Postfix 2.2 and later. 



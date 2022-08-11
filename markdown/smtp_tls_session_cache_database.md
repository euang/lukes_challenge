# smtp_tls_session_cache_database (default: empty)
 Name of the file containing the optional Postfix SMTP client
TLS session cache. Specify a database type that supports enumeration,
such as **btree** or **sdbm**; there is no need to support
concurrent access. The file is created if it does not exist. The smtp(8)
daemon does not use this parameter directly, rather the cache is
implemented indirectly in the tlsmgr(8) daemon. This means that
per-smtp-instance master.cf overrides of this parameter are not effective.
Note that each of the cache databases supported by tlsmgr(8) daemon:
$smtpd\_tls\_session\_cache\_database, $smtp\_tls\_session\_cache\_database
(and with Postfix 2.3 and later $lmtp\_tls\_session\_cache\_database), needs to
be stored separately. It is not at this time possible to store multiple
caches in a single database. 


 Note: **dbm** databases are not suitable. TLS
session objects are too large. 


 As of version 2.5, Postfix no longer uses root privileges when
opening this file. The file should now be stored under the Postfix-owned
data\_directory. As a migration aid, an attempt to open the file
under a non-Postfix directory is redirected to the Postfix-owned
data\_directory, and a warning is logged. 


 Example: 



```

smtp\_tls\_session\_cache\_database = btree:/var/lib/postfix/smtp\_scache

```

 This feature is available in Postfix 2.2 and later. 



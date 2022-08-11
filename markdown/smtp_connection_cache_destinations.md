# smtp_connection_cache_destinations (default: empty)
 Permanently enable SMTP connection caching for the specified
destinations. With SMTP connection caching, a connection is not
closed immediately after completion of a mail transaction. Instead,
the connection is kept open for up to $smtp\_connection\_cache\_time\_limit
seconds. This allows connections to be reused for other deliveries,
and can improve mail delivery performance. 


 Specify a comma or white space separated list of destinations
or pseudo-destinations: 


* if mail is sent without a relay host: a domain name (the
right-hand side of an email address, without the [] around a numeric
IP address),
* if mail is sent via a relay host: a relay host name (without
[] or non-default TCP port), as specified in main.cf or in the
transport map,
* if mail is sent via a UNIX-domain socket: a pathname (without
the unix: prefix),
* a /file/name with domain names and/or relay host names as
defined above,
* a "type:table" with domain names and/or relay host names on
the left-hand side. The right-hand side result from "type:table"
lookups is ignored.


 This feature is available in Postfix 2.2 and later. 



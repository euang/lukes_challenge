# proxy_read_maps (default: see "postconf -d" output)

The lookup tables that the proxymap(8) server is allowed to
access for the read-only service.




Specify zero or more "type:name" lookup tables, separated by
whitespace or comma.
Table references that don't begin with proxy: are ignored.




This feature is available in Postfix 2.0 and later.




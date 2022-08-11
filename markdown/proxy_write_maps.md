# proxy_write_maps (default: see "postconf -d" output)
 The lookup tables that the proxymap(8) server is allowed to
access for the read-write service. Postfix-owned local database
files should be stored under the Postfix-owned data\_directory.
Table references that don't begin with proxy: are ignored. 



This feature is available in Postfix 2.5 and later.




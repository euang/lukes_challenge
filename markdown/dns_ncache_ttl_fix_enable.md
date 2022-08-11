# dns_ncache_ttl_fix_enable (default: no)
 Enable a workaround for future libc incompatibility. The Postfix
implementation of RFC 2308 negative reply caching relies on the
promise that res\_query() and res\_search() invoke res\_send(), which
returns the server response in an application buffer even if the
requested record does not exist. If this promise is broken, specify
"yes" to enable a workaround for DNS reputation lookups. 



This feature is available in Postfix 3.1 and later.




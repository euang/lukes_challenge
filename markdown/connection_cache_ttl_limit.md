# connection_cache_ttl_limit (default: 2s)
 The maximal time-to-live value that the scache(8) connection
cache server
allows. Requests that specify a larger TTL will be stored with the
maximum allowed TTL. The purpose of this additional control is to
protect the infrastructure against careless people. The cache TTL
is already bounded by $max\_idle. 



# postscreen_cache_map (default: btree:$data_directory/postscreen_cache)
 Persistent storage for the postscreen(8) server decisions. 


 To share a postscreen(8) cache between multiple postscreen(8)
instances, use "postscreen\_cache\_map = proxy:btree:/path/to/file".
This requires Postfix version 2.9 or later; earlier proxymap(8)
implementations don't support cache cleanup. For an alternative
approach see the memcache\_table(5) manpage. 


 This feature is available in Postfix 2.8. 



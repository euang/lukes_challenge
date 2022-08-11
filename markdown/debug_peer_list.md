# debug_peer_list (default: empty)
 Optional list of nexthop destination, remote client or server
name or network address patterns that, if matched, cause the verbose
logging level to increase by the amount specified in $debug\_peer\_level.



 Per-nexthop debug logging is available in Postfix 3.6 and later. 


 Specify domain names, network/netmask patterns, "/file/name"
patterns or "type:table" lookup tables. The right-hand side result
from "type:table" lookups is ignored. 


 Pattern matching of domain names is controlled by the presence
or absence of "debug\_peer\_list" in the parent\_domain\_matches\_subdomains
parameter value. 



Examples:




```

debug\_peer\_list = 127.0.0.1
debug\_peer\_list = example.com

```


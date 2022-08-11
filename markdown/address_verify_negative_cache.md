# address_verify_negative_cache (default: yes)

Enable caching of failed address verification probe results. When
this feature is enabled, the cache may pollute quickly with garbage.
When this feature is disabled, Postfix will generate an address
probe for every lookup.




This feature is available in Postfix 2.1 and later.




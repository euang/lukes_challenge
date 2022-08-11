# resolve_null_domain (default: no)
 Resolve an address that ends in the "@" null domain as if the
local hostname were specified, instead of rejecting the address as
invalid. 


 This feature is available in Postfix 2.1 and later.
Earlier versions always resolve the null domain as the local
hostname. 


 The Postfix SMTP server uses this feature to reject mail from
or to addresses that end in the "@" null domain, and from addresses
that rewrite into a form that ends in the "@" null domain. 



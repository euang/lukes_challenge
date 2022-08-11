# virtual_alias_domains (default: $virtual_alias_maps)
 Postfix is the final destination for the specified list of virtual
alias domains, that is, domains for which all addresses are aliased
to addresses in other local or remote domains. The SMTP server
validates recipient addresses with $virtual\_alias\_maps and rejects
non-existent recipients. See also the virtual alias domain class
in the ADDRESS\_CLASS\_README file 



This feature is available in Postfix 2.0 and later. The default
value is backwards compatible with Postfix version 1.1.




The default value is $virtual\_alias\_maps so that you can keep all
information about virtual alias domains in one place. If you have
many users, it is better to separate information that changes more
frequently (virtual address -> local or remote address mapping)
from information that changes less frequently (the list of virtual
domain names).



 Specify a list of host or domain names, "/file/name" or
"type:table" patterns, separated by commas and/or whitespace. A
"/file/name" pattern is replaced by its contents; a "type:table"
lookup table is matched when a table entry matches a host or domain name
(the lookup result is ignored). Continue long lines by starting
the next line with whitespace. Specify "!pattern" to exclude a host
or domain name from the list. The form "!/file/name" is supported
only in Postfix version 2.4 and later. 



See also the VIRTUAL\_README and ADDRESS\_CLASS\_README documents
for further information.




Example:




```

virtual\_alias\_domains = virtual1.tld virtual2.tld

```


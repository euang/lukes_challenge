# smtpd_authorized_xforward_hosts (default: empty)

What remote SMTP clients are allowed to use the XFORWARD feature. This
command forwards information that is used to improve logging after
SMTP-based content filters. See the XFORWARD\_README document for
details.




This feature is available in Postfix 2.1 and later.




By default, no clients are allowed to specify XFORWARD.




Specify a list of network/netmask patterns, separated by commas
and/or whitespace. The mask specifies the number of bits in the
network part of a host address. You can also specify hostnames or
.domain names (the initial dot causes the domain to match any name
below it), "/file/name" or "type:table" patterns. A "/file/name"
pattern is replaced by its contents; a "type:table" lookup table
is matched when a table entry matches a lookup string (the lookup
result is ignored). Continue long lines by starting the next line
with whitespace. Specify "!pattern" to exclude an address or network
block from the list. The form "!/file/name" is supported only in
Postfix version 2.4 and later. 


 Note: IP version 6 address information must be specified inside
[] in the smtpd\_authorized\_xforward\_hosts value, and in
files specified with "/file/name". IP version 6 addresses contain
the ":" character, and would otherwise be confused with a "type:table"
pattern. 



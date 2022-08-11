# smtpd_sasl_exceptions_networks (default: empty)

What remote SMTP clients the Postfix SMTP server will not offer
AUTH support to.




Some clients (Netscape 4 at least) have a bug that causes them to
require a login and password whenever AUTH is offered, whether it's
necessary or not. To work around this, specify, for example,
$mynetworks to prevent Postfix from offering AUTH to local clients.




Specify a list of network/netmask patterns, separated by commas
and/or whitespace. The mask specifies the number of bits in the
network part of a host address. You can also specify "/file/name" or
"type:table" patterns. A "/file/name" pattern is replaced by its
contents; a "type:table" lookup table is matched when a table entry
matches a lookup string (the lookup result is ignored). Continue
long lines by starting the next line with whitespace. Specify
"!pattern" to exclude an address or network block from the list.
The form "!/file/name" is supported only in Postfix version 2.4 and
later. 


 Note: IP version 6 address information must be specified inside
[] in the smtpd\_sasl\_exceptions\_networks value, and in
files specified with "/file/name". IP version 6 addresses contain
the ":" character, and would otherwise be confused with a "type:table"
pattern. 



Example:




```

smtpd\_sasl\_exceptions\_networks = $mynetworks

```


This feature is available in Postfix 2.1 and later.




# virtual_mailbox_maps (default: empty)

Optional lookup tables with all valid addresses in the domains that
match $virtual\_mailbox\_domains.




Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.




In a lookup table, specify a left-hand side of "@domain.tld" to
match any user in the specified domain that does not have a specific
"user@domain.tld" entry.




With the default "virtual\_mailbox\_domains = $virtual\_mailbox\_maps",
lookup tables also need entries with a left-hand side of "domain.tld"
to satisfy virtual\_mailbox\_domain lookups (the right-hand side is
required but will not be used).



 The remainder of this text is specific to the virtual(8) delivery
agent. It does not apply when mail is delivered with a different
mail delivery program. 



The virtual(8) delivery agent uses this table to look up the
per-recipient mailbox or maildir pathname. If the lookup result
ends in a slash ("/"), maildir-style delivery is carried out,
otherwise the path is assumed to specify a UNIX-style mailbox file.
Note that $virtual\_mailbox\_base is unconditionally prepended to
this path.




When a recipient address has an optional address extension
(user+foo@domain.tld), the virtual(8) delivery agent looks up
the full address first, and when the lookup fails, it looks up the
unextended address (user@domain.tld).




Note 1: for security reasons, the virtual(8) delivery agent disallows
regular expression substitution of $1 etc. in regular expression
lookup tables, because that would open a security hole.




Note 2: for security reasons, the virtual(8) delivery agent will
silently ignore requests to use the proxymap(8) server. Instead
it will open the table directly. Before Postfix version 2.2, the
virtual(8) delivery agent will terminate with a fatal error.




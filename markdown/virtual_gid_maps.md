# virtual_gid_maps (default: empty)

Lookup tables with the per-recipient group ID for virtual(8) mailbox
delivery.



 This parameter is specific to the virtual(8) delivery agent.
It does not apply when mail is delivered with a different mail
delivery program. 



Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.




In a lookup table, specify a left-hand side of "@domain.tld" to
match any user in the specified domain that does not have a specific
"user@domain.tld" entry.




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




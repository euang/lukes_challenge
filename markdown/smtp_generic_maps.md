# smtp_generic_maps (default: empty)
 Optional lookup tables that perform address rewriting in the
Postfix SMTP client, typically to transform a locally valid address into
a globally valid address when sending mail across the Internet.
This is needed when the local machine does not have its own Internet
domain name, but uses something like *localdomain.local*
instead. 



Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.



 The table format and lookups are documented in generic(5);
examples are shown in the ADDRESS\_REWRITING\_README and
STANDARD\_CONFIGURATION\_README documents. 


 This feature is available in Postfix 2.2 and later. 



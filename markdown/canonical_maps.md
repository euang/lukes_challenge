# canonical_maps (default: empty)

Optional address mapping lookup tables for message headers and
envelopes. The mapping is applied to both sender and recipient
addresses, in both envelopes and in headers, as controlled
with the canonical\_classes parameter. This is typically used
to clean up dirty addresses from legacy mail systems, or to replace
login names by Firstname.Lastname. The table format and lookups
are documented in canonical(5). For an overview of Postfix address
manipulations see the ADDRESS\_REWRITING\_README document.




Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.
Note: these lookups are recursive.




If you use this feature, run "**postmap /etc/postfix/canonical**" to
build the necessary DBM or DB file after every change. The changes
will become visible after a minute or so. Use "**postfix reload**"
to eliminate the delay.



 Note: with Postfix version 2.2, message header address mapping
happens only when message header address rewriting is enabled: 


* The message is received with the Postfix sendmail(1) command,
* The message is received from a network client that matches
$local\_header\_rewrite\_clients,
* The message is received from the network, and the
remote\_header\_rewrite\_domain parameter specifies a non-empty value.


 To get the behavior before Postfix version 2.2, specify
"local\_header\_rewrite\_clients = static:all". 



Examples:




```

canonical\_maps = dbm:/etc/postfix/canonical
canonical\_maps = hash:/etc/postfix/canonical

```


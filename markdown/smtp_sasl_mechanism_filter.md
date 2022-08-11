# smtp_sasl_mechanism_filter (default: empty)

If non-empty, a Postfix SMTP client filter for the remote SMTP
server's list of offered SASL mechanisms. Different client and
server implementations may support different mechanism lists; by
default, the Postfix SMTP client will use the intersection of the
two. smtp\_sasl\_mechanism\_filter specifies an optional third mechanism
list to intersect with. 


 Specify mechanism names, "/file/name" patterns or "type:table"
lookup tables. The right-hand side result from "type:table" lookups
is ignored. Specify "!pattern" to exclude a mechanism name from the
list. The form "!/file/name" is supported only in Postfix version
2.4 and later. 


 This feature is available in Postfix 2.2 and later. 



Examples:




```

smtp\_sasl\_mechanism\_filter = plain, login
smtp\_sasl\_mechanism\_filter = /etc/postfix/smtp\_mechs
smtp\_sasl\_mechanism\_filter = !gssapi, !login, static:rest

```


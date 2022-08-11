# smtpd_sasl_mechanism_filter (default: !external, static:rest)
 If non-empty, a filter for the SASL mechanism names that the
Postfix SMTP server will announce in the EHLO response. By default,
the Postfix SMTP server will not announce the EXTERNAL mechanism,
because Postfix support for that is not implemented. 


 Specify mechanism names, "/file/name" patterns, or "type:table"
lookup tables, separated by comma or whitespace. The right-hand
side result from "type:table" lookups is ignored. Specify "!pattern"
to exclude a mechanism name from the list. 



Examples:




```

smtpd\_sasl\_mechanism\_filter = !external, !gssapi, static:rest
smtpd\_sasl\_mechanism\_filter = login, plain
smtpd\_sasl\_mechanism\_filter = /etc/postfix/smtpd\_mechs

```

 This feature is available in Postfix 3.6 and later. 



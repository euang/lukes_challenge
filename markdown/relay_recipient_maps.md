# relay_recipient_maps (default: empty)
 Optional lookup tables with all valid addresses in the domains
that match $relay\_domains. Specify @domain as a wild-card for
domains that have no valid recipient list, and become a source of
backscatter mail: Postfix accepts spam for non-existent recipients
and then floods innocent people with undeliverable mail. Technically,
tables
listed with $relay\_recipient\_maps are used as lists: Postfix needs
to know only if a lookup string is found or not, but it does not
use the result from the table lookup. 



Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.




If this parameter is non-empty, then the Postfix SMTP server will reject
mail to unknown relay users. This feature is off by default.




See also the relay domains address class in the ADDRESS\_CLASS\_README
file.




Example:




```

relay\_recipient\_maps = hash:/etc/postfix/relay\_recipients

```


This feature is available in Postfix 2.0 and later.




# sender_canonical_maps (default: empty)

Optional address mapping lookup tables for envelope and header
sender addresses.
The table format and lookups are documented in canonical(5).




Example: you want to rewrite the SENDER address "user@ugly.domain"
to "user@pretty.domain", while still being able to send mail to
the RECIPIENT address "user@ugly.domain".




Note: $sender\_canonical\_maps is processed before $canonical\_maps.




Example:




```

sender\_canonical\_maps = hash:/etc/postfix/sender\_canonical

```


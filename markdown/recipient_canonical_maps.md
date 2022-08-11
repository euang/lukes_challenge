# recipient_canonical_maps (default: empty)

Optional address mapping lookup tables for envelope and header
recipient addresses.
The table format and lookups are documented in canonical(5).




Note: $recipient\_canonical\_maps is processed before $canonical\_maps.




Example:




```

recipient\_canonical\_maps = hash:/etc/postfix/recipient\_canonical

```


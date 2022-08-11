# virtual_alias_maps (default: $virtual_maps)

Optional lookup tables that alias specific mail addresses or domains
to other local or remote addresses. The table format and lookups
are documented in virtual(5). For an overview of Postfix address
manipulations see the ADDRESS\_REWRITING\_README document.




This feature is available in Postfix 2.0 and later. The default
value is backwards compatible with Postfix version 1.1.




Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.
Note: these lookups are recursive.




If you use this feature with indexed files, run "**postmap
/etc/postfix/virtual**" after changing the file.




Examples:




```

virtual\_alias\_maps = dbm:/etc/postfix/virtual
virtual\_alias\_maps = hash:/etc/postfix/virtual

```


# masquerade_exceptions (default: empty)

Optional list of user names that are not subjected to address
masquerading, even when their addresses match $masquerade\_domains.




By default, address masquerading makes no exceptions.




Specify a list of user names, "/file/name" or "type:table" patterns,
separated by commas and/or whitespace. The list is matched left to
right, and the search stops on the first match. A "/file/name"
pattern is replaced
by its contents; a "type:table" lookup table is matched when a name
matches a lookup key (the lookup result is ignored). Continue long
lines by starting the next line with whitespace. Specify "!pattern"
to exclude a name from the list. The form "!/file/name" is supported
only in Postfix version 2.4 and later. 



Examples:




```

masquerade\_exceptions = root, mailer-daemon
masquerade\_exceptions = root

```


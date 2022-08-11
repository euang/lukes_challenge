# address_verify_map (default: see "postconf -d" output)

Lookup table for persistent address verification status
storage. The table is maintained by the verify(8) service, and
is opened before the process releases privileges.




The lookup table is persistent by default (Postfix 2.7 and later).
Specify an empty table name to keep the information in volatile
memory which is lost after "**postfix reload**" or "**postfix
stop**". This is the default with Postfix version 2.6 and earlier.




Specify a location in a file system that will not fill up. If the
database becomes corrupted, the world comes to an end. To recover,
delete (NOT: truncate) the file and do "**postfix reload**".



 Postfix daemon processes do not use root privileges when opening
this file (Postfix 2.5 and later). The file must therefore be
stored under a Postfix-owned directory such as the data\_directory.
As a migration aid, an attempt to open the file under a non-Postfix
directory is redirected to the Postfix-owned data\_directory, and a
warning is logged. 



Examples:




```

address\_verify\_map = hash:/var/lib/postfix/verify
address\_verify\_map = btree:/var/lib/postfix/verify

```


This feature is available in Postfix 2.1 and later.




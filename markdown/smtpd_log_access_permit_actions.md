# smtpd_log_access_permit_actions (default: empty)
 Enable logging of the named "permit" actions in SMTP server
access lists (by default, the SMTP server logs "reject" actions but
not "permit" actions). This feature does not affect conditional
actions such as "defer\_if\_permit". 


 Specify a list of "permit" action names, "/file/name" or
"type:table" patterns, separated by commas and/or whitespace. The
list is matched left to right, and the search stops on the first
match. A "/file/name" pattern is replaced by its contents; a
"type:table" lookup table is matched when a name matches a lookup
key (the lookup result is ignored). Continue long lines by starting
the next line with whitespace. Specify "!pattern" to exclude a name
from the list. 


 Examples: 



```

/etc/postfix/main.cf:
    # Log all "permit" actions.
    smtpd\_log\_access\_permit\_actions = static:all

```


```

/etc/postfix/main.cf:
    # Log "permit\_dnswl\_client" only.
    smtpd\_log\_access\_permit\_actions = permit\_dnswl\_client

```

 This feature is available in Postfix 2.10 and later. 



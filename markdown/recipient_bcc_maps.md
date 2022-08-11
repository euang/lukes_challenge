# recipient_bcc_maps (default: empty)

Optional BCC (blind carbon-copy) address lookup tables, indexed by
recipient address. The BCC address (multiple results are not
supported) is added when mail enters from outside of Postfix.




Specify zero or more "type:name" lookup tables, separated by
whitespace or comma. Tables will be searched in the specified order
until a match is found.




The table search order is as follows:



* Look up the "user+extension@domain.tld" address including the
optional address extension.
* Look up the "user@domain.tld" address without the optional
address extension.
* Look up the "user+extension" address local part when the
recipient domain equals $myorigin, $mydestination, $inet\_interfaces
or $proxy\_interfaces.
* Look up the "user" address local part when the recipient domain
equals $myorigin, $mydestination, $inet\_interfaces or $proxy\_interfaces.
* Look up the "@domain.tld" part.



Note: with Postfix 2.3 and later the BCC address is added as if it
was specified with NOTIFY=NONE. The sender will not be notified
when the BCC address is undeliverable, as long as all down-stream
software implements RFC 3461.




Note: with Postfix 2.2 and earlier the sender will unconditionally
be notified when the BCC address is undeliverable.



 Note: automatic BCC recipients are produced only for new mail.
To avoid mailer loops, automatic BCC recipients are not generated
after Postfix forwards mail internally, or after Postfix generates
mail itself. 



Example:




```

recipient\_bcc\_maps = hash:/etc/postfix/recipient\_bcc

```


After a change, run "**postmap /etc/postfix/recipient\_bcc**".




This feature is available in Postfix 2.1 and later.




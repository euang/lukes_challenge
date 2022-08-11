# address_verify_poll_count (default: normal: 3, overload: 1)

How many times to query the verify(8) service for the completion
of an address verification request in progress.



 By default, the Postfix SMTP server polls the verify(8) service
up to three times under non-overload conditions, and only once when
under overload. With Postfix version 2.5 and earlier, the SMTP
server always polls the verify(8) service up to three times by
default. 



Specify 1 to implement a crude form of greylisting, that is, always
defer the first delivery request for a new address.




Examples:




```

# Postfix ≤ 2.6 default
address\_verify\_poll\_count = 3
# Poor man's greylisting
address\_verify\_poll\_count = 1

```


This feature is available in Postfix 2.1 and later.




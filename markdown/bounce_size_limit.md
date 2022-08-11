# bounce_size_limit (default: 50000)
 The maximal amount of original message text that is sent in a
non-delivery notification. Specify a byte count. A message is
returned as either message/rfc822 (the complete original) or as
text/rfc822-headers (the headers only). With Postfix version 2.4
and earlier, a message is always returned as message/rfc822 and is
truncated when it exceeds the size limit.



 Notes: 


* If you increase this limit, then you should increase the
mime\_nesting\_limit value proportionally.
* Be careful when making changes. Excessively large values
will result in the loss of non-delivery notifications, when a bounce
message size exceeds a local or remote MTA's message size limit.



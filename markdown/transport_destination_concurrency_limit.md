# transport_destination_concurrency_limit (default: $default_destination_concurrency_limit)
 A transport-specific override for the
default\_destination\_concurrency\_limit parameter value, where
*transport* is the master.cf name of the message delivery
transport. 


 Note: some *transport*\_destination\_concurrency\_limit
parameters will not show up in "postconf" command output before
Postfix version 2.9. This limitation applies to many parameters
whose name is a combination of a master.cf service name and a
built-in suffix (in this case: "\_destination\_concurrency\_limit").




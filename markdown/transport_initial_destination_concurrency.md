# transport_initial_destination_concurrency (default: $initial_destination_concurrency)
 A transport-specific override for the initial\_destination\_concurrency
parameter value, where *transport* is the master.cf name of
the message delivery transport. 


 Note: some *transport*\_initial\_destination\_concurrency
parameters will not show up in "postconf" command output before
Postfix version 2.9. This limitation applies to many parameters
whose name is a combination of a master.cf service name and a
built-in suffix (in this case: "\_initial\_destination\_concurrency").



 This feature is available in Postfix 2.5 and later. 



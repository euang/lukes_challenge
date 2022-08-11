# transport_destination_concurrency_failed_cohort_limit (default: $default_destination_concurrency_failed_cohort_limit)
 A transport-specific override for the
default\_destination\_concurrency\_failed\_cohort\_limit parameter value,
where *transport* is the master.cf name of the message delivery
transport. 


 Note: some *transport*\_destination\_concurrency\_failed\_cohort\_limit
parameters will not show up in "postconf" command output before
Postfix version 2.9. This limitation applies to many parameters
whose name is a combination of a master.cf service name and a
built-in suffix (in this case:
"\_destination\_concurrency\_failed\_cohort\_limit"). 


 This feature is available in Postfix 2.5 and later. 



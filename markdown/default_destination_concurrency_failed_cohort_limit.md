# default_destination_concurrency_failed_cohort_limit (default: 1)
 How many pseudo-cohorts must suffer connection or handshake
failure before a specific destination is considered unavailable
(and further delivery is suspended). Specify zero to disable this
feature. A destination's pseudo-cohort failure count is reset each
time a delivery completes without connection or handshake failure
for that specific destination. 


 A pseudo-cohort is the number of deliveries equal to a destination's
delivery concurrency. 


 Use *transport*\_destination\_concurrency\_failed\_cohort\_limit to specify
a transport-specific override, where *transport* is the master.cf
name of the message delivery transport. 


 This feature is available in Postfix 2.5. The default setting
is compatible with earlier Postfix versions. 



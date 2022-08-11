# default_destination_concurrency_negative_feedback (default: 1)
 The per-destination amount of delivery concurrency negative
feedback, after a delivery completes with a connection or handshake
failure. Feedback values are in the range 0..1 inclusive. With
negative feedback, concurrency is decremented at the beginning of
a sequence of length 1/feedback. This is unlike positive feedback,
where concurrency is incremented at the end of a sequence of length
1/feedback. 


 As of Postfix version 2.5, negative feedback cannot reduce
delivery concurrency to zero. Instead, a destination is marked
dead (further delivery suspended) after the failed pseudo-cohort
count reaches $default\_destination\_concurrency\_failed\_cohort\_limit
(or $*transport*\_destination\_concurrency\_failed\_cohort\_limit).
To make the scheduler completely immune to connection or handshake
failures, specify a zero feedback value and a zero failed pseudo-cohort
limit. 


 Specify one of the following forms: 



 ***number***  
 ***number* / *number***  
 Constant feedback. The value must be in the range 0..1 inclusive.
The default setting of "1" is compatible with Postfix versions
before 2.5, where a destination's delivery concurrency is throttled
down to zero (and further delivery suspended) after a single failed
pseudo-cohort. 
 ***number* / concurrency**  
 Variable feedback of "*number* / (delivery concurrency)".
The *number* must be in the range 0..1 inclusive. With
*number* equal to "1", a destination's delivery concurrency
is decremented by 1 after each failed pseudo-cohort. 

 A pseudo-cohort is the number of deliveries equal to a destination's
delivery concurrency. 


 Use *transport*\_destination\_concurrency\_negative\_feedback
to specify a transport-specific override, where *transport*
is the master.cf
name of the message delivery transport. 


 This feature is available in Postfix 2.5. The default setting
is compatible with earlier Postfix versions. 



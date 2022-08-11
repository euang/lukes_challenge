# default_destination_concurrency_positive_feedback (default: 1)
 The per-destination amount of delivery concurrency positive
feedback, after a delivery completes without connection or handshake
failure. Feedback values are in the range 0..1 inclusive. The
concurrency increases until it reaches the per-destination maximal
concurrency limit. With positive feedback, concurrency is incremented
at the end of a sequence with length 1/feedback. This is unlike
negative feedback, where concurrency is decremented at the start
of a sequence of length 1/feedback. 


 Specify one of the following forms: 



 ***number***  
 ***number* / *number***  
 Constant feedback. The value must be in the range 0..1
inclusive. The default setting of "1" is compatible with Postfix
versions before 2.5, where a destination's delivery concurrency
doubles after each successful pseudo-cohort. 
 ***number* / concurrency**  
 Variable feedback of "*number* / (delivery concurrency)".
The *number* must be in the range 0..1 inclusive. With
*number* equal to "1", a destination's delivery concurrency
is incremented by 1 after each successful pseudo-cohort. 

 A pseudo-cohort is the number of deliveries equal to a destination's
delivery concurrency. 


 Use *transport*\_destination\_concurrency\_positive\_feedback
to specify a transport-specific override, where *transport*
is the master.cf name of the message delivery transport. 


 This feature is available in Postfix 2.5 and later. 



# transport_recipient_refill_delay (default: $default_recipient_refill_delay)
 A transport-specific override for the default\_recipient\_refill\_delay
parameter value, where *transport* is the master.cf name of
the message delivery transport. 


 Note: *transport*\_recipient\_refill\_delay parameters will
not show up in "postconf" command output before Postfix version
2.9. This limitation applies to many parameters whose name is a
combination of a master.cf service name and a built-in suffix (in
this case: "\_recipient\_refill\_delay"). 


 This feature is available in Postfix 2.4 and later. 



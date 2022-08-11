# transport_delivery_slot_discount (default: $default_delivery_slot_discount)
 A transport-specific override for the default\_delivery\_slot\_discount
parameter value, where *transport* is the master.cf name of
the message delivery transport. 


 Note: *transport*\_delivery\_slot\_discount parameters will
not show up in "postconf" command output before Postfix version
2.9. This limitation applies to many parameters whose name is a
combination of a master.cf service name and a built-in suffix (in
this case: "\_delivery\_slot\_discount"). 



# unverified_recipient_reject_code (default: 450)

The numerical Postfix SMTP server response when a recipient address
is rejected by the reject\_unverified\_recipient restriction.




Unlike elsewhere in Postfix, you can specify 250 in order to
accept the address anyway.




Do not change this unless you have a complete understanding of RFC 5321.




This feature is available in Postfix 2.1 and later.




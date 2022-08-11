# unverified_recipient_defer_code (default: 450)

The numerical Postfix SMTP server response when a recipient address
probe fails due to a temporary error condition.




Unlike elsewhere in Postfix, you can specify 250 in order to
accept the address anyway.




Do not change this unless you have a complete understanding of RFC 5321.




This feature is available in Postfix 2.6 and later.




# smtpd_reject_unlisted_recipient (default: yes)

Request that the Postfix SMTP server rejects mail for unknown
recipient addresses, even when no explicit reject\_unlisted\_recipient
access restriction is specified. This prevents the Postfix queue
from filling up with undeliverable MAILER-DAEMON messages.



 An address is considered "unknown" when 1) it does not match a
virtual(5) alias or canonical(5) mapping, and 2) the address is not
valid for its address class. For a definition of class-based address
validation, see 
ADDRESS\_CLASS\_README. 



This feature is available in Postfix 2.1 and later.




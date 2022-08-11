# smtpd_reject_unlisted_sender (default: no)
 Request that the Postfix SMTP server rejects mail from unknown
sender addresses, even when no explicit reject\_unlisted\_sender
access restriction is specified. This can slow down an explosion
of forged mail from worms or viruses. 


 An address is considered "unknown" when 1) it does not match a
virtual(5) alias or canonical(5) mapping, and 2) the address is not
valid for its address class. For a definition of class-based address
validation, see 
ADDRESS\_CLASS\_README. 



This feature is available in Postfix 2.1 and later.




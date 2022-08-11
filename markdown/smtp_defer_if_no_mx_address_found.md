# smtp_defer_if_no_mx_address_found (default: no)

Defer mail delivery when no MX record resolves to an IP address.




The default (no) is to return the mail as undeliverable. With older
Postfix versions the default was to keep trying to deliver the mail
until someone fixed the MX record or until the mail was too old.




Note: the Postfix SMTP client always ignores MX records with equal
or worse preference
than the local MTA itself.




This feature is available in Postfix 2.1 and later.




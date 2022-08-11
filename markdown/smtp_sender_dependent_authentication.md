# smtp_sender_dependent_authentication (default: no)

Enable sender-dependent authentication in the Postfix SMTP client; this is
available only with SASL authentication, and disables SMTP connection
caching to ensure that mail from different senders will use the
appropriate credentials. 



This feature is available in Postfix 2.3 and later.




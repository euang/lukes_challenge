# smtp_connection_cache_on_demand (default: yes)
 Temporarily enable SMTP connection caching while a destination
has a high volume of mail in the active queue. With SMTP connection
caching, a connection is not closed immediately after completion
of a mail transaction. Instead, the connection is kept open for
up to $smtp\_connection\_cache\_time\_limit seconds. This allows
connections to be reused for other deliveries, and can improve mail
delivery performance. 


 This feature is available in Postfix 2.2 and later. 



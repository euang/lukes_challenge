# smtpd_peername_lookup (default: yes)
 Attempt to look up the remote SMTP client hostname, and verify that
the name matches the client IP address. A client name is set to
"unknown" when it cannot be looked up or verified, or when name
lookup is disabled. Turning off name lookup reduces delays due to
DNS lookup and increases the maximal inbound delivery rate. 


 This feature is available in Postfix 2.3 and later. 



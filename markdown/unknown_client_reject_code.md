# unknown_client_reject_code (default: 450)

The numerical Postfix SMTP server response code when a client
without valid address <=> name mapping is rejected by the
reject\_unknown\_client\_hostname restriction. The SMTP server always replies
with 450 when the mapping failed due to a temporary error condition.




Do not change this unless you have a complete understanding of RFC 5321.




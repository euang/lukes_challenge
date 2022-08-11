# smtp_tls_block_early_mail_reply (default: no)
 Try to detect a mail hijacking attack based on a TLS protocol
vulnerability (CVE-2009-3555), where an attacker prepends malicious
HELO, MAIL, RCPT, DATA commands to a Postfix SMTP client TLS session.
The attack would succeed with non-Postfix SMTP servers that reply
to the malicious HELO, MAIL, RCPT, DATA commands after negotiating
the Postfix SMTP client TLS session. 


 This feature is available in Postfix 2.7. 



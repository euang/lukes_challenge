# smtp_always_send_ehlo (default: yes)

Always send EHLO at the start of an SMTP session.




With "smtp\_always\_send\_ehlo = no", the Postfix SMTP client sends
EHLO only when
the word "ESMTP" appears in the server greeting banner (example:
220 spike.porcupine.org ESMTP Postfix).




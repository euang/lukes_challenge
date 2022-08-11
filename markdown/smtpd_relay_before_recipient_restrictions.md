# smtpd_relay_before_recipient_restrictions (default: see "postconf -d" output)
 Evaluate smtpd\_relay\_restrictions before smtpd\_recipient\_restrictions.
Historically, smtpd\_relay\_restrictions was evaluated after
smtpd\_recipient\_restrictions, contradicting documented behavior. 


 Background: the smtpd\_relay\_restrictions feature is primarily
designed to enforce a mail relaying policy, while
smtpd\_recipient\_restrictions is primarily designed to enforce spam
blocking policy. Both are evaluated while replying to the RCPT TO
command, and both support the same features. 


 This feature is available in Postfix 3.6 and later. 



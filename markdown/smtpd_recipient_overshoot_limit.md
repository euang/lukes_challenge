# smtpd_recipient_overshoot_limit (default: 1000)
 The number of recipients that a remote SMTP client can send in
excess of the limit specified with $smtpd\_recipient\_limit, before
the Postfix SMTP server increments the per-session error count
for each excess recipient. 



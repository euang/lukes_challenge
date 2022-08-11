# smtpd_delay_open_until_valid_rcpt (default: yes)
 Postpone the start of an SMTP mail transaction until a valid
RCPT TO command is received. Specify "no" to create a mail transaction
as soon as the Postfix SMTP server receives a valid MAIL FROM
command. 


 With sites that reject lots of mail, the default setting reduces
the use of
disk, CPU and memory resources. The downside is that rejected
recipients are logged with NOQUEUE instead of a mail transaction
ID. This complicates the logfile analysis of multi-recipient mail.



 This feature is available in Postfix 2.3 and later. 



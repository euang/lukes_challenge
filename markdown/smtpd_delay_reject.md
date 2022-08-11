# smtpd_delay_reject (default: yes)

Wait until the RCPT TO command before evaluating
$smtpd\_client\_restrictions, $smtpd\_helo\_restrictions and
$smtpd\_sender\_restrictions, or wait until the ETRN command before
evaluating $smtpd\_client\_restrictions and $smtpd\_helo\_restrictions.




This feature is turned on by default because some clients apparently
mis-behave when the Postfix SMTP server rejects commands before
RCPT TO.




The default setting has one major benefit: it allows Postfix to log
recipient address information when rejecting a client name/address
or sender address, so that it is possible to find out whose mail
is being rejected.




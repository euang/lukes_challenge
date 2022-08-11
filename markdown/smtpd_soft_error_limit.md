# smtpd_soft_error_limit (default: 10)

The number of errors a remote SMTP client is allowed to make without
delivering mail before the Postfix SMTP server slows down all its
responses.



* With Postfix version 2.1 and later, when the error count
is > $smtpd\_soft\_error\_limit, the Postfix SMTP server
delays all responses by $smtpd\_error\_sleep\_time.
* With Postfix versions 2.0 and earlier, when the error count
is > $smtpd\_soft\_error\_limit, the Postfix SMTP server delays all
responses by the larger of (number of errors) seconds or
$smtpd\_error\_sleep\_time.
* With Postfix versions 2.0 and earlier, when the error count
is ≤ $smtpd\_soft\_error\_limit, the Postfix SMTP server delays 4XX
and 5XX responses by $smtpd\_error\_sleep\_time.



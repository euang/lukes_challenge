# smtpd_hard_error_limit (default: normal: 20, overload: 1)

The maximal number of errors a remote SMTP client is allowed to
make without delivering mail. The Postfix SMTP server disconnects
when the limit is reached. Normally the default limit is 20, but
it changes under overload to just 1. With Postfix 2.5 and earlier,
the SMTP server always allows up to 20 errors by default.
Valid values are greater than zero.





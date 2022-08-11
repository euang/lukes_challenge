# smtpd_junk_command_limit (default: normal: 100, overload: 1)

The number of junk commands (NOOP, VRFY, ETRN or RSET) that a remote
SMTP client can send before the Postfix SMTP server starts to
increment the error counter with each junk command. The junk
command count is reset after mail is delivered. See also the
smtpd\_error\_sleep\_time and smtpd\_soft\_error\_limit configuration
parameters. Normally the default limit is 100, but it changes under
overload to just 1. With Postfix 2.5 and earlier, the SMTP server
always allows up to 100 junk commands by default. 



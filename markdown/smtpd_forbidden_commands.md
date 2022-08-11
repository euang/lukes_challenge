# smtpd_forbidden_commands (default: CONNECT GET POST regexp:{{/^[^A-Z]/ Bogus}})

List of commands that cause the Postfix SMTP server to immediately
terminate the session with a 221 code. This can be used to disconnect
clients that obviously attempt to abuse the system. In addition to the
commands listed in this parameter, commands that follow the "Label:"
format of message headers will also cause a disconnect. With Postfix
versions 3.6 and earlier, the default value is "CONNECT GET POST".




This feature is available in Postfix 2.2 and later.




Support for inline regular expressions was added in Postfix version
3.7. See regexp\_table(5) for a description of the syntax and features.




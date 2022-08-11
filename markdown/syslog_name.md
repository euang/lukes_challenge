# syslog_name (default: see "postconf -d" output)

A prefix that is prepended to the process name in syslog
records, so that, for example, "smtpd" becomes "prefix/smtpd".




Warning: a non-default syslog\_name setting takes effect only after
a Postfix process has completed initialization. Errors during
process initialization will be logged with the default name. Examples
are errors while parsing the command line arguments, and errors
while accessing the Postfix main.cf configuration file.




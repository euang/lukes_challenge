# syslog_facility (default: mail)

The syslog facility of Postfix logging. Specify a facility as
defined in syslog.conf(5). The default facility is "mail".




Warning: a non-default syslog\_facility setting takes effect only
after a Postfix process has completed initialization. Errors during
process initialization will be logged with the default facility.
Examples are errors while parsing the command line arguments, and
errors while accessing the Postfix main.cf configuration file.




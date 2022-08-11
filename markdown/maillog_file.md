# maillog_file (default: empty)
 The name of an optional logfile that is written by the Postfix
postlogd(8) service. An empty value selects logging to syslogd(8).
Specify "/dev/stdout" to select logging to standard output. Stdout
logging requires that Postfix is started with "postfix start-fg".



 Note 1: The maillog\_file parameter value must contain a prefix
that is specified with the maillog\_file\_prefixes parameter. 


 Note 2: Some Postfix non-daemon programs may still log information
to syslogd(8), before they have processed their configuration
parameters and command-line options. 


 This feature is available in Postfix 3.4 and later. 



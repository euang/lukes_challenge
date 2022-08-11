# smtpd_proxy_filter (default: empty)
 The hostname and TCP port of the mail filtering proxy server.
The proxy receives all mail from the Postfix SMTP server, and is
supposed to give the result to another Postfix SMTP server process.



 Specify "host:port" or "inet:host:port" for a TCP endpoint, or
"unix:pathname" for a UNIX-domain endpoint. The host can be specified
as an IP address or as a symbolic name; no MX lookups are done.
When no "host" or "host:" is specified, the local machine is
assumed. Pathname interpretation is relative to the Postfix queue
directory. 


 This feature is available in Postfix 2.1 and later. 


 The "inet:" and "unix:" prefixes are available in Postfix 2.3
and later. 



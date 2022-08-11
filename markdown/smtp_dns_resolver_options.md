# smtp_dns_resolver_options (default: empty)
 DNS Resolver options for the Postfix SMTP client. Specify zero
or more of the following options, separated by comma or whitespace.
Option names are case-sensitive. Some options refer to domain names
that are specified in the file /etc/resolv.conf or equivalent. 



**res\_defnames**
 Append the current domain name to single-component names (those
that do not contain a "." character). This can produce incorrect
results, and is the hard-coded behavior prior to Postfix 2.8. 
**res\_dnsrch**
 Search for host names in the current domain and in parent
domains. This can produce incorrect results and is therefore not
recommended. 

 This feature is available in Postfix 2.8 and later. 



# mydestination (default: $myhostname, localhost.$mydomain, localhost)
 The list of domains that are delivered via the $local\_transport
mail delivery transport. By default this is the Postfix local(8)
delivery agent which looks up all recipients in /etc/passwd and
/etc/aliases. The SMTP server validates recipient addresses with
$local\_recipient\_maps and rejects non-existent recipients. See also
the local domain class in the ADDRESS\_CLASS\_README file.




The default mydestination value specifies names for the local
machine only. On a mail domain gateway, you should also include
$mydomain.




The $local\_transport delivery method is also selected for mail
addressed to user@[the.net.work.address] of the mail system (the
IP addresses specified with the inet\_interfaces and proxy\_interfaces
parameters).




Warnings:



* Do not specify the names of virtual domains - those domains
are specified elsewhere. See VIRTUAL\_README for more information.
* Do not specify the names of domains that this machine is
backup MX host for. See STANDARD\_CONFIGURATION\_README for how to
set up backup MX hosts.
* By default, the Postfix SMTP server rejects mail for recipients
not listed with the local\_recipient\_maps parameter. See the
postconf(5) manual for a description of the local\_recipient\_maps
and unknown\_local\_recipient\_reject\_code parameters.



Specify a list of host or domain names, "/file/name" or "type:table"
patterns, separated by commas and/or whitespace. A "/file/name"
pattern is replaced by its contents; a "type:table" lookup table
is matched when a name matches a lookup key (the lookup result is
ignored). Continue long lines by starting the next line with
whitespace. 



Examples:




```

mydestination = $myhostname, localhost.$mydomain $mydomain
mydestination = $myhostname, localhost.$mydomain www.$mydomain, ftp.$mydomain

```


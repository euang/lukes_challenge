# smtp_bind_address (default: empty)

An optional numerical network address that the Postfix SMTP client
should bind to when making an IPv4 connection.




This can be specified in the main.cf file for all SMTP clients, or
it can be specified in the master.cf file for a specific client,
for example:




> 
> 
> ```
> 
> /etc/postfix/master.cf:
>     smtp ... smtp -o smtp\_bind\_address=11.22.33.44
> 
> ```
> 
> 


 See smtp\_bind\_address\_enforce for how Postfix should handle
errors (Postfix 3.7 and later). 


 Note 1: when inet\_interfaces specifies no more than one IPv4
address, and that address is a non-loopback address, it is
automatically used as the smtp\_bind\_address. This supports virtual
IP hosting, but can be a problem on multi-homed firewalls. See the
inet\_interfaces documentation for more detail. 


 Note 2: address information may be enclosed inside [],
but this form is not required here. 


